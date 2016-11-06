# Created by: Hamza Salman
# Created on: Novembor 2016
# Created for: ICS3U
# This program is a address program.

import ui

def print_mail_address(city, province, postal_code, street_address, apartment_number = ''): 
    #print mailing address, shows errors if not all required textfields are filled in.

    if city == '':
        view['city_label'].text = 'please enter city name *' 
    
    if street_address == '': 
         view['street_label'].text = 'please enter street name *' 
         
    if province == '':
        view['province_label'].text = 'please enter province name *' 
        
    if postal_code == '':
        view['postal_code_label'].text = 'please enter postal code *' 
        
    if city == '':
        view['output_label'].text = '' 
        
    elif street_address == '':
        view['output_label'].text = '' 
        
    elif province == '':
        view['output_label'].text = '' 
        
    elif postal_code == '':
        view['output_label'].text = '' 
        
    elif apartment_number == '': 
        view['output_label'].text = ('street: ' + street_address + ' city: ' + city + ' province: ' + province + ' postal code: ' + postal_code) 
        
    else: 
        view['output_label'].text = 'Apartment number: ' + apartment_number + (' street: ' + street_address + ' city: ' + city + ' province: ' + province + ' postal code: ' + postal_code)

def post_touch_up_inside(sender):

# when the button is pressed check what has been inputed, calles other function to show output. Sets all labels to blank the reassigns.

    view['city_label'].text = ''
    view['street_label'].text = '' 
    view['province_label'].text = '' 
    view['postal_code_label'].text = '' 
    view['output_label'].text = '' 
    enter_street_address = view['address_textfield'].text 
    enter_city = view['city_textfield'].text 
    enter_province = view['province_textfield'].text 
    enter_postal_code = view['postal_code_textfield'].text 
    enter_apartment_number = view['apartment_textfield'].text

    print_mail_address(enter_city,enter_province, enter_postal_code, enter_street_address, apartment_number = enter_apartment_number)

view = ui.load_view() 
view.present('fullscreen')
