def delete():
    with open('codeList.txt', 'w', encoding='utf-8', newline='') as out:
        with open('file/out.txt', 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().replace("\n", "")
                if not line:
                    break
                start = line.find(":")
                line = line[:start]
                out.write(line)
                out.write('\n')

def splite():
    with open('codeList.txt', 'w', encoding='utf-8') as out:
        with open('file/out.txt', 'r', encoding='utf-8') as f:
            while True:
                line = f.readline().replace("\n", "").replace(" ", "\ ")
                if not line:
                    break
                start = line.find(":")
                line = line[:start]
                out.write(line)
                out.write('\n')

if __name__ == '__main__':
    delete()