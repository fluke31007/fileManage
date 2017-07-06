import sys
import getpass
import os
import datetime
import math
import re
import maya.cmds as mc

if not "C:/Users/"+getpass.getuser()+"/Documents/gitfolder/fileManage" in sys.path:
    sys.path.append("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/fileManage")


import ManagePack.Function as mp
reload(mp)
x = mp.Function()
x.runOpen()
x.cal()
x.runSaveCur()
x.runSaveAs()

x.CWD()