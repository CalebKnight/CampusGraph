class CampusRoute:
    def __init__(self, fromBuilding, toBuilding, distance, security, barriers):
        self.fromBuilding = fromBuilding
        self.toBuilding = toBuilding
        self.distance = distance
        self.security = security
        self.barriers = barriers
    def setFromBuilding(self, fromBuilding):
        self.fromBuilding = fromBuilding
    def setToBuilding(self, toBuilding):
        self.toBuilding = toBuilding
    def setDistance(self, distance):
        self.distance = distance
    def setSecurity(self, security):
        self.security = security
    def setBarriers(self, barriers):
        self.barriers = barriers
        
      