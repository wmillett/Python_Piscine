def all_thing_is_obj(object: any) -> int:

    if isinstance(object, str):
        print(object, "is in the kitchen : <class 'str'>")
    elif object:
        obj_type = type(object)
        type_name = str(obj_type).split("'")[1]
        if isinstance(object, (int, float, bool, complex)):
            print("Type not found")
        else:
            print(type_name.capitalize(), ":", obj_type)
    else:
        print("Type not found")
    return 42
