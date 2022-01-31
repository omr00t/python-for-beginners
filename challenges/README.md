# 0. What's my prayer time based on my city?

Write a program that gets the prayer time of any city in Oman based on its name.

hint:
- [Check out this link](https://www.mara.gov.om/calendar_page4.asp)

Example:

```
> python prayer_time.py
python prayer_time.py <city>
python prayer_time.py Bidiya

> python prayer_time.py Bidiya
Bidiya
        Prayer     Time
        ----------------
        Fajr     : 05:24
        Shorouk  : 06:43
        Dhuhr    : 12:12
        Asr      : 03:14
        Maghrib  : 05:35
        Isha     : 06:50

> python prayer_time.py Muscat
Muscat
        Prayer     Time
        ----------------
        Fajr     : 05:27
        Shorouk  : 06:48
        Dhuhr    : 12:14
        Asr      : 03:15
        Maghrib  : 05:35
        Isha     : 06:50
```

# 1. Word searcher

Write a program that 
- searches for a word in a list of files.
- Tells you the line at which the word is found if there's a match.
- Once done, you can improve the program by adding the functionality to search for several words in several files.

hints:

- `glob.glob` to get a list of files.
- `os.path.isdir` to get a list of files.
- You can loop through each line in a file using:

```python
file_path = "search_me.txt"
opened_file =  open(file_path, "r")
for line in opened_file:
	print(line)
```
		

# 2. Simple Math Solver

Write a program that
- Reads simple math problems from a file provided by command line and calculate the result.
- Store the result in an output file along with the math problem solved.

Example input file `math_problems.txt`:
```
15 - 12
15 * 11
15 + 1 
 2 / 2
 8 / 0
```

Example of output file `solved_math_problems.txt`:
```
15 - 12 = 3
15 * 11 = 165
15 + 1  = 16
2  / 2  = 1.0
8  / 0  = Error - cannot divide by 0
```


Example

```
> python solve_math.py
python solve_math.py <input_file> <output_file>
python solve_math.py math_problems.txt solved_math_problems.txt
```
