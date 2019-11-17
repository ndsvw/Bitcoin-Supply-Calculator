# Bitcoin-Supply-Calculator

A very simple algorithm that calculates the total bitcoin supply after a given block

## Examples

#### 2009-01-03:
```python
btcSupplyAtBlock(0)   # returns 50
btcSupplyAtBlock(1)   # returns 100
btcSupplyAtBlock(2)   # returns 150
btcSupplyAtBlock(3)   # returns 200
btcSupplyAtBlock(3)   # returns 250
```

#### 2012-11-28:
```python
btcSupplyAtBlock(209998)   # returns 10,499,950
btcSupplyAtBlock(209999)   # returns 10,500,000
btcSupplyAtBlock(210000)   # returns 10,500,025
btcSupplyAtBlock(210001)   # returns 10,500,050
btcSupplyAtBlock(210001)   # returns 10,500,075
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