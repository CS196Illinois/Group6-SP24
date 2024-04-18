import requests


def get_data(food_list):
    data_list = []
    for food in food_list:
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(food)
        response = requests.get(api_url, headers={'X-Api-Key': 'YL3SDxlSUYRbBz2X2mRgNw==nwTO87jdfvCFVhyA'})
        if response.status_code == requests.codes.ok:
            data_list.append(response.json())  # Assuming the response is in JSON format
        else:
            print("Error:", response.status_code, response.text)
    return data_list

# Example usage:
foodList = ['1lb brisket and fries', 'apple', 'banana']

result = get_data(foodList)
print(result)
