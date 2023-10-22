#%%
# Lessgoo lets make a dataset of Sadhguru's quotes
import chardet

with open('Sadhguru Quotes old.txt', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

with open('Sadhguru Quotes old.txt', 'r', encoding=encoding) as file:
    quotes = file.readlines()

print(len(quotes))

# Remove all those elements from the list which are == '\n'
quotes = [quote for quote in quotes if quote != '\n']

# Remove those elements which start with Oct, Sep, Aug or Jul.
quotes = [q for q in quotes if not q.startswith(('Sep', 'Oct', 'Nov', 'Dec', 'Jan'))]

# For every element in the list, remove the '\n' at the end.
quotes = [q[:-1] for q in quotes]

# Remove the element 'quotation mark' from the list.
quotes.remove('quotation mark')
print(len(quotes))

# Save the list as a txt file.
with open('sadhguru_quotes_old_cleaned.txt', 'w', encoding=encoding) as f:
    for quote in quotes:
        f.write(quote + '\n')
#%%
# Let's make a dataset of Sadhguru's quotes
import chardet

with open('Sadhguru Quotes from quoteslifetime.com website.txt', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

with open('Sadhguru Quotes from quoteslifetime.com website.txt', 'r',
                                                    encoding=encoding) as file:
    quotes = file.readlines()

print(len(quotes))

quotes = [quote for quote in quotes if quote != '\n']
# Remove any element which has the word 'Sadhguru' or 'sadhguru' in it.
quotes = [q for q in quotes if 'Sadhguru' not in q]
quotes = [q for q in quotes if 'sadhguru' not in q]
quotes = [q for q in quotes if 'sadguru' not in q]
quotes = [q for q in quotes if 'quotes' not in q]

print(len(quotes))

# From each element, remove the '\n' at the end and any instance of ".
quotes = [q[:-1] for q in quotes]
quotes = [q.replace('"', '') for q in quotes]
print(len(quotes))

with open('sadhguru_quotes_2_cleaned.txt', 'w', encoding=encoding) as f:
    for quote in quotes:
        f.write(quote + '\n')
#%%
# Let's make a dataset of Sadhguru's quotes
import chardet

with open('Sadhguru Quotes from yogi.press website.txt', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

with open('Sadhguru Quotes from yogi.press website.txt', 'r',
                                                    encoding=encoding) as file:
    quotes = file.readlines()

print(len(quotes))
#%%
quotes = [quote for quote in quotes if quote != '\n']
#%%
quotes = [q.replace('” — Sadhguru', '') for q in quotes]
# quotes = [q.replace('“', '') for q in quotes]

print(len(quotes))
# %%
quotes.remove('…AND A FEW MORE QUOTES BY SADHGURU WE LOVE\n')
print(len(quotes))
# %%
# If the first character of the element is ' ', remove the space.
quotes = [q[1:] if q.startswith(' ') else q for q in quotes]
# %%
# Save the list as a txt file.
with open('sadhguru_quotes_4_cleaned.txt', 'w', encoding=encoding) as f:
    for quote in quotes:
        f.write(quote)
# %%
# Let's make a dataset of Sadhguru's quotes
import chardet

with open('Sadhguru Quotes from invajy.com website.txt', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

with open('Sadhguru Quotes from invajy.com website.txt', 'r',
                                                    encoding=encoding) as file:
    quotes = file.readlines()

print(len(quotes))
#%%
# Remove any line which has the word 'Sadhguru' and the word 'Quotes' in it.
quotes = [q for q in quotes if 'Quotes' not in q]
#%%
# Remove the characters '”~ Sadhguru' from each element.
quotes = [q.replace('”~ Sadhguru', '') for q in quotes]
# Remove the characters '“' from each element.
quotes = [q.replace('“', '') for q in quotes]

print(len(quotes))
#%%
# Remove the last 11 characters from each element.
quotes = [q[:-2] for q in quotes]
#%%
# Save the list as a txt file.
with open('sadhguru_quotes_5_cleaned.txt', 'w', encoding=encoding) as f:
    for quote in quotes:
        f.write(quote + '\n')
# %%
# Let's make a dataset of Sadhguru's quotes
import chardet

with open('Sadhguru Quotes from invajy.com website.txt', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

with open('Sadhguru Quotes from invajy.com website.txt', 'r',
                                                    encoding=encoding) as file:
    quotes = file.readlines()

print(len(quotes))