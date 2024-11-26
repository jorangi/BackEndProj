import ssl
import urllib.parse
import urllib.request
import json

url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"

context = ssl._create_unverified_context()

client_id = "ytzb1tfff5"
client_secret = "FBy8BwDwoL6zlhTB4b8afzrRRwDfbanWYeG4utKw"
source_language = "en"
target_language = "ko"
source_text = "I think it''s a career peak for [Bong Joon-ho]."

encText = urllib.parse.quote(source_text)

data = "source=%s&target=%s&text=%s" % (source_language, target_language, encText)
request = urllib.request.Request(url)
request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
request.add_header("X-NCP-APIGW-API-KEY", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"), context=context)
rescode = response.getcode()

response_body = response.read()
result_json = json.loads(response_body.decode("utf-8"))
translated_text = result_json['message']['result']['translatedText']

print(translated_text)