from collections import deque


increments = {
    0: (0, 1),      # going up
    1: (1, 0),      # going right
    2: (0, -1),     # going down
    3: (-1, 0)      # going left
}

class EmergencyHullRobot:
    def __init__(self, mem, phase_setting=None, startcolor = 0):
        self.mem = mem[:]
        self.ip = 0
        self.phase_setting = phase_setting
        self.relative_base = 0
        self.inputQ = deque(
            []) if phase_setting is None else deque([phase_setting])
        self.output = []
        self.outputs = []
        self.halted = False

        self.x, self.y = 0, 0
        self.visited = {}
        self.dir = 0

        self.visited[(0, 0)] = startcolor

    def getOperandValue(self, parameter, mode):
        if mode == 0:
            return self.mem[parameter]
        if mode == 1:
            return parameter
        if mode == 2:
            return self.mem[parameter + self.relative_base]

    def getAddress(self, parameter, mode):
        if mode == 0:
            return parameter
        if mode == 1:
            print("this shouldnt happen")
        if mode == 2:
            return parameter + self.relative_base

    def run(self, inputs=[]):  # inputs: list of inputs after phase_setting
        self.inputQ.extend(inputs)
        while (self.ip < len(self.mem)):
            op_code = self.mem[self.ip] % 100
            p1_mode = (self.mem[self.ip] // 100) % 10
            p2_mode = (self.mem[self.ip] // 1000) % 10
            p3_mode = (self.mem[self.ip] // 10000) % 10

            param1, param2, param3 = (None if self.ip+1 >= len(self.mem) else self.mem[self.ip+1]), \
                                     (None if self.ip+2 >= len(self.mem) else self.mem[self.ip+2]), \
                                     (None if self.ip+3 >= len(self.mem)
                                      else self.mem[self.ip+3])

            if op_code == 1:
                addend1, addend2 = self.getOperandValue(
                    param1, p1_mode), self.getOperandValue(param2, p2_mode)
                self.mem[self.getAddress(param3, p3_mode)] = addend1 + addend2
                self.ip += 4
            elif op_code == 2:
                mul1, mul2 = self.getOperandValue(
                    param1, p1_mode), self.getOperandValue(param2, p2_mode)
                self.mem[self.getAddress(param3, p3_mode)] = mul1 * mul2
                self.ip += 4
            elif op_code == 3:
                # print("3")
                inp = 0 if (
                    self.x, self.y) not in self.visited else self.visited[(self.x, self.y)]
                self.inputQ.append(inp)
                if len(self.inputQ) <= 0:
                    print("Error; input queue empty\n\n")
                val = self.inputQ.popleft()
                self.mem[self.getAddress(param1, p1_mode)] = int(val)

                self.ip += 2
            elif op_code == 4:
                # print("4")
                val = self.getOperandValue(param1, p1_mode)
                self.output.append(val)

                if len(self.output) >= 2:
                    self.outputs.append(self.output[:])
                    self.visited[(self.x, self.y)] = self.output[0]

                    if self.output[1] == 0:
                        self.dir -= 1
                    elif self.output[1] == 1:
                        self.dir += 1
                    if self.dir == 4:
                        self.dir = 0
                    if self.dir == -1:
                        self.dir = 3
                    incx, incy = increments[self.dir]

                    self.x, self.y = self.x + incx, self.y + incy
                    self.output.clear()

                self.ip += 2
                return val
            elif op_code == 5:
                param1, param2 = self.getOperandValue(
                    param1, p1_mode), self.getOperandValue(param2, p2_mode)
                if param1 != 0:
                    self.ip = param2
                else:
                    self.ip += 3
            elif op_code == 6:
                param1, param2 = self.getOperandValue(
                    param1, p1_mode), self.getOperandValue(param2, p2_mode)
                if param1 == 0:
                    self.ip = param2
                else:
                    self.ip += 3
            elif op_code == 7:
                param1, param2 = self.getOperandValue(
                    param1, p1_mode), self.getOperandValue(param2, p2_mode)
                self.mem[self.getAddress(
                    param3, p3_mode)] = 1 if param1 < param2 else 0
                self.ip += 4
            elif op_code == 8:
                param1, param2 = self.getOperandValue(
                    param1, p1_mode), self.getOperandValue(param2, p2_mode)
                self.mem[self.getAddress(
                    param3, p3_mode)] = 1 if param1 == param2 else 0
                self.ip += 4
            elif op_code == 9:
                param1 = self.getOperandValue(param1, p1_mode)
                self.relative_base += param1
                self.ip += 2
            elif op_code == 99:
                self.halted = True
                break
            else:
                print("invalid opcode", op_code)
                break
