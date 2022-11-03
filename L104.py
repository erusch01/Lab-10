#Emily Rusch and Kaylen Nyhuis
red_velvet = {"flour": 3, "baking soda" :1, "cocoa powder" : 2, "salt": .50, "butter": .50, "sugar" :2, "oil": 1, "eggs" : 4, "vanilla" : 1, "butttermilk": 1, "red food coloring": 1}
lemon = {"flour": 3, "baking powder": 2, "baking soda": .50, "salt": .50, "butter": 1, "sugar": 2, "vanilla": 2, "milk": 1, "lemon zest" : 1}
def cake():
    match = []
    x = red_velvet
    y = lemon
    for ingredient in x:
        if ingredient in y:
          match.append(ingredient)
    print(match)
cake()
