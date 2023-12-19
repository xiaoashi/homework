import re

def check_duplicate_string(s):
    pattern = r"(.)\1{1,}"
    match = re.search(pattern, s)
    if match:
        return True
    else:
        return False

s = input("请输入字符串：")
result = check_duplicate_string(s)
print(result)