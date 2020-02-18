import hashlib
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from emoji import emojize

os.system("./sudocheck")
exitTFF = open("overkillPrivacyDD.txt", 'r')
exitTF = exitTFF.read()
if exitTF == "exit\n":
  os.system("cat /dev/null > overkillPrivacyDD.txt")
  exit()

pwdPath = "/usr/bin/OverkillPrivacy/pwdf.txt"
pwdFile = open(pwdPath, 'r')
pwd = pwdFile.read()
os.system("cd " + pwd)

passPath = "/usr/bin/OverkillPrivacy/pass.txt"
passFile = open(passPath, 'r')
password = passFile.read()
passWriteFile = open(passPath, 'w')
storyPath = "/usr/bin/OverkillPrivacy/story.txt"
storyFile = open(storyPath, 'r')
story = storyFile.read()
storyWriteFile = open(storyPath, 'w')


while (True):
  menu = input("OVERKILL PRIVACY MACHINE 1.0\nP: Password menu\nE: Encrypt\nD: Decrypt\nI: Info\nX: Exit\n")
  menu = menu.lower()
  if menu == "i":
    print("Programmed by Gian Brar for Trisha Reddy's 14th birthday, OVERKILL PRIVACY MACHINE is for the writer who wishes for others not to view anything they write. It utilizes military grade SHA (Secure Hash Algorithim) encryption with a program that has been proven mathematically impossible to reverse in order to hide your private info from your family.")
  elif menu == "p":
    passwordMenu = input("M: Make password\nD: Delete password\nG: Get password key\n")
    passwordMenu = passwordMenu.lower()
    if passwordMenu == "m":
    # sLevel = input("Please choose level of security.\nBASIC: Simple encryption; medium security level.\nADVANCED: More complex encryption which may take longer for larger inputs.\nGOD: Incredibly complicated encryption which may take very long time to en/decrypt.")
    # sLevel = sLevel.lower()
      passwordI = input("Please enter password.")
      passwordIE = hashlib.sha3_512(passwordI.encode("utf-8")).hexdigest()
      passWriteFile.write(passwordIE)
      passWriteFile.write("\n")
      print(emojize(":closed_lock_with_key:") + " " + passwordI + " was ENCRYPTED into password list. " + emojize(":closed_lock_with_key:"))
    elif passwordMenu == "d":
      deletePassword = input("Choose password to be deleted:\n" + password)
    elif passwordMenu == "g":
      getPassword = input("Enter password for key generation testing; password will NOT be added to list.")
      print(hashlib.sha3_512(getPassword.encode("utf-8")).hexdigest())
  elif menu == "e":
    encryptMenu = input("T: Type out story\nG: Encrypt from Google Doc\n")
    encryptMenu = encryptMenu.lower()
    if encryptMenu == "t":
      encryptName = input("Please give name of story.")
      encryptName = encryptName.replace(" ", "")
      encryptNameBool = encryptName.endswith(".txt")
      if encryptNameBool == False:
        encryptName = encryptName + ".txt"
      os.system("vim -c 'startinsert' " + encryptName)
      
    elif encryptMenu == "g":
      print("Placeholder")
  elif menu == "x":
    print("Exiting")
    exit()
  else:
    print("Please select a listed choice.")
