#!/usr/bin/env python3
import queue
import sys


class Fringe(object):
    """wrapper for queue lib from python to keep track of some statistics"""

    # ### DO NOT CHANGE __MAX_FRINGE_SIZE ###
    __MAX_FRINGE_SIZE = 50000
    __fringe = None
    __insertions = 0
    __deletions = 0
    __maxSize = 0

    def create_fringe(self, fringe_type):
        """
        Creates a fringe of type fringe_type
        :param fringe_type: The desired type for the queue
        :return: A queue of type fringe_type
        """
        if fringe_type == "STACK":
            return queue.LifoQueue(self.__MAX_FRINGE_SIZE)

        if fringe_type == "FIFO":
            return queue.Queue(self.__MAX_FRINGE_SIZE)

        if fringe_type == "PRIORITY":
            return queue.PriorityQueue(self.__MAX_FRINGE_SIZE)

    def __init__(self, fringe_type='FIFO'):
        self.__type = fringe_type
        super(Fringe, self).__init__()
        self.__fringe = self.create_fringe(self.__type)

    def push(self, item):
        """
        puts the item in the fringe
        :param item: item to put in the fringe
        """
        # If the fringe is full, print an error and exit
        if self.__fringe.full():
            print("Error: trying to apply push on an fringe that already contains MAX ("
                  + str(self.__MAX_FRINGE_SIZE) + ") elements")
            self.print_stats()
            sys.exit(1)
        self.__fringe.put(item, block=False)
        if self.__fringe.qsize() > self.__maxSize:
            self.__maxSize = self.__fringe.qsize()
        self.__insertions += 1

    def pop(self):
        """
        :return: item from fringe, None if the fringe is empty
        """
        if self.__fringe.empty():
            return None
        self.__deletions += 1
        return self.__fringe.get()

    def is_empty(self):
        """
        :return: True if fringe is empty, false otherwise
        """
        return self.__fringe.empty()

    # returns the number of insertions
    def get_insertions(self):
        """
        :return: The number of insertions in the fringe
        """
        return self.__insertions

    def get_deletions(self):
        """
        :return: number of items deleted from fringe
        """
        return self.__deletions

    def print_stats(self):
        """ Prints the statistics of the fringe """
        print("#### fringe statistics:")
        print("size: {0:>15d}".format(self.__fringe.qsize()))
        print("maximum size: {0:>7d}".format(self.__maxSize))
        print("insertions: {0:>9d}".format(self.get_insertions()))
        print("deletions: {0:>10d}".format(self.get_deletions()))


class GreedyFringe(Fringe):
    def __init__(self, heuristic_func, fringe_type='PRIORITY'):
        super().__init__(fringe_type)
        self.heuristic_func = heuristic_func

    def push_fringe(self, item):
        super().push(item)

    def push(self, item):
        heuristic = self.heuristic_func(item)
        super().push((heuristic, item))

    def pop(self):
        # Pop the item with the smallest heuristic value
        item = super().pop()
        if isinstance(item, tuple):
            return item[1]  # Return the item if it's not a tuple
        else:
            return item


class UCSFringe(GreedyFringe):
    def __init__(self, path_cost, fringe_type='PRIORITY'):
        super().__init__(fringe_type)
        self.path_cost = path_cost

    def push(self, item):
        cost = self.path_cost(item)
        super().push_fringe((cost, item))


class AStarFringe(GreedyFringe):
    def __init__(self, cost_func, fringe_type='PRIORITY'):
        super().__init__(fringe_type)
        self.cost_func = cost_func

    def push(self, item):
        current_cost = self.cost_func(item)
        self.push_fringe((current_cost, item))
