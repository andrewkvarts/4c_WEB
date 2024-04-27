from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def do_a(self) -> str:
        pass

class ProductA1(AbstractProductA):
    def do_a(self) -> str:
        return "A1 робить щось A"

class ProductA2(AbstractProductA):
    def do_a(self) -> str:
        return "A2 робить щось A"


class AbstractProductB(ABC):
    @abstractmethod
    def do_b(self) -> str:
        pass

class ProductB1(AbstractProductB):
    def do_b(self) -> str:
        return "B1 робить щось B"

class ProductB2(AbstractProductB):
    def do_b(self) -> str:
        return "B2 робить щось B"


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class Factory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()


class Factory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ProductB2()


def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.do_a())
    print(product_b.do_b())


if __name__ == "__main__":
    print("Використання першої конкретної фабрики:")
    client_code(Factory1())

    print("\nВикористання другої конкретної фабрики:")
    client_code(Factory2())
