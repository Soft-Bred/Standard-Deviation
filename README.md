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
This wont Change Anything, But If You Want A Screenshot, You Might Want To.

Change The Fist Value In This List:
```py
myTable = PrettyTable(["Number Of Parked Cars / Hour",
                      "Frequency (ƒ)",
                      "Cumulative Frequency",
                      "Upper Class Boundary",
                      "Mid Point (𝑥)",
                      "ƒ𝑥"])
```
