from typing import Callable, List


# Definindo as funções de observer com argumento nomeado
def update_observer1(value: str) -> None:
    print(f"Observer 1 received {value}")


def update_observer2(value: str) -> None:
    print(f"Observer 2 received {value}")


# Definindo o tipo para as funções de atualização
UpdateFn = Callable[[str], None]


def notify(update_fns: List[UpdateFn], value: str) -> None:
    for update_fn in update_fns:
        update_fn(value)


def main() -> None:
    update_fns = [update_observer1, update_observer2]
    notify(update_fns, "Some Data!")


if __name__ == "__main__":
    main()
