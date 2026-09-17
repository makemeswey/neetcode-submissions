class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = start = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:               # can't reach i+1 from start
                start = i + 1          # restart from next station
                tank = 0

        return start

        
        