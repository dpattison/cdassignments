def draw_stars(a):
    for item in a:
        if isinstance(item, int):
            stars = ""
            for x in xrange(item):
                stars += "*"
            print stars
        elif isinstance(item, str):
            letters = ""
            for x in xrange(len(item)):
                letters += item[0].lower()
            print letters


y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
x = [4, 6, 1, 3, 5, 7, 25]



draw_stars(y)
