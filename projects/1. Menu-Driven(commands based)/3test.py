# importing the helper libraries
import os

# code
name = input('\nHello! IIEC assistant here \nwhat should i call you...: ')
print('Its good to meet you Mr./Ms.: ' + name.upper())
# print('use help() to check the available commands\n')
while True:  
	# we're creating an infinitte loop for the input, 
	# until the command says exit.
	# note: need to enchance the menu (as of now we're only accepting the direct message from an user)
	user_input = input("\nam listening...(" + name.upper() + '): ')
	user_input = user_input.lower()


	# terminating condition is created,
	# used dailly vocabulary to validate the condition and break the infinite loop.
	# note: can add more words too. 
	if(('tail' in user_input) or ('discontinue' in user_input) or ('dis continue' in user_input) or ('abort' in user_input) or ('finish' in user_input) or ('end' in user_input) or ('close' in user_input) or ('exit' in user_input) or ('terminate' in user_input) or ('shutdown' in user_input) or ('shut down' in user_input) or ('cancel' in user_input) or ('quit' in user_input)):
		if(('not' in user_input) or ('no' in user_input) or ("don't" in user_input) or ('dont' in user_input) or ('do not' in user_input)):
			continue
		else:
			print('_'*49,'Hope you enjoyed our services. Visit Again!!','_'*49)
			break

	elif(('show' in user_input) or ('help' in user_input) or ('display' in user_input)):
		print('COMMANDS: `firefox`, `chrome`, `editor`, `camera`, `ubuntu-software`, `file explorer`, `calculator`, `calendar`, `libreoffice`, `libreoffice(presentation)`, `libreoffice(sheet)`, `libreoffice(word)`, `videos_list`, `screenshot`, `facebook`, `instagram`, `likedin`, `github`, `gmail`, `discord`, `slack`, `youtube`, `wikipedia`, `reddit`, `pinterest`, `playstore`, `quora`, `flipkart`, `amazon`')

	# currently am executing this code in ubuntu, so all the commands related to the ubuntu.
	# note: trying to develop the same for the windows commands to
	elif(('not' in user_input) or ('no' in user_input) or ("don't" in user_input) or ('dont' in user_input) or ('do not' in user_input)):
		print('_'*50,'as you requested, :', user_input, '_'*50)

	elif(('launch' in user_input) or ('start' in user_input) or ('initiate' in user_input)):
		if(('chrome' in user_input) or ('google chrome' in user_input) or ('googlechrome' in user_input) or ('google' in user_input)):
			if(('facebook' in user_input) or ('fb' in user_input) or ('face book')):
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
			elif True:
				os.system('google-chrome'+ user_input)
			else:
				os.system('google-chrome')

		elif(('firefox' in user_input) or ('fire fox' in user_input)):
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
				os.system('firefox')
		else:
			if(('camera' in user_input) or ('cam' in user_input) or ('photo' in user_input) or ('pic' in user_input) or ('picture' in user_input)):
				os.system('cheese')
			elif(('editor' in user_input) or ('notepad' in user_input) or ('sublime' in user_input) or ('notes' in user_input) or ('note' in user_input)):
				os.system('subl')
			elif(('ubuntu store' in user_input) or ('ubuntu software' in user_input) or ('store' in user_input)):
				os.system('ubuntu-software') 
			#elif(('files' in user_input) or ('file explorer' in user_input) or ('files explorer')):
			#	os.system('nautilus') 
			elif(('calc' in user_input) or ('calculator' in user_input)):
				os.system('gcalctool')
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

	elif(('clear' in user_input) or ('cls' in user_input)):
		os.system('clear')

	else:
		print('Do you want me to google search it')
		x = input('(Y/n) ?')
		x = x.lower()
		if(('y' in x) or ('yes') in x):
			os.system("google-chrome  "+user_input)
		else:
			print("I am still learning, try `help` for more info.")


