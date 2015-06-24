
import md5 as md5lib

def md5(str):
    m = md5lib.new()
    m.update(str)
    return m.hexdigest()
