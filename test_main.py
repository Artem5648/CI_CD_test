import pytest
from main import sort_by_area, sort_by_population

# 1. Фікстура: створюємо тестові дані для перевірки
@pytest.fixture
def sample_data():
    return [
        {"country": "Country A", "area": 500, "population": 10},
        {"country": "Country B", "area": 100, "population": 50},
        {"country": "Country C", "area": 300, "population": 5}
    ]

# 2. Параметризація для тестування сортування за площею
# Перевіряємо, чи правильно визначається перша (найменша) країна
@pytest.mark.parametrize("expected_first", ["Country B"])
def test_sort_by_area(sample_data, expected_first):
    sorted_data = sort_by_area(sample_data)
    assert sorted_data[0]["country"] == expected_first

# 3. Параметризація для тестування сортування за населенням
@pytest.mark.parametrize("expected_first", ["Country C"])
def test_sort_by_population(sample_data, expected_first):
    sorted_data = sort_by_population(sample_data)
    assert sorted_data[0]["country"] == expected_first