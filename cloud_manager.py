# cloud_manager.py
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models as cvm_models
from tencentcloud.cdb.v20170320 import cdb_client, models as cdb_models

class CloudAssetsManager:
    def __init__(self, config):
        self.config = config
        self.cred = credential.Credential(config.secret_id, config.secret_key)
        self.http_profile = HttpProfile()
        self.client_profile = ClientProfile()
        self.client_profile.httpProfile = self.http_profile

    def get_cvm_instances(self):
        """获取云服务器实例列表"""
        try:
            client = cvm_client.CvmClient(self.cred, self.config.region, self.client_profile)
            req = cvm_models.DescribeInstancesRequest()
            resp = client.DescribeInstances(req)
            return resp.InstanceSet
        except TencentCloudSDKException as err:
            print(f"获取云服务器实例失败: {err}")
            return []

    def get_cdb_instances(self):
        """获取云数据库实例列表"""
        try:
            client = cdb_client.CdbClient(self.cred, self.config.region, self.client_profile)
            req = cdb_models.DescribeDBInstancesRequest()
            resp = client.DescribeDBInstances(req)
            return resp.Items
        except TencentCloudSDKException as err:
            print(f"获取云数据库实例失败: {err}")
            return []

    def print_assets_summary(self):
        """打印资产摘要"""
        print("\n=== 腾讯云资产摘要 ===")
        print(f"区域: {self.config.region}")
        
        # 获取并打印CVM实例信息
        cvm_instances = self.get_cvm_instances()
        print(f"\n云服务器实例数量: {len(cvm_instances)}")
        for instance in cvm_instances:
            print(f"- 实例ID: {instance.InstanceId}")
            print(f"  名称: {instance.InstanceName}")
            print(f"  状态: {instance.InstanceState}")
            print(f"  配置: {instance.CPU}核 {instance.Memory}GB内存")
            print(f"  公网IP: {instance.PublicIpAddresses if instance.PublicIpAddresses else '无'}")
            print("---")

        # 获取并打印CDB实例信息
        db_instances = self.get_cdb_instances()
        print(f"\n云数据库实例数量: {len(db_instances)}")
        for db in db_instances:
            print(f"- 实例ID: {db.InstanceId}")
            print(f"  名称: {db.InstanceName}")
            print(f"  状态: {db.Status}")
            print(f"  类型: {db.InstanceType}")
            print("---")