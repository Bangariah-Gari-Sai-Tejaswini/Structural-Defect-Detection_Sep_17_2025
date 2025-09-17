import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

#configure the model
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

#upload and show image
st.sidebar.title('UPLOAD YOUR IMAGE HERE')
uploaded_image = st.sidebar.file_uploader('Here',type=['jpeg','jpg','png'])
if uploaded_image:
    image = Image.open(uploaded_image)
    st.sidebar.subheader(':blue[UPLOADED IMAGE]')
    st.sidebar.image(image)

#create main page
st.title(':red[STRUCTURAL DEFECTS : :green[AI assisted structure defect ' \
'identifier in construction business]]')

tips = '''To use the application follow the steps below:
* Upload the image
* Click on the button to generate summary
* Click download to save the report generated'''
st.write(tips)

rep_title = st.text_input('Report Title : ',None)
prep_by = st.text_input('Report Prepared by : ',None)
prep_for = st.text_input('Report Prepared for : ',None)

import datetime as dt

today = dt.datetime.now().strftime("%B %d, %Y")

prompt = f"""
You are a highly experienced structural engineer. The user has uploaded an image of a structure.  
Analyze the image for structural defects and prepare a professional assessment report.  

The report must start with the following details:

**Report Title**: {rep_title}  
**Prepared By**: {prep_by}  
**Prepared For**: {prep_for}  
**Date**: {today}  

---

### Report Requirements:

1. **Defect Identification**
   - Detect and classify all visible defects (e.g., cracks, spalling, corrosion, honeycombing, etc.).
   - If multiple defects are present, list them separately.

2. **Defect Analysis**
   - Severity of each defect (Low / Medium / High).  
   - Whether the defect is inevitable or avoidable.  
   - Estimated time before catastrophic failure if left untreated.  

3. **Repair & Mitigation**
   - Short-term solutions (cost in INR + estimated time).  
   - Long-term solutions (cost in INR + estimated time).  
   - Suggested precautions to prevent recurrence.  

4. **Report Style**
   - Use bullet points where possible.  
   - Use tables for comparison (e.g., severity, cost, time).  
   - Keep report length ≤ 3 pages.  
   - Write in **professional, concise language**.  
   - Format output so it can be easily exported into a Word document.  

---
"""

if st.button('Generate Report'):
    if uploaded_image is None:
        st.error('Please upload an image first')
    else:
        with st.spinner('Generating Report.....'):
            response = model.generate_content([prompt,image],generation_config=
                                              {'temperature':0.2})
            st.write(response.text)
            st.download_button('Download Report',
                      data = response.text,
                      file_name='structural_defect_report.txt',
                      mime='text/plain')

