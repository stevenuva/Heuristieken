import math


# class for using the spacecraft properties
# adds cargo, calculates the cost, and mass and volume used and remaining


class Spacecraft:

    def __init__(self, payload_mass, volume, spacecraft_mass, base_cost, ftw):
        self.base_cost = base_cost
        self.cargo_list = []
        self.filled_mass = 0
        self.filled_volume = 0
        self.ftw = ftw / (1 - ftw)
        self.ratio = payload_mass / volume
        self.remaining_mass = payload_mass
        self.remaining_volume = volume
        self.removed_list = []
        self.payload_mass = payload_mass
        self.spacecraft_mass = spacecraft_mass
        self.volume = volume

    def add_cargo(self, cargo_id, cargo_weight, cargo_volume):
        self.remaining_mass -= cargo_weight
        self.remaining_volume -= cargo_volume
        self.filled_mass = self.payload_mass - (self.remaining_mass)
        self.filled_volume = self.volume - (self.remaining_volume)
        self.cargo = {"id": cargo_id, "mass": cargo_weight,
                      "volume": cargo_volume, "kg/m3": (cargo_weight / cargo_volume)}
        self.cargo_list.append(self.cargo)
        return self.remaining_mass, self.remaining_volume, self.cargo_list,
        self.filled_mass, self.filled_volume

    def cost(self):
        self.filled_mass = self.payload_mass - (self.remaining_mass)
        self.filled_volume = self.volume - (self.remaining_volume)
        self.fuel = (self.filled_mass + self.spacecraft_mass) * self.ftw
        self.total_cost = (math.ceil(self.fuel * 1000) * 5) + self.base_cost
        return self.total_cost

    def filled(self):
        self.filled_mass = self.payload_mass - (self.remaining_mass)
        self.filled_volume = self.volume - (self.remaining_volume)
        return self.filled_mass, self.filled_volume, self.cargo_list

    def remaining(self):
        return self.remaining_mass, self.remaining_volume

    def remove_cargo(self, cargo_id):
        for parcel in self.cargo_list:
            if parcel.get("id") == cargo_id:
                removed_cargo = parcel
                self.remaining_mass += parcel["mass"]
                self.remaining_volume += parcel["volume"]
                self.filled_mass = self.payload_mass - (self.remaining_mass)
                self.filled_volume = self.volume - (self.remaining_volume)
                self.cargo_list.remove(parcel)
                self.removed_list.append(parcel)
                return self.removed_list, self.remaining_mass, self.remaining_volume, self.cargo_list,
                self.filled_mass, self.filled_volume

    # def score(self)

# # define properties of the spacecrafts
# Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)
# Progress = Spacecraft(2400, 7.6, 7020, 175, 0.74)
# Kounotori = Spacecraft(5200, 14, 10500, 420, 0.71)
# Dragon = Spacecraft(6000, 10, 12200, 347, 0.72)
# TianZhou = Spacecraft(6500, 15, 13500, 412, 0.75)
# Verne_ATV = Spacecraft(7500, 48, 20500, 1080, 0.72)

# Cygnus = Spacecraft(2000, 18.9, 7400, 390000000, 0.73)
# print(Cygnus.remaining())
# Cygnus.add_cargo("#4", 100, 10)
# print(Cygnus.filled())
# print(Cygnus.remaining())
# print(Cygnus.cost())
