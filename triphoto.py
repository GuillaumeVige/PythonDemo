#Guillaume Vige 25/11/2018
#Suppression des photos en double (merci Anna)

import os

def dup_fileremove(dir1,dir2):
#cette fonction supprime dans dir2 les fichiers qui ont le meme nom qu'un fichier de dir1
#attention dangereux !
   i1=0; nbDoublon=0
   duplicate = set()
   os.chdir(dir1)
   path=os.getcwd()
   print ("The dir is: ", path)
   for filename1 in os.listdir(dir1):
      i1=i1+1
      i2=0
      for filename2 in os.listdir(dir2):
         i2=i2+1
         if (filename2==filename1):# and (filename2[0:4]=="2017"):
            nbDoublon=nbDoublon+1
            filepath2=os.path.join(dir2, filename2)
            print(filepath2)
            #os.remove(filepath2)
   print("dir 1 :"+dir1+" "+str(i1)+"  files")
   print("dir 2 :"+dir2+" "+str(i2)+"  files")
   print("Nb doublons : "+str(nbDoublon))

dir1 = "/home/guillaume/Images/2017"
dir2 = "/home/guillaume/Images/2018"
os.chdir(dir1)
dup_fileremove(dir1,dir2)



