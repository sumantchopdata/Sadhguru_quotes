#%%
# Check if there are duplicate quotes
quote_lists = []
file_names = ['sadhguru_quotes_1_cleaned.txt', 'sadhguru_quotes_2_cleaned.txt',
              'sadhguru_quotes_3_cleaned.txt', 'sadhguru_quotes_4_cleaned.txt',
              'sadhguru_quotes_5_cleaned.txt']

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        quotes = file.read().splitlines()
        quote_lists.append(quotes)

all_quotes = [quote for quotes in quote_lists for quote in quotes]

unique_quotes = list(set(all_quotes))
print(len(all_quotes))
#%%
duplicates = [quote for quote in all_quotes if all_quotes.count(quote) > 1]
print(len(duplicates))
#%%
# Remove duplicates
unique_quotes = []
for q in all_quotes:
    if q in duplicates:
        all_quotes.remove(q)

print(len(unique_quotes))
print(len(all_quotes))
#%%
# Check if any quotes are empty
empty_quotes = [quote for quote in unique_quotes if quote == '']
print(len(empty_quotes))
#%%
# Remove the elements 'quotation mark', 'Jan 10, 2021' and 'Mar 8, 2021' from unique_quotes
all_quotes = [quote for quote in all_quotes if quote != 'quotation mark']
all_quotes = [quote for quote in all_quotes if quote != 'Jan 10, 2021']
all_quotes = [quote for quote in all_quotes if quote != 'Mar 8, 2021']

print(len(all_quotes))
# %%
# Save the quotes to a text file
with open('sadhguru_quotes_cleaned.txt', 'w', encoding='utf-8') as file:
    for quote in all_quotes:
        file.write(quote + '\n')
#%%
# print all the lengths of the quotes in words
lengths = []
for quote in all_quotes:
    lengths.append(len(quote.split(' ')))
print(lengths)
#%%
# print the quote with the most words
max_length = max(lengths)
print(max_length)
print(all_quotes[lengths.index(max_length)])