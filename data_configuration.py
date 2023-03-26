import requests
from bs4 import BeautifulSoup
import os

# use the requests to send an HTTP requests to the NBA page
# and store the response variable
url = "https://www.nba.com/stats"
response = requests.get(url)

# create a beautiful soup object from the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# use find_all to extract all classes that contain player stats
data = []
tables = soup.find_all(
    'table', class_="LeaderBoardPlayerCard_lbpcTable__q3iZD")
# loop through all tables to extract player data
for table in tables:
    headers = [header.text for header in table.find_all('th')]
    for row in table.find_all('tr')[0:]:
        cells = row.find_all('td')
        player_name = cells[1].text.strip()
        try:
            points_per_game = cells[2].text.strip()
        except IndexError:
            points_per_game = "NA"
        data.append((player_name, points_per_game))

print(data)

# print the type of each element stored in tuple
for tup in data:
    for item in tup:
        print(type(item))

# convert digits to ints
data = [(int(x[0]), x[1]) if x[0].isdigit() else x for x in data]
print(data)
data = [(x[0], int(x[1])) if x[1].isdigit() else x for x in data]
print(data)

# filter the data so it only includes tuples with the first type of string
data = [tup for tup in data if isinstance(tup[0], str)]
print(data)

# slice the last two elements in the list since it contained garbage data
data = data[:-2]
print(data)

for i, (s, n) in enumerate(data):
    # Slice the string to separate the last three characters
    first_part, last_part = s[:-3], s[-3:]
    # Concatenate the first part with the last part separated by a whitespace
    new_s = f"{first_part} {last_part}"
    # Replace the original tuple with the new tuple
    data[i] = (new_s, n)

print(data)

len(data)

# separate into sub arrays for each category (points, rebounds, etc.)
sub_arrays = [data[i:i+5] for i in range(0, len(data), 5)]

print(sub_arrays)

# assign each category to relevant sub array
point_leaders = sub_arrays[0]
rebound_leaders = sub_arrays[1]
assist_leaders = sub_arrays[2]
block_leaders = sub_arrays[3]
steal_leaders = sub_arrays[4]
turnover_leaders = sub_arrays[5]
three_leaders = sub_arrays[6]
free_throw_leaders = sub_arrays[7]

print(point_leaders)
print(rebound_leaders)
print(assist_leaders)
print(block_leaders)
print(steal_leaders)
print(turnover_leaders)
print(three_leaders)
print(free_throw_leaders)

leading_scorer = point_leaders[0][0]
scorer_amt = point_leaders[0][1]

leading_rebounder = rebound_leaders[0][0]
rebounder_amt = rebound_leaders[0][1]

leading_assist = assist_leaders[0][0]
assist_amt = assist_leaders[0][1]

leading_blocks = block_leaders[0][0]
block_amt = block_leaders[0][1]

leading_steals = steal_leaders[0][0]
steal_amt = steal_leaders[0][1]

leading_turnovers = turnover_leaders[0][0]
turnover_amt = turnover_leaders[0][1]

leading_threes = three_leaders[0][0]
three_amt = three_leaders[0][1]

leading_ft = free_throw_leaders[0][0]
ft_amt = free_throw_leaders[0][1]


message = f"Stat Leaders for today:\n{leading_scorer} {scorer_amt} points \n{leading_rebounder} {rebounder_amt} rebounds \n{leading_assist} {assist_amt} assists\n{leading_blocks} {block_amt} blocks\n{leading_steals} {steal_amt} steals\n{leading_turnovers} {turnover_amt} turnovers\n{leading_threes} {three_amt} three pointers made\n{leading_ft} {ft_amt} free throws made"
