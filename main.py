number = input("Phone number: ")
item = input("Item name: ")
category = input("Category(Lost/Found): ")
loc = input(f"Where was it {category}? ")
other = input("Other details(optional): ")

with open("data.csv", "a") as data:
    data.write(f"\n{number},{item},{category},{loc},{other}")

print(f"""
You entered:
Phone number: {number}
Item name: {item}
Category: {category}
Location: {loc}
Other details: {other}
""")
