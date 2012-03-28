#!/usr/bin/env python
__author__= "Mariya Semenikhina"
###########################################
# monkey.py v1.0
# Usage: python monkey.py sumofdigits
# to solve the monkey problem
"""
There is a monkey which can walk around on a planar grid. The monkey can
move one space at a time left, right, up or down. That is, from (x, y) the
monkey can go to (x+1, y), (x-1, y), (x, y+1), and (x, y-1). Points where
the sum of the digits of the x coordinate plus the sum of the digits of the
y coordinate are greater than 25 are inaccessible to the monkey. For
example, the point (59, 79) is inaccessible because 5 + 9 + 7 + 9 = 30,
which is greater than 25. The sum of the digits for negative coordinates
should be calculated based on the absolute value.  For example, the sum of
the digits of (-22, 12) equals the sum of the digits of (22, 12).
How many points can the monkey access if it starts at (0, 0), including (0,
0) itself?
"""
###########################################
import sys

#pre: sum of digits default: 25
#post: returns the lonest straight path the monkey can take
#      in other words the graph boundary
#ex: max sum of digits for 11 is 2+9 so longest straight path is (0,11)
def longestpath(sumofdigits):
    try:
	i = sumofdigits
	pathstr = ''
	while i > 9:
	    i = i-9 # 9 is the largest component contributing to the sum of digits
                    # max sum is set at reg ex: '[0-9]+[9]*'
	    pathstr+='9'
	pathstr = str(i+1) + pathstr
	return int(pathstr)
    except:
	return 1

def usage():
    print "Usage:  {0} max sum of digits".format(os.path.basename(sys.argv[0]))

#pre: (optional) argv[1] max sum of digits
#     networkx 1.6 module easy_install networkx
#post: Points the monkey can access if it starts at (0, 0)
import argparse
def main():

    args = sys.argv[1:]
    if "-h" in args or "--help" in args:
        usage()
        sys.exit(2)
    try:
	sumofdigits = int(args[0])
    except:
	sumofdigits = 25 
    axislength = longestpath(sumofdigits)

    # python package networkx
    # easy_install networkx

    import networkx as nx
    # MultiGraph can be multiple disconnected graphs
    # for the unaccessable "bubbles" whose value is <= sumofdigits
    G = nx.MultiGraph() 
    try:
	for x in xrange(0,axislength):
	     for y in xrange(0,axislength):
		#sum of digits on current location, map str to int
		if sum(map(int,str(x)))+sum(map(int,str(y))) <= sumofdigits:
		    #find the edge moving forward, take advantage of symmetry
		    if sum(map(int,str(x+1)))+sum(map(int,str(y))) <= sumofdigits:
			#Edges like ('0,0', '0,1'),..
		        G.add_edge(str(x)+','+str(y),str(x+1)+','+str(y)) 
		        G.add_edge(str(x)+','+str(y),str(x)+','+str(y+1))
    except:
	print 'main error building edges graph'
	sys.exit()
    # biggest connected component is always the first
    # axislength gets counted twice
    # there's 4 axis of symetry
    print 'Monkey can bounce to {0} squares!'.format(len(nx.connected_components(G)[0])*4-2*axislength)
if __name__=="__main__": 
    main()


