import re

def dest(symbol):
    dest_code = {
        "": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }
    return dest_code.get(symbol, "000")

def comp(symbol):
    comp_code = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
    }
    return comp_code.get(symbol, "0000000")

def jump(symbol):
    jump_code = {
        "": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }
    return jump_code.get(symbol, "000")

def parse_c_instruction(instruction):
    comp_pattern = re.compile(r'(A?M?D?)=?([01ADM!+-]+);?(JGT|JEQ|JGE|JLT|JNE|JLE|JMP)?')
    match = comp_pattern.match(instruction)
    dest_part = match.group(1) if match.group(1) else ""
    comp_part = match.group(2) if match.group(2) else ""
    jump_part = match.group(3) if match.group(3) else ""
    return f"111{comp(comp_part)}{dest(dest_part)}{jump(jump_part)}"

def parse_a_instruction(instruction):
    if instruction.startswith("@"):
        address_part = instruction[1:]
        if address_part.isdigit():
            # A-instruction with a numeric address
            address = int(address_part)
        else:
            # A-instruction with a symbolic address
            # You may want to replace this with your symbol table lookup logic
            address = 0  # Replace with actual symbol lookup logic
    else:
        # Handle symbolic A-instruction without @ (e.g., OUTPUT)
        # You may want to replace this with your symbol table lookup logic
        address = int(instruction)  # Replace with actual symbol lookup logic

    binary_address = bin(address)[2:].zfill(15)
    return f"0{binary_address}"



def assemble(assembly_code):
    binary_code = []
    for line in assembly_code:
        if line.startswith("@"):
            binary_code.append(parse_a_instruction(line))
        else:
            binary_code.append(parse_c_instruction(line))
    return binary_code

if __name__ == "__main__":
    # 測試組譯器
    assembly_code = [
        "@21",
        "D=M",
        "@22",
        "D=D+M;JGT",
        "@23",
        "D;JEQ",
        "@OUTPUT",
        "0;JMP",
    ]

    binary_code = assemble(assembly_code)
    for binary_instruction in binary_code:
        print(binary_instruction)
