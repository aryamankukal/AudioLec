from google.cloud import language_v1

import os
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/gkukal/PycharmProjects/HackTheLib/googleNLPAPIcodes.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "googleNLPAPIcodes.json"

def sample_analyze_entities(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})

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

    peoplePlacesOrganOther = {"people": people5, "placesOrOrganizations": placesOrOrganizations5, "other": other5}

    return peoplePlacesOrganOther

# print(sample_analyze_entities("USA TODAY is keeping track of the news surrounding COVID-19 as a pair of vaccines join the U.S. fight against a virus that has killed more than 348,000 Americans since the first reported fatality in February. Keep refreshing this page for the latest updates surrounding the coronavirus, including who is getting the vaccines from Pfizer and Moderna, as well as other top news from across the USA TODAY Network. Sign up for our Coronavirus Watch newsletter for updates directly to your inbox, join our Facebook group or scroll through our in-depth answers to reader questions for everything you need to know about the coronavirus. In the headlines: ► The Senate adjourned Friday night without securing $2,000 stimulus checks, leaving hopes for another round of payments in the hands of the next Congress. The homes of Senate Majority Leader Mitch McConnell and House Speaker Nancy Pelosi were vandalized over the weekend, with vandals leaving messages like wheres my money. Virginia state Sen. Ben Chafin Jr. died Friday after contracting the coronavirus, his office announced in a statement. Chafin, 60, was treated in Richmond at the VCU Medical Center for two weeks before his death. ► At least three U.S. states and 33 countries have identified a more contagious COVID-19 variant first identified in the United Kingdom. Several nations have also identified an additional variant, first identified in South Africa, that appears to infect people more easily. ► Hospitals struggling to provide enough oxygen for the sickest coronavirus patients in the Los Angeles area received some relief Saturday when U.S. Army Corps of Engineers crews arrived. California Gov. Gavin Newsom’s office says crews helped some aging hospitals update their oxygen delivery systems. California reported a record 585 coronavirus deaths Friday. ► Vaccine rollout in the U.S. is still ramping up, and just over four million people have received a first dose, according to the CDC. Chicago Mayor Lori Lightfoot said in a Twitter post Saturday that the city has distributed more than 95% of the vaccine doses it has received but at the current rate of dose allocation from the federal government, it would take 71 weeks – nearly one and a half years – to fully vaccinate the entire city. U.S. Sen. Mitt Romney, R-Utah, slammed the U.S. vaccine rollout in a statement Friday, saying the nation is falling behind and calling for urgent action to develop a comprehensive vaccination plan at the federal level. I know that when something isn’t working, you need to acknowledge reality and develop a plan, he said. ► Britain is allowing people to mix and match vaccines in certain circumstances, despite no evidence supporting the interchangeability of vaccines. In an update to their vaccination guidelines, health officials said another vaccine may be substituted if the original is not available or is unknown, particularly in situations where the person is at immediate high risk or is considered unlikely to attend again. India tested its COVID-19 vaccine delivery system Saturday with a nationwide trial, a day after authorizing the Oxford/AstraZeneca vaccine for emergency use. ► The World Health Organization authorized the vaccine by Pfizer/BioNTech for emergency use Thursday, making it easier for countries to expedite their own regulatory approval processes and allowing UNICEF and the Pan-American Health Organization to procure the vaccine. ► The Navajo Nation laid off more than 1,100 casino workers Friday because of prolonged closures caused by the coronavirus pandemic. The tribe operates four casinos in Arizona and New Mexico. The Nation’s vision took years to build but the Nation has been successful, Navajo Gaming Board Chairman Quincy Natay said. If it allows its gaming industry to fail, a permanent closure will cause a long-term setback for Navajo economic development, even if it eventually reopens. Todays numbers: The U.S. has more than 20 million confirmed coronavirus cases and 348,600 deaths, according to Johns Hopkins University data. The global totals: More than 84 million cases and 1.8 million deaths. What were reading: Teachers should be next COVID-19 vaccine schedule, CDC says. Can a shot reopen schools? Virginia state Sen. Ben Chafin Jr. dies after contracting COVID-19 State Sen. Ben Chafin Jr. died Friday after contracting the coronavirus, his office announced in a statement. State senator Augustus Denton (Ben) Chafin Jr., a native son of Russell County located in Southwest Virginia, passed away on January 1, 2021 from COVID-19 complications, the news release from his office stated. Chafin, 60, was treated in Richmond at the VCU Medical Center for two weeks before his death. A Republican, Chafin was elected to the Virginia House of Delegates in 2013 before being elected to the state senate the following year. Days before Chafin’s death, Rep.-elect Luke Letlow, R-La., 41, also died after contracting the virus. On Saturday, Pennsylvania state Rep. Mike Reese, 42, died following an apparent brain aneurysm, weeks after he announced that he had tested positive for COVID-19. – Sarah Elbeshbishi $2,000 checks? They will have to wait for new Congress The Senate on Friday did not take up whether to increase the $600 stimulus check payments that President Donald Trump demanded be raised to $2,000. Now, Congress will not reconvene until Sunday to end the 116th Congress. Democrats vowed to swiftly revive the $2,000 checks after the new Congress is sworn in Sunday. “President-elect Joe Biden has made clear that the pandemic relief bill that Congress passed is simply a down payment on the work that needs to continue,” said Rep. Hakeem Jeffries, D-N.Y., the chair of the House Democratic caucus. “We’re going to continue to fight for a $2,000 direct payment check.” Sen. Lindsey Graham, R-S.C., was the one of the few GOP senators pushing for a standalone vote on the $2,000 stimulus checks, saying that in the new Congress, you could get a vote."))

