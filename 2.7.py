import json

data='{"name":"Nguyễn Văn A", "age": 20, "city":"Nam Định","phone": "0123456789"}'

json_data=json.dumps(data)
print("Chuỗi JSON từ đối tượng Python:")
print(json_data)

# In ra tất cả các giá trị từ đối tượng Python
for key, value in data:
    print(f"{key}: {value}")