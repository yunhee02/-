import requests

url = 'http://apis.data.go.kr/1543061/animalShelterSrvc/shelterInfo'
params ={'serviceKey' : 'b%2BtgQOSKFv%2F5ivIKWS9DtVAEL6QjkOnwyWjwFf5Bhwlg6aoUfxeDA03PNDVNfYFXk3cFG67aBMMsmriS5X5f%2BQ%3D%3D', 'care_reg_no' : ' ', 'care_nm' : ' ', 'numOfRows' : '3', 'pageNo' : '1', '_type' : ' ' }

response = requests.get(url, params=params)
print(response.content)