#!/usr/bin/python3
# Table Printer
# This function takes a list of strings and displays it in a well-organized table.
# Each column should be right-justified
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(lsts:list):
    for table in lsts:
        print(table)

printTable(tableData)