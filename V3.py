from sre_parse import GLOBAL_FLAGS
from tkinter import ttk
from tkinter import *
import time
import serial
import tkinter
import tkinter as tk

def MDesplegable(event):  #Funcion MDesplegable
    global ser
    Puerto = event.widget.get()
    print("Conexion con exito al puerto: " + Puerto)
    ser = serial.Serial(Puerto, 9600)

#Variable serial
#ser = serial.Serial(Puerto, 9600) #Conexion Manual
#Funcion de envio
def Mover(aCommand):
    #Esta funcion envia el comando de angulos articulares al arduino para mover los servos a las posiciones deseadas
    aCommand = 0  #Soporte sin usar para permitir que la función funcione en vivo con la barra de escala
    ser.flushInput()
    ser.flushOutput()
    command = str(Inferior.get()) +','+ str(Izquierda.get()) +','+ str(Derecha.get()) +','+ str(Superior.get()) +'d'
    print(command)
    ser.write((command).encode())
    #espera hasta una respuesta si se encuentra desde el arduino
    OK = 'd'
    while (OK != 'd'):
        OK = ser.read(1)

def recordArmPost():
    #Esta función registra las posiciones actuales de la GUI y las coloca en un archivo TXT en el mismo directorio de este programa
    readPostCommand = str(Inferior.get()) + ',' + str(Izquierda.get()) + ',' + str(Derecha.get()) + ',' + str(Superior.get()) + ',' + str(Velocidad.get()) + '\n'
    recordFile = open('RegistroComando.txt', 'a')
    recordFile.write(readPostCommand)
    recordFile.close()

def recordPause():
    #Esta función registra pauseCommand y la coloca en un archivo TXT en el mismo directorio de este programa
    pauseCommand = 'Pausa' + '\n'
    recordFile = open('RegistroComando.txt', 'a')
    recordFile.write(pauseCommand)
    recordFile.close()

def playback():
    #Esta función lee el archivo de registro creado en recordArmPos() y envía los comandos al brazo para que se repita una secuencia de movimientos
    recordFile = open('RegistroComando.txt', 'r')
    Count = 1
    for line in recordFile:
        Count = Count + 1
        recordedCommand = line
        #enviar el comando al arduino usando otra función
        sendCommand(recordedCommand) #Arreglar
    print("Hecho")

#GUI
root = Tk()
#root.iconbitmap('Icono.ico')
root.title('Interfaz Grafica')
#Las barras de desplazamiento
armControl = Frame(root)
armControl.pack()
armLabel = Label(armControl,padx = 400, text = "Brazo Robotico Arduino", fg ="white", bg = "red")
armLabel.pack()
LabelFrameM = LabelFrame(armControl) #LFrame del menu desplegable
LabelFrameM.pack()
#Menu desplegable Puerto
DesplegableLabel = ttk.Combobox(LabelFrameM, values=["/dev/ttyACM0","COM8","/dev/ttyS0"], state='readonly')
DesplegableLabel.bind("<<ComboboxSelected>>", MDesplegable)
DesplegableLabel.set("Elige el Puerto:")
DesplegableLabel.pack(padx=5, pady=5)
#Pinza
SuperiorLabel = Label(armControl, text = "Pinza", padx = 100, borderwidth = 2, relief="ridge")
SuperiorLabel.pack()
Superior = Scale(armControl, from_= 0, to = 40, length = 300, orient = HORIZONTAL,tickinterval=20, command = Mover)
Superior.set(10)
Superior.pack()
#Imagen
Imglabel = Label(armControl)
Img = tkinter.PhotoImage(file="Servo.png")
Img = Img.subsample(4, 4)
Imglabel.config(image=Img)
Imglabel.pack()
#Inferior
InferiorLabel = Label(armControl, text = "Inferior", padx = 100, borderwidth = 2, relief="ridge")
InferiorLabel.pack()
Inferior = Scale(armControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Inferior.pack()
#Izquierda
IzquierdaControl = Frame(armControl)
IzquierdaControl.place(x=20, y=150)
IzquierdaLabel = Label(IzquierdaControl, text = "Izquierda", padx = 100, borderwidth = 2, relief="ridge")
IzquierdaLabel.pack()
Izquierda = Scale(IzquierdaControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Izquierda.set(100)
Izquierda.pack()
#Derecha
DerechaControl = Frame(armControl)
DerechaControl.place(x=605, y=150)
DerechaLabel = Label(DerechaControl, text = "Derecha", padx = 100, borderwidth = 2, relief="ridge")
DerechaLabel.pack()
Derecha = Scale(DerechaControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Derecha.set(140)
Derecha.pack()
#Velocidad
VelocidadLabel = Label(armControl, text = "Velocidad",padx = 100, borderwidth = 2, relief="ridge")  #TERMINAR SLIDER VELOCIDAD FALTA DEFINIR FUNCION, SCRIPT ARDUINO
VelocidadLabel.pack()
Velocidad = Scale(armControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Velocidad.set(0)
Velocidad.pack()

LabelFrameV = LabelFrame(armControl, text="Beta v0.1") #LFrame de nuevas funciones
LabelFrameV.pack()
#Btn en proceso......
BtnPausa = Button(LabelFrameV, text = "Pausa por Tiempo", command = recordPause)
BtnPausa.pack(padx=5, pady=5)
BtnRegistro = Button(LabelFrameV, text = "Posición de Registro", command = recordArmPost)
BtnRegistro.pack()
BtnReproduccion = Button(LabelFrameV, text = "Secuencia de Reproducción", command = playback)
BtnReproduccion.pack(padx=5, pady=5)


root.mainloop()