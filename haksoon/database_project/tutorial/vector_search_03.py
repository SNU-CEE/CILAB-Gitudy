from pymilvus import connections
conn = connections.connect(host="127.0.0.1", port=19530)

from pymilvus import Collection
collection = Collection("book")      # Get an existing collection.
collection.load()

search_params = {
    "metric_type": "L2", 
    "offset": 5, 
    "ignore_growing": False, 
    "params": {"nprobe": 10}
}

results = collection.search(
    data=[[0.1, 0.2]], 
    anns_field="book_intro", 
    # the sum of `offset` in `param` and `limit` 
    # should be less than 16384.
    param=search_params,
    limit=10,
    expr=None,
    # set the names of the fields you want to 
    # retrieve from the search result.
    output_fields=['book_name'],
    consistency_level="Strong"
)

results[0].ids
results[0].distances

print(results[0].ids)
print(results[0].distances)

hit = results[0][0]
hit.entity.get('book_name')

print(hit)
print(hit.entity.get('book_name'))
