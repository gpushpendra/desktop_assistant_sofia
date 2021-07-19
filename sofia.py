import pyttsx3# package is used for convert speech to text
import speech_recognition as sr
import datetime , time
import os
import winrandom #to generate randome number
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit #to open any web application
import sys
import pyjokes
import subprocess, os
import pyautogui
import easygui
import smtplib, email
from email import encoders
from email.mime.base import  MIMEBase



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


engine = pyttsx3.init('sapi5')
voice= engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)

#function for text to voice
def speak(voice):           
    engine.say(voice)
    print(voice)
    engine.runAndWait()


    
#function to take voice input from user    
def take_query():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print('listining.......')
        r.paus_thershold = 5
        audio = r.listen(source, phrase_time_limit=5)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        query = query  
        print(f"user said:{query}")
        
    
    except Exception as e:
        speak("i am unable to listen you") 
        return "none "
    return query.lower()

def run():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print('listining.......')
        r.paus_thershold = 5
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        query = query  
        print(f"user said:{query}")
        return query.lower()

    except Exception as e:
        return "none "
    #return query.lower()    

# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    print(datetime.datetime.now().time().strftime("%I:%M %p"))
    if hour==0 or hour<=12:
        speak('good morning')
    elif hour>=12 or hour<=18:
        speak('good afternoon')
    else:
        speak('good evening')

    speak(" I am sofia your personal assistent.")
    speak("how may i help you?")

def countdown(t):	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1


        


