from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
text = prompt.format(product="colorful socks")

llm = OpenAI()

print(llm.invoke(text))

