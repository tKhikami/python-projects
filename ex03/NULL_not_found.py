def NULL_not_found(object: any) -> int:
    if object in [None, 0, False, ""] or object != object:
        print(f"{type(object).__name__}: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1