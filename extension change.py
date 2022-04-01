import os


def add_extension(filepath):
    if os.path.isfile(filepath):
        filename, extension = os.path.splitext(filepath)
        changed_path = f'{filename}{extension}.a1pHa'
        os.rename(filepath, changed_path)
    else:
        pass


def remove_extension(filepath):
    filename, extension = os.path.splitext(filepath)
    if extension == '.a1pHa':
        os.rename(filepath, filename)
    else:
        pass


root, extension = os.path.splitext('/Users/jithendranadh/PycharmProjects/Ransomwar/TEST/impfile.txt.a1pHa')
print(root, extension)

remove_extension('/Users/jithendranadh/PycharmProjects/Ransomwar/TEST/impfile.txt.a1pHa')
"""print(root, extension)

if root[-6:] == '.aplha':
    print('yes')
else:
    print(root[-6: ])"""