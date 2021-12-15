import math as mt
import functions as fu

show_code_grid = True  # True / False

while True:
    option = input('Pick opction: press \'c\' to code or \'d\' to decode or \'e\' to exit ')
    if option == 'e':
        break;
    elif option == 'c':
        pass
    elif option == 'd':
        pass
    else:
        print('option error')
    while option == 'c' or option == 'd':
        input_text = input('Paste here text to code/decode: ')
        key = input('key: ')
        input_simplefied = ''.join(e for e in input_text if e.isalnum())
        input_simplefied = input_simplefied.upper()
        key_simplefied = ''.join(e for e in key if e.isalnum())
        key_simplefied = key_simplefied.upper()
        key_simplefied = key_simplefied + "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        key_simplefied = ''.join([j for i, j in enumerate(key_simplefied) if j not in key_simplefied[:i]])
        output_text = ''
        fu.key_square_fill(key_simplefied)

        lit1 = 0
        for i in range(mt.ceil(len(input_simplefied) / 2)):
            char1 = input_simplefied[lit1]
            if lit1 + 1 >= len(input_simplefied):
                char2 = 'X'
            else:
                char2 = input_simplefied[lit1 + 1]
            lit1 = lit1 + 2

            cord1 = fu.coordinates(char1)
            cord2 = fu.coordinates(char2)

            if option == 'c':
                output_text = output_text + fu.code(cord1, cord2)
            elif option == 'd':
                output_text = output_text + fu.decode(cord1, cord2)

        if show_code_grid == True:
            print(fu.playfair_grid + '')
            print('')

        print(output_text)
        print('')
        break;
