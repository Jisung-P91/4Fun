import pandas as pd
import matplotlib.pyplot as plt

from datetime import date, datetime, timedelta

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

for OP_dates in perdelta(date(1997, 7, 19), date(2020, 5, 25), timedelta(days=7)):
        print (OP_dates)

OP_dates_df = pd.DataFrame(OP_dates)

print(op_dates_df.tail(3))



