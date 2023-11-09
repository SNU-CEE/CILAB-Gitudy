from pymilvus import connections
conn = connections.connect(host="127.0.0.1", port=19530)

index_params = {
  "metric_type":"L2",
  "index_type":"IVF_FLAT",
  "params":{"nlist":1024}
}


from pymilvus import Collection, utility
collection = Collection("book")      
collection.create_index(
  field_name="book_intro", 
  index_params=index_params
)

utility.index_building_progress("book")
