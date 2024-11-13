# config.py
import os
from dotenv import load_dotenv

class CloudConfig:
    def __init__(self):
        # 加载.env文件中的环境变量
        load_dotenv()
        self.secret_id = os.getenv('TENCENTCLOUD_SECRET_ID')
        self.secret_key = os.getenv('TENCENTCLOUD_SECRET_KEY')
        self.region = os.getenv('TENCENTCLOUD_REGION', 'ap-beijing')

        self.secret_id = "LTAI5tJvURREPkRuBkK2GCa5"
        self.secret_key = "*******"

        self.secret_id = "PCOM4DJPRHL7EY82M4UL"
        self.secret_key = "*******"

        self.secret_id = "AKIDeSJC1wLqGpVLD7FMgtwNwhP0Z8e4jl4b"
        self.secret_key = "*******"

        self.secret_id = "AKIA263PLMO7TYGTWEHO"
        self.secret_key = "*******"


    def validate(self):
        if not all([self.secret_id, self.secret_key]):
            raise ValueError("请确保设置了 TENCENTCLOUD_SECRET_ID 和 TENCENTCLOUD_SECRET_KEY 环境变量")
