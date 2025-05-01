from typing import Callable, Generator
import re

def generator_numbers (text: str) -> Generator[float, None, None] :
        padded_text = f' {text} '
        pattern = r'\s(\d+(?:\.\d+)?)\s'
        matches = re.findall(pattern, padded_text)
        for number in matches:
            yield float(number)
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))