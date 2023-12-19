import re
def validate_id_card(id_card):
    pattern = r'^\d{17}[\dXx]$'
    if re.match(pattern, id_card):
        return True
    else:
        return False
id_card = input("请输入需要验证的身份证号：")
print(validate_id_card(id_card))