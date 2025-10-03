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
    initial_sidebar_state="collapsed"  # Sidebar standardmäßig geschlossen
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
        if 'current_page' not in st.session_state:  # Vereinfachte Navigation
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
        
        # Navigation über Buttons - Vereinfacht
        st.markdown("---")
        st.subheader("🚀 Starten Sie hier")
        
        # Erste Button-Reihe
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("**🔍 Screening starten**", use_container_width=True, help="30 oder 60 Fragen - Ihr persönliches Big Five Profil"):
                st.session_state.current_page = "screening"
                st.experimental_rerun()
        
        with col2:
            if st.button("**📚 Training & Wissen**", use_container_width=True, help="Lernen Sie alles über die Big Five Dimensionen"):
                st.session_state.current_page = "training"
                st.experimental_rerun()
        
        with col3:
            if st.button("**❓ Quiz & Test**", use_container_width=True, help="Testen Sie Ihr Wissen über Persönlichkeitspsychologie"):
                st.session_state.current_page = "quiz"
                st.experimental_rerun()
        
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
                    st.experimental_rerun()
        
        with col5:
            if st.button("**ℹ️ Über die App**", use_container_width=True, help="Informationen zur wissenschaftlichen Grundlage"):
                st.session_state.current_page = "about"
                st.experimental_rerun()
        
        with col6:
            if st.button("**🔄 Zurück zur Startseite**", use_container_width=True, help="Zurück zur Übersicht"):
                st.session_state.current_page = "overview"
                st.experimental_rerun()
        
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

    # Die restlichen Methoden (show_screening, show_training, etc.) bleiben gleich
    def show_screening(self):
        """Screening-Seite"""
        # Zurück-Button
        if st.button("← Zurück zur Übersicht"):
            st.session_state.current_page = "overview"
            st.experimental_rerun()
            
        st.header("Persönlichkeitsscreening")
        
        # Rest der bestehenden Screening-Logik hier...
        # [Ihr bestehender Screening-Code]

# Hauptanwendung ausführen
if __name__ == "__main__":
    app = BigFiveApp()
    app.run()
