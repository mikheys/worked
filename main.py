country = ["Вьетнам", "китай", "швеция", "Ямайка", "Испания", "США", "мексика"]
for count in country:
    if count.lower() == "сша":
        print(count.upper())
    else:
        print(count.title())

