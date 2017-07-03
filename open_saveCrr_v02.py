import maya.cmds as mc
import os
import re
class openFile(object):
    def __init__(self):
        self.userP ="C:/users/Admins/Documents/yggintern/"
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
        print self.listFile
        self.listPath = "%s%s/scenes/"%(self.listShotnum,self.depart[dePart-1])
        print self.listPath
    def openSc(self,num):
        mc.file("%s%s"%(self.listPath,self.listFile[num-1]),open=True)    
    def saveCrr(self,numType):
        for x in range(len(self.listFile)):
            self.patt += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[master]*[.]+[v]",self.listFile[x])
            self.pattBl += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[block]*[.]+[v]",self.listFile[x])
            self.pattPol += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[polish]*[.]+[v]",self.listFile[x])
        print len(self.patt)
        print len(self.pattBl)
        print len(self.pattPol)
        self.blockVer = len(self.pattBl)
        self.polVer = len(self.pattPol)
        self.Version = len(self.patt)
        if self.patt == 0:
            if numType == 1:
                 print "%s%s00%s"%(self.listPath,self.pattBl[0],self.blockVer+1)    
            elif numType == 2:
                 print "%s%s00%s"%(self.listPath,self.pattPol[0],self.polVer+1)           
        elif self.patt !=0:
             print "%s%s00%s"%(self.listPath,self.patt[0],self.Version+1)    
        """self.countVer = re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[a-z]*[.]+[v]+[0-9]*","".join(self.listFile))
        self.Version = "%03d"%(len(self.countVer)+1)
        print "%s___%s"%(self.countVer,self.Version)
        mc.file(rename="%s%s%s"%(self.listPath,"".join(self.patt),self.Version))
        mc.file(save=True,type="mayaAscii")"""
        
x =openFile()
x.openS1()
x.openS2(1)
x.openS3(2)
x.openS4(1)
x.openS5(1)
x.openS6(2)
x.saveCrr(1)