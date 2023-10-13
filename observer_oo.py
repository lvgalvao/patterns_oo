from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Observer(ABC):
    @abstractmethod
    def update(self, value: str) -> None:
        pass


@dataclass
class ConcreteObserver(Observer):
    name: str

    def update(self, value: str) -> None:
        print(f"{self.name} received {value}")


@dataclass
class Subject:
    observers: list[Observer] = field(default_factory=list)

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify(self, value: str) -> None:
        for observer in self.observers:
            observer.update(value)


def main() -> None:
    subject = Subject()

    observer1 = ConcreteObserver("Observer 1")
    subject.attach(observer1)

    observer2 = ConcreteObserver("Observer 2")
    subject.attach(observer2)

    subject.notify("Some Data!")


if __name__ == "__main__":
    main()
