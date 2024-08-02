import multiprocessing


class WarehouseManager(object):
    def __init__(self):
        self.data = dict()

    def process_request(self, request):
        if request[1] == 'receipt':
            if request[0] in self.data.keys():
                self.data[request[0]] += request[2]
            else:
                self.data[request[0]] = request[2]
        elif request[1] == 'shipment':
            if request[0] in self.data.keys() and request[2] <= self.data[request[0]]:
                self.data[request[0]] -= request[2]
            elif request[0] in self.data.keys() and request[2] > self.data[request[0]]:
                self.data[request[0]] = 0
        #     else:
        #         print('Невозможно выполнить запрос.')
        # else:
        #     print("Нет изменений на складе.")

    def run(self, requests):
        with multiprocessing.Pool(processes=3) as pool:
            all_requests = []
            for request in requests:
                all_requests.append(request)
            pool.map(self.process_request, all_requests)


if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager.run(requests)
    print(manager.data)
