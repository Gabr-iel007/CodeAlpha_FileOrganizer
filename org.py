import os
import shutil

folder_path = input("Enter folder path: ").strip() # include folder path you want to organize

files = os.listdir(folder_path)

print(files) #lists all files in the directory

os.makedirs(folder_path + "\\Images", exist_ok=True)#creates folders
os.makedirs(folder_path + "\\Videos", exist_ok=True)
os.makedirs(folder_path + "\\Music", exist_ok=True)
os.makedirs(folder_path + "\\Document", exist_ok=True)

for file in files:
    name, extension = os.path.splitext(file)

    if extension in [".jpg", ".jpeg", ".png"]: #checks for extensions of each file
        source = os.path.join(folder_path, file)# source of file
        destination = os.path.join(folder_path, "Images")# destination of file
        shutil.move(source, destination) #move file to new destination
        print(file, "-> Images") # file type, image

    elif extension in [".mp4", ".mkv"]:
        source = os.path.join(folder_path, file)
        destination = os.path.join(folder_path, "Videos")
        shutil.move(source, destination)
        print(file, "-> Videos")
    
    elif extension in [".mp3", ".wav"]:
        source = os.path.join(folder_path, file)
        destination = os.path.join(folder_path, "Music")
        shutil.move(source, destination)
        print(file, "-> Music")

    elif extension in [".txt", ".pdf", ".docx"]:
        source = os.path.join(folder_path, file)
        destination = os.path.join(folder_path, "Document")
        shutil.move(source, destination)
        print(file, "-> Document")
        
    