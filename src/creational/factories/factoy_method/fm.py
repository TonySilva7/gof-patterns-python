"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""

from abc import ABC, abstractmethod

# from enum import Enum
from typing import Literal

# class TypeVehicle(Enum):
#     LUX = "lux"
#     POPULAR = "popular"
#     MOTO = "moto"


TypeVehicle = Literal["lux", "popular", "moto"]


class Vehicle(ABC):
    @abstractmethod
    def get_passanger(self) -> None:
        pass


class LuxCar(Vehicle):
    def get_passanger(self) -> None:
        print("LuxCar pegou 4 passangers")


class Motocicle(Vehicle):
    def get_passanger(self) -> None:
        print("Lux Moto pegou 4 passangers")


class PoupularCar(Vehicle):
    def get_passanger(self) -> None:
        print("PoupularCar pegou 4 passangers")


class FactoryVehicle(ABC):
    def __init__(self, type_vehicle: TypeVehicle) -> None:
        self.vehicle: Vehicle = self.get_vehicle(type_vehicle)

    @staticmethod
    @abstractmethod
    def get_vehicle(
        type_vehicle: TypeVehicle,
    ) -> Vehicle:
        pass

    def get_passanger(self) -> None:
        self.vehicle.get_passanger()


class SouthZone(FactoryVehicle):
    # ------- Factory method -------
    @staticmethod
    def get_vehicle(
        type_vehicle: TypeVehicle,
    ) -> Vehicle:
        if type_vehicle == "lux":
            return LuxCar()

        if type_vehicle == "pulular":
            return PoupularCar()

        if type_vehicle == "moto":
            return Motocicle()

        raise AssertionError("Vehicle not found")


class EastZone(FactoryVehicle):
    @staticmethod
    def get_vehicle(
        type_vehicle: TypeVehicle,
    ) -> Vehicle:
        if type_vehicle == "lux":
            return LuxCar()

        if type_vehicle == "popular":
            return PoupularCar()

        raise AssertionError("Vehicle not found")


if __name__ == "__main__":
    car1 = SouthZone("lux")
    car1.vehicle.get_passanger()
    moto = SouthZone("moto")
    moto.vehicle.get_passanger()

    car2 = EastZone("popular")
    car2.vehicle.get_passanger()
