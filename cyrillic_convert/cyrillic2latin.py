# -*- coding: utf-8 -*-


# run with python2

def convert(text):
    replacements = {

        # small case letters 34
        u'\u0430': 'a', #a
        u'\u0431': 'b',
        u'\u0432': 'v',
        u'\u0433': 'g',
        u'\u0434': 'd',
        u'\u0435': 'e',
        u'\u0436': 'j',
        u'\u0437': 'z',
        u'\u0438': 'i',
        u'\u0439': 'y',
        u'\u043A': 'k',
        u'\u043B': 'l',
        u'\u043C': 'm',
        u'\u043D': 'n',
        u'\u043E': 'o',
        u'\u043F': 'p',
        u'\u0440': 'r',
        u'\u0441': 's',
        u'\u0442': 't',
        u'\u0443': 'u',
        u'\u0444': 'f',
        u'\u0445': 'x',
        u'\u0446': 'S',
        u'\u0447': 'ch',
        u'\u0448': 'sh',
        u'\u044A': u'\u2019', # tutuq belgisi
        u'\u044C': '',
        u'\u044D': 'e',
        u'\u044E': 'yu',
        u'\u044F': 'ya',
        u'\u045E': u'\u006F' + u'\u2018', # o' harfi
        u'\u0493': u'\u0047' + u'\u2018', # g'
        u'\u049B': 'q',
        u'\u04B3': 'h', 
        u'\u0451': 'yo',

        # upper case
        u'\u0410': 'A', #a
        u'\u0411': 'B',
        u'\u0412': 'V',
        u'\u0413': 'G',
        u'\u0414': 'D',
        u'\u0415': 'E',
        u'\u0416': 'J',
        u'\u0417': 'Z',
        u'\u0418': 'I',
        u'\u0419': 'Y',
        u'\u041A': 'K',
        u'\u041B': 'L',
        u'\u041C': 'M',
        u'\u041D': 'N',
        u'\u041E': 'O',
        u'\u041F': 'P',
        u'\u0420': 'R',
        u'\u0421': 'S',
        u'\u0422': 'T',
        u'\u0423': 'U',
        u'\u0424': 'F',
        u'\u0425': 'X',
        u'\u0426': 'S',
        u'\u0427': 'Ch',
        u'\u0428': 'Sh',
        u'\u042A': u'\u2019', # tutuq belgisi
        u'\u042C': '',
        u'\u042D': 'E',
        u'\u042E': 'Yu',
        u'\u042F': 'Ya',
        u'\u040E': u'\u1d0f' + u'\u2018', # o' harfi
        u'\u0492': u'\u0262' + u'\u2018', # g'
        u'\u049A': 'Q',
        u'\u04B2': 'H', 
        u'\u0401': 'Yo',

    }
    text = "".join([replacements.get(c, c) for c in text])
    return text


