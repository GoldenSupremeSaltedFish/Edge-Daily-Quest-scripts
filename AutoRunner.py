import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bulabula import GibberishGenerator
from SetEnv import install_package
def setup_driver():
    """设置 Edge 浏览器驱动程序的默认选项"""
    options = webdriver.EdgeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)
    return driver

def search_in_edge(pages=60, scroll_pause_time=10, scroll_depth=1):
    """
    使用 Edge 浏览器进行搜索，并滚动指定深度后关闭。
    :param search_query: 搜索的内容。
    :param pages: 要搜索的页面数量。
    :param scroll_pause_time: 滚动后的等待时间（秒）。
    :param scroll_depth: 每个页面向下滚动的次数。
    """
    install_package("selenium")
    # 初始化浏览器驱动
    generator = GibberishGenerator(word_length_range=(4, 8), sentence_length_range=(6, 10))
    driver = setup_driver()
    driver.get("https://www.bing.com/")
    for i in range(pages):
        
        try:
        # 打开 Edge 浏览器的默认主页
           
            time.sleep(2)

        # 找到搜索框并输入内容
            
            random_text = generator.generate_gibberish(length=5)
            search_box = driver.find_element(By.NAME, "q")  # Bing 搜索框的 name 属性
            search_box.clear()
            search_box.send_keys(random_text)
            search_box.send_keys(Keys.RETURN)  # 模拟回车键

        # 等待页面加载
            time.sleep(2)
            # 滚动页面
            for _ in range(scroll_depth):
                driver.execute_script("window.scrollBy(0, window.innerHeight);")
                time.sleep(scroll_pause_time)

        # 等待一段时间后关闭浏览器
            time.sleep(2)
           
        except Exception as e:
            print(f"发生错误：{e}")
    driver.quit()

def get_default_edge_options():
    options = webdriver.EdgeOptions()
    options.add_argument("--no-sandbox")
    return options

if __name__ == "__main__":
     search_in_edge()
    
       

        
