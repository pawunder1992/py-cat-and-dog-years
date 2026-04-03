def get_human_age(cat_age: int, dog_age: int) -> list:
    if (not isinstance(cat_age, (int, float))
            or not isinstance(dog_age, (int, float))):
        raise TypeError
    cat_age = int(cat_age)
    dog_age = int(dog_age)
    list_of_years = [15, 9, 4]
    result = [0, 0]
    for i in list_of_years:
        cat_age -= i
        if cat_age >= 0:
            result[0] += 1
        else:
            break
        while (cat_age >= 0) and i == list_of_years[2]:
            cat_age -= i
            if cat_age >= 0:
                result[0] += 1
    list_of_years[2] += 1
    for i in list_of_years:
        dog_age -= i
        if dog_age >= 0:
            result[1] += 1
        else:
            break
        while (dog_age >= 0) and i == list_of_years[2]:
            dog_age -= i
            if dog_age >= 0:
                result[1] += 1
    return result
