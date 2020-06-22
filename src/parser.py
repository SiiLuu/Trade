##
## EPITECH PROJECT, 2020
## CNA_trade_2019
## File description:
## parser
##

import  sys
import  src.classes
import  src.algorithm

def parsing(inp, money, candle):

    if "update game stacks" in inp:
        money.BTC = float(inp.split(" ")[3].split(",")[0].split(":")[1])
        money.ETH = float(inp.split(" ")[3].split(",")[1].split(":")[1])
        money.USDT = float(inp.split(" ")[3].split(",")[2].split(":")[1])
    if "update game next_candles" in inp:
        candle.CLOSE_BTC_ETH.append(float(inp.split(" ")[3].split(";")[0].split(",")[5]))
        candle.VOLUME_BTC_ETH.append(float(inp.split(" ")[3].split(";")[0].split(",")[6]))
        candle.CLOSE_USDT_ETH.append(float(inp.split(" ")[3].split(";")[1].split(",")[5]))
        candle.VOLUME_USDT_ETH.append(float(inp.split(" ")[3].split(";")[1].split(",")[6]))
        candle.CLOSE_USDT_BTC.append(float(inp.split(" ")[3].split(";")[2].split(",")[5]))
        candle.VOLUME_USDT_BTC.append(float(inp.split(" ")[3].split(";")[2].split(",")[6]))

def doActions(inp, money, candle, trade):

    if ("action order 2000" in inp):
        src.algorithm.execAlgo(money, candle, trade)

def mainLoop():

    money = src.classes.Money()
    candle = src.classes.Candle()
    trade = src.classes.Trade()
    i = 0
    while (True):
        try:
            inp = input()
            parsing(inp, money, candle)
            doActions(inp, money, candle, trade)
            i += 1
        except EOFError:
            break
