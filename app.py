import streamlit as st
import pandas as pd
import plotly.express as px
from modules.screening import PersonalityScreener
from modules.training import TrainingModule
from modules.quiz import QuizModule
from modules.recommendations import RecommendationEngine

# Streamlit Konfiguration MUSS ZUERST kommen!
st.set_page_config(
    page_title="Big Five Personality Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🎨 MODERNES CSS STYLING
css_styles = """
<style>
    /* Haupt-Hintergrund mit subtilem Gradient */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        min-height: 100vh;
    }
    
    /* 📱 MODERNE BUTTONS */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 18px 25px;
        border-radius: 15px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
        width: 100%;
        margin: 8px 0;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* 🎯 HEADER STYLING MIT GRADIENT */
    h1 {
        color: #2c3e50;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-bottom: 15px;
        font-weight: 800;
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 30px;
    }
    
    h2 {
        color: #34495e;
        margin-top: 30px !important;
        font-weight: 700;
        border-left: 5px solid #667eea;
        padding-left: 15px;
        background: linear-gradient(135deg, #667eea20 0%, #764ba220 100%);
        padding: 15px;
        border-radius: 0 10px 10px 0;
    }
    
    h3 {
        color: #5d6d7e;
        font-weight: 600;
        margin-top: 25px;
    }
    
    /* 📊 METRIC CARDS - NOCH SCHÖNER */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border: none;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border-left: 5px solid #667eea;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    /* 📝 TEXT CONTAINER STYLING */
    .stMarkdown {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
    }
    
    /* 🔄 PROGRESS BAR STYLING */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* 📦 HAUPT CONTAINER */
    .block-container {
        padding-top: 3rem;
        max-width: 1200px;
    }
    
    /* 🎪 EXPANDER STYLING - MODERN */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 12px;
        border: none;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin: 10px 0;
        padding: 20px;
    }
    
    .streamlit-expanderContent {
        background: white;
        border-radius: 0 0 12px 12px;
        padding: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    /* 📱 MOBILE OPTIMIERUNG */
    @media (max-width: 768px) {
        .stButton > button {
            padding: 16px 20px;
            font-size: 15px;
        }
        
        h1 {
            font-size: 2em;
        }
    }
    
    /* 🌈 FARBIGE INFO-BOXEN - UPGRADED */
    .info-box {
        background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%);
        border-left: 5px solid #3498db;
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 6px 20px rgba(52, 152, 219, 0.2);
    }
    
    .success-box {
        background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%);
        border-left: 5px solid #27ae60;
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 6px 20px rgba(39, 174, 96, 0.2);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%);
        border-left: 5px solid #f39c12;
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 6px 20px rgba(243, 156, 18, 0.2);
    }
    
    /* 🔥 BESONDERE ELEMENTE */
    
    /* Radio Buttons stylen */
    .stRadio > div {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    /* Selectbox stylen */
    .stSelectbox > div > div {
        background: white;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    /* Custom Divider */
    .custom-divider {
        height: 3px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border: none;
        margin: 30px 0;
        border-radius: 3px;
    }
    
    /* DIMENSION CARDS */
    .dimension-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin: 25px 0;
    }
    
    .dimension-card {
        padding: 15px;
        border-radius: 12px;
        border-left: 4px solid;
        color: #2c3e50;
    }
    
    .dimension-openness {
        background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%);
        border-left-color: #3498db;
    }
    
    .dimension-conscientiousness {
        background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%);
        border-left-color: #27ae60;
    }
    
    .dimension-extraversion {
        background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%);
        border-left-color: #f39c12;
    }
    
    .dimension-agreeableness {
        background: linear-gradient(135deg, #fde8e8 0%, #f9d6d6 100%);
        border-left-color: #e74c3c;
    }
    
    .dimension-neuroticism {
        background: linear-gradient(135deg, #f3e8fd 0%, #e9d6fd 100%);
        border-left-color: #9b59b6;
        grid-column: 1 / -1;
    }
</style>
"""

st.markdown(css_styles, unsafe_allow_html=True)

class BigFiveApp:
    def __init__(self):
        self.screener = PersonalityScreener()
        self.training = TrainingModule()
        self.quiz = QuizModule()
        self.recommendations = RecommendationEngine()
        
        # Session State initialisieren
        if 'scores' not in st.session_state:
            st.session_state.scores = None
        if 'profile' not in st.session_state:
            st.session_state.profile = None
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "overview"
    
    def run(self):
        """Hauptanwendung"""
        st.title("🧠 Big Five Personality Analyzer")
        st.markdown("""
        Eine umfassende Anwendung zur Persönlichkeitsanalyse basierend auf dem wissenschaftlich 
        validierten Fünf-Faktoren-Modell (Big Five / NEO-PI-R).
        """)
        
        # Navigation über Session State
        if st.session_state.current_page == "overview":
            self.show_overview()
        elif st.session_state.current_page == "screening":
            self.show_screening()
        elif st.session_state.current_page == "training":
            self.show_training()
        elif st.session_state.current_page == "quiz":
            self.show_quiz()
        elif st.session_state.current_page == "recommendations":
            self.show_recommendations()
        elif st.session_state.current_page == "about":
            self.show_about()
    
    def show_overview(self):
        """Startseite mit Überblick und Navigation"""
        
        # 📊 INFO CARDS
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h3 style="color: #2c3e50; margin-top: 0; border-bottom: 2px solid #667eea; padding-bottom: 10px;">Was sind die Big Five?</h3>
            <p>Das <strong>Fünf-Faktoren-Modell</strong> ist das international anerkannte Standardmodell 
            in der Persönlichkeitsforschung mit über 3.000 wissenschaftlichen Studien.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Dimension Cards mit CSS-Klassen
        st.markdown("""
        <div class="dimension-grid">
            <div class="dimension-card dimension-openness">
                <strong>Offenheit</strong><br>Kreativität & Neugier
            </div>
            <div class="dimension-card dimension-conscientiousness">
                <strong>Gewissenhaftigkeit</strong><br>Ordnung & Zuverlässigkeit
            </div>
            <div class="dimension-card dimension-extraversion">
                <strong>Extraversion</strong><br>Geselligkeit & Energie
            </div>
            <div class="dimension-card dimension-agreeableness">
                <strong>Verträglichkeit</strong><br>Kooperation & Mitgefühl
            </div>
            <div class="dimension-card dimension-neuroticism">
                <strong>Neurotizismus</strong><br>Emotionale Stabilität
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 🎮 NAVIGATION MIT CUSTOM DIVIDER
        st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
        st.subheader("App Navigation")
        st.markdown("<p style='color: #5d6d7e; font-size: 1.1em; text-align: center;'>Wählen Sie einen Bereich um zu starten</p>", unsafe_allow_html=True)
        
        # Erste Button-Reihe
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("**Screening starten**", use_container_width=True, 
                        help="30 oder 60 Fragen - Ihr persönliches Big Five Profil"):
                st.session_state.current_page = "screening"
                st.rerun()
        
        with col2:
            if st.button("**Training & Wissen**", use_container_width=True, 
                        help="Lernen Sie alles über die Big Five Dimensionen"):
                st.session_state.current_page = "training"
                st.rerun()
        
        with col3:
            if st.button("**Quiz & Test**", use_container_width=True, 
                        help="Testen Sie Ihr Wissen über Persönlichkeitspsychologie"):
                st.session_state.current_page = "quiz"
                st.rerun()
        
        # Zweite Button-Reihe
        col4, col5, col6 = st.columns(3)
        
        with col4:
            button_disabled = st.session_state.scores is None
            if st.button("**Meine Empfehlungen**", 
                        disabled=button_disabled,
                        use_container_width=True, 
                        help="Evidenzbasierte Entwicklungsempfehlungen" if not button_disabled else "Bitte zuerst Screening durchführen"):
                if not button_disabled:
                    st.session_state.current_page = "recommendations"
                    st.rerun()
        
        with col5:
            if st.button("**Über die App**", use_container_width=True, 
                        help="Informationen zur wissenschaftlichen Grundlage"):
                st.session_state.current_page = "about"
                st.rerun()
        
        with col6:
            if st.button("**Startseite**", use_container_width=True, 
                        help="Zurück zur Übersicht"):
                st.session_state.current_page = "overview"
                st.rerun()
        
        # Status-Anzeige wenn Screening bereits durchgeführt
        if st.session_state.scores is not None:
            st.markdown("""
            <div class="success-box">
                <strong>Sie haben bereits ein Screening abgeschlossen!</strong><br>
                Besuchen Sie die <strong>Empfehlungen</strong> für personalisiertes Feedback.
            </div>
            """, unsafe_allow_html=True)
            
            # Mini-Ergebnisvorschau
            st.subheader("Ihr aktuelles Profil")
            cols = st.columns(5)
            dimension_names = {
                'O': 'Offenheit', 'C': 'Gewissenhaftigkeit', 'E': 'Extraversion',
                'A': 'Verträglichkeit', 'N': 'Neurotizismus'
            }
            
            for i, (dim, score) in enumerate(st.session_state.scores.items()):
                with cols[i]:
                    level = st.session_state.profile[dim]
                    st.metric(
                        label=dimension_names[dim],
                        value=f"{score:.0f}",
                        delta=level.capitalize()
                    )

    def show_screening(self):
        """Screening-Seite"""
        if st.button("← Zurück zur Übersicht"):
            st.session_state.current_page = "overview"
            st.rerun()
            
        st.header("Persönlichkeitsscreening")
        
        # Wenn bereits Ergebnisse vorhanden sind, diese zuerst anzeigen
        if st.session_state.scores is not None:
            self.show_screening_results(st.session_state.scores, st.session_state.profile)
            return
        
        screening_method = st.radio(
            "Wählen Sie eine Screening-Methode:",
            ["Schnelles Screening (30 Fragen)", "Ausführlicher Fragebogen (60 Fragen)"],
            horizontal=True
        )
        
        if screening_method == "Schnelles Screening (30 Fragen)":
            scores = self.screener.quick_screening()
        else:
            scores = self.screener.behavioral_questionnaire()
        
        # Ergebnisse anzeigen wenn scores vorhanden
        if scores is not None:
            profile = self.screener.classify_profile(scores)
            st.session_state.scores = scores
            st.session_state.profile = profile
            self.show_screening_results(scores, profile)
    
    def show_screening_results(self, scores, profile):
        """Zeigt die Screening-Ergebnisse"""
        st.markdown("""
        <div class="success-box">
            <strong>Auswertung abgeschlossen!</strong> Ihr persönliches Big Five Profil wurde erstellt.
        </div>
        """, unsafe_allow_html=True)
        
        # Radar-Diagramm
        fig = self.screener.create_radar_chart(scores)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Radar-Diagramm konnte nicht erstellt werden.")
        
        # Detaillierte Ergebnisse
        st.subheader("Detaillierte Auswertung")
        
        cols = st.columns(5)
        dimension_names = {
            'O': 'Offenheit', 'C': 'Gewissenhaftigkeit', 'E': 'Extraversion',
            'A': 'Verträglichkeit', 'N': 'Neurotizismus'
        }
        
        for i, (dim, score) in enumerate(scores.items()):
            with cols[i]:
                level = profile[dim]
                color = "🟢" if level == "hoch" and dim != "N" else "🔴" if level == "niedrig" and dim != "N" else "🟡"
                st.metric(
                    label=dimension_names[dim],
                    value=f"{score:.0f}",
                    delta=level.capitalize()
                )
                st.write(f"{color} {level}")
        
        # Ähnlichkeitsanalyse
        st.subheader("Ähnlichkeitsanalyse")
        similarities = self.screener.calculate_similarity(scores)
        
        if similarities:
            similarity_df = pd.DataFrame(
                list(similarities.items()),
                columns=['Profiltyp', 'Ähnlichkeit (%)']
            )
            
            fig = px.bar(
                similarity_df,
                x='Ähnlichkeit (%)',
                y='Profiltyp',
                orientation='h',
                title="Ähnlichkeit mit typischen Profilen"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Nächste Schritte
        st.markdown("""
        <div class="info-box">
            <strong>Nächste Schritte:</strong><br>
            • Besuchen Sie das <strong>Training</strong>-Modul, um mehr über die Big Five zu lernen<br>
            • Testen Sie Ihr Wissen im <strong>Quiz</strong><br>
            • Holen Sie sich <strong>personalisiertes Feedback</strong> im Empfehlungs-Modul
        </div>
        """, unsafe_allow_html=True)
        
        # Reset Button
        if st.button("🔄 Neues Screening starten"):
            st.session_state.scores = None
            st.session_state.profile = None
            st.rerun()

    def show_training(self):
        """Training-Seite"""
        if st.button("← Zurück zur Übersicht"):
            st.session_state.current_page = "overview"
            st.rerun()
            
        st.header("Big Five Training")
        
        training_topic = st.selectbox(
            "Wählen Sie ein Thema:",
            [
                "📖 Überblick - Grundlagen & Dimensionen",
                "🧬 Wissenschaft - Genetik & Veränderbarkeit",
                "🧩 Methodik - Aufbau & Messung", 
                "🎓 Anwendung - Beruf & Forschung",
                "⚖️ Reflexion - Kritik & Grenzen",
                "💡 Fazit - Zusammenfassung & Umsetzung"
            ]
        )
        
        # Training-Module aufrufen
        if training_topic == "📖 Überblick - Grundlagen & Dimensionen":
            self.training.show_model_overview()
        elif training_topic == "🧬 Wissenschaft - Genetik & Veränderbarkeit":
            self.training.show_nature_nurture()
        elif training_topic == "🧩 Methodik - Aufbau & Messung":
            self.training.show_structure_measurement()
        elif training_topic == "🎓 Anwendung - Beruf & Forschung":
            self.training.show_application_science()
        elif training_topic == "⚖️ Reflexion - Kritik & Grenzen":
            self.training.show_limitations_critique()
        elif training_topic == "💡 Fazit - Zusammenfassung & Umsetzung":
            self.training.show_conclusion()

    def show_quiz(self):
        """Quiz-Seite"""
        if st.button("← Zurück zur Übersicht"):
            st.session_state.current_page = "overview"
            st.rerun()
            
        st.header("Big Five Quiz")
        self.quiz.display_quiz()

    def show_recommendations(self):
        """Empfehlungs-Seite"""
        if st.button("← Zurück zur Übersicht"):
            st.session_state.current_page = "overview"
            st.rerun()
            
        st.header("Personalisiertes Feedback")
        
        if st.session_state.scores is None:
            st.markdown("""
            <div class="warning-box">
                <strong>Bitte führen Sie zuerst ein Screening durch</strong>, um personalisierte 
                Empfehlungen zu erhalten.
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Zum Screening gehen"):
                st.session_state.current_page = "screening"
                st.rerun()
            return
        
        # Empfehlungen generieren
        self.recommendations.generate_recommendations(
            st.session_state.profile, 
            st.session_state.scores
        )
        
        # Entwicklungsplan
        st.subheader("Persönlicher Entwicklungsplan")
        
        development_plan = self.create_development_plan(
            st.session_state.profile, 
            st.session_state.scores
        )
        
        for goal, actions in development_plan.items():
            with st.expander(f"{goal}"):
                for action in actions:
                    st.write(f"• {action}")
    
    def create_development_plan(self, profile, scores):
        """Erstellt einen persönlichen Entwicklungsplan"""
        plan = {}
        
        # Entwicklungsziele basierend auf Profil
        if profile.get('N') == 'hoch':
            plan["Emotionale Resilienz stärken"] = [
                "Praktiziere täglich 10 Minuten Achtsamkeitsmeditation",
                "Führe ein Stimmungstagebuch zur besseren Selbstwahrnehmung",
                "Lerne kognitive Umstrukturierungstechniken",
                "Entwickle gesunde Bewältigungsstrategien für Stress"
            ]
        
        if profile.get('C') == 'niedrig':
            plan["Organisation und Struktur verbessern"] = [
                "Beginne mit täglichen To-Do-Listen",
                "Nutze Kalender für Termine und Deadlines",
                "Richte feste Arbeitsroutinen ein",
                "Setze dir wöchentliche Prioritäten"
            ]
        
        if profile.get('O') == 'niedrig':
            plan["Offenheit für Neues entwickeln"] = [
                "Probiere monatlich eine neue Aktivität aus",
                "Lies Bücher ausserhalb deines gewohnten Genres",
                "Besuche kulturelle Veranstaltungen",
                "Tausche dich mit Menschen unterschiedlicher Hintergründe aus"
            ]
        
        if not plan:  # Falls kein spezifischer Entwicklungsbedarf
            plan["Persönliches Wachstum fördern"] = [
                "Reflektiere regelmässig über persönliche Stärken",
                "Setze dir herausfordernde aber realistische Ziele",
                "Suche aktiv nach Feedback von anderen",
                "Bleibe neugierig und lernbereit"
            ]
        
        return plan

    def show_about(self):
        """Über-Seite mit Informationen zur App - KORRIGIERTE VERSION"""
        if st.button("← Zurück zur Übersicht"):
            st.session_state.current_page = "overview"
            st.rerun()
            
        st.header("Über diese Anwendung")
        
        st.markdown("### Wissenschaftliche Grundlage")
        st.markdown("""
        Diese Anwendung basiert auf dem **Fünf-Faktoren-Modell** (Big Five), 
        dem international anerkannten Standardmodell der Persönlichkeitsforschung.
        """)
        
        st.markdown("""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 12px; margin: 20px 0;">
            <strong>Wichtige Quellen:</strong><br>
            • Costa, P. T., & McCrae, R. R. (1992). NEO-PI-R Professional Manual<br>
            • Goldberg, L. R. (1993). The structure of phenotypic personality traits<br>
            • John, O. P., & Srivastava, S. (1999). The Big Five trait taxonomy
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Technische Umsetzung")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); padding: 15px; border-radius: 10px;">
                <strong>Funktionen:</strong><br>
                • Screening mit Fragebögen<br>
                • Profilanalyse<br>
                • Wissenschaftliches Training<br>
                • Personalisierte Empfehlungen
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%); padding: 15px; border-radius: 10px;">
                <strong>Hinweis:</strong><br>
                Diese Anwendung dient Bildungszwecken und ersetzt keine professionelle psychologische Beratung.
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### Entwickler")
        st.markdown("""
        Diese Streamlit-Anwendung wurde entwickelt, um das Big-five-Modell 
        zugänglich und anwendbar zu machen.
        """)

# Hauptanwendung ausführen
if __name__ == "__main__":
    app = BigFiveApp()
    app.run()
