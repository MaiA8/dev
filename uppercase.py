from cs50 import get_string

before = get_string("before: ")
#print("after: ", end="")
#for c in before:
#    print(c.upper(), end="")

print(f"after: {before.upper()}")
print(f"after: {before.lower()}")
print(f"after: {before.capitalize()}")