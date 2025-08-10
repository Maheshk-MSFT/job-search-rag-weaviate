import weaviate

#client = weaviate.Client("http://localhost:8080")

client = weaviate.connect_to_local()

print("Client is ready:", client.is_ready())

client.close()
