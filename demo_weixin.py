# _*_coding:UTF-8_*_
# 创建于2019/4/16:10:50

import os
import logging

from aip import AipOcr

from key import APP_ID,API_KEY,SECRET_KEY

logging.basicConfig(level=logging.INFO)


""" 你的 APPID AK SK """
APP_ID = APP_ID
API_KEY = API_KEY
SECRET_KEY = SECRET_KEY
IMG_EXT = ['.png', '.jpg', '.jpeg', '.bmp']

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
# image = get_file_content('1.png')
#
# """ 调用通用文字识别, 图片参数为本地图片 """
# api_result=client.basicGeneral(image)
#
# world_result=[i['words'] for i in api_result['words_result']]
# result='\n'.join(world_result)
# print(result)


# 第一步优化
def ocr_basic_general(filename):
    logging.info(f'正在转换图片{filename}')
    with open(filename, 'rb') as fp:
        image = fp.read()
    api_result = client.basicGeneral(image)
    world_result = (i['words'] for i in api_result['words_result'])
    result = '\n'.join(world_result)
    # print(result)
    return result


# ocr_basic_general('./demo/python.png')

# 递归？
def handle_file(filename):
    # 可能是绝对路径也有可能是相对路径
    # ./python.png # 读取图片内容的文件
    # ./python.txt # 写入文本内容的文件
    filename_no_ext, ext = os.path.splitext(filename)

    if ext in IMG_EXT:
        filename_txt = filename_no_ext + '.txt'
        content = ocr_basic_general(filename)
        with open(filename_txt, 'w', encoding='utf-8') as f:
            f.write(content)


def handle_path(path):
    # 如果路径不存在直接return
    if not os.path.exists(path):
        return
    # 如果路径是文件夹，那么获取路径文件夹下面所有的文件和文件夹，然后遍历处理
    if os.path.isdir(path):
        for child_dir_or_file in os.listdir(path):
            child_path = os.path.join(path, child_dir_or_file)
            if os.path.isfile(child_path):
                handle_file(child_path)
            else:
                # 递归
                handle_path(child_path)
    # 如果路径是文件，直接进行处理
    else:
        handle_file(path)

# handle_path('./python.png')






