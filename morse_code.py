import sys
import RPi.GPIO as GPIO
import time



PIN = 40
DOT = "."
DASH = "-"
WS = " "
SPEED = 0.3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.LOW)

def translate_morse_code(input_str):
    """
    translate the input string into morse code
    :param input_str: string to translate
    """
    morse = []
    alphabet = get_alphabet()
    for char in input_str:
        morse.extend(convert_char(char, alphabet))

    emit_morse_code(morse)

def emit_morse_code(morse_code):
    for element in morse_code:
        print(element)
        if element == WS:
            emitWS()
        elif element == DOT:
            emitDot()
        elif element == DASH:
            emitDash()
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(3 * SPEED)


def emitDot():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(SPEED)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(SPEED)

def emitDash():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(3*SPEED)

def emitWS():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(7*SPEED)


def convert_char(input_char, alphabet):
    """
    convert a single character to morse code
    :param input_char: character to convert
    :param alphabet: cached alphabet
    :return: List of DOTs and/or DASHes
    """
    return alphabet.get(input_char.upper(), WS)


def get_alphabet():
    """
    build the alphabet
    :return:
    """
    return {
        "A": [DOT, DASH],
        "B": [DASH, DOT, DOT],
        "C": [DASH, DOT, DASH, DOT],
        "D": [DASH, DOT, DOT],
        "E": [DOT],
        "F": [DOT, DOT, DASH, DOT],
        "G": [DASH, DASH, DOT],
        "H": [DOT, DOT, DOT, DOT],
        "I": [DOT, DOT],
        "J": [DOT, DASH, DASH, DASH],
        "K": [DASH, DOT, DASH],
        "L": [DOT, DASH, DOT, DOT],
        "M": [DASH, DASH],
        "N": [DASH, DOT],
        "O": [DASH, DASH, DASH],
        "P": [DOT, DASH, DASH, DOT],
        "Q": [DASH, DASH, DOT, DASH],
        "R": [DOT, DASH, DOT],
        "S": [DOT, DOT, DOT],
        "T": [DASH],
        "U": [DOT, DOT, DASH],
        "V": [DOT, DOT, DOT, DASH],
        "W": [DOT, DASH, DASH],
        "X": [DASH, DOT, DOT, DASH],
        "Y": [DASH, DOT, DASH, DASH],
        "Z": [DASH, DASH, DOT, DOT],
        "0": [DASH, DASH, DASH, DASH, DASH],
        "1": [DOT, DASH, DASH, DASH, DASH],
        "2": [DOT, DOT, DASH, DASH, DASH],
        "3": [DOT, DOT, DOT, DASH, DASH],
        "4": [DOT, DOT, DOT, DOT, DASH],
        "5": [DOT, DOT, DOT, DOT, DOT],
        "6": [DASH, DOT, DOT, DOT, DOT],
        "7": [DASH, DASH, DOT, DOT, DOT],
        "8": [DASH, DASH, DASH, DOT, DOT],
        "9": [DASH, DASH, DASH, DASH, DOT],
        "&": [DOT, DASH, DOT, DOT, DOT],
        "'": [DOT, DASH, DASH, DASH, DASH, DOT],
        "@": [DOT, DASH, DASH, DOT, DASH, DOT],
        ")": [DASH, DOT, DASH, DASH, DOT, DASH],
        "(": [DASH, DOT, DASH, DASH, DOT],
        ":": [DASH, DASH, DASH, DOT, DOT, DOT],
        ",": [DASH, DASH, DOT, DOT, DASH, DASH],
        "=": [DASH, DOT, DOT, DOT, DASH],
        "!": [DASH, DOT, DASH, DOT, DASH, DASH],
        ".": [DOT, DASH, DOT, DASH, DOT, DASH],
        "-": [DASH, DOT, DOT, DOT, DOT, DASH],
        "+": [DOT, DASH, DOT, DASH, DOT],
        "?": [DOT, DOT, DASH, DASH, DOT, DOT],
        "/": [DASH, DOT, DOT, DASH, DOT],
    }


if __name__ == "__main__":
    translate_morse_code(sys.argv[1])


