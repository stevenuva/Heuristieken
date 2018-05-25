import math

"""
Class spacecraft

Used to initialize a spacecraft and to add, remove cargo
Functions include cost calculation and volume and mass checks
"""


class Spacecraft:

    def __init__(self, payload_mass, volume, spacecraft_mass, base_cost, ftw):
        """
        Function to initialize a spacecraft
        """
        self.base_cost = base_cost
        self.cargo_list = []
        self.filled_mass = 0
        self.filled_volume = 0
        self.ftw = round((ftw / (1 - ftw)), 3)
        self.ratio = round((payload_mass / volume), 3)
        self.remaining_mass = round(payload_mass, 3)
        self.remaining_volume = round(volume, 3)
        self.removed_list = []
        self.payload_mass = payload_mass
        self.spacecraft_mass = spacecraft_mass
        self.volume = volume

    def add_cargo(self, cargo_id, cargo_weight, cargo_volume):
        """
        Function to add cargo to a spaceship
        """
        self.remaining_mass -= round(cargo_weight, 3)
        self.remaining_volume -= round(cargo_volume, 3)
        self.filled_mass = round((self.payload_mass - (self.remaining_mass)), 3)
        self.filled_volume = round((self.volume - (self.remaining_volume)), 3)
        self.cargo = {"id": cargo_id, "mass": cargo_weight,
                      "volume": cargo_volume, "kg/m3": (cargo_weight / cargo_volume)}
        self.cargo_list.append(self.cargo)
        return self.remaining_mass, self.remaining_volume, self.cargo_list,
        self.filled_mass, self.filled_volume

    def cost(self):
        """
        Function to calculate the cost of a spaceship
        """
        self.filled_mass = self.payload_mass - (self.remaining_mass)
        self.filled_volume = self.volume - (self.remaining_volume)
        self.fuel = (self.filled_mass + self.spacecraft_mass) * self.ftw
        self.total_cost = (math.ceil(self.fuel * 1000) * 5) + self.base_cost
        return self.total_cost

    def filled(self):
        """
        Function to check how space craft is filled
        Checks the cargolist and the used mass and volume
        """
        self.filled_mass = self.payload_mass - (self.remaining_mass)
        self.filled_volume = self.volume - (self.remaining_volume)
        return self.filled_mass, self.filled_volume, self.cargo_list

    def remaining(self):
        """
        Function to check the remaining mass and volume
        """
        return self.remaining_mass, self.remaining_volume

    def remove_cargo(self, cargo_id):
        """
        Function to remove cargo from the spacecraft
        """
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
