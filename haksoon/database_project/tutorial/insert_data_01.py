import random
data = [
  [i for i in range(2000)],
  [str(i) for i in range(2000)],
  [i for i in range(10000, 12000)],
  [[random.random() for _ in range(2)] for _ in range(2000)],
]

# data.append([str("dy"*i) for i in range(2000)])

from pymilvus import connections, db
conn = connections.connect(host="127.0.0.1", port=19530)

from pymilvus import Collection
collection = Collection("book")      # Get an existing collection.
mr = collection.insert(data)



# index_params = {
#   "metric_type":"L2",
#   "index_type":"IVF_FLAT",
#   "params":{"nlist":1024}
# }

# from pymilvus import Collection, utility
# collection = Collection("book")      
# collection.create_index(
#   field_name="book_intro", 
#   index_params=index_params
# )

# utility.index_building_progress("book")





# collection.load()

# search_params = {
#     "metric_type": "L2", 
#     "offset": 5, 
#     "ignore_growing": False, 
#     "params": {"nprobe": 10}
# }

# results = collection.search(
#     data=[[0.1, 0.2]], 
#     anns_field="book_intro", 
#     # the sum of `offset` in `param` and `limit` 
#     # should be less than 16384.
#     param=search_params,
#     limit=10,
#     expr=None,
#     # set the names of the fields you want to 
#     # retrieve from the search result.
#     output_fields=['title'],
#     consistency_level="Strong"
# )

# print(results[0].ids)
# print(results[0].distances)

# hit = results[0][0]

# print(hit)
# print(hit.entity.get('title'))