if __name__=="__main__":
    wish()
    while True:
        query = take_query()  
        #logic building for tasks
        
        # this is query for plying song
        if 'play' in query:
            songname = query.replace('play','')
            
            
            if 'some song' in query: #to play random song avilable on Pc
                speak("playing random song" )
                music_folder="F:\\dj song\\mix"
                songs = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
                i = winrandom.range(len(songs)-1)
                os.startfile(os.path.join(music_folder,songs[i]))
                
            elif 'romantic song' in query:
                speak("playing romantic song ")
                music_folder="F:\ganaa"
                songs = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
                i = winrandom.range(len(songs)-1)
                os.startfile(os.path.join(music_folder,songs[i]))
                
             #to play song on youtube    
            else:
                speak("playing.."+ songname + " on youtube")
                pywhatkit.playonyt(songname)  
        
        elif "stop audio" in query:
            pyautogui.press('playpause')
            speak("audio paused")

        
        elif 'open' in query: 

            if 'editor' in query or 'notepad' in query:
                speak("opening notepad")
                os.system('C:\\Windows\\Start Menu\\Programs\\Notepad++.lnk')
                
            elif 'cmd' in query or 'query prompt' in query:
                speak("opening query prompt")
                os.system('start cmd')
                
            elif ' camera' in query:
                speak("opening camera")
                subprocess.run('start microsoft.windows.camera:' , shell=True)
        
            elif "youtube"in query:
                speak("Sir, What should i search on youtube")
                cm =take_query()  
                pywhatkit.playonyt(cm)


        #close notepade 
        elif 'close' in query:

            if"notepad" in query:
                speak("okay sir, closing notepad")
                os.system("taskill /f /im Notepad++.lnk ")
            
            elif 'cmd' in query or 'close query prompt' in query:
                speak("closing query prompt")
                os.system('exit cmd')

            
            elif"chrome" in query:
                speak("okay sir, closing chrome")
                os.system("taskill /f /im chrome.exe ")

            elif"camera" in query:
                speak("okay sir, closing camera")            
                subprocess.run('Taskkill /IM WindowsCamera.exe /F' , shell=True)
        

        elif "tell me about" in query  or "what is" in query or "who" in query or "where" in query:

            if "time" in query:
                hour = datetime.datetime.now().time().strftime("%I:%M %p")
                speak(hour)

            elif "are you" in query or"yourself" in query:
                speak("I am Sofia a desktop voice assistent, version '1.0.3'. I am programmed by Pushpendra Goswami. My work is to help and save time to peform computer task in day to day life.")
            
            elif "my ip address" in query:
                ip =get('https://api.ipify.org').text
                speak(f"your IP address is: {ip}")

            elif "my net speed" in query or "my internet speed" in query:
                speak("I am calculating")
                import speedtest
                st = speedtest.Speedtest()
                dnl= int(st.download()/8000)
                upl = int(st.upload()/8000)
                speak(f"sir we have {dnl}/kb per second download speed and {upl}/kb per second upload speed")

            elif "my location" in query or "we are" in query:
                speak("wait, i am finding location")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    #speak(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data =geo_requests.json()
                    #speak(geo_data)
                    city = geo_data['city']
                    state = geo_data['region']
                    country = geo_data['country']
                    speak(f"sir according to my search we are in {city} city of {state} state of {country}")
                except Exception as e:
                    speak("sorry sir, i am not able to find location")
                    pass

            else:
                speak("searching on wikipedia.....")
                query = query.replace("Tell me about", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia " + result)

        #to find a joke 
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke) # import pyjoke

        elif "take screenshot" in query:
            #name= input("write the file name:")
            speak("please wait, i am capturing screenshort")
            time.sleep(3)
            img = pyautogui.screenshot()
            speak("provide name for your screenshort")
            name =take_query()  
            img.save(f"{name}.png")
            speak(f"screenshot is saved sucessfull with the name of {name}")            

        elif "google"in query:
            speak("Sir, What should i search on google")
            cm =take_query()  
            webbrowser.open(f"{cm}")

        
        
        elif "power we have" in query or "battery status" in query or "power left" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            percentage = battery.percent
            speak(f"sir our system have  {percentage} percent power")
            if percentage>=75:
                speak ("we have enough power to continue our work")
            elif percentage<=75 and percentage>=40:
                speak ("we should connect charger to  charge battery")
            elif percentage<=40 and percentage>=15:
                speak ("we dont  have enough power to continue, please charge the system")
            else:
                speak ("we have very low power, please connect to charger otherwise system will shutdown soon")
        
        
        
        elif "switch window" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
            speak("window switched")

        elif "minimise window" in query:
            pyautogui.keyDown('win')
            pyautogui.press('m')
            time.sleep(1)
            pyautogui.keyUp('win')
            speak("window minimised")
        
        elif "restore window" in query:
            pyautogui.keyDown('win')
            pyautogui.keyDown('shift')
            pyautogui.press('m')
            time.sleep(1)
            pyautogui.keyUp('win')
            pyautogui.keyUp('shift')
            speak("window restore")

        elif "whatsapp message" in query:

            speak("please provide whatsapp number of sender")
            contact ="+91"+input("Type Here: ")
            hour = int(datetime.datetime.now().hour) 
            minute = int(datetime.datetime.now().minute+1)
            print(hour , minute )

            try:
                speak("Sir, What should i send")
                cm =take_query()  
                pywhatkit.sendwhatmsg(contact, cm , hour, minute)
                speak("message send succcessfully")

            except:
                speak("error")
        
        elif "email" in query or "mail" in query:
            speak("do you want to send attechment")
            query = take_query()  
            if "yes" in query or "ok" in query:
                email = input("your email id: ")
                password = input("Your Password: ")
                send_to_eamil = input("receivers mail id: ")
                speak("okay sir, what is the subject for this email")
                query = take_query()  
                subject = query
                speak("and sir what is message for this email")
                query2 =take_query()  
                message = query2
                speak("sir please select the file which you want to send as Attachment")
                file= easygui.fileopenbox()

                speak("please wait, i am sending email")

                msg = MIMEMultipart()
                msg['From'] = email
                msg["To"] = send_to_eamil
                msg["Subject"]= subject

                msg.attach(MIMEText(message, 'plain'))

                # setup the attachment
                filename = os.path.basename(file)
                attachment = open(file, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" %filename)

                msg.attach(part)

                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(email , password)
                message = msg.as_string()
                speak("whome should i send message, please enter email id")
                reciver = input("email id: ") 
                speak("and sir what is message for this email")
                query2 =take_query()  
                message = query2
                s.sendmail(email, reciver, message)
                s.quit()
                speak("mail send successfully")

            else:
                try:
                    email = input("your email id: ")
                    password = input("Your Password: ")
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    s.login(email,password)
                    message = "this is python generated code message agian"
                    speak("whome should i send message, please enter email id")
                    reciver = input() 
                    s.sendmail(email, reciver, message)

                    speak("mail send sussfully")
                except Exception as e:
                    print(e) 

                s.quit()
        


        elif "shut down" in query:
            speak("Shuting down system")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 5")

        elif "sleep mode" in query:
            speak("making sleep mode to system")
            os.system("rundll32.exe powrprof.dil,SetSuspendState 0,1,0")

        elif "i am done" in query or "no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()
        
        elif "please wait" in query:
            speak("ok sir!")
            countdown(int(10))
            
            


        elif "wait a minute" in query:
            speak("ok sir!")
            countdown(int(60))
            

        elif "go to sleep" in query or "not now" in query:
                speak("ok sir! i am going to sleep , when you need me please call")
                while True:
                    query=run()
                    if "sofia" in query or "listen" in query:
                        speak("yes sir, how may i help you?")
                        break
                continue            

        else:
            if  query.__eq__(" "):
                speak('speak again')
            else:
                speak('sir, this task is not define in my program, do you have other work')
            continue

        speak(" sir, do you have other work")
        #g-ginues, a-artificial, y- your, u-use
#a ginues artificial for your use
#a knowledeged realiaty inteligent  technology for you...... support of featured inteligent assistent
