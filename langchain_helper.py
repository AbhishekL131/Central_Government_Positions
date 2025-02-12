from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from secret_key import  gemini_api_key

import google.generativeai as genai

import os

os.environ["GOOGLE_API_KEY"] = gemini_api_key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.6)

def generate_response(position):
    prompt_template_position = PromptTemplate(
        input_variables=["position"],
        template="explain the responsibility of {position} in central government , answer pointwise "
    )

    pos_chain = LLMChain(llm = model,prompt = prompt_template_position)

    response = pos_chain({"position" : position})

    return response



