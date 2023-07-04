def on_log_full():
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
datalogger.on_log_full(on_log_full)

def on_button_pressed_a():
    global logging
    logging = True
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global logging
    logging = False
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_received_value(name, value):
    global id2
    id2 = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
    basic.show_string("" + name + ":")
    basic.show_number(value)
    serial.write_value("" + str(id2) + ":" + "", value)
radio.on_received_value(on_received_value)

id2 = 0
logging = False
radio.set_group(47)
led.set_brightness(10)
logging = False
datalogger.set_column_titles("temperatura", "luce")
basic.show_icon(IconNames.NO)

def on_every_interval():
    if logging:
        datalogger.log(datalogger.create_cv("temperatura", input.temperature()),
            datalogger.create_cv("luce", input.light_level()))
loops.every_interval(60000, on_every_interval)
