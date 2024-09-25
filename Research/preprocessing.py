import re
from typing import AnyStr

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
    print(tokenizer.split_test("Hello, world. Is this-- a test?").__name__)
    exit = input("Press enter to exit.")
    