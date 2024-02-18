import json
import os
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile

from dotenv import load_dotenv
load_dotenv()



if __name__ == '__main__':
    linkedin_data = scrape_linkedin_profile()
    #linkedin_data_str = json.dumps(linkedin_data, indent=4)
    # print(linkedin_data_str)
    print(os.getenv('OPENAI_API_KEY'))
    
    summary_template = """ 
    given the linked information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm =ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    response = chain.invoke(input={"information":linkedin_data})
    response_str = json.dumps(response["text"], indent=4)
    print(response_str)

