import json

data='{"name":"Nguyễn Văn A", "age": 20, "city":"Nam Định","phone": "0123456789"}'

my_data=json.loads(data)

print("Đối tượng Python từ dữ liệu JSON:", my_data)
print("Tên:", my_data['name'])
print("Tuổi:", my_data['age'])
print("Thành phố:", my_data['city'])
print("Số điện thoại:",my_data['phone'])