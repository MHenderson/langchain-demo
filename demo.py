from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.schema import HumanMessage

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

llm = OpenAI()
chat_model = ChatOpenAI()

print(llm.invoke(text))

print(chat_model.invoke(messages))
