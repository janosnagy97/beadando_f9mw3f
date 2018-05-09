def EX6_withDictionary(str):
    dict = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'}

    t = ''
    if str[0] == '.' or str[0] == '-':
        for i in str.split(' '):
            for k,v in dict.items():
                if i == v:
                    t += k
    else:
        str = str.upper()
        for i in str:
            for k,v in dict.items():
                if i == k:
                    t += v
                    t += ' '
    return t

print(EX6_withDictionary(input('Leforditando szoveg: ')))
