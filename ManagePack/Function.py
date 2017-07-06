import maya.cmds as mc
import os
import re
import getpass
import datetime
import math
class Function(object):
    def __init__(self):
        self.userP ="C:/users/"+getpass.getuser()+"/Documents/yggintern/"
        self.workN=""
        self.proJ=""        
        self.typeW=""
        self.shotN=""
        self.depart=""
        self.patt=[]
        self.pattBl=[]
        self.pattPol=[]
        self.blockVer=0
        self.polVer=0
        self.Version=0
        self.anim =""
        self.curFile =""
        self.listFile=""
        self.savepath1=""
        self.savepath2=""
        self.savepath3=""
        self.DisDate=""
        self.DisSizeB=""
        self.DisSizeN=""
        self.listPath=""
    def openS1(self):
        self.listA = self.userP
        self.proJ = os.listdir("%s"%(self.userP))
        print self.proJ
        print self.listA  
        
    def openS2(self,W):
        self.listWork = self.listA + self.proJ[W-1]+"/"
        self.typeW = os.listdir("%s"%(self.listWork))
        print self.typeW
        print self.listWork  
    def openS3(self,SqA):
        self.listType = self.listWork + self.typeW[SqA-1]+"/"
        self.workN = os.listdir("%s"%(self.listType))
        print self.workN
        print self.listType
    def openS4(self,Part):
        self.listPart = self.listType + self.workN[Part-1]+"/"
        self.shotN = os.listdir("%s"%(self.listPart))
        print self.shotN
        print self.listPart
    def openS5(self,shotnum):
        self.listShotnum = self.listPart + self.shotN[shotnum-1]+"/"
        self.depart = os.listdir("%s"%(self.listShotnum))
        print self.depart
        print self.listShotnum
    def openS6(self,dePart):
        self.listFile = os.listdir("%s%s/scenes/"%(self.listShotnum,self.depart[dePart-1]))
        self.anim = self.depart[dePart-1]    
        print self.listFile
        self.listPath = "%s%s/scenes/"%(self.listShotnum,self.depart[dePart-1])
        print self.listPath
    def openSc(self,num):
        self.curFile = self.listFile[num-1]
        mc.file("%s%s"%(self.listPath,self.listFile[num-1]),open=True)    
    def saveCrr(self):
        self.listFile = os.listdir("%s"%(self.listPath))
        print self.listFile
        if self.listFile != []:
            for x in range(len(self.listFile)):
                self.patt += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[master]*[.]+[v]",self.listFile[x])
                self.patt += re.findall("[a-z]*[_]+[a-z]*[_]+[a-z]*[.]+[v]",self.listFile[x])
                self.pattBl += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[block]*[.]+[v]",self.listFile[x])
                self.pattPol += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[polish]*[.]+[v]",self.listFile[x])
            self.blockVer = "%03d"%(len(self.pattBl)+1)
            self.polVer = "%03d"%(len(self.pattPol)+1)
            self.Version = "%03d"%(len(self.patt)+1)
            if self.anim == "Animation":
                numType = input("block/polish : 1/2\n")
                if numType == 1:
                     mc.file(rename="%s%s%s" %(self.listPath,self.pattBl[0],self.blockVer))
                     mc.file(save=True,type="mayaAscii")
                     saveCurPath = "%s%s%s" %(self.listPath,self.pattBl[0],self.blockVer)
                     self.curFile = "%s%s.ma"%(self.pattBl[0],self.blockVer)
                     print saveCurPath
                     print self.curFile
                elif numType == 2:
                     mc.file(rename="%s%s%s" %(self.listPath,self.pattPol[0],self.polVer))
                     mc.file(save=True,type="mayaAscii")
                     saveCurPath = "%s%s%s" %(self.listPath,self.pattPol[0],self.polVer)
                     self.curFile = "%s%s.ma"%(self.pattPol[0],self.polVer)
                     print saveCurPath         
                     print self.curFile  
            elif len(self.patt) != 0:
                 mc.file(rename="%s%s%s"%(self.listPath,self.patt[0],self.Version))
                 mc.file(save=True,type="mayaAscii")
                 saveCurPath = "%s%s%s" %(self.listPath,self.patt[0],self.Version)
                 self.curFile = "%s%s.ma"%(self.patt[0],self.Version)
                 print saveCurPath
                 print self.curFile
                 self.patt =[]
        else:
            print "error"             
    def saveA1(self):
        self.listA = self.userP
        self.proJ = os.listdir("%s"%(self.userP))
        print self.proJ
        print self.listA  
    def saveA2(self,W):
        self.listWork = self.listA + self.proJ[W-1]+"/"
        self.typeW = os.listdir("%s"%(self.listWork))
        print self.typeW
        print self.listWork  
    def saveA3(self,SqA):
        self.listType = self.listWork + self.typeW[SqA-1]+"/"
        self.workN = os.listdir("%s"%(self.listType))
        print self.workN
        print self.listType
    def saveA4(self,Part):
        self.listPart = self.listType + self.workN[Part-1]+"/"
        self.shotN = os.listdir("%s"%(self.listPart))
        print self.shotN
        print self.listPart
    def saveA5(self,shotnum):
        self.listShotnum = self.listPart + self.shotN[shotnum-1]+"/"
        self.depart = os.listdir("%s"%(self.listShotnum))
        self.savepath1 = self.shotN[shotnum-1]
        print self.depart
        print self.listShotnum
    def saveA6(self,dePart):
        self.listFile = os.listdir("%s%s/scenes/"%(self.listShotnum,self.depart[dePart-1]))   
        self.listPath = "%s%s/scenes/"%(self.listShotnum,self.depart[dePart-1])
        self.savepath2 = self.depart[dePart-1]
        print self.listFile
        print self.listPath
    def saveAsFile (self):
        print self.savepath1
        print self.savepath2        
        for x in range(len(self.listFile)):
            self.patt += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[master]*[.]+[v]",self.listFile[x])
            self.pattBl += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[block]*[.]+[v]",self.listFile[x])
            self.pattPol += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[polish]*[.]+[v]",self.listFile[x])
        self.blockVer = "%03d"%(len(self.pattBl)+1)
        self.polVer = "%03d"%(len(self.pattPol)+1)
        self.Version = "%03d"%(len(self.patt)+1)
        if self.savepath2 == "Animation":
            self.anim = input("block/polish : 1/2\n")
            if self.anim == 1:
                self.savepath3 = "block" 
                print "%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.blockVer)
                mc.file(rename="%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.blockVer))
                mc.file(save=True,type="mayaAscii")  
                self.curFile = "%s_%s_%s.v%s.ma"%(self.savepath1,self.savepath2,self.savepath3,self.blockVer)
            elif self.anim == 2:
                self.savepath3 = "polish"
                print "%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.polVer) 
                mc.file(rename="%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.polVer))
                mc.file(save=True,type="mayaAscii")
                self.curFile = "%s_%s_%s.v%s.ma"%(self.savepath1,self.savepath2,self.savepath3,self.polVer)    
        elif self.savepath2 == "model":
            self.savepath3 = "model"
            print "%schar_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath3,self.Version)
            mc.file(rename="%schar_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath3,self.Version))
            mc.file(save=True,type="mayaAscii")
            self.curFile = "char_%s_%s.v%s.ma"%(self.savepath1,self.savepath3,self.Version)

        elif self.savepath2 == "rig":
            self.savepath3 = "rig"
            print "%schar_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath3,self.Version)
            mc.file(rename="%schar_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath3,self.Version))
            mc.file(save=True,type="mayaAscii")
            self.curFile = "char_%s_%s.v%s.ma"%(self.savepath1,self.savepath3,self.Version)
        else:
            self.savepath3 = "master"        
            print "%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.Version)
            mc.file(rename="%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.Version))
            mc.file(save=True,type="mayaAscii")
            self.curFile = "%s_%s_%s.v%s.ma"%(self.savepath1,self.savepath2,self.savepath3,self.Version)    
    def modification_date(self,filename):
        t = os.path.getmtime(filename)
        date_time = datetime.datetime.fromtimestamp(t)
        tmp = str(date_time).split('.')
        self.DisDate = tmp[0]
    def getSize(self,filename):
        st = os.stat(filename)
        self.DisSizeB = st.st_size
    def convertSize(self,size_bytes):
       if size_bytes == 0:
           return "0B"
       size_name = ("B", "KB", "MB", "GB")
       i = int(math.floor(math.log(size_bytes, 1024)))
       p = math.pow(1024, i)
       s = round(size_bytes / p, 2)
       self.DisSizeN = "%s %s" % (s, size_name[i])
    def runOpen(self):
        self.openS1()
        in1 = input()
        self.openS2(in1)
        in2 = input()
        self.openS3(in2)
        in3 = input()
        self.openS4(in3)
        in4 = input()
        self.openS5(in4)
        in5 = input()
        self.openS6(in5)
        in6 = input()
        self.openSc(in6)
    def runSaveCur(self):
        self.saveCrr()
        
    def runSaveAs(self):
        self.saveA1()
        A2input = input()
        self.saveA2(A2input)
        A3input = input()
        self.saveA3(A3input)
        A4input = input()
        self.saveA4(A4input)
        A5input = input()
        self.saveA5(A5input)
        A6input = input()
        self.saveA6(A6input)
        self.saveAsFile()
    def cal(self):
       self.modification_date("%s%s"%(self.listPath,self.curFile))
       self.getSize("%s%s"%(self.listPath,self.curFile))
       self.convertSize(self.DisSizeB)
       print self.curFile
       print self.DisDate
       print self.DisSizeN
    def CWD(self):
       print mc.file("%s%s"%(self.listPath,self.curFile),q=True,loc=True)