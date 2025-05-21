import os, shutil

path = r"C:/Users/Visie Groep.TEMP-09/Documents/Python File Sorter/"
file_name = os.listdir(path)

folder_names = ['odp files','ods files','odt files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        #print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".odp" in file and not os.path.exists(path + "odp files/" + file):
        shutil.move(path + file, path + "odp files/" + file)
    elif "ods" in file and not os.path.exists(path + "ods files/" + file):
        shutil.move(path + file, path + "ods files/" + file)
    elif "odt" in file and not os.path.exists(path + "odt files/" + file):
        shutil.move(path + file, path + "odt files/" + file)

