def digit_stack(commands):
    stack, result = [], 0
    for c in commands:
        if c.startswith('PUSH'):
            stack.append(int(c[-1]))
        elif c.startswith('POP'):
            result += stack.pop() if stack else 0
        elif c.startswith('PEEK'):
            result += stack[-1] if stack else 0
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
