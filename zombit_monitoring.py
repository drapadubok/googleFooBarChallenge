"""
Zombit monitoring
=================

The first successfully created zombit specimen, Dolly the Zombit, needs constant monitoring, and Professor Boolean has tasked the 

minions with it. Any minion who monitors the zombit records the start and end times of their shifts. However, those minions, they are a 

bit disorganized: there may be times when multiple minions are monitoring the zombit, and times when there are none!

That's fine, Professor Boolean thinks, one can always hire more minions... Besides, Professor Boolean can at least figure out the total 

amount of time that Dolly the Zombit was monitored. He has entrusted you, another one of his trusty minions, to do just that. Are you up 

to the task?

Write a function answer(intervals) that takes a list of pairs [start, end] and returns the total amount of time that Dolly the Zombit 

was monitored by at least one minion. Each [start, end] pair represents the times when a minion started and finished monitoring the 

zombit. All values will be positive integers no greater than 2^30 - 1. You will always have end > start for each interval.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) intervals = [[1, 3], [3, 6]]
Output:
    (int) 5

Inputs:
    (int) intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
Output:
    (int) 16
"""

def answer(intervals):
	merged_intervals = merge_intervals(intervals)
	total = solve(merged_intervals)
	return total

def merge_intervals(intervals):
	# sort on basis of lower number	
	sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
	retstack = []
	processed_interval = sorted_intervals.pop(0)
	
	while sorted_intervals:
		current_interval = sorted_intervals.pop(0)
		# if current_interval overlaps, but extends beyond, adjust the end of the processed_interval
		if current_interval[1] > processed_interval[1] and current_interval[0] <= processed_interval[1]:
			processed_interval[1] = current_interval[1]
		# if current_interval is disconnected from processed_interval
		elif current_interval[0] > processed_interval[1]:
			retstack.append(processed_interval)
			processed_interval = current_interval
				
	retstack.append(processed_interval)
	return retstack	

def solve(merged_intervals):
	total = 0
	while merged_intervals:
		interval = merged_intervals.pop()
		total += interval[1] - interval[0]
	return total
