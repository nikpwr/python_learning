"""
--- Day 1: Not Quite Lisp ---

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?

--- Part Two ---

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?

Answers:
    - Part1: 74
    - Part2: 1795
"""

try:
    with open('c:/Users/np056433/OneDrive - Taitotalo/Python/AdventOfCode.2015.1/instructions.txt','r') as file:
        instructions = file.read().rstrip('\n')
except Exception as e :
    raise(f'File not found. Stopping {str(e)}')

# floorcount = 0
# for index, val in enumerate(instructions):
#     match val:
#         case '(':
#             floorcount += 1
#         case ')':
#             floorcount -= 1
#     if floorcount == -1 :
#         print(index+1)
# print(f'floorcount is {floorcount}')

kerros = 0
sijanti = None

for index, char in enumerate(instructions):
    kerros += 1 if char == '(' else -1
    if kerros == -1:
        if not sijanti:
            sijanti = index + 1

print(f'Osa 1: Kerros on {kerros}')
print(f'Osa 2: Sijanti {sijanti}')