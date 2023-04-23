from tkinter import *
from tkinter import filedialog
import os
import shutil


image = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
video = ['.mp4', '.avi', '.mov', '.wmv', '.mkv']
sound = ['.mp3', '.wav', '.flac', '.m4a', '.ogg']
text = ['.txt', '.doc', '.docx', '.md', '.pdf']
software = ['.exe', '.app', '.deb', '.rpm', '.jar', '.py', '.cpp', '.h', '.cs', '.dll']

root = Tk()
root.geometry("450x200")


# main function
def organize(folder_path):
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)): # Is ir a file?
            extension = os.path.splitext(file)[1]
            # Is it an image?
            if extension in image:
                if not os.path.exists(os.path.join(folder_path, 'image')):
                    os.makedirs(os.path.join(folder_path, 'image'))
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'image', file))
            # Is it a video?
            elif extension in video:
                if not os.path.exists(os.path.join(folder_path, 'video')):
                    os.makedirs(os.path.join(folder_path, 'video'))
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'video', file))
            # Is it a sound?
            elif extension in sound:
                if not os.path.exists(os.path.join(folder_path, 'sound')):
                    os.makedirs(os.path.join(folder_path, 'sound'))
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'sound', file))
            # Is it a text?
            elif extension in text:
                if not os.path.exists(os.path.join(folder_path, 'text')):
                    os.makedirs(os.path.join(folder_path, 'text'))
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'text', file))
            # Is it a softwate?
            elif extension in software:
                if not os.path.exists(os.path.join(folder_path, 'software')):
                    os.makedirs(os.path.join(folder_path, 'software'))
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'software', file))
            # Else
            else:
                if not os.path.exists(os.path.join(folder_path, 'other')):
                    os.makedirs(os.path.join(folder_path, 'other'))
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'other', file))

# Select folder function
def select_folder():
    
    path = filedialog.askdirectory()
    organize(path)


# App title
root.title("Folder Organizer")

# App title
app_title = Label(root, text="Folder Organizer", font=('Arial', 18))
app_title.pack()

# Button
choose = Button(root, name="aaa", text="Select the folder", command=select_folder)
choose.pack(padx=5, pady=5)


root.mainloop()