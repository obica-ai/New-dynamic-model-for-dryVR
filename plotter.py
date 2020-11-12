import argparse
import pygraphviz as pgv

from src.plotter.parser import parse
from src.plotter.plot import plot

parser = argparse.ArgumentParser(
    description='This is plotter script for DryVR generated reach tube output'
)

parser.add_argument('-f', type=str, default='output/reachtube.txt', help='file path for reach tube')
parser.add_argument('-y', type=str, default='[1]',
                    help='dimension number you want to plot, ex [1,2], default first dimension')
parser.add_argument('-x', type=str, default='0', help='dimension number you want to plot, ex 0, default time')
parser.add_argument('-o', type=str, default='plotResult.png', help='output file name')
args = parser.parse_args()

try:
    file_handle = open(args.f, 'r')
except IOError:
    print ('File does not exist')

lines = file_handle.readlines()
init_node, y_min, y_max = parse(lines)

ydim = eval(args.y)
xdim = eval(args.x)
# Using DFS algorithm to Draw image per Node
stack = [init_node]
while stack:
    cur_node = stack.pop()
    for c in cur_node.child:
        stack.append(cur_node.child[c])
    plot(cur_node, ydim, y_min, y_max, xdim)

# Construct node graph
G = pgv.AGraph(strict=True, directed=True)

# Using DFS algorithm to add node and edge of the graph
G.add_node(init_node.file_name, image='output/' + init_node.file_name + '.png')
stack = [init_node]
while stack:
    cur_node = stack.pop()
    for c in cur_node.child:
        child_node = cur_node.child[c]
        G.add_node(child_node.file_name, image='output/' + child_node.file_name + '.png')
        G.add_edge(cur_node.file_name, child_node.file_name)
        stack.append(child_node)
G.layout(prog='dot')
G.draw(args.o)  # write previously positioned graph to PNG file
