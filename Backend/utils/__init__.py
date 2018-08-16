"""
工具函数
"""
import pytesseract
from PIL import Image


def dictsub(obj, fields):
    """字典截取
    input: obj dict对象
           fields 需要的key值
    output: dict 截取好的字典
    """
    return {k: v for k, v in obj.items() if k in fields}


def remove_invalid_char(obj):
    """去除字符串中无效字符
    input: str
    out: str
    """
    vaild_char = [char for char in obj if char.isidentifier()]

    return ''.join(vaild_char)


def ocr_extract_word(img_path):
    """ocr提取图片内文字
    input: img_path str
    out: str
    """
    img = Image.open(img_path)
    out = pytesseract.image_to_string(img, lang="chi_sim")

    return remove_invalid_char(out)
