# 1. Система обробки замовлень в ресторані:
# Черга для зберігання замовлень в ресторані,
# де замовлення обробляються за порядком їх надходження.
# from queue import Queue
#
# class RestaurantOrder:
#     def __init__(self):
#         self.orders = Queue()
#
#     def put_order(self, order):
#         self.orders.put(order)
#         print(f'Замовлення {order} прийнято.')
#
#     def process(self):
#         while not self.orders.empty():
#             order = self.orders.get()
#             print(f'Замовлення {order} готується.')
#
#     def complete(self, order):
#         print(f'Замовлення {order} готове')
#
# restaurant = RestaurantOrder()
# restaurant.put_order('Бургер')
# restaurant.put_order('Картопля Фрі')
# restaurant.put_order('Сік')
#
# print('Початок обробки замовлення ...')
# restaurant.process()
# print()
# restaurant.complete('Бургер')


# Завдання 1
# Створіть клас черги для роботи із символьними значеннями.
# Ви маєте створити реалізації для операцій над елементами:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ Enqueue — додати новий елемент до черги;
# ■ Dequeue — видалення елемента з черги;
# ■ Show — відображення на екрані всіх елементів черги.
# На старті додатка відобразіть меню, в якому користувач
# може вибрати необхідну операцію.
# class CharQueue:
#     def __init__(self, size):
#         self.size = size
#         self.queue = []
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
#     def is_full(self):
#         return len(self.queue) == self.size
#
#     def enqueue(self, item):
#         if not self.is_full():
#             self.queue.append(item)
#             print(f'Елемент {item} додано до черги.')
#         else:
#             print('Черга повна.')
#
#     def dequeue(self):
#         if not self.is_empty():
#             item = self.queue.pop(0)
#             print(f'Елемент {item} видалено з черги')
#         else:
#             print('Черга порожня.')
#
#     def show(self):
#         if not self.is_empty():
#             print('Елементи черги:')
#             for item in self.queue:
#                 print(item)
#             else:
#                 print('Черга порожня.')
#
#     def display(self):
#         print('Меню:')
#         print("1. Перевірити, чи черга порожня")
#         print("2. Перевірити, чи черга заповнена")
#         print("3. Додати елемент до черги")
#         print("4. Видалити елемент з черги")
#         print("5. Показати елементи черги")
#         print("0. Вийти з програми")
#
#         while True:
#             choice = input('Введіть ваш вибір:')
#
#             if choice == '1':
#                 if self.is_empty():
#                     print('Черга порожня.')
#                 else:
#                     print('Черга не порожня')
#             elif choice == '2':
#                 if self.is_full():
#                     print('Черга повна.')
#                 else:
#                     print('Черга не повна.')
#             elif choice == '3':
#                 item = input('Введіть елементи, аби додати до черги:')
#                 self.enqueue(item)
#             elif choice == '4':
#                 self.dequeue()
#             elif choice == '5':
#                 self.show()
#             elif choice == '0':
#                 break
#             else:
#                 print('Некоректний вибір')
#
# size = int(input('Введіть розмір черги:'))
# queue = CharQueue(size)
# queue.display()


# Завдання 2
# Створіть клас черги з пріоритетами для роботи із
# символьними значеннями.
# Ви маєте створити реалізації для операцій над елементами черги:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ InsertWithPriority — додати елемент з пріоритетом у
# чергу■ PullHighestPriorityElement — видалення елемента з
# найвищим пріоритетом із черги;
# ■ Peek — повернення найбільшого за пріоритетом елемента. Зверніть увагу, що елемент не видаляється з
# черги;
# ■ Show — відображення на екрані всіх елементів черги.
# Показуючи елемент, також необхідно вказати і його
# пріоритет.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return False

    def insert_with_priority(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0], reverse=True)

    def pull_highest_priority_element(self):
        if not self.is_empty():
            priority, item = self.queue.pop(0)
            print(f"Видалено елемент '{item}' з найвищим пріоритетом {priority}.")
        else:
            print("Черга порожня. Неможливо видалити елемент.")

    def peek(self):
        if not self.is_empty():
            priority, item = self.queue[0]
            print(f"Найвищий пріоритет має елемент '{item}' з пріоритетом {priority}.")
        else:
            print("Черга порожня. Неможливо показати елемент.")

    def show(self):
        if not self.is_empty():
            print("Елементи черги з пріоритетами:")
            for priority, item in self.queue:
                print(f"Елемент: {item}, Пріоритет: {priority}")
        else:
            print("Черга порожня.")

    def display(self):
        print('Меню:')
        print("1. Перевірити, чи черга порожня")
        print("2. Додати елемент з пріоритетом у чергу")
        print("3. Видалити елемент з найвищим пріоритетом")
        print("4. Показати найвищий за пріоритетом елемент")
        print("5. Показати всі елементи черги з пріоритетами")
        print("0. Вийти з програми")

        while True:
            choice = input('Введіть ваш вибір:')

            if choice == '1':
                if self.is_empty():
                    print("Черга порожня.")
                else:
                    print("Черга не порожня.")
            elif choice == '2':
                item = input("Введіть елемент для додавання: ")
                priority = int(input("Введіть пріоритет для елемента: "))
                self.insert_with_priority(item, priority)
            elif choice == '3':
                self.pull_highest_priority_element()
            elif choice == '4':
                self.peek()
            elif choice == '5':
                self.show()
            elif choice == '0':
                print("Програма завершена.")
                break
            else:
                print("Некоректний вибір.")


queue = PriorityQueue()
queue.display()



