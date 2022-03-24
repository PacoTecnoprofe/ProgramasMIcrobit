Secuencia = ""

def on_button_pressed_a():
    global Secuencia
    Secuencia = "" + Secuencia + "A"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string(Secuencia)
    if Secuencia == "ABBA":
        pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Secuencia
    Secuencia = "" + Secuencia + "B"
input.on_button_pressed(Button.B, on_button_pressed_b)
