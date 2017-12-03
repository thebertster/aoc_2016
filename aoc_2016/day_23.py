#program = ["cpy 1 a", "cpy 1 b", "cpy 26 d", "jnz c 2", "jnz 1 5", "cpy 7 c", "inc d", "dec c", "jnz c -2", "cpy a c", "inc a", "dec b", "jnz b -2", "cpy c b", "dec d", "jnz d -6", "cpy 13 c", "cpy 14 d", "inc a", "dec d", "jnz d -2", "dec c", "jnz c -5"]
program = [ "cpy a b", "dec b", "cpy a d", "cpy 0 a", "cpy b c", "inc a", "dec c", "jnz c -2", "dec d", "jnz d -5", "dec b", "cpy b c", "cpy c d", "dec d", "inc c", "jnz d -2", "tgl c", "cpy -16 c", "jnz 1 c", "cpy 81 c", "jnz 73 d", "inc a", "inc d", "jnz d -2", "inc c", "jnz c -5" ]

programCode = list(map(lambda c: c.split(" "), program))

registers = { 'a':12, 'b':0, 'c':1, 'd':0 }

pc = 0

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
    pc += 1

print()
print("Final state:")
for r,v in registers.items():
    print("%s = %d" % (r,v), end=", ")
