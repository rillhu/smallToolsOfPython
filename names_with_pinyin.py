#-*-coding:gb2312-*-
import openpyxl
from xpinyin import Pinyin

def remove_extra_spaces(string):
    # 将字符串按空格分割成列表
    words = string.split()
    
    # 如果只有一个单词,直接返回
    if len(words) == 1:
        return string
    
    # 将第一个单词与剩余部分拼接,去除剩余部分中的空格
    result = words[0] + ' ' + ''.join(words[1:])
    return result

def capitalize_string(string):
    # 使用title()方法将每个单词的首字母变成大写
    capitalized_string = string.title()
    return capitalized_string

# 打开Excel文件
workbook = openpyxl.load_workbook('name.xlsx')
sheet = workbook.active

# 遍历姓名列表
for row in range(2, sheet.max_row + 1):
    name = sheet.cell(row=row, column=1).value
    
    p = Pinyin()
    # 将姓名转换为拼音
    pinyin_name = p.get_pinyin(name, ' ')
    # 删除多余空格
    pinyin_name =  remove_extra_spaces(pinyin_name)
    # 首字母大写
    pinyin_name = capitalize_string(pinyin_name)
    
    # 将拼音写回Excel文件
    sheet.cell(row=row, column=2).value = pinyin_name

# 保存Excel文件
workbook.save('names_with_pinyin.xlsx')