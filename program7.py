
def amplifier(line, input_signals, letter=None):
    i = 0
    output=None
    while (i<len(line)):
        #print(i)
        op_code = line[i]%100
        one_param_mode = (line[i] // 100) % 10
        two_param_mode = (line[i] // 1000) % 10
        thr_param_mode = (line[i] // 10000) % 10
        #print("----", i, line[i], op_code, one_param_mode, two_param_mode, thr_param_mode)
        if thr_param_mode != 0: print("WARANING")

        try:
            if op_code == 1:
                addend1 = line[i+1] if one_param_mode else line[line[i+1]]
                addend2 = line[i+2] if two_param_mode else line[line[i+2]]
                replace_pos = line[i+3] if not thr_param_mode else line[line[i+3]]
                line[replace_pos] = addend1 + addend2
                i+=4
            elif op_code == 2:
                mul1 = line[i+1] if one_param_mode else line[line[i+1]]
                mul2 = line[i+2] if two_param_mode else line[line[i+2]]
                replace_pos = line[i+3] if not thr_param_mode else line[line[i+3]]
                #print('rp',replace_pos, mul1, mul2)
                line[replace_pos] = mul1 * mul2
                i+=4
            elif op_code == 3:
                pos = line[i+1]
                val = input_signals.pop()
                line[pos] = int(val)
                #print(line[pos])
                i+=2
            elif op_code == 4:
                val = line[i+1]
                output=line[val]
                #print('OUTPUT', line[val])
                i+=2
            elif op_code == 5:
                param1, param2 = line[i+1:i+3]
                param1 = param1 if one_param_mode else line[param1]
                param2 = param2 if two_param_mode else line[param2]
                if param1 != 0: 
                    i = param2
                    continue
                i+= 3
            elif op_code == 6:
                param1, param2 = line[i+1:i+3]
                param1 = param1 if one_param_mode else line[param1]
                param2 = param2 if two_param_mode else line[param2]
                if param1 == 0: 
                    i = param2
                    continue
                i+= 3
            elif op_code == 7:
                param1, param2, param3 = line[i+1:i+4]
                param1 = param1 if one_param_mode else line[param1]
                param2 = param2 if two_param_mode else line[param2]
                param3 = param3 if not thr_param_mode else line[param3]
                line[param3] = 1 if param1 < param2 else 0
                i+= 4
            elif op_code == 8:
                param1, param2, param3 = line[i+1:i+4]
                param1 = param1 if one_param_mode else line[param1]
                param2 = param2 if two_param_mode else line[param2]
                param3 = param3 if not thr_param_mode else line[param3]
                line[param3] = 1 if param1 == param2 else 0
                i+= 4
                
            elif op_code == 99:
                break
            else:
                print('weird op_code', op_code)
                i+=1
                break
        except:
            #print(line)
            break
    return output
    
    
class Amplifier:
    def __init__(self, program, phase_setting, letter=None, optionalinput = None):
        self.mem = program[:]
        self.phase_setting = phase_setting
        self.hasbeenrun = False
        self.letter=letter
        self.halted=False
        self.i=0
        
    def run(self, input):
        res = self.amplify(input)
        return res
    
    def amplify(self, input_signals, letter=None):
        print(self.letter, self.i, input_signals)
        #print(self.mem)
        print(self.letter, input_signals, self.hasbeenrun)
        cnt = 0
        output=None
        while (self.i<len(self.mem)):
            op_code = self.mem[self.i]%100
            one_param_mode = (self.mem[self.i] // 100) % 10
            two_param_mode = (self.mem[self.i] // 1000) % 10
            thr_param_mode = (self.mem[self.i] // 10000) % 10
            if(cnt<30):
                print("----", self.i, self.mem[self.i], op_code, self.hasbeenrun)
                cnt+=1
            if thr_param_mode != 0: print("WARANING")

            #print(self.mem)
            if op_code == 1:
                addend1 = self.mem[self.i+1] if one_param_mode else self.mem[self.mem[self.i+1]]
                addend2 = self.mem[self.i+2] if two_param_mode else self.mem[self.mem[self.i+2]]
                replace_pos = self.mem[self.i+3] if not thr_param_mode else self.mem[self.mem[self.i+3]]
                self.mem[replace_pos] = addend1 + addend2
                self.i+=4
            elif op_code == 2:
                mul1 = self.mem[self.i+1] if one_param_mode else self.mem[self.mem[self.i+1]]
                mul2 = self.mem[self.i+2] if two_param_mode else self.mem[self.mem[self.i+2]]
                replace_pos = self.mem[self.i+3] if not thr_param_mode else self.mem[self.mem[self.i+3]]
                #print('rp',replace_pos, mul1, mul2)
                self.mem[replace_pos] = mul1 * mul2
                self.i+=4
            elif op_code == 3:
                pos = self.mem[self.i+1]
                if not self.hasbeenrun:
                    val = self.phase_setting
                    self.hasbeenrun = True
                else:
                    val = input_signals
                self.mem[pos] = int(val)
                self.i+=2
            elif op_code == 4:
                val = self.mem[self.i+1]
                output=self.mem[val]
                self.i+=2
                print('outputting', output)
                return output
            elif op_code == 5:
                param1, param2 = self.mem[self.i+1:self.i+3]
                param1 = param1 if one_param_mode else self.mem[param1]
                param2 = param2 if two_param_mode else self.mem[param2]
                if param1 != 0: 
                    self.i = param2
                    continue
                self.i+= 3
            elif op_code == 6:
                param1, param2 = self.mem[i+1:i+3]
                param1 = param1 if one_param_mode else self.mem[param1]
                param2 = param2 if two_param_mode else self.mem[param2]
                if param1 == 0: 
                    self.i = param2
                    continue
                self.i+= 3
            elif op_code == 7:
                param1, param2, param3 = self.mem[self.i+1:self.i+4]
                param1 = param1 if one_param_mode else self.mem[param1]
                param2 = param2 if two_param_mode else self.mem[param2]
                param3 = param3 if not thr_param_mode else self.mem[param3]
                self.mem[param3] = 1 if param1 < param2 else 0
                self.i+= 4
            elif op_code == 8:
                param1, param2, param3 = self.mem[self.i+1:self.i+4]
                param1 = param1 if one_param_mode else self.mem[param1]
                param2 = param2 if two_param_mode else self.mem[param2]
                param3 = param3 if not thr_param_mode else self.mem[param3]
                self.mem[param3] = 1 if param1 == param2 else 0
                self.i+= 4
                
            elif op_code == 99:
                self.halted = True
                print('halted')
                return output
            else:
                print('weird op_code', op_code)
                i+=1
                break
        
        #return output