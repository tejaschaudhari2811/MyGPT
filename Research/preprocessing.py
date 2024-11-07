import re
from typing import AnyStr
import tiktoken

class SimpleTokenizer:
    def __init__(self, vocab = None):
        self.vocab = vocab

    def split_test(self, text) -> AnyStr:
        # TODO: Change this code to encode function that converts the text to vocabulary
        pattern = r'([,.;:!@#$%^&*()\']|--|\s)'
        response=re.split(pattern, text)
        response = [item for item in response if item.strip()]
        return response
    
    def decode(self, ids):
        pass


if __name__=="__main__":
    tokenizer = SimpleTokenizer()
    # print(tokenizer.split_test("Hello, world. Is this-- a test?").__name__)
    tokenizer = tiktoken.get_encoding("gpt2")
    text = "Akwirw ier"
    print(tokenizer.encode(text))
    print(tokenizer.decode([33901, 86, 343, 86, 220, 959]))
    exit = input("Press enter to exit.")
    