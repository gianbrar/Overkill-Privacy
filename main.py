import hashlib
import os

breakLoop = False
passPath = "/bin/OverkillPrivacy/pass.txt"
passFile = open(passPath, 'r')
password = passFile.read()
passWriteFile = open(passPath, 'w')

while (breakLoop == False):
  menu = input("OVERKILL PRIVACY MACHINE 1.0\nP: Password menu\nE: Encrypt\nD: Decrypt\nI: Info")
  menu = menu.lower()
  if menu == "i":
    print("Programmed by Gian Brar for Trisha Reddy's 14th birthday, OVERKILL PRIVACY MACHINE is for the writer who wishes for others not to view anything they write. It utilizes military grade SHA (Secure Hash Algorithim) encryption with a program that has been proven mathematically impossible to reverse in order to hide your private info from your family.")
  elif menu == "p":
    passwordMenu = input("M: Make password\nD: Delete password\nG: Get password key")
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
      getPassword = input("Enter password for key generation; password will NOT be added to list.")
      print(hashlib.sha3_512(getPassword.encode("utf-8")).hexdigest())
  else:
    print("Please select a listed choice.")
