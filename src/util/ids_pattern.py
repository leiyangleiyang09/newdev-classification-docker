"""
@author Min LI
@date 02 March 2022
"""

neg_pattern = ['not ', 'no ', ' no', ':no', 'n/a', 'non-', 'not-', 'unavailable', 'exclude', 'virtual', 'demo',
               'display', 'without', 'information', 'choice', 'floorplan', 'illustr', 'virtua', 'supplied',
               'purchase', 'nego', 'option', 'request', 'possible', 'addition', 'photo', 'layout', 'depict',
               'store', 'information', 'disclaim', 'present', 'source', 'party', 'above', 'arrangement',
               'suit', 'source', 'unfortunately', "won't", 'wont', 'sorry', '@', '.com', 'www', 'http',
               'photograph', 'potential', 'dream', 'even', 'about to be completed']

p_patterns_pos = ['mortgagee', 'mortagee']
e_patterns_pos = ['deceased']

d_priceprefix_group_1_pos = [('vend', 'sell'), ('vend', 'sold'),
                             ('seller', 'sell'), ('seller', 'sold'),
                             ('owner', 'sell'), ('owner', 'sold'),
                             ('must', 'sell'), ('must', 'sold'),
                             ('keen', 'sell'), ('keen', 'sold')]
d_priceprefix_group_1_neg = ['more', 'another', 'by', 'see', 'if']

d_priceprefix_group_2_pos = [('want', 'sold'), ('want', 'sell'),
                             ('need', 'sold'), ('need', 'sell')]
d_priceprefix_group_2_neg = ['more', 'another', 'by', 'see']

d_priceprefix_group_3_pos = [('instruct', 'sold'), ('instruct', 'sell')]
d_priceprefix_group_3_neg = ['wait']

d_priceprefix_group_4_pos = ['urgent']
d_priceprefix_group_4_neg = ['more', 'another', 'by', 'see', 'if']

d_priceprefix_group_5_pos = ['quick sale']

d_priceprefix_group_6_pos = [('consider', 'all'),
                             ('reduc', 'heavily'), ('reduc', 'major'),
                             ('reduc', 'huge'), ('reduc', 'massive'),
                             ('reduc', 'again'), ('reduc', 'sell'),
                             ('reduc', 'relocat'), ('reduc', 'dramatic'),
                             ('drop', 'heavily'), ('drop', 'major'),
                             ('drop', 'huge'), ('drop', 'massive'),
                             ('drop', 'again'), ('drop', 'sell'),
                             ('drop', 'relocat'), ('drop', 'dramatic')]

d_summary_group_1_pos = [('vend', 'sell'), ('vend', 'sold'),
                         ('seller', 'sell'), ('seller', 'sold'),
                         ('owner', 'sell'), ('owner', 'sold'),
                         ('must', 'sell'), ('must', 'sold'),
                         ('keen', 'sell'), ('keen', 'sold')]
d_summary_group_1_neg = ['more', 'another', 'by', 'see', 'if']

d_summary_group_2_pos = [('want', 'sold'), ('want', 'sell')]
d_summary_group_2_neg = ['more', 'another', 'by', 'see', 'if']

d_summary_group_3_pos = ['need this sold', 'need to sell', 'need to be sold',
                         'need their home sold', 'need their home to be sold',
                         'needs this sold', 'needs to sell', 'needs to be sold',
                         'needs their home sold', 'needs their home to be sold']
d_summary_group_3_neg = ['offer']

d_summary_group_4_pos = [('instruct', 'sold'), ('instruct', 'sell')]
d_summary_group_4_neg = ['wait']

d_summary_group_5_pos = ['urgent']
d_summary_group_5_neg = ['more', 'another', 'by', 'see', 'if']

d_summary_group_6_pos = ['quick sale']

d_summary_group_7_pos = [('consider', 'all'),
                         ('reduc', 'heavily'), ('reduc', 'major'), ('reduc', 'huge'), ('reduc', 'massive'),
                         ('reduc', 'again'), ('reduc', 'sell'), ('reduc', 'relocat'), ('reduc', 'dramatic'),
                         ('drop', 'heavily'), ('drop', 'major'), ('drop', 'huge'), ('drop', 'massive'),
                         ('drop', 'again'), ('drop', 'sell'), ('drop', 'relocat'), ('drop', 'dramatic')]

d_description_group_1_pos = ['must sell', 'must be sold', 'keen to sell',
                             'want it sold', 'want sold', 'want them sold', 'want this sold', 'want to sell',
                             'wants it sold', 'wants sold', 'wants them sold', 'wants this Sold', 'wants to sell',
                             'urgent sale', 'motivated vendor', 'motivated seller', 'motivated owner', 'keen seller']
