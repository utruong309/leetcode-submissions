class UndergroundSystem:

    def __init__(self):
        """
        {id: [stationName, time]} # check in at one place at a time, so need to check out before check in again? 
        {(startStation, endStation): (time, count)} -> calculate using startTime from 1st dict and checkout time 
        """
        self.checkin = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkin[id]
        del self.checkin[id]

        if (startStation, stationName) not in self.routes: 
            self.routes[(startStation, stationName)] = [0] * 2 

        self.routes[(startStation, stationName)][0] += t - startTime
        self.routes[(startStation, stationName)][1] += 1 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.routes[(startStation, endStation)][0]
        cnt = self.routes[(startStation, endStation)][1]
        return time / cnt 
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)