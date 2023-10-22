#%%
import chardet

with open('sadhguru_quotes_cleaned.txt', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

with open('sadhguru_quotes_cleaned.txt', 'r', encoding=encoding) as file:
    quotes = file.readlines()
#%%

lines_to_change = [93, 383, 466, 486 396, 404, 423, 436, 437, 438]
# 383 is duplicate with 154, 466 is there in 436, 486 is a duplicate of 77
# 489 is there in 404
# 396, 404, 423, 436, 437, 438 are multiple quotes
#%%
# add the lengths of the quotes in words to a list and make its histogram
lengths = []
for quote in quotes:
    lengths.append(len(quote.split()))
plt.hist(lengths)