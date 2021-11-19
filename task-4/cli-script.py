import os
import sys
import requests

if len(sys.argv) > 3:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 3:
    print('You need to specify the date and id to query')
    sys.exit()

def save_file(file_path, content):
    with open(file_path, 'w') as save_to_file:
        save_to_file.write(content)



payload = {'earth_date': sys.argv[1], 'api_key': 'EteRFwVGxW5FGYrzLheKfZfKGbrYTOHJ5Z33o8Vp'}
r = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/" + sys.argv[2] + "/photos", params=payload)

output_path = os.path.join(os.getcwd(), sys.argv[1])
if not os.path.isdir(output_path):
    os.makedirs(output_path)

save_file(os.path.join(output_path, 'query_response.json'), r.text)
