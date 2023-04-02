animals = ["tiger", "Lion", "Rabbit", "Koala", "koala"]
k_list = []

for animal in animals:
    if animal.startswith("k") or animal.startswith("K"):
        k_list.append(animal) 
    
print(k_list)