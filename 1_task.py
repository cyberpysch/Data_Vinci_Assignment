#input_text = "Hello world! Hello Python."
#output = {"hello": 2, "world": 1, "python": 1}
from collections import Counter
import re
def count_str(string:str):
    filtered_str = re.findall(r'\b[a-z]+\b', string.lower())
    counter = Counter(filtered_str)
    return dict(counter)

print(count_str("Hello world! Hello Python."))