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
reload (mp)

aa = mp.Function()
class Gui(object):
    def __init__(self):
        self.window = "windowNN";
        self.title = "File Manager";
    def delUI(self):
        mc.deleteUI('%s'%(self.window))
    def comLayout(self):
        if mc.window('%s'%(self.window),ex=True):
            mc.deleteUI('%s'%(self.window))
        mc.window('%s'%(self.window),t='%s'%(self.title))
        self.mainPane = mc.paneLayout('MainPane',cn="horizontal3",ps=[(1,50,5)])
        mc.columnLayout("column1",adj=True)
        mc.text("txt1",l="File Manager")
        self.midPane = mc.paneLayout("midpane",cn='vertical2',p=self.mainPane)
        self.tabs = mc.tabLayout('tab1')
        self.channel1 = mc.columnLayout('channel1')
        
        mc.columnLayout(self.channel1,p=self.channel1)
        mc.text('')
        mc.rowColumnLayout('row1_0',nc=3,p=self.channel1,cw=[(1,100),(2,10),(3,100)])
        mc.text('Proj',l ='Project')
        mc.text(l='                ')
        aa.openS1()
        mc.optionMenu('ProBox',cc=aa.openS2)
        for x in aa.proJ :
            mc.menuItem('ProBox_%s'%(x),l=x,p='ProBox')       
        
        mc.rowColumnLayout('row1_1',nc=3,p=self.channel1,cw=[(1,100),(2,10),(3,100)])
        mc.text('cate',l ='Categories')
        mc.text(l='         ')
        mc.optionMenu('CateBox',cc=aa.openS3)
        
        mc.rowColumnLayout('row1_2',nc=3,p=self.channel1,cw=[(1,100),(2,10),(3,100)])
        mc.text('subCate',l ='Sub Categories')
        mc.text(l='     ')
        mc.optionMenu('SubBox',cc=aa.openS4)

        mc.rowColumnLayout('row1_3',nc=3,p=self.channel1,cw=[(1,100),(2,10),(3,100)])
        mc.text('shots',l ='shot')
        mc.text(l='')
        mc.optionMenu('ShotBox',cc=aa.openS5)

        mc.rowColumnLayout('row1_4',nc=3,p=self.channel1,cw=[(1,100),(2,10),(3,100)])
        mc.text('dePart',l ='Department')
        mc.text(l='')
        mc.optionMenu('DepBox',cc=aa.openS6)
        
        mc.rowColumnLayout('row1_5',nc=3,p=self.channel1,cw=[(1,100),(2,10),(3,100)])
        mc.text(l='')
        mc.text(l='')
        
        self.channel2 = mc.columnLayout('channel2',p=self.tabs)
        mc.rowColumnLayout('row2_M',nc=3,p=self.channel2,cw=[(1,100),(2,10),(3,100)])
        mc.text(l='')
        mc.text(l='')
        
        mc.rowColumnLayout('row2_0',nc=3,p=self.channel2,cw=[(1,100),(2,10),(3,100)])
        mc.text('Proj',l ='Project')
        mc.text(l='                ')
        mc.optionMenu('S_ProBox')
        mc.menuItem('S_ProBox0',l='')
        mc.menuItem('S_ProBox1',l='1')
        mc.menuItem('S_ProBox2',l='2')
        
        
        mc.rowColumnLayout('row2_1',nc=3,p=self.channel2,cw=[(1,100),(2,10),(3,100)])
        mc.text('cate',l ='Categories')
        mc.text(l='         ')
        mc.optionMenu('S_CateBox')
        mc.menuItem('S_CateBox0',l='')
        mc.menuItem('S_CateBox1',l='1')
        mc.menuItem('S_CateBox2',l='2')
        
        mc.rowColumnLayout('row2_2',nc=3,p=self.channel2,cw=[(1,100),(2,10),(3,100)])
        mc.text('subCate',l ='Sub Categories')
        mc.text(l='     ')
        mc.optionMenu('S_SubBox')
        mc.menuItem('S_SubBox0',l='')
        mc.menuItem('S_SubBox1',l='1')
        mc.menuItem('S_SubBox2',l='2')
        
        mc.rowColumnLayout('row2_3',nc=3,p=self.channel2,cw=[(1,100),(2,10),(3,100)])
        mc.text('shots',l ='shot')
        mc.text(l='')
        mc.optionMenu('S_ShotBox')
        mc.menuItem('S_ShotBox0',l='')
        mc.menuItem('S_ShotBox1',l='1')
        mc.menuItem('S_ShotBox2',l='2')
        
        mc.rowColumnLayout('row2_4',nc=3,p=self.channel2,cw=[(1,100),(2,10),(3,100)])
        mc.text('dePart',l ='Department')
        mc.text(l='')
        mc.optionMenu('S_DepBox')
        mc.menuItem('S_DepBox0',l='')
        mc.menuItem('S_DepBox1',l='1')
        mc.menuItem('S_DepBox2',l='2')
        
        mc.rowColumnLayout('row2_5',nc=3,p=self.channel2,cw=[(1,100),(2,10),(3,100)])
        mc.text(l='Type Animation')
        mc.separator(st='none')
        mc.optionMenu('S_TpeBox')
        mc.menuItem('S_TpeBox0',l='')
        mc.menuItem('S_TpeBox1',l='1')
        mc.menuItem('S_TpeBox2',l='2')
        mc.tabLayout(self.tabs, edit=True,tabLabel=((self.channel1, 'Open'),(self.channel2, 'Save')),p=self.midPane )
        
        self.rightPane = mc.paneLayout('rightPane',cn='horizontal2',p=self.midPane)
        mc.textScrollList('list',p=self.rightPane)
        mc.textScrollList('data',p=self.rightPane)
        self.botPane = mc.paneLayout('bottompane',cn='vertical2',p=self.mainPane)
        self.botcolumn = mc.columnLayout(adj=True,p=self.botPane)
        mc.rowColumnLayout('botRow0',nc=2,p=self.botcolumn,cw=[(1,150),(2,100),(3,10)])
        mc.separator(st='none')
        mc.rowColumnLayout('botRow1',nc=2,p=self.botcolumn,cw=[(1,90),(2,380),(3,10)])
        mc.text(l="Show Path")
        mc.textField('Path',tx='%s'%(aa.listA))
        mc.separator(st='none')
        mc.rowColumnLayout('botRow2',nc=2,p=self.botcolumn,cw=[(1,120),(2,350),(3,10)])
        mc.text(l="Current Working Path")
        mc.textField(tx='aa')
        mc.columnLayout('botRow3',p=self.botPane)
        mc.button('runOpen',l='Open',w=150)
        mc.text(l='')
        mc.button('runsave',l='Save NewVersion',w=150)
        mc.text(l='')
        mc.button('runsaveAs',l='Save As',w=150)
        mc.text(l='')
        mc.button(l='Close',w=150)
        mc.showWindow(self.window)
x = Gui()
x.comLayout()
x.rightPane
#x.delUI()
print aa.typeW
