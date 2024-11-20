from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai
from pdf2image import convert_from_bytes

# Configure Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to process the PDF
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            # Specify the path to Poppler if it's not in the system PATH
            poppler_path = r"C:\Users\shalu\ATS Screening system\poppler-24.08.0\Library\bin"  # Update this path as per your Poppler installation
            
            # Convert the PDF to images
            images = pdf2image.convert_from_bytes(
                uploaded_file.read(),
                poppler_path=poppler_path  # Provide poppler_path explicitly
            )
            
            # Get the first page as an image
            first_page = images[0]
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            # Prepare base64-encoded image for API
            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()
                }
            ]
            return pdf_parts
        
        except FileNotFoundError:
            st.error("Poppler is not installed or the path is incorrect. Please check the setup.")
            return None
        except Exception as e:
            st.error(f"An error occurred while processing the PDF: {str(e)}")
            return None
    else:
        raise FileNotFoundError("No file uploaded")

# Function to interact with Generative AI
def get_gemini_response(input_text, pdf_content, prompt):
    # Use the updated model name
    model_name = 'gemini-1.5-flash'  # Updated to the newer model
    
    try:
        # Generate the response using the updated model
        model = genai.GenerativeModel(model_name)
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        # Handle errors gracefully
        st.error(f"An error occurred while generating a response: {str(e)}")
        return None


# Streamlit app configuration
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# Input fields
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

# Buttons
submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("Percentage Match")

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
Your task is to evaluate the resume against the provided job description. Give me the percentage match if the resume matches
the job description. First, the output should come as a percentage, followed by keywords missing, and finally, overall thoughts.
"""

# Button actions
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content is not None:
            response = get_gemini_response(input_text, pdf_content, input_prompt1)
            st.subheader("The Response is:")
            st.write(response)
    else:
        st.error("Please upload the resume.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content is not None:
            response = get_gemini_response(input_text, pdf_content, input_prompt2)
            st.subheader("The Response is:")
            st.write(response)
    else:
        st.error("Please upload the resume.")
