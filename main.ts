datalogger.onLogFull(function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.clearScreen()
})
radio.onReceivedValue(function (name, value) {
    id = radio.receivedPacket(RadioPacketProperty.SerialNumber)
    basic.showString("" + name + ":")
    basic.showNumber(value)
    serial.writeValue("" + id + ":" + name, value)
    datalogger.log(
    datalogger.createCV("name", name),
    datalogger.createCV("h2o", value)
    )
})
let id = 0
radio.setGroup(77)
led.setBrightness(15)
datalogger.setColumnTitles(
"name",
"h2o"
)
