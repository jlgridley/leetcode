def suggestedProducts(products, str):
    products = sorted(products)
    still_ok = [1 for i in range(len(products))]
    output = []
    for i in range(len(str)):
        currList = []
        for j in range(len(still_ok)):
            if not still_ok[j]:
                continue
            if str[i] == product[j][i]:
                currList.append(product[j])
                if len(currList) == 3:
                    break
            else:
                still_ok[j] = 0
        output.append(currList)
    return output

products = ["ca", "cb", "cc", "ccc", "cccc"]
str = "ccc"
"""
output = [["ca", "cb", "cc"], ["cc", "ccc", "cccc"], ["ccc", "cccc"]]
"""
# products = ["mobile","mouse","moneypot","monitor","mousepad"]
# str = "mouse"
#
# products = ["bags","baggage","banner","box","cloths"]
# str = "bags"
#
# products = ["havana"]
# str = "havana"
#
# products = ["havana"]
# str = "tatiana"

suggestedProducts(products, str)


"""
hunch: trie
no? then you have to get the rest of the word

naive solution:
sort products
for each prefix, search entire list of prefixes
O(n^2)

duplicated work:
have already iterated over previous prefixes
potential fix?: array indicating products still being considered
can just start at the letter at the current index
O(nlogn)?
sorting:
    worst case: multiple words with lower lexicographic value are eliminated

do we have to sort?
yes, because in the worst case, you have to sort them all anyway

sort products in ascending order
create array arr to indicate whether product is still a potential match (all initialized to 1)
initialize list of lists (output)
for each letter at index i in str:
    For each element == 1 in array:
        if letter at i equals the letter at i in str:
            add product to list of lists
            if you have 3 products in the list, break


test cases:
smallest possible
words in products are extremely similar

"""

"""
sort products in ascending order
create array `still_ok` to indicate whether product is still a potential match (all initialized to 1)
initialize list of lists (output)
for each letter at index i in str:
    For each element == 1 in array:
        if letter at i equals the letter at i in str:
            add product to list of lists
            if you have 3 products in the list, break
        else:
            set still_ok[i] to 0
"""
