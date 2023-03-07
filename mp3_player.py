# import required library to create gui and play music
import os
import tkinter as tkr
from tkinter.filedialog import askdirectory
import pygame



def main():
    #create gui for mp3 player
    music_player= tkr.Tk()
    music_player.title('Mp3 player')
    music_player.geometry('450x200')
    music_player.resizable(0,1)
    # get location of music dir
    mydir= askdirectory()
    #get  list of music files
    #set parameters , font, size, bold
    text_font=('Helvetica',12,'bold')
    background='yellow'
    #get  list of music files
    songs= os.listdir(mydir)
    #change directory for songs to be current diretory
    os.chdir(mydir)
    #create list box
    playlist= tkr.Listbox(music_player,font=text_font,bg=background, selectmode=tkr.SINGLE)
    for song in songs:
        pos=0
        playlist.insert(pos,song)
        pos+=1

    # intialise pygame
    pygame.init()
    pygame.mixer.init()
    #create functions to play,stop,pause and unpause
    #play
    var= tkr.StringVar()
    def  play():
        '''function that loads music based on current selection and plays'''
        pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
        var.set(playlist.get(tkr.ACTIVE))
        pygame.mixer.music.play()
    #stop
    def stop():
        '''function stops the music which is being played'''
        pygame.mixer.music.stop()

    #pause
    def pause():
        '''function pauses the music'''
        pygame.mixer.music.pause()

    #unpause
    def unpause():
        '''function unpause the music'''
        pygame.mixer.music.unpause()


    #create buttons for functions

    button1= tkr.Button(music_player,width=5,height=3, bg='blue',fg='white',font=text_font,text='play',command=play)
    button2 = tkr.Button(music_player,font=text_font,text='Stop',command=stop,bg='red',fg='white',width=5,height=3)
    button3 = tkr.Button(music_player,width=5,height=3,text='Pause',command=pause,bg='green',fg='white',font=text_font)
    button4= tkr.Button(music_player,width=5,height=3,font=text_font,text='Unpause',command=unpause,bg='purple',fg='white')

    # create objects on main window
    song_title= tkr.Label(music_player,font=text_font, textvariable=var)

    #place on main window
    
    song_title.pack(fill='both')
    button1.pack(fill='x')
    button2.pack(fill='x')
    button3.pack(fill='x')
    button4.pack(fill='x')
    playlist.pack(fill='both', expand='yes')
    music_player.mainloop()
    #create buttons for functions
    music_player.mainloop()

if __name__=='__main__':
    main()
