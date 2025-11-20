import streamlit as st
from PIL import Image
import base64
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Page Config
st.set_page_config(
    page_title="Yash Jain | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Top Navigation
st.markdown("""
<div class="nav-bar">
    <a href="#home">Home</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#deployed-work">Deployed Work</a>
    <a href="#skills">Skills</a>
    <a href="#certifications">Certifications</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# Main Content

# Hero Section
st.markdown('<a id="home"></a>', unsafe_allow_html=True)
col1, col2 = st.columns([1.5, 1])

with col1:
    st.title("Yash Jain")
    st.markdown("### Computer Science Graduate & Data Enthusiast")
    
    st.markdown("""
    Dynamic and passionate Computer Science graduate with a strong foundation in **Software Development, Machine Learning, Deep Learning, GenAI, and Data Engineering**. 
    
    I have experience designing high-quality, efficient, and scalable software solutions in fast-paced environments. Proficient in **Python, C++, SQL, Java, and Cloud Technologies**, with hands-on experience in distributed systems and automated testing workflows.
    """)
    
    st.markdown("""
    <div class="social-links" style="text-align: left; margin-bottom: 20px;">
        <a href="https://linkedin.com/in/yashjhota" target="_blank">LinkedIn</a>
        <a href="https://github.com/yashjhota" target="_blank">GitHub</a>
        <a href="mailto:jhotayash@zohomail.in">Email</a>
    </div>
    """, unsafe_allow_html=True)

    st.download_button(
        label="📄 Download Resume",
        data=open("YASH_JAIN_RESUME.pdf", "rb").read(),
        file_name="YASH_JAIN_RESUME.pdf",
        mime="application/pdf"
    )

with col2:
    # Display profile photo in a circular shape or styled frame
    col2_1, col2_2, col2_3 = st.columns([1, 2, 1])
    with col2_2:
        st.image("profile_photo.png", width=300)

st.markdown("---")

# Education Section
st.header("🎓 Education")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="stCard">
        <h3>Bachelor of Technology in Computer Science</h3>
        <p style="color: #ffffff;">Jain University, Bangalore</p>
        <p style="color: #FFD700;">Sep 2022 - Present</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stCard">
        <h3>Higher Secondary in Computer Science</h3>
        <p style="color: #ffffff;">Guhan School, Madurai</p>
        <p style="color: #FFD700;">Apr 2021 - May 2022</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Experience Section
st.markdown('<a id="experience"></a>', unsafe_allow_html=True)
st.header("💼 Professional Experience")

st.markdown("""
<div class="timeline-item">
    <h3>Data Analyst Intern</h3>
    <p style="color: #FFD700;">UptoSkills | Remote | Jan 2025 - April 2025</p>
    <ul>
        <li style="color: #ffffff;">Analyzing large datasets using SQL, Pandas, and Power BI, uncovering insights that improved business decisions.</li>
        <li style="color: #ffffff;">Built interactive dashboards that enhanced reporting efficiency by 25%.</li>
        <li style="color: #ffffff;">Conducted predictive analysis to forecast trends, leveraging machine learning models.</li>
    </ul>
</div>

<div class="timeline-item">
    <h3>SQL Intern</h3>
    <p style="color: #FFD700;">HubbleMind Pvt Ltd | Remote | Oct 2024 - Nov 2024</p>
    <ul>
        <li style="color: #ffffff;">Developed optimized SQL queries, reducing execution time by 20%, improving database efficiency.</li>
        <li style="color: #ffffff;">Designed and integrated data pipelines for interactive Power BI dashboards, aiding decision-making.</li>
        <li style="color: #ffffff;">Automated ETL workflows, increasing data processing efficiency by 15%.</li>
        <li style="color: #ffffff;">Applied data warehousing techniques, ensuring smooth and scalable data retrieval.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Projects Section
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.header("🚀 Featured Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="stCard">
        <h3>💬 Poof40 - Real-Time Vanishing Chat App</h3>
        <p style="color: #ffffff;">Designed a self-expiring chat system using AI-assisted development and prompt engineering.</p>
        <p style="color: #ffffff;"><strong>Tech Stack:</strong> Supabase Realtime API, PostgreSQL, Netlify</p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="stCard">
        <h3>🧠 BrainScanNet: Brain Tumor Classification</h3>
        <p style="color: #ffffff;">Brain tumor detection system using EfficientNetB2 and custom MRI preprocessing, achieving 99.84% accuracy.</p>
        <p style="color: #ffffff;"><strong>Tech Stack:</strong> Deep Learning, EfficientNetB2, Grad-CAM</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stCard">
        <h3>👤 FRAS: Identity Verification System</h3>
        <p style="color: #ffffff;">Face recognition system that reduced manual attendance efforts by 80% with 95% accuracy.</p>
        <p style="color: #ffffff;"><strong>Tech Stack:</strong> Face Recognition, LBP, PCA, Excel Integration</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Deployed Work Section
st.markdown('<a id="deployed-work"></a>', unsafe_allow_html=True)
st.header("🌐 Deployed Work")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="stCard">
        <h3>💎 QJ Jewels</h3>
        <p style="color: #ffffff;">Jewelry showcase platform.</p>
        <a href="https://qj-jewels.lovable.app/" target="_blank" style="color: #FFD700; text-decoration: none;"><strong>Visit Site ↗</strong></a>
    </div>
    <br>
    <div class="stCard">
        <h3>🤖 AI Chatbot</h3>
        <p style="color: #ffffff;">Interactive AI conversational assistant.</p>
        <a href="https://chatbotyash.streamlit.app/" target="_blank" style="color: #FFD700; text-decoration: none;"><strong>Visit Site ↗</strong></a>
    </div>
    <br>
    <div class="stCard">
        <h3>💰 Jhota Budget Tracker</h3>
        <p style="color: #ffffff;">Personal finance and budget tracking tool.</p>
        <a href="https://jhotabudgettracker.streamlit.app/" target="_blank" style="color: #FFD700; text-decoration: none;"><strong>Visit Site ↗</strong></a>
    </div>
    <br>
    <div class="stCard">
        <h3>❤️ Love Invoice</h3>
        <p style="color: #ffffff;">Fun invoice generator for couples.</p>
        <a href="https://jhota-love-invoice.lovable.app/" target="_blank" style="color: #FFD700; text-decoration: none;"><strong>Visit Site ↗</strong></a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stCard">
        <h3>📊 Text Sentiment Analyzer</h3>
        <p style="color: #ffffff;">Analyze text sentiment using NLP.</p>
        <a href="https://text-sentimentanalyzer.streamlit.app/" target="_blank" style="color: #FFD700; text-decoration: none;"><strong>Visit Site ↗</strong></a>
    </div>
    <br>
    <div class="stCard">
        <h3>🏢 Rishabh Enterprises</h3>
        <p style="color: #ffffff;">Business portfolio website.</p>
        <a href="https://rishabhenterprises.netlify.app/" target="_blank" style="color: #FFD700; text-decoration: none;"><strong>Visit Site ↗</strong></a>
    </div>
    <br>
    <div class="stCard">
        <h3>🌐 SAJSV</h3>
        <p style="color: #ffffff;">Web application for SAJSV.</p>
        <a href="https://sajsv.lovable.app" target="_blank" style="color: #FFD700; text-decoration: none;"><strong>Visit Site ↗</strong></a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Skills Section
st.markdown('<a id="skills"></a>', unsafe_allow_html=True)
st.header("🛠 Technical Skills")

skills = [
    "Python", "Java", "C++", "SQL", "Bash",
    "VS Code", "Eclipse", "GCP", "PowerBI", "MongoDB", "MySQL",
    "Linux", "GitHub", "LangChain", "HuggingFace", "FastAPI", "Gen-AI","LangGraph"
]

skill_html = ""
for skill in skills:
    skill_html += f'<span class="skill-tag">{skill}</span>'

st.markdown(f"""
<div style="margin-top: 20px; text-align: center;">
    {skill_html}
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Certifications & Publications
col1, col2 = st.columns(2)

with col1:
    st.markdown('<a id="certifications"></a>', unsafe_allow_html=True)
    st.header("📜 Certifications")
    st.markdown("""
    <div class="stCard">
        <ul style="list-style-type: none; padding-left: 0;">
            <li style="margin-bottom: 10px;color:#ffffff;">🏆 <strong>Oracle Cloud Infrastructure 2025 Certified Data Science Professional</strong> (Oct 2025)</li>
            <li style="margin-bottom: 10px;color:#ffffff;">🏆 <strong>Oracle Cloud Infrastructure 2025 Certified Generative AI Professional</strong> (Aug 2025)</li>
            <li style="margin-bottom: 10px;color:#ffffff;">🏆 <strong>Ubuntu Linux Professional Certificate</strong> by Canonical (March 2025)</li>
            <li style="margin-bottom: 10px;color:#ffffff;">🏆 <strong>Google Data Analytics Professional Certificate</strong> (Feb 2025)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<a id="publications"></a>', unsafe_allow_html=True)
    st.header("� Publications")
    st.markdown("""
    <div class="stCard">
        <ul style="list-style-type: none; padding-left: 0;">
            <li style="margin-bottom: 10px;">📄 <a href="https://ieeexplore.ieee.org/document/11188200" target="_blank" style="color: #ffffff; text-decoration: none;"><strong>Deep Learning in Ophthalmology: A Novel Approach for Retinal Condition Prediction</strong></a> (2025)</li>
            <li style="margin-bottom: 10px;">📄 <a href="https://ieeexplore.ieee.org/document/11188339" target="_blank" style="color: #ffffff; text-decoration: none;"><strong>A Predictive Analysis of Increasing IDSystem Accuracy Using ML Algorithms</strong></a> (2025)</li>
            <li style="margin-bottom: 10px;">📄 <a href="https://ieeexplore.ieee.org/document/11188325" target="_blank" style="color: #ffffff; text-decoration: none;"><strong>Advancing IDS: A Comparative Analysis of Algorithms on the Kyoto 2015 Benchmark Dataset</strong></a> (2025)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("---")

# Contact Section
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("📬 Get In Touch")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color: #111; padding: 20px; border-radius: 10px; border: 1px solid #333;">
        <h3>Let's Connect!</h3>
        <p style="color: #ffffff;">Interested in collaborating or have a project in mind? Feel free to reach out!</p>
        <br>
        <p style="color: #ffffff;">📧 <strong>Email:</strong> <a href="mailto:jhotayash@zohomail.in" style="color: #FFD700;">jhotayash@zohomail.in</a></p>
        <p style="color: #ffffff;">📱 <strong>Phone:</strong> +91 7339615381</p>
        <p style="color: #ffffff;">📍 <strong>Location:</strong> Bangalore, Karnataka</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize Google Sheets Connection
@st.cache_resource
def init_google_sheet():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds_dict = st.secrets["gcp_service_account"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        return client.open("project").sheet1
    except Exception as e:
        return None

sheet = init_google_sheet()

with col2:
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            if not name or not email or not message:
                st.warning("Please fill in all fields.")
            elif sheet is None:
                st.error("Google Sheets connection not configured. Please check your secrets and ensure a sheet named 'project' exists.")
            else:
                try:
                    sheet.append_row([name, email, message])
                    st.success("Thanks for reaching out! Your message have been sent to Jain ❤️.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
