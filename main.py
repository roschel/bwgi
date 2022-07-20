import csv
from pathlib import Path
from pprint import pprint
from typing import List, Tuple
from copy import deepcopy


def reconcile_accounts(transactions1: List[List[str]], transactions2: List[List[str]]) -> Tuple[List[List[str]], List[List[str]]]:
    transaction_1_copy = deepcopy(transactions1)
    
    for transaction in transactions1:
        if transaction in transactions2:
            transaction.append('FOUND')
        else:
            transaction.append('MISSING')
            
    for transaction in transactions2:
        if transaction in transaction_1_copy:
            transaction.append('FOUND')
        else:
            transaction.append('MISSING')
                
    return transactions1, transactions2

if __name__ == '__main__':
    transactions1 = list(csv.reader(Path('transactions1.csv').open()))
    transactions2 = list(csv.reader(Path('transactions2.csv').open()))
    out1, out2 = reconcile_accounts(transactions1, transactions2)
    pprint(out1)
    print('')
    pprint(out2)