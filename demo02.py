hdict = {
    "name":"张三",
    "high":"173cm",
    "key":"value",
    "dict1":{"name2":"李四"}
} #键值对 key：value


print(hdict["name"])
print(hdict["dict1"])
""" value = hdict.get("name") #通过key取值
print(value)


value2 = hdict.pop("dict1") #取走
print(value2)
print(hdict)

del hdict["high"]
print(hdict)

value3 = hdict.copy()
print(value3)


value4 = hdict.clear()
print(value4) """
