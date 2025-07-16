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


def load_custom_css() -> None:
    """Inject complete, structured portfolio CSS for medical AI."""
    st.markdown(
        """
        <style>
        /* ========== GOOGLE FONT ========== */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        /* ========== CSS VARIABLES ========== */
        :root {
            --primary-blue: #1e3c72;
            --secondary-blue: #2a5298;
            --accent-teal: #10b981;
            --light-blue: #e0e7ff;
            --dark-navy: #1f2937;
        }

        /* ========== GLOBAL ========== */
        div[data-testid="stAppViewContainer"] > main {
            padding: 1.5rem 3rem;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }

        /* ========== TYPOGRAPHY ========== */
        .section-title {
            font-size: 1.5rem !important;
            font-weight: 600 !important;
            line-height: 1.5rem !important;
            color: var(--dark-navy);
            margin: 0;
            position: relative;
            display: inline-block;
        }
        .section-title::after {
            content: '';
            position: absolute;
            bottom: 0 !important;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            border-radius: 2px;
            background: linear-gradient(90deg, var(--primary-blue), var(--accent-teal));
        }
        h3 {
            font-size: 1.2rem !important;
            font-weight: 600 !important;
        }
        h4 {
            font-size: 1.1rem !important;
            font-weight: 600 !important;
        }

        /* ========== HERO SECTION ========== */
        .hero-container {
            background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
            color: #fff;
            padding: 3rem 2rem;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,.12);
        }
        .hero-flex {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1.5rem;
            text-align: center;
        }
        @media(min-width:900px){
            .hero-flex {flex-direction: row; text-align: left;}
        }
        .hero-image {
            width: 180px; height: 180px; border-radius: 50%;
            border: 5px solid #fff; object-fit: cover;
            box-shadow: 0 6px 20px rgba(0,0,0,.25);
        }
        .hero-title {font-size: 2.8rem; font-weight: 800; margin: 0;}
        .hero-subtitle {font-size: 1.6rem; font-weight: 600; margin: 0.3rem 0 0;}
        .hero-description {
            font-size: 1.1rem; line-height: 1.6; max-width: 550px;
            margin-top: 0.8rem; max-width: 100% !important; text-align: left !important;
        }
        .badge-container {display: flex; gap: 0.8rem; flex-wrap: wrap; margin-top: 1rem;}
        .hero-badge {
            background: rgba(255,255,255,.15);
            padding: 0.3rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 620;
        }

        /* ========== NAVBAR LINKS ========== */
        .navbar-links {
            display: flex; justify-content: center;
            gap: 1.5rem; margin-top: -0.5rem;
            background: var(--dark-navy);
            padding: 0.1rem 0.1rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        }
        .navbar-links a {
            text-decoration: none;
            color: white;
            font-weight: 600;
            font-size: 1.05rem;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
        }
        .navbar-links a:hover {
            color: var(--accent-teal);
            transform: translateY(-2px);
        }

        /* ========== SECTION HEADERS ========== */
        .section-header {
            text-align: center;
            margin-bottom: 3rem;
        }
        .section-subtitle {
            font-size: 1.05rem; color: #64748b;
            max-width: 800px; margin: 0.8rem auto; line-height: 1.7;
            max-width: 100% !important; text-align: left !important;
        }
        .section-header .section-title {margin-bottom: 1rem;}
        .section-header .section-subtitle {margin-top: 0.3rem;}

        /* ========== PROJECT & METRIC CARDS ========== */
        .featured-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px,1fr));
            gap: 2rem;
        }
        .project-card {
            background: var(--light-blue);
            border: 1px solid #c7d2fe;
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            box-shadow: 0 6px 24px rgba(0,0,0,.08);
            transition: .3s; height: 100%;
        }
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(0,0,0,.12);
        }
        .project-card::before {
            content: ''; position: absolute; top: 0; left: 0;
            width: 100%; height: 5px;
            background: linear-gradient(90deg,var(--primary-blue),var(--accent-teal));
        }
        .metric-card {
            background: linear-gradient(135deg,#f8fafc,#e0e7ff);
            border: 1px solid #c7d2fe;
            border-radius: 15px;
            padding: 1.2rem; text-align: center;
        }

        /* ========== STATUS & TECH TAGS ========== */
        .status-live, .status-coming {
            padding: 0.2rem 0.9rem; border-radius: 15px; font-size: 0.75rem; color: #fff;
        }
        .status-live {background: var(--accent-teal);}
        .status-coming {background: #f59e0b;}
        .tech-container {
            display: flex; flex-wrap: wrap; gap: 0.5rem;
            margin-top: 1rem; margin-bottom: 0.9rem !important;
        }
        .tech-tag {
            background: #e0e7ff; color: var(--primary-blue);
            padding: 0.25rem 0.75rem; border-radius: 15px; font-size: 0.8rem;
        }

        /* ========== TIMELINE ========== */
        .timeline-container {position: relative; padding-left: 3rem; margin: 2rem 0;}
        .timeline-line {
            position: absolute; left: 1rem; top: 0; bottom: 0; width: 3px;
            background: linear-gradient(var(--primary-blue),var(--accent-teal));
        }
        .timeline-item {
            position: relative; margin-left: 1rem; margin-bottom: 2rem; background: #fff;
            padding: 1.3rem; border-radius: 15px;
            box-shadow: 0 4px 18px rgba(0,0,0,.08);
        }
        .timeline-dot {
            position: absolute; left: -1.2rem; top: 1.4rem; width: 14px; height: 14px;
            border-radius: 50%; background: var(--accent-teal); border: 3px solid #fff;
            box-shadow: 0 0 0 3px rgba(16,185,129,.2);
        }

        /* ========== SKILL & EXPANDER CARDS ========== */
        .skill-badge {
            background: linear-gradient(135deg,#dbeafe,#bfdbfe);
            color: var(--primary-blue);
            padding: 0.45rem 0.9rem; border-radius: 18px; font-size: 0.85rem; font-weight: 500;
            border: 1px solid #93c5fd; display: inline-block; margin: 0.25rem; transition: .2s;
        }
        .skill-badge:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(16,185,129,.2);
        }
        .expander-card {
            background: linear-gradient(135deg,#e0f2ff 0%,#c7e0ff 100%);
            border: 1px solid #a5cfff;
            border-radius: 15px; padding: 1.25rem; margin-bottom: 1rem;
        }

        /* ========== CERTIFICATIONS INSIDE EXPANDER ========== */
        ul.certification-list {
            background: linear-gradient(135deg, #e0f2ff 0%, #c7e0ff 100%);
            border: 2px solid var(--accent-teal);
            border-radius: 12px; padding: 1rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1); margin-top: 0.5rem;
            list-style: none;
        }
        ul.certification-list li {
            background: var(--light-blue);
            border-left: 4px solid var(--accent-teal);
            padding: 0.5rem 1rem; margin-bottom: 0.5rem;
            border-radius: 8px; font-weight: 500;
        }

        /* ========== CONTACT BUTTONS ========== */
        .contact-button {
            background: var(--accent-teal); color: #fff !important;
            padding: 0.65rem 2rem; border-radius: 25px;
            font-weight: 600; text-decoration: none !important;
            box-shadow: 0 4px 15px rgba(16,185,129,.3);
            display: inline-block; transition: all 0.3s ease;
        }
        .contact-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(16,185,129,.4);
        }

        /* ========== EXPANDER HEADERS RESTORED ========== */
        details > summary {
            background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
            color: white;
            padding: 1rem;
            border-radius: 12px;
            font-weight: 600;
            cursor: pointer;
            list-style: none;
            transition: all 0.3s ease;
        }
        details > summary::-webkit-details-marker {display: none;}
        details[open] > summary {
            border-bottom-left-radius: 0;
            border-bottom-right-radius: 0;
        }

        /* ========== FOOTER ========== */
        .footer-container {
            background: var(--dark-navy); color: #fff;
            margin-top: 1rem !important; padding: 1rem 1rem !important;
            border-radius: 20px 20px 0 0; width: 100% !important; text-align: center;
        }

        /* ========== CLEANUP ========== */
        #MainMenu, footer, header, .stDeployButton {visibility: hidden;}
        div.block-container {
            padding-top: 0 !important; padding-bottom: 0 !important;
            margin-top: 0 !important; margin-bottom: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero_section() -> None:
    """
    Full-width banner + horizontal contact bar immediately after hero image,
    followed by mission text + stylish badges.
    Place `hero.png` (1920×500 banner) in the app root.
    """
    import base64, pathlib, textwrap
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)

    # ── 1. Banner image ─────────────────────────────────────────────
    img_path = pathlib.Path("hero.png")
    if img_path.exists():
        b64 = base64.b64encode(img_path.read_bytes()).decode()
        st.markdown(
            f'<img src="data:image/png;base64,{b64}" '
            f'style="width:100%;max-width:100%;border-radius:12px;">',
            unsafe_allow_html=True,
        )
    else:
        st.error("❌  hero.png not found – place it in the app folder")

    # ── 2. Contact bar immediately after hero image ────────────────
    st.markdown(
        textwrap.dedent(
            """
            <div class="navbar-links">
                <a href="mailto:dr.ridwan.oladipo@gmail.com">📧 Contact</a>
                <a href="https://linkedin.com/in/drridwanoladipoai" target="_blank">💼 LinkedIn</a>
                <a href="https://github.com/dr-ridwanoladipo" target="_blank">🔗 GitHub</a>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    # ── 3. Mission statement ──────────────────────────────────────
    st.markdown(
        """
        <p class="hero-description" style="text-align:center;margin-top:1.7rem;font-size:1.15rem;">
            Bridging clinical excellence with <strong>cutting-edge AI</strong> to build
            <strong>production-ready healthcare systems</strong> that save lives
            and elevate patient care.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # ── 4. Stylish pill-badges  ───────────────────────────────────
    st.markdown(
        """
        <div class="badge-container">
            <span class="hero-badge">🎓 MD • 2023 Graduate</span>
            <span class="hero-badge">🚀 MLOps • Docker • AWS</span>
            <span class="hero-badge">🤖 Deep Learning & NLP</span>
            <span class="hero-badge">🩺 Production AI Systems</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


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
    """Render one project card with better button layout and clear widget keys."""
    slug = project_data["title"].lower().replace(" ", "_")

    with col:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)

        # ── header ──────────────────────────────────────────────
        st.markdown(
            f"""
            <div style="display:flex;justify-content:flex-start;align-items:center;gap:0.8rem;margin-bottom:0.3rem;">
                <h3 style="margin:0;color:#1f2937;">{project_data['icon']} {project_data['title']}</h3>
                <span class="{project_data['status_class']}">{project_data['status']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── description ────────────────────────────────────────
        st.markdown(project_data["description"])

        # ── metrics grid (2 × N) ───────────────────────────────
        if project_data.get("metrics"):
            c1, c2 = st.columns(2)
            for i, m in enumerate(project_data["metrics"]):
                with (c1 if i % 2 == 0 else c2):
                    st.markdown(create_metric_card(m["value"], m["label"]), unsafe_allow_html=True)

        # ── tech tags ───────────────────────────────────────────
        if project_data.get("tech_stack"):
            tags_html = "".join(f'<span class="tech-tag">{t}</span>' for t in project_data["tech_stack"])
            st.markdown(f'<div class="tech-container">{tags_html}</div>', unsafe_allow_html=True)

        # ── action buttons side-by-side ─────────────────────────
        demo = project_data.get("demo_url")
        git  = project_data.get("github_url")

        if demo or git:
            b1, b2 = st.columns(2)
            if demo:
                with b1:
                    st.link_button("🌐 Live Demo", demo, use_container_width=True)
            if git:
                with b2:
                    st.link_button("📝 GitHub", git, use_container_width=True)

        # ── coming-soon badge (unique key) ──────────────────────
        if project_data.get("coming_soon"):
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
                    subject_line = f"Contact Form: {subject}"
                    body_text = (
                        f"NEW CONTACT FORM SUBMISSION\n\n"
                        f"📧 From: {email}\n"
                        f"📝 Subject: {subject}\n\n"
                        f"{message}"
                    )
                    send_email(subject_line, body_text)
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
            "status": "Live",
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
            "status": "Q3 2025",
            "status_class": "status-coming",
            "description": "**Deep learning** arrhythmia detection with clinical-grade accuracy. Real-time multi-lead ECG analysis.",
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
            "status": "Q3 2025",
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
            "year": "2017-2023",
            "title": "Medical Education & Clinical Excellence",
            "description": "M.B.Ch.B with clinical excellence. Built foundation in evidence-based medicine, patient care, and healthcare systems."
        },
        {
            "year": "2024",
            "title": "Strategic Pivot to AI",
            "description": "Python (NumPy, Pandas, Scikit-learn, Matplotlib), Advanced SQL, ML/DL frameworks (PyTorch & TensorFlow), statistical analysis, and medical NLP. Harvard CS50 + specialized certifications."
        },
        {
            "year": "2025",
            "title": "Medical AI Specialist",
            "description": "Advanced MLOps with FastAPI, Docker, and comprehensive AWS architecture (ECS/Fargate, ECR, ALB, Route 53, EC2, Lambda, Auto-scaling, EventBridge, Boto3 automation). CI/CD pipelines, LLMs, RAG pipelines, and AI APIs — building enterprise-ready healthcare solutions.  <span style='color:#10b981; font-weight:600; font-style:italic;'>Currently preparing for AWS Machine Learning Specialty Certification</span>"
        }
    ]


def get_skills_data():
    """Get skills organized by category."""
    return {
        "Medical AI & Machine Learning": [
            "XGBoost & Ensemble Methods",
            "Deep Learning (PyTorch, TensorFlow)",
            "SHAP & GradCAM Explainability",
            "Optuna Hyperparameter Optimization",
            "Medical Image Processing (MONAI)",
            "BioClinicalBERT & Medical NLP",
            "Time Series Analysis",
            "Clinical Decision Support Systems",
            "LLMs & RAG Pipelines"
        ],
        "Data Science & Engineering": [
            "Python (NumPy, Pandas, Scikit-learn)",
            "Advanced SQL & PostgreSQL",
            "Statistical Analysis & Feature Engineering",
            "Clinical Data Processing & Validation",
            "Medical Knowledge Graphs"
        ],
        "Production & Deployment": [
            "FastAPI & RESTful Services",
            "AWS (ECS/Fargate, ECR, ALB, Route 53, EC2, Lambda, EventBridge)",
            "Docker & Containerization",
            "Auto-scaling & Load Balancing",
            "CI/CD with GitHub Actions",
            "Boto3 Automation",
            "Microservices Architecture",
            "Zero-downtime Deployments"
        ],
        "Frontend & Visualization": [
            "Streamlit & Medical UI",
            "Plotly Interactive Dashboards",
            "Clinical Workflow Design",
            "Data Visualization & UX",
            "Responsive Design"
        ]
    }
