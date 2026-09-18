import os
import sys


from agents.data_agent import data_agent
from langchain_core.messages import HumanMessage
from utils.llm_pick import pick_llm
from dotenv import load_dotenv  

if __name__ == "__main__":

    data_agent_root = os.path.abspath(os.path.dirname(__file__))
    input_file_path = os.path.join(data_agent_root, "data", "extract", "extracted_data.csv")
    output_folder = os.path.join(data_agent_root, "data", "transform")

    response = data_agent.invoke(
        {"messages": [HumanMessage(content=f"""
         I want to transform the data stored in the '{input_file_path}' file
         and save the transformed data in the '{output_folder}' folder in the csv format.
        The transformation should filter the data to show bulbasaur pokemon only.
     """)],
         "route_response": ""}
    )

    print(response)