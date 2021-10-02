from tkinter import *
import webbrowser
import os

Ventana=Tk()
Ventana.geometry('525x475')
Ventana.title('Menú')
Ventana.resizable(0,0)
Ventana.config(bg='lavender')

#Botones
def Google():
    webbrowser.open('https://www.google.es')
BotonGoogle=Button(Ventana,bg='darkorange',fg='black',text='Google',command=Google)
BotonGoogle.place(width=100,height=100,x=25,y=50)

def Classroom():
    webbrowser.open('https://classroom.google.com')
BotonClassRoom=Button(Ventana,bg='forestgreen',fg='Black',text='Clasroom',command=Classroom)
BotonClassRoom.place(height=100,width=100,x=150,y=50)

def Gmail():
    webbrowser.open('https://mail.google.com')
BotonGmail=Button(Ventana,bg='red',fg='black',text='Gmail',command=Gmail)
BotonGmail.place(height=100,width=100,x=275,y=50)

def Drive():
    webbrowser.open('https://drive.google.com')
BotonDrive=Button(Ventana,bg='yellow',fg='black',text='Drive',command=Drive)
BotonDrive.place(height=100,width=100,x=400,y=50)

def Github():
    webbrowser.open('https://github.com')
BotonGithub=Button(Ventana,bg='Black',fg='White',text='Github',command=Github)
BotonGithub.place(height=100,width=100,x=25,y=175)

def YouTube():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
BotonYouTube=Button(Ventana,bg='darkred',fg='White',text='YouTube',command=YouTube)
BotonYouTube.place(height=100,width=100,x=150,y=175)

def StackOverflow():
    webbrowser.open('https://es.stackoverflow.com')
BotonYouTube=Button(Ventana,bg='chocolate',fg='White',text='StackOverflow',command=StackOverflow)
BotonYouTube.place(height=100,width=100,x=275,y=175)

def ElLadodelMal():
    webbrowser.open('https://www.elladodelmal.com')
BotonStackOverflow=Button(Ventana,bg='gray',fg='white',text='LadoDelMal',command=ElLadodelMal)
BotonStackOverflow.place(height=100,width=100,x=400,y=175)

def Apagado():
    os.system('shutdown -s')
BotonApagado=Button(Ventana,bg='fuchsia',fg='yellow',text='APAGAR',command=Apagado)
BotonApagado.place(width=200,height=100,x=41,y=300)

def Reinicio():
    os.system('shutdown -r')
BotonReincio=Button(Ventana,bg='Blue',fg='Yellow',text='REINICIAR',command=Reinicio)
BotonReincio.place(width=200,height=100,x=282,y=300)

Ventana.mainloop()