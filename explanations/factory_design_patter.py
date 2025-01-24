from abc import ABC, abstractmethod


# Step 1: Define the Product interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass


# Step 2: Implement Concrete Products
class Espresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong Espresso."


class Latte(Coffee):
    def prepare(self):
        return "Preparing a smooth and creamy Latte."


class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a frothy Cappuccino."


# Step 3: Implement the Factory (CoffeeMachine)
class CoffeeMachine:
    def make_coffee(self, coffee_type):
        if coffee_type == "Espresso":
            return Espresso().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        elif coffee_type == "Cappuccino":
            return Cappuccino().prepare()
        else:
            return "Unknown coffee type!"


# Step 4: Use the Factory to Create Products
if __name__ == "__main__":
    machine = CoffeeMachine()

    coffee = machine.make_coffee("Espresso")
    print(coffee)  # Output: Preparing a rich and strong Espresso.

    coffee = machine.make_coffee("Latte")
    print(coffee)  # Output: Preparing a smooth and creamy Latte.

    coffee = machine.make_coffee("Cappuccino")
    print(coffee)  # Output: Preparing a frothy Cappuccino.

#This code demonstrates the **Factory Design Pattern** using a coffee-making example. The `Coffee` interface defines a common blueprint for different coffee types, and specific types like `Espresso`, `Latte`, and `Cappuccino` implement it with their own `prepare` method. The `CoffeeMachine` acts as the factory, creating the desired coffee type based on a given string input (`coffee_type`). When the `make_coffee` method is called, it returns the preparation message for the specified coffee. This approach simplifies the creation process by encapsulating the logic of object creation in the factory, making it easy to add new coffee types in the future.
