# The Influence of Institutional Investors on Initial Coin Offering Performance
# Rebecka: 24864@student.hhs.se
# Maja: 24845@student.hhs.se

import numpy as np
import pandas as pd
import matplotlib

# Change the path to the path of your computer to reach the CSV file of "Final dataset BHAR 3"
# Now you are ready to run the code

# Change the path to the CSV file by copying your path and insert inside the paranthesis below
df = pd.read_csv("/Users/majastromberg/Desktop/Data finansuppsats/BHAR2.csv", delimiter=";")
# Columns:
    #Id, Namn, Time-start, Date 180, Price 1, mktcap 1, Price 180, mktcap 180

df = df.stack().str.replace(',', '.').unstack()

df["Price 180"] = pd.to_numeric(df["Price 180"], downcast="float")
df["Price 1"] = pd.to_numeric(df["Price 1"], downcast="float")
df["mktcap 180"] = pd.to_numeric(df["mktcap 180"], downcast="float")

df = df.drop("Id", axis=1)

BHAR = []
f = open("BHAR Resultat.csv", "w")

for i in range(len(df)):
    print(i)
    var_1 = (df.loc[i, "Price 180"] - df.loc[i, "Price 1"]) / df.loc[i, "Price 1"]
    namn = df.loc[i, "Namn"]
    var_2 = 0

    for j in range(len(df)):
        if j != i:
            taljer = df.loc[j, "mktcap 180"]
            namer = df["mktcap 180"].sum() - df.loc[i, "mktcap 180"]
            kvot = taljer/namer
            var_3 = (df.loc[j, "Price 180"] - df.loc[j, "Price 1"]) / df.loc[j, "Price 1"]
            var_2 += (kvot * var_3)
    var_4 = var_1 - var_2
    BHAR.append([namn, var_4])

    write_string = str(namn) + "," + str(var_4) + "\n"
    f.write(write_string)

for i in BHAR:
    print(i)
