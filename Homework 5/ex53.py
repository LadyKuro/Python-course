import random

def random_walk(start):
    """Simulate a random walk starting at the given integer."""
    position = start
    i = 0
    while True:
        position += random.choice([-1, 1])
        yield position
        i += 1
        if i % 100 == 0:
            position = start

experiment_results = []
counter = 0
for i in random_walk(0):
    counter += 1
    if counter % 99 == 0:
        experiment_results.append(i)
    if counter == 100000:
        break

print(experiment_results[:30])
print(sum(experiment_results)/len(experiment_results))