import requests

api_key = "236b4e4775ebf81e9be0655e4742ed2f"

def loc2geocode(address):
    url = f"https://restapi.amap.com/v3/geocode/geo?key={api_key}&address={address}"
    response = requests.get(url)
    data = response.json()
    try:
        location = data['geocodes'][0]['location']
        longitude, latitude = location.split(',')
        return float(longitude), float(latitude)
    except Exception as ne:
        print(f"Raised {ne} by loc2geocode function..")
        return None, None

def geocode2loc(longitude, latitude):
    url = f"https://restapi.amap.com/v3/geocode/regeo?key={api_key}&location={longitude},{latitude}"
    response = requests.get(url)
    data = response.json()
    try:
        address = data['regeocode']['addressComponent']
        format_address = data['regeocode']['formatted_address']
        return address, format_address
    except Exception as ne:
        print(f"Raised {ne} by geocode2loc function..")
        return None, None

if __name__ == '__main__':
    address = "北京市中国人民大学"
    longitude, latitude = loc2geocode(address)
    print(f"x: {longitude}, y: {latitude}")
    address, format_address = geocode2loc(longitude, latitude)
    print(format_address)