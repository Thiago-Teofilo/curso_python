name = "Thiago Teofilo"
len_name = len(name)

count = 0
new_str = ""
while count < len_name:
    new_str += f"*{name[count]}"
    count += 1

print(new_str)