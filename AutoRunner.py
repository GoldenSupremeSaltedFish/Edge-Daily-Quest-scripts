import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config import HOT_WORDS_API, KEYWORDS_SOURCES, DEFAULT_SEARCH_WORDS, minDeleyTime, maxDeleyTime

def smooth_scroll(driver):
    """平滑滚动页面到底部"""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

def search_in_edge(pages=60, scroll_pause_time=10, scroll_depth=1):
    """
    使用 Edge 浏览器进行搜索，并滚动指定深度后关闭。
    :param pages: 要搜索的页面数量。
    :param scroll_pause_time: 滚动后的等待时间（秒）。
    :param scroll_depth: 每个页面向下滚动的次数。
    """

    # 获取热点词
    search_words = get_hot_words()
    if not search_words:
        search_words = DEFAULT_SEARCH_WORDS

    # 初始化浏览器驱动
    driver = setup_driver()
    driver.get("https://www.bing.com/")

    for i in range(pages):
        
        try:
            # 随机等待时间（10秒到30秒之间）
            random_delay = random.randint(minDeleyTime, maxDeleyTime)
            time.sleep(random_delay)

            # 随机选择一个热点词
            search_word = random.choice(search_words)
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            search_box.send_keys(search_word)
            search_box.send_keys(Keys.RETURN)

            # 等待页面加载
            time.sleep(2)

            # 平滑滚动页面
            for _ in range(scroll_depth):
                smooth_scroll(driver)
                time.sleep(scroll_pause_time)

            # 返回 Bing 主页
            driver.get("https://www.bing.com/")

        except Exception as e:
            print(f"发生错误：{e}")

    driver.quit()

def setup_driver():
    """设置 Edge 浏览器驱动程序的默认选项"""
    options = webdriver.EdgeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)
    return driver

def get_hot_words():
    """从热点词 API 获取搜索词"""
    current_source_index = 0
    while current_source_index < len(KEYWORDS_SOURCES):
        source = KEYWORDS_SOURCES[current_source_index]
        url = f"{HOT_WORDS_API}{source}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get("data"):
                    return [item["title"] for item in data["data"]]
        except Exception as e:
            print(f"请求热点词失败: {e}")
        current_source_index += 1
    return DEFAULT_SEARCH_WORDS

if __name__ == "__main__":
    search_in_edge()
