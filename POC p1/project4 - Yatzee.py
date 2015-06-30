"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            pos_outcomes = list(outcomes)
            for elm in partial_sequence:
                pos_outcomes.remove(elm)
            for item in outcomes:
                if item in pos_outcomes:                 
                    new_sequence = list(partial_sequence)
                    new_sequence.append(item)
                    new_item = list(new_sequence)
                    new_item.sort()
                    temp_set.add(tuple(new_item))
            answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    result = [0 for _ in range(6)]
    for dice in hand:
        result[dice-1] += dice
    return max(result)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    result = ()
    variants = num_die_sides**num_free_dice
    print variants
    dice_sum = 0
    for side_number in range(num_die_sides):
        print 'side_number', side_number
        dice_sum += (side_number+1)*num_free_dice
    print 'dice_sum', dice_sum
    print 'float(dice_sum)/variants', float(dice_sum)/variants
    result = 3.5*(num_free_dice)- float(dice_sum)/variants
    print result
#-----------------------
    print 'try find result:'
    delta = 3.5*len(held_dice)-sum(held_dice)
    print 'delta', delta


#-----------------------
    return result+1


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    result = list([()])
    for item in hand:
        result += ([(item,)])
#    result += ([(item,)])
    if len(hand)>1:
        result += ([(hand)])
    
    result = list([()]) 
    for idx in range(len(hand)):
        result += gen_all_sequences(hand, idx)
    #if len(hand)>1:
    result += ([(hand)])        
    return set(result)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    result = 0
  #  for dice in hand:
  #      for side in range(num_die_sides):
  #         result += side+1
    print result
    result =  float(result) / num_die_sides    
    print result    
    return (result, ())


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    


print expected_value((2, 2), 6, 2) 
print expected_value((1,), 6, 2)

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



