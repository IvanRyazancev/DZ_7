# Задача №2. Напишите функцию print_operation_table(operation, num_rows=6,
#  num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую
# элемент по номеру строки и столбца. Аргументы num_rows и num_columns 
# указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание:
# бинарной операцией называется любая операция, у которой ровно два аргумента, как, 
# например, у операции умножения.
# 
# *Пример:*
# 
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**


def print_operation_table(operation,num_rows,num_colums):
    for i in range(1,num_rows):
        k = ""
        for j in range(1,num_colums):
            k = k + operation(i,j) + " "
        print(k)
print_operation_table((lambda x,y: str(x*y)),7,7)