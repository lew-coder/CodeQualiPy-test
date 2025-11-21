"""
HCS503 - Data Structures and Algorithms
Final Assessment Unit 2
By Lewis Edwards - Uni ID: 2310187
"""

# Importing the relevant modules for this program.

import math
import hashlib
import sys
import drawsvg as dw


class Point:  # (II) Creating a Point class using x & y coordinates to instantiate point objects.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # Function to return strings of Point objects.
        return f"({self.x}, {self.y})"

    def distance(self, other_point):  # Function to determine distance between 2 chosen points.
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (math.sqrt(dx ** 2 + dy ** 2))

    def neighbours(self, origin, max_distance):  # Function to determine neighbouring points within a distance of 20.
        i = 1
        for i in range(len(y_list)):
            p2 = Point(x_list[i], y_list[i])
            other_point = p2
            i += 1
            if 0 < p1.distance(p2) < max_distance:
                print(f"Point {point_a_ref}:", p1, "->", f"Point {i}:", p2, "- Distance:", p1.distance(p2))
        return

    def edges():  # Function to determine number of edges between neighbours in the dataset.
        i = 1
        j = 1
        number_edges = 0
        for i in range(len(y_list)):
            p1 = Point(x_list[i], y_list[i])
            i += 1
            for j in range(len(y_list)):
                p2 = Point(x_list[j], y_list[j])
                j += 1
                if 0 < p1.distance(p2) <= 20:
                    number_edges += 1
        return number_edges

    def prim_edges():  # Function to return a Matrix of all distances to neighbours in the dataset including 0's for distances > 20.
        i = 1
        j = 1
        matrix = []
        for i in range(len(y_list)):
            coordinate = []
            p1 = Point(x_list[i], y_list[i])
            i += 1
            for j in range(len(y_list)):
                p2 = Point(x_list[j], y_list[j])
                j += 1
                if 0 < p1.distance(p2) <= 20:
                    coordinate += ([p1.distance(p2)])
                else:
                    coordinate += [0]
            matrix.append(coordinate)
        return matrix

    def time_complexity():  # Method to determine which Minimum Spanning Tree algorithm to use.
        v = len(y_list)
        graph_edge = Point.edges()
        e = (graph_edge / 2)  # Halving the number of edges to remove double connections from the calculation.
        kruskal = v + (e * math.log(v, 2) * e) + (e * v)  # Time complexity = O(V + ElogE + EV)
        prim = v * v * v  # Time complexity = O(V^3),
        # Source: https://pythonwife.com/kruskal-and-prims-algorithm-in-python/

        if kruskal < prim:
            print("(V) The algorithm with the best time complexity is Kruskal:", kruskal, "<", prim, "\n")
        elif kruskal > prim:
            print("(V) The algorithm with the best time complexity is Prim's:", prim, "<", kruskal, "\n")
        elif kruskal == prim:
            print("(V) The time complexity for both algorithms is the same:", kruskal, "=", prim, "\n")
        else:
            print("(V) Error. \n")


# Implementing a Graph class to instantiate a graph object.
# using the previous Point & Neighbour values to represent vertices and edges on the MST.

