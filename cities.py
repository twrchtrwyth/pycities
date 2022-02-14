import random
import json

class CapitalCities:
    def __init__(self):
        self.filename = "country-capitals.json"
        with open(self.filename) as f:
            self.country_data = json.load(f)

    def get_continent_list(self):
        """Creates a list of all continents referred to in the json file.
        """
        self.continent_list = []
        for entry in self.country_data:
            continent = entry["ContinentName"]
            if continent in self.continent_list:
                # Ignore if already in list.
                pass
            else:
                # Add to the list.
                self.continent_list.append(continent)
        return self.continent_list

    def get_random_continent(self):
        self.get_continent_list()
        """Returns a random continent from the list."""
        random_index = random.randint(0, len(self.continent_list) - 1)
        return self.continent_list[random_index]

    def get_country_list(self, continent=False):
        """Returns a random country from the list. Can specify continent if
        desired.
        """
        self.country_list = []
        for entry in self.country_data:
            country = entry["CountryName"]
            if continent:
                # Only return countries from the specified continent.
                if entry["ContinentName"] == continent:
                    if country in self.country_list:
                        # Ignore if already in list.
                        pass
                    else:
                        # Add to the list.
                        self.country_list.append(country)
                else:
                    pass
            else:
                # Return all countries.
                if country in self.country_list:
                    # Ignore if already in list.
                    pass
                else:
                    # Add to the list.
                    self.country_list.append(country)
        return self.country_list

    def get_city_list(self, continent=False):
        """Returns a random city from the list. Can specify continent if
        desired.
        """
        self.city_list = []
        for entry in self.country_data:
            city = entry["CapitalName"]
            if continent:
                # Only return countries from the specified continent.
                if entry["ContinentName"] == continent:
                    if city in self.city_list:
                        # Ignore if already in list.
                        pass
                    else:
                        # Add to the list.
                        self.city_list.append(city)
                else:
                    pass
            else:
                # Return all countries.
                if city in self.city_list:
                    # Ignore if already in list.
                    pass
                else:
                    # Add to the list.
                    self.city_list.append(city)

    def get_random_country(self, continent=False):
        """Returns a random country from the list."""
        if continent:
            # Only return countries from the specified continent.
            self.get_country_list(continent)
        else:
            # Return all countries.
            self.get_country_list()
        random_index = random.randint(0, len(self.country_list) - 1)
        return self.country_list[random_index]

    def get_random_city(self, continent=False):
        """Returns a random city from the list."""
        if continent:
            # Only return countries from the specified continent.
            self.get_city_list(continent)
        else:
            # Return all countries.
            self.get_city_list()
        random_index = random.randint(0, len(self.city_list) - 1)
        return self.city_list[random_index]

    def get_capital_city(self, country):
        for entry in self.country_data:
            if entry["CountryName"] == country:
                return entry["CapitalName"]
            else:
                pass

    def get_country(self, city):
        for entry in self.country_data:
            if entry["CapitalName"] == city:
                return entry["CountryName"]
            else:
                pass


def guess_the_city(score, continent=False):
    capital_cities = CapitalCities()
    country = capital_cities.get_random_country(continent)
    guess = input(f"What is the capital of {country}? ")
    correct_answer = capital_cities.get_capital_city(country)
    if guess.lower() == correct_answer.lower():
        print("That's right!")
        score += 1
    else:
        print(f"Nope, the correct answer is {correct_answer}.")
        print(f"You answered {score} correctly in a row.")
        score = 0
    return score


def guess_the_country(score, continent=False):
    capital_cities = CapitalCities()
    city = capital_cities.get_random_city(continent)
    guess = input(f"{city} is the capital of which country? ")
    correct_answer = capital_cities.get_country(city)
    if guess.lower() == correct_answer.lower():
        print("That's right!")
        score += 1
    else:
        print(f"Nope, the correct answer is {correct_answer}.")
        print(f"You answered {score} correctly in a row.")
        score = 0
    return score


if __name__ == "__main__":
    # Determine whether to pick countries from specific continent.
    while True:
        continent = input("Specify a continent, or just hit enter. ").title()
        if continent in CapitalCities().get_continent_list():
            break
        elif continent == "":
            break
        else:
            print(f"Sorry, {continent} does not match any known continents.")

    # Determine whether to guess capital city from country, or vice versa.
    while True:
        mode = input("Do you want to guess countries (1) or cities (2)? ")
        if str(mode) not in ("1", "2"):
            print("Please enter either 1 or 2.")
        else:
            break

    # Main loop.
    score = 0
    while True:
        if str(mode) == "1":
            if continent:
                score = guess_the_country(score, continent)
            else:
                score = guess_the_country(score)
        elif str(mode) == "2":
            if continent:
                score = guess_the_city(score, continent)
            else:
                score = guess_the_city(score)
        play_again = input("Play again? (y/n) ")
        if play_again.lower() == "n":
            break
        elif play_again.lower() == "y":
            pass
        else:
            print("I'll take that as a yes.")
