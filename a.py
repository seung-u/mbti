from openai import OpenAI

client = OpenAI(
  api_key= "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",
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "해당 질문과 답 데이터를 기반으로 사용자가 좋아할만한 음악 장르 1개만 말하고 다른 말을 하지 말아주세요."
    },
    {
      "role": "user",
      "content": "{'음악을 듣는 주된 목적이 무엇인가요': '집중하기 위해서', '음악을 들을때 가사와 멜로디 중 무엇을 더 중요하게 생각하는가': '가사를 중요하게 생각합니다', '여행을 갈 때 주로 어떤 음악을 듣는가': '흥겨운 음악을 듣는다.', '운동할 때 주로 어떤 스타일의 음악을 듣는가': '클래식을 듣는것을 좋아한다.', '친구들과 함께 있을 때 어떤 종류의 음악을 듣는 것을 좋아하는가': '나의 취향을 친구들과 공유한다.', '여유로운 시간에 음악을 들을 때 어떤 분위기를 선호하는가': '흥겨운 분위기의 음악을 듣는다.'}"
    }
  ],
  temperature=0,
  max_tokens=5,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response.choices[0].message.content)