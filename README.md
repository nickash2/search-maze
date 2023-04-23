# Lab Assignment 1: Agents & Search

## Prerequisites:
* Python >= 3.8
* Pylama ([Linting](https://code.visualstudio.com/docs/python/linting#:~:text=Linting%20highlights%20syntactical%20and%20stylistic,that%20can%20lead%20to%20errors.) Purposes)
* [autopep8](https://pypi.org/project/autopep8/)

## TODO List:
- [x] ~~Implement Greedy Search~~
- [x] ~~Implement A*~~
- [x] ~~Implement UCS~~
- [ ] Implement IDS


### Notes
* Before committing anything, ensure that it is autopep8'd by using the command:  
```
autopep8 --in-place <filename>
```

* For UCS, we need to order the priorty queue on the cost, as currently we are ordering it on the room number. 
    * That can be done by creating a class, and pushing the cost to the fringe rather than the number
* For A* and Greedy Search, a tuple is being added to the fringe, and since the priority queue is ordered based on the first element in the tuple in this case, it works as expected.

