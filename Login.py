from tkinter import *
import os
import time
import hashlib
import playsound
import speech_recognition as sr
from gtts import gTTS
import cv2
from PIL import Image, ImageTk

def speak_Camera(text):

    tts = gTTS(text = text)
    filename = "Instructions.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speak(text):

    tts = gTTS(text = text)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def speak_error(text):

    tts = gTTS(text = text)
    filename = "Error.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    global said
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


def register_user():

    if not username.get():
        Label(screen1, text = "Registration unsuccesful", fg = "red", font = ("Calibri",11)).pack()
        return
    if not password.get():
        Label(screen1, text = "Registration unsuccesful", fg = "red", font = ("Calibri",11)).pack()
        return
    username_info = username.get()
    password_info = password.get()

    file = open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Succesful", fg = "green", font = ("Calibri",11)).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    
    global username_login
    global password_login
    global username_entry_login
    global password_entry_login
    
    username_login = StringVar()
    password_login = StringVar()

    Label(screen2, text = "Please enter the details below ").pack()
    Label(text = "").pack()


    Label(screen2, text = "Username * ").pack()
    Label(text = "").pack()
    username_entry_login = Entry(screen2, textvariable = username_login)
    username_entry_login.pack()
    Label(screen2, text = "Password * ").pack()
    password_entry_login = Entry(screen2, textvariable = password_login,show = "*")
    password_entry_login.pack()
    Label(text = "").pack()

    Button(screen2, text = "Login", width = 10, height = 1, command = login_user).pack()
    
    
def login_user():

    global username1
    username1 = username_login.get()
    password1 = password_login.get()

    list_of_files = os.listdir()

    if(username1 in list_of_files):
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if(password1 in verify):
           print("Login success")
           Label(screen2, text = "Login Succesful", fg = "green", font = ("Calibri",11)).pack()
           screen.quit()
           game_menu()
           print("Opening")
           time.sleep(2)
        else:
            print("Password is wrong")
            Label(screen2, text = "Check the password!!!!", fg = "red", font = ("Calibri",11)).pack()
    else:
        print("User not found")
        Label(screen2, text = "User not found!!", fg = "red", font = ("Calibri",11)).pack()
    username_entry_login.delete(0,END)
    password_entry_login.delete(0,END)

    

    
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter the details below ").pack()
    Label(text = "").pack()


    Label(screen1, text = "Username * ").pack()
    Label(text = "").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password,show = "*")

    password_entry.pack()
    Label(text = "").pack()

    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

playsound.playsound("OpeningCamera.mp3")
playsound.playsound("Instructions.mp3")


cam = cv2.VideoCapture(0)
cv2.namedWindow("Profile Picture")

img_counter = 0

while True:
    

    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Profile Picture", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        global img_name
        img_name = "profile_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        break

    
def main_screen():
    global screen
    screen = Tk()
    screen.configure(bg="black")
    screen.geometry("1255x944")
    
    image = Image.open(img_name)
    image = image.resize((100,100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    user_label = Label(image = photo)

    user_label.pack()

    #os.startfile(r"C:\Users\ThinkPad\Desktop\PythonProject\Music\playMusicMainMenu.py")

    #playSong()
    screen.title("GameHub")
    Label(text = "GameHub", bg = "orange", width = "300",height = "2", font = ("Candara",14)).pack()
    Label(text = "").pack()
    Button(text = "Login" ,height = "2", width = "30",command = login).pack()
    Label(text = "").pack()
    Button(text = "Register",height = "2", width = "30",command = register).pack()

    screen.mainloop()


def game_menu():
    
    global screen_game
    screen_game = Tk()
    screen_game.configure(bg = "pink")
    screen_game.geometry("720x360")
    screen_game.title("Select Game")
    Label(text = "Game Menu", bg = "orange", width = "300",height = "2", font = ("Candara",12)).pack()
    Label(text = "").pack()
    Button(text = "Emoji Race" ,height = "2", width = "30",command = Emoji_Race).pack()
    Button(text = "Rock Paper Scissors" ,height = "2", width = "30",command = RPS).pack()
    Button(text = "Cricket" ,height = "2", width = "30",command = Cricket).pack()
    Button(text = "Text Game" ,height = "2", width = "30",command = text_Game).pack()
    Label(text = "").pack()
    #Button(text = "Exit",height = "2", width = "30",command = Exit).pack()
    Button(text = "Speech Recognition" ,height = "2", width = "30",command = Recognition).pack()

def text_Game():
    os.startfile(r"C:\Users\ThinkPad\Desktop\PythonProject\TextGame.py")

def Emoji_Race():
    os.startfile(r"C:\Users\ThinkPad\Desktop\PythonProject\Emoji_Race.py")

def RPS():
    os.startfile(r"C:\Users\ThinkPad\Desktop\PythonProject\rock papers and knife.py")

def Cricket():
    os.startfile(r"C:\Users\ThinkPad\Desktop\PythonProject\cric.py")

def speak_user(text):

    tts = gTTS(text = text)
    filename = "username.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def Recognition():
    
    playsound.playsound("username.mp3")
    playsound.playsound("voice.mp3")
    get_audio()
    if(said == "emoji race"):
        Emoji_Race()
        print(said)
    elif(said == "rps"):
        RPS()
        print(said)
    elif(said == "cricket"):
        Cricket()
        print(said)
    elif(said == "text game"):
        text_Game()
        print(said)
    else:
        print("WRONG")
        print(said)
        speak_error("Sorry! I was not able to understand that. Please try again")
        get_audio()

    
main_screen()
