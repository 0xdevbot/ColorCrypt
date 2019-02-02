import sys
from collections import OrderedDict
import tkinter as tk
from tkinter import filedialog
import hashlib,binascii
from PIL import Image
import math





class Encrypt:
    def encrypt(self):
        password = None
        Pin = None
        while password == None:
            password = input('please enter a password\n')
        while Pin == None:
            Pin = input('please enter a 3-digit pin\n')
            if (int(Pin) < 0) or (int(Pin) > 4096):
                sys.exit("ERROR: Pin can not be greater then 4096")
        Upperpass = filter(str.isupper, password)
        Lowerpass = filter(str.islower, password)
        Numberpass = filter(str.isnumeric, password)
        lpwd = "".join(OrderedDict.fromkeys(Lowerpass))
        upwd = "".join(OrderedDict.fromkeys(Upperpass))
        npwd = "".join(OrderedDict.fromkeys(Numberpass))
        SPass = str(lpwd + upwd + npwd)
        spwd = password.strip(SPass)

        B = ' \ '
        BS = B.lstrip(' ')
        PinS = int(float(Pin) + 30)
        PinCL = int(float(Pin) + 10)
        PinN = int(float(Pin) + 20)
        Pinll = int(float(Pin))
        llPin = Pinll
        CLPin = PinCL
        NPin = PinN

        Set1lluni = [
            [llPin, 61],
            [llPin, 62],
            [llPin, 63],
            [llPin, 64],
            [llPin, 65],
            [llPin, 66],
            [llPin, 67],
            [llPin, 68],
            [llPin, 69],
            [41, 61],
            [42, 62],
            [43, 63],
            [44, 64],
            [45, 65],
            [46, 66],
            [llPin, 70],
            [llPin, 71],
            [llPin, 72],
            [llPin, 73],
            [llPin, 74],
            [llPin, 75],
            [llPin, 76],
            [llPin, 77],
            [llPin, 78],
            [llPin, 79],
            [41, 71]]

        Set1Clunit = [
            [CLPin, 41],
            [CLPin, 42],
            [CLPin, 43],
            [CLPin, 44],
            [CLPin, 45],
            [CLPin, 46],
            [CLPin, 47],
            [CLPin, 48],
            [CLPin, 49],
            [41, 41],
            [42, 42],
            [43, 43],
            [44, 44],
            [45, 45],
            [46, 46],
            [CLPin, 50],
            [CLPin, 51],
            [CLPin, 52],
            [CLPin, 53],
            [CLPin, 54],
            [CLPin, 55],
            [CLPin, 56],
            [CLPin, 57],
            [CLPin, 58],
            [CLPin, 59],
            [41, 51]]

        Set1ll = [
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z']

        Set1Cl = [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z']

        Set1Nuni = [
            [NPin, 30],
            [NPin, 31],
            [NPin, 32],
            [NPin, 33],
            [NPin, 34],
            [NPin, 35],
            [NPin, 36],
            [NPin, 37],
            [NPin, 38],
            [NPin, 39]
        ]

        Set1N = [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9'
        ]

        Set1S = [
            '`',
            '~',
            '!',
            '@',
            '#',
            '$',
            '%',
            '^',
            '&',
            '*',
            '(',
            ')',
            '-',
            '_',
            '+',
            '=',
            '[',
            '{',
            ']',
            '}',
            BS,
            '|',
            ';',
            ':',
            "'",
            '"',
            ',',
            '<',
            '.',
            '>',
            '/',
            '?',
            ' ',
        ]

        Set1Suni = [
            [PinS, 60],
            [45, 74],
            [PinS, 21],
            [PinS, 40],
            [PinS, 23],
            [PinS, 24],
            [PinS, 25],
            [65, 55],
            [PinS, 26],
            [41, 21],
            [PinS, 28],
            [PinS, 29],
            [44, 24],
            [46, 56],
            [42, 22],
            [44, 34],
            [42, 52],
            [42, 72],
            [44, 54],
            [64, 74],
            [43, 53],
            [43, 73],
            [42, 32],
            [41, 31],
            [PinS, 27],
            [PinS, 22],
            [43, 23],
            [43, 33],
            [45, 25],
            [45, 35],
            [46, 26],
            [46, 36],
            [PinS, 20],
        ]

        MI_path = None
        FILE_PATH = None

        while MI_path == None:
            print('please select your Master Image')
            root = tk.Tk()
            root.withdraw()
            MI_path = filedialog.askopenfilename(filetypes=(
                ('jpeg files', '*.jpg'),
                ('png files', '*.png'),
                ("All files", "*.*")))
        while FILE_PATH == None:
            print('please select the file you would like to encrypt')
            root = tk.Tk()
            root.withdraw()
            FILE_PATH = filedialog.askopenfilename(filetypes=(
                ('Text Files', '*.txt'),
                ("All files", "*.*")))

            with open(FILE_PATH) as BASE_TEXT:
                paz = BASE_TEXT.read().encode()
                salt = hashlib.pbkdf2_hmac('sha256', Pin.encode(), b'salt', 100000)
                soft_hash = hashlib.pbkdf2_hmac('sha256', paz, b'salt', 100000)
                _HASH_ = binascii.hexlify(soft_hash)
                print(_HASH_)
        I = 0
        x = _HASH_
        Y = int(math.log((int(len(x))), 2))
        X = int((len(x)) / Y)

        if ((len(x)) % 2) > 0:
            X = int(((len(x)) + 1) / Y) + 1

        Y = int(math.log((int(len(x))), 2))

        if ((len(x)) % 2) > 0:
            Y = int(math.log((int(len(x) + 1)), 2))

        MI = Image.open(MI_path)
        image_out = Image.new(MI.mode, (X + 1, Y))
        print(X)
        print(Y)
        pix_data = []
        print('Encrypting file...')

        while True:
            c = str(_HASH_)[I]
            if c in Set1ll:
                cIndexNum = Set1ll.index(c)
                cPixX = Set1lluni[cIndexNum][0]
                cPixY = Set1lluni[cIndexNum][1]
                pix = MI.load()
                Pixvalue = pix[cPixX, cPixY]
                pix_data.append(Pixvalue)
                I += 1

            if c in Set1Cl:
                cIndexNum = Set1Cl.index(c)
                cPixX = Set1Clunit[cIndexNum][0]
                cPixY = Set1Clunit[cIndexNum][1]
                pix = MI.load()
                Pixvalue = pix[cPixX, cPixY]
                pix_data.append(Pixvalue)
                I += 1

            if c in Set1N:
                pixelsN_out = ()
                cIndexNum = Set1N.index(c)
                cPixX = Set1Nuni[cIndexNum][0]
                cPixY = Set1Nuni[cIndexNum][1]
                pix = MI.load()
                Pixvalue = pix[cPixX, cPixY]
                PixvalueSTR = str(Pixvalue)
                pix_data.append(Pixvalue)
                pixelsN_out = ()
                I += 1

            if c in Set1S:
                cIndexNum = Set1S.index(c)
                cPixX = Set1Suni[cIndexNum][0]
                cPixY = Set1Suni[cIndexNum][1]
                pix = MI.load()
                Pixvalue = pix[cPixX, cPixY]
                pix_data.append(Pixvalue)
                I += 1

            if I == len(_HASH_):
                break

        print(pix_data)
        Pixdata = list(pix_data)
        print(Pixdata)
        image_out.putdata(Pixdata)
        image_out.save('temp.png')
        data = Image.open('temp.png').convert("RGBA")
        trans = list(data.getdata())

        for i, pixel in enumerate(trans):
            if pixel[:3] != (0, 0, 0):
                trans[i] = (trans[i][0], trans[i][1], trans[i][2], 0)

        print(trans)
        data.putdata(trans)
        data.save('output.png')
        print('Encryption done!')
        sys.exit(0)

        return 0