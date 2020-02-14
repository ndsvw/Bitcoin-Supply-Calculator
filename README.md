# Bitcoin-Supply-Calculator

A very simple algorithm that calculates the total bitcoin supply after a given block

## Explanation

The Bitcoin block reward (the reward a miner gets for mining a block) halves every 210,000 blocks (~ 4 years).

The first block was mined on 2009-01-03 by "Satoshi Nakamoto".

The first halving was on 2012-11-28 (from 50 BTC to 25 BTC) and the second one on 2016-07-09 (from 25 BTC to 12.5 BTC)... There are 32 halvings and 210,000 blocks after that (in 2140) the reward will drop from 1 Satoshi (0,00000001 Bitcoins) to 0 Bitcoins.

*This algorithm calculates the total BTC-supply after a given block regarding this halving-rule. The calculated value is the hypothetical largest possible supply after the given block. Lost bitcoins (because someone lost his or her private key(s), died without giving someone access to the bitcoins, etc) are of course not considered by this algorithm.*

There is an upper bound of around 21M bitcoins (actually only 20,999,999.9769).

More about the reward-halving: https://www.bitcoinmining.com/what-is-the-bitcoin-block-reward/

More about why it's not 21M: https://bitcoin.stackexchange.com/questions/38994/will-there-be-21-million-bitcoins-eventually

## Examples

#### 2009-01-03:
```python
btcSupplyAtBlock(0)   # returns 50
btcSupplyAtBlock(1)   # returns 100
btcSupplyAtBlock(2)   # returns 150
btcSupplyAtBlock(3)   # returns 200
btcSupplyAtBlock(4)   # returns 250
```

#### 2012-11-28:
```python
btcSupplyAtBlock(209998)   # returns 10,499,950
btcSupplyAtBlock(209999)   # returns 10,500,000
btcSupplyAtBlock(210000)   # returns 10,500,025
btcSupplyAtBlock(210001)   # returns 10,500,050
btcSupplyAtBlock(210002)   # returns 10,500,075
```

#### 2016-07-09:
```python
btcSupplyAtBlock(419998)   # returns 15,749,975
btcSupplyAtBlock(419999)   # returns 15,750,000
btcSupplyAtBlock(420000)   # returns 15,750,012.5
btcSupplyAtBlock(420001)   # returns 15,750,025.0
btcSupplyAtBlock(420002)   # returns 15,750,037.5
```

#### 2020:
```python
btcSupplyAtBlock(629998)   # returns 18,374,987.5
btcSupplyAtBlock(629999)   # returns 18,375,000.0
btcSupplyAtBlock(630000)   # returns 18,375,006.25
btcSupplyAtBlock(630001)   # returns 18,375,012.5
btcSupplyAtBlock(630002)   # returns 18,375,018.75
```

#### 2024:
```python
btcSupplyAtBlock(839998)   # returns 19,687,493.75
btcSupplyAtBlock(839999)   # returns 19,687,500.0
btcSupplyAtBlock(840000)   # returns 19,687,503.125
btcSupplyAtBlock(840001)   # returns 19,687,506.25
btcSupplyAtBlock(840002)   # returns 19,687,509.375
```

#### over time:
```python
btcSupplyAtBlock(10)       # returns 550
btcSupplyAtBlock(100)      # returns 5,050
btcSupplyAtBlock(1000)     # returns 50,050
btcSupplyAtBlock(10000)    # returns 500,050
btcSupplyAtBlock(100000)   # returns 5,000,050
btcSupplyAtBlock(250000)   # returns 11,500,025.0
btcSupplyAtBlock(500000)   # returns 16,750,012.5
btcSupplyAtBlock(750000)   # returns 19,125,006.25
btcSupplyAtBlock(1000000)  # returns 20,187,503.125
btcSupplyAtBlock(2500000)  # returns 20,994,384.78851406
```

#### end of reward halvings:
```python
btcSupplyAtBlock(6929996)  # returns 20,999,999.97689997
btcSupplyAtBlock(6929997)  # returns 20,999,999.97689998
btcSupplyAtBlock(6929998)  # returns 20,999,999.97689999
btcSupplyAtBlock(6929999)  # returns 20,999,999.9769
btcSupplyAtBlock(6930000)  # returns 20,999,999.9769
btcSupplyAtBlock(6930001)  # returns 20,999,999.9769
btcSupplyAtBlock(6930002)  # returns 20,999,999.9769
btcSupplyAtBlock(6930003)  # returns 20,999,999.9769
btcSupplyAtBlock(6930004)  # returns 20,999,999.9769
```