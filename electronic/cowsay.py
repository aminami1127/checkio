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
    rows, i = [''], 0
    words = text.split(' ')
    for w in words:
        if len(rows[i]) + len(w) >= MAX_ROW:
            i += 1
            rows.append('')
        rows[i] += w if not rows[i] else ' ' + w
    return rows


def cowsay(text):
    if len(text) <= MAX_ROW:
        quote = r'''
 {}
< {} >
 {}'''
        width = len(text) + 2
        return quote.format(TOP * width, text, BOTTOM * width) + COW
    else:
        quote = r'''
 {}
{}
 {}'''
        width = MAX_ROW + 2
        rows = make_rows(text)
        for i, row in enumerate(rows):
            if i == 0:
                rows[i] = BORDERS[0] + ' ' + rows[i].ljust(MAX_ROW) + ' ' + BORDERS[1]
            elif i == len(rows) - 1:
                rows[i] = BORDERS[1] + ' ' + rows[i].ljust(MAX_ROW) + ' ' + BORDERS[0]
            else:
                rows[i] = BORDERS[2] + ' ' + rows[i].ljust(MAX_ROW) + ' ' + BORDERS[2]
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
    #assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    import pdb;pdb.set_trace()
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do ' 'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    # assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
