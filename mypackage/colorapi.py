import requests

# * Gets data on 18k colors
def color_api():
    request = requests.get('https://color-names.herokuapp.com/v1/')
    all_colors = request.json()['colors']

    return all_colors

# * isolates the name and hex from the data
def name_hex(all_colors):
    name_hex = []

    # * iterates through the array and only use name and hex
    for _all in all_colors:
        only_color = _all['name']
        only_hex = _all['hex']

        # * put together in a tuple of lists
        name_hex.append([only_color, only_hex])

    return name_hex
