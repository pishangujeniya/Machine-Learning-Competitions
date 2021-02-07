import os
markdownString = ""
for x in os.listdir("."):
    if os.path.isdir(x):
        markdownString += "[" + x + "]" + "(./" + x + ")" + "\r\n"

print(markdownString)
with open("dir_markdown_generator.md", "w") as text_file:
    print(markdownString, file=text_file)


