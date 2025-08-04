# Animal Speak

Based on
[Inheritance Farm](https://github.com/hovey/pyschool/tree/master/src/pyschool/inheritance_farm),
a Python implementation demonstrating OOP and inheritance, this kata explores
reimplementation of that original implementation, but now with the context of
both Functional Programming (FP) approaches, and the Julia programming language.

At present, there will be two (and only two) types of animals: Dogs and Cats
on the farm.  Also, the farm is now just a "farm"; it is no longer considered
an "inheritance farm" because inheritance overly specifies implementation.

Dogs and Cats both have three attributes:

1. A `name` (string)
2. An `age` (integer)
3. They introduce themseves with either with either a "Ruff!" or "Meow!"

Dogs and Cats are either born on the farm, or they are adopted into the farm
long after they are born.  When they are born, their `age` is `0`, and then 
`1` at the first year, and so on.

Dogs and Cats have one behavior:  They `speak` with examples as shown below.

"Ruff. My name is Rex, and I am 1 year old."
"Ruff. My name is Fido, and I am 6 years old."
"Meow. My name is Kitty, and I am 0 years old."
"Meow. My name is Sylvester, and I am 2 years old."

Create an implementation with the above animals and their respective
four `speak` sentences.