import streamlit as st
from PIL import Image
from send_email import send_email  # Make sure this import works with your setup

# Page configuration
st.set_page_config(page_title="Dr. Ridwan Oladipo - Portfolio", layout="wide")

# Custom CSS to improve the app's appearance
st.markdown("""
<style>
    body {
        color: #333;
        background-color: #f0f8ff;
    }
    .main {
        padding: 0.1rem;
        font-family: 'Helvetica', sans-serif;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-weight: bold;
    }
    .project-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 2px solid #3498db;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }
    .skill-box {
        background-color: #e3f2fd;
        border-radius: 5px;
        padding: 0.5rem;
        margin: 0.2rem;
        display: inline-block;
        transition: all 0.3s ease;
    }
    .skill-box:hover {
        background-color: #bbdefb;
    }
    .contact-link {
        background-color: #2ecc71;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 1rem;
        transition: all 0.3s ease;
    }
    .contact-link:hover {
        background-color: #27ae60;
        transform: translateY(-2px);
    }
    .emoji-header {
        font-size: 1.5em;
        margin-right: 0.5rem;
    }
    .custom-expander {
        border: 1px solid #3498db;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .custom-expander summary {
        background-color: #3498db;
        color: white;
        padding: 0.5rem;
        cursor: pointer;
    }
    .custom-expander .content {
        padding: 1rem;
        background-color: white;
    }
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .tech-item {
        background-color: #e3f2fd;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
    }
    .tech-item:hover {
        background-color: #bbdefb;
        transform: translateY(-2px);
    }
    .tech-item .emoji {
        margin-right: 0.5rem;
    }
    .desktop-view-message {
        background-color: #fff3cd;
        border-left: 5px solid #ffeeba;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)


def main():

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('rid2.png')
    with col2:
        st.title("Dr. Ridwan Oladipo")
        st.write("Medical Doctor | Data Scientist | Innovator")
        st.write("📧 [dr.ridwan.oladipo@gmail.com](mailto:dr.ridwan.oladipo@gmail.com)")
        st.write("🔗 [LinkedIn](Your_LinkedIn_URL)")
        st.write("🐙 [GitHub](https://github.com/dr-ridwanoladipo)")
    st.markdown("</div>", unsafe_allow_html=True)

    # About Me
    st.header("🧑‍⚕️ About Me")
    st.write("""
    A visionary medical professional with a passion for leveraging technology to revolutionize healthcare. 
    Bridging the worlds of medicine and data science to pioneer innovative solutions for global health challenges.
    """)

    # Education
    st.subheader("🎓 Education")
    st.write("- MB.ChB, Obafemi Awolowo University, Nigeria (2024)")
    st.write("- Consistently ranked among the top students in my graduating class.")

    # Skills
    st.subheader("🛠️ Tech Stack")
    tech_stack = [
        ("🐍", "Python"),
        ("📊", "Data Science"),
        ("🤖", "AI / Machine Learning"),
        ("🌐", "Flask / Django"),
        ("💾", "SQL (PostgreSQL, MySQL, SQLite)"),
        ("🗣️", "Natural Language Processing (NLP)"),
        ("🔥", "PyTorch"),
        ("👁️", "Computer Vision"),
        ("💻", "HTML / CSS / JavaScript")
    ]

    st.markdown("<div class='tech-stack'>", unsafe_allow_html=True)
    for emoji, tech in tech_stack:
        st.markdown(f"<div class='tech-item'><span class='emoji'>{emoji}</span>{tech}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Projects
    st.header("🚀 Featured Projects")
    st.markdown("""
    <div class='desktop-view-message'>
        <strong>📌 Note:</strong> While these projects are responsive, a desktop view is recommended for the best experience with live demos.
    </div>
    """, unsafe_allow_html=True)

    projects = [
        {
            "name": "WeatherPro",
            "description": "Advanced weather forecast application using Streamlit. Implements complex data visualization techniques and API integration for real-time weather data analysis.",
            "github": "https://github.com/dr-ridwanoladipo/WeatherPro",
            "website": "https://weatherpro-by-drridwan.streamlit.app"
        },
        {
            "name": "Film_Oracle",
            "description": "Sophisticated movie recommendation system leveraging collaborative filtering and content-based algorithms. Demonstrates proficiency in data processing and machine learning techniques.",
            "github": "https://github.com/dr-ridwanoladipo/film-oracle",
            "website": "https://film-oracle-by-drridwan.streamlit.app"
        },
        {
            "name": "NLP BookMiner",
            "description": "Cutting-edge NLP tool for in-depth text analysis. Utilizes advanced natural language processing techniques including sentiment analysis, named entity recognition, and text summarization.",
            "github": "https://github.com/dr-ridwanoladipo/NLP-BookMiner",
            "website": "https://nlp-bookminer-by-drridwan.streamlit.app"
        },
        {
            "name": "EduTrack QT Suite",
            "description": "Comprehensive education management system showcasing database design, user authentication, and dynamic reporting capabilities. Demonstrates full-stack development skills.",
            "github": "https://github.com/dr-ridwanoladipo/edutrack-qt-suite",
            "website": "https://edutrack-qt-by-drridwan.streamlit.app"
        },
        {
            "name": "SecurePassVault",
            "description": "Robust password management application implementing advanced cryptographic techniques. Utilizes Fernet symmetric encryption and secure hashing algorithms (SHA-256) for top-tier data protection.",
            "github": "https://github.com/dr-ridwanoladipo/SecurePassVault",
            "website": "https://securevaults-by-drridwan.streamlit.app"
        }
    ]

    for project in projects:
        st.markdown(f"""
        <details class="custom-expander">
            <summary>{project['name']}</summary>
            <div class="content">
                <p>{project['description']}</p>
                <p><a href="{project['github']}">GitHub</a> | <a href="{project['website']}">Live Demo</a></p>
            </div>
        </details>
        """, unsafe_allow_html=True)

    # Additional projects
    st.subheader("🔍 More Projects")
    st.write(
        "Click on the project names below to explore more of my work on GitHub. Each repository contains detailed project descriptions and documentation in the README.md files.")

    additional_projects = [
        "web-scraper-gig-alert", "django-dynamic-jobportal", "django-culinary-canvas",
        "SmartForm-flask", "python-oop-hotel-system", "ai-powered-pyqt-chatbot",
        "smart-home-security", "flask-weather-dashboard", "DailyDigestBot",
        "automated-invoice-pdf-generator", "automated-pdf-generator", "todo-app"
    ]

    for project in additional_projects:
        st.write(f"- [{project}](https://github.com/dr-ridwanoladipo/{project})")

    # HTML/CSS Projects
    st.subheader("🎨 Web Design Projects")
    html_css_projects = [
        {
            "name": "Ecoventure",
            "description": "Modern, responsive website for an eco-tourism company showcasing advanced CSS techniques.",
            "github": "https://github.com/dr-ridwanoladipo/Ecoventure",
            "website": "https://ecoventure-by-drridwan.netlify.app"
        },
        {
            "name": "Estateology",
            "description": "Sleek real estate website demonstrating proficiency in responsive design and modern CSS frameworks.",
            "github": "https://github.com/dr-ridwanoladipo/Estateology",
            "website": "https://estateology-by-drridwan.netlify.app"
        }
    ]

    for project in html_css_projects:
        st.markdown(f"""
        <details class="custom-expander">
            <summary>{project['name']}</summary>
            <div class="content">
                <p>{project['description']}</p>
                <p><a href="{project['github']}">GitHub</a> | <a href="{project['website']}">Live Demo</a></p>
            </div>
        </details>
        """, unsafe_allow_html=True)

    # Certifications
    st.header("🏆 Certifications")
    certifications = [
        "CS50 by Harvard University",
        "Complete A.I. & Machine Learning, Data Science Bootcamp (Andrei Neagoie, Daniel Bourke)",
        "100 Days of Code: The Complete Python Pro Bootcamp (Angela Yu)",
        "Python Mega Course: Learn Python in 60 days (Ardit Sulce)"
    ]
    for cert in certifications:
        st.write(f"- {cert}")

    # Career Aspirations
    st.header("🎯 Career Aspirations")
    st.write("""
    - Pioneering the field of medical data science, with a focus on solving critical healthcare problems through AI and ML.
    - Developing a world-class, AI-driven medical education platform to support aspiring and current medical students globally.
    """)

    # Contact Form
    st.header("📩 Contact Me")
    with st.form(key="email_forms"):
        user_email = st.text_input("Your email address")
        raw_message = st.text_area("Your message")
        message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
        button = st.form_submit_button("Submit")
        if button:
            send_email(message)
            st.success("Your message was sent successfully!")


if __name__ == "__main__":
    main()