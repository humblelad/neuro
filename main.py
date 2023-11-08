import netlas
import json
apikey = "enternetlasapi"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# Get user input for the query
d = input("Enter the domain: ")
netlas_query = netlas_connection.download(query="*."+d, datatype="domain",size=100,fields="domain")

count=0
def extract_domain(iterator):

    for json_bytes in iterator:
        # Decode the JSON bytes to a Python object
        json_object = json.loads(json_bytes)

        # Extract the domain value
        domain = json_object['data']['domain']

        # Yield the extracted domain value
        yield domain

file_path = "lol.txt"

try:
    # Step 1: Open the file in write mode
    with open(file_path, "w") as file:
        # Step 2: Write data to the file

        for domain in extract_domain(netlas_query):
            count=count+1
            file.write(domain+"\n")

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
else:
    print(f"Data has been successfully written to {file_path}.")

print(count)


