import csv
import geopy.distance
from json import dumps

def closest_venues(lat : float, long : float, limit : int):

    # Initial Object
    venues = {}
    distances = {}
    all_categories = []

    with open('venues.csv', newline = '', encoding = "utf-8") as FILE:
        reader = csv.DictReader(FILE)

        num_restaurants = 0
        for restaurant in reader:
            r_categories = restaurant['categories'].split(",")
            r_lat = float(restaurant['latitude'])
            r_long = float(restaurant['longitude'])
            dist = geopy.distance.distance((r_lat, r_long), (lat, long)).km 

            # Update the distance to the given lat/long for each restaurant
            distances.update({dist : (restaurant['name'], restaurant['address'], restaurant['categories'])})

            # Get all categories from the csv
            for category in r_categories:
                if category != 'NULL' and '$' not in category:
                    all_categories.append(category)

            num_restaurants += 1

        
        # Sort categories alphabetically
        categories = sorted(set(categories), key=str.casefold)

        # Update venues object {category : [restaurant details]}
        for category in categories:
            venues.update({category : []})
    
    # sort restaurants by distance to given lat/long
    distances = sorted(distances.items(), key=lambda tup: tup[0])

    # Check limit is less than or equal to num_restaurants, to prevent out of bounds access
    if limit > num_restaurants:
        limit = num_restaurants

    # update venues dictionary, for closest X restaurants
    for category, List in venues.items():
        for i in range(limit):
            restaurant = distances[i]
            v_categories = restaurant[1][2]
            v_categories = v_categories.split(",")
            if category in v_categories:
                List.append({"name" : restaurant[1][0], "address" : restaurant[1][1]})

    venues = sorted(venues.items(), key=lambda tup: len(tup[1]), reverse = True)
    

    # Populate final return object
    result = []
    for venue in venues:
        if len(venue[1]) > 0:
            result.append({"category": venue[0], "venues" : venue[1]})

    return result