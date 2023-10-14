import pandas as pd
import random
from typing import Callable, List


def load_data(data: pd.DataFrame) -> pd.DataFrame:
    print("Loading data...")
    return data


def save_data(data: pd.DataFrame) -> None:
    print("Saving data...")


def multiply_data(factor: int, data: pd.DataFrame) -> pd.DataFrame:
    print(f"Multiplying data by {factor}...")
    return data * factor


def add_random_number(data: pd.DataFrame) -> pd.DataFrame:
    random_number = random.randint(1, 10)
    print(f"Adding random number {random_number} to data...")
    return data + random_number


def data_transform_pipeline(
    transform_fns: List[Callable[[pd.DataFrame], pd.DataFrame]], data: pd.DataFrame
) -> pd.DataFrame:
    data = load_data(data)
    for transform_fn in transform_fns:
        data = transform_fn(data)
    save_data(data)
    return data


# Exemplo de uso
if __name__ == "__main__":
    # Criando um DataFrame de exemplo
    data = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})

    # Usando funções de transformação de dados
    transformed_data_1 = data_transform_pipeline(
        [lambda data: multiply_data(2, data)], data
    )
    print(transformed_data_1)

    transformed_data_2 = data_transform_pipeline([add_random_number], data)
    print(transformed_data_2)

    transformed_data_3 = data_transform_pipeline(
        [lambda data: multiply_data(2, data), add_random_number], data
    )
    print(transformed_data_3)
