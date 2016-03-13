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

class VideoPlayerApp(App):

	def build(self):
		
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		filename = askopenfilename(filetypes=[('All Types',('.webm','.drc','.gif', '.wmv',
		'.mov','.qt','.gifv','.rm','.rmvb',
		'.asf','.mp4','.mpg','.mp2',
		'.mpeg','.mpe','.mpv','.m2v','.m4v',
		'.svi','.3gp','.mxf','.3g2','.nsv','.roq',
		'.mkv','.vob','.ogv','.flv')),('WebM', '.webm'),('Dirac','.drc'),('GIF','.gif'),
		('Windows Media Video','.wmv'),('Quick time file Format','.mov'),
		('Quick Time FileFormat','.qt'),('Video Alternatives to GIF','.gifv'),
		('Raw Video Format','.yuv'),('RealMedia','.rm'),('RealMedia Variable Bytes','.rmvb'),('AdvancedSystems Formats','.asf'),('MPEG-4','.mp4'),('MPEG-4 Part 14','.mp4'),
		('MPEG-1','.mpg'),('MPEG-2','.mp2'),('MPEG','.mpeg'),('MPE','.mpe'),('MPV','.mpv'),	('MPEG-2 Video','.m2v'),('M4V','.m4v'),('SVI','.svi'),('3GPP','.3gp'),
		('MaterialExchange Format','.mxf'),('3GPP2','.3g2'),('Nullsoft Streaming Video','.nsv'),('ROQ','.roq'),	('Matroska','.mkv'),('Vob','.vob'),('Ogg','.ogv'), ('Flash Videos', '.flv')])
		#root = Tkinter.Tk()
		#fileName = tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the image as...")
		player=VideoPlayer(source=filename,state="play",options={'eos':'loop'})
		return player
		
if __name__ == '__main__':
#	Editor().run()
	VideoPlayerApp().run()
