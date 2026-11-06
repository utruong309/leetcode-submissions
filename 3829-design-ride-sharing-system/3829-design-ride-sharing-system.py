class RideSharingSystem:

    def __init__(self):
        self.riders = deque() 
        self.drivers = deque() 
        self.riders_set = set() 
        
    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.riders_set.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        
        while self.riders and self.riders[0] not in self.riders_set: 
            self.riders.popleft() 
        
        if self.riders and self.drivers: 
            rider = self.riders.popleft() 
            driver = self.drivers.popleft() 

            self.riders_set.remove(rider)

            return [driver, rider]
        
        else: 
            return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        self.riders_set.discard(riderId)
        

# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)