def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print("Nothing: None <class 'NoneType'>")
        elif isinstance(object, float) and object != object:
            print("Cheese: nan <class 'float'>")
        elif object is False and isinstance(object, bool):
            print("Fake: False <class 'bool'>")
        elif object == 0 and isinstance(object, int):
            print("Zero: 0 <class 'int'>")
        elif object == '' and isinstance(object, str):
            print("Empty: <class 'str'>")
        else:
            print("Type not Found")
            return 1
        return 0
    except Exception as e:
        print("Error: Unexpected issue occurred")
        return 1
