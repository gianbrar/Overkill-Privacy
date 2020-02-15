import hashlib
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

pwdPath = "/bin/OverkillPrivacy/pwdf.txt"
pwdFile = open(pwdPath, 'r')
pwd = pwdFile.read()
os.system("cd " + pwd)
os.system("./sudocheck")

breakLoop = False
passPath = "/bin/OverkillPrivacy/pass.txt"
passFile = open(passPath, 'r')
password = passFile.read()
passWriteFile = open(passPath, 'w')
storyPath = "/bin/OverkillPrivacy/story.txt"
storyFile = open(storyPath, 'r')
story = storyFile.read()
storyWriteFile = open(storyPath, 'w')


while (breakLoop == False):
  menu = input("OVERKILL PRIVACY MACHINE 1.0\nP: Password menu\nE: Encrypt\nD: Decrypt\nI: Info\n")
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
      print(passwordI + " was ENCRYPTED into password list.")
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
      encryptNameBool = encryptName.endswith(".txt")
      if encryptNameBool == True:
        os.system("vim -c 'startinsert' " + encryptName)
      else:
        os.system("vim -c 'startinsert' " + encryptName + ".txt")
    elif encryptMenu == "g":
      gauth = GoogleAuth()
      gauth.LocalWebserverAuth()
      drive = GoogleDrive(gauth)
      file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
      selection = input("Please choose Google Doc Name.")
      file1 = drive.CreateFile({'id': file1['id']})
      file1.GetContentFile(selection)
  else:
    print("Please select a listed choice.")
