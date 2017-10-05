
def shout_echo(word1, echo=1):

  echo_word = ""
  shout_words = ""

  if echo < 0:
    raise ValueError ("echo must be greater than 0")
  else:
    echo_word = word1 * echo
    shout_word = echo_word + '!!!'    
  return shout_word

    # Call shout_echo
shout_echo("particle", echo=5)


# result = filter(lambda x: x[0:2] == "RT", tweets_df['text'])

# res_list = list(result)
# # Print all retweets in res_list
# for tweet in res_list:
#     print(tweet)

# Define count_entries()
def count_entries(df, col_name='lang'):
    cols_count = {}

    try:
        col = df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
        return cols_count
    except:
        'The DataFrame does not have a ' + col_name + ' column.'
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang1')
