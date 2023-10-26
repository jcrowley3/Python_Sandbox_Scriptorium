from dataclasses import dataclass, asdict

@dataclass
class MyClass:
    x_uuid: str = None
    y_uuid: str = None
    uuid: str = None

    @property
    def filtered_dict(self, ):
        return {k: v for k, v in vars(self).items() if k != "z"}

    # @property
    # def z(self, ):
    #     return self.__z

# m = MyClass(x_uuid="foo", y_uuid="bar", uuid="baz")

# get a dict with specific key, value pairs
# var1 = asdict(m, dict_factory=lambda x: {k: v for k, v in x if k in ["x_uuid"]})
# print(getattr(m, "x")) # foo

# print(m.filtered_dict) # {'x': 'foo', 'y': 'bar'}
# print(m.z) # 'baz'

# pytest assert statements with extra info
# def test_api_call_returns_status_200():
#     response = requests.get('https://example.com/api')
#     assert response.status_code == 200, f"The API call failed with status code {response.status_code}: {response.text}"


def check_it(checkie):
    if checkie:
        checkie = "bar"
        return checkie
    else:
        return False

def return_test(a_var):
    if check_it(a_var):
        return check_it(a_var)

    print("foo")



var1 = True

answer = return_test(var1)
print(answer)


{"insert into experience_image (experience_uuid,image_uuid,check,uuid,_filtered_dict) values ('c48ffe54551aef26e03e3a0774566bd714c47321f033c2887f763ffc','_Test!','True','c48ffe54551aef26e03e3a0774566bd714c47321f033c2887f763ffc_Test!','{'experience_uuid': 'c48ffe54551aef26e03e3a0774566bd714c47321f033c2887f763ffc', 'source_uuid_image': None, 'hero': None, 'active': None, 'resized': None, 'uuid': 'c48ffe54551aef26e03e3a0774566bd714c47321f033c2887f763ffc_Test!'}');"}

"insert into experience_image (experience_uuid,uuid) values ('c48ffe54551aef26e03e3a0774566bd714c47321f033c2887f763ffc','c48ffe54551aef26e03e3a0774566bd714c47321f033c2887f763ffc_Test!');"
