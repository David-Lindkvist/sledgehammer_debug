def on_bluetooth_connected():
    global connected
    basic.show_string("C")
    connected = 1
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    basic.show_string("D")
    connected = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    if connected == 1:
        bluetooth.uart_write_string("HELLO")
    else:
        basic.show_string("Connect me!")
input.on_button_pressed(Button.A, on_button_pressed_a)

delay = 0
connected = 0
hz = 100
bluetooth.start_uart_service()
basic.show_string("Connect me!")

def on_forever():
    global delay
    if connected == 1:
        signal = pins.analog_read_pin(AnalogPin.P0)
        bluetooth.uart_write_string("" + str(signal))
    delay = 1000 / hz
    basic.pause(delay)
basic.forever(on_forever)
