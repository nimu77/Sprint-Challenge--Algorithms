'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    '''
    this function counts the number of times 'th' 
    appears inside the string
    '''
   
    # empty string would be the base case
    if word == '':
        return 0
    # add the count by 1 if 'th' is present
    if word[0:2] == 'th':
        return 1 + count_th(word[1:])
    # otherwise keep moving to next index in a word
    else:
        return count_th(word[1:])