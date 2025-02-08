### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
st.set_page_config(page_title="Nutritional Assistant App")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
st.sidebar.image("law.jpg", width=150)
st.sidebar.subheader(" Nana Owusu Aduomi")
st.sidebar.subheader("Email: lawrenceowusu0541@gmail.com")
st.sidebar.subheader("ML and MLOps Engineer, GenAI engineer, Data Scientist, Data Engineer, DevOps Engineer")
st.sidebar.subheader("Credentials: BSc, M.S., M.S., PhD candiate, 6X AWS certifiedd, Certified Spark Developer, Certified Terraform Associate, Certifird ScrumMaster, SQL Developer.")
st.sidebar.subheader("Technical Skills: Python programming, FastAPI, Spark, Airflow, Kubernetes, Docker, Git, AWS, Streamlit, Jenkins")
st.sidebar.link_button("Link to Publication", "https://doi.org/10.5815/ijisa.2024.05.05")
st.title("Nutritional Assistance Chatbot")
st.markdown("""The Nutritional Assistance Chatbot is an AI-powered tool designed to analyze food content from uploaded images and provide insights into its nutritional value. 
The chatbot leverages the reasoning capabilities of LLMs to identify food items, estimate portion sizes, and assess macronutrient and micronutrient composition.
By evaluating food images, the chatbot helps users make informed dietary choices, track calorie intake, and maintain balanced nutrition. 
It can also provide tailored recommendations based on dietary goals, health conditions, or specific nutritional needs. This technology is particularly beneficial for individuals monitoring their diet, healthcare professionals, and organizations promoting nutrition awareness.""")
st.subheader('Profile of the Developer')
st.markdown("""I am a Machine Learning consultant with three years of experience in building production-grade ML, Deep Learning, and Generative AI applications. 
I specialize in configuring Virtual Private Clouds (VPCs), provisioning cloud infrastructure with Terraform, containerizing ML applications, and orchestrating their deployment and scaling in Kubernetes environments.
Additionally, I have expertise in configuring and automating end-to-end machine learning workflows. I am proficient in Python, Terraform, Kubernetes, Apache Spark, Solidity, Git, and Jenkins. My research interests include adversarial machine learning, privacy-preserving algorithms, and data security""")
st.divider()

## Function to load Google Gemini Pro Vision API And get response
#st.header("Nutritional Assistant Chatbot")
name = st.text_input("What is your you name ?")
if name:
    input=st.text(f"Welcome {name}, I am your nutritional assistant and happy to help you improve your diet.  Take a high-resolution photo of your food and upload it using the 'Browse Files' button below to receive the best advice from me. I will then leverage my human-like reasoning capabilities to assess the nutritional value of your food and provide tailored recommendations")
      

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

input=st.text_input("How may I help you today?",key="input")


#input=st.text_input("I am a nutritional assistant. I help users to improve their diet. How may I help you today ?",key="input")
uploaded_file = st.file_uploader("Upload the photo of your food", type=["jpg", "jpeg", "png","jfif"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit=st.button("Please, click here for response")

input_prompt="""
You are an expert nutritionist. First welcome the user. 
You should analyze its components to identify the ingredients, assess their nutritional value, and determine whether the meal is healthy or not . 
Using advanced food recognition and nutritional analysis, provide insights into the macronutrients, micronutrients, and overall balance of your meal. 
Also, offer recommendations on how to improve the nutritional quality of your food, suggest healthier alternatives if needed, and highlight potential health impacts based on your meal’s composition. 
               1. Item 1 - Impact on human health
               2. Item 2 - Impact on human health
               ----
               ----


"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    #st.subheader("The Response is")
    st.write(response)

