# Brenda Woodard 873464752
# worked with V.Phinney
# Performs an experiment to determine the probability of two people sharing
# a birthday

# Implement 3 functions
# function 1:
import random
import sys

def single_trial(people, days):
    ''' Randomly assigns each person a birthday '''
    duplicate = False
    bdays_dict = {}
    unique = set()

    for num in range(people):
        bdays_dict[num] = random.randint(1, days+1)

    for day in bdays_dict.values():
        unique.add(day)

    if len(unique) < people:
        duplicate = True
    return (duplicate)

# function 2:
def probability(people, days, trials):
    ''' Determines the probability of two people having the same birthday,
    given the amount of people, days, and trials. '''
    trial = 0
    successes = [0]
    while trial < int(trials):
        if single_trial(people, days):
            successes += 1
        trial += 1

    return (successes/int(trials))

# function 3:
def main():
    '''Processes arguments, accepts two flags, and prints the results
    in CSV format'''
    # default parameters
    people = 1
    trials = 100
    days = 365
    argi = 1
    successes = 0

    while argi < len(sys.argv):
      ## extract argument
      arg = sys.argv[argi]
      ## process valid flags
      if arg[0] != '-':
          break
      if arg == '-d':
        days = int(sys.argv[argi+1])
        argi += 1
      elif arg == '-t':
        trials = int(sys.argv[argi+1])
        argi += 1
      else:
        # prints to standard error and not to standard out
        print(f"unrecognized option: {arg}",
              file=sys.stderr)
      ## next argument
      argi += 1

    while people < int(days) + 1:
        prob_2 = probability(people, days, trials)
        print(people, ",", prob_2)
        people += 1
## run main if script is executed
if __name__ == "__main__":
    main()
