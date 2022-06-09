import os
import chardet
from tqdm import tqdm 

s = open("source_list.txt", "r", encoding="utf-8")
source_list = s.readlines()

for source in tqdm(source_list):
    source = source.replace("\n", "").replace("'", "")
    rawData = open(source, 'rb').read()
    result = chardet.detect(rawData)
    enc = result['encoding']

    input = open(source, "r", encoding = enc)
    lines = input.readlines()
    input.close()

    output = open(source, "w")
    for line in lines:
        if line.find("package") != -1:
            continue
        output.write(line)
    output.close()
s.close()
