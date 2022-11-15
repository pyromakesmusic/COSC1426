import json

personal_info = {
    "firstname" : "Tayo",
    "lastname" : "Castro",
    "age" : 27,
    "favcolor" : "black"
}

def main():
    print("Name: ", personal_info["firstname"], personal_info["lastname"])
    print("Phone Number: ", end="")
    if "phone_number" in personal_info:
        print(personal_info["phone_number"])
    else:
        print("REDACTED")

    personal_info["favorite food"] = "beef"
    print("Favorite Food: ", personal_info["favorite food"])
    personal_info["favcolor"] = "charcoal"

    del personal_info["age"]

    for key in personal_info:
        print(key, end=": ")
        print(personal_info[key])

    print(personal_info.get("firstname", "not tracked"))
    print(personal_info.get("height", "not tracked"))
    for key in personal_info:
        key = key.upper()

    for key in personal_info:
        personal_info[key] = personal_info[key].upper()

    print(json.dumps(personal_info))
    return

main()