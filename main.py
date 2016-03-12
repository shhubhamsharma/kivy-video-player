from Tkinter import Tk
from tkFileDialog import askopenfilename
from kivy.uix.videoplayer import VideoPlayer
from kivy.app import App
import os
dirName = os.path.dirname(os.path.abspath(__file__))
bitmapDir = os.path.join(dirName, 'bitmaps')


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os



 # show an "Open" dialog box and return the path to the selected file

class HelloApp(App):
	def start( self ):
		if self.ct:
			raise 'cannot run another copy of vplayer'
		self.exitFlag= 0
		self.ct= thread.start_new_thread( self.readerLoop, () )
	def build(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		filename = askopenfilename()
		player=VideoPlayer(source=filename,state="play",options={'eos':'loop'})
		return player
		
if __name__ == '__main__':
#	Editor().run()
	HelloApp().run()
