import array
import random

# Генеруємо випадковий масив з 6 цілих чисел в діапазоні [1; 55]
random_numbers = array.array('i', [random.randint(1, 55) for _ in range(6)])

# Відсортовуємо масив за зростанням
random_numbers = array.array('i', sorted(random_numbers))

# Створюємо два нових масиви з перших 3 і останніх 3 елементів відсортованого масиву
first_three = random_numbers[:3]
last_three = random_numbers[-3:]

# Знаходимо індекс найменшого елемента в відсортованому масиві
min_index = random_numbers.index(min(random_numbers))

# Видаляємо найменший елемент з масиву
random_numbers.pop(min_index)

# Виводимо результати
print("Відсортований масив:", random_numbers)
print("Перші три елементи:", first_three)
print("Останні три елементи:", last_three)
print("Масив без найменшого елемента:", random_numbers)


