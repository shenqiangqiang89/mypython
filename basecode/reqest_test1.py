import  requests

res = requests.get("https://w-1.test.betawm.com/Beta.UserTokenExtH5Api/IsOk")

print(res.status_code)
print(res.headers)
print(res.content)
print(res.body)