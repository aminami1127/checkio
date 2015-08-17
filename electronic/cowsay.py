COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
TOP = '_'
BOTTOM = '-'
BORDERS = '/\\|'

MAX_ROW = 39


def make_rows(text):
    rows, num = [''], 0
    words = text.split(' ')
    for i, w in enumerate(words):
        # slice words that have over MAX_ROW characters
        if len(w) > MAX_ROW:
            words.insert(words.index(w) + 1, w[MAX_ROW:])
            w = w[:MAX_ROW]
        # if the word is first, don't append row
        if len(rows[num]) + len(w) >= MAX_ROW and i:
            num += 1
            rows.append('')
        rows[num] += w if not rows[num] else ' ' + w
    return rows


def cowsay(text):
    import re
    text = re.sub('\s+', ' ', text)
    if len(text) <= MAX_ROW:
        quote = r'''
 {}
< {} >
 {}'''
        width = len(text) + 2
    else:
        quote = r'''
 {}
{}
 {}'''
        rows = make_rows(text)
        width = max(len(x) for x in rows) + 2
        concat = lambda x, y, z: x + ' ' + y + ' ' + z
        for i, row in enumerate(rows):
            if i == 0:
                rows[i] = concat(BORDERS[0], rows[i].ljust(width - 2), BORDERS[1])
            elif i == len(rows) - 1:
                rows[i] = concat(BORDERS[1], rows[i].ljust(width - 2), BORDERS[0])
            else:
                rows[i] = concat(BORDERS[2], rows[i].ljust(width - 2), BORDERS[2])
        text = '\n'.join(rows)
    return quote.format(TOP * width, text, BOTTOM * width) + COW


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do ' 'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
