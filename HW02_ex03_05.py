#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.

# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body


#Symbols used in the graph.
node = '+'
v_edge = '|'
h_edge = '-'

#Function for printing a set of any four symbols side by side, with continuous printing.
def print_four(x):
	print x, x, x, x,

#Function for printing a single segment of an edge row.
def print_edge_seg():
	print node, 
	print_four(h_edge)

#Function for creating a set of four segments to create any row.
def call_four(f):
	f()
	f()
	f()
	f()

#Function for printing the ending node of an edge row
#and prompting print to continue on the following row.
def print_right_edge_node():
	print node

#Function for printing an edge row. 
def draw_edge_row():
	call_four(print_edge_seg)
	print_right_edge_node()

#Function for printing a single segment of a body row.
def print_body_seg():
	print v_edge,
	print_four(' ')

#Function for printing the ending node of a body row
#and prompting print to continue on the following row.
def print_right_node():
	print v_edge

#Function for printing a body row. 
def draw_body_row():
	call_four(print_body_seg)
	print_right_node()

#Function to print a block of rows.
def draw_block():
	draw_edge_row()
	call_four(draw_body_row)

#Function to print grid.
def draw_grid():
	call_four(draw_block)
	draw_edge_row()

# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    draw_grid()

if __name__ == "__main__":
    main()