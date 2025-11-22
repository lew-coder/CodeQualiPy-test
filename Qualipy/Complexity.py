# Initial Code Complexity File

from radon.metrics import h_visit, mi_visit, mi_parameters
from radon.complexity import cc_visit
import sys

filepath = sys.argv[1]
with open(filepath, encoding="utf-8") as f:
    code = f.read()

# Halstead
halstead = h_visit(code)
print("\nTotal Halstead Volume:", halstead.total.volume)

# Cyclomatic
complexity = cc_visit(code)
total_complexity = sum(block.complexity for block in complexity)
print("\nTotal Cyclomatic Complexity:", total_complexity)

# Maintainability
mi = mi_visit(code, multi=True)
print("\nMaintainability Index:", mi)

#Metrics
mat = mi_parameters(code)
print("\nLines of Source code:", mat[2])
print("\nNumber of Comments:", mat[3])


breakdown = input(str("\nWould you like to see a block by block breakdown instead? y/n \n"))
if breakdown == "y":
    print("\n\nHalstead Volume: \n")
    print(type(halstead))
    print(halstead)
    print("\n\nCyclomatic Complexity: \n")
    for block in complexity:
        print(f"{block.name} - Complexity: {block.complexity}")
else:
    exit(1)