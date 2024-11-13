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

    def validate(self):
        if not all([self.secret_id, self.secret_key]):
            raise ValueError("请确保设置了 TENCENTCLOUD_SECRET_ID 和 TENCENTCLOUD_SECRET_KEY 环境变量")
