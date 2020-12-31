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
    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})

    for entity in response.entities:
        return format(entity.name)
