"""
🩺 Dr. Ridwan Oladipo - Medical AI Specialist Portfolio
Main application file that uses helper functions from app_helpers.py

Author: Dr. Ridwan Oladipo, MD | Medical AI Specialist
"""

import streamlit as st
from app_helpers import (
    load_custom_css,
    render_hero_section,
    render_section_header,
    render_project_card,
    render_timeline_item,
    render_skill_section,
    render_contact_form,
    render_footer,
    get_featured_projects,
    get_timeline_data,
    get_skills_data
)

# ===============================
# PAGE CONFIGURATION
# ===============================
st.set_page_config(
    page_title="Dr. Ridwan Oladipo | Medical AI Specialist",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===============================
# MAIN APPLICATION
# ===============================
def main():
    """Main portfolio application."""

    # Load custom CSS styling
    load_custom_css()

    # ========== HERO SECTION ==========
    render_hero_section()

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider

    # ========== MISSION STATEMENT ==========
    render_section_header(
        "🎯 Mission Statement",
        "As a recently graduated Medical Doctor with specialized expertise in AI and machine learning, "
        "I'm dedicated to developing production-grade medical AI systems that transform clinical decision-making. "
        "My unique combination of medical domain knowledge and advanced technical skills positions me to build "
        "clinically-validated, explainable AI solutions for real-world healthcare challenges."
    )

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider

    # ========== FEATURED PROJECTS ==========
    render_section_header(
        "🏥 Featured Medical AI Portfolio",
        "Production-ready healthcare AI systems combining clinical expertise with advanced machine learning"
    )

    # Create columns for projects
    projects = get_featured_projects()
    cols = st.columns(3)

    for i, project in enumerate(projects):
        render_project_card(project, cols[i])

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider

    # ========== PROFESSIONAL TIMELINE ==========
    render_section_header(
        "📚 Professional Evolution",
        "Strategic transformation from clinical medicine to medical AI specialist"
    )

    # Timeline container
    st.markdown('<div class="timeline-container"><div class="timeline-line"></div>', unsafe_allow_html=True)

    timeline_data = get_timeline_data()
    for item in timeline_data:
        render_timeline_item(item["year"], item["title"], item["description"])

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider

    # ========== TECHNICAL EXPERTISE ==========
    render_section_header(
        "🧬 Technical Expertise",
        "Deep specialization in medical AI with production deployment capabilities"
    )

    # Skills grid
    skills_data = get_skills_data()
    col1, col2 = st.columns(2)

    with col1:
        render_skill_section("Medical AI & Machine Learning", "🤖", skills_data["Medical AI & Machine Learning"])
        st.markdown('<div style="margin-top: 1rem;"></div>', unsafe_allow_html=True)
        render_skill_section("Data Science & Engineering", "⚗️", skills_data["Data Science & Engineering"])

    with col2:
        render_skill_section("Production & Deployment", "🏗️", skills_data["Production & Deployment"])
        st.markdown('<div style="margin-top: 1rem;"></div>', unsafe_allow_html=True)
        render_skill_section("Frontend & Visualization", "🎨", skills_data["Frontend & Visualization"])

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider

    # ========== PROFESSIONAL IMPACT ==========
    render_section_header(
        "📊 Professional Impact",
        "Quantified achievements in medical education, clinical practice, and AI development"
    )

    impact_col1, impact_col2, impact_col3 = st.columns(3)

    with impact_col1:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🎓 Educational Leadership")
        st.markdown("""
        - Founded **Distinction Group** reaching 6+ universities
        - Trained **5,000+ students** in high-income skills
        - **Best Teacher** awards at multiple centers
        - Alumni now lead student associations on LinkedIn
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with impact_col2:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🏥 Clinical Excellence")
        st.markdown("""
        - **Top scorer** in clinical medicine examination
        - **10/12 excellent grades** in medical school
        - **2023 M.B.Ch.B** graduate with distinction
        - Strong foundation in patient care and diagnostics
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with impact_col3:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 AI System Performance")
        st.markdown("""
        - **97% sensitivity** in heart disease detection
        - **<200ms** API response times
        - **99.9% uptime** production systems
        - Clinical-grade accuracy with explainable AI
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider

    # ========== VALUE PROPOSITION ==========
    render_section_header(
        "💼 Professional Value Proposition",
        "Unique competitive advantages and target opportunities"
    )

    val_col1, val_col2 = st.columns(2)

    with val_col1:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Unique Competitive Advantage")
        st.markdown("""
        **Medical Domain Expertise:** Recently graduated MD with clinical training and deep healthcare systems knowledge.
        
        **Production ML Engineering:** End-to-end system development, deployment, and monitoring capabilities.
        
        **Healthcare AI Specialization:** HIPAA-compliant, clinically-validated solutions with explainable AI.
        
        **Cross-functional Leadership:** Proven ability to bridge medical teams and engineering organizations.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with val_col2:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 Target Opportunities")
        st.markdown("""
        Seeking roles with **world-class healthcare organizations** and **innovative medical AI companies**:
        
        • Senior Medical Data Scientist  
        • Clinical AI Engineer  
        • Healthcare ML Lead  
        • Medical AI Product Manager  
        • Clinical Decision Support Developer  
        • Healthcare Innovation Specialist
        
        **Open to:** Remote, Hybrid, or Relocation
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider

    # ========== ADDITIONAL PROJECTS (Expandable) ==========
    with st.expander("📚 Additional Technical Projects", expanded=False):
        additional_projects = [
            {
                "title": "🎬 Film Oracle",
                "desc": "Advanced recommendation system with collaborative filtering",
                "github": "https://github.com/dr-ridwanoladipo/film-oracle",
                "demo": "https://film-oracle-by-drridwan.streamlit.app"
            },
            {
                "title": "📖 NLP BookMiner",
                "desc": "NLP toolkit with sentiment analysis and entity recognition",
                "github": "https://github.com/dr-ridwanoladipo/NLP-BookMiner",
                "demo": "https://nlp-bookminer-by-drridwan.streamlit.app"
            },
            {
                "title": "🌦️ WeatherPro",
                "desc": "Real-time weather forecast with API integration",
                "github": "https://github.com/dr-ridwanoladipo/WeatherPro",
                "demo": "https://weatherpro-by-drridwan.streamlit.app"
            },
            {
                "title": "🔐 SecurePassVault",
                "desc": "Password manager with Fernet encryption",
                "github": "https://github.com/dr-ridwanoladipo/SecurePassVault",
                "demo": "https://securevaults-by-drridwan.streamlit.app"
            }
        ]

        for p in additional_projects:
            st.markdown('<div class="expander-card">', unsafe_allow_html=True)

            # title + description
            st.markdown(f"**{p['title']}**  \n{p['desc']}")

            # buttons side-by-side
            b1, b2 = st.columns(2)
            with b1:
                st.link_button("📝 GitHub", p['github'], use_container_width=True)
            with b2:
                st.link_button("🌐 Demo", p['demo'], use_container_width=True)

            st.markdown('</div>', unsafe_allow_html=True)

    # ========== CERTIFICATIONS (Expandable) ==========
    with st.expander("🏆 Professional Certifications & Training", expanded=False):
        certifications = [
            "🏛️ **Harvard CS50** - Introduction to Computer Science",
            "🤖 **Complete AI & ML Bootcamp** - Andrei Neagoie, Daniel Bourke",
            "🐍 **100 Days of Code: Python** - Angela Yu",
            "🚀 **FastAPI Complete Course** - Eric Roby, Chad Darby",
            "🏥 **Deep Learning for Medical Image Analysis** - PyTorch specialization",
            "🤖 **Generative AI with Langchain** - Krish Naik"
        ]

        for cert in certifications:
            st.markdown(f"- {cert}")

        st.info("🎯 Currently preparing for **AWS Machine Learning Specialty Certification**")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider

    # ========== CONTACT SECTION ==========
    render_section_header(
        "🤝 Let's Build the Future of Healthcare AI",
        "Ready to revolutionize healthcare through AI? Let's connect and discuss how we can "
        "transform patient care through intelligent, compassionate technology solutions."
    )

    # Contact columns
    contact_col1, contact_col2 = st.columns([1, 1])

    with contact_col1:
        render_contact_form()

    with contact_col2:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🌐 Connect Directly")

        st.info("🎯 **Open to Senior Medical AI Roles**")

        st.markdown('''
        <div style="margin-top: 1rem;">
            <a href="mailto:dr.ridwan.oladipo@gmail.com" class="contact-button" style="display: block; text-align: center; margin-bottom: 1rem;">
                📧 dr.ridwan.oladipo@gmail.com
            </a>
            <a href="https://linkedin.com/in/drridwanoladipoai" class="contact-button" target="_blank" style="display: block; text-align: center; margin-bottom: 1rem;">
                💼 LinkedIn Profile
            </a>
            <a href="https://github.com/dr-ridwanoladipo" class="contact-button" target="_blank" style="display: block; text-align: center; margin-bottom: 1rem;">
                🔗 GitHub Portfolio
            </a>
            <a href="https://cardio.mednexai.com" class="contact-button" target="_blank" style="display: block; text-align: center;">
                🩺 Live Medical AI Demo
            </a>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)  # ⬅ divider
    # ========== FOOTER ==========
    render_footer()


# ===============================
# ENTRY POINT
# ===============================
if __name__ == "__main__":
    main()