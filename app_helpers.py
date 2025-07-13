"""
🩺 Dr. Ridwan Oladipo - Medical AI Portfolio Helper Functions
All reusable functions, styling, and components for the portfolio.

Author: Dr. Ridwan Oladipo, MD | Medical AI Specialist
"""

import streamlit as st
from PIL import Image
import base64
from io import BytesIO
from typing import Dict, List, Any


def load_custom_css():
    """Load comprehensive CSS styling with medical-grade aesthetics."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');

        /* Global Reset and Variables */
        :root {
            --primary-blue: #1e3c72;
            --secondary-blue: #2a5298;
            --accent-red: #ef4444;
            --success-green: #10b981;
            --warning-amber: #f59e0b;
            --dark-gray: #1f2937;
            --light-gray: #f3f4f6;
            --white: #ffffff;
            --shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
        }

        /* Main App Container */
        .main {
            padding: 0 !important;
            max-width: 100% !important;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }

        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }

        /* Hero Section - Full Width */
        .hero-container {
            background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
            padding: 4rem 2rem;
            color: white;
            text-align: center;
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
        }

        .hero-container::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse 3s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.1); opacity: 0.8; }
        }

        .hero-image {
            width: 250px;
            height: 250px;
            border-radius: 50%;
            border: 5px solid white;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            object-fit: cover;
            margin: 0 auto 2rem;
            display: block;
        }

        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            letter-spacing: -1px;
        }

        .hero-subtitle {
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 1rem;
            opacity: 0.95;
        }

        .hero-description {
            font-size: 1.2rem;
            line-height: 1.8;
            max-width: 800px;
            margin: 0 auto 2rem;
            opacity: 0.9;
        }

        /* Badge Styles */
        .badge-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .hero-badge {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1.5rem;
            border-radius: 30px;
            font-weight: 600;
            font-size: 0.9rem;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        /* Contact Buttons */
        .contact-container {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .contact-button {
            background: var(--success-green);
            color: white !important;
            padding: 0.75rem 2rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
            display: inline-block;
        }

        .contact-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
            text-decoration: none;
        }

        /* Section Styling */
        .section-header {
            text-align: center;
            margin: 4rem 0 3rem;
        }

        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--dark-gray);
            margin-bottom: 1rem;
            position: relative;
            display: inline-block;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary-blue), var(--accent-red));
            border-radius: 2px;
        }

        .section-subtitle {
            font-size: 1.1rem;
            color: #64748b;
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
        }

        /* Professional Cards */
        .project-card {
            background: white;
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
            border: 1px solid #e5e7eb;
            transition: all 0.3s ease;
            height: 100%;
            position: relative;
            overflow: hidden;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, var(--primary-blue), var(--accent-red));
        }

        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
        }

        /* Status Badges */
        .status-live {
            background: var(--success-green);
            color: white;
            padding: 0.25rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-block;
        }

        .status-coming {
            background: var(--warning-amber);
            color: white;
            padding: 0.25rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-block;
        }

        /* Metrics */
        .metric-card {
            background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid #c7d2fe;
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: var(--primary-blue);
            margin-bottom: 0.5rem;
        }

        .metric-label {
            color: #64748b;
            font-size: 0.9rem;
            font-weight: 500;
        }

        /* Tech Tags */
        .tech-container {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1rem 0;
        }

        .tech-tag {
            background: #e0e7ff;
            color: var(--primary-blue);
            padding: 0.25rem 0.75rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        /* Timeline */
        .timeline-container {
            position: relative;
            padding-left: 3rem;
            margin: 2rem 0;
        }

        .timeline-line {
            position: absolute;
            left: 1rem;
            top: 0;
            bottom: 0;
            width: 3px;
            background: linear-gradient(180deg, var(--primary-blue) 0%, var(--accent-red) 100%);
        }

        .timeline-item {
            position: relative;
            margin-bottom: 2rem;
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            margin-left: 1rem;
        }

        .timeline-dot {
            position: absolute;
            left: -2.4rem;
            top: 1.5rem;
            width: 15px;
            height: 15px;
            background: var(--accent-red);
            border-radius: 50%;
            border: 3px solid white;
            box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.2);
        }

        /* Skills */
        .skill-badge {
            background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
            color: var(--primary-blue);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            border: 1px solid #93c5fd;
            display: inline-block;
            margin: 0.25rem;
            transition: all 0.2s ease;
        }

        .skill-badge:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
        }

        /* Footer */
        .footer-container {
            background: var(--dark-gray);
            color: white;
            padding: 3rem 2rem;
            border-radius: 30px 30px 0 0;
            text-align: center;
            margin-top: 4rem;
        }

        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}

        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-title { font-size: 2.5rem; }
            .hero-subtitle { font-size: 1.4rem; }
            .section-title { font-size: 2rem; }
        }
    </style>
    """, unsafe_allow_html=True)


