# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

satpam = LINETCR.LINE() # Koplaxs
satpam.login(token="EmH3a4j9Ws5GDpOmQn1d.7rvSHV/LyctaRlOw94IEBq.WoKYvL8Yx8KIeoWJ1kuEjNOop4V6oMNhsHJhZDcGk3k=")
satpam.loginResult()

cl = LINETCR.LINE() #Luffy
cl.login(token="EmqEUQ1EsqqllSNAeej5.2MEDguZXZnXI+n0eT1GqXq.OO3ZkTKutvYwueh0glm7IpWOuhCiTLVjBAcGJavOGfU=")
cl.loginResult()

ki = LINETCR.LINE() #Zorro
ki.login(token="ElqobeHtTSoa3rQMeRi3.Gb6Qn331R6g2Wz0CsOsN0W.wEJidLuv2IXWEtv6C8OZzocG0OV5O6zb7Sa8Vn67E0w=")
ki.loginResult()

kk = LINETCR.LINE() #Sanji
kk.login(token="ElZageFErf2aai3xiNGe.W4nNn5a7f7Ny+JDgQw0hFG.X+PiQlbD9sNvOk2xmv7Cs3NvuD/O81ohRE/ov38U2pc=")
kk.loginResult()

kc = LINETCR.LINE() #Ussop
kc.login(token="ElVUY1fzfZrX6raoHUL1.znOFgwZ3Bpwf7NyOO3RLaq.ZaCe2K0h1w3iXUXsLAqGfxkqJpTyvnPyMGv4nnHShcY=")
kc.loginResult()

ks = LINETCR.LINE() #Chooper
ks.login(token="Elwj51B8Iua0euPovTJc.jf+XttKo1MOAZLcxBzIH+a.6Qm3oeFbfR9rRcZ+ybkya8Ox5IS/8Kyl+IfxhOF+h/k=")
ks.loginResult()

ka = LINETCR.LINE() #Franky
ka.login(token="El0ZOS3tnbB93N7iumP6.ThIZGMdUGG5NlyD4epVVnG.numswW7q5MTDBpixXFl0EVGciIGwCQMf1u/AMlzlS4g=")
ka.loginResult()

kb = LINETCR.LINE() #Brook
kb.login(token="ElT7GljgzFv1Iys0mA27.7b656S5SXJP+IQ3XR7YA9W.RjHETCwM7xN2eTVTpcjJ6uxDn80pmeaLQFSo7Hd2w6A=")
kb.loginResult()

ku = LINETCR.LINE() #Nami
ku.login(token="ElMmGcldrOeHLCjoSt50.A8sXP7Df+/Ovd4ui1UKIGa.YiOgT+5T+xqF7tFNVi4cI25qUNT4ZvDwCwKybGeOLdk=")
ku.loginResult()

ke = LINETCR.LINE() #Robin
ke.login(token="EmAfNIlCC9Zv1agwRmo0.Y00CqhaENcteJzCWN27b8a.rxwUqATGUrQYShpTTbkvK9VQwSVA3yF48tul2SCrNB8=")
ke.loginResult()

ko = LINETCR.LINE() # Jinbei
ko.login(token="EmrVMU8iGygAv7VuWLTf.COZUP/ShaopYOrHcnEKKpW.Hu4uN7326ypI9JjkoZ57FBQemOj6FUSx/6YaNpvOmRA=")
ko.loginResult()

k1 = LINETCR.LINE() #Backup
k1.login(token="Emiki05dLGYyttvrL1Ed.MvoKP48DWJ08plIY06TjVq.4u/TErYCpqbzrprJzrn3ipPyMiUJBr205a4+oYva0TQ=")
k1.loginResult()

print "login success plak"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉
Owner : ✰ЌờᎮḼΛẌֆ✰
-==================-
◄]·♦·Menu For Public·♦·[►
[•]Adminlist
[•]Ownerlist
[•]Info Group
[•]Welcome
[•]Creator
[•]Bot
◄]·♦·Menu For Admin·♦·[►
-==================-
[•]Cancel
[•]「Buka/Tutup」qr
[•]Mid Bot
[•]Speed/Sp
[•]「Cctv/Ciduk」
[•]Status/Set
[•]Gurl
[•]Jam「On/Off」
[•]Tag all/Tagall
[•]Absen/Respon
[•]Banlist
>>[Perintah Proteksi]<<
👑Hanya Untuk Owner👑
-==================-
O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉
-==================-
"""

Setgroup =""" 
    [Admin Menu]
==================
||[Protect QR]
||- Qr on/off
||[Protect Join]
||- Join on/off
||[Mid Via Contact]
||- Contact on/off
||-[Cancel Invited]
||- Cancel all
===================
O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉
==================="""
KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
DEF1=[ki,kk,kc,ks,ka,kb,ko,ke,ku]
DEF2=[cl,kk,kc,ks,ka,kb,ko,ke,ku]
DEF3=[cl,ki,kc,ks,ka,kb,ko,ke,ku]
DEF4=[cl,ki,kk,ks,ka,kb,ko,ke,ku]
DEF5=[cl,ki,kk,kc,ka,kb,ko,ke,ku]
DEF6=[cl,ki,kk,kc,ks,kb,ko,ke,ku]
DEF7=[cl,ki,kk,kc,ks,ka,ko,ke,ku]
DEF8=[cl,ki,kk,kc,ks,ka,kb,ke,ku]
DEF9=[cl,ki,kk,kc,ks,ka,kb,ko,ku]
DEF10=[cl,ki,kk,kc,ks,ka,kb,ko,ke]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Gmid = ku.getProfile().mid
Hmid = ke.getProfile().mid
Imid = ko.getProfile().mid
Smid = satpam.getProfile().mid
mid1 = k1.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Smid,mid1]
admin=["ued156c86ffa56024c0acba16f7889e6d","u2d76b3ee0f0795aa93d29bdfb5f2172c","uad208d16f70d0cc48645b9f5d5909936","u5ddba0b0366f32d148979ef879edf1f0","u98d947035133daf4ca2cadbe330e47af"] #mamih,awil,gamar,fatimah2
owner=["ued156c86ffa56024c0acba16f7889e6d"]
kawan=["u88cd7ee9fd691d6306e5e19be5d16f69"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
≫ ONE PIECE BOT PROTECT ≪

Ready:

≫ bot protect ≪
≫ SelfBot ≪


ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆ ONE PIECE TEAM PROTECT ☆
☆ SMULE VOICE FAMILY ☆
☆ FOUNDER COMMUNITY ☆
☆ Generasi Kickers Killers ☆


Minat? Silahkan PM!
Idline: http://line.me/ti/p/~hanavy1992""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    #"cName":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName2":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName3":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName4":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName5":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName6":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName7":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName8":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName9":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName10":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    #"cName11":"",
    #"cName12":"O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉ ",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

mimic = {
     "status":False,
     "target":{}
     }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'copy':False,
    'target':{},
    'midsTarget':{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                cl.kickoutFromGroup(op.param1,[op.param2])
                X = cl.getGroup(op.param1)
                X.preventJoinByTicket = True
                cl.updateGroup(X)
            else:
              print "Random Group Update"
          else:
            pass
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#  
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Amid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ks.acceptGroupInvitation(op.param1)
                else:
                  ks.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Emid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ka.acceptGroupInvitation(op.param1)
                else:
                  ka.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Fmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kb.acceptGroupInvitation(op.param1)
                else:
                  kb.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Gmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ku.acceptGroupInvitation(op.param1)
                else:
                  ku.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Hmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ke.acceptGroupInvitation(op.param1)
                else:
                  ke.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Imid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ko.acceptGroupInvitation(op.param1)
                else:
                  ko.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if Smid in op.param3:
              if wait["autoJoin"] == True:
                satpam.acceptGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
            
        if op.type == 17: #awal 17 ubah 13
          if wait["Protectjoin"] == True:
            if op.param2 not in admin or Bots:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).sendText(op.param1, "Protect Join Is On\nMatiin Terlebih dahulu Lalu Invite lagi\Joinn off")
        #------Joined User Kick start------#
        #if op.type == 19: #Member Ke Kick
          #if op.param2 in Bots:
            #pass
          #if op.param2 in admin:
            #pass
          #else:
            #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            #random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or admin:
                try:
                  G = satpam.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  satpam.updateGroup(G)
                  Ticket = satpam.reissueGroupTicket(op.param1)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  k1.kickoutFromGroup(op.param1,[op.param2])
                  H = k1.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  k1.updateGroup(H)
                  Ticket = k1.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  cl.sendText(op.param1, "Makasih Brader")
                  k1.sendText(op.param1, "Sama² Brader")
                  k1.sendText(op.param1, "Ane Balik Dulu\nAssalamualaikum")
                  cl.sendText(op.param1, "Wa'alaikumsalam")
                  k1.leaveGroup(op.param1)
                  G = satpam.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  satpam.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  k1.kickoutFromGroup(op.param1,[op.param2])
                  H = k1.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  k1.updateGroup(H)
                  Ticket = k1.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  cl.sendText(op.param1, "Makasih Brader")
                  k1.sendText(op.param1, "Sama² Brader")
                  k1.sendText(op.param1, "Ane Balik Dulu\nAssalamualaikum")
                  cl.sendText(op.param1, "Wa'alaikumsalam")
                  k1.leaveGroup(op.param1)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Amid:
              if op.param2 not in Bots or admin:
                try:
                  G = kk.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Bmid:
              if op.param2 not in Bots or admin:
                try:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Cmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ks.getGroup(op.param1)
                  ks.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Dmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ka.getGroup(op.param1)
                  ka.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ka.updateGroup(G)
                  Ticket = ka.reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ka.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Emid:
              if op.param2 not in Bots or admin:
                try:
                  G = kb.getGroup(op.param1)
                  kb.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kb.updateGroup(G)
                  Ticket = kb.reissueGroupTicket(op.param1)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kb.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Fmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ku.getGroup(op.param1)
                  ku.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ku.updateGroup(G)
                  Ticket = ku.reissueGroupTicket(op.param1)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ku.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Gmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ke.getGroup(op.param1)
                  ke.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ke.updateGroup(G)
                  Ticket = ke.reissueGroupTicket(op.param1)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Hmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ko.getGroup(op.param1)
                  ko.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ko.updateGroup(G)
                  Ticket = ko.reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ko.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Imid:
              if op.param2 not in Bots or admin:
                try:
                  G = cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in Smid:
              if op.param2 not in Bots:
                try:
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  k1.kickoutFromGroup(op.param1,[op.param2])
                  H = k1.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  k1.updateGroup(H)
                  Ticket = k1.reissueGroupTicket(op.param1)
                  satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  satpam.sendText(op.param1, "Makasih Brader")
                  k1.sendText(op.param1, "Sama² Brader")
                  k1.sendText(op.param1, "Ane Balik Dulu\nAssalamualaikum")
                  satpam.sendText(op.param1, "Wa'alaikumsalam")
                  k1.leaveGroup(op.param1)
                  G = cl.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  k1.kickoutFromGroup(op.param1,[op.param2])
                  H = k1.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  k1.updateGroup(H)
                  Ticket = k1.reissueGroupTicket(op.param1)
                  satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  satpam.sendText(op.param1, "Makasih Brader")
                  k1.sendText(op.param1, "Sama² Brader")
                  k1.sendText(op.param1, "Ane Balik Dulu\nAssalamualaikum")
                  satpam.sendText(op.param1, "Wa'alaikumsalam")
                  k1.leaveGroup(op.param1)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in admin:
              if op.param2 not in Bots:
                try:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,[op.param3])
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in kawan:
              if op.param2 not in Bots or owner:
                try:
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  cl.inviteIntoGroup(op.param1,[op.param3])
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
#--------------------------------                      
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
              if msg.from_ in owner:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
              text = msg.text
              if text is not None:
                cl.sendText(msg.to,text)
              else:
                if msg.contentType == 7:
                  msg.text = None
                  msg.contentMetadata = {
                                       "STKID": "100",
                                       "STKPKGID": "1",
                                       "STKVER": "100" }
                  cl.sendMessage(msg)
                elif msg.contentType == 13:
                  msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
                  cl.sendMessage(msg)
                  
            elif msg.text in ["Admin menu"]:
              if msg.from_ in owner:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Luffy gn " in msg.text):
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Zorro gn " in msg.text):
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Sanji gn " in msg.text):
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Luffy kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Zorro kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Sanji kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Zinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Zinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Sinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Sinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Uinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Uinvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif "Cinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Cinvite ","")
                ks.findAndAddContactsByMid(midd)
                ks.inviteIntoGroup(msg.to,[midd])
            elif "Finvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Finvite ","")
                ka.findAndAddContactsByMid(midd)
                ka.inviteIntoGroup(msg.to,[midd])
            elif "Binvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Binvite ","")
                kb.findAndAddContactsByMid(midd)
                kb.inviteIntoGroup(msg.to,[midd])
            elif "Ninvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Ninvite ","")
                ku.findAndAddContactsByMid(midd)
                ku.inviteIntoGroup(msg.to,[midd])
            elif "Rinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Rinvite ","")
                ke.findAndAddContactsByMid(midd)
                ke.inviteIntoGroup(msg.to,[midd])
            elif "Jinvite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Jinvite ","")
                ko.findAndAddContactsByMid(midd)
                ko.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Sudah Ditambahkan Boss")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Admin One Piece Bot||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
                  
            elif msg.text in ["Ownerlist","ownerlist"]:
              if owner == []:
                  cl.sendText(msg.to,"The Owner is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Owner One Piece Bot||\n====================\n"
                  for mi_d in owner:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Ownerlist executed"
    #--------------- Lawan atau Whitelist -------
            elif "Kawan add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Kawan add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Orang nya Ga Keliatan Kaya Setan")
                else:
                   for target in targets:
                        try:
                            kawan.append(target)
                            cl.sendText(msg.to,"Kawan Ditambahkan")
                        except:
                            pass
                print "[Command]Kawan add executed"
              else:
                cl.sendText(msg.to,"Lu Bukan Bukan Boss Gw Njir !!!")
                cl.sendText(msg.to,"Perintah Di Tolak\Beliin Gw Susu Gantung Dulu")
                
            elif "Kawan remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Kawan remove executing"
                _name = msg.text.replace("Kawan remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Orangnya ga ada Lagi Colli")
                else:
                   for target in targets:
                        try:
                            kawan.remove(target)
                            cl.sendText(msg.to,"Kawan Dihapus")
                        except:
                            pass
                print "[Command]Kawan remove executed"
              else:
                cl.sendText(msg.to,"Lu Bukan Bukan Boss Gw Njir !!!")
                cl.sendText(msg.to,"Perintah Di Tolak\Beliin Gw Susu Gantung Dulu")
                
            elif msg.text in ["Kawanlist","Kawan List","Kawan list"]:
              if admin == []:
                  cl.sendText(msg.to,"Kawan nya Kosong Boss")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "👥Kawan One Piece Team👥\n=====================\n"
                  for mi_d in kawan:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #---------------= Mimic =--------------
            elif "Mimic:" in msg.text:
              if msg.from_ in owner:
                cmd = msg.text.replace("Mimic:","")
                if cmd == "on":
                  if mimic["status"] == False:
                    mimic["status"] = True
                    cl.sendText(msg.to,"Mimic On Bossque")
                  else:
                    cl.sendText(msg.to,"Mimic Sudah On Bossque")
                elif cmd == "off":
                  if mimic["status"] == True:
                    mimic["status"] = False
                    cl.sendText(msg.to,"Mimic Off Bossque")
                  else:
                    cl.sendText(msg.to,"Mimic Sudah off")
                elif "add:" in cmd:
                  target0 = msg.text.replace("Mimic:add:","")
                  target1 = target0.lstrip()
                  target2 = target1.replace("@","")
                  target3 = target2.rstrip()
                  _name = target3
                  gInfo = cl.getGroup(msg.to)
                  targets = []
                  for a in gInfo.members:
                    if _name == a.displayName:
                      targets.append(a.mid)
                  if targets == []:
                    cl.sendText(msg.to,"No targets")
                  else:
                    for target in targets:
                      try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Success added target")
                        cl.sendMessageWithMention(msg.to,target)
                        break
                      except:
                        cl.sendText(msg.to,"Siap Ngikutin Chat Target Boss")
                        break
                elif "del:" in cmd:
                  target0 = msg.text.replace("Mimic:del:","")
                  target1 = target0.lstrip()
                  target2 = target1.replace("@","")
                  target3 = target2.rstrip()
                  _name = target3
                  gInfo = cl.getGroup(msg.to)
                  targets = []
                  for a in gInfo.members:
                    if _name == a.displayName:
                      targets.append(a.mid)
                  if targets == []:
                    cl.sendText(msg.to,"No targets")
                  else:
                    for target in targets:
                      try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Success deleted target")
                        cl.sendMessageWithMention(msg.to,target)
                        break
                      except:
                        cl.sendText(msg.to,"Ane Ga ngikutin lagi ah\nCape Gak Dapet Duit")
                        break
                elif cmd == "list":
                  if mimic["target"] == {}:
                    cl.sendText(msg.to,"No target")
                  else:
                    lst = "<<List Target>>"
                    total = len(mimic["target"])
                    for a in mimic["target"]:
                      if mimic["target"][a] == True:
                        stat = "On"
                      else:
                        stat = "Off"
                        lst += "\n->" + cl.getContact(a).displayName + " | " + stat
                        cl.sendText(msg.to,lst + "\nTotal:" + total)
#=================================Whitelist==========================
            elif "Whitelist " in msg.text:
              if msg.from_ in owner:
                whitelist0 = msg.text.replace("Whitelist ","")
                whitelist1 = whitelist0.lstrip()
                whitelist2 = whitelist1.replace("@","")
                whitelist3 = whitelist2.rstrip()
                _name = whitelist3
                groups = cl.getGroup(msg.to)
                targets = []
                for s in groups.members:
                  if _name in s.displayName:
                    targets.append(s.mid)
                if targets == []:
                  cl.sendText(msg.to,"Penduduk tidak ditemukan")
                  pass
                else:
                  for target in targets:
                    if target in wait["blacklist"]:
                      cl.sendText(msg.to,"User berada dalam daftar blacklist")
                    elif target in wait["whitelist"]:
                      cl.sendText(msg.to,"User sudah ada didalam whitelist")
                    elif target in admin:
                      cl.sendText(msg.to,"Admin tidak bisa ditambahkan kedalam whitelist")
                    elif target in owner:
                      cl.sendText(msg.to,"Owner tidak bisa ditambahkan kedalam whitelist")
                    else:
                      try:
                        wait["whitelist"][target] = True
                        cl.sendText(msg.to,"Berhasil menambahkan ke whitelist")
                      except:
                        cl.sendText(msg.to,"Sukses Boss")
                        break
            
            elif msg.text in ["Whitelist?"]:
              if msg.from_ in owner:
                if wait["whitelist"] == {}:
                  cl.sendText(msg.to,"Tidak ada whitelist saat ini")
                else:
                  mc = "===[Daftar User Whitelist]==="
                  for mi_d in wait["whitelist"]:
                    mc += "\n[" + cl.getContact(mi_d).displayName + "]"
                    mc += "\n -+MID\n  ->" + mi_d
                  cl.sendText(msg.to,mc)
                  
            elif "Hapuswhitelist " in msg.text:
              if msg.from_ in owner:
                whitelist0 = msg.text.replace("Hapuswhitelist ","")
                whitelist1 = whitelist0.lstrip()
                whitelist2 = whitelist1.replace("@","")
                whitelist3 = whitelist2.rstrip()
                _name = whitelist3
                groups = cl.getGroup(msg.to)
                targets = []
                for s in groups.members:
                  if _name in s.displayName:
                    targets.append(s.mid)
                if targets == []:
                  cl.sendText(msg.to,"Penduduk tidak ditemukan")
                  pass
                else:
                  for target in targets:
                    try:
                      del wait["whitelist"][target]
                      cl.sendText(msg.to,"Berhasil hapus dari whitelist")
                    except:
                      cl.sendText(msg.to,"Error!")
                      break
#====================================================================
    #--------------------------------------
    #-------------- Add Friends -----------
            elif "Bot add @" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  gs = ka.getGroup(msg.to)
                  gs = kb.getGroup(msg.to)
                  gs = ke.getGroup(msg.to)
                  gs = ko.getGroup(msg.to)
                  gs = ku.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        ka.findAndAddContactsByMid(target)
                        kb.findAndAddContactsByMid(target)
                        ko.findAndAddContactsByMid(target)
                        ke.findAndAddContactsByMid(target)
                        ku.findAndAddContactsByMid(target)
                        satpam.findAndAddContactsByMid(target)
                        cl.sendText(msg.to,"Kami Sudah Menambahkannya Sebagai Teman")
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Owner Kami")
                  
    #-------------=SC AllBio=----------------
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ku.getProfile()
                    profile.statusMessage = string
                    ku.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif "Spam " in msg.text:
              if msg.from_ in owner:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                #Keke cantik <3
                if txt[1] == "on":
                  if jmlh <= 1000:
                    for x in range(jmlh):
                      cl.sendText(msg.to, teks)
                  else:
                    cl.sendText(msg.to, "Out of range! ")
                elif txt[1] == "off":
                  if jmlh <= 2000:
                    cl.sendText(msg.to, tulisan)
                  else:
                    cl.sendText(msg.to, "Out of range! ")
                    
            elif "Fbc " in msg.text:
              if msg.from_ in owner:
	              print "[Friend Broadcast Excuted]"
	              bctxt = msg.text.replace("Fbc ","")
	              n = cl.getAllContactIds()
	              for people in n:
	                cl.sendText(people, (bctxt))
    #-----------------=Selesai=------------------
            elif msg.text in ["Bot?"]:
              if msg.from_ in owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ku.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ko.sendMessage(msg)
            elif msg.text in ["Me"]:
              if msg.from_ in owner:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in owner:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Op cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luffy buka qr","Luffy open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done Plak")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro buka qr","Zorro open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji open qr","Sanji buka qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luffy close qr","Luffy tutup qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro tutup qr","Zorro close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Plak")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji tutup qr","Sanji close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Info Group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
              random.choice(KAC).sendText(msg.to, msg.from_)
              
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                kb.sendText(msg.to,Fmid)
                ko.sendText(msg.to,Gmid)
                ke.sendText(msg.to,Hmid)
                ku.sendText(msg.to,Imid)
            elif "Koplaxs" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,Smid)
            elif "Luffy" == msg.text:
              if msg.from_ in admin:
                ki.sendText(msg.to,mid)
            elif "Zorro" == msg.text:
              if msg.from_ in admin:
                kk.sendText(msg.to,Amid)
            elif "Sanji" == msg.text:
              if msg.from_ in admin:
                kc.sendText(msg.to,Bmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in owner:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Bot1 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot3 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot3 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_C = kk.getProfile()
                    profile_C.displayName = string
                    kk.updateProfile(profile_C)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot4 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot4 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_D = kc.getProfile()
                    profile_D.displayName = string
                    kc.updateProfile(profile_D)
                    kc.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot5 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot5 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_E = ks.getProfile()
                    profile_E.displayName = string
                    ks.updateProfile(profile_E)
                    ks.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot6 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot6 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_F = ka.getProfile()
                    profile_F.displayName = string
                    ka.updateProfile(profile_F)
                    ka.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot7 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot7 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_G = kb.getProfile()
                    profile_G.displayName = string
                    kb.updateProfile(profile_G)
                    kb.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot8 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot8 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_H = ku.getProfile()
                    profile_H.displayName = string
                    ku.updateProfile(profile_H)
                    ku.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot9 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot9 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_I = ke.getProfile()
                    profile_I.displayName = string
                    ke.updateProfile(profile_I)
                    ke.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot10 rename "]:
              if msg.from_ in owner:
                string = msg.text.replace("Bot10 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_J = ko.getProfile()
                    profile_J.displayName = string
                    ko.updateProfile(profile_J)
                    ko.sendText(msg.to,"name " + string + " done")
            
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","Set"]:
              if msg.from_ in admin:
                md = "⭐Status Proteksi⭐\n*============*\n"
                if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
                if wait["contact"] == True: md+="[•]Contact [On]\n"
                else: md+="[•]Contact [Off]\n"
                if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[•]Auto Leave [On]\n"
                else: md+=" Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="[•]Share [On]\n"
                else:md+="[•]Share [Off]\n"
                if wait["autoAdd"] == True: md+="[•]Auto Add [On]\n"
                else:md+="[•]Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="[•]Comment [On]\n"
                else:md+="[•]Comment [Off]\n*============*\n⭐One Piece Bot⭐\n*============*"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
              if msg.from_ in owner:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
              if msg.from_ in owner:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
              if msg.from_ in owner:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
              if msg.from_ in owner:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
              if msg.from_ in owner:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
              if msg.from_ in owner:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
              if msg.from_ in owner:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
              if msg.from_ in admin:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
              if msg.from_ in admin:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
              if msg.from_ in owner:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in owner:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in owner:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
              if msg.from_ in owner:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
              if msg.from_ in owner:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "Cctv":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Cek CCTV")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "Ciduk":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "||Di Read Oleh||%s\n||By : Koplaxs BOT||\n\n>Pelaku CCTV<\n%s-=CCTV=-\n•Bintitan\n•Panuan\n•Kurapan\n•Kudisan\n\nAmiin Ya Allah\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu Koplak\nBaru Ketil Ciduk\nDASAR PIKUN ♪")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Kuy","Masuk","Join kuy"]:
              if msg.from_ in owner:
                G = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = cl.getGroup(msg.to)
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                print "Semua Sudah Lengkap"
                
            elif msg.text in ["Kuya","Kunyuk"]:
              if msg.from_ in owner:
                G = satpam.getGroup(msg.to)
                ginfo = satpam.getGroup(msg.to)
                G.preventJoinByTicket = False
                satpam.updateGroup(G)
                invsend = 0
                Ticket = satpam.reissueGroupTicket(msg.to)
                cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                G = satpam.getGroup(msg.to)
                G.preventJoinByTicket = True
                satpam.updateGroup(G)
                print "Semua Sudah Lengkap"
                
            elif msg.text in ["Luffy join"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Zorro join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Sanji join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Ussop Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Bye op","Kabur all","Kaboor all"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["Kaboor"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
                      
            elif msg.text in ["Bye zorro"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye sanji"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Ussop"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe1"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe2"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe3"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag all","Tagall"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Bot Like", "Bot like"]:
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
              else:
                cl.sendText(msg.to,"Command Ini Hanya Untuk Owner\nMaaf yah Ka")
                
            elif msg.text in ["Like temen", "Bot like temen"]:
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Ready op" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Ready op","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = ku.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = ko.getGroup(msg.to)
                    #random.choice(KAC).sendText(msg.to,"maaf kalo gak sopan")
                    random.choice(KAC).sendText(msg.to,"makasih semuanya..")
                    #random.choice(KAC).sendText(msg.to,"hehehhehe")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target in admin:
                            pass
                          if target in Bots:
                            pass
                          else:
                            try:
                              klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                              kicker=random.choice(klist)
                              kicker.kickoutFromGroup(msg.to,[target])
                              print (msg.to,[g.mid])
                            except:
                              random.choice(KAC).kickoutFromGroup(msg.to,[target])
                              #random.choice(KAC).kickoutFromGroup(msg.to,[target])
                              #random.choice(KAC).kickoutFromGroup(msg.to,[target])
        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in owner:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                  cl.sendText(msg.to,"user does not exist")
                  pass
                else:
                   for target in targets:
                      k1.kickoutFromGroup(msg.to,[target])
                      k1.leaveGroup(msg.to)
                      gs = cl.getGroup(msg.to)
                      gs.preventJoinByTicket = True
                      cl.updateGroup(gs)
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Ban @ " in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Ban @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes Plak")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
                                
            elif "Unban all" in msg.text:
              if msg.from_ in owner:
                del wait["blacklist"][target]
                f=codecs.open('st2__b.json','w','utf-8')
                json.dump(wait["blacklist"],f, sort_keys=True,indent=4,ensure_ascii=False)
                cl.sendText(msg.to,"Berhasil Dihapus")
        #----------------Fungsi Unbanned User Target Finish-----------------------#
        #-------=-----==---= Send PM -------
            elif "/kirimpesan: " in msg.text:
              if msg.from_ in owner:
                cond = msg.text.split(" ")
                target = int(cond[1])
                text = msg.text.replace("/kirimpesan: " + str(target) + "\n/Message: ","")
                try:
                  cl.findAndAddContactsByMid(target)
                  ki.findAndAddContactsByMid(target)
                  kk.findAndAddContactsByMid(target)
                  kc.findAndAddContactsByMid(target)
                  ks.findAndAddContactsByMid(target)
                  ka.findAndAddContactsByMid(target)
                  kb.findAndAddContactsByMid(target)
                  ku.findAndAddContactsByMid(target)
                  ke.findAndAddContactsByMid(target)
                  ko.findAndAddContactsByMid(target)
                  cl.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  ki.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  kk.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  kc.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  ks.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  ka.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  kb.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  ku.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  ke.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  ko.sendText(target,"Saya membawakan pesan dari presiden untuk anda yang berisi: \"" + text + "\"")
                  cl.sendText(msg.to,"Berhasil mengirim pesan")
                except:
                  cl.sendText(msg.to,"Gagal mengirim pesan, mungkin midnya salah")
        #------------- Copy profile -----------
            elif "Copy @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Copy @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                  if _nametarget == g.displayName:
                    targets.append(g.mid)
                if targets == []:
                  sendMessage(msg.to, "Not Found...")
                else:
                  for target in targets:
                    try:
                      cl.cloneContactProfile(target)
                      cl.sendText(msg.to, "Success Copy profile ~")
                    except Exception as e:
                      print e
                            
            elif msg.text in ["Backup","backup"]:
              if msg.from_ in owner:
                try:
                  cl.updateDisplayPicture(backup.pictureStatus)
                  cl.updateProfile(backup)
                  cl.sendText(msg.to, "Backup done")
                except Exception as e:
                  cl.sendText(msg.to, str(e))
                  
            elif "Steal dp @" in msg.text:
              if msg.from_ in owner:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                   if _nametarget == g.displayName:
                    targets.append(g.mid)
                if targets == []:
                  ki.sendText(msg.to,"Contact not found")
                else:
                  for target in targets:
                    try:
                      contact = cl.getContact(target)
                      path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                      cl.sendImageWithURL(msg.to, path)
                    except:
                      pass
                print "[Command]dp executed"
                
            elif "Contact bc " in msg.text:
              if msg.from_ in owner:
                bctxt = msg.text.replace("Contact bc ", "")
                t = cl.getAllContactIds()
                t = 100
                while(t):
                  cl.sendText(msg.to, (bctxt))
                  t-=1
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg.from_ in owner:
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!����")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text:
              if msg.from_ in owner:
                bctxt = msg.text.replace("Bc ","")
                a = cl.getGroupIdsJoined()
                a = ki.getGroupIdsJoined()
                a = kk.getGroupIdsJoined()
                a = kc.getGroupIdsJoined()
                a = ks.getGroupIdsJoined()
                a = ka.getGroupIdsJoined()
                a = ku.getGroupIdsJoined()
                a = ke.getGroupIdsJoined()
                a = ko.getGroupIdsJoined()
                a = kb.getGroupIdsJoined()
                for taf in a:
                  cl.sendText(taf, (bctxt))
                  ki.sendText(taf, (bctxt))
                  kk.sendText(taf, (bctxt))
                  kc.sendText(taf, (bctxt))
                  ks.sendText(taf, (bctxt))
                  ka.sendText(taf, (bctxt))
                  kb.sendText(taf, (bctxt))
                  ke.sendText(taf, (bctxt))
                  ku.sendText(taf, (bctxt))
                  ko.sendText(taf, (bctxt))
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["LG"]:
              if msg.from_ in owner:
                gids = cl.getGroupIdsJoined()
                h = ""
                for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   + "👉" + str(len(cl.getGroup(i).members)))
                cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :" + str(len(gids)))
                
            elif msg.text in ["LG2"]:
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Bot out","Op bye"]:
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = kk.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = ks.getGroupIdsJoined()
                gid = ka.getGroupIdsJoined()
                gid = kb.getGroupIdsJoined()
                gid = ko.getGroupIdsJoined()
                gid = ke.getGroupIdsJoined()
                gid = ku.getGroupIdsJoined()
                for i in gid:
                  ku.leaveGroup(i)
                  ke.leaveGroup(i)
                  ko.leaveGroup(i)
                  kb.leaveGroup(i)
                  ka.leaveGroup(i)
                  ks.leaveGroup(i)
                  kc.leaveGroup(i)
                  ki.leaveGroup(i)
                  kk.leaveGroup(i)
                  cl.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Sayonara")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#------------------------End---------------------

 #-----------------End-----------
            elif msg.text in ["Op katakan hi"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
#-----------------------------------------------
            elif msg.text in ["Welcome"]:
                cl.sendText(msg.to,"Selamat datang di Group Kami")
                cl.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                #kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                #kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen","Absen bot","Absen dulu","Respon"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"⭐")
                ki.sendText(msg.to,"⭐⭐")
                kk.sendText(msg.to,"⭐⭐⭐")
                kc.sendText(msg.to,"⭐⭐⭐⭐")
                ks.sendText(msg.to,"⭐⭐⭐⭐⭐")
                ka.sendText(msg.to,"⭐⭐⭐⭐⭐")
                kb.sendText(msg.to,"⭐⭐⭐⭐")
                ko.sendText(msg.to,"⭐⭐⭐")
                ke.sendText(msg.to,"⭐⭐")
                ku.sendText(msg.to,"⭐")
                cl.sendText(msg.to,"Semua Udah Hadir Boss\nSiap Protect Group\nAman Gak Aman Yang Penting Anu")
      #-------------Fungsi Respon Finish---------------------#    
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")
      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in admin:
                start = time.time()
                cl.sendText(msg.to, "Sabar Plak...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'ued156c86ffa56024c0acba16f7889e6d'}
              cl.sendText(msg.to,"======================")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"======================")
              cl.sendText(msg.to,"Itu Creator Kami Yang Pea 😜")
                
      #-------------Fungsi Chat ----------------
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in owner or admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "Random " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("Random ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "Fakecat" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          cl.sendText(op.param1, "👥Selamat Datang Di Grup👥\n" + "👉" + str(ginfo.name) + "👈" + "\n" + "👑Founder Grup👑" + str(ginfo.name) + "\n" + ginfo.creator.displayName + "\n\n" + "Group Ini Di Protect Oleh :" + "\n⭐||One Piece Team Protect||⭐")
          #random.choice(KAC).sendText(op.param1, "Founder Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
          #random.choice(KAC).sendText(op.param1,"Budayakan Baca Note !!! yah Ka 😊\nSemoga Betah Kk 😘")
          print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
          if op.param2 in Bots:
            return
          random.choice(KAC).sendText(op.param1, "Kenapa Tuh Leave?\nBaper Kayaknya")
          print "MEMBER HAS LEFT THE GROUP"
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,1000):
      hasil = cl.activity(limit=1000)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by ⭐⭐Koplaxs⭐⭐👈\n\nO҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉")
          satpam.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #kb.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ku.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          #ko.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,1000):
        hasil = cl.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by : O҉n҉e҉ ҉P҉i҉e҉c҉e҉ ҉T҉e҉a҉m҉ ҉P҉r҉o҉t҉e҉c҉t҉\nStatus Boss udah Kami Like\nOwner Kami :\nHanavy Koplaxs")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"
                
#def nameUpdate():
    #while True:
        #try:
        #while a2():
            #pass
            #if wait["clock"] == True:
                #now2 = datetime.now()
                #nowT = datetime.strftime(now2,"(%H:%M)")
                #profile = cl.getProfile()
                #profile.displayName = wait["cName"]
                #cl.updateProfile(profile)

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
