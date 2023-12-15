compdict={
    "0":"0101010","1":"0111111","-1":"0111010",
    "D":"0001100","A":"0110000","M":"1110000",
    "!D":"0001101","!A":"0110001","!M":"1110001",
    "-D":"0001111","-A":"0110001","-M":"1110001",
    "D+1":"0011111","A+1":"0110111","M+1":"1110111",
    "1+D":"0011111","1+A":"0110111","1+M":"1110111",
    "D-1":"0001110","A-1":"0110010","M-1":"1110010",
    "D+A":"0000010","D+M":"1000010",
    "A+D":"0000010","M+D":"1000010",
    "D-A":"0010011","D-M":"1010011",
    "A-D":"0000111","M-D":"1000111",
    "D&A":"0000000","D&M":"1000000",
    "D|A":"0010101","D|M":"1010101"
}
destdict={
    "0":"000",
    "M":"001",
    "D":"010",
    "DM":"011",
    "A":"100",
    "AM":"101",
    "AD":"110",
    "ADM":"111"
}
jumpdict={
    "":"000",
    "JGT":"001",
    "JEQ":"010",
    "JGE":"011",
    "JLT":"100",
    "JNE":"101",
    "JLE":"110",
    "JMP":"111"
}

symboldict={
    "R0":0,"R1":1,"R2":2,"R3":3,"R4":4,"R5":5,"R6":6,"R7":7,"R8":8,"R9":9,"R10":10,"R11":11,"R12":12,"R13":13,"R14":14,"R15":15,
    "SCREEN":16384,"KBD":24576
}
count=0
first="111"
file_path="file.hack"
file_list=[]
with open("file.asm","r",encoding="utf-8") as file:
    File_modification=file.readlines()
File_modification=[line.split("//")[0].strip() for line in File_modification]
File_modification=[line for line in File_modification if line]
first_non_whitespace_line=next(line.strip() for line in File_modification if line.strip())
File_modification.remove(first_non_whitespace_line)
File_modification.insert(0,first_non_whitespace_line)
File_modification.append("")
with open("file_Revise.asm","w",encoding="utf-8") as file:
    file.write("\n".join(File_modification))
with open("file_Revise.asm","r") as file:
    code=file.readlines()
    index=16
    for i in range(len(code)):
        cur=code[i]
        if cur[0]=="(":
            if count==0:
                symboldict[cur[1:len(cur)-2]]=i
            else:
                symboldict[cur[1:len(cur)-2]]=i-count
            count+=1
    for i in range(len(code)):
        cur=code[i]
        if cur[0]=="@":
            if cur[1:len(cur)-1].isalpha():
                if cur[1:len(cur)-1] not in symboldict:
                    symboldict[cur[1:len(cur)-1]]=index
                    index+=1
    with open(file_path,"w") as file:
        for i in range(len(code)):
            cur=code[i]
            if "(" not in cur:
                if cur[0]=="@":
                    if cur[1:len(cur)-1].isalpha():
                        zero=""
                        if len(bin(symboldict.get(cur[1:len(cur)-1]))[2:])!=16:
                            for k in range(16-len(bin(symboldict.get(cur[1:len(cur)-1]))[2:])):
                                zero+="0"
                            file_list.append(zero+bin(symboldict.get(cur[1:len(cur)-1]))[2:])
                    else:
                        if len(bin(int(cur[1:len(cur)-1]))[2:])!=16:
                            zero=""
                            for k in range(16-len(bin(int(cur[1:len(cur)-1]))[2:])):
                                zero+="0"
                            file_list.append(zero+bin(int(cur[1:len(cur)-1]))[2:])
                else:
                    if cur[1]=="=":
                        for j in range(len(cur)):
                            if ";" in cur:
                                file_list.append("111"+compdict.get(cur[2:j])+destdict.get(cur[0])+jumpdict.get(cur[j+1:len(code[i])-1]))
                        else:
                            file_list.append("111"+compdict.get(cur[2:len(code[i])-1])+destdict.get(cur[0])+"000")
                            #print(cur[2:len(code[i])-1])
                    else:
                        file_list.append("111"+compdict.get(cur[0])+"000"+jumpdict.get(cur[2:len(code[i])-1]))
                        #print((cur[2:len(code[i])-1]))
        file_str = "\n".join(file_list)
        file.write(file_str)

    


    
        





