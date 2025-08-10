import weaviate
from weaviate.classes.query import Filter

client = weaviate.connect_to_local()

# Get the collection
job_postings = client.collections.get("JobPosting")

# Delete all objects where the 'job_id' property exists
response = job_postings.data.delete_many(
    where=Filter.by_property("job_id").like("*")
)

print(response)

client.close()