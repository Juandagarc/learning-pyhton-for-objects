from objects import figures

def print_areas():
    for figure in figures:
        print(f"The area of the {figure.__class__.__name__} is: {figure.area()}")

if __name__ == "__main__":
    print_areas()
