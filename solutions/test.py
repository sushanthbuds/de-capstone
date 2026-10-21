import pandas as pd 

data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})

logs["next_num"] = logs["num"].shift(1)
logs["previous_num"] = logs["num"].shift(-1)
logs = logs[(logs["num"] == logs["next_num"]) & (logs["num"] == logs["previous_num"])]

logs = logs.rename(columns={"num":"ConsecutiveNums"})

