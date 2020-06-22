##
## EPITECH PROJECT, 2020
## CNA_trade_2019
## File description:
## Makefile
##

all:
	cp trade.py trade
	chmod +x trade

clean:
	rm trade

fclean: clean

re: fclean all