# Lab Assignment 1: Agents & Search

## Prerequisites:
* Python >= 3.8
* Pylama ([Linting](https://code.visualstudio.com/docs/python/linting#:~:text=Linting%20highlights%20syntactical%20and%20stylistic,that%20can%20lead%20to%20errors.) Purposes)

## TODO List:
- [x] Implement Greedy Search
- [x] Implement A*
- [ ] Implement UCS
- [ ] Implement Error Catching in A* & Greedy Search (insertions, deletions, fringe being full)


### Notes
* For UCS, we need to order the priorty queue on the cost, as currently we are ordering it on the room number. 
    * That can be done by creating a class, and pushing the cost to the fringe rather than the number

