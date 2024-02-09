input_string = input("Enter a string: ")

def string_to_binary(input_string):
    binary_data = ''.join(format(ord(char), '08b') for char in input_string)
    return binary_data

def binary_to_number(binary_data):
    count_list = []
    current_count = 1
    prev_digit = binary_data[0]

    for digit in binary_data[1:]:
        if digit == prev_digit:
            current_count += 1
        else:
            count_list.append(current_count)
            current_count = 1
            prev_digit = digit

    count_list.append(current_count)

    result = int(''.join(map(str, count_list)))
    return result


def number_to_emojis(number):
    emoji_mapping = {
        '0': '😀',
        '1': '😎',
        '2': '😊',
        '3': '🥳',
        '4': '😜',
        '5': '😇',
        '6': '😍',
        '7': '🤩',
        '8': '😂',
        '9': '🤔',
    }

    emoji_string = ''.join(emoji_mapping[digit] for digit in str(number))
    return emoji_string

binary_data = string_to_binary(input_string)
result_number = binary_to_number(binary_data)
emoji_string = number_to_emojis(result_number)

print(f"Output Emojis: {emoji_string}")
