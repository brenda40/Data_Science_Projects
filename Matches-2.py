# Brenda Woodard ID# 873464752
# Searches a given dictionary for words matching a certain format

import sys
import re

def lines_matching(file, regexes):
    ''' Yields the lines of the file that match all of the given
    regular expressions'''

    # for standard in
    if file == sys.stdin:
        for line in file:
            if all(re.search(reg, line) for reg in regexes):
                yield line

    else:
        with open(file, mode = 'r', encoding = "utf8")as f:
            for line in f:
                if all(re.search(reg, line) for reg in regexes):
                    yield line

def main():
    ''' Processes the arguments. '''
    # extract argument
    argi = 1
    regexes = []
    while argi < len(sys.argv):
        arg = sys.argv[argi]
        # convert each flag into a regular expression and add to a list.
        # specify a lower bound
        if arg == '-l':
            m = int(sys.argv[argi+1])
            reg_exp_l = (fr'^.{{{m},}}$')
            regexes.append(reg_exp_l)
            argi += 1

        # specify an upper bound
        elif arg == '-u':
            n = int(sys.argv[argi+1])
            reg_exp_u = (fr'^.{{,{n}}}$')
            regexes.append(reg_exp_u)
            argi +=1

        # specify a list of characters to exclude
        elif arg == '-x':
            x = ''
            for _ in sys.argv[argi+1]:
                x += _
                x += '?'
            reg_exp_x = (fr'^[^{x}]*$')
            regexes.append(reg_exp_x)
            argi +=1

        # specify an order for the characters that only prints words containing
        # the given characters of STRING in the given order.
        elif arg == '-o':
            o = ''
            for _ in sys.argv[argi+1]:
                o += _
                o += '*'
            reg_exp_o = (fr'^{o}$')
            regexes.append(reg_exp_o)
            argi +=1
            pass

        # specify a subset requirement that only prints words that could be
        # made by removing characters from STRING.
        elif arg == '-s':
            s = ''
            for _ in sys.argv[argi+1]:
                s += _
                s += '?'
            reg_exp_s = (fr'^{s}$')
            regexes.append(reg_exp_s)
            argi +=1
            pass

        # assume remaining arguments are file names
        elif arg[0] != '-':
            # from each file, print lines matching all of the regular expressions
            matches = lines_matching(arg, regexes)
            for line in matches:
                print(line, end = '')

        else:
            # print to standard error and not to standard out
            print(f"unrecognized option: {arg}", file=sys.stderr)

        # next argument
        argi += 1

    # processes standard in if no file names are given
    else:
        while argi == len(sys.argv):
            arg = sys.stdin
            matches = lines_matching(arg, regexes)
            for line in matches:
                print(line, end = '')

# run main if script is executed
if __name__ == '__main__':
    main()
