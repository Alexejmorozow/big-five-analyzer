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

# 🎨 MODERNES CSS STYLING - KORRIGIERTE VERSION
css_styles = """
<style>
    /* Haupt-Hintergrund */
    .main {
        background-color: #f8f9fa;
    }
    
    /* 📱 MODERNE BUTTONS */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 25px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px 0 rgba(0,0,0,0.1);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(0,0,0,0.15);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* 🎯 HEADER STYLING */
    h1 {
        color: #2c3e50;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
        font-weight: 700;
    }
    
    h2 {
        color: #34495e;
        margin-top: 25px !important;
        font-weight: 600;
    }
    
    h3 {
        color: #5d6d7e;
        font-weight: 600;
    }
    
    /* 📊 METRIC CARDS - Schöner gemacht */
    [data-testid="metric-container"] {
        background: white;
        border: 1px solid #e1e8ed;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        transition: transform 0.2s ease;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.12);
    }
    
    /* 📝 TEXT STYLING */
    .stMarkdown {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* 🔄 PROGRESS BAR */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* 📦 CONTAINER STYLING */
    .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }
    
    /* 🎪 EXPANDER STYLING */
    .streamlit-expanderHeader {
        background-color: #f8f9fa;
        border-radius: 8px;
        border: 1px solid #e1e8ed;
        font-weight: 600;
    }
    
    /* 📱 MOBILE OPTIMIERUNG */
    @media (max-width: 768px) {
        .stButton > button {
            padding: 12px 20px;
            font-size: 14px;
        }
    }
    
    /* 🌈 FARBIGE INFO-BOXEN */
    .info-box {
        background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%);
        border-left: 5px solid #3498db;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .success-box {
        background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%);
        border-left: 5px solid #27ae60;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%);
        border-left: 5px solid #f39c12;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
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
        st.header("Willkommen beim Big Five Personality Analyzer")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### Was sind die Big Five?
            
            Das **Fünf-Faktoren-Modell** (Big Five) ist das international anerkannte Standardmodell 
            in der Persönlichkeitsforschung. Es beschreibt die menschliche Persönlichkeit anhand 
            von fünf Hauptdimensionen:
            
            - **O**ffenheit für Erfahrungen
            - **G**ewissenhaftigkeit  
            - **E**xtraversion
            - **V**erträglichkeit
            - **N**eurotizismus
            
            ### Wissenschaftliche Grundlage
            
            - Basierend auf dem lexikalischen Ansatz
            - Über 3.000 wissenschaftliche Studien
            - 40-60% genetische Komponente
            - Kulturübergreifend validiert
            """)
        
        with col2:
            st.image("https://via.placeholder.com/300x200/4B7BEC/FFFFFF?text=Big+Five+Model", 
                    caption="Das OCEAN-Modell der Persönlichkeit")
            
            st.info("""
            **Funktionen:**
            - 🔍 Persönlichkeitsscreening
            - 📚 Wissenschaftliches Training  
            - ❓ Interaktives Quiz
            - 💡 Personalisierte Empfehlungen
            """)
        
        # Navigation über Buttons
        st.markdown("---")
        st.subheader("🚀 Starten Sie hier")
        
        # Erste Button-Reihe
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("**🔍 Screening starten**", use_container_width=True, 
                        help="30 oder 60 Fragen - Ihr persönliches Big Five Profil"):
                st.session_state.current_page = "screening"
                st.rerun()
        
        with col2:
            if st.button("**📚 Training & Wissen**", use_container_width=True, 
                        help="Lernen Sie alles über die Big Five Dimensionen"):
                st.session_state.current_page = "training"
                st.rerun()
        
        with col3:
            if st.button("**❓ Quiz & Test**", use_container_width=True, 
                        help="Testen Sie Ihr Wissen über Persönlichkeitspsychologie"):
                st.session_state.current_page = "quiz"
                st.rerun()
        
        # Zweite Button-Reihe
        col4, col5, col6 = st.columns(3)
        
        with col4:
            button_disabled = st.session_state.scores is None
            if st.button("**💡 Meine Empfehlungen**", 
                        disabled=button_disabled,
                        use_container_width=True, 
                        help="Evidenzbasierte Entwicklungsempfehlungen" if not button_disabled else "Bitte zuerst Screening durchführen"):
                if not button_disabled:
                    st.session_state.current_page = "recommendations"
                    st.rerun()
        
        with col5:
            if st.button("**ℹ️ Über die App**", use_container_width=True, 
                        help="Informationen zur wissenschaftlichen Grundlage"):
                st.session_state.current_page = "about"
                st.rerun()
        
        with col6:
            if st.button("**🔄 Zurück zur Startseite**", use_container_width=True, 
                        help="Zurück zur Übersicht"):
                st.session_state.current_page = "overview"
                st.rerun()
        
        # Status-Anzeige wenn Screening bereits durchgeführt
        if st.session_state.scores is not None:
            st.success("""
            🎉 **Sie haben bereits ein Screening abgeschlossen!**
            Besuchen Sie die **Empfehlungen** für personalisiertes Feedback.
            """)
            
            # Mini-Ergebnisvorschau
            st.subheader("📊 Ihr aktuelles Profil")
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
        # Zurück-Button
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
        st.success("🎉 Auswertung abgeschlossen!")
        
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
        st.info("""
        **Nächste Schritte:**
        - Besuchen Sie das **Training**-Modul, um mehr über die Big Five zu lernen
        - Testen Sie Ihr Wissen im **Quiz**
        - Holen Sie sich **personalisiertes Feedback** im Empfehlungs-Modul
        """)
        
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
                "Überblick über das Big-Five-Modell",
                "Offenheit für Erfahrungen", 
                "Gewissenhaftigkeit",
                "Extraversion",
                "Verträglichkeit", 
                "Neurotizismus",
                "Wissenschaftliche Grundlagen",
                "Hierarchische Struktur"
            ]
        )
        
        if training_topic == "Überblick über das Big-Five-Modell":
            self.show_model_overview()
        elif training_topic == "Offenheit für Erfahrungen":
            self.training.show_dimension_details('O')
        elif training_topic == "Gewissenhaftigkeit":
            self.training.show_dimension_details('C')
        elif training_topic == "Extraversion":
            self.training.show_dimension_details('E')
        elif training_topic == "Verträglichkeit":
            self.training.show_dimension_details('A')
        elif training_topic == "Neurotizismus":
            self.training.show_dimension_details('N')
        elif training_topic == "Wissenschaftliche Grundlagen":
            self.training.show_genetic_information()
        elif training_topic == "Hierarchische Struktur":
            self.training.show_hierarchical_structure()
    
    def show_model_overview(self):
        """Zeigt einen Überblick über das Big-Five-Modell"""
        st.markdown("""
        ## Das Fünf-Faktoren-Modell (Big Five)
        
        ### Historische Entwicklung
        
        Das Big-Five-Modell entwickelte sich aus dem **lexikalischen Ansatz**, der besagt, 
        dass alle wichtigen Persönlichkeitsmerkmale in der natürlichen Sprache kodiert sind.
        
        **Wichtige Meilensteine:**
        - 1936: Allport & Odbert identifizieren 18.000 Persönlichkeitsbegriffe
        - 1960er: Cattell reduziert auf 16 Faktoren
        - 1980er: Fünf stabile Faktoren werden international bestätigt
        - 1990er: NEO-PI-R etabliert standardisiertes Messinstrument
        
        ### Die fünf Dimensionen
        """)
        
        dimensions_info = {
            'O': {
                'name': 'Offenheit für Erfahrungen',
                'description': 'Beschreibt die Offenheit für neue Erfahrungen, Kreativität und intellektuelle Neugier',
                'high': 'Kreativ, neugierig, vielseitig',
                'low': 'Praktisch, konventionell, traditionell'
            },
            'C': {
                'name': 'Gewissenhaftigkeit', 
                'description': 'Bezieht sich auf Organisation, Zuverlässigkeit und Zielstrebigkeit',
                'high': 'Organisiert, verantwortungsbewusst, zuverlässig',
                'low': 'Spontan, flexibel, ungezwungen'
            },
            'E': {
                'name': 'Extraversion',
                'description': 'Beschreibt Geselligkeit, Energie und positive Emotionalität',
                'high': 'Gesellig, energisch, gesprächig',
                'low': 'Zurückhaltend, ruhig, reserviert'
            },
            'A': {
                'name': 'Verträglichkeit',
                'description': 'Bezieht sich auf Mitgefühl, Kooperationsbereitschaft und Vertrauen',
                'high': 'Hilfsbereit, vertrauensvoll, mitfühlend',
                'low': 'Skeptisch, wettbewerbsorientiert, direkt'
            },
            'N': {
                'name': 'Neurotizismus',
                'description': 'Beschreibt emotionale Stabilität und Anfälligkeit für negative Emotionen',
                'high': 'Emotional, sensibel, besorgt',
                'low': 'Gelassen, emotional stabil, resilient'
            }
        }
        
        for dim, info in dimensions_info.items():
            with st.expander(f"{info['name']} ({dim})"):
                st.write(f"**Beschreibung:** {info['description']}")
                col1, col2 = st.columns(2)
                with col1:
                    st.success(f"**Hohe Ausprägung:** {info['high']}")
                with col2:
                    st.info(f"**Niedrige Ausprägung:** {info['low']}")

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
            st.warning("""
            ⚠️ Bitte führen Sie zuerst ein Screening durch, um personalisierte 
            Empfehlungen zu erhalten.
            """)
            
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
            with st.expander(f"🎯 {goal}"):
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
                "Lies Bücher außerhalb deines gewohnten Genres",
                "Besuche kulturelle Veranstaltungen",
                "Tausche dich mit Menschen unterschiedlicher Hintergründe aus"
            ]
        
        if not plan:  # Falls kein spezifischer Entwicklungsbedarf
            plan["Persönliches Wachstum fördern"] = [
                "Reflektiere regelmäßig über persönliche Stärken",
                "Setze dir herausfordernde aber realistische Ziele",
                "Suche aktiv nach Feedback von anderen",
                "Bleibe neugierig und lernbereit"
            ]
        
        return plan

    def show_about(self):
        """Über-Seite mit Informationen zur App"""
        if st.button("← Zurück zur Übersicht"):
            st.session_state.current_page = "overview"
            st.rerun()
            
        st.header("Über diese Anwendung")
        
        st.markdown("""
        ### Wissenschaftliche Grundlage
        
        Diese Anwendung basiert auf dem **Fünf-Faktoren-Modell** (Big Five), 
        dem international anerkannten Standardmodell der Persönlichkeitsforschung.
        
        **Wichtige Quellen:**
        - Costa, P. T., & McCrae, R. R. (1992). NEO-PI-R Professional Manual
        - Goldberg, L. R. (1993). The structure of phenotypic personality traits
        - John, O. P., & Srivastava, S. (1999). The Big Five trait taxonomy
        
        ### Technische Umsetzung
        
        **Funktionen:**
        - Screening mit verhaltensbasierten Fragebögen
        - ML-gestützte Profilanalyse
        - Wissenschaftlich fundiertes Training
        - Interaktive Wissensüberprüfung
        - Personalisierte Handlungsempfehlungen
        
        **Hinweis:** Diese Anwendung dient Bildungszwecken und ersetzt keine 
        professionelle psychologische Beratung.
        
        ### Entwickler
        
        Diese Streamlit-Anwendung wurde entwickelt, um das Big-five-Modell 
        zugänglich und anwendbar zu machen.
        """)

# Hauptanwendung ausführen
if __name__ == "__main__":
    app = BigFiveApp()
    app.run()
