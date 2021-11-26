from prettytable import PrettyTable
import math 

HowManyRows = int(input("How Many Rows Are There"))

ClassDifference = int(input("What Is The Difference Between The Classes"))

ClassIntervalR = int(input("What Is The Right Value Of The First Class Difference"))

MidPointX = []
Frequency = []
FXList    = []

for H in range(HowManyRows):
    Frequency.append(float(input(f"Frequency {H+1}")))


# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Number Of Parked Cars / Hour",
                       "Frequency (ƒ)",
                       "Cumulative Frequency",
                       "Upper Class Boundary",
                       "Mid Point (𝑥)",
                       "ƒ𝑥"])


# Add rows
# [Separate] First Row

# Assign First Frequency To Variable To With Later
Y = int(Frequency[0])  # 1
MidPointRow1 = (ClassIntervalR+ClassDifference)-(ClassDifference/2)

                 # Number Of Parked Cars / Hour
myTable.add_row([f"{ClassIntervalR} ≤ X < {ClassIntervalR+ClassDifference}", 
                 # Frequency (ƒ)
                 int(Frequency[0]),
                 # Cumulative Frequency
                 Y,
                 # Upper Class Boundary
                 f"{ClassIntervalR+(ClassDifference)}",
                 # Mid Point (𝑥)
                 MidPointRow1,
                 # ƒ𝑥
                 float(Y)*float(MidPointRow1)
                 ])
MidPointX.append(MidPointRow1)
FXList.append(float(MidPointX[0])*float(Frequency[0]))



# [Separate] Second Row
# Frequency For Second Row
NewCum = Y + int(Frequency[1])  # X = 3 = 1 + 2
MidPointRow2 = (ClassIntervalR+(ClassDifference*2))-(ClassDifference/2)

                 # Number Of Parked Cars / Hour
myTable.add_row([f"{ClassIntervalR+ClassDifference} ≤ X < {ClassIntervalR+(ClassDifference*2)}",  
                 # Frequency (ƒ)
                 int(Frequency[1]),
                 # Cumulative Frequency
                 NewCum,
                 # Upper Class Boundary
                 f"{ClassIntervalR+(ClassDifference*(2))}",
                 # Mid Point (𝑥)
                 MidPointRow2,
                 # ƒ𝑥
                 float(Frequency[1])*float(MidPointRow2)
                 ])
MidPointX.append(MidPointRow2)
FXList.append(float(MidPointX[1])*float(Frequency[1]))


# Rows After Second
for Row in range(HowManyRows-2):
    
    if ClassIntervalR == 0:
        NewCum = NewCum + int(Frequency[Row+2])
        MidPointVar = (ClassIntervalR+(ClassDifference*(Row+3))) - (ClassDifference/2)
        MidPointX.append(MidPointVar)
        FXList.append(float(MidPointX[Row+2])*float(Frequency[Row+2]))

        myTable.add_row([f"{ClassDifference+(ClassDifference*(Row+1))} ≤ X < {ClassIntervalR+(ClassDifference*(Row+3))}",
                         int(Frequency[Row+2]),
                         NewCum,
                         f"{ClassIntervalR+(ClassDifference*(Row+3))}",
                         MidPointVar,
                         float(Frequency[Row+2])*float(MidPointVar)
                         ])
    else:
        NewCum = NewCum + int(Frequency[Row+2])
        MidPointVar = (ClassIntervalR+(ClassDifference*(Row+3))) - (ClassDifference/2)
        MidPointX.append(MidPointVar)
        FXList.append(float(MidPointX[Row+2])*float(Frequency[Row+2]))

        myTable.add_row([f"{ClassIntervalR+(ClassDifference*(Row+2))} ≤ X < {ClassIntervalR+(ClassDifference*(Row+3))}",
                         int(Frequency[Row+2]),
                         NewCum,
                         f"{ClassIntervalR+(ClassDifference*(Row+3))}",
                         MidPointVar,
                         float(Frequency[Row+2])*float(MidPointVar)
                         ])

u = sum(FXList)/sum(Frequency)


# Add (𝑥-μ)²
xu2List = []
for i in range(HowManyRows):
    xu2List.append(round((MidPointX[i]-u)**2, 2))

myTable.add_column("(𝑥-μ)²", xu2List)

# Add ƒ(𝑥-μ)²
Fxu2 = []
for i in range(HowManyRows):
    Fxu2.append(round((xu2List[i]*Frequency[i]), 2))

myTable.add_column("ƒ(𝑥-μ)²", Fxu2)

# Add Empty Row
myTable.add_row(["", "", "", "", "", "", "", ""])

# Add Total Row
myTable.add_row(["Total", int(sum(Frequency)), " ", " ",
                sum(MidPointX), sum(FXList), " ", round(sum(Fxu2),2)])

SD = math.sqrt(sum(Fxu2)/sum(Frequency))

# Print

print("")
print(f"Rows: {HowManyRows}")
print(f"Class Difference: {ClassDifference}")
print(f"First Value: {ClassIntervalR}")
print("")

print(myTable)

print("")
print(f"The Mean (μ) Is: {round(u,2)}")
print("")
print(f"The Median Value To Use With A Graph Is: {(sum(Frequency)+1)/2}")
print("")
print(f"The Standard Deviation (σ) Is: {round(SD,2)}")
