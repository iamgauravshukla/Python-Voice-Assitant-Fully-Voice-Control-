import wolframalpha

client = wolframalpha.Client("3647V2-7GHV2X2VL4")  # APi Key from Wolframalpha
import wikipedia                                   # Importing Wikipedia to Search Query
import PySimpleGUI as sg                           # Importing PysimpleGui for Custom Layout
import speech_recognition as sr                    # Importing Speech Recognitions for voice Input
import pyttsx3                                     # Importing pyttsx3 for text-to-speech conversion

#                       Intro
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume',1.0)
engine.say("Hello I am Beast Your Voice Assistance")
print("Hello I am Beast")
engine.say("Say Your Query")
print("Say Your Query")
engine.runAndWait()

g = sr.Recognizer() # creating our own recognizer instance

# Function to convert text to Voice
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    engine.say(command)
    engine.runAndWait()

# use the default microphone as the audio source
with sr.Microphone() as source2:
    g.adjust_for_ambient_noise(source2,duration=0.1)  # listen for 2 second to calibrate the energy threshold for ambient noise levels
    audio2 = g.listen(source2)

MyText = g.recognize_google(audio2)                   # recognize speech using Google Speech Recognition
MyText = MyText.lower()                                #converting input voice text to all lower case
query = "Your Query about "
SpeakText(query)
SpeakText(MyText)
waitMessage = "Please wait Boss i am searching for you."
print("Searching for your query about " + MyText)
SpeakText(waitMessage)

#     Adding Popup Window with Reddit Theme from Pysimple Gui
sg.theme('Reddit')
window = sg.Window('Beast : Your Personal Assistance')

#       Changing  Speech Rate % Volume
SearchEngine = pyttsx3.init()  # object creation
SearchEngine .setProperty('rate', 180)
SearchEngine.setProperty('volume',1.0)


# Different Try & Except blocks to search the most accurate result from Wolfram & Wikipedia
try:
    wiki_res = wikipedia.summary(MyText, sentences=2)
    res = client.query(MyText)
    wolfram_res = next(res.results).text
    sg.PopupNonBlocking("Wolfram Result : " + wolfram_res, "Wikipedia Result :" + wiki_res)
    SearchEngine.say(wolfram_res)
    SearchEngine.say(wiki_res)

except wikipedia.exceptions.DisambiguationError:
    res = client.query(MyText)
    wolfram_res = next(res.results).text
    sg.PopupNonBlocking("Wolfram Result : " + wolfram_res)
    SearchEngine.say(wolfram_res)

except wikipedia.exceptions.PageError:
    res = client.query(MyText)
    wolfram_res = next(res.results).text
    sg.PopupNonBlocking("Wolfram Result : " + wolfram_res)
    SearchEngine.say(wolfram_res)

except:
    wiki_res = wikipedia.summary(MyText, sentences=2)
    sg.PopupNonBlocking("Wikipedia Result : " + wiki_res)
    SearchEngine.say(wiki_res)

SearchEngine.runAndWait()

window.close()
