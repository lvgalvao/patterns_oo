from abc import ABC, abstractmethod


class Template(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        if self.hook1():
            self.base_operation3()
        self.hook2()
        self.required_operation2()

    def base_operation1(self) -> None:
        print("Template says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("Template says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("Template says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operation1(self) -> None:
        pass

    def required_operation2(self) -> None:
        pass

    def hook1(self) -> bool:
        return True

    def hook2(self) -> None:
        pass


class ConcreteClass1(Template):
    def required_operation1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operation2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")

    def hook2(self) -> None:
        print("ConcreteClass1 says: Overridden Hook2")


class ConcreteClass2(Template):
    def required_operation1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operation2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> bool:
        print("ConcreteClass2 says: Overridden Hook1")
        return False


def main() -> None:
    concrete_class1 = ConcreteClass1()
    concrete_class1.template_method()

    concrete_class2 = ConcreteClass2()
    concrete_class2.template_method()


if __name__ == "__main__":
    main()
