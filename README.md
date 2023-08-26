# AI Search Project
![README image](https://github.com/faridmmz/AI-Search-Python-Proj/blob/main/README_Image.jpg)

Welcome to the first chapter of me uploading my university projects to my Git Hub! Hope you enjoy and apologies in advance for not having enough comments.
This project is part of my university AI course and involves implementing different search algorithms for solving puzzles on a given board. 
It might not be my best project but as a showcase of what I have done in many years of university here it is. Thank you very much to whoever is reading this I hope you don't get lost reading this and implementing your versions. Happy coding!

## Table of Contents

- [Description](#description)
- [Files](#files)
- [Usage](#usage)
- [Test Cases](#test-cases)
- [Algorithms](#algorithms)
- [Contributing](#contributing)

## Description

The project focuses on solving puzzles using various search algorithms. The puzzle consists of a board with cells having different operations and values. The goal is to find a path from the start cell ('s') to the goal cell ('g') that satisfies certain conditions and yields the desired result.

## Files

- `Board.py`: Defines the `Board` class used to represent the puzzle board.
- `Cell.py`: Defines the `Cell` class used to represent individual cells on the board.
- `Find.py`: Implements different search algorithms to solve the puzzle.
- `main.py`: Handles user input, initializes the board, and triggers the search algorithms.

## Usage

1. Install Python on your system if not already installed.
2. Clone this repository using `git clone <repository_url>` or download the ZIP.
3. Navigate to the project directory.
4. Run the program using the command: `python main.py`.
5. Follow the on-screen instructions to input the board dimensions and cell values.

* Or just use Google Colab!

## Test Cases

The project includes several test cases to demonstrate the functionality of the implemented search algorithms. Here are a few examples:

### Test Case 1

Input:
```
2 3
s1 -7 -8
*3 +6 g5
```
Output:
```
3
1 1
2 1
2 2
```

### Test Case 2

Input:
```
4 4
s1 *1 *10 *2
*1 -10 -100 +10
+5 *10 g100 +5
*1 +5 +90 +10
```
Output:
```
6
1 1
2 1
3 1
3 2
4 2
4 3
```

### Test Case 3

Input:
```
6 6
s1 +9 *1 *1 *1 *1
*5 +5 *1 *1 *1 *1
*2 +15 w0 w0 w0 +10
-50 -50 w0 g100 w0 +10
*1 *1 a10 -10 +10 +10
+10 +10 b10 w0 -10 -100
```
Output:
```
14
1 1
1 2
2 2
2 1
3 1
3 2
4 2
5 2
5 1
6 1
6 2
6 3
5 3
5 4
```

## Algorithms

The project implements the following search algorithms:
- Breadth-First Search (BFS)
- Iterative Deepening Search (IDS)
- Bidirectional Search (BDS)
- A* Search
- Iterative Deepening A* Search (IDA*)

Each algorithm is implemented in the `Find.py` file.

## Contributing

Any contribution to this project is welcome! If you find any issues or have improvements to suggest, please feel free to open an issue or create a pull request. Also, my email is visible in my profile so if you have any questions on these subjects don't hesitate to ask!
