united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

united_kingdom [1]["name"] = "Cardiff"

country_4 = {
  "name": "Northern Ireland",
  "population": 1811000,
  "capital": "Belfast"
}

united_kingdom.append(country_4)

for country in united_kingdom:
  print(country["name"])

total_population = 0
for country in united_kingdom:
  total_population += country["population"]
print(total_population)

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
# 3. Use a loop to print the names of all the countries in the UK.
# 4. Use a loop to find the total population of the UK.
