#!/usr/bin/python2
from sys import argv
import wave

def binaryMessage(message):
   binarymessage = ''
   for c in message:
      binarymessage += bin(ord(c))[2:].zfill(8)
   return binarymessage

def changelsb(c, value):
   c = (c[:7] + value).zfill(8)
   return c

def hide(audiofile):
   audio = wave.open(audiofile, 'r')
   message = raw_input("Enter message: ")
   binarymessage = binaryMessage(message)
   nframes = audio.getnframes()
   naudio = wave.open('n' + audiofile, 'w')
   naudio.setparams(audio.getparams())
   messagepos, pos, i = 0, 0, 0
   snumber = input('Enter a "security" number: ')
   for f in xrange(nframes):
      frame = audio.readframes(f)
      for c in frame:
	 if i > snumber:
            if messagepos < len(binarymessage) and pos % * == 0:
               cbinary = bin(ord(c))[2:].zfill(8)
               cbinary = changelsb(cbinary, binarymessage[messagepos])
               c = chr(int(cbinary, 2))
               messagepos += 1
            pos += 1
         i += 1
         naudio.writeframesraw(c)
   naudio.close()
   audio.close()
   print "The message is hidden in n%s." %audiofile

try:
   audiofile = argv[1]
except:
   audiofile = raw_input("Wave file: ")

hide(audiofile)
