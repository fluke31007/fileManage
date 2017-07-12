import maya.cmds as mc
import os
import re
import getpass
import datetime
import math
class Function(object):
    def __init__(self):
        self.userP ="C:/Users/"+getpass.getuser()+"/Documents/yggintern/"
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
        self.saveType =""
        self.openInput = ""
        self.CateBox=[]
        self.SubBox=[]
        self.ShotBox=[]
        self.DepBox=[]
        self.S_CateBox=[]
        self.S_SubBox=[]
        self.S_ShotBox=[]
        self.S_DepBox=[]
    def openS1(self):
        
        self.listA = self.userP
        self.proJ = os.listdir("%s"%(self.userP))

    def openS2(self,W):
        self.listWork = self.listA+W+"/"
        if self.CateBox != [] :
            for num in self.CateBox:
                mc.deleteUI('CateBox_%s'%(num),menuItem=True)
            self.CateBox=[]
        if self.SubBox != []:
            for num in self.SubBox :
                mc.deleteUI('SubBox_%s'%(num),menuItem=True)
                self.SubBox=[]
        if self.ShotBox != []:
            for num in self.ShotBox :
                mc.deleteUI('ShotBox_%s'%(num),menuItem=True)
                self.ShotBox=[]
        if self.DepBox !=[]:
            for num in self.DepBox :
                mc.deleteUI('DepBox_%s'%(num),menuItem=True)
                self.DepBox =[]
        self.typeW = os.listdir("%s"%(self.listWork))
        print self.typeW
        print self.listWork
        # sq/asset
        for num in self.typeW : 
            mc.menuItem('CateBox_%s'%(num),l=num,p='CateBox')
            self.CateBox.append(num)

        mc.optionMenu('CateBox',e=True,select=1)
        mc.optionMenu('ProBox',e=True)
        mc.textField('Path',e=True,tx='%s'%(self.listWork))
    def openS3(self,SqA):
        self.listType = self.listWork+SqA+"/"
        
        if self.SubBox != []:
            for num in self.SubBox :
                mc.deleteUI('SubBox_%s'%(num),menuItem=True)
                self.SubBox=[]
        if self.ShotBox != []:
            for num in self.ShotBox :
                mc.deleteUI('ShotBox_%s'%(num),menuItem=True)
                self.ShotBox=[]
        if self.DepBox !=[]:
            for num in self.DepBox :
                mc.deleteUI('DepBox_%s'%(num),menuItem=True)
                self.DepBox =[]
        self.workN = os.listdir("%s"%(self.listType))
        print self.workN
        print self.listType
        # y01-02 or char rig
        for num in self.workN :
            mc.menuItem('SubBox_%s'%(num),l=num,p='SubBox') 
            self.SubBox.append(num)
        mc.textField('Path',e=True,tx='%s'%(self.listType))
  
    def openS4(self,Part):
        self.listPart = self.listType+Part+"/"
        
        if self.ShotBox != []:
            for num in self.ShotBox :
                mc.deleteUI('ShotBox_%s'%(num),menuItem=True)
                self.ShotBox=[]
        if self.DepBox !=[]:
            for num in self.DepBox :
                mc.deleteUI('DepBox_%s'%(num),menuItem=True)
                self.DepBox =[]
        self.shotN = os.listdir("%s"%(self.listPart))
        print self.shotN
        print self.listPart
        # shot num or charracter
        for num in self.shotN :
            mc.menuItem('ShotBox_%s'%(num),l=num,p='ShotBox') 
            self.ShotBox.append(num)
        mc.textField('Path',e=True,tx='%s'%(self.listPart))

    def openS5(self,shotnum):
        self.listShotnum = self.listPart+shotnum+"/"
        
        if self.DepBox !=[]:
            for num in self.DepBox :
                mc.deleteUI('DepBox_%s'%(num),menuItem=True)
                self.DepBox =[]
        self.depart = os.listdir("%s"%(self.listShotnum))
        print self.depart  
        print self.listShotnum
        # department
        for num in self.depart :
            mc.menuItem('DepBox_%s'%(num),l=num,p='DepBox') 
            self.DepBox.append(num)
        mc.textField('Path',e=True,tx='%s'%(self.listShotnum))
        
    def openS6(self,dePart):
        self.listFile = os.listdir("%s%s/scenes/"%(self.listShotnum,dePart))
        self.anim = dePart
        print self.listFile
        self.listPath = "%s%s/scenes/"%(self.listShotnum,dePart)
        print self.listPath
        mc.textScrollList('list',e=True,ra=True)
        for d in self.listFile:
            mc.textScrollList('list',e=True,a=d,sc=self.ShowPath) 
            
    def ShowPath(self,*arg):
        self.openInput = "".join(mc.textScrollList('list',q=True,si=True))
        self.cal()
        mc.textScrollList('data',e=True,ra=True)
        mc.textScrollList('data',e=True,a=self.openInput)
        mc.textScrollList('data',e=True,a=self.DisSizeN)
        mc.textScrollList('data',e=True,a=self.DisDate)
    def openSc(self,*arg):
        mc.file("%s%s"%(self.listPath,self.openInput),open=True)
        self.curFile = "%s%s"%(self.listPath,self.openInput)
        mc.textField('cw',e=True,tx=self.curFile)
        if re.search('master',self.openInput):
            self.saveType= 'master'
            print self.saveType
        elif re.search('block',self.openInput):
            self.saveType = 'block'
            print self.saveType
        elif re.search('polish',self.openInput):
            self.saveType = 'polish'    
            print self.saveType    
        self.resetPath()
    def saveCrr(self,*arg):
        if self.listFile != "":
            self.listFile = os.listdir("%s"%(self.listPath))
            print self.listFile
            self.patt =[]
            self.pattBl=[]
            self.pattPol=[]  
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
                    
                    if self.saveType == 'block':
                         mc.file(rename="%s%s%s" %(self.listPath,self.pattBl[0],self.blockVer))
                         mc.file(save=True,type="mayaAscii")
                         saveCurPath = "%s%s%s" %(self.listPath,self.pattBl[0],self.blockVer)
                         self.curFile = "%s%s.ma"%(self.pattBl[0],self.blockVer)
                         print saveCurPath
                         print self.curFile
                    elif self.saveType == 'polish':
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
            mc.textField('cw',e=True,tx='%s%s'%(self.listPath,self.curFile)) 
        elif self.listFile == "":
            mc.window('showlog')
            mc.columnLayout('Mlay')
            mc.text(l='Open File First')
            mc.showWindow('showlog')          
        self.listFile = os.listdir(self.listPath)
        mc.textScrollList('list',e=True,ra=True)
        for d in self.listFile:
            mc.textScrollList('list',e=True,a=d,sc=self.ShowPath)
    def saveA1(self):
        
        self.proJ = os.listdir("%s"%(self.userP))
        self.listA = self.userP
        
    def saveA2(self,W):
        self.listFile=""
        if self.S_CateBox !=[]:
            for x in self.S_CateBox:
                mc.deleteUI('S_CateBox_%s'%(x),menuItem=True)
                self.S_CateBox=[]
        if self.S_SubBox != []:
            for x in self.S_SubBox:
                mc.deleteUI('S_SubBox_%s'%(x),menuItem=True)
                self.S_SubBox=[]
        if self.S_ShotBox != []:
            for x in self.S_ShotBox:
                mc.deleteUI('S_ShotBox_%s'%(x),menuItem=True)
                self.S_ShotBox=[]
        if self.S_DepBox != []:
            for x in self.S_DepBox:
                mc.deleteUI('S_DepBox_%s'%(x),menuItem=True)
                self.S_DepBox=[]
        self.listWork = self.listA +W+"/"
        self.typeW = os.listdir("%s"%(self.listWork))
        for x in self.typeW:
            mc.menuItem('S_CateBox_%s'%(x),l=x,p='S_CateBox')
            self.S_CateBox.append(x)
        print self.typeW
        print self.listWork  
        mc.textField('Path',e=True,tx='%s'%(self.listWork))
        mc.textScrollList('list',e=True,ra=True)
    def saveA3(self,SqA):
        if self.S_SubBox != []:
            for x in self.S_SubBox:
                mc.deleteUI('S_SubBox_%s'%(x),menuItem=True)
                self.S_SubBox=[]
        if self.S_ShotBox != []:
            for x in self.S_ShotBox:
                mc.deleteUI('S_ShotBox_%s'%(x),menuItem=True)
                self.S_ShotBox=[]
        if self.S_DepBox != []:
            for x in self.S_DepBox:
                mc.deleteUI('S_DepBox_%s'%(x),menuItem=True)
                self.S_DepBox=[]
        self.listType = self.listWork +SqA+"/"
        self.workN = os.listdir("%s"%(self.listType))
        for x in self.workN:
            mc.menuItem('S_SubBox_%s'%(x),l=x,p='S_SubBox')
            self.S_SubBox.append(x)
        print self.workN
        print self.listType
        mc.textField('Path',e=True,tx='%s'%(self.listType))
    def saveA4(self,Part):
        if self.S_ShotBox != []:
            for x in self.S_ShotBox:
                mc.deleteUI('S_ShotBox_%s'%(x),menuItem=True)
                self.S_ShotBox=[]
        if self.S_DepBox != []:
            for x in self.S_DepBox:
                mc.deleteUI('S_DepBox_%s'%(x),menuItem=True)
                self.S_DepBox=[]
        self.listPart = self.listType +Part+"/"
        self.shotN = os.listdir("%s"%(self.listPart))
        for x in self.shotN:
            mc.menuItem('S_ShotBox_%s'%(x),l=x,p='S_ShotBox')
            self.S_ShotBox.append(x)
        print self.shotN
        print self.listPart
        mc.textField('Path',e=True,tx='%s'%(self.listPart))
    def saveA5(self,shotnum):
        if self.S_DepBox != []:
            for x in self.S_DepBox:
                mc.deleteUI('S_DepBox_%s'%(x),menuItem=True)
                self.S_DepBox=[]
        self.listShotnum = self.listPart +shotnum+"/"
        self.depart = os.listdir("%s"%(self.listShotnum))
        self.savepath1 = shotnum
        for x in self.depart:
            mc.menuItem('S_DepBox_%s'%(x),l=x,p='S_DepBox')
            self.S_DepBox.append(x)
        print self.depart
        print self.listShotnum
        mc.textField('Path',e=True,tx='%s'%(self.listShotnum))
    def saveA6(self,dePart):
        self.listFile = os.listdir("%s%s/scenes/"%(self.listShotnum,dePart))   
        self.listPath = "%s%s/scenes/"%(self.listShotnum,dePart)
        print self.listFile
        print self.listPath
        self.savepath2 = dePart
        mc.textScrollList('list',e=True,ra=True)
        for d in self.listFile:
            mc.textScrollList('list',e=True,a=d,sc=self.ShowPath) 
        mc.textField('Path',e=True,tx='%s'%(self.listPath))
        print self.savepath2
    def saveA7(self,task):
        self.saveType = task
        if self.savepath2 == 'Animation' and self.saveType == 'master':
            mc.window('error_log',t = 'not correct type',wh=(10,10))
            mc.columnLayout('errLog',adj=True)
            mc.text(l='not correct type pls use block or polish')
            mc.showWindow('error_log')
            
    def saveAsFile (self,*arg):
        print self.savepath1
        print self.savepath2 
        print self.savepath3    
        print self.saveType 
        self.patt =[]
        self.pattBl=[]
        self.pattPol=[]  
        if self.listFile != "":
            for x in range(len(self.listFile)):
                self.patt += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[master]*[.]+[v]",self.listFile[x])
                self.pattBl += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[block]*[.]+[v]",self.listFile[x])
                self.pattPol += re.findall("[A-Z]+[0-9]*[_]+[0-9]*[_]+[A-Za-z]*[_]+[polish]*[.]+[v]",self.listFile[x])
                self.patt += re.findall("[a-z]*[_]+[norman]+[_]+[a-z]*[.]+[v]",self.listFile[x])
                print self.patt
            self.blockVer = "%03d"%(len(self.pattBl)+1)
            self.polVer = "%03d"%(len(self.pattPol)+1)
            self.Version = "%03d"%(len(self.patt)+1)
            if self.savepath2 == "Animation":
                if self.saveType == 'block':
                    self.savepath3 = "block" 
                    print "%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.blockVer)
                    mc.file(rename="%s%s_%s_%s.v%s"%(self.listPath,self.savepath1,self.savepath2,self.savepath3,self.blockVer))
                    mc.file(save=True,type="mayaAscii")  
                    self.curFile = "%s_%s_%s.v%s.ma"%(self.savepath1,self.savepath2,self.savepath3,self.blockVer)
                elif self.saveType == 'polish':
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
            mc.textField('cw',e=True,tx='%s%s'%(self.listPath,self.curFile))
            mc.textField('Path',e=True,tx='%s'%(self.listPath))
            self.listFile = os.listdir("%s%s/scenes/"%(self.listShotnum,self.savepath2))
            mc.textScrollList('list',e=True,ra=True)
            for d in self.listFile:
                mc.textScrollList('list',e=True,a=d,sc=self.ShowPath)
            mc.textScrollList('data',e=True,ra=True)
        elif self.listFile == "":
            mc.window('win_log',t='Log',wh=(20,20))
            mc.columnLayout('LogList',adj=True)
            mc.text(l='pls select all path')
            mc.showWindow('win_log')
        self.resetPath()  
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

    def cal(self):
       self.modification_date("%s%s"%(self.listPath,self.openInput))
       self.getSize("%s%s"%(self.listPath,self.openInput))
       self.convertSize(self.DisSizeB)
       print self.DisDate
       print self.DisSizeN
    def resetPath(self):
        self.workN=""      
        self.typeW=""
        self.shotN=""
        self.depart=""