def is_digit(string) :
    if string.isdigit() :
        return True
    else :
        try :
            float(string)
            return True
        except ValueError :
            return False


def from_json(str) :
    temp_sign = ""
    char_list = list()
    item = ""
    key = ""
    value = ""
    if str[0] == '[' :
        item = list()
        char_list.append(']')
    if str[0] == '{' :
        item = dict()
        char_list.append('}')
    if str[0] == '"' and str[-1] == '"' :  ## возвращаем примитивные типы
        return str[1 :-1]
    if is_digit(str) :
        if '.' in str :
            return float(str)
        else :
            return int(str)
    if str == 'false' :
        return False
    if str == 'true' :
        return True
    if str == 'null' :
        return None
    i = 1  # position не забывать плюсовать!!!!!!!!!
    while i < len(str) :
        char = str[i]
        if char == ' ' :
            i += 1
            continue
        if '}' in char_list :
            while str[i] != ':' :
                key += str[i]
                i += 1
            i += 2
            while True :
                if str[i] == "[" :
                    char_list.append('[')
                elif str[i] == "{" :
                    char_list.append('{')
                elif str[i] == ']' or str[i] == '}' :
                    temp_sign = char_list.pop()
                    if len(char_list) == 0 :
                        char_list.append(temp_sign)
                        break

                value += str[i]
                i += 1
                if str[i] == ',' and len(char_list) == 1 :
                    i += 1
                    break

            if str[i] == '}' :
                char_list.pop()
            value = value.strip()
            i += 1
            key = from_json(key)
            item[key] = from_json(value)
            key = ""
            value = ""
            continue

        if ']' in char_list :
            while True :
                if str[i] == "[" :
                    char_list.append('[')
                elif str[i] == "{" :
                    char_list.append('{')
                elif str[i] == ']' or str[i] == '}' :
                    temp_sign = char_list.pop()
                    if len(char_list) == 0 :
                        char_list.append(temp_sign)
                        break

                value += str[i]
                i += 1
                if str[i] == ',' and len(char_list) == 1 :
                    i += 1
                    break

            if str[i] == ']' :
                char_list.pop()
            value = value.strip()
            i += 1
            item.append(from_json(value))
            value = ""
            continue
    return item
