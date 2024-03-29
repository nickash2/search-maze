# Lab Assignment 1: Agents & Search
The following is an implementation of various search algorithms, for searching in a 3D maze, implemented with the use of OOP principles.
## Prerequisites:
* Python >= 3.8
* Pylama ([Linting](https://code.visualstudio.com/docs/python/linting#:~:text=Linting%20highlights%20syntactical%20and%20stylistic,that%20can%20lead%20to%20errors.) Purposes)
* [autopep8](https://pypi.org/project/autopep8/)

## TODO List:
- [x] ~~Fix DFS~~
- [x] ~~Fix BFS~~
- [x] ~~Implement UCS~~
- [x] ~~Implement Greedy Search~~
- [x] ~~Implement A*~~
- [x] ~~Implement IDS~~


## Iterative Deepening Search(IDS)
* IDS uses an additional function DLS (Depth Limited Search), this function limits the search in terms of depth. 
* The IDS algorithm then constantly increments until the goal is reached.

## Other Algorithms Implemented
* For UCS, A* & Greedy Search, a tuple is being added to the fringe, and since the priority queue is ordered based on the **first element** in the tuple in this case, it works as expected.



#### Notes
* **Before committing anything, ensure that it is autopep8'd by using the command:** 
```
autopep8 --in-place <filename>
```


* The implementation of the rooms and states already include built-in functions for the heuristic values of each room, and the cost to reach a certain state.

