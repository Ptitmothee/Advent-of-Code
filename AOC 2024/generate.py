import os, sys

cur_dir = os.path.abspath(os.path.dirname(__file__))

for i in range(12,26):
    with open(cur_dir + "\Day " + str(i) + "\solution.py", "r+", encoding="utf-8") as file:
        file.truncate(0)
        file.write(f'\
\"\"\"\nAdvent of Code 2024 : Day {i}\n\"\"\"\nimport sys\nimport os\n\n\
# Add the parent directory of `main.py` to `sys.path`\ncur_dir = os.path.abspath(os.path.dirname(__file__))\n\
parent_dir = os.path.abspath(os.path.join(cur_dir, ".."))\n\
sys.path.insert(0, parent_dir)\n\
import module\n\
PATH = cur_dir + "/input.txt"\n\
with open(PATH, "r", encoding="utf-8") as file:\n\tpass')
