## Desenvolvimento de Design Patterns: Uma Exploração de Perspectivas OO e FN

### Descrição do Repositório

Bem-vindo ao repositório onde exploramos a implementação de diferentes **Design Patterns** através de duas lentes distintas: a programação orientada a objetos (OO) e a programação funcional (FN). O objetivo é fornecer um terreno experimental para desenvolvedores, estudantes e entusiastas interessados em descobrir, aprender e comparar as abordagens OO e FN na aplicação de diversos padrões de design em software.

### Objetivos

1. **Exploração de Design Patterns**: Investigar e implementar vários padrões de design usando duas abordagens de programação distintas.
    
2. **Comparação de Paradigmas**: Analisar as diferenças, vantagens e desvantagens entre as abordagens OO e FN para cada padrão de design.
    
3. **Aprendizado e Colaboração**: Servir como uma plataforma para aprendizado contínuo e colaboração entre desenvolvedores de todas as habilidades e níveis de experiência.
    

### Design Patterns Abordados

* **Template**: É um padrão de design comportamental que define o esqueleto de um algoritmo na superclasse mas permite que as subclasses substituam etapas específicas do algoritmo sem alterar sua estrutura.
    
* **Strategy**: Explorando o padrão Strategy através de abordagens OO tradicionais e funções de primeira classe FN.
    
* **Observer**: Implementação do padrão Observer, explorando a natureza baseada em estado do OO contra a natureza stateless do FN.

### Design Aplicado a uma ETL

* **ETL**: Explorando o padrão Template através de abordagem funcional.

```python
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
```
