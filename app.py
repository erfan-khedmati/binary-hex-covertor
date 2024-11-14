# Hex covert
hex_character = {
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
}

# Calculate number
def cal_number(type, number):
    # List of the result
    num_list = []

    # If type is binary (type = 0 = binary)
    if type == "0":
        while number > 0:
            remain = number % 2
            # Add to the list
            num_list.append(remain)
            number //= 2
        # Revers the list
        num_list.reverse()

        # convert to the txt
        txt_result = ""
        for txt in num_list:
            txt_result += str(txt)
        # Return the result
        return txt_result

print(cal_number("0", 12))
