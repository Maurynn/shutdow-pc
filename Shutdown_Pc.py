from tkinter import *
from tkinter import ttk
import customtkinter
from tkinter import messagebox
import os

#FUNÇÃO DESLIGAR E REINICIAR
def desligar():
    return os.system("shutdown /s /t 1")

def reiniciar():
    return os.system("shutdown /r /t 1")

def aviso():
    messagebox.showinfo('ATENÇAÕ!!!','O COMPUTADOR SERÁ DESLIGADO\nEM ALGUNS MINUTOS...')

#CRONÔMETRO
def tick(validador=False, sec=None):
    if validador == False:
        sec = int(entrada.get())
        sec *= 60
    if sec == 0:
        cronometro.text_label['text'] = 'DESLIGANDO'
        return os.system("shutdown /s /t 1")
   
    else:
        
        mins, secs = divmod(sec, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        sec = sec - 1
        cronometro.text_label['text'] = timer
        label.after(1000, lambda: tick(True, sec))
#RESETAR        
def reset(validador=True):
    if validador == True:
        tempo = '00:00'
        cronometro.text_label['text'] = tempo
        
#MÓDULO CUSTOMTKINTER[ESTE MÓDULO DEIXA A INTERFACE MAIS MODERNA]
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#UI
app = customtkinter.CTk()
app.geometry("260x350")
app.title("Dev_by_Mauro")

frame = customtkinter.CTkFrame(master=app, width=250, height=150, corner_radius=10, border_width=1, border_color='cyan')
frame.pack(padx=10, pady=10, fill="both", expand=True)
frame2 = customtkinter.CTkFrame(master=app, width=250, height=50, corner_radius=10, border_width=1, border_color='cyan')
frame2.pack(padx=10, pady=10, fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=frame, text="SHUTDOWN PC", text_color='white', text_font='georgia')
label.pack(pady=6, padx=10)

button = customtkinter.CTkButton(
    master=frame, text="DESLIGAR", text_color='white', width=12, corner_radius=10, border_width=1, command=desligar)
button.pack(pady=5, padx=10)

button = customtkinter.CTkButton(
    master=frame, text="REINICIAR", text_color='white', width=12, corner_radius=10, border_width=1, command=reiniciar)
button.pack(pady=5, padx=10)

timer = customtkinter.CTkLabel(
    master=frame2, text="CRONÔMETRO:", text_color='white', text_font='georgia')
timer.pack(pady=6, padx=10)

entrada = customtkinter.CTkEntry(
    master=frame2, width=60, height=5, justify='center', text_font='system 8')
entrada.pack(pady=6, padx=10)

cronometro = customtkinter.CTkLabel(
    master=frame2, text='00:00', text_color='white', text_font='fixedsys 18')
cronometro.pack(pady=6, padx=10)
button = customtkinter.CTkButton(master=frame2, text="INICIAR",
                                 text_color='white', width=10, text_font='Bahnschrift 9', corner_radius=10, border_width=1, command=lambda:[tick(), aviso()])
button.pack(pady=6, padx=10)


app.mainloop()
