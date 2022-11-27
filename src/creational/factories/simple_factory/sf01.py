"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.
Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.
    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).
    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.
Desvantagens:
    Podem introduzir muitas classes no código
Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory
Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_passanger(self) -> None:
        pass


class LuxCar(Vehicle):
    def get_passanger(self) -> None:
        print("LuxCar pegou 4 passangers")


class PoupularCar(Vehicle):
    def get_passanger(self) -> None:
        print("PoupularCar pegou 4 passangers")


class FactoryVehicle:
    @staticmethod
    def get_vehicle(type_vehicle: str) -> Vehicle:
        if type_vehicle == "lux":
            return LuxCar()

        if type_vehicle == "popular":
            return PoupularCar()

        raise AssertionError("Vehicle not found")


if __name__ == "__main__":
    car1: Vehicle = FactoryVehicle.get_vehicle("lux")
    car1.get_passanger()

    car2: Vehicle = FactoryVehicle.get_vehicle("popular")
    car2.get_passanger()

    car3: Vehicle = FactoryVehicle.get_vehicle("byke")
    car3.get_passanger()