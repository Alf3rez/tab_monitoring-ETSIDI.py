#Herramienta de monitorizacion basica

#yIntroduccion de variables previas

import PySimpleGUI as sg
import psutil
import time
import GPUtil
import platform


sg.theme('BrownBlue') #Para elegir el tema de la ventana

    #Variables CPU

CPUus = psutil.cpu_percent(interval=1)
CPUfq = psutil.cpu_freq(percpu=False).current

    #Variables RAM

RAMus = psutil.swap_memory().percent
RAMused = psutil.swap_memory().used
RAMfree = psutil.swap_memory().free

    #Variables GPU
"""
GPUs = GPUtil.getGPUs()

gpu_load = f"{gpu.load*100}"
gpu_used_memory = f"{gpu.memoryUsed}"

GPUus = gpu_load
GPUmem = gpu_used_memory
"""

    #Variables Discos

DISKus = psutil.disk_usage('/').percent
Diskload = psutil.disk_usage('/').used
Diskfree = psutil.disk_usage('/').free

#Pestañas


tab1_layout =  [[sg.Text(f'CPU carga: {CPUus} %')], 
                [sg.Text(f'CPU frecuencia: {CPUfq*0.001} MHz')]
               ]

tab2_layout =  [[sg.Text(f'RAM carga: {RAMus} %')],
                [sg.Text(f'RAM utilizada: {RAMused*0.0000000009313225746:.2f} GB')],
                [sg.Text(f'RAM libre: {RAMfree*0.0000000009313225746:.2f} GB')]]
                
tab3_layout =  [[sg.Text(f'GPU uso: {CPUus} %')], #Esta con los valores de la CPU para poder seguir usando el código sin tener que poner 4 o 5 comentarios mas mientras averiguo como sacar datos de la GPU
                [sg.Text(f'GPU memoria: {CPUus} MB')]]

tab4_layout =  [[sg.Text(f'Disco carga: {DISKus} %')],
                [sg.Text(f'Disco utilizado: {Diskload*0.0000000009313225746:.2f} GB')],
                [sg.Text(f'Disco libre: {Diskfree*0.0000000009313225746:.2f} GB')]]


#Interfaz como tal

layout = [[sg.TabGroup([[sg.Tab('CPU', tab1_layout), sg.Tab('RAM', tab2_layout), sg.Tab('GPU', tab3_layout), sg.Tab('Discos', tab4_layout)]])],
              [sg.Button('Actualizar')], [sg.Button('Cerrar')]

]

#Bucle de la ventana

window = sg.Window('Monitoreo', layout)

while True:
    event, values =window.read()
    
    Seconds = time.localtime().tm_sec

    Timer = round(Seconds*0.1)
    
    if event ==sg.WIN_CLOSED or event == 'Cerrar' :
        break
        
#Intentando meter un temporizador en el bucle para actualizar los valores

  """  elif Timer == 5 :
        print('Hola') """
        
window.close(); del window

#Intento de añadir un icon tray para poder minimizarla en segundo plano

"""

import PySimpleGUIQt as sg

menu_def = ['BLANK', ['&Abrir', '---', '&Cerrar']]

tray = sg.SystemTray(menu=menu_def, filename=r'default_icon.ico')

while True:  # The event loop
    menu_item = tray.read()
    print(menu_item)
    if menu_item == 'Cerrar':
        break
    elif menu_item == 'Abrir':
        sg.popup('Menu item chosen', menu_item)
        
"""
