# can we show AST from radon?
# https://radon.readthedocs.io/en/latest/api.html
from radon.complexity import cc_rank, cc_visit
import sys

def analyze(filepath):
    with open(filepath, encoding="utf-8") as f:
        code = f.read()
        print(f"Loaded {len(code)} characters from {filepath}")
    results = cc_visit(code)

    for block in results:
        rank = cc_rank(block.complexity)
        print(f'{block.name} ({block.__class__.__name__}) - Complexity: {block.complexity}')
    if any(b.complexity > 10 for b in results):
        print("Complexity Threshold of 10 Exceeded.")
        exit(1)

if __name__ == "__main__":
    try:
        analyze(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}")
        exit(1)