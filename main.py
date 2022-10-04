
from asyncio.windows_events import NULL

def CodeController(code): # kodun doğruluğunun kontrolü
    alphabe = "GHIJKLMNOPQRSTUVWXYZ "
    equality = False
    for i in code:
        for x in alphabe:
            if i == x:
                equality = True
                return equality

    return equality


def TakeMachineCode(): # makine kodunun alınması
    Truth = False
    while (Truth == False):
        code = input("Enter a Machine Code with 8 byte (example:E0865007): ")
        code = str(code)
        code = code.upper()

        if (len(code) == 8 and CodeController(code) == False):
            print("Entered code = {}".format(code))
            Truth = True
            return code
        else:
            raise Exception("Code is too large or has invalid characters(G-Z)")


def findTwoscomplement(str): # binary sayının two's complementinin bulunması
    n = len(str)

    # Traverse the string to get first
    # '1' from the last of string
    i = n - 1
    while (i >= 0):
        if (str[i] == '1'):
            break

        i -= 1

    # If there exists no '1' concatenate 1
    # at the starting of string
    if (i == -1):
        return '1' + str

    # Continue traversal after the
    # position of first '1'
    k = i - 1
    while (k >= 0):

        # Just flip the values
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)

        k -= 1

    # return the modified string
    return str


def HexaToDecimal(code):  # hexadecimal sayının decimale çevrilmesi
    scale = 16  ## equals to hexadecimal

    num_of_bits = 32

    decimal = bin(int(code, scale))[2:].zfill(num_of_bits)
    return decimal


def detectOP(code):  # OP kodun tipinin tespit edilmesi
    process_type = NULL
    op = code[31 - 27] + code[31 - 27 + 1]

    if op == "00":
        process_type = "Data Processing"
    elif op == "01":
        process_type = "Memory"
    elif op == "10":
        process_type = "Branch"
    else:
        return process_type
    return process_type


def detectCond(code): # cond kodun tipinin tespit edilmesi
    name = ""
    cond = code[0:4]
    if cond == "0000":
        name = "EQ"
    elif cond == "0001":
        name = "NE"
    elif cond == "0010":
        name = "CS/HS"
    elif cond == "0011":
        name = "CC/LO"
    elif cond == "0100":
        name = "MI"
    elif cond == "0101":
        name = "PL"
    elif cond == "0110":
        name = "VS"
    elif cond == "0111":
        name = "VC"
    elif cond == "1000":
        name = "HI"
    elif cond == "1001":
        name = "LS"
    elif cond == "1010":
        name = "GE"
    elif cond == "1011":
        name = "LT"
    elif cond == "1100":
        name = "GT"
    elif cond == "1101":
        name = "LE"
    elif cond == "1110":
        name = ""
    return name



def detectImm24(code):  # imm24'ün bulunması
    imm24 = code[8:32]
    return imm24


def detectI(code):  # I'nın bulunması
    I = code[31 - 25]
    return I


def detectS(code): # S'nin bulunması
    S = code[31 - 20]
    return S


def detectinstr(code):  # belirli bitler arasındaki instruction un bulunması
    instr = code[20:28]
    return instr


def detectSh(code):  # sh'nin bulunması
    sh = code[25:27]
    return sh


def detectinstr2(code):  # belirli bitler arasındaki instruction'un bulunması
    instr2 = code[20:25]
    return instr2


def detectRot(code): # rotasyonun bulunması
    rot = code[20:24]
    return rot


def detectImm8(code): # Imm8'in bulunması
    imm = code[24:32]
    return imm

def detectImm12(code): # Imm12'nin bulunması
    imm = code[20:32]
    return imm


def detectRm(code): # Rm'nin bulunması
    rm = code[28:32]
    return rm


def detectFourthB(code):  # sağdan 4. bitin bulunması
    fourthB = code[27]
    return fourthB


def detectShamt5(code): # shamt5'in bulunması
    shamt5 = code[20:25]
    return shamt5


def detectRs(code):  #Rs'nin bulunması
    rs = code[20:24]
    return rs
def detectRd(code):  # rd'nin bulunması
    rd = code[16:20]
    return rd
def detecRn(code): # Rn 'nin bulunması
    rn = code[12:16]
    return rn



def DataProcessing_Src2(code, src2_type):  # data prc fpnksiyoonu

    if src2_type == "immediate-8":
        rot = int(detectRot(code), 2)
        imm = int(detectImm8(code), 2)

        return rot, imm
    else:
        rm = int(detectRm(code), 2)
        if detectFourthB(code) == "0":
            shamt5 = int(detectShamt5(code), 2)

            return rm, shamt5
        else:
            rs = int(detectRs(code), 2)
            return rm, rs


