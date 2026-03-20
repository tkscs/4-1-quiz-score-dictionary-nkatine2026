def make_dictionary(keys_list, values_list):
    """
    turn 2 lists into a dictionary
    
    Here are some tests. Make sure your code can handle these cases!
    >>> make_dictionary(["a", "b"], [1, 2])
    {'a': 1, 'b': 2}
    >>> make_dictionary([1, 2, 3], [5, 6, 7])
    {1:5, 2: 6, 3: 7}
    >>> make_dictionary(["a", "b", "c", "b"], ["apple", "banana", "clementine", "date"])
    {'a': 'apple', 'b': 'banana', 'c': 'clementine', 'd': 'date'}
    >>> make_dictionary(["key"], ["value"])
    {'key': 'value'}
    """

    return #### YOUR CODE HERE

print(make_dictionary(["a", "b"], [1, 2]))
print(make_dictionary([1, 2, 3], [5, 6, 7]))
print(make_dictionary(["a", "b", "c", "b"], ["apple", "banana", "clementine", "date"]))
print(make_dictionary(["key"], ["value"]))

# You have been given the following list fo students and their test scores:
names = ["Maria", "Nushi", "Mohammed", "Jose", "Wei", "John Doe"]
scores = [6.7, 2, 0, 189, 122, 1482239]

# Assign the result of make_dictionary to score_dict, which will be used in the
# exercises that follow.
score_dict = make_dictionary(names, scores)
score_dict = {"Maria":6.7, "Nushi":0, "Mohammed":189, "Jose":2, "Wei":122, "John Doe":1482239}
#2. Using `score_dict`, find the score for "Nushi"
#### YOUR CODE HERE
a = score_dict["Nushi"]
print(f"Nushi has a {a}")
# 3. Add a score 19 for "John"
#### YOUR CODE HERE
score_dict["joe"] = 19
# 4. Calculate the average of all the scores in `score_dict`
#### YOUR CODE HERE
b = (score_dict["Nushi"] + score_dict["joe"] + score_dict["Maria"] + score_dict["Jose"] + score_dict["Mohammed"] + score_dict["Wei"] - score_dict["John Doe"])/6
print(f"{b} is the class average for these idiots")
# 5. Update the score for "Wei" to be 13
#### YOUR CODE HERE
del score_dict["Wei"]
score_dict["Wei"] = 666
# 6. Nushi has just dropped this class. Delete "Nushi" and his score from
# `score_dict`
del score_dict["Nushi"]
print("Nushi is a weakling")
#### YOUR CODE HERE