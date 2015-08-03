def checkio(time_string):
    ON, OFF = '.', '-'
    hour, minitue, second = ['{:0>2}'.format(x) for x in time_string.split(':')]
    convert = lambda x: x.replace('0', ON).replace('1', OFF)
    to_bin = lambda x: bin(int(x))[2:]
    binary = [to_bin(x) for x in hour + minitue + second]
    morse = convert('{:0>2} {:0>4} : {:0>3} {:0>4} : {:0>3} {:0>4}'.format(*binary))
    return morse


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
