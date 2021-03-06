import utils
import datetime as dt
import pandas as pd


def test_isTradable():
    assert(utils.isTradable(dt.date(2020, 7, 1)) == False)
    assert(utils.isTradable(dt.date(2020, 7, 2)) == True)
    assert(utils.isTradable(dt.date(2020, 7, 12)) == False)
    assert(utils.isTradable(dt.date(2020, 7, 13)) == True)


def test_loadData():
    ticker = '388'
    assert(len(utils.loadData(ticker, '', '20200724')) == 8)
    assert(len(utils.loadData(ticker, '20200720', '20200724')) == 5)


def test_calTickSize():
    hkex = pd.read_csv('feeds/388/20200715.csv')
    tencent = pd.read_csv('feeds/700/20200715.csv')
    assert(utils.calTickSize(hkex) == 0.2)
    assert(utils.calTickSize(tencent) == 0.5)


def test_combParams():
    inp = {
        'foo': ['a', 'b'],
        'bar': [1, 2, 3]
    }
    exp = [
        {'foo': 'a', 'bar': 1},
        {'foo': 'a', 'bar': 2},
        {'foo': 'a', 'bar': 3},
        {'foo': 'b', 'bar': 1},
        {'foo': 'b', 'bar': 2},
        {'foo': 'b', 'bar': 3}
    ]
    assert(utils.combParams(inp) == exp)
