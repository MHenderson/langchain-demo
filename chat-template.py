from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

messages = chat_prompt.format_messages(input_language="English", output_language="Korean", text="I love programming.")

chat_model = ChatOpenAI()

print(chat_model.invoke(messages))
