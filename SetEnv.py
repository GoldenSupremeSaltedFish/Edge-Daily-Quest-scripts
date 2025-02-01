import subprocess
import sys
def install_package(package_name):
    """安装指定的 Python 包"""
    try:
        __import__(package_name)
        print(f"'{package_name}' 已经安装。")
     
    except ImportError:
        print(f"正在安装 '{package_name}'...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"'{package_name}' 安装完成！")

