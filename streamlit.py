import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain
from src.mcqgenerator.utils import read_file,get_table_quiz
from src.mcqgenerator.logging import logging
import streamlit as st

#Loading json response file template input for ouput format

with open("response.json",'r') as file:
    RESPONSE_JSON=json.load(file)
    
st.title("MCQ Creator Application using Google AI and Langchain   🤖 ")

with st.form("user_iputs"):
    #file upload
    uploaded_file=st.file_uploader("Upload a td or txt file")
    
    #input field
    number=st.number_input("No of MCQs to create",min_value=3,max_value=50)
    subject=st.text_input("Insert Subject")
    tone=st.text_input("Complexity level of Quetsions",max_chars=20,placeholder="simple")
    
    #Add submit button
    button=st.form_submit_button("Create MCQs")
    
    #Check if the button is clicked and all fileds are input
    
    if button and uploaded_file is not None and number and subject and tone:
        with st.spinner("loading...."):
            try:
                text=read_file(uploaded_file)
                response=generate_evaluate_chain(
                    {
                        "text": text,
                        "number": number,
                        "subject":subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                    )
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")
                
            else:
                if isinstance(response,dict):
                    quiz=response.get("quiz",None)
                    if quiz is not None:
                        quiz=quiz.replace('```json\n', '').replace('```', '')
                        table_data=get_table_quiz(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            #Display the review in a text box as well
                            st.text_area(label="Review",value=response["review"])
                        else:
                            st.error("Error in the table data")
                else:
                    st.write(response)
                    
                                    
                
            
  
  
  
  
  
    
#"text", "number", "subject", "tone", "response_json"  


    