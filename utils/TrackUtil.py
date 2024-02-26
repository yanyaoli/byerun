import json
import random
import time
from geopy.distance import geodesic

class Location:
    def __init__(self, id, location, edge):
        self.id = id
        self.location = location
        self.edge = edge

def gen(distance, locations):
    current_distance = 0
    start_index = random.choice(locations)
    current_location = start_index
    result = []

    start_time = int(time.time() * 1000) - 30 * 60 * 1000
    last_index = -1

    current = current_location.location.split(",")
    result.append(f"{current[0]}-{current[1]}-{start_time}-{rand_accuracy():.1f}")

    while current_distance < distance:
        current = current_location.location.split(",")
        edge = current_location.edge

        if not edge:
            print("edge为空")
        edge_index = random.choice(edge)
        if edge_index == last_index:
            edge_index = random.choice(list(set(edge) - {last_index}))
        next = locations[edge_index]

        start = current
        end = next.location.split(",")
        start_data = list(map(float, start))
        end_data = list(map(float, end))

        go_distance = calculate_distance(start_data, end_data)
        current_distance += go_distance

        start_time += go_distance / random.randint(1, 5) * 1000
        result.append(f"{end[0]}-{end[1]}-{start_time}-{rand_accuracy():.1f}")

        last_index = current_location.id
        current_location = next

    start_time += random.randint(5, 10) * 1000
    replace = current_location.location.replace(',', '-')
    result.append(f"{replace}-{start_time}-{rand_accuracy():.1f}")
    return json.dumps(result)

def calculate_distance(start, end):
    return geodesic((start[1], start[0]), (end[1], end[0])).meters

def rand_accuracy():
    return 10 * random.random()

def rand_int(a, b):
    return random.randint(a, b)

def genTrackPoints(runTime, map_choice):
    from app.Map import getMapData
    data = getMapData(map_choice)
    locations = [Location(d['id'], d['location'], d['edge']) for d in data]
    result = gen(runTime, locations)
    return result
