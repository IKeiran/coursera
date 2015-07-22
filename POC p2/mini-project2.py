"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result = list()
    for item in list1:
        if item not in result:
            result.append(item)
    return result

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = list()
    for item in list1:
        if item in list2:
            result.append(item)
    print result
    return result

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """ 
    max1 = len(list1)
    max2 = len(list2)
    index1, index2 = 0, 0
    result = list()
    for _ in range(max1+max2):
        if (index1 == max1):
            for item in list2[index2:]:
                result.append(item)            
            return result
        elif (index2 == max2):   
            for item in list1[index1:]:
                result.append(item)  
            return result
        elif (list1[index1]<=list2[index2]):
            result.append(list1[index1])
            index1 +=1 
        else:
            result.append(list2[index2])
            index2 +=1         
    return result
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if list1 == []:
        return list1
    else:
        centered = list1[0]
        lower = [item for item in list1 if item<centered]
        current = [item for item in list1 if item == centered]
        greater = [item for item in list1 if item > centered]
    return merge_sort(lower)+current+merge_sort(greater)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
#    Split the input word into two parts: the first character (first) and the remaining part (rest).
#Use gen_all_strings to generate all appropriate strings for rest. Call this list rest_strings.

    #For each string in rest_strings, generate new strings by inserting the initial character, first, in all possible positions within the string.
    #Return a list containing the strings in rest_strings as well as the new strings generated in step 3.
    print 'in gen, word: ', word
    if word == '':
        return ['']
    if len(word) == 1:
        lst = list(word)
        lst.append('',)
        print 'lst', lst
        return lst
    rest_strings = list()
    first = word[0]
    rest = word[1:]
    new_list = list(first)
    rest_strings += gen_all_strings(rest)
    print 'rest_strings', rest_strings
    
 #   if len (rest_strings)>0:
    for item in rest_strings:
        print 'work item: ', item
        if len(item)>0:
            new_list.append(item+first)
        for index in range(len(item)):
            begin = item[0:index]
            last = item[index:]
            tmp_str = begin+first+last
            print 'begin "%s" last "%s", insert %s' %(begin,last, first)
            print 'tmp_str', tmp_str
            print 'add: ', begin+first+last
            new_list.append(begin+first+last)
            
    #         new_list.append(rest_strings)
    new_list += rest_strings
    return new_list 

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    result = list()
    work_file = urllib2.urlopen(filename)
    for line in work_file:
        result.append(line[:-1])
    return result

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# print gen_all_strings('abc')
# Uncomment when you are ready to try the game
# run()

    
    
