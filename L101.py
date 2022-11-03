#Emily Rusch and Kaylen Nyhuis
dict = {"k": 2, "a": 3,  "y" : 5, "l":  3, "e": 7, "n":  9, "m": 0, "i": 9}
def my_get_method(x, y):
    d = dict
    if x in d:
        print (dict[x])
    else:
        print(y)

my_get_method("a", 8)
my_get_method("z", 0)

dict.get("a", 8)
dict.get("z", 0)
