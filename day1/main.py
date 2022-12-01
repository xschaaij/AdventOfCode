data = list(map(lambda x: [int(y) for y in x], [x.splitlines() for x in open('day1/input.txt').read().split('\n\n')]))

elves = []
for x in data:
    elves.append({
        'backpack': x,
        'total_calories': sum(x)
    })
    
elves.sort(key=lambda x: x['total_calories'], reverse=True)

top3sum = sum(x['total_calories'] for x in elves[0:3])

print(top3sum)