import json

data = [['cards', 'win', '%win', 'lose', '%lose', 'tie', '%tie', 'EV'],
         ['Ac', '7c', '375672', '27.41', '990580', '72.27', '4502', '0.33', '0.275'],
         ['5s', '4s', '271553', '19.81', '1094699', '79.86', '4502', '0.33', '0.199'],
         ['Ks', 'Kd', '719027', '52.45', '647225', '47.22', '4502', '0.33', '0.526']]

number_of_keys = len(data[0])

json_data = {
  "headers": data[0],
  "values": data[1:]
}

print(json.dumps(json_data, indent=2))