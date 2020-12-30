from google.cloud import language_v1

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/gkukal/Documents/JGAryaman/GoogleAPIKey/NLPForHacks-b2a763718dea.json"

from google.cloud import language_v1

def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})

    for entity in response.entities:
        return format(entity.name)


sample_analyze_entities("The Oxford-AstraZeneca vaccine has been approved for use in the UK, with the first doses due to be given on Monday.There will be 530,000 doses available from next week, and vaccination "
                        "centres will now start inviting patients to come and get the jab. "
                        "Priority groups for immunisation have already been identified, "
                        "starting with care home residents, the over-80s, and health and care workers.")