##
## EPITECH PROJECT, 2020
## CNA_trade_2019
## File description:
## help
##

import sys

def helpMe():

    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("USAGE\n\t./trade\n\nDESCRIPTION")
        exit(0)
