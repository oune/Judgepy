def get_one_file(message):
    files = filedialog.askopenfilenames(initialdir="..", title=message)

    if files == '':
        messagebox.showwarning("경고", "파일을 추가 하세요")  # 파일 선택 안했을 때 메세지 출력

    return files[0]


if __name__ == '__main__':
    from tkinter import filedialog
    from tkinter import messagebox
    import sys
    import os
    import zipfile
    import subprocess

    bandizip_path = get_one_file("반디집 실행파일을 선택 해 주세요")
    filePath = get_one_file("파일을 선택 해 주세요")
    folderPath = filePath[:-4]

    subprocess.run([bandizip_path, 'x', '-y', '-o:' + folderPath, filePath])
    os.chdir(folderPath)

    folders = os.listdir()
    for folder in folders:
        filepath = os.path.join(folderPath, folder)
        os.chdir(filepath)
        files = os.listdir()

        for file in files:
            filePath = os.path.join(os.getcwd(), file)
            subprocess.run([bandizip_path, 'x', '-y', filePath])
