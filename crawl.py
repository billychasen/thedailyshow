
import requests
import os
import sys

# it's like you can almost see the different people that worked on this by how they
# each decided to format their URLs.
formats = [
#    "http://3.images.comedycentral.com/images/shows/tds/videos/batch6/ds_%s%s_%s_nws_v6.jpg",
#    "http://1.images.comedycentral.com/images/shows/tds/videos/batch7/ds_%s%s_%s_nws_v6.jpg",
#    "http://1.images.comedycentral.com/images/shows/tds/videos/batch11/ds_%s%s_%s_stw_v6.jpg",
#    "http://2.images.comedycentral.com/images/shows/tds/videos/batch10/ds_%s%s_%s_nws_v6.jpg",
#    "http://3.images.comedycentral.com/images/shows/tds/videos/batch8/ds_%s%s_%s_rco_v6.jpg",
#    "http://1.images.comedycentral.com/images/shows/tds/videos/batch8/ds_%s%s_%s_nws_v6.jpg",
#    "http://1.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/tds_%s%s_%s_stw_v6.jpg",
#    "http://2.images.comedycentral.com/images/shows/tds/videos/batch9/ds_%s%s_%s_nws_v6.jpg",

#    "http://1.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_%s_stw_v6.jpg",
#    "http://1.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_%s_nws_v6.jpg",
#    "http://3.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_%s_olv_v6.jpg",
#    "http://3.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_%s_col_v6.jpg",
#    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_%s_stw_rev_v6.jpg",
#    "http://3.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_%s_v6.jpg",
#    "http://2.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_%s_msc_v6.jpg",

#    "http://3.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%sA/ds_%s%sA_%s_stw_v6.jpg",
#    "http://1.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%sB/ds_%s%sB_%s_stw_v6.jpg",
#---
#    "http://1.images.comedycentral.com/images/shows/tds/videos/season_%s_v/batch3/tds_%s%s_headline_%s_v6.jpg",
#    "http://3.images.comedycentral.com/images/shows/tds/videos/headlines/tds_%s%s_headline_%s_v6.jpg",
#    "http://2.images.comedycentral.com/images/shows/tds/videos/headlines/tds_%s%s_%s_hdl_v6.jpg",
#     "http://2.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_%s_nws_v6.jpg",
#     "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_a_%s_nws_v6.jpg",
#    "http://1.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/tds_%s%s_%s_nws_v6.jpg",
#    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/ds_%s%s_a_%s_nws-copy_v6.jpg",
#    "http://1.images.comedycentral.com/images/shows/tds/videos/season_%s/episode_%s/tds_%s%s_b_%s_nws_v6.jpg",
#     "http://1.images.comedycentral.com/images/shows/tds/videos/season_%s_v/batch2/tds_%s%s_headline_%s_cor_v6.jpg",
#     "http://3.images.comedycentral.com/images/shows/tds/videos/season_%s_v/batch3/tds_%s%s_headline_%s_v6.jpg",
#    "http://2.images.comedycentral.com/images/shows/tds/videos/season_%s_v/batch3/tds_%s%s_headline_%s_v6.jpg",
#    "http://2.images.comedycentral.com/images/shows/tds/videos/season_%s/Season_12_screengrabs/ds_%s%s_headline_%s_v6.jpg",
#    "http://3.images.comedycentral.com/images/shows/tds/videos/season_%s_v/batch3/tds_headline_%s%s_%s_v6.jpg",
#    "http://3.images.comedycentral.com/images/shows/tds/videos/season_%s_v/batch3/tds_%s%s_headline_%s_v6.jpg",
#    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/%s%s/v1-v9/tds_%s%s_%s_v6.jpg",
#    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/%s%s/v1-v9/ds_%s%s_%s_v6.jpg",
#    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/%s%s/ds_%s%s_%s_v6.jpg",
#    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/%s%s/tds_%s%s_%s_v6.jpg",
#    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/%s%s/ds_%s%s_%s_1920x1080.jpg",
#    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/%s%s/ds_%s%s_%s_16x9.jpg",
    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/%s%s/ds_%s_%s_%s.jpg",
    "http://4.images.comedycentral.com/images/shows/tds/videos/season_%s/%s%s/ds_%s%s_%s.jpg",
]

save_dir = "/Volumes/chillydisk/dailyshow"

def request_url(url):
    r = requests.get(url)
    if "cc_missing" in r.url:
        return False
    else:
        return r

def crawl_episode(season, num, screenshot):
    season = '%02d' % season
    num = '%03d' % num
    screenshot = '%02d' % screenshot

    for format in formats:
        #url = format % (season, season, num, season, num, screenshot)
        '''
        if screenshot == "01":
            screenshot = "a"
        elif screenshot == "02":
            screenshot = "b"
        else:
            return False
        '''
        dimensions = "?quality=1&width=1280&height=720&crop=true"

        if "batch" in format:
            url = format % (season, num, screenshot) + dimensions
        else:
            url = format % (season, season, num, season, num, screenshot) + dimensions
        r = request_url(url)
        if r:
            print "success with " + url
            break

    if r:
        return r.content
    return False

def save_file(season, num, data, filename):
    sd = "%s/%s" % (save_dir, season)
    if not os.path.exists(sd):
        os.makedirs(sd)
    
    sd += "/%s" % num
    if not os.path.exists(sd):
        os.makedirs(sd)

    sd += "/" + filename
    with open(sd, "w") as f:
        f.write(data)

def save_episode(season, num):
    got_some = False
    for screenshot in range(1, 7):
        data = crawl_episode(season, num, screenshot)
        if data:
            save_file(season, num, data, "/%s_%s.jpg" % (num, screenshot))
            got_some = True
        
    if not got_some:
        print "no screenshots for %s %s" % (season, num)

def get_metadata(season, num):
    r = requests.get("http://www.omdbapi.com/?t=Daily Show&Season=%s&Episode=%s" % (season, num))
    js = r.json()
    if not js["Response"]:
        return False
    else:
        return str(js)

if len(sys.argv) == 3:
    save_episode(int(sys.argv[1]), int(sys.argv[2]))
else:
    for i in range(1, 200):
        save_episode(2, i)

#save_file(20, 43, get_metadata(20, 114), "data.json")

