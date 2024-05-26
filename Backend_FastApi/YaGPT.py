import requests
# Яндекс GPT
def GPT(input_str, type):
  if type == 0:
    text = "Составь из этого текста только один вопрос для теста и только один развёрнутый ответ на него, вопрос и ответы раздели словом ответ: " + str(input_str)
  else:
    text = "Составь из этого текста только один вопрос для теста и несколько вариантов ответа на него, вопрос и ответы раздели словом ответ: " + str(input_str)
  prompt = {
      "modelUri": "gpt://b1g1o9j4lup4tvhfe5u6/yandexgpt-lite",
      "completionOptions": {
          "stream": False,
          "temperature": 0.4,
          "maxTokens": "8000"
      },
      "messages": [
          {
              "role": "user",
              "text": text
          }
      ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Api-Key AQVN36QRntV3Gys6tAvWaL1nEZeEYkCkW2hsYdqV"
  }

  response = requests.post(url, headers=headers, json=prompt)

  result = response.text
  #print(result)
  result = result.replace('{"result":{"alternatives":[{"message":{"role":"assistant","text":"','')

  result = result[:-147]#-156
  result = result.replace("{",'')
  result = result.replace('}','')
  result = result.replace('*','')
  result = result.replace('"','')
  result = result.replace('//','')
  result = result.replace('n','')
  result = result.replace("\\", "")

  return result
