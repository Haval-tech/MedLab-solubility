import streamlit as st
import smtplib
from email.mime.text import MIMEText

def home_page():
    st.title('MedLab Project')

    st.subheader("MedLab")
    st.write("**The next era of drug discovery starts here.**")

    st.write("""
    At MedLab, we’re building AI to revolutionize drug discovery, making the process faster, smarter, and more efficient.
    Our first mission is clear: create a powerful predictive model that estimates essential drug properties, allowing researchers to identify promising compounds long before they reach the lab.
    This means faster breakthroughs, reduced costs, and a fundamentally new way to accelerate discovery.
    """)

    st.subheader("Why This Matters")
    st.write("""
    MedLab speeds up drug discovery by simulating key drug properties, enabling us to filter out weak candidates and focus on those with real promise.
    Beyond research, It’s also a valuable learning tool, giving students practical experience with AI in pharmacy and medicine.
    MedLab isn’t just a project; it’s a revolution in the drug discovery process.
    """)

    st.write("**Join us in shaping the future.**")
    st.write("_Haval, MPharm Student, UEA, Norwich, UK_")

    st.markdown("<p style='color:#f5f5dc; font-weight:bold; margin-top:20px;'>If you’re interested, Please fill out the form below to contribute, collaborate, or stay updated.</p>", unsafe_allow_html=True)

    with st.form("collaboration_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        academic_status = st.text_input("Your Academic Status (e.g., '3rd-year Pharmacy Student at UEA')")
        skills = st.text_area("Skill(s) (e.g., research, data analysis, drug formulation, etc.)")
        expected_skills = st.text_area("What skill(s) do you expect to achieve by collaborating on this project?")
        hours = st.slider("How many hours are you able to dedicate to this project per week?", 1, 10)
        submit_button = st.form_submit_button("Submit")

    def send_email(recipient_email, subject, body):
        sender_email = "halo.wigan@gmail.com"
        sender_password = "snod ncei ellk xxzb"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

    if submit_button:
        if full_name and email and academic_status and skills and expected_skills:
            st.success("Thank you for submitting your information, we'll be in touch soon via email.")
            
            email_subject = "Confirmation of Information Submission"
            email_body = f"Dear {full_name},\n\n" \
                         "Thank you for submitting your information to the MedLab Project: Collaboration Hub. " \
                         "We have received your details, and one of our team members will be in touch with you soon to discuss the next steps.\n\n" \
                         "Best regards,\n" \
                         "The MedLab Team"
            
            send_email(email, email_subject, email_body)
        else:
            st.error("Please complete all fields before submitting.")
