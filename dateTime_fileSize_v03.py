import os
import datetime
import math
def modification_date(filename):
    t = os.path.getmtime(filename)
    date_time = datetime.datetime.fromtimestamp(t)
    tmp = str(date_time).split('.')
    return tmp[0]
def getSize(filename):
    st = os.stat(filename)
    return st.st_size
def convertSize(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
d =modification_date("D:/ygg/Ygg_pipeline/scenes/animScene.ma")
print d
b = getSize("D:/ygg/Ygg_pipeline/scenes/animScene.ma")
print b
c = convertSize(b)
print c