class Graph:  # (IV)
    def __init__(self, vertices, edge, nodes):
        self.vertices = vertices
        self.edge = edge
        self.nodes = nodes
        self.MST = []
        self.Drawing = []

    def print_solution(self):  # Function to print the MST in writing.
        for s, d, w in self.MST:
            print("Point %s -> Point %s: Distance %s" % (s, d, w))

    def prims_algorithm(self):  # (V & VI) Function to implement Prim's Algorithm, Source: https://pythonwife.com/kruskal-and-prims-algorithm-in-python/
        print("Using Prim's Algorithm:")
        print("The following is a list of points and the order in which they connect on the MST: \n")
        visited = [0] * self.vertices
        edge = 0
        visited[0] = True
        f = dw.Drawing(150, 150, origin=(-25, -25))
        f.set_pixel_scale(2)
        while edge < self.vertices - 1:
            min = sys.maxsize
            for i in range(self.vertices):
                if visited[i]:
                    for j in range(self.vertices):
                        if ((not visited[j]) and self.edge[i][j]):
                            if min > self.edge[i][j]:
                                min = self.edge[i][j]
                                s = i
                                d = j
            line = dw.Line(x_list[s], y_list[s], x_list[d], y_list[d], stroke="blue")
            circle1 = dw.Circle(x_list[s], y_list[s], 0.25, stroke="red", fill="none")
            circle2 = dw.Circle(x_list[d], y_list[d], 0.25, stroke="red", fill="none")
            f.append(line)
            f.append(circle1)
            f.append(circle2)
            self.MST.append([self.nodes[s], self.nodes[d], self.edge[s][d]])
            visited[d] = True
            edge += 1
        self.print_solution()
        f.save_svg(r"C:\Users\lewis\Documents\Minimum Spanning Tree.svg")
        d
        print("\n(VI) Refer to the attached .svg file for the visual MST representation.")


# Dataset for this Assignment:

x_list = list(range(1, 101))
y_list = (20, 93, 72, 35, 54, 95, 25, 37, 29, 72,
          65, 66, 49, 43, 35, 61, 97, 66, 64, 22,
          83, 69, 19, 21, 69, 40, 35, 81, 15, 41,
          74, 12, 3, 65, 31, 12, 48, 68, 41, 40,
          99, 13, 70, 30, 20, 35, 84, 96, 1, 93,
          61, 83, 24, 27, 93, 86, 96, 43, 10, 51,
          27, 87, 40, 35, 83, 44, 15, 89, 71, 79,
          25, 84, 43, 49, 66, 0, 88, 80, 4, 3,
          74, 10, 41, 45, 75, 34, 41, 44, 50, 99,
          41, 37, 26, 6, 94, 94, 76, 48, 32, 42)


# (I) Checking validity of test data using a SHA256 checksum:
print(" \n(I) Validating Test Data: \n")
y_string = str("209372355495253729726566494335619766642283691921694035811541741236"
               "531124868414099137030203584961936183242793869643105127874035834415"
               "89717925844349660888043741041457534414450994137266949476483242")
y_verification = "5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a"

# Source: https://medium.com/@wepypixel/python-sha256-secure-hashing-implementation-pypixel-7b8434a9b244
hash_string = hashlib.sha256(y_string.encode("utf-8"))
hex_dig = hash_string.hexdigest()

print("Hashed String:", hex_dig)
print("Provided Hashed String:", y_verification)

if hex_dig == y_verification:  # Verification of SHA256 checksum.
    print("Verification: True | Hashed String == Provided String \n")
else:
    print("Verification: False | Hashed String != Provided String \n")


# (II) This section refers to the Point class.
print("(II) Refer to the Point class in the program.\n")
# Printing a statement to keep linear progression through assignment questions.


# (III) This section is used for displaying all neighbours of each point within a distance of 20.
point_a = 0
point_a_ref = 1
closeness = 20

print("(III) The following is a list of all points and their neighbours within a distance of 20: \n")
for i in range(100):
    p1 = Point(x_list[point_a], y_list[point_a])
    p1.neighbours(origin=p1, max_distance=closeness)
    point_a += 1
    point_a_ref += 1
    print("")


# (IV) This section refers to the Graph class.
print("(IV) Refer to the Graph class in the program.\n")
# Printing a statement to keep linear progression through assignment questions.

# (V) Applying Prims algorithm for implementing an MST.
Point.time_complexity()  # Displaying the reason for choice of algorithm.

edges = Point.prim_edges()
vertices = []
vertices_no = 0
nodes = x_list

for i in range(len(y_list)):
    vertices.append([Point(x_list[vertices_no], y_list[vertices_no])])
    vertices_no += 1

g = Graph(len(y_list), edges, nodes)  # Instantiating the data into the graph class.
g.prims_algorithm()  # Calling on Prims algorithm to develop the MST.