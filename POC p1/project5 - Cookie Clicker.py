"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(120)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookoes = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        print 'time', self.get_time()
        
        print 'time2 %f' % self.get_time()
        result = 'Time: %f Current Cookies: %.1f CPS: %.1f Total Cookies: %.1f History (length: %d): %s' \
        % (float(self.get_time()), self.get_cookies(), self.get_cps(), self._total_cookoes, len(self.get_history()), self.get_history())
        return result
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        result = list()
        for item in self._history:
            result += (item,)
        return list(result)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies < self.get_cookies():
            return 0.0
        else:
            time = math.ceil((cookies - self.get_cookies())/self.get_cps()) 
            return time
        
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time>0:
            new_cookies = self._cps*time
            self._total_cookoes += new_cookies
            self._current_cookies += new_cookies
            self._current_time += time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost<= self.get_cookies():
            self._current_cookies -= cost
            self._cps += additional_cps
            self._history.append((self.get_time(), item_name, cost, self._total_cookoes))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    time_left = duration
    clicker = ClickerState()
    
    while time_left >= 0:
        item = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history, time_left, build_info)
        print 'item', item
        if item is None:
            print 'None'
            clicker.wait(time_left)
            time_left = -1
        elif time_left < clicker.time_until(build_info.get_cost(item)):
            print 'low time'
            clicker.wait(time_left)
            time_left = -1
        else:
            print 'normal run'
            cost = build_info.get_cost(item)
            print 'cookies', clicker.get_cookies()
            print 'cost', cost
            wait_time = clicker.time_until(cost)
            print 'wait_time', wait_time
            time_left -= wait_time
            print 'time_left', time_left
            clicker.wait(wait_time)
            clicker.buy_item(item, cost, build_info.get_cps(item))
            
            print 'cps', clicker.get_cps()
            build_info.update_item(item)

    return clicker


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cost = float("inf")
    max_cookies = cookies + cps*time_left
    result = None
    for item in build_info.build_items():
        item_cost = build_info.get_cost(item)
        if  item_cost < cost:
            if item_cost <= max_cookies:
                cost = item_cost
                result = item
    return result

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    cost = float("-inf")
    max_cookies = cookies + cps*time_left
    result = None
    for item in build_info.build_items():
        item_cost = build_info.get_cost(item)
        if  item_cost > cost:
            if item_cost <= max_cookies:
                cost = item_cost
                result = item
    return result

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    def get_best_choice(time_left):
        """
        check optimal variant
        """
        new_item = dict()
        new_item['name'] = None
        new_item['profit'] = -1
        new_item['time']= 0
        for item in build_info.build_items():
            cost = build_info.get_cost(item)
            max_cost = cookies + cps*time_left
            time_wait = math.ceil((cookies - cost)/cps)
            if time_wait<0:
                time_wait = 0
            if (cost <= max_cost)and(time_left>=time_wait):
                new_cps = build_info.get_cps(item)+cps
                profit = time_wait*cps+(time_left-time_wait)*new_cps
                print profit
                if profit>new_item['profit']:
                    new_item['name'] = item
                    new_item['profit'] = profit
                    new_item['time'] = time_wait
                    
        return new_item
    
    
    # generate name-cps-cost list
    new_item = get_best_choice(time_left)
    time = new_item['time']
    while time>1:
        print 'time', time
        one_item = get_best_choice(int(new_item['time']))
        if one_item['name'] is not None:
            new_item = one_item 

    
            
    
    print new_item
    
    return new_item['name']

simulate_clicker(provided.BuildInfo(), SIM_TIME, strategy_best)

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)


    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

#run()
