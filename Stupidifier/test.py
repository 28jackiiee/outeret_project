import openai

openai.api_key = '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'
model_id = 'gpt-4'
def gpt_function(prompt):
    conversation =[]
    prompt = "Can you turn this sentence into adult humor:" + prompt
    conversation.append({'role': 'user', 'content': prompt})
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    return response.choices[0].message["content"]
    
print(gpt_function(input()))