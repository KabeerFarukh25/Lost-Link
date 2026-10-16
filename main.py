number = input("Phone number: ")
item = input("Item name: ")
category = input("Category(Lost/Found): ")
loc = input(f"Where was it {category}? ")
other = input("Other details(optional): ")

print(f"""
You entered:
Phone number: {number}
Item name: {item}
Category: {category}
Location: {loc}
Other details: {other}
""")
