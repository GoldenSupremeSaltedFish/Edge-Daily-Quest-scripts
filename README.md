# 🐾 Edge-Daily-Quest-scripts - 自动化搜索小助手 🐾

欢迎来到 **Edge-Daily-Quest-scripts**，这是一个专门为帮助大家轻松完成每日搜索任务而设计的自动化小助手！🎉 无论是为了完成搜索引擎的每日任务，还是为了测试自动化脚本，这个小助手都能帮你省时省力，让你不再为重复的搜索任务烦恼！😊

---

## 🎀 项目结构

- **AutoRunner.py**: 主脚本，负责启动 Edge 浏览器并执行自动化搜索任务。
- ~~**bulabula.py**: 生成随机文本的小工具，用来生成可爱的搜索内容。~~（现在更新的脚本可以爬取关键词）
- **EdgeRunner.bat**: 双击就能运行的批处理文件，超级方便！
- **SetEnv.py**: 自动安装所需 Python 包的小助手。

---

## 🌟 功能

- 🖥️ 自动启动 Edge 浏览器并访问 Bing。
- 🎲 生成文本并在 Bing 上进行搜索。
- ⚙️ 支持自定义搜索页面数量和滚动深度。
- 📦 自动安装所需的 Python 包（如 Selenium）。

---

## 🐾 使用方法

1. **克隆项目**:
   ```bash
   git clone https://github.com/your-username/AutoRunner.git
   cd AutoRunner
   ```

2. **安装依赖**:
   确保你已经安装了 Python 3 和 pip。然后运行以下命令安装依赖：
   ```bash
   pip install selenium requests
   ```

3. **运行项目**:
   双击 `EdgeRunner.bat` 文件，小助手就会自动启动 Edge 浏览器并开始执行搜索任务啦！✨

---

## 🎨 自定义配置

你可以在 `AutoRunner.py` 中修改以下参数来定制搜索行为：

- `pages`: 要搜索的页面数量，默认为 60。
- `scroll_pause_time`: 每次滚动后的等待时间（秒），默认为 1。
- `scroll_depth`: 每个页面向下滚动的次数，默认为 1。

---

## 🧸 依赖

- Python 3.x
- Selenium requests
- Edge 浏览器

---

## 🐱 贡献

欢迎提交 Issue 和 Pull Request 来改进项目！让我们一起让这个小助手变得更可爱、更强大吧！💪

---

## 🍬 许可证

本项目采用 Apache License 2.0 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

---

**温馨提示**: 请确保你已经安装了 Edge 浏览器，并且 EdgeDriver 的版本与浏览器版本匹配。你可以从 [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) 下载并配置 EdgeDriver。

---

希望你喜欢这个助手！🐾 如果有任何问题或建议，随时告诉我~ 😊
