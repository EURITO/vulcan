import pandas as pd

def flatten_list(a_list,freq=False,norm=False):
    '''
    Flattens a list. Offers the option to count term occurrences

    Args:
        a_list (list) is a nested list
        freq (Bool) is whether we want the flat list or frequencies
        norm (Bool) is whether we want to normalise frequencies (only relevant when calculating these)

    '''

    fl = [x for el in a_list for x in el]

    if freq==False:
        return(fl)
    else:
        return(pd.Series(fl).value_counts(norm))

