reference_manual = []
def print_color_map():
    global reference_manual
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            reference_manual.append(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(result == 24)
assert(reference_manual[0][0] == '1')
assert(reference_manual[0].find('|') == reference_manual[24].find('|') )
print("All is well (maybe!)\n")
