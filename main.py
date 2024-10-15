import sqlite3 as sql
import pandas as pd

# loads SQL magic into notebook
%load_ext sql
# %reload_ext sql
# connects SQL magic notebook backend to the Basketball Dataset 
%sql sqlite:///../input/basketball/basketball.sqlite 

