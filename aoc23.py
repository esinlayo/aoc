from IntcodeComputer import IntcodeComputer

def createMem(str): return list(map(int, str.strip("\n").split(",")))

def make_mac_output(machine):
    retnow = machine.run()
    if retnow == 'input':
        return
    retnow = machine.run()
    if retnow == 'input':
        return
    machine.run()
    return

machines = []
for i in range(50):
    mac = IntcodeComputer(createMem(open("aoc23.txt", "r").readline()), [i])
    machines.append(mac)

for i in range(50):
    print(machines[i], machines[i].inputQ)

def part1():
    while True:
        for i in range(50):
            machine = machines[i]
            
            make_mac_output(machine)
            
            dest, x, y = None, None, None
            if len(machine.output) == 3:
                dest, x, y = machine.output
                #print(machine.output)
                
                if 0 <= dest < 50:
                    machines[dest].inputQ.extend([x, y])
                if dest == 255:
                    print(y)
                    return
                machine.output.clear()
part1()










def isIdle(network):
    return all([len(mac.inputQ) == 0 or mac.inputQ[0] == -1 for mac in network])

def make_mac_output(machine):
    retnow = machine.run()
    if retnow == 'input':
        return
    retnow = machine.run()
    if retnow == 'input':
        return
    machine.run()
    return

machines = []
for i in range(50):
    mac = IntcodeComputer(createMem(open("aoc23.txt", "r").readline()), [i])
    machines.append(mac)
machines.extend([None for _ in range(256-50)])
machines[255] = IntcodeComputer(createMem(open("aoc23.txt", "r").readline()), [255])
nat = machines[255]
nat.run()

def part2():
    while True:
        for i in list(range(50)):
            machine = machines[i]

            make_mac_output(machine)

            if len(machine.output) == 3:
                dest, x, y = machine.output
                #print(f"machine {i} to {dest}: X={x}, Y={y}")
                
                if 0 <= dest < 50:
                    machines[dest].inputQ.extend([x, y])
                if dest == 255:
                    machines[dest].inputQ.clear()
                    machines[dest].inputQ.extend([x, y])

                
                if dest == 0 and i == 255:
                    print('wow')
                    
                machine.output.clear()
                    
        if isIdle(machines[:50]) and len(nat.inputQ) > 0:
            x, y = nat.inputQ
            nat.inputQ.clear()
            
            machines[0].inputQ.extend([x,y])
            print(f"machine {255} to {0}: X={x}, Y={y}")

part2()

