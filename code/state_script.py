from sys import argv

#filename = '/Users/baobaozhang/Dropbox/jpr-bst-file/tests/my_test.bib'
#new_file_name = '/Users/baobaozhang/Dropbox/jpr-bst-file/tests/my_test_py.bib'

filename = raw_input("Original bib file:")
new_file_name = raw_input("New bib file:")

# States Dictionary
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

# New Dictionary 
states_dic = dict(zip(states.values(), states.keys()))

# Find and Replace State Names  
def multipleReplace(text, wordDict):
    """
    take a text and replace words that match the key in a dictionary
    with the associated value, return the changed text
    """
    for key in wordDict:
        text = text.replace(key, wordDict[key])
    return text

# Go Through Each Line and Fine and Replace
with open(new_file_name, 'a') as n_file:
        with open(filename) as f:
            for line in f:
                if 'address' in line:
                        if 'New York, ' in line or '{New York' in line:
                                result = 'address = {New York},\n';
                                n_file.write(result)
                        else:
                                result = multipleReplace(line, states_dic)
                                n_file.write(result)
                else:
                        result = multipleReplace(line, states_dic)
                        n_file.write(result)




