instr = [ "swap letter a with letter d", "move position 6 to position 4", "move position 5 to position 1", "swap letter h with letter e", "rotate based on position of letter a", "move position 6 to position 2", "reverse positions 0 through 1", "rotate based on position of letter h", "rotate based on position of letter g", "rotate based on position of letter h", "reverse positions 4 through 7", "swap letter a with letter f", "swap position 2 with position 7", "move position 7 to position 5", "reverse positions 0 through 5", "rotate based on position of letter f", "rotate right 4 steps", "swap position 3 with position 0", "move position 1 to position 2", "reverse positions 4 through 6", "swap position 3 with position 5", "swap letter a with letter c", "swap position 5 with position 2", "swap position 7 with position 2", "move position 2 to position 5", "rotate based on position of letter h", "rotate right 2 steps", "swap position 3 with position 4", "move position 0 to position 1", "reverse positions 1 through 7", "reverse positions 1 through 4", "rotate based on position of letter b", "rotate right 7 steps", "rotate left 0 steps", "swap position 6 with position 1", "reverse positions 1 through 3", "reverse positions 0 through 3", "move position 0 to position 4", "rotate based on position of letter f", "reverse positions 0 through 7", "reverse positions 0 through 1", "move position 1 to position 7", "move position 7 to position 6", "rotate based on position of letter b", "reverse positions 3 through 5", "reverse positions 0 through 3", "swap letter c with letter h", "reverse positions 3 through 5", "swap position 3 with position 6", "swap letter d with letter g", "move position 5 to position 6", "swap position 6 with position 2", "rotate right 5 steps", "swap letter e with letter g", "rotate based on position of letter e", "rotate based on position of letter c", "swap letter g with letter e", "rotate based on position of letter b", "rotate based on position of letter b", "swap position 0 with position 2", "move position 6 to position 0", "move position 5 to position 0", "rotate left 2 steps", "move position 0 to position 5", "rotate left 7 steps", "swap letter b with letter g", "rotate based on position of letter d", "swap letter h with letter e", "swap letter d with letter c", "rotate based on position of letter f", "move position 5 to position 0", "rotate left 5 steps", "swap position 0 with position 7", "swap position 0 with position 3", "rotate left 4 steps", "rotate left 1 step", "rotate right 6 steps", "swap position 0 with position 1", "reverse positions 4 through 6", "reverse positions 4 through 6", "move position 6 to position 3", "move position 7 to position 4", "rotate right 4 steps", "swap letter g with letter d", "swap letter c with letter e", "swap letter e with letter h", "rotate right 5 steps", "rotate based on position of letter g", "rotate based on position of letter g", "rotate left 3 steps", "swap letter h with letter g", "reverse positions 0 through 4", "rotate right 4 steps", "move position 6 to position 4", "rotate based on position of letter c", "swap position 2 with position 6", "swap position 7 with position 2", "rotate right 1 step", "swap position 3 with position 1", "swap position 4 with position 6" ]

password = list("fbgdceah")

#instr = [ "swap position 4 with position 0", "swap letter d with letter b", "reverse positions 0 through 4", "rotate left 1 step", "move position 1 to position 4", "move position 3 to position 0", "rotate based on position of letter b", "rotate based on position of letter d" ]
#password = list("abcde")

'''

for i in instr:
    words = i.split(" ")

    if words[0] == "swap":
        if words[1] == "position":
            x = int(words[2])
            y = int(words[5])
            password[x], password[y] = password[y], password[x]
        elif words[1] == "letter":
            for c in range(len(password)):
                if password[c] == words[2]:
                    password[c] = words[5]
                elif password[c] == words[5]:
                    password[c] = words[2]
    elif words[0] == "rotate":
        if words[1] == "based":
            if words[6] in password:
                pos = password.index(words[6])
                rots = (pos+(2 if pos>=4 else 1)) % len(password)
                password = password[-rots:] + password[:-rots]
        else:
            rots = int(words[2])
            if words[1] == "left":
                password = password[rots:] + password[:rots]
            elif words[1] == "right":
                password = password[-rots:] + password[:-rots]

    elif words[0] == "reverse":
        x = int(words[2])
        y = int(words[4])
        password = password[:x] + list(reversed(password[x:y+1])) + password[y+1:]
    elif words[0] == "move":
        x = int(words[2])
        y = int(words[5])
        if y>x:
            password = password[:x] + password[x+1:y+1] + password[x:x+1] + password[y+1:]
        elif x>y:
            password = password[:y] + password[x:x+1] + password[y:x] + password[x+1:]

'''

for i in reversed(instr):
    words = i.split(" ")

    if words[0] == "swap":
        if words[1] == "position":
            x = int(words[2])
            y = int(words[5])
            password[x], password[y] = password[y], password[x]
        elif words[1] == "letter":
            for c in range(len(password)):
                if password[c] == words[2]:
                    password[c] = words[5]
                elif password[c] == words[5]:
                    password[c] = words[2]
    elif words[0] == "rotate":
        if words[1] == "based":
            if words[6] in password:
                pos = password.index(words[6])
                rots = [ 1, 1, 6, 2, 7, 3, 0, 4 ][pos]
                password = password[rots:] + password[:rots]
        else:
            rots = int(words[2])
            if words[1] == "right":
                password = password[rots:] + password[:rots]
            elif words[1] == "left":
                password = password[-rots:] + password[:-rots]

    elif words[0] == "reverse":
        x = int(words[2])
        y = int(words[4])
        password = password[:x] + list(reversed(password[x:y+1])) + password[y+1:]
    elif words[0] == "move":
        x = int(words[5])
        y = int(words[2])
        if y>x:
            password = password[:x] + password[x+1:y+1] + password[x:x+1] + password[y+1:]
        elif x>y:
            password = password[:y] + password[x:x+1] + password[y:x] + password[x+1:]

print("".join(password))