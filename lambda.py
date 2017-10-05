from functools import reduce


echo_word = (lambda word1, echo: word1 * echo)

result = echo_word('hey', 5)

print(result)


spells = ["protego", "accio", "expecto patronum",  "legilimens"]

shout_spells = map(lambda item: item + "!!!", spells)

shout_spells_list = list(shout_spells)
print (shout_spells_list)



nums = [2, 4, 6, 8, 10]

result = map(lambda a: a ** 2, nums)


fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

result = filter(lambda member: len(member) > 6, fellowship)

print (list(result))

stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

result = reduce(lambda item1, item2: item1 + item2, stark)

print (result)

























