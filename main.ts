input.onButtonPressed(Button.A, function () {
    Secuencia = "" + Secuencia + "A"
})
input.onButtonPressed(Button.AB, function () {
    basic.showString(Secuencia)
    if (Secuencia == "ABBA") {
        servos.P0.setAngle(90)
        Secuencia = ""
    }
})
input.onButtonPressed(Button.B, function () {
    Secuencia = "" + Secuencia + "B"
})
let Secuencia = ""
servos.P0.setAngle(0)
