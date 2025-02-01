import random
import string

class GibberishGenerator:
    """生成胡言乱语的工具类"""
    
    def __init__(self, word_length_range=(3, 10), sentence_length_range=(5, 15)):
        """
        初始化生成器。
        :param word_length_range: 每个单词的长度范围（最小长度，最大长度）。
        :param sentence_length_range: 每个句子的单词数量范围（最小单词数，最大单词数）。
        """
        self.word_length_range = word_length_range
        self.sentence_length_range = sentence_length_range

    def generate_word(self):
        """生成一个随机单词"""
        length = random.randint(*self.word_length_range)  # 解包元组作为参数
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    def generate_sentence(self):
        """生成一个随机句子"""
        num_words = random.randint(*self.sentence_length_range)  # 解包元组作为参数
        words = [self.generate_word() for _ in range(num_words)]
        return ' '.join(words).capitalize() + '.'

    def generate_gibberish(self, length=10):
        """
        生成指定长度的胡言乱语。
        :param length: 生成的句子数量。
        :return: 一段无意义的文本。
        """
        return ' '.join(self.generate_sentence() for _ in range(length))

# if __name__ == "__main__":
#     # 示例用法
#     generator = GibberishGenerator()

#     # 生成 5 句无意义的搜索内容
#     for i in range(5):
#         gibberish_text = generator.generate_gibberish(length=1)
#         print("生成的胡言乱语搜索内容：")
#         print(gibberish_text)
