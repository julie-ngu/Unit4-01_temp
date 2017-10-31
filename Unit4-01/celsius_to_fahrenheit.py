# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program converts a temperature in celsius that the user inputs to Fahrenheit

import ui

def calculate_fahrenheit(celsius_temperature):
    # calculates inputted temperature in celsius to fahrenheit
    
    fahrenheit_temperature = 1.8 * celsius_temperature + 32
    view['answer_label'].text = str(celsius_temperature) + " in Celsius is " + str(fahrenheit_temperature) + " in temperature."
    
def calculate_button_touch_up_inside(sender):
    # converts inputted celsius temperature to fahrenheit
    
    # input
    celsius = int(view['input_textfield'].text)
    
    calculate_fahrenheit(celsius)

view = ui.load_view()
view.present('sheet')
