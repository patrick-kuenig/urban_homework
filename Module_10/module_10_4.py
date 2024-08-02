import threading
import queue
import time


class Table(object):
    def __init__(self, number: int):
        self.number = number
        self.is_busy = False


class Cafe(object):

    def __init__(self, tables: list[Table]):
        self.tables = tables
        self.queue = queue.Queue(maxsize=0)

    def customer_arrival(self, max_customers=24):
        threads = list()
        for i in range(max_customers):
            customer = Customer()
            self.queue.put(customer)
            print(f'Посетитель номер {customer} прибыл.')
            table_state = []
            for table in self.tables:
                table_state.append(table.is_busy)
            if False not in table_state:
                print(f'Посетитель номер {customer} ожидает свободный стол.')
            th = threading.Thread(target=self.serve_customer, args=())
            threads.append(th)
            th.start()
            time.sleep(1)

        for thread in threads:
            thread.join()

    def serve_customer(self):
        while self.queue.empty() is False:
            for table in self.tables:
                time.sleep(0.1)
                if table.is_busy is False:
                    customer = self.queue.get()
                    table.is_busy = True
                    print(f'Посетитель номер {customer} сел за стол {table.number}.')
                    time.sleep(5)
                    print(f'Посетитель номер {customer} покушал и ушел.')
                    table.is_busy = False
            self.serve_customer()


class Customer(object):
    customer_count = 0

    def __init__(self):
        Customer.customer_count += 1
        self.customer_number = Customer.customer_count

    def __str__(self):
        return str(self.customer_number)


if __name__ == "__main__":
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]

    cafe = Cafe(tables)

    customer_arrival_thread1 = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread1.start()
    customer_arrival_thread1.join()