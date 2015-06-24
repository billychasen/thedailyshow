import fnmatch
import os
import shutil

class Iterator:
    def iterate_copy(self, base_dir, save_dir, files_per_episode = 2):
        directories = []
        for root, dirnames, filenames in os.walk(base_dir):
            try:
                s = root.split("/")
                int(s[-2])
                int(s[-1])
                directories.append({"root": root, "filenames": filenames})
            except:
                pass

        sorted_dir = sorted(directories, cmp=self.compare)
        for d in sorted_dir:
            x = 0
            for filename in fnmatch.filter(d["filenames"], '*.jpg'):
                if x >= files_per_episode:
                    break
                s = d["root"].split("/")
                season = s[-2]
                episode = s[-1]
                shutil.copy(os.path.join(d["root"], filename), os.path.join(save_dir, "%s_%s_%s.jpg" % (season, episode, x)))
                x += 1

    def iterate(self, base_dir):
        files = []
        for f in os.listdir(base_dir):
            if f.endswith(".jpg"):
                files.append(os.path.join(base_dir, f))
        return sorted(files, cmp=self.compare_files)

    def compare_files(self, x, y):
        parts1 = x.split("/")[-1].replace(".jpg", "").split("_")
        season1 = int(parts1[0])
        episode1 = int(parts1[1])

        parts2 = y.split("/")[-1].replace(".jpg", "").split("_")
        season2 = int(parts2[0])
        episode2 = int(parts2[1])

        if season1 == season2:
            return episode1 - episode2
        return season1 - season2

    def compare(self, x, y):
        xsplit = x["root"].split("/")
        ysplit = y["root"].split("/")

        first_dir1 = int(xsplit[-2])
        first_dir2 = int(ysplit[-2])
        sec_dir1 = int(xsplit[-1])
        sec_dir2 = int(ysplit[-1])

        if first_dir1 == first_dir2:
            return sec_dir1 - sec_dir2
        return first_dir1 - first_dir2
