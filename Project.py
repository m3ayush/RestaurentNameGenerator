import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
API_KEY = os.getenv("API_KEY")

os.environ['GROQ_API_KEY']= API_KEY
 
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.6)  #0=safe 1=creative 
#name=llm.invoke("I want to open restaurent for Italian food. Suggest just one fancy name for this. Only name no discription nothing just name")
#print(name)



def generated(cuisine):
    prompt_template_name= PromptTemplate(
    input_variables=['cuisine'],
    template= "I want to open restaurent for {cuisine} food. Suggest just one fancy name for this. Only name no discription nothing just name"
    )

    prompt=prompt_template_name.format(cuisine=cuisine)
    #print(prompt)

    response = llm.invoke(prompt)

    return response

if __name__=="__main__":
    print(generated("Italian"))