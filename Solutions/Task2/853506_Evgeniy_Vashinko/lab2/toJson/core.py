def obj_to_json(obj, result="") :
    symbols = list()
    if type(obj) == dict :
        result += "{"
        symbols.append("}")
        for item in obj :
            result += obj_to_json(item)
            result += ": "
            result += obj_to_json(obj[item])
            result += ", "
        result = result[:len(result) - 2]
        result += symbols.pop()
    elif type(obj) == list or type(obj) == tuple :
        result += "["
        symbols.append("]")
        for item in obj :
            result += obj_to_json(item)
            result += ", "
        result = result[:len(result) - 2]
        result += symbols.pop()
    elif type(obj) == str :
        result += "\""
        symbols.append("\"")
        result += obj
        result += symbols.pop()
    elif type(obj) == int or type(obj) == float :
        result += str(obj)
    elif obj == True :
        result += "true"
    elif obj == False :
        result += "false"
    elif obj == None :
        result += "null"
    return result
