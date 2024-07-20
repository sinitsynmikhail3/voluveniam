# Sample list
data = [10, 20, 30, 40, 50]

# Iterate over the range, excluding the first and last indices
for i in range(1, len(data) - 1):
    print(f'Index: {i}, Current: {data[i]}, Left Neighbor: {data[i - 1]}, Right Neighbor: {data[i + 1]}')
