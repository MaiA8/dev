from cs50 import get_string
# user = {
#     "name":"Mai",
#     "age":26
#     "country":"Egypt"
# }
# print( user['name'] )

people = {
    "Mai":"01000",
    "Medo":"12345"
}
# "key":"value"
name = get_string("name: ")
if name in people:
    print(f"Number: {people[name]}")