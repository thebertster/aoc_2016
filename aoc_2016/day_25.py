import itertools

program = [ "cpy a d", "cpy 15 c", "cpy 170 b", "inc d", "dec b", "jnz b -2", "dec c", "jnz c -5", "cpy d a", "jnz 0 0", "cpy a b", "cpy 0 a", "cpy 2 c", "jnz b 2", "jnz 1 6", "dec b", "dec c", "jnz c -4", "inc a", "jnz 1 -7", "cpy 2 b", "jnz c 2", "jnz 1 4", "dec b", "dec c", "jnz 1 -4", "jnz 0 0", "out b", "jnz a -19", "jnz 1 -21" ]

programCode = list(map(lambda c: c.split(" "), program))

registers = { 'a':0, 'b':0, 'c':1, 'd':0 }

for v in itertools.count(1):

    pc = 0
    registers['a'] = v
    output = 1
    print(v, end = " ", flush = True)

    while pc < len(programCode):
        #print("pc = %d" % pc, end=", ")
        #for r,v in registers.items():
        #    print("%s = %d" % (r,v), end=", ")
        #print("instr = %s" % program[pc])
        #input("")
    
        code = programCode[pc]

        if code[0] == "inc":
                registers[code[1]] += 1
        elif code[0] == "dec":
                registers[code[1]] -= 1
        elif code[0] == "cpy":
            if code[2].isalpha():
                if code[1].isalpha():
                    registers[code[2]] = registers[code[1]]            
                else:
                    registers[code[2]] = int(code[1])
        elif code[0] == "jnz":
            if code[1].isalpha():
                check = registers[code[1]]        
            else:
                check = int(code[1])
            if check != 0:
                if code[2].isalpha():
                    newpc = pc + registers[code[2]]
                else:
                    newpc = pc + int(code[2])
                if 0 <= newpc < len(program):
                    pc = newpc - 1
        elif code[0] == "tgl":
            if code[1].isalpha():
                toggle = pc+registers[code[1]]          
            else:
                toggle = pc+int(code[1])
            if 0 <= toggle < len(program):
                newCode = programCode[toggle]
                if len(newCode) == 2:
                    if newCode[0] == "inc":
                        newCode[0] = "dec"
                    else:
                        newCode[0] = "inc"
                if len(newCode) == 3:
                    if newCode[0] == "jnz":
                        newCode[0] = "cpy"
                    else:
                        newCode[0] = "jnz"
                programCode[toggle][0] = newCode[0]
        elif code[0] == "out":
            if code[1].isalpha():
                nextOut = registers[code[1]]    
            else:
                nextOut = int(code[1])

            if (output == 0 and nextOut == 1) or (output == 1 and nextOut == 0):
                output=nextOut
            else:
                print("NO!")
                break
        pc += 1

print()
print("Final state:")
for r,v in registers.items():
    print("%s = %d" % (r,v), end=", ")
