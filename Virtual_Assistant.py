import speech_recognition as sr    #To convert speech into text
import pyttsx3                     #To convert text into speech
import datetime                    #To get the date and time
import wikipedia                   #To get information from wikipedia
import webbrowser                  #To open websites
import os                          #To open files
import time                        #To calculate time
import subprocess                  #To open files
from tkinter import *              #For the graphics
import pyjokes
from playsound import playsound

def delete1():
    screen.destroy()
  
file1 = open("Assistant_name", "r")
name_assistant = file1.read()
engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    print(name_assistant + " : "  +  text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
   
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
 
    else:
        speak("Hello,Good Evening")


def get_audio(): 

    r = sr.Recognizer() 
    audio = '' 

    with sr.Microphone() as source: 

        print("Listening") 
        playsound("bike.wav")
        audio = r.listen(source, phrase_time_limit = 3) 
        playsound("close.wav")
        print("Stop.") 
        
    try: 
        text = r.recognize_google(audio, language ='en-US') 
        print('You: ' +text)
        return text


    except Exception as e:

        
        return "None"
        return statement


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 
    

    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')

wishMe()


def Process_audio():

    run = 1
    if __name__=='__main__':
        while run==1:

            statement = get_audio().lower()
            results = ''
            run +=1

            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('your personal assistant ' + name_assistant +' is shutting down, Good bye')
                delete1()
                break

            if 'wikipedia' in statement:


              speak('Searching Wikipedia...')
              statement = statement.replace("wikipedia", "")
              results = wikipedia.summary(statement, sentences = 3)
              speak("According to Wikipedia")
              speak(results)

            if 'joke' in statement:
              speak(pyjokes.get_joke())    
     
            if 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)


            if 'open google' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)


            if 'open gmail' in statement:
                    webbrowser.open_new_tab("mail.google.com")
                    speak("Google Mail open now")
                    time.sleep(5)

            if 'open netflix' in statement:
                    webbrowser.open_new_tab("netflix.com/browse") 
                    speak("Netflix open now")


            if 'open primevideo' in statement:
                    webbrowser.open_new_tab("primevideo.com") 
                    speak("Amazon Prime Video open now")
                    time.sleep(5)

            if 'open word' in statement:
                os.startfile(r'C:\Users\shriraksha\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows 7\Microsoft Office Word 2007')
                speak("Microsoft office word is opening now")

            if 'open powerpoint' in statement:
                os.startfile(r'C:\Users\shriraksha\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows 7\Microsoft Office PowerPoint 2007')
                speak("Microsoft office PowerPoint is opening now")

            if 'open excel' in statement:
                os.startfile(r'C:\Users\shriraksha\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows 7\Microsoft Office Excel 2007')
                speak("Microsoft office Excel is opening now")
        
            if 'open notepad' in statement:
                os.startfile(r'C:\Users\shriraksha\AppData\Roaming\Microsoft\Windows\Start Mename\Programs\Accessories\Notepad.lnk')
                speak("NotePad is opening now")


            if 'open chrome' in statement:
                os.startfile(r'C:\Users\shriraksha\AppData\Roaming\Microsoft\Windows\Start Mename\Programs\Google Chrome.lnk')
                speak("Google chrome is opening now")
        
            if 'open zoom' in statement:
                os.startfile(r'C:\Users\shriraksha\AppData\Roaming\Microsoft\Windows\Start Mename\Programs\Zoom.lnk')
                speak("Google chrome is opening now")
                       

            elif 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)

            elif 'cricket' in statement:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)

            elif 'corona' in statement:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 namembers')
                time.sleep(6)

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
            if 'date' in statement:
                date()
            elif 'who are you' in statement or 'what can you do' in statement:
                    speak('I am '+name_assistant+' your personal assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra') 


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Abhhi  Sannayya")

            
            elif 'make a note' in statement:
                statement = statement.replace("make a note", "")
                note(statement)


            elif 'note this' in statement:    
                statement = statement.replace("note this", "")
                note(statement)           

            speak(results)


def change_name():

  global name_info

  name_info = name.get()
  file=open("Assistant_name", "w")
  file.write(name_info+"\n")
  file.close()

  name_entry.delete(0, END)


def change():
    
      global screen1
      screen1 = Toplevel(screen)
      screen1.title("Settings")
      screen1.geometry("300x250")
      
      global name
      global name_entry
      
      name = StringVar()

      Label(screen1, text = "Changes will take place if you ").pack()
      Label(screen1, text = "close the main window and open it again ").pack()
      Label(screen1, text = "").pack()  
      Label(screen1, text = "Current name: "+name_assistant).pack()
      Label(screen1, text = "Please enter your Virtual Assistant's name below").pack()    
      Label(screen1, text = "").pack()
      Label(screen1, text = "Name").pack()
     
      name_entry = Entry(screen1, textvariable =name)
      name_entry.pack()
      

      Label(screen1, text = "").pack()
      Button(screen1, text = "Ok", width = 10, height = 1, command = change_name).pack()


def info():
  screen2 = Toplevel(screen)
  screen2.title("Info")
  screen2.geometry("150x100")
  Label(screen2,text = "Created by Abhhi Sannayya").pack()
  Label(screen2, text = "For Makerspace").pack()


def main_screen():

      global screen
      screen = Tk()
      screen.title(name_assistant)
      screen.geometry("150x350")
      Label(text = name_assistant, bg = "grey", width = "300", height = "2", fg="white", font = ("Calibri", 15)).pack()
      Label(text = "").pack()
      photo1 = PhotoImage(file = "Microphone_on.png")
      Button(image=photo1, command = Process_audio).pack()
      Label(text = "").pack()
      photo2 = PhotoImage(file = "settings.png")
      Button(image=photo2, command =change).pack()
      Label(text = "").pack()
      Button(text ="Info", width = 20, height = 4, command = info).pack()

      screen.mainloop()


main_screen()