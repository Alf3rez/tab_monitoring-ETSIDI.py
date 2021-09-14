#Herramienta de monitorizacion basica

#yIntroduccion de variables previas

import PySimpleGUI as sg
import psutil
def get_cpu_usage_pct():
return psutil.cpu_percent(interval=0.5);


sg.theme('BrownBlue') #Para elegir el tema de la ventana

#Pestañas

tab1_layout =  [[print('CPU uso: {} %'. format(get_cpu_usage_pct()))]]

tab2_layout =  [[sg.Text('RAM uso: {} %')]]

tab3_layout =  [[sg.Text('GPU uso: {} %')]]

tab4_layout =  [[sg.Text('Disco uso: {} %')]]

#Interfaz como tal

layout = [[sg.TabGroup([[sg.Tab('CPU', tab1_layout), sg.Tab('RAM', tab2_layout), sg.Tab('GPU', tab3_layout), sg.Tab('Discos', tab4_layout)]])],
              [sg.Button('Cerrar')]

]

#Bucle de la ventana

window = sg.Window('Monitoreo', layout)

while True:
    event, values =window.read()
    if event ==sg.WIN_CLOSED or event == 'Cerrar' :
        break

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