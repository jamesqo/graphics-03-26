from display import *
from draw import *
from THE_PARSER import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges, polygon = [], []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', edges, polygon, transform, screen, color )
