"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = list()
    if len(line)==1:
        result = line
    else:
        lst = list()
        for dummy_num in line:
            if dummy_num != 0:
                lst.append(dummy_num)
        skip_pos = False
        for dummy_index in range(len(lst)-1):
            if not skip_pos:
                if lst[dummy_index] == lst[dummy_index+1]:
                    result.append(2*lst[dummy_index])
                    skip_pos = True
                else:
                    result.append(lst[dummy_index])
                    skip_pos=False
            else:
                skip_pos = False
        if not skip_pos:
            result.append(lst[-1])
        if len(result) < len(line):
            for dummy_i in range(len(line)-len(result)):
                result.append(0)

    return result
