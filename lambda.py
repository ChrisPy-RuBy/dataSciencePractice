
echo_word = (lambda word1, echo: word1 * echo)

result = echo_word('hey', 5)

print(result)


spells = ["protego", "accio", "expecto patronum",  "legilimens"]

shout_spells = map(lambda item: item + "!!!", spells)

shout_spells_list = list(shout_spells)
print (shout_spells_list)



nums = [2, 4, 6, 8, 10]

result = map(lambda a: a ** 2, nums)