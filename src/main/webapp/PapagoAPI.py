import ssl
import urllib.parse
import urllib.request
import json

url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"

context = ssl._create_unverified_context()

client_id = "ytzb1tfff5"
client_secret = "FBy8BwDwoL6zlhTB4b8afzrRRwDfbanWYeG4utKw"

def translate(text="", source="en", target="ko"):
    data = "source=%s&target=%s&text=%s" % (source, target, text)
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    request.add_header("X-NCP-APIGW-API-KEY", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"), context=context)
    response_body = response.read()
    result_json = json.loads(response_body.decode("utf-8"))
    translated_text = result_json['message']['result']['translatedText']
    return translated_text