# main.py
def main():
    try:
        # 初始化配置
        config = CloudConfig()
        config.validate()

        # 初始化资产管理器
        manager = CloudAssetsManager(config)
        
        # 打印资产摘要
        manager.print_assets_summary()

    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main()