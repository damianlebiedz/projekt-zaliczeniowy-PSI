# Range of timeframe
start_date = '2025-03-17'
end_date = '2025-04-17'

# Stock to analyze
# NOTE THAT IT SHOULD BE A STOCK/INDEX FROM US STOCK, otherwise the analysis can make no sense
# ticker = '^VIX' by default
ticker = '^VIX'

# How many days with the biggest change do you want to analyze
# num_of_biggest changes = 3 by default
num_of_biggest_changes = 3

# Number of first x comments sorted by the number of upvote to analyze from thread
# top_x = 50 by default, more is not recommended due to a time efficiency
top_x = 50

# Number of clusters you want the algorithm to create from the given data
# n_clusters = 5 by default
n_clusters = 5