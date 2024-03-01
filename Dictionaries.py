# 5. Person: Use a dictionary to store information about a person you know.
Person = {"first_name": "Marta", "last_name": "Kharchenko", "age": "17", "city": "Kyiv"}
for key in Person:
    print(key, "->", Person[key])
print()

# 6. Glossary: A Python dictionary can be used to model an actual dictionary.
Glossary = {"Loop": "A sequence of instructions that is continually repeated until a certain condition is reached.",
            "Recursion": "An algorithm that calls itself recursively.",
            "Dictionary": "A data structure that maps keys to values and store them in an array or collection.",
            "Parameter": "A special kind of variable used in a function to refer to one pieces of data.",
            "Tuple": "An ordered sequence of values that is immutable."
            }
for key in Glossary:
    print(key, ":\n", Glossary[key])
