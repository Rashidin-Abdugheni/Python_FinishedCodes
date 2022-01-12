#pip install bacdive
import bacdive
client = bacdive.BacdiveClient('17326099485@189.cn', 'M032711m')

# the search method fetches all BacDive-IDs matching your query
# and returns the number of IDs found
count = client.search(taxonomy='Blautia')
print(count, 'strains found.')

# the retrieve method lets you iterate over all strains
# and returns the full entry as dict
# Entries can be further filtered using a list of keys (e.g. ['keywords'])
for strain in client.retrieve():
    print(strain)


