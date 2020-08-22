"""
Code is developed on Ubuntu OS
Created by: VenkataSai Adicherla 
Time: 11:00 am 22 August (updated)
Guidance: Mr. Vimal Daga Sir (IIEC-RISE) 
Feel free to download the code and check it
Any errors or questions can contact me(details in my git profile)

Note:  Check the requirements.txt file before executing the code
"""

# importing the helper libraries
import os 
from pyttsx3 import speak 
import pyjokes

# code begins from here
# snippet to control the voice rate and volume, can adjust by changing newVoiceRate, newVolume.
import pyttsx3
voiceEngine = pyttsx3.init()
rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
newVoiceRate,newVolume =  160, 0.3
voiceEngine.setProperty('rate', newVoiceRate)
voiceEngine.setProperty('volume', newVolume)

# sinppet to greet 
import time
currentTime = int(time.strftime('%H'))   

if currentTime < 12 :
     speak('Good morning')
if currentTime > 12 :
     speak('Good afternoon')
if currentTime > 18 :
     speak('Good evening')


speak("I am Tau your virtual personal assistant" + "    ")
speak("what do people call you")
name = input("what do people call you: ")
speak("It's great to interact with you      "+name)
speak("try help to know what all i can do")
#print('I can server these commands better:\n', '-'*140 ,'\n`firefox`, `chrome`, `editor`, `camera`, `ubuntu-software`, `calendar`, `libreoffice`, `libreoffice(presentation)`, `libreoffice(sheet)`, `libreoffice(word)`, `videos_list`, `screenshot`, `facebook`, `instagram`, `likedin`, `github`, `gmail`, `discord`, `slack`, `youtube`, `wikipedia`, `reddit`, `pinterest`, `playstore`, `quora`, `flipkart`, `amazon` \n', '-'*140)


