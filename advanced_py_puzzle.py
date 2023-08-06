import shutil
import os
import re

# shutil.unpack_archive('unzip_me_for_instructions.zip','instructions_unzipped','zip')

folders_list = os.listdir(os.getcwd()+'\instructions_unzipped\extracted_content')

for folder , sub_folders , files in os.walk(os.getcwd()+'\instructions_unzipped\extracted_content'):
    
    # print("Currently looking at folder: "+ folder)
    # print('\n')
    # print("THE SUBFOLDERS ARE: ")
    # for sub_fold in sub_folders:
    #     print("\t Subfolder: "+sub_fold )
    for f in files:
        
        if f != 'Instructions.txt':
            file_content = open(folder+'\\'+f,"r")
            text = file_content.read()
            result = re.search(r"\d{3}-\d{3}-\d{4}",text)
            if result != None:
                print(folder)
                print("\t File: "+f)
                print(result.group())
                break