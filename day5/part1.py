import math

def solve(data: str) -> int:

    def convert_string_to_map(lines: str, attributes: list[str]) -> list[range]:
        _, *map_stats = lines.split('\n')


        res = {
            attributes[1]: [],
            attributes[0]: []
        }

        for stats_line in map_stats:
            destination_range_start, source_range_start, range_length = stats_line.split(' ')
            res[attributes[1]].append((int(source_range_start), int(source_range_start) + int(range_length)))
            res[attributes[0]].append((int(destination_range_start), int(destination_range_start) + int(range_length)))

        return res

    def extract_from_mapping(value: int, mapping: dict) -> int:
        attr1, attr2 = mapping.keys()

        for i in range(len(mapping[attr1])):
            if mapping[attr1][i][0] <= value < mapping[attr1][i][1]:
                diff = value - mapping[attr1][i][0]
                return mapping[attr2][i][0] + diff

        return value


    seed_info, seed_to_soil_info, soil_to_fertilizer_info, fertilizer_to_water_info, water_to_light_info, light_to_temperature_info, temperature_to_humidity_info, humidity_to_location_info = data

    seeds = list(map(int, seed_info.split(': ')[-1].split(' ')))

    seed_to_soil_map = convert_string_to_map(seed_to_soil_info, ['soil', 'seed'])
    soil_to_fertilizer_map = convert_string_to_map(soil_to_fertilizer_info, ['fertilizer', 'soil'])
    fertilizer_to_water_map = convert_string_to_map(fertilizer_to_water_info, ['water', 'fertilizer'])
    water_to_light_map = convert_string_to_map(water_to_light_info, ['light', 'water'])
    light_to_temperature_map = convert_string_to_map(light_to_temperature_info, ['temperature', 'light'])
    temperature_to_humidity_map = convert_string_to_map(temperature_to_humidity_info, ['humidity', 'temperature'])
    humidity_to_location_map = convert_string_to_map(humidity_to_location_info, ['location', 'humidity'])

    min_location = math.inf

    for seed in seeds:
        soil = extract_from_mapping(seed, seed_to_soil_map)
        fertilizer = extract_from_mapping(soil, soil_to_fertilizer_map)
        water = extract_from_mapping(fertilizer, fertilizer_to_water_map)
        light = extract_from_mapping(water, water_to_light_map)
        temperature = extract_from_mapping(light, light_to_temperature_map)
        humidity = extract_from_mapping(temperature, temperature_to_humidity_map)
        location = extract_from_mapping(humidity, humidity_to_location_map)

        min_location = min(min_location, location)

    return min_location


with open('input.txt', 'r') as f:
# with open('small.txt', 'r') as f:
    lines = f.read().split('\n\n')

print(solve(lines))
