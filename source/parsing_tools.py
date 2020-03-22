# Delete spaces at the beginning and at the end of the word
def strip(str):
    while str[0] == ' ':
        str = str[1:len(str)]

    while str[len(str) - 1] == ' ':
        str = str[0:len(str) - 1]

    return str


def clear_spaces(str):
    i = 0
    while i < len(str):
        if str[i] == ' ':
            str = str[0:i] + str[i + 1:len(str)]
            i -= 1
        i += 1
    return str


def separate_to_lines(text):
    lines = []
    temp_str = ""

    for symb in text:
        if symb == '\n' and len(temp_str) > 0:
            print(temp_str)  # marker
            lines.append(temp_str)
            print(lines)  # marker
            temp_str = ""
            continue

        temp_str += symb

    if temp_str != "":
        lines.append(temp_str)

    return lines
