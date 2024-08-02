import requests
import pprint
import numpy as np
import pandas as pd

# requests используется для запросов к http-серверам для получения/отправки информации/данных
# <Response [200]> - ответ на http-запрос GET
r = requests.get("https://api.github.com")
print(r)

# Возвращает json-объект ответа с сервера, до этого можно проверить ответ с сайта чтоб r.json() не дало ошибку
if r.status_code == 200:
    pprint.pprint(r.json())
elif r.status_code == 404:
    print("Didn't receive a valid response from the server.")

# application/json; charset=utf-8 - можно обратиться к определенному хэдеру из ответа request.headers, словарь
print(r.headers['content-type'])

# Насколько пишут на сайте https://pandas.pydata.org/docs/user_guide/10min.html#min, numpy и pandas обычно импортируются
# вместе
# pandas работает с двумя типами данных - series и dataframe
# np.nan - репрезентация значения 'not a number' с плавающей точкой (поэтому dtype: float64)
ex_series = pd.Series([2, 4, 6, np.nan, 20])
print(ex_series)

# пример dataframe
free_time = pd.date_range('20240729', periods=14)
df = pd.DataFrame(np.random.randn(14, 14), index=free_time, columns=list(range(14)))
print(df)
