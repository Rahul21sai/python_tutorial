import os

files = os.listdir("python practice")
i = 1
for file in files:
    if file.endswith(".png"):
     print(file)
     os.rename(f"python practice/{file}",f"python practice/{i}.png")
     i = i+1
# os.rename('python practice/file.txt', 'python practice/6.txt')