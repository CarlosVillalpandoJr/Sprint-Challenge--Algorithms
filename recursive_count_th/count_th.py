'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# Go through word 
# Find occurances of 'th'
# Increment count for every 'th'

def count_th(word):
    # TBC
    if len(word) == 0:
        return 0
    else:
        count = 0
        if word[0:2] == 'th':
            count += 1
        return count + count_th(word[1:])





print(count_th('thealksdjaslaksjdthetheasdkjasdsad'))






