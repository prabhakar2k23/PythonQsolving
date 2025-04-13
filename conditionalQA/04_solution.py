#Q. Determine if a fruit is ripe,overripr, or unripe based on its color.
#(e.g., Banana:Green-Unripe, Yellow-Ripe, Brown-Overripe)
fruits="Banana"
color="Brown"

if fruits=="Banana":
    if color=="Green":
       print("Unripe")
    elif color=="Yellow":
       print("Ripe")
    elif color=="Brown":
       print("Overripe")
else:
   print("Not a banana")
