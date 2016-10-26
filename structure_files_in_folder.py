# A python script to structure different types of files in the folder. For Example
# if your path contains many sql files, xls files, doc files, docx files and py files
# and it is difficult to maintain, this script will structure all single type of files by creating
# a  folder into this path. Thus you can structure your folder comfortably.
# It will accept three inputs -
# a) The path in your drive that needs structuring
# b) The folder name that you want to give
# c) The type of file you want to atructure.
import os
import shutil
import time
# Taking input from the user
path = input("Enter the path where you need restructuring. A new folder will be created there : ")
# To check if path exist or not
if not (os.path.isdir(path)) :
    print("The path - "+path+" does not exist. Enter the correct path. So exiting...")
    time.sleep(2)
    exit(1)
folder_name = input("Enter the name of the folder you want to create : ")
file_type = input("Enter the file type that you wish to structure from "+path+" in the above folder "+folder_name+" (SQL,DOCX,DOC,PDF,TXT,MSG,XLSX,XLS,PY,JPEG,PNG formats are acceptable): ")
newpath = path + "/" + folder_name
found_file_type = False
try :
# If newpath does not exist, create a new one
    if not os.path.exists(newpath): os.makedirs(newpath)
    os.chdir('C:\\')
    # Setting the source and destination folders
    dir_src = path+"/"
    dir_dst = newpath
    # For SQL Files
    if file_type in ('SQL','sql','.SQL','.sql') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.sql'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    # For DOCX Files
    if file_type in ('docx','DOCX','.docx','.DOCX') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.docx'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    # For DOC Files
    if file_type in ('doc','DOC','.doc','.DOC') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.doc'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    # For PDF Files
    if file_type in ('pdf','PDF','.pdf','.PDF') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.pdf'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    # For TXT Files
    if file_type in ('txt','TXT','.txt','.TXT') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.txt'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    # For OUTLOOK MESSAGE Files
    if file_type in ('msg','MSG','.msg','.MSG') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.msg'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    # For EXCEL Files
    if file_type in ('xlsx','XLSX','.xlsx','.XLSX') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.xlsx'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    if file_type in ('xls','XLS','.xls','.XLS') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.xls'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    # For Python Script Files
    if file_type in ('py','PY','.py','.PY') :
        for filename in os.listdir(dir_src):
            if filename.endswith('.py'):
                shutil.move( dir_src + filename, dir_dst)
                found_file_type = True
    # For JPEG Files
    if file_type in ('jpeg','JPEG','.jpeg','.JPEG') : 
            for filename in os.listdir(dir_src):
                if filename.endswith('.jpeg'):
                    shutil.move( dir_src + filename, dir_dst)
                    found_file_type = True
     # For PNG Files
    if file_type in ('png','PNG','.png','.PNG') :
            for filename in os.listdir(dir_src):
                if filename.endswith('.png'):
                    shutil.move( dir_src + filename, dir_dst)
                    found_file_type = True                
except OSError : print("The path given by you : "+path+" does not exist");
if not found_file_type :
    print("No ."+file_type+" file type is present in the path : "+path+". So exiting...")
    if os.path.exists(newpath) : os.removedirs(newpath)
    time.sleep(2)
    exit(1)
    
    