while True:

	user_input = input("am listening...	(" + name.upper() + "): ")
	user_input = user_input.lower()

	'''system_cmd = ['camera', 'cam', 'photo', 'pic', 'picture', 'pictures', 'editor', 'sublime', 'sublime editor', 'notepad', 'notes', 'note', 'ubuntu store', 'ubuntu softwares', 'store', 'application store', 'apps store', 'what day it is', 'today', 'cal', 'excel sheet', 'sheets', 'libreoffice sheets', 'libreoffice calc', 'word', 'libreoffice word','libreoffice writer', 'ppt', 'presentation', 'libreoffice ppt', 'libreoffice impress', 'screen shots', 'screen shot', 'screeshot']

	for cmd in system_cmd:
		if system_cmd[cmd] in user_input:'''

	# terminating condition is created,
	# used daily vocabulary to validate the condition and break the infinite loop.
	# note: can add more words too. 
	if(('tail' in user_input) or ('discontinue' in user_input) or ('dis continue' in user_input) or ('abort' in user_input) or ('finish' in user_input) or ('end' in user_input) or ('close' in user_input) or ('exit' in user_input) or ('terminate' in user_input) or ('shutdown' in user_input) or ('shut down' in user_input) or ('cancel' in user_input) or ('quit' in user_input)):
		if(('not' in user_input) or ('no' in user_input) or ("don't" in user_input) or ('dont' in user_input) or ('do not' in user_input)):
			speak("I am clever enough to understand somethings, try help to more about me")
			continue
		else:
			speak('Hope I served you better. Visit Again' + name)
			print('_'*140)
			break


	# condition to check the help commands 
	elif(('show' in user_input) or ('help' in user_input) or ('display' in user_input)):
		speak('I can perform this for you')
		print('1. for website search use <site-name>.com  \n2. use `clear` command to clear the screen \n3.commands\n', '-'*140 ,'\n`firefox`, `chrome`, `editor`, `camera`, `ubuntu-software`, `calendar`, `libreoffice`, `libreoffice(presentation)`, `libreoffice(sheet)`, `libreoffice(word)`, `videos_list`, `screenshot`, `facebook`, `instagram`, `likedin`, `github`, `gmail`, `discord`, `slack`, `youtube`, `wikipedia`, `reddit`, `pinterest`, `playstore`, `quora`, `flipkart`, `amazon` \n', '-'*140)


	# condition to initiates all the commands
	# it overcome the bug `not to do command`, in such it speaks out `as you requested.......`
	# else it does the operation,  here you can choose chrome or fire fox
	# currently fire fox based aren't working properly 
	elif(('launch' in user_input) or ('start' in user_input) or ('initiate' in user_input) or('search' in user_input)):
		if(('not' in user_input) or ('no' in user_input) or ("don't" in user_input) or ('dont' in user_input) or ('do not' in user_input)):

			speak('as you requested' + user_input)

		else:
			if(('chrome' in user_input) or ('google chrome' in user_input) or ('googlechrome' in user_input) or ('google' in user_input)):

			
				speak('Launching  Please wait')
				if(('facebook' in user_input) or ('fb' in user_input) or ('face book'in user_input)):
					os.system('google-chrome  facebook.com')
				elif(('instagram' in user_input) or ('insta gram' in user_input) or ('ig' in user_input) or ('insta' in user_input)):
					os.system('google-chrome instagram.com')
				elif(('linkedin' in user_input) or ('linked in' in user_input)):
					os.system('google-chrome likedin.com')
				elif(('github' in user_input) or ('git hub' in user_input) or ('git' in user_input)):
					os.system('google-chrome github.com')
				elif(('gmail' in user_input) or ('g mail' in user_input)):
					os.system('google-chrome gmail.com')
				elif(('discord' in user_input) or ('discord channel' in user_input)):
					os.system('google-chrome discord.com')
				elif(('slack' in user_input) or ('slack channel' in user_input)):
					os.system('google-chrome slack.com')
				elif(('youtube' in user_input) or ('you tube' in user_input) or ('u tube' in user_input)):
					os.system('google-chrome youtube.com')
				elif(('wikipedia' in user_input) or ('wiki' in user_input)):
					os.system('google-chrome en.wikipedia.org')
				elif(('reddit' in user_input) or ('red dit' in user_input)):
					os.system('google-chrome reddit.com')
				elif(('pinterest' in user_input)):
					os.system('google-chrome pinterest.com')
				elif(('play store' in user_input) or ('google play store'in user_input) or ('playstore' in user_input)):
					os.system('google-chrome play.google.com')
				elif(('quora' in user_input)):
					os.system('google-chrome quora.com')
				elif(('flipkart' in user_input) or ('flip kart'in user_input)):
					os.system('google-chrome flipkart.com')
				elif(('amazon' in user_input)):
					os.system('google-chrome amazon.com')
				else:
					# if isn't available pre-definedly, pop ups the chrome browser to search for youself
					speak(" I am sorry, I couldn't understand, why don't you search it here")
					os.system('google-chrome')


			# note firefox browser operations aren't working properly		

			elif(('firefox' in user_input) or ('fire fox' in user_input)):

				speak('Launching  Please wait')

				if(('facebook' in user_input) or ('fb' in user_input) or ('face book')):
					os.system('firefox  facebook.com')
				elif(('instagram' in user_input) or ('insta gram' in user_input) or ('ig' in user_input) or ('insta' in user_input)):
					os.system('firefox instagram.com')
				elif(('linkedin' in user_input) or ('linked in' in user_input)):
					os.system('firefox likedin.com')
				elif(('github' in user_input) or ('git hub' in user_input) or ('git' in user_input)):
					os.system('firefox github.com')
				elif(('gmail' in user_input) or ('g mail' in user_input)):
					os.system('firefox gmail.com')
				elif(('discord' in user_input) or ('discord channel' in user_input)):
					os.system('firefox discord.com')
				elif(('slack' in user_input) or ('slack channel' in user_input)):
					os.system('firefox slack.com')
				elif(('youtube' in user_input) or ('you tube' in user_input) or ('u tube' in user_input)):
					os.system('firefox youtube.com')
				elif(('wikipedia' in user_input) or ('wiki' in user_input)):
					os.system('firefox en.wikipedia.org')
				elif(('reddit' in user_input) or ('red dit' in user_input)):
					os.system('firefox  reddit.com')
				elif(('pinterest' in user_input)):
					os.system('firefox pinterest.com')
				elif(('play store' in user_input) or ('google play store'in user_input) or ('playstore' in user_input)):
					os.system('firefox  play.google.com')
				elif(('quora' in user_input)):
					os.system('firefox quora.com')
				elif(('flipkart' in user_input) or ('flip kart'in user_input)):
					os.system('firefox flipkart.com')
				elif(('amazon' in user_input)):
					os.system('firefox amazon.com')
				else:
					# if isn't available pre-definedly, pop ups the chrome browser to search for youself
					speak(" I am sorry, I couldn't understand, why don't you search it here")
					os.system('firefox')

			# above discussed all are web based commmands
			# here comes the system based, i had used only few beacuse of lack of applications i didn't test
			# mentioned are tested and perfeclty working

			else:
				if(('camera' in user_input) or ('cam' in user_input) or ('photo' in user_input) or ('pic' in user_input) or ('picture' in user_input)):
					os.system('cheese')
				elif(('editor' in user_input) or ('notepad' in user_input) or ('sublime' in user_input) or ('notes' in user_input) or ('note' in user_input)):
					os.system('subl')
				elif(('ubuntu store' in user_input) or ('ubuntu software' in user_input) or ('store' in user_input)):
					os.system('ubuntu-software') 
			# commented them because they are mis behaving sometimes.		
			#elif(('files' in user_input) or ('file explorer' in user_input) or ('files explorer')):
			#	os.system('nautilus') 
			#elif(('calc' in user_input) or ('calculator' in user_input)):
			#	os.system('gcalctool')
				elif(('what day it is' in user_input) or ('day' in user_input)):
					os.system('zenity --calendar') 
				elif(('libreoffice' in user_input) or ('libre office' in user_input)):
					os.system('libreoffice') 
				elif(('ppt' in user_input) or ('presentation' in user_input) or ('libreoffice(presentation)' in user_input) or ('libreoffice(ppt)' in user_input)):
					os.system('libreoffice --impress')
				elif(('sheet' in user_input) or ('excel sheet' in user_input) or ('excelsheet' in user_input) or ('libreoffice(sheet)' in user_input)):
					os.system('libreoffice --calc') 
				elif(('word' in user_input) or ('libreoffice(word)' in user_input)):
					os.system('libreoffice --writer')
				elif(('videos_list' in user_input) or ('videos list' in user_input) or ('videos folder' in user_input)):
					os.system('xdg-open Videos')
				elif(('screenshot' in user_input) or ('screen shot' in user_input) or ('shot it' in user_input)):
					os.system('gnome-screenshot')
				else:
					speak("My machine had limited applications, so i didn't test these command")
					speak("why dont you search it here")
					os.system('google-chrome')

	# condition to clear the screen
	elif(('clear' in user_input) or ('cls' in user_input) or ('clean' in user_input)):
		if(('not' in user_input) or ('no' in user_input) or ("don't" in user_input) or ('dont' in user_input) or ('do not' in user_input)):
			speak("as you command ill not clean the screen")
			continue
		else:
			speak('Oops! the screen looks messy, ill clean it up')
			os.system('clear')

	# condtion to tell you a joke
	elif(('fun' in user_input) or ('joke' in user_input) or ('jokes' in user_input)):
		if(('not' in user_input) or ('no' in user_input) or ("don't" in user_input) or ('dont' in user_input) or ('do not' in user_input)):
			
			speak("It's strange you ask me not to joke")
			
			continue
		else:
			newVoiceRate,newVolume =  140, 0.3
			voiceEngine.setProperty('rate', newVoiceRate)
			speak(pyjokes.get_joke())
		
	# condtion to avoid null input
	elif not user_input :
		speak('Please write something')
		
	# it might be seem like a repeatative part
	# if any of the above conditions doesn't match, here were asking user manually to search in google
	# it acts according to the input and search else it print 'I am still learning....'
	else:
		speak('Do you want me to google search it')
		x = input('Do you want me to google search it (Y/n) ?')
		x = x.lower()
		if(('y' in x) or ('yes') in x):
			speak(" I am sorry, I couldn't understand, why don't you search it here")
			os.system('google-chrome')
		else:
			print("I am still learning, try 'help' for more info.")








