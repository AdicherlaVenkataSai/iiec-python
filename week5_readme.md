## WEEK 5
### DAY 8 | 6 September | [8. Python 3 API and CGI](https://www.youtube.com/watch?v=p-9unDfaZCo)

**[Summary](https://www.linkedin.com/posts/iiec-rise_iiecrise-activity-6708415432400887809-o_ol/)**
-  To integrate voice with python we need few modules support to record the audio and use it. We're using API(Google/ Amazom) to convert the audio into text and feed it to the program we created, now the `command in voice out` worka as `voice in voice out`.
- Modules used `pyaudio` install it using `conda install pyaudio`, `speech_recoginition` install it using `pip install SpeechRecognition`, apart from these we need the respective modules to interact with the os.

    `MIC` --> `Source` --> `Audio` --> `Google API (/Amazon)` --> `Text` --> `To Program`

```
import speech_recognition as sr
# In the first place were importing the speech_recognition module, in order to use it multiple times and make easy of typing were using the concept of aliasing.
# aliasing is a concept were we can rename the actual name and use it multiple times.

r = sr.Recognizer()
# here were creating an instance of speech_recogition and using the Recognizer() function to recognize the audio.

sr.Microphone()
# this function connects with individual microphone as a device,here it uses pyaudio library to connect to mic, then we can record the audio.


with sr.Microphone() as source:
    print('am listening.....speak')
    audio = r.listen(source)
    print('done...')
# after the recording the audio (listen) - on's the mic, then save it, and turn off the mic.
# with key word is used to switch on and switch off, before and after the work respectively.(here it switch on mic when were talking and switch of the mic as soon as we stop).


type(audio)
# output its type as speech_recognition.AudioData

audio.frame_data
# We might be curious to look at the auido how its gonna store - its completely in binary format here is the small look at the data (its just a part of actual one)\xff\xba\x04\xbb\x04\xbb\xf8\xba\x0b\xbb\x19\xbb\x1c\xbb\x19\xbb"\xbb#\xbb\x19\xbb\r\xbb\x13\xbb\x18\xbb\x17\xbb\n\xbb\x06\xbb*\x


r.recognize_google(audio)
# this function enables us to use the google api to convert he audio back to text format, demo output 'hello how are you hello how are you hello how are you'

# we consider this output as an user input to the Menu Based program (voice in voice out).

# Note: Before try this code ensure all the requiremets are satisfied or not. 
```