def render_hero_section():
    """Render the hero section with image and contact info."""
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)

    # Try to load and display image
    try:
        img = Image.open('rid2.png')
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(f'<img src="data:image/png;base64,{img_str}" class="hero-image" alt="Dr. Ridwan Oladipo">',
                    unsafe_allow_html=True)
    except:
        st.markdown(
            '<div style="width: 250px; height: 250px; background: rgba(255,255,255,0.2); border-radius: 50%; margin: 0 auto 2rem; display: flex; align-items: center; justify-content: center; font-size: 5rem;">🩺</div>',
            unsafe_allow_html=True)

    st.markdown('<h1 class="hero-title">Dr. Ridwan Oladipo</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="hero-subtitle">Medical AI Specialist</h2>', unsafe_allow_html=True)
    st.markdown('''
    <p class="hero-description">
        Bridging clinical excellence with cutting-edge artificial intelligence to build 
        production-ready healthcare systems that save lives and enhance patient care.
    </p>
    ''', unsafe_allow_html=True)

    # Badges
    st.markdown('''
    <div class="badge-container">
        <span class="hero-badge">MD • 2023 Graduate</span>
        <span class="hero-badge">Deep Learning & NLP</span>
        <span class="hero-badge">MLOps & AWS</span>
        <span class="hero-badge">Production AI Systems</span>
    </div>
    ''', unsafe_allow_html=True)

    # Contact Links
    st.markdown('''
    <div class="contact-container">
        <a href="mailto:dr.ridwan.oladipo@gmail.com" class="contact-button">📧 Contact</a>
        <a href="https://linkedin.com/in/drridwanoladipoai" class="contact-button" target="_blank">💼 LinkedIn</a>
        <a href="https://github.com/dr-ridwanoladipo" class="contact-button" target="_blank">🔗 GitHub</a>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_section_header(title: str, subtitle: str):
    """Render a section header with title and subtitle."""
    st.markdown(f'''
    <div class="section-header">
        <h2 class="section-title">{title}</h2>
        <p class="section-subtitle">{subtitle}</p>
    </div>
    ''', unsafe_allow_html=True)


def create_metric_card(value: str, label: str) -> str:
    """Create HTML for a metric card."""
    return f'''
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    '''


def render_project_card(project_data: Dict[str, Any], col):
    """Render one project card with unique keys where required (only for st.button)."""
    slug = project_data["title"].lower().replace(" ", "_")   # unique slug for widget keys

    with col:
        # ── Card container ───────────────────────────────────────────
        st.markdown('<div class="project-card">', unsafe_allow_html=True)

        # ── Header (title + status badge) ────────────────────────────
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">
                <h3 style="margin:0;color:#1f2937;">{project_data['icon']} {project_data['title']}</h3>
                <span class="{project_data['status_class']}">{project_data['status']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Description ──────────────────────────────────────────────
        st.markdown(project_data["description"])

        # ── Metrics grid (2 × N) ─────────────────────────────────────
        if project_data.get("metrics"):
            c1, c2 = st.columns(2)
            for i, m in enumerate(project_data["metrics"]):
                target_col = c1 if i % 2 == 0 else c2
                with target_col:
                    st.markdown(create_metric_card(m["value"], m["label"]), unsafe_allow_html=True)

        # ── Tech-stack tags ──────────────────────────────────────────
        if project_data.get("tech_stack"):
            tags_html = "".join(f'<span class="tech-tag">{t}</span>' for t in project_data["tech_stack"])
            st.markdown(f'<div class="tech-container">{tags_html}</div>', unsafe_allow_html=True)

        # ── Action buttons ───────────────────────────────────────────
        if project_data.get("demo_url"):
            st.link_button("🌐 Live Demo", project_data["demo_url"], use_container_width=True)

        if project_data.get("github_url"):
            st.link_button("📝 GitHub", project_data["github_url"], use_container_width=True)

        if project_data.get("coming_soon"):
            # st.button requires a unique key; link_button doesn’t accept key
            st.button("🚧 Coming Soon", disabled=True,
                      key=f"{slug}_coming_btn", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)


def render_timeline_item(year: str, title: str, description: str):
    """Render a single timeline item."""
    st.markdown(f'''
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div style="background: #e0e7ff; color: #1e3c72; padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.8rem; font-weight: 600; display: inline-block; margin-bottom: 0.5rem;">
            {year}
        </div>
        <h4 style="color: #1f2937; margin-bottom: 0.5rem;">{title}</h4>
        <p style="color: #64748b; margin: 0;">{description}</p>
    </div>
    ''', unsafe_allow_html=True)


def render_skill_section(title: str, icon: str, skills: List[str]):
    """Render a skill section with badges."""
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown(f"### {icon} {title}")

    for skill in skills:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_contact_form():
    """Render the contact form."""
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown("### 📧 Send a Message")

    with st.form(key="contact_form"):
        email = st.text_input("Your Email", placeholder="your.email@company.com")
        subject = st.text_input("Subject", placeholder="Collaboration opportunity")
        message = st.text_area("Message", placeholder="Hello Dr. Ridwan...", height=100)

        submitted = st.form_submit_button("Send Message", use_container_width=True)

        if submitted:
            if email and message:
                try:
                    from send_email import send_email
                    full_message = f"Subject: {subject}\nFrom: {email}\n\n{message}"
                    send_email(full_message)
                    st.success("✅ Message sent successfully!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
            else:
                st.warning("⚠️ Please fill all fields")

    st.markdown('</div>', unsafe_allow_html=True)


def render_footer():
    """Render the footer section."""
    st.markdown('''
    <div class="footer-container">
        <h3 style="color: white; margin-bottom: 1rem;">💡 Ready to Transform Healthcare?</h3>
        <p style="opacity: 0.9; margin-bottom: 1.5rem; line-height: 1.6; max-width: 800px; margin-left: auto; margin-right: auto;">
            I'm actively seeking opportunities to join world-class healthcare organizations 
            and innovative medical AI companies where I can apply my unique blend of medical 
            expertise and technical mastery to build transformative, life-saving technologies.
        </p>
        <p style="opacity: 0.7; margin: 0;">
            <strong>© 2025 Dr. Ridwan Oladipo, MD | Medical AI Specialist</strong><br>
            <em>Transforming healthcare through intelligent, compassionate AI solutions</em>
        </p>
    </div>
    ''', unsafe_allow_html=True)


# ===============================
# PROJECT DATA
# ===============================
def get_featured_projects():
    """Get data for featured projects."""
    return [
        {
            "icon": "🩺",
            "title": "Clinical Heart Disease AI",
            "status": "Live Production",
            "status_class": "status-live",
            "description": "**97% sensitivity** cardiovascular risk assessment with SHAP explainability. AWS ECS Fargate deployment.",
            "metrics": [
                {"value": "97%", "label": "Sensitivity"},
                {"value": "0.91", "label": "ROC-AUC"},
                {"value": "50+", "label": "Optuna Trials"},
                {"value": "AWS", "label": "Production"}
            ],
            "tech_stack": ["XGBoost", "SHAP", "FastAPI", "Streamlit", "AWS ECS", "Docker"],
            "demo_url": "https://cardio.mednexai.com",
            "github_url": "https://github.com/dr-ridwanoladipo/cardio-ai-predictor"
        },
        {
            "icon": "📈",
            "title": "ECG Cardiac Rhythm AI",
            "status": "Q2 2025",
            "status_class": "status-coming",
            "description": "**Deep learning** arrhythmia detection with clinical-grade accuracy. Multi-lead ECG analysis.",
            "metrics": [
                {"value": "94%", "label": "Target Accuracy"},
                {"value": "12-Lead", "label": "ECG Analysis"},
                {"value": "Real-time", "label": "Processing"},
                {"value": "MONAI", "label": "Framework"}
            ],
            "tech_stack": ["PyTorch", "MONAI", "CNN+LSTM", "GradCAM", "Time Series"],
            "coming_soon": True
        },
        {
            "icon": "📝",
            "title": "Medical Transcription AI",
            "status": "Q2 2025",
            "status_class": "status-coming",
            "description": "**Multi-label** clinical specialty classification using fine-tuned BioClinicalBERT.",
            "metrics": [
                {"value": "89%", "label": "Multi-label F1"},
                {"value": "<100ms", "label": "Inference"},
                {"value": "15+", "label": "Specialties"},
                {"value": "ONNX", "label": "Optimized"}
            ],
            "tech_stack": ["BioClinicalBERT", "Transformers", "ONNX", "Medical NLP"],
            "coming_soon": True
        }
    ]


def get_timeline_data():
    """Get timeline data."""
    return [
        {
            "year": "2018-2023",
            "title": "Medical Education & Clinical Excellence",
            "description": "M.B.Ch.B, Obafemi Awolowo University. Top scorer in clinical medicine, founded educational initiatives."
        },
        {
            "year": "2024",
            "title": "Strategic Pivot to AI",
            "description": "Intensive self-directed learning in ML, DL, and medical AI. Harvard CS50 and specialized certifications."
        },
        {
            "year": "2025",
            "title": "Medical AI Specialist",
            "description": "Launched production medical AI systems. Seeking senior roles to drive healthcare innovation."
        }
    ]


def get_skills_data():
    """Get skills organized by category."""
    return {
        "Medical AI & Machine Learning": [
            "XGBoost & Ensemble Methods", "Deep Learning (PyTorch/TensorFlow)",
            "SHAP & GradCAM Explainability", "Optuna Optimization",
            "Medical Image Processing", "BioClinicalBERT & Medical NLP",
            "MONAI Framework", "Clinical Decision Support"
        ],
        "Data Science & Engineering": [
            "Python (NumPy, Pandas, Scikit-learn)", "Advanced SQL",
            "Statistical Analysis", "Feature Engineering",
            "Clinical Data Processing", "Model Validation"
        ],
        "Production & Deployment": [
            "FastAPI & RESTful Services", "AWS (ECS, ECR, ALB, Route 53)",
            "Docker & Containerization", "CI/CD with GitHub Actions",
            "Microservices Architecture", "Zero-downtime Deployments"
        ],
        "Frontend & Visualization": [
            "Streamlit & Medical UI", "Plotly & Dashboards",
            "Clinical Workflow Design", "Data Visualization",
            "User Experience", "Responsive Design"
        ]
    }