from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
openai_model = ChatOpenAI(model="gpt-4o")

from langchain_deepseek import ChatDeepSeek
deepseek_model = ChatDeepSeek(model="deepseek-chat", temperature=0.0, streaming=True)
