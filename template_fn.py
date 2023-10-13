from typing import Callable
from functools import partial


def base_operations1() -> None:
    print("Template says: I am doing the bulk of the work")


def base_operations2() -> None:
    print("Template says: But I let subclasses override some operations")


def base_operations3() -> None:
    print("Template says: But I am doing the bulk of the work anyway")


def template_method(
    required_operation1: Callable[[], None],
    required_operation2: Callable[[], None],
    hook1: Callable[[], bool] = lambda: True,
    hook2: Callable[[], None] = lambda: None,
) -> None:
    base_operations1()
    required_operation1()
    base_operations2()
    if hook1():
        base_operations3()
    hook2()
    required_operation2()


def operation1_imp() -> None:
    print("ConcreteClass1 says: Implemented Operation1")


def operation2_imp() -> None:
    print("ConcreteClass1 says: Implemented Operation2")


def override_hook1() -> bool:
    print("ConcreteClass1 says: Overridden Hook1")
    return False


def main() -> None:
    application = partial(template_method, operation1_imp, operation2_imp)

    application()

    application(override_hook1)


if __name__ == "__main__":
    main()
