import importlib

def import_or_install(module_name):
    """
    這個函數用於導入或安裝指定的Python模塊。

    Args:
        module_name (str): 要導入或安裝的模塊名稱。

    Returns:
        None

    Raises:
        ImportError: 如果無法導入指定的模塊。
    """
    try:
        module = importlib.import_module(module_name)
        print(f"{module_name}版本:", module.__version__)
    except ImportError:
        print(f"未找到{module_name}模塊，正在安裝...")
        try:
            import subprocess
            subprocess.check_call(["pip", "install", module_name])
            print(f"{module_name}安裝成功！")
        except Exception as e:
            print(f"安裝{module_name}時發生錯誤: {e}")
