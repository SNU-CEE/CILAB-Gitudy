from pymilvus import CollectionSchema, FieldSchema, DataType

# PROJECT_STRUCTURED
project_id = FieldSchema(name="project_id", dtype=DataType.INT64, is_primary=True)
project_expense = FieldSchema(name="project_expense", dtype=DataType.INT32)
project_type = FieldSchema(name="project_type", dtype=DataType.VARCHAR)
project_orderer = FieldSchema(name="project_orderer", dtype=DataType.VARCHAR)

# PROJECT_UNSTRUCTURED
project_name = FieldSchema(name="project_name", dtype=DataType.VARCHAR, is_primary=True)
project_scale = FieldSchema(name="project_scale", dtype=DataType.VARCHAR)
project_location = FieldSchema(name="project_location", dtype=DataType.VARCHAR)
project_overview = FieldSchema(name="project_overview", dtype=DataType.VARCHAR)
project_detail = FieldSchema(name="project_detail", dtype=DataType.VARCHAR)

# BC RATIO
bc_ratio_plan = FieldSchema(name="bc_ratio_plan", dtype=DataType.FLOAT)
bc_ratio_actual = FieldSchema(name="bc_ratio_actual", dtype=DataType.FLOAT)

# GRADIENT
gradient_bc = FieldSchema(name="gradient_bc", dtype=DataType.FLOAT)
gradient_demand = FieldSchema(name="gradient_demand", dtype=DataType.FLOAT)
gradient_expense = FieldSchema(name="gradient_expense", dtype=DataType.FLOAT)
gradient_period = FieldSchema(name="gradient_period", dtype=DataType.FLOAT)

# COMMUNITY
community_population = FieldSchema(name="community_population", dtype=DataType.FLOAT)
community_employee = FieldSchema(name="community_employee", dtype=DataType.FLOAT)
community_gdp = FieldSchema(name="community_gdp", dtype=DataType.INT64)
community_population = FieldSchema(name="community_population", dtype=DataType.FLOAT)

# COMPLAINT
complaint_occur = FieldSchema(name="complaint_occur", dtype=DataType.INT16)
complaint_handle = FieldSchema(name="complaint_handle", dtype=DataType.INT16)

# DEFECT
defect_occur = FieldSchema(name="defect_occur", dtype=DataType.INT16)
defect_handle = FieldSchema(name="defect_handle", dtype=DataType.INT16)

# DATE
date_completion = FieldSchema(name="date_completion", dtype=DataType.STRING)
date_evaluation = FieldSchema(name="date_evaluation", dtype=DataType.STRING)

book_name = FieldSchema(
  name="book_name",
  dtype=DataType.VARCHAR,
  max_length=200,
  # The default value will be used if this field is left empty during data inserts or upserts.
  # The data type of `default_value` must be the same as that specified in `dtype`.
  default_value="Unknown"
)
word_count = FieldSchema(
  name="word_count",
  dtype=DataType.INT64,
  # The default value will be used if this field is left empty during data inserts or upserts.
  # The data type of `default_value` must be the same as that specified in `dtype`.
  default_value=9999
)

schema = CollectionSchema(
  fields=[book_id, book_name, word_count, book_intro],
  description="Test book search",
  enable_dynamic_field=True
)
collection_name = "book"

from pymilvus import connections, db
conn = connections.connect(host="127.0.0.1", port=19530)

from pymilvus import Collection
collection = Collection(
    name=collection_name,
    schema=schema,
    using='default',
    shards_num=2
    )
print(collection)
print(collection.schema)
