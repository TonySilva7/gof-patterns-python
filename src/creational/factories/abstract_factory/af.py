"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.
Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.
Princípio: programe para interfaces, não para implementações
"""
from abc import ABC, abstractmethod
from typing import Literal

TypeVehicle = Literal["lux", "popular", "moto"]


class LuxVehicle(ABC):
    @abstractmethod
    def get_passanger(self) -> None:
        pass


class PopularVehicle(ABC):
    @abstractmethod
    def get_passanger(self) -> None:
        pass


class LuxCar(LuxVehicle):
    def get_passanger(self) -> None:
        print("LuxCar pegou 4 passangers")


class Motocicle(PopularVehicle):
    def get_passanger(self) -> None:
        print("Lux Moto pegou 4 passangers")


class PoupularCar(PopularVehicle):
    def get_passanger(self) -> None:
        print("PoupularCar pegou 4 passangers")


class FactoryVehicle(ABC):
    @staticmethod
    @abstractmethod
    def get_lux_vehicle() -> LuxVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_popular_vehicle() -> PopularVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_popular_moto() -> PopularVehicle:
        pass


class SouthZone(FactoryVehicle):
    # ------- Factory method -------
    @staticmethod
    def get_lux_vehicle() -> LuxVehicle:
        return LuxCar()

    @staticmethod
    def get_popular_vehicle() -> PopularVehicle:
        return PoupularCar()

    @staticmethod
    def get_popular_moto() -> PopularVehicle:
        return Motocicle()


class EastZone(FactoryVehicle):
    @staticmethod
    def get_lux_vehicle() -> LuxVehicle:
        return LuxCar()

    @staticmethod
    def get_popular_vehicle() -> PopularVehicle:
        return PoupularCar()

    @staticmethod
    def get_popular_moto() -> PopularVehicle:
        return Motocicle()


class Franchise:
    def get_passangers(self):
        for factory in [SouthZone(), EastZone()]:
            popular_car = factory.get_popular_vehicle()
            popular_car.get_passanger()

            lux_car = factory.get_lux_vehicle()
            lux_car.get_passanger()


if __name__ == "__main__":
    franchise = Franchise()
    franchise.get_passangers()
