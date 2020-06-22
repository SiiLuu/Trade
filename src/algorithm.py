##
## EPITECH PROJECT, 2020
## CNA_trade_2019
## File description:
## algorithm
##

import sys

def buy_usdt_in_eth(money, candle, trade, check):

    if (candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] <= min(candle.CLOSE_USDT_ETH)):
        if (money.USDT > candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]):
            fivePercent = (money.USDT * 15) / 100
            vol = fivePercent / candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_ETH {}".format(vol)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - min(candle.CLOSE_USDT_ETH)) < 5 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - min(candle.CLOSE_USDT_ETH)) > 0):
        if (money.USDT > candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]):
            fivePercent = (money.USDT * 12.5) / 100
            vol = fivePercent / candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_ETH {}".format(vol)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - min(candle.CLOSE_USDT_ETH)) < 10 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - min(candle.CLOSE_USDT_ETH)) > 0):
        if (money.USDT > candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]):
            fivePercent = (money.USDT * 8.5) / 100
            vol = fivePercent / candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_ETH {}".format(vol)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - min(candle.CLOSE_USDT_ETH)) < 15 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - min(candle.CLOSE_USDT_ETH)) > 0):
        if (money.USDT > candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]):
            fivePercent = (money.USDT * 6.5) / 100
            vol = fivePercent / candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_ETH {}".format(vol)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - min(candle.CLOSE_USDT_ETH)) < 20 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - min(candle.CLOSE_USDT_ETH)) > 0):
        if (money.USDT > candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]):
            fivePercent = (money.USDT * 4.5) / 100
            vol = fivePercent / candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_ETH {}".format(vol)


    if (candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] >= max(candle.CLOSE_USDT_ETH)):
        if (money.ETH != 0 and money.ETH > ((money.ETH * 15) / 100)):
            sold = (money.ETH * 15) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_ETH {}".format(sold)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) < 5 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) > 0):
        if (money.ETH != 0 and money.ETH > ((money.ETH * 12.5) / 100)):
            sold = (money.ETH * 12.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_ETH {}".format(sold)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) < 10 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) > 0):
        if (money.ETH != 0 and money.ETH > ((money.ETH * 10) / 100)):
            sold = (money.ETH * 10) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_ETH {}".format(sold)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) < 15 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) > 0):
        if (money.ETH != 0 and money.ETH > ((money.ETH * 8.5) / 100)):
            sold = (money.ETH * 8.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_ETH {}".format(sold)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) < 20 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) > 0):
        if (money.ETH != 0 and money.ETH > ((money.ETH * 6.5) / 100)):
            sold = (money.ETH * 6.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_ETH {}".format(sold)
    elif (abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) < 25 and
        abs(candle.CLOSE_USDT_ETH[len(candle.CLOSE_USDT_ETH) - 1] - max(candle.CLOSE_USDT_ETH)) > 0):
        if (money.ETH != 0 and money.ETH > ((money.ETH * 4.5) / 100)):
            sold = (money.ETH * 4.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_ETH {}".format(sold)
    return check

def buy_usdt_in_btc(money, candle, trade, check):

    if (candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] <= min(candle.CLOSE_USDT_BTC)):
        if (money.USDT > candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]):
            fivePercent = (money.USDT * 16) / 100
            vol = fivePercent / candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_BTC {}".format(vol)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - min(candle.CLOSE_USDT_BTC)) < 5 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - min(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.USDT > candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]):
            fivePercent = (money.USDT * 13.5) / 100
            vol = fivePercent / candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_BTC {}".format(vol)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - min(candle.CLOSE_USDT_BTC)) < 10 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - min(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.USDT > candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]):
            fivePercent = (money.USDT * 9.5) / 100
            vol = fivePercent / candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_BTC {}".format(vol)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - min(candle.CLOSE_USDT_BTC)) < 15 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - min(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.USDT > candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]):
            fivePercent = (money.USDT * 7.5) / 100
            vol = fivePercent / candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_BTC {}".format(vol)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - min(candle.CLOSE_USDT_BTC)) < 20 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - min(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.USDT > candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]):
            fivePercent = (money.USDT * 5.5) / 100
            vol = fivePercent / candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy USDT_BTC {}".format(vol)


    if (candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] >= max(candle.CLOSE_USDT_BTC)):
        if (money.BTC != 0 and money.BTC > ((money.BTC * 16) / 100)):
            sold = (money.BTC * 16) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_BTC {}".format(sold)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) < 5 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.BTC != 0 and money.BTC > ((money.BTC * 14) / 100)):
            sold = (money.BTC * 14) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_BTC {}".format(sold)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) < 10 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.BTC != 0 and money.BTC > ((money.BTC * 12) / 100)):
            sold = (money.BTC * 12) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_BTC {}".format(sold)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) < 15 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.BTC != 0 and money.BTC > ((money.BTC * 10) / 100)):
            sold = (money.BTC * 10) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_BTC {}".format(sold)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) < 20 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.BTC != 0 and money.BTC > ((money.BTC * 7.5) / 100)):
            sold = (money.BTC * 7.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_BTC {}".format(sold)
    elif ((abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) < 25 and
        abs(candle.CLOSE_USDT_BTC[len(candle.CLOSE_USDT_BTC) - 1] - max(candle.CLOSE_USDT_BTC)) > 0)):
        if (money.BTC != 0 and money.BTC > ((money.BTC * 5.5) / 100)):
            sold = (money.BTC * 5.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell USDT_BTC {}".format(sold)
    return check

def buy_btc_in_eth(money, candle, trade, check):

    if (candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] <= min(candle.CLOSE_BTC_ETH)):
        if (money.BTC > candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]):
            fivePercent = (money.BTC * 15) / 100
            vol = fivePercent / candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy BTC_ETH {}".format(vol)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - min(candle.CLOSE_BTC_ETH)) < 5 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - min(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.BTC > candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]):
            fivePercent = (money.BTC * 12.5) / 100
            vol = fivePercent / candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy BTC_ETH {}".format(vol)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - min(candle.CLOSE_BTC_ETH)) < 10 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - min(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.BTC > candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]):
            fivePercent = (money.BTC * 8.5) / 100
            vol = fivePercent / candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy BTC_ETH {}".format(vol)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - min(candle.CLOSE_BTC_ETH)) < 15 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - min(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.BTC > candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]):
            fivePercent = (money.BTC * 6.5) / 100
            vol = fivePercent / candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy BTC_ETH {}".format(vol)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - min(candle.CLOSE_BTC_ETH)) < 20 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - min(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.BTC > candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]):
            fivePercent = (money.BTC * 4.5) / 100
            vol = fivePercent / candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1]
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "buy BTC_ETH {}".format(vol)


    if (candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] >= max(candle.CLOSE_BTC_ETH)):
        if (money.ETH != 0 and money.ETH > ((money.ETH * 15) / 100)):
            sold = (money.ETH * 15) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell BTC_ETH {}".format(sold)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) < 5 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.ETH != 0 and money.BTC > ((money.ETH * 12.5) / 100)):
            sold = (money.ETH * 12.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell BTC_ETH {}".format(sold)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) < 10 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.ETH != 0 and money.BTC > ((money.ETH * 10) / 100)):
            sold = (money.ETH * 10) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell BTC_ETH {}".format(sold)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) < 15 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.ETH != 0 and money.BTC > ((money.ETH * 8.5) / 100)):
            sold = (money.ETH * 8.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell BTC_ETH {}".format(sold)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) < 20 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.ETH != 0 and money.BTC > ((money.ETH * 6.5) / 100)):
            sold = (money.ETH * 6.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell BTC_ETH {}".format(sold)
    elif ((abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) < 25 and
        abs(candle.CLOSE_BTC_ETH[len(candle.CLOSE_BTC_ETH) - 1] - max(candle.CLOSE_BTC_ETH)) > 0)):
        if (money.ETH != 0 and money.BTC > ((money.ETH * 4.5) / 100)):
            sold = (money.ETH * 4.5) / 100
            check = True
            if (len(trade.BUY) > 0):
                trade.BUY += ";"
            trade.BUY += "sell BTC_ETH {}".format(sold)
    return check

def execAlgo(money, candle, trade):

    trade.BUY = ""
    trade.SELL = ""
    first = buy_usdt_in_eth(money, candle, trade, False)
    second = buy_usdt_in_btc(money, candle, trade, False)
    third = buy_btc_in_eth(money, candle, trade, False)
    if (first == False and second == False and third == False):
        print("pass")
    else:
        print(trade.BUY)
        sys.stderr.write(trade.BUY + "\n")
