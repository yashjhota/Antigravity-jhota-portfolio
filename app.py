import streamlit as st
from PIL import Image
import base64
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import PyPDF2
from groq import Groq

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

# Projects Data
projects_data = [
    {
        "title": "💬 Poof40 - Real-Time Vanishing Chat App",
        "desc": "Designed a self-expiring chat system using AI-assisted development and prompt engineering.",
        "tech": "Supabase Realtime API, PostgreSQL, Netlify",
        "category": "Web Development",
        "type": "Featured",
        "link": None
    },
    {
        "title": "🧠 BrainScanNet: Brain Tumor Classification",
        "desc": "Brain tumor detection system using EfficientNetB2 and custom MRI preprocessing, achieving 99.84% accuracy.",
        "tech": "Deep Learning, EfficientNetB2, Grad-CAM",
        "category": "Machine Learning/AI",
        "type": "Featured",
        "link": None
    },
    {
        "title": "👤 FRAS: Identity Verification System",
        "desc": "Face recognition system that reduced manual attendance efforts by 80% with 95% accuracy.",
        "tech": "Face Recognition, LBP, PCA, Excel Integration",
        "category": "Machine Learning/AI",
        "type": "Featured",
        "link": None
    },
    {
        "title": "💎 QJ Jewels",
        "desc": "Jewelry showcase platform developed for a client solving their business problems.",
        "tech": "Web Development",
        "category": "Web Development",
        "type": "Deployed",
        "link": "https://qj-jewels.lovable.app/"
    },
    {
        "title": "🤖 AI Chatbot",
        "desc": "Interactive AI conversational assistant developed using groq api and streamlit.",
        "tech": "Streamlit, Groq API",
        "category": "Machine Learning/AI",
        "type": "Deployed",
        "link": "https://chatbotyash.streamlit.app/"
    },
    {
        "title": "💰 Jhota Budget Tracker",
        "desc": "Personal finance and budget tracking tool.",
        "tech": "Streamlit, Python",
        "category": "Web Development",
        "type": "Deployed",
        "link": "https://jhotabudgettracker.streamlit.app/"
    },
    {
        "title": "❤️ Love Invoice",
        "desc": "Fun invoice generator for a client solving their business problems.",
        "tech": "Web Development",
        "category": "Web Development",
        "type": "Deployed",
        "link": "https://jhota-love-invoice.lovable.app/"
    },
    {
        "title": "📊 Text Sentiment Analyzer",
        "desc": "Analyze text sentiment using NLP.",
        "tech": "NLP, Python, Streamlit",
        "category": "Machine Learning/AI",
        "type": "Deployed",
        "link": "https://text-sentimentanalyzer.streamlit.app/"
    },
    {
        "title": "🏢 Rishabh Enterprises",
        "desc": "Business portfolio website developed for a client solving their business problems and showcasing their products.",
        "tech": "Web Development",
        "category": "Web Development",
        "type": "Deployed",
        "link": "https://rishabhenterprises.netlify.app/"
    },
    {
        "title": "🌐 SAJSV",
        "desc": "Web application for Sri Adinath Jain Sanskar Vatika Madurai.",
        "tech": "Web Development",
        "category": "Web Development",
        "type": "Deployed",
        "link": "https://sajsv.lovable.app"
    }
]

# Projects Section
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.header("🚀 Projects")

# Filter UI
filter_col1, filter_col2 = st.columns([1, 3])
with filter_col1:
    category_filter = st.radio(
        "**Filter by Category:**",
        ["All", "Web Development", "Machine Learning/AI"],
        index=0
    )

# Filter Logic
filtered_projects = projects_data if category_filter == "All" else [p for p in projects_data if p['category'] == category_filter]

featured_projects = [p for p in filtered_projects if p['type'] == 'Featured']
deployed_projects = [p for p in filtered_projects if p['type'] == 'Deployed']

def render_project_card(project):
    link_html = f'<a href="{project["link"]}" target="_blank" style="color: #FFD700; text-decoration: none;"><strong>Visit Site ↗</strong></a>' if project["link"] else ""
    tech_html = f'<p style="color: #ffffff;"><strong>Tech Stack:</strong> {project["tech"]}</p>' if project["tech"] else ""
    
    st.markdown(f"""
    <div class="stCard" style="height: 100%; min-height: 250px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
            <h3>{project["title"]}</h3>
            <p style="color: #ffffff;">{project["desc"]}</p>
            {tech_html}
        </div>
        <div style="margin-top: 10px;">
            {link_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Render Featured
if featured_projects:
    st.subheader("Featured Projects")
    for i in range(0, len(featured_projects), 2):
        col1, col2 = st.columns(2)
        with col1:
            render_project_card(featured_projects[i])
        if i + 1 < len(featured_projects):
            with col2:
                render_project_card(featured_projects[i+1])
    st.markdown("<br>", unsafe_allow_html=True)

# Render Deployed
if deployed_projects:
    st.markdown('<a id="deployed-work"></a>', unsafe_allow_html=True)
    st.subheader("Deployed Work")
    for i in range(0, len(deployed_projects), 2):
        col1, col2 = st.columns(2)
        with col1:
            render_project_card(deployed_projects[i])
        if i + 1 < len(deployed_projects):
            with col2:
                render_project_card(deployed_projects[i+1])

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


col1, col2 = st.columns([1, 1])

with col1:
    # Radar Chart Data
    categories = ['Python', 'SQL', 'Machine Learning', 'Data Engineering', 'Web Dev', 'Cloud (GCP/OCI)']
    values = [95, 90, 85, 80, 75, 70]

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Yash Jain',
        line_color='#FFD700',
        fillcolor='rgba(255, 215, 0, 0.2)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(color='gray'),
                gridcolor='#333'
            ),
            angularaxis=dict(
                tickfont=dict(color='#ffffff', size=12),
                rotation=90
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        margin=dict(l=40, r=40, t=20, b=20),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("### ⚡ Proficiency Breakdown")
    st.markdown("""
    My technical expertise spans across **Data Science, Full Stack Development, and Cloud Computing**.
    
    - **Python & SQL**: My strongest suits, used daily for data analysis and backend logic.
    - **Machine Learning**: Extensive experience building and deploying models (EfficientNet, NLP).
    - **Data Engineering**: Proficient in building ETL pipelines and warehousing solutions.
    - **Cloud**: Certified in Oracle Cloud (OCI) and experienced with GCP.
    """)
    
    st.markdown("#### All Skills")
    st.markdown(f"""
    <div style="margin-top: 10px;">
        {skill_html}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Currently Learning Section
st.header("📚 Currently Learning")
st.markdown("I am constantly expanding my knowledge base. Here is what I am currently diving deep into:")

learn_col1, learn_col2, learn_col3 = st.columns(3)

with learn_col1:
    st.markdown("""
    <div class="stCard" style="text-align: center;">
        <h4 style="color: #FFD700;">🔐 Cybersecurity</h4>
        <p style="color: #ffffff; font-size: 0.9rem;">Exploring network security, ethical hacking, and secure system design.</p>
    </div>
    """, unsafe_allow_html=True)

with learn_col2:
    st.markdown("""
    <div class="stCard" style="text-align: center;">
        <h4 style="color: #FFD700;">🤖 Advanced AI</h4>
        <p style="color: #ffffff; font-size: 0.9rem;">Building <strong>AI Agents</strong>, mastering <strong>RAG</strong> pipelines, and experimenting with <strong>GANs</strong>.</p>
    </div>
    """, unsafe_allow_html=True)

with learn_col3:
    st.markdown("""
    <div class="stCard" style="text-align: center;">
        <h4 style="color: #FFD700;">📈 Product Management</h4>
        <p style="color: #ffffff; font-size: 0.9rem;">Learning product strategy, roadmapping, and user-centric development lifecycles.</p>
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
        return client.open("project")
    except Exception as e:
        return None

spreadsheet = init_google_sheet()

# Visitor Counter Logic
if "visitor_count" not in st.session_state:
    if spreadsheet:
        try:
            try:
                visitor_sheet = spreadsheet.worksheet("visitors")
            except:
                # Try to create if it doesn't exist
                try:
                    visitor_sheet = spreadsheet.add_worksheet(title="visitors", rows=1, cols=1)
                    visitor_sheet.update_cell(1, 1, "0")
                except:
                    visitor_sheet = None
            
            if visitor_sheet:
                current_val = visitor_sheet.cell(1, 1).value
                current_count = int(current_val) if current_val else 0
                new_count = current_count + 1
                visitor_sheet.update_cell(1, 1, str(new_count))
                st.session_state.visitor_count = new_count
            else:
                st.session_state.visitor_count = "N/A"
        except Exception as e:
            st.session_state.visitor_count = "N/A"
    else:
        st.session_state.visitor_count = "N/A"

with col2:
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            if not name or not email or not message:
                st.warning("Please fill in all fields.")
            elif spreadsheet is None:
                st.error("Google Sheets connection not configured. Please check your secrets and ensure a sheet named 'project' exists.")
            else:
                try:
                    sheet = spreadsheet.sheet1
                    sheet.append_row([name, email, message])
                    st.success("Thanks for reaching out! Your message have been sent to Jain ❤️.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

# Footer / Visitor Counter Display
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 20px; color: #666;">
    <p>Designed & Built by Yash Jain</p>
    <p style="font-size: 0.9rem;">👀 Total Visitors: <span style="color: #FFD700; font-weight: bold;">{st.session_state.get('visitor_count', '...')}</span></p>
</div>
""", unsafe_allow_html=True)
