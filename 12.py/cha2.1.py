words = ["lion", "tiger", "cat", "dog", "rabbit", "elephant"]

newWords = [x for i,x in enumerate(words) if i % 2 == 1]
print(newWords)