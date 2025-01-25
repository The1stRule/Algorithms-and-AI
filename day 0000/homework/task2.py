
def convert_base(a, b, c):
    if a != 10:
        conv = {
            "A": 10, "B": 11,
            "C": 12, "D": 13,
            "E": 14, "F": 15
        }

        num = 0
        new_c = 0
        for i in c[::-1]:
            if i not in "0123456789":
                i = conv[i]
            new_c += (a ** num) * int(i)
            num += 1
        if b == 10:
            return new_c
        
        c = new_c

    converter = {
        0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
        6: "6", 7: "7", 8: "8", 9: "9", 10: "A",
        11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
    }

    
    result = ""
    while c != 0:
        result += converter[c % b]
        c //= b
    if b == 2:
        result += "0"

    return result[::-1]


print(convert_base(10, 4, 5))