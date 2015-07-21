#!/usr/bin/env python
# encoding: utf-8

'''
 Copyright (C) 2015

 Cristiano Antonio de Souza - cristianoantonio.souza10@gmail.com
 Gabriel Custódio Martins - gcmartins93@gmail.com

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''

from file_parser import FileParser
from settings import Settings
from dijkstra import Dijkstra
from a_star import AStar
from graph import Graph
from menu import Menu
import getopt, sys

def usage():
    print('Usage:\n  search_algs [<arguments>]\n')
    print('Arguments:\n  -h or --help:\tShow help options\n' \
          '  -f or --file:\tSpecify file to parse\n  -d:\t\tEnables debugging mode\n')

def main(argv):
    _file = "Entrada.txt"

    try:
        opts, args = getopt.getopt(argv, 'hf:d', ['help', 'file='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt == '-d':
            Settings.debug = True
        elif opt in ('-f', '--file'):
            _file = arg

    parser = FileParser(_file)
    content = parser.read_content()

    graph = Graph()
    graph.build(content['vertices'], content['caminho'], content['h'])

    start = graph.get_vertex(content['início'][0][0])
    final = graph.get_vertex(content['final'][0][0])

    dijkstra = Dijkstra(graph, start, final)
    a_star = AStar(graph, start, final)

    Menu(graph, dijkstra, a_star).run()

if __name__ == '__main__':
    main(sys.argv[1:])
