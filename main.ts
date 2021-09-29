bluetooth.onBluetoothConnected(function () {
    connected = 1
    basic.showLeds(`
        . # # . .
        # . . # .
        # . . . .
        # . . # .
        . # # . .
        `)
})
bluetooth.onBluetoothDisconnected(function () {
    connected = 0
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
})
input.onButtonPressed(Button.A, function () {
    let signal: number;
signal = pins.analogReadPin(AnalogPin.P2)
    basic.showNumber(signal)
})
let delay = 0
let connected = 0
let hz = 500
bluetooth.startUartService()
basic.forever(function () {
    let signal: number;
if (connected == 1) {
        signal = pins.analogReadPin(AnalogPin.P2)
        bluetooth.uartWriteLine("" + signal + "")
    }
    delay = 1000 / hz
    basic.pause(delay)
})
