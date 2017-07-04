import maya.cmds as mc
import re
import os
import getpass
class saveAs(object):
    def __init__(self):
        #super(saveAs,self).__init__()
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
        self.savepath1=""
        self.savepath2=""
        self.savepath3=""
        
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
            elif self.anim == 2:
                self.savepath3 = "polish"
                print "%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.polVer) 
                mc.file(rename="%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.polVer))
                mc.file(save=True,type="mayaAscii")
        else:
            self.savepath3 = "master"        
            print "%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.Version)
            mc.file(rename="%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.Version))
            mc.file(save=True,type="mayaAscii")
        #mc.file(rename = "%s_%s_%s"%(self.savepath1,self.savepath2,self.savepath3))
        #mc.file(save=True,type="mayaAscii")
#        mc.file(rename="%s%s"%(self.listPath,self.listFile[num-1]),open=True) 
a= saveAs()
a.saveA1()
a.saveA2(1)
a.saveA3(2)
a.saveA4(1)
a.saveA5(1)
a.saveA6(1)
a.saveAsFile()