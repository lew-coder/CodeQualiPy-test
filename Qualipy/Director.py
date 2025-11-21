import sys

from Qualipy.CCcomplexity import analyze as cc_analyze
from Qualipy.CChalstead import analyze as h_analyze

if __name__ == "__main__":
    filepath = sys.argv[1]
    print(f"== Cyclomatic Complexity ==")
    cc_analyze(filepath)
    print(f"== Halstead Metrics ==")
    h_analyze(filepath)