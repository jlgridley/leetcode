def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
	 output = [0 for i in range(len(temperatures))]
	 temps = [0 for i in range(100 - 30 + 1)]
	 for i in reversed(range(len(temperatures))):
		 curr = temperatures[i]
		 soonest = 0
		 for j in range(curr - 30 + 1, len(temps)):
			 if temps[j] != 0:
				 num_days = temps[j] - i
				 if soonest == 0:
					 soonest = num_days
				 elif soonest > num_days:
					 soonest = num_days
		 output[i] = soonest
		 temps[curr - 30] = i
	 return output


"""
30 31
[0, 0]
[0, 1, 0, ....]

curr = 30

"""