def detectSrc2(code, process_type, I):  #I'nın tipinin bulunması
    I_Name = NULL
    if process_type == "Data Processing":
        if I == "1":
            I_Name = "immediate-8"

        else:
            if detectFourthB(code) == "0":
                I_Name = "register"
            else:
                I_Name = "register-shifted-register"
        return I_Name
    elif process_type == "Memory":
        if I == "1":
            I_Name = "register"
        else:
            I_Name = "immediate-12"
        return I_Name
    else:
        L = code[31 - 25 + 1]
        I_Name = "immediate-24"

        if L == "1":
            process_type = "BL"
            return I_Name, process_type
        else:
            process_type = "B"
    return I_Name, process_type


def detectCmd(code, S, I): # cmd kodun bulunması
    name = ""
    instr = detectinstr(code)
    sh = detectSh(code)
    instr2 = detectinstr2(code)
    cmd = code[31 - 24] + code[31 - 23] + code[31 - 22] + code[31 - 21]
    if cmd == "0000":
        name = "AND"
    elif cmd == "0001":
        name = "EOR"
    elif cmd == "0010":
        name = "SUB"
    elif cmd == "0011":
        name = "RSB"
    elif cmd == "0100":
        name = "ADD"
    elif cmd == "0101":
        name = "ADC"
    elif cmd == "0110":
        name = "SBC"
    elif cmd == "0111":
        name = "RSC"
    elif cmd == "1000" and S == "1":
        name = "TST"
    elif cmd == "1001" and S == "1":
        name = "TEQ"
    elif cmd == "1010" and S == "1":
        name = "CMP"
    elif cmd == "1011" and S == "1":
        name = "CMN"
    elif cmd == "1100":
        name = "ORR"
    elif cmd == "1101":
        if I == "1" or instr == "00000000":
            name = "MOV"
        elif I == "0" and sh == "00" and instr != "00000000":
            name = "LSL"
        elif I == "0" and sh == "01":
            name = "LSR"
        elif I == "0" and sh == "10":
            name = "ASR"
        elif I == "0" and sh == "11" and instr2 != "00000":
            name = "ROR"
    elif cmd == "1110":
        name = "BIC"
    elif cmd == "1111":
        name = "MVN"

    if(S =="1" and (name != "TST" and name != "TEQ" and name != "CMP" and name != "CMN")):
        return name+"S"
    else:
        return name

def detectMemFunct(code):  # memory için memFunct'un bulunması
    I = detectI(code)
    P = code[31 - 24]
    U = code[31 - 23]
    B = code[31 - 22]
    W = code[31 - 21]
    L = code[31 - 20]
    return I + P + U + B + W + L

def branch(code,codeB,process_type,I,cond):  # komut branchsa işlemin yapılması
    I_name, process_type2 = detectSrc2(codeB, process_type, I)
    imm24 = detectImm24(codeB)

    if code[2] != "F":

        i = int(imm24, 2)
        i = i + 2
        i = str(i)
        i_type = "forward"
    else:
        x = findTwoscomplement(imm24)
        i = int(x, 2)
        i = i - 2
        i = str(i)
        i_type = "back"

    print("{}{} (code goes  {} steps {} )".format(process_type2, cond, i, i_type))


def dataProcessing(I_name,codeB,cmd,cond,rd,rn):  # komut dataProcessing ise işlemin yapılması
    if (I_name == "immediate-8"):
        rot, imm = DataProcessing_Src2(codeB, I_name)
        if (rot != 0):
            rot = int((32 - (rot * 2)))
            imm = imm << rot
        if(cmd == "MOV"):
            print("{} {},{}".format(cmd + cond, "R" + rd, "#" + str(imm)))  # immediate dp
        elif (cmd == "CMP" or cmd == "CMN"):
            print("{} {},{}".format(cmd + cond, "R" + rn, "#" + str(imm)))
        else:
            print("{} {},{},{}".format(cmd + cond, "R" + rd, "R" + rn, "#" + str(imm)))
    elif (I_name == "register"):  # register dp
        rm, shamt5 = DataProcessing_Src2(codeB, I_name)
        if (shamt5 == 0):
            if (cmd == "MOV"):
                print("{} {},{}".format(cmd + cond, "R" + rd, "R" + str(rm)))
            elif (cmd == "CMP" or cmd == "CMN"):
                print("{} {},{}".format(cmd + cond, "R" + rn, "R" + str(rm)))
            else:
                print("{} {},{},{}".format(cmd + cond, "R" + rd, "R" + rn, "R" + str(rm)))

        else:
            print("{} {},{},{}".format(cmd + cond, "R" + rd, "R" + str(rm), "#" + str(shamt5)))

    else:  # register shifted register
        rm, rs = DataProcessing_Src2(codeB, I_name)
        print("{} {},{},{}".format(cmd + cond, "R" + rd, "R" + str(rm), "R" + str(rs)))


def memory(I_name,codeB,mode_name,bl_name,cond,rd,rn,u_name):  # komut memory ise işlemin yapılması
    if (I_name == "immediate-12"):
        imm = str(int(detectImm12(codeB), 2))
        if (mode_name == "postindex"):
            print("{} {},{},{}".format(bl_name + cond, "R" + rd, "[R" + str(rn) + "]", "#" + u_name + imm))
        elif (mode_name == "offset"):
            print("{} {},{}".format(bl_name + cond, "R" + rd, "[R" + str(rn) + ",#" + u_name + imm + "]"))
        else:
            print("{} {},{}".format(bl_name + cond, "R" + rd, "[R" + str(rn) + ",#" + u_name + imm + "]!"))
    else:
        rm, shamt5 = DataProcessing_Src2(codeB, I_name)
        if (shamt5 == 0):
            if (mode_name == "postindex"):
                print("{} {},{},{}".format(bl_name + cond, "R" + rd, "[R" + rn + "]", u_name + "R" + str(rm)))
            elif (mode_name == "offset"):
                print("{} {},{}".format(bl_name + cond, "R" + rd, "[R" + rn + "," + u_name + "R" + str(rm) + "]"))
            else:
                print("{} {},{}".format(bl_name + cond, "R" + rd, "[R" + rn + "," + u_name + "R" + str(rm) + "]!"))
        else:
            if (mode_name == "postindex"):
                print("{} {},{},{}".format(bl_name + cond, "R" + rd, "[R" + str(rm) + "]", "#" + u_name + str(shamt5)))
            elif (mode_name == "offset"):
                print("{} {},{}".format(bl_name + cond, "R" + rd, "[R" + str(rm) + ",#" + u_name + str(shamt5) + "]"))
            else:
                print("{} {},{}".format(bl_name + cond, "R" + rd, "[R" + str(rm) + ",#" + u_name + str(shamt5) + "]!"))


def detectIndexingMode_Others(ipubwl):  # index modun bulunması
    mode = ipubwl[1] + ipubwl[4]
    mode_name = NULL
    u = ipubwl[2]
    u_name = NULL
    bl = ipubwl[3] + ipubwl[5]
    bl_name = NULL
    if mode == "01":
        raise Exception("NOT SUPPORTED İNDEXİNG MODE")
    elif mode == "00":
        mode_name = "postindex"
    elif mode == "10":
        mode_name = "offset"
    elif mode == "11":
        mode_name = "preindex"

    if u == "0":
        u_name = "-"
    else:
        u_name = ""

    if bl == "00":
        bl_name = "STR"
    elif bl == "01":
        bl_name = "LDR"
    elif bl == "10":
        bl_name = "STRB"
    else:
        bl_name = "LDRB"

    return mode_name, u_name, bl_name

def main():
    code = TakeMachineCode()  # machine kodun alınması
    codeB = HexaToDecimal(code)  # kodun binarye çevrilmesi
    process_type = detectOP(codeB)  # op kodun bulunması
    cond = detectCond(codeB)  # cond kodun bulunması
    I = detectI(codeB)  # I'nın tespit edilmesi

    if process_type == "Branch":  # branch
       branch(code,codeB,process_type,I,cond)
    else:
        rd = str(int(detectRd(codeB), 2))
        rn = str(int(detecRn(codeB), 2))
        I_name = detectSrc2(codeB, process_type, I)
        if(process_type == "Data Processing"):  # data processing
            S = detectS(codeB)
            cmd = detectCmd(codeB, S, I)
            dataProcessing(I_name,codeB,cmd,cond,rd,rn)
        else:   # memory
            ipubwl = detectMemFunct(codeB)
            mode_name, u_name, bl_name = detectIndexingMode_Others(ipubwl)
            memory(I_name,codeB,mode_name,bl_name,cond,rd,rn,u_name)

main()





