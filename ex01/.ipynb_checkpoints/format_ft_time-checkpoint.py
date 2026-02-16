import time as tm
from datetime import date as dt

second = tm.time()
print("Seconds since January 1, 1970: " f"{second:,.4f}" " or " f"{second:.2e}" " in scientific notation")
print(dt.today().strftime("%a %d %Y"))