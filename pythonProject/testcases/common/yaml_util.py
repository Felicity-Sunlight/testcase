import os
import yaml


class YamlUtil:

    # 读取extract.yml文件
    def read_extract_yml(self):
        with open(os.getcwd() + "/extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 写入extract.yml文件
    def write_extract_yml(self, data):
        with open(os.getcwd() + "/extract.yml", mode='w', encoding='utf-8') as f:
            value = yaml.dump(data=data, stream=f, allow_unicode=True)
            return value
