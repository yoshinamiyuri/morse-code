# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close() # take some resources so you should close

# ToDO: Reading　# 読み終わったら、閉じてくれる
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# ToDO: Writing= "w" Appending="a　# appendしてくれる
with open("my_file.txt", mode="a") as file:
    file.write("\nJust saw an enemy.")

# ToDo: 新しいファイルを作成してくれる
with open("new_file.txt", mode="w") as file:
    file.write("New Text.")