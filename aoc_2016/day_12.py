program = ["cpy 1 a", "cpy 1 b", "cpy 26 d", "jnz c 2", "jnz 1 5", "cpy 7 c", "inc d", "dec c", "jnz c -2", "cpy a c", "inc a", "dec b", "jnz b -2", "cpy c b", "dec d", "jnz d -6", "cpy 13 c", "cpy 14 d", "inc a", "dec d", "jnz d -2", "dec c", "jnz c -5"]

registers = { 'a':0, 'b':0, 'c':1, 'd':0 }

pc = 0

while pc < len(program):
    #print("pc = %d" % pc, end=", ")
    #for r,v in registers.items():
    #    print("%s = %d" % (r,v), end=", ")
    #print("instr = %s" % program[pc])
    
    code = program[pc].split(" ")
    if code[0] == "inc":
        registers[code[1]] += 1
    elif code[0] == "dec":
        registers[code[1]] -= 1
    elif code[0] == "cpy":
        if code[1].isdigit():
            registers[code[2]] = int(code[1])
        else:
            registers[code[2]] = registers[code[1]]
    elif code[0] == "jnz":
        if code[1].isdigit():
            check = int(code[1])
        else:
            check = registers[code[1]]
        if check != 0:
            pc += int(code[2]) - 1
    pc += 1

print()
print("Final state:")
for r,v in registers.items():
    print("%s = %d" % (r,v), end=", ")
