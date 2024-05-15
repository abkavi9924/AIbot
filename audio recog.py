import speech_recognition as sr
from gtts import gTTS
import pygame
from nltk.tokenize import word_tokenize


#Defining of Functions
def tokenize_text(text):
    return word_tokenize(text)

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    pygame.event.wait() 

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
#done with functions
book_reviews = {
    "Game Of Thrones": "This is a fantastic book with a gripping plot.",
    "book2": "An engaging read with well-developed characters.",
}


booknames = book_reviews.keys()
booktitle = None
user_input = get_audio()
user_input = user_input.lower()
print("You said:", user_input)


#loop to get book name from the dictionary
for i in booknames:
    j = i.lower()
    if j in user_input:
        print("True")
        booktitle = i
#loop ends

        
#get the review
review_text = book_reviews.get(booktitle)
tokens = tokenize_text(user_input)#Tokenize the User input(unnecessary as of now)
text_to_speech(review_text)#(Reading out the review)
