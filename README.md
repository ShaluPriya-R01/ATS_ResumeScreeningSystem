# ATS Resume Expert

## Overview

**ATS Resume Expert** is a web application designed to analyze resumes (in PDF format) against job descriptions using advanced machine learning models. The app helps HR professionals and recruiters evaluate resumes for compatibility with job requirements, offering insights into strengths, weaknesses, percentage match, and keyword analysis.

The application leverages **Google's Gemini AI** for advanced generative responses and uses **Poppler** to process PDFs into images for AI model input.

---

## Features

- **Job Description Input**: Users can enter the job description for the role.
- **Resume Upload**: Users can upload a resume in PDF format.
- **AI Evaluation**: The app generates a professional evaluation of the resume against the job description using the **Gemini AI** model.
  - **Tell Me About the Resume**: Provides a review of the candidate’s strengths and weaknesses.
  - **Percentage Match**: Provides a match percentage based on the job description and identifies keywords that are missing in the resume.
  
---

## Requirements

- Python 3.10 or above
- **Streamlit** for web-based UI
- **Google Generative AI** SDK
- **Poppler** for PDF processing (necessary for `pdf2image` functionality)
- **Pillow** for image manipulation
- **Dotenv** for environment variable management

---

## Installation

### 1. **Set up the Virtual Environment**

Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. **Install Dependencies**

Use `pip` to install the required Python packages:

```bash
pip install -r requirements.txt
```

Here is a sample `requirements.txt`:

```
streamlit==1.16.0
google-generativeai==1.0.0
pdf2image==1.16.3
pillow==8.4.0
python-dotenv==0.20.0
```

### 3. **Install and Configure Poppler**

- **Download Poppler** from the [official repository](https://github.com/oschwartz10612/poppler-windows/releases/).
- Extract the files and ensure the `bin` folder (containing `pdfinfo.exe`) is available on your system.
- Add the `bin` folder to your system’s **PATH** environment variable.

Example Poppler installation path:
```
C:\poppler\bin
```

---

## Configuration

### 1. **API Key Setup**

To access **Google's Gemini AI**, you need to provide an API key. 

- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Enable the **Gemini API**.
- Create a service account and download the credentials.
- Add your API key to the `.env` file:

```plaintext
GOOGLE_API_KEY=your_api_key_here
```

### 2. **Environment Variables**

The app uses **dotenv** to load environment variables from a `.env` file. Ensure the `.env` file is in the root directory.

---

## Usage

1. **Launch the App**

Run the Streamlit app by executing the following command:

```bash
streamlit run app.py
```

2. **Interacting with the App**

- **Job Description**: Enter the job description in the provided text box.
- **Upload Resume**: Upload a PDF version of the resume.
- **Generate Evaluation**: Choose one of the options:
  - **Tell Me About the Resume**: View a professional evaluation of the resume.
  - **Percentage Match**: View the percentage match of the resume to the job description, along with missing keywords.

---

## Troubleshooting

### 1. **PDF Processing Error**  
If you encounter the error `Unable to get page count. Is poppler installed and in PATH?`:
- Ensure Poppler is installed correctly and the `bin` folder is added to the system’s **PATH**.
- Restart the system or IDE to apply changes.

### 2. **API Errors**
If you encounter issues related to **Gemini AI**:
- Make sure your API key is correctly set in the `.env` file.
- Ensure you’re using the correct model name (e.g., `gemini-1.5-flash`).

