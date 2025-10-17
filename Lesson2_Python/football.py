import sys

sports_markets = [
    {"city": "Arizona", "nfl": "Cardinals", "mlb": "Diamondbacks", "nba": "Suns", "nhl": "Coyotes"},
    {"city": "Atlanta", "nfl": "Falcons", "mlb": "Braves", "nba": "Hawks"},
    {"city": "Baltimore", "nfl": "Ravens", "mlb": "Orioles"},
    {"city": "Boston", "nfl": "Patriots", "mlb": "Red Sox", "nba": "Celtics", "nhl": "Bruins"},
    {"city": "Buffalo", "nfl": "Bills", "nhl": "Sabres"},
    {"city": "Carolina", "nfl": "Panthers", "nba": "Hornets", "nhl": "Hurricanes"},
    {"city": "Chicago", "nfl": "Bears", "mlb": "Cubs/White Sox", "nba": "Bulls", "nhl": "Blackhawks"},
    {"city": "Cincinnati", "nfl": "Bengals", "mlb": "Reds"},
    {"city": "Cleveland", "nfl": "Browns", "mlb": "Guardians", "nba": "Cavaliers"},
    {"city": "Dallas", "nfl": "Cowboys", "mlb": "Rangers", "nba": "Mavericks", "nhl": "Stars"},
    {"city": "Denver", "nfl": "Broncos", "mlb": "Rockies", "nba": "Nuggets", "nhl": "Avalanche"},
    {"city": "Detroit", "nfl": "Lions", "mlb": "Tigers", "nba": "Pistons", "nhl": "Red Wings"},
    {"city": "Green Bay", "nfl": "Packers"},
    {"city": "Houston", "nfl": "Texans", "mlb": "Astros", "nba": "Rockets"},
    {"city": "Indianapolis", "nfl": "Colts", "nba": "Pacers"},
    {"city": "Jacksonville", "nfl": "Jaguars"},
    {"city": "Kansas City", "nfl": "Chiefs", "mlb": "Royals"},
    {"city": "Las Vegas", "nfl": "Raiders", "nhl": "Golden Knights"},  # MLB Athletics move pending
    {"city": "Los Angeles", "nfl": "Rams/Chargers", "mlb": "Dodgers/Angels", "nba": "Lakers/Clippers", "nhl": "Kings/Ducks"},
    {"city": "Miami", "nfl": "Dolphins", "mlb": "Marlins", "nba": "Heat", "nhl": "Panthers"},
    {"city": "Milwaukee", "mlb": "Brewers", "nba": "Bucks"},
    {"city": "Minnesota", "nfl": "Vikings", "mlb": "Twins", "nba": "Timberwolves", "nhl": "Wild"},
    {"city": "Nashville", "nfl": "Titans", "nhl": "Predators"},
    {"city": "New Orleans", "nfl": "Saints", "nba": "Pelicans"},
    {"city": "New York", "nfl": "Giants/Jets", "mlb": "Yankees/Mets", "nba": "Knicks/Nets", "nhl": "Rangers/Islanders/Devils"},
    {"city": "Philadelphia", "nfl": "Eagles", "mlb": "Phillies", "nba": "76ers", "nhl": "Flyers"},
    {"city": "Pittsburgh", "nfl": "Steelers", "mlb": "Pirates", "nhl": "Penguins"},
    {"city": "San Francisco Bay Area", "nfl": "49ers", "mlb": "Giants/Athletics", "nba": "Warriors", "nhl": "Sharks"},
    {"city": "Seattle", "nfl": "Seahawks", "mlb": "Mariners", "nhl": "Kraken"},
    {"city": "Tampa Bay", "nfl": "Buccaneers", "mlb": "Rays", "nhl": "Lightning"},
    {"city": "Washington", "nfl": "Commanders", "mlb": "Nationals", "nba": "Wizards", "nhl": "Capitals"}
]

city_search = (input("City: ").capitalize())
league = (input("League: ").lower())

for entry in sports_markets:
    if city_search == entry["city"]:
        try:
            entry.get(league) == entry[league]
            print(f"The {league} team in {city_search} is the {entry.get(league)}")  
        except KeyError:
            print(f"There is no {league} team in {city_search}.")
    elif city_search!= entry["city"]:
        print(f"There is no {league} team in {city_search}.")
        sys.exit(1)