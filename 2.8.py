import json

data='{"name":"Nguyễn Văn A", "age": 20, "city":"Nam Định","phone": "0123456789"}'

json_data=json.dumps(data,indent=4)
print("Chuỗi JSON từ đối tượng Python:",json_data)
