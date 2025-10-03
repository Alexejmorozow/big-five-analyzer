import streamlit as st
import pandas as pd
import plotly.express as px
from modules.screening import PersonalityScreener
from modules.training import TrainingModule
from modules.quiz import QuizModule
from modules.recommendations import RecommendationEngine

# Streamlit Konfiguration
st.set_page_config(
    page_title="Big Five Personality Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    
    def run(self):
        """Hauptanwendung"""
        st.title("🧠 Big Five Personality Analyzer")
        st.markdown("""
        Eine umfassende Anwendung zur Persönlichkeitsanalyse basierend auf dem wissenschaftlich 
        validierten Fünf-Faktoren-Modell (Big Five / NEO-PI-R).
        """)
        
        # Seitenauswahl in der Sidebar
        st.sidebar.title("Navigation")
        app_mode = st.sidebar.selectbox(
            "Wählen Sie einen Modus:",
            ["🏠 Übersicht", "🔍 Screening", "📚 Training", "❓ Quiz", "💡 Empfehlungen", "ℹ️ Über"]
        )
        
        # Seiten basierend auf Auswahl anzeigen
        if app_mode == "🏠 Übersicht":
            self.show_overview()
        elif app_mode == "🔍 Screening":
            self.show_screening()
        elif app_mode == "📚 Training":
            self.show_training()
        elif app_mode == "❓ Quiz":
            self.show_quiz()
        elif app_mode == "💡 Empfehlungen":
            self.show_recommendations()
        elif app_mode == "ℹ️ Über":
            self.show_about()
    
    def show_overview(self):
        """Startseite mit Überblick"""
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
        
        # Schnellstart-Bereich
        st.subheader("Schnellstart")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎯 Schnelles Screening starten", use_container_width=True):
                st.session_state.app_mode = "🔍 Screening"
                st.rerun()
        
        with col2:
            if st.button("📚 Training beginnen", use_container_width=True):
                st.session_state.app_mode = "📚 Training"
                st.rerun()
        
        with col3:
            if st.button("❓ Quiz testen", use_container_width=True):
                st.session_state.app_mode = "❓ Quiz"
                st.rerun()
    
    def show_screening(self):
        """Screening-Seite"""
        st.header("Persönlichkeitsscreening")
        
        screening_method = st.radio(
            "Wählen Sie eine Screening-Methode:",
            ["Schnelles Screening (10 Fragen)", "Ausführlicher Fragebogen (30 Fragen)"],
            horizontal=True
        )
        
        if screening_method == "Schnelles Screening (10 Fragen)":
            scores = self.screener.quick_screening()
        else:
            scores = self.screener.behavioral_questionnaire()
        
        if st.button("Auswerten", type="primary"):
            # Profil klassifizieren
            profile = self.screener.classify_profile(scores)
            st.session_state.scores = scores
            st.session_state.profile = profile
            
            # Ergebnisse anzeigen
            self.show_screening_results(scores, profile)
    
    def show_screening_results(self, scores, profile):
        """Zeigt die Screening-Ergebnisse"""
        st.success("🎉 Auswertung abgeschlossen!")
        
        # Radar-Diagramm
        fig = self.screener.create_radar_chart(scores)
        st.plotly_chart(fig, use_container_width=True)
        
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
    
    def show_training(self):
        """Training-Seite"""
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
        self.quiz.display_quiz()
    
    def show_recommendations(self):
        """Empfehlungs-Seite"""
        st.header("Personalisiertes Feedback")
        
        if st.session_state.scores is None:
            st.warning("""
            ⚠️ Bitte führen Sie zuerst ein Screening durch, um personalisierte 
            Empfehlungen zu erhalten.
            """)
            
            if st.button("Zum Screening gehen"):
                st.session_state.app_mode = "🔍 Screening"
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
        
        Diese Streamlit-Anwendung wurde entwickelt, um das Big-Five-Modell 
        zugänglich und anwendbar zu machen.
        """)

# Hauptanwendung ausführen
if __name__ == "__main__":
    app = BigFiveApp()
    app.run()
