def read_data(file_path):
    """Зчитує дані з файлу та повертає список словників."""
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            country, area, population = line.strip().split(',')
            data.append({
                "country": country.strip(),
                "area": int(area.strip()),
                "population": int(population.strip())
            })
    return data

def sort_by_area(data):
    """Сортує дані за площею (від меншого до більшого)."""
    return sorted(data, key=lambda x: x['area'])

def sort_by_population(data):
    """Сортує дані за населенням (від меншого до більшого)."""
    return sorted(data, key=lambda x: x['population'])

if __name__ == "__main__":
    filename = "data.txt"

    try:
        print("--- Зчитування даних ---")
        countries = read_data(filename)
        for c in countries:
            print(c)

        print("\n--- Сортування за площею ---")
        sorted_area = sort_by_area(countries)
        for c in sorted_area:
            print(f"{c['country']}: {c['area']} км²")

        print("\n--- Сортування за населенням ---")
        sorted_pop = sort_by_population(countries)
        for c in sorted_pop:
            print(f"{c['country']}: {c['population']} осіб")

    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено!")
    except Exception as e:
        print(f"Виникла помилка: {e}")