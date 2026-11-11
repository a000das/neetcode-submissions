from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars by position, closest to target first
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time = 0  # arrival time of the fleet directly ahead

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > slowest_time:   # can't catch the fleet ahead -> new fleet
                fleets += 1
                slowest_time = time

        return fleets

