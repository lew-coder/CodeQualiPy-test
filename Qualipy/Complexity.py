# Initial Code Complexity File

from radon.metrics import h_visit, mi_visit, mi_parameters
from radon.complexity import cc_visit
import sys

filepath = sys.argv[1]
with open(filepath, encoding="utf-8") as f:
    code = f.read()

# Introduction
print("\n\nCode Complexity Metrics:")

# Halstead
halstead = h_visit(code)
print("\nTotal Halstead Volume:", round(halstead.total.volume, 2))

# Cyclomatic
complexity = cc_visit(code)
total_complexity = sum(block.complexity for block in complexity)
print("\nTotal Cyclomatic Complexity:", total_complexity)

# Maintainability
mi = mi_visit(code, multi=True)
print("\nMaintainability Index:", round(mi, 2))

# Additional Metrics
mat = mi_parameters(code)
print("\nLines of Source code:", mat[2])
print("\nNumber of Comments:", round(mat[3]))

# Breakdown of Each Metric
print("\n\nHere is a breakdown of each metric:")
print("\nHalstead Volume: \n")
print(type(halstead))
print(halstead)
print("\n\nCyclomatic Complexity: \n")
for block in complexity:
    print(f"{block.name} - Complexity: {block.complexity}")
else:
    exit(1)