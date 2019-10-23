# Brenda Woodard # 873464752
# Takes a list of file names, which are assumed to contain raw HTML,
# and uses BeautifulSoup to parse the HTML in each of those files by
# searching for every table tag

import csv
import sys
from bs4 import BeautifulSoup

def table_to_list(table_tag):
    ''' Iterates through the rows of a table, extracting every column entry
     from that row, and returns the data as a list of lists. '''
    tr_tags = []
    for row in table_tag.find_all('tr'):
        tr = row.getText()
        tr_tag = tr.strip()
        tr_tags.append([tr_tag + ','])
    return tr_tags


def main():
    argi = 1
    while argi < len(sys.argv):
        arg = sys.argv[argi]
        # open the file name, create a BeautifulSoup object with its contents
        with open(arg) as f:
            table_tag = BeautifulSoup(f.read(), features="html5lib")

            # iterate over all table tags in that file
            table_tag.find_all('table')
            # convert each table into a two-dimensional list
            for table in table_tag:
                table_list = table_to_list(table)
                # print first row only
                print(table_list[0:1:1])


        # prompt user for file name
        name = input('enter file name:')
        # if user enters nothing, pass
        if name == '':
            pass
        # if user enters a name, open that file for writing & save as a CSV
        else:
            print(f'Saving {table_list} to {name}...')
            with open('name.csv', 'w') as f:
                wr = csv.writer(f)
                wr.writerows(table_list)
            f.close()

# run main if script is executed
if __name__ == '__main__':
    main()
