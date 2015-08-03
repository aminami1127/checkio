import collections


def letter_queue(commands):
    que = collections.deque()
    for x in commands:
        if 'PUSH' in x:
            que.append(x[-1])
        elif 'POP' in x:
            try:
                que.popleft()
            except IndexError:
                continue
    return ''.join(list(que))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
