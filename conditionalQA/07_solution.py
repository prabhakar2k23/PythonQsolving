# Print only unique item
items = ["apple","lychee","mango","orange","kiwi","apple","mango"]
unique_item=list()

for i in items:
    if(i not in unique_item):
        unique_item.append(i)
    else:
        continue

print(unique_item)