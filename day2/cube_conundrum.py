from input import game_records

# utils


def parse_records(record: str):
    game_split = record.split(":")
    game_id = int(game_split[0].replace("Game ", ""))

    game_sets_str = game_split[1].replace(" ", "").split(";")
    game_sets = [game_set.split(",") for game_set in game_sets_str]

    return game_id, game_sets


# Part 1

max_red = 12
max_green = 13
max_blue = 14

possible_games = []

for record in game_records:
    game_id, game_sets = parse_records(record)

    possible = True

    for sets in game_sets:
        red, blue, green = 0, 0, 0
        for kube in sets:
            if "red" in kube:
                red = int(kube.replace("red", ""))
            elif "blue" in kube:
                blue = int(kube.replace("blue", ""))
            elif "green" in kube:
                green = int(kube.replace("green", ""))

        if red > max_red or blue > max_blue or green > max_green:
            possible = False
            break

    if possible:
        possible_games.append(game_id)

print("part 1: ", sum(possible_games))

# Part 2

powers = []

for record in game_records:
    max_red, max_blue, max_green = 0, 0, 0

    _, game_sets = parse_records(record)

    for sets in game_sets:
        red, blue, green = 0, 0, 0
        for kube in sets:
            if "red" in kube:
                red = int(kube.replace("red", ""))
            elif "blue" in kube:
                blue = int(kube.replace("blue", ""))
            elif "green" in kube:
                green = int(kube.replace("green", ""))

        if red > max_red:
            max_red = red
        if blue > max_blue:
            max_blue = blue
        if green > max_green:
            max_green = green

    powers.append(max_red * max_blue * max_green)

print("part 2: ", sum(powers))
