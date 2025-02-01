def solve(numheads, numlegs):

    for c in range(numheads + 1):
        r = numheads - c
        if 2 * c + 4 * r == numlegs:
            return c, r
    return None, None


numheads = int(input("Enter number of heads: "))
numlegs = int(input("Enter number of legs: "))
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
