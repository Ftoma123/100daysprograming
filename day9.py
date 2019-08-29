age = 36
text = "my age is {}"
print(text.format(age))

apple = 3
banana = 5
streberry = 10
text1 = "I bought {} apples, {} bananas and {} straeberry."

print(text1.format(apple, banana, streberry))


apple = 10
banana = 55
streberry = 30
text2 = "I bought {2} straeberry, {1} bananas and {0} apples."
print(text2.format(apple, banana, streberry))