# import random
# with open('numbers.txt', 'w') as f:
#     f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(50000000))

import tempfile


def merge(firstfile, secondfile, res) :
    firstfile.seek(0)
    secondfile.seek(0)
    res.seek(0)
    line1 = firstfile.readline()
    line2 = secondfile.readline()
    while line1 and line2 :
        if int(line1) < int(line2) :
            res.writelines(line1)
            line1 = firstfile.readline()
        else :
            res.writelines(line2)
            line2 = secondfile.readline()
    if line1 :
        while line1 :
            res.writelines(line1)
            line1 = firstfile.readline()
    else :
        while line2 :
            res.writelines(line2)
            line2 = secondfile.readline()
    firstfile.seek(0)
    secondfile.seek(0)
    res.seek(0)


def sort(input_file, output_file, size=100000) :
    data = list()
    temp_files = list()
    merge_files = list()
    with open(output_file, 'w') as out :
        with open(input_file) as input_file :
            line = input_file.readline()
            word_count = 0
            while line :
                data.append(int(line))
                word_count += 1
                if word_count == size :
                    temp = tempfile.NamedTemporaryFile(mode="w+")
                    temp_files.append(temp)
                    temp.writelines(str(line) + "\n" for line in sorted(data))
                    temp.seek(0)
                    data.clear()
                    word_count = 0
                line = input_file.readline()
            temp = tempfile.NamedTemporaryFile(mode="w+")
            temp_files.append(temp)
            temp.writelines(str(line) + "\n" for line in sorted(data))
            temp.seek(0)
            data.clear()
            while len(temp_files) > 2 :
                while len(temp_files) > 1 :
                    mergf = tempfile.NamedTemporaryFile(mode="w+")
                    merge(temp_files.pop(0), temp_files.pop(0), mergf)
                    merge_files.append(mergf)
                if len(temp_files) == 1 :
                    merge_files.append(temp_files.pop(0))
                temp_files = merge_files[:]
                merge_files.clear()
            if len(temp_files) == 2 :
                merge(temp_files.pop(0), temp_files.pop(0), out)
            else :
                file = temp_files.pop(0)
                line = file.readline()
                while line :
                    out.writelines(line)
