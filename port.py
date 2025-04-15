import streamlit as st
from PIL import Image
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Abhishek Giri | Portfolio", layout="wide")

# --- LOAD PROFILE PIC ---
profile_pic = Image.open("me.jpg")  # Ensure 'profile.jpg' is in the same folder

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #f9f9f9, #eef2f3);
        }

        [data-testid="stSidebar"] {
            background-color: #f0f2f6;
            padding: 2rem 1rem;
            color: black !important;
        }

        [data-testid="stSidebar"] * {
            color: black !important;
            font-size: 16px !important;
        }

        .big-font {
            font-size: 2.4rem;
            font-weight: 700;
            color: #303952;
            animation: fadeInDown 1.5s ease;
        }

        .sub-font {
            font-size: 1.2rem;
            color: #576574;
            margin-top: -10px;
        }

        .section {
            animation: fadeInDown 1.3s ease;
            padding: 1rem 2rem;
            font-size: 19px;
            color: #2f3640;
            line-height: 1.7;
        }

        @keyframes fadeInDown {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .download-btn {
            background-color: #1e3799;
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }

        .download-btn:hover {
            background-color: #4a69bd;
        }

        .stTabs [role="tablist"] {
            justify-content: center;
        }

        h3 {
            font-size: 1.8rem;
            font-weight: 600;
            color: #222f3e;
            margin-bottom: 0.8rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image(profile_pic, width=150)
    st.markdown('<div class="big-font">Abhishek Giri</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-font">PEGA Certified Senior System Architect</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**Email:** abhishekgiri356@gmail.com")
    st.markdown("**Phone:** +91 8583906679")
    st.markdown("**LinkedIn:** [linkedin.com/in/abhishek-9iri](https://www.linkedin.com/in/abhishek-9iri/)")
    st.markdown("**Location:** India")
    st.markdown("---")
    st.markdown("*“Career, growth, and learning are my biggest motivators.”*")
    st.markdown("---")

    # Download Resume Button
    with open("FINAL Abhishek_Giri_Resume.pdf", "rb") as f:
        resume_data = f.read()
    b64_resume = base64.b64encode(resume_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64_resume}" download="Abhishek_Giri_Resume.pdf" class="download-btn">Download Resume</a>'
    st.markdown(href, unsafe_allow_html=True)

# --- MAIN TABS ---
tabs = st.tabs([
    "Summary", "Education", "Experience",
    "Projects", "Certifications", "Achievements", "Hobbies"
])

# --- TAB CONTENT ---
with tabs[0]:
    st.markdown('<h3>Professional Summary</h3>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    PEGA Developer with 9+ years of experience in full-cycle development, debugging, deployment, and agile teamwork. Proven track record in designing scalable, maintainable systems while mentoring junior devs and managing client interactions.

    Key areas of expertise include:
    - Advanced PEGA 7.x and 8.x frameworks
    - Case lifecycle management and REST APIs
    - Agile/Scrum methodology with onsite delivery experience
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<h3>Education</h3>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    - Bachelor of Computer Applications (BCA), Narula Institute of Technology — 2015
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<h3>Work Experience</h3>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    jobs = {
        "Tavant Technologies (Sep 2023 – Present)": "Associate Technical Architect",
        "ATIT, Saudi Arabia (Mar 2022 – Sep 2023)": "PEGA Senior Developer",
        "Capgemini Dubai (Dec 2020 – Mar 2022)": "PEGA Developer",
        "Capgemini India (Jun 2019 – Nov 2020)": "Associate Consultant",
        "Cognizant India (Jul 2015 – Jun 2019)": "Programmer Analyst"
    }
    for company, role in jobs.items():
        st.markdown(f"**{role}**  \n{company}")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<h3>Highlighted Projects</h3>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    - **Booking.com** – Insurance claims automation for car rentals using PEGA 8.4 & 8.21  
    - **Taqadhi (Ministry of Justice)** – Court case notifications system in Saudi Arabia  
    - **Abu Dhabi Executive Office** – Strategic policy execution platform  
    - **TNB (Malaysia)** – Power sector service & billing optimization via PEGA  
    - **Royal Bank of Canada** – Migrated 10 legacy PEGA apps to modern platform  
    - **CITI (STaRS)** – Banking automation platform for customer interactions  
    - **HealthNet** – Insurance claim management & automation in healthcare
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<h3>Certifications</h3>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    - PEGA Certified Senior System Architect – PRPC v8  
    - PEGA Certified System Architect – PRPC v7.1
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[5]:
    st.markdown('<h3>Achievements</h3>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    - Promoted to Senior Architect for delivering high-impact PEGA applications  
    - Successfully led cross-country client delivery in Abu Dhabi  
    - Consistently mentored and coached junior team members  
    - Delivered critical projects under strict timelines and complex scope
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[6]:
    st.markdown('<h3>Hobbies & Interests</h3>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.write("""
    Passionate about:
    - Exploring new technologies & automation tools  
    - Reading tech blogs and industry case studies  
    - Gaming and interactive storytelling  
    - Traveling and learning from global experiences
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""<hr style='margin-top: 3rem;'>
<small style='color:gray'>© 2025 Abhishek Giri. Built with ❤️ using Streamlit.</small>
""", unsafe_allow_html=True)
