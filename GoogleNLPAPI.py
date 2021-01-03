from google.cloud import language_v1

import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/gkukal/PycharmProjects/HackTheLib/googleNLPAPIcodes.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "googleNLPAPIcodes.json"


def sample_analyze_entities(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_entities(
        request={'document': document, 'encoding_type': encoding_type})

    entitiesDict = {}
    for entity in response.entities:
        entitiesDict[entity.name] = entity.type_.name

    people = []
    placesOrOrganizations = []
    other = []

    for entity in entitiesDict.items():
        if entity[1] == "PERSON" or entity[1] == "PROPER":
            people.append(entity[0])
        elif entity[1] == "LOCATION" or entity[1] == "ORGANIZATION":
            placesOrOrganizations.append(entity[0])
        else:
            other.append(entity[0])

    people5 = []
    placesOrOrganizations5 = []
    other5 = []
    for x in people[:5]:
        people5.append(x)
    for y in placesOrOrganizations[:5]:
        placesOrOrganizations5.append(y)
    for z in other[:5]:
        other5.append(z)

    peoplePlacesOrganOther = {
        "people": people5, "placesOrOrganizations": placesOrOrganizations5, "other": other5}

    return peoplePlacesOrganOther
