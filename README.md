# How To Use

## Step 1
Enter Amount Of Rows In Table (Excluding Total)<br/>
`Example: Amount Of Rows Would Be 5`
```py
+------------------------------+
| Number Of Parked Cars / Hour |
+------------------------------+
|          0 ≤ X < 10          |
|         10 ≤ X < 20          |
|         20 ≤ X < 30          |
|         30 ≤ X < 40          |
|         40 ≤ X < 50          |
|                              |
|            Total             |
+------------------------------+
```

## Step 2
Enter The Difference Between The First Value & The Second

`Example: Differance Would Be 10`

```0 ≤ X < 10```


## Step 3
Enter The First Value Of The First Interval

`Example: Frist Value Would Be 0`

```0 ≤ X < 10```

## Setp 4
Enter All Frequencies, In Order.

`Example:`

Your Input would be: `9`,`*Enter*`,`14`,`*Enter*`,`27`,`*Enter*`,`18`,`*Enter*`,`17`,`*Enter*`
```py
+------------------------------+---------------+
| Number Of Parked Cars / Hour | Frequency (ƒ) |
+------------------------------+---------------+
|          0 ≤ X < 10          |       9       |
|         10 ≤ X < 20          |       14      |
|         20 ≤ X < 30          |       27      |
|         30 ≤ X < 40          |       18      |
|         40 ≤ X < 50          |       17      |
|                              |               |
|            Total             |       85      |
+------------------------------+---------------+
```

## Optional
Changing The First Value Of The Table Titles (In This Example `Number Of Parked Cars / Hour`)  
This Won't Change Anything, But If You Want A Screenshot, You Might Want To.

Change The Fist Value In This List:
```py
myTable = PrettyTable(["Number Of Parked Cars / Hour",
                      "Frequency (ƒ)",
                      "Cumulative Frequency",
                      "Upper Class Boundary",
                      "Mid Point (𝑥)",
                      "ƒ𝑥"])
```

# Output
Output Should Look Something Like This Depending On How Many Rows You Enter:
```
Rows: 5
Class Difference: 10
First Value: 0

+------------------------------+---------------+----------------------+----------------------+---------------+--------+--------+----------+
| Number Of Parked Cars / Hour | Frequency (ƒ) | Cumulative Frequency | Upper Class Boundary | Mid Point (𝑥) |   ƒ𝑥   | (𝑥-μ)² | ƒ(𝑥-μ)²  |
+------------------------------+---------------+----------------------+----------------------+---------------+--------+--------+----------+
|          0 ≤ X < 10          |       9       |          9           |          10          |      5.0      |  45.0  | 499.65 | 4496.85  |
|         10 ≤ X < 20          |       14      |          23          |          20          |      15.0     | 210.0  | 152.6  |  2136.4  |
|         20 ≤ X < 30          |       27      |          50          |          30          |      25.0     | 675.0  |  5.54  |  149.58  |
|         30 ≤ X < 40          |       18      |          68          |          40          |      35.0     | 630.0  | 58.48  | 1052.64  |
|         40 ≤ X < 50          |       17      |          85          |          50          |      45.0     | 765.0  | 311.42 | 5294.14  |
|                              |               |                      |                      |               |        |        |          |
|            Total             |       85      |                      |                      |     125.0     | 2325.0 |        | 13129.61 |
+------------------------------+---------------+----------------------+----------------------+---------------+--------+--------+----------+

The Mean (μ) Is: 27.35

The Median Value To Use With A Graph Is: 43.0

The Standard Deviation (σ) Is: 154.47
```
