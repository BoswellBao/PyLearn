import json

array = ['d', 'b', 'c', 'a', {'b':100, 'a':'letter a'}]
encodestr = json.dumps(array)
org_obj = json.loads(encodestr)
print(type(encodestr),encodestr)
print(type(org_obj),org_obj)
