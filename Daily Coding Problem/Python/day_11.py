'''
This problem was asked by Twitter:

Implement an autocomplete system. That is, given a string s and a set of possible
query strings return all strings in the set that have s as a prefix.

for example if the query string is "de"
and the set of strings is [dog, deer, deal], return [deer, deal]
'''

strings = ["dog", "deer", "deal"]


def autocomplete(strings, query=None):
    matches = []
    if not query:
        query = input("Prefix: ")
    for string in strings:
        str_match = list(string)
        q_match = list(query)
        search_len = len(q_match)
        if str_match[0:search_len] == q_match:
            matches.append(string)
    
    return matches


#print(autocomplete(strings))

print(autocomplete(["self", "supper", "secret", "sassy", "superb", "salt"]))