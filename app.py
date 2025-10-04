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
    
    /* SCHNELLSTART CARDS */
    .quickstart-card {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        border-left: 4px solid #667eea;
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
        """Startseite mit Überblick und Navigation - KORRIGIERT"""
        
        # 📊 INFO CARDS IN ZWEI SPALTEN
        col1, col2 = st.columns([2, 1])
        
        with col1:
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
        
        with col2:
            # Schnellstart-Bereich - KORRIGIERT
            st.markdown("""
            <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); height: 100%;">
                <h3 style="color: #2c3e50; margin-top: 0; border-bottom: 2px solid #667eea; padding-bottom: 10px;">Schnellstart</h3>
                <p style="color: #5d6d7e;">Wählen Sie eine Funktion um zu starten:</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Schnellstart-Optionen mit korrektem HTML
            st.markdown("""
            <div class="quickstart-card">
                <strong>Screening</strong><br>Ihr Persönlichkeitsprofil
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="quickstart-card">
                <strong>Training</strong><br>Wissenschaftliche Grundlagen
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="quickstart-card">
                <strong>Empfehlungen</strong><br>Personalisierte Tipps
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
        """Training-Seite - OPTIMIERT & REDUZIERT"""
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
        
        if training_topic == "📖 Überblick - Grundlagen & Dimensionen":
            self.show_model_overview()
        elif training_topic == "🧬 Wissenschaft - Genetik & Veränderbarkeit":
            self.show_nature_nurture()
        elif training_topic == "🧩 Methodik - Aufbau & Messung":
            self.show_structure_measurement()
        elif training_topic == "🎓 Anwendung - Beruf & Forschung":
            self.show_application_science()
        elif training_topic == "⚖️ Reflexion - Kritik & Grenzen":
            self.show_limitations_critique()
        elif training_topic == "💡 Fazit - Zusammenfassung & Umsetzung":
            self.show_conclusion()

    def show_model_overview(self):
        """Zeigt einen Überblick über das Big-Five-Modell - KORRIGIERT"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">📖 Überblick - Grundlagen & Dimensionen</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Historische Entwicklung
        st.markdown("### Historische Entwicklung")
        st.markdown("""
        Die Big Five basieren auf dem sogenannten lexikalischen Ansatz. 
        Dieser geht davon aus, dass sich alle wichtigen Merkmale menschlicher Persönlichkeit in der Sprache niedergeschlagen haben.
        Bereits in den 1930er-Jahren identifizierten Allport und Odbert über 18'000 persönlichkeitsrelevante Begriffe. 
        Durch statistische Analysen (Faktorenanalysen) kristallisierten sich daraus die fünf stabilen Dimensionen heraus, die kulturübergreifend bestätigt wurden.
        """)
        
        st.markdown("""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 12px; margin: 20px 0;">
            <strong>Wichtige Meilensteine:</strong><br>
            • 1936: Allport & Odbert identifizieren 18.000 Persönlichkeitsbegriffe<br>
            • 1960er: Cattell reduziert auf 16 Faktoren<br>
            • 1980er: Fünf stabile Faktoren werden international bestätigt<br>
            • 1990er: NEO-PI-R etabliert standardisiertes Messinstrument
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Die fünf Dimensionen")
        
        dimensions_info = {
            'O': {
                'name': 'Offenheit für Erfahrungen',
                'description': 'Offene Menschen sind neugierig, kreativ, fantasievoll und interessieren sich für Kunst, Philosophie oder neue Ideen. Sie hinterfragen Konventionen, suchen Abwechslung und zeigen eine hohe intellektuelle Neugier. Wenig offene Menschen bevorzugen hingegen Stabilität, Routinen und Bekanntes. Hohe Offenheit steht in der modernen Arbeitswelt mit Innovationsfähigkeit, Lernbereitschaft und kognitiver Flexibilität in Verbindung',
                'high': 'Kreativ, neugierig, vielseitig',
                'low': 'Praktisch, konventionell, traditionell'
            },
            'C': {
                'name': 'Gewissenhaftigkeit', 
                'description': 'Dieser Faktor beschreibt Zielstrebigkeit, Organisation und Verantwortungsbewusstsein. Menschen mit hoher Gewissenhaftigkeit planen ihren Tag sorgfältig, handeln überlegt, dokumentieren gewissenhaft und verfolgen ihre Ziele diszipliniert. Forschungsergebnisse zeigen, dass Gewissenhaftigkeit der beste Prädiktor für beruflichen und akademischen Erfolg ist – über alle Branchen hinweg. Sie wirkt sich zudem positiv auf die Gesundheit und Lebenszufriedenheit aus',
                'high': 'Organisiert, verantwortungsbewusst, zuverlässig',
                'low': 'Spontan, flexibel, ungezwungen'
            },
            'E': {
                'name': 'Extraversion',
                'description': 'Extravertierte Personen sind gesellig, aktiv, kontaktfreudig und energiegeladen. Sie initiieren Gespräche, fühlen sich in Gruppen wohl und suchen den Austausch. Introvertierte Personen sind dagegen eher zurückhaltend, beobachtend und ruhig, was jedoch keineswegs mit Schüchternheit gleichzusetzen ist. Je nach Situation können beide Ausprägungen Vorteile bieten.',
                'high': 'Gesellig, energisch, gesprächig',
                'low': 'Zurückhaltend, ruhig, reserviert'
            },
            'A': {
                'name': 'Verträglichkeit',
                'description': 'Verträgliche Menschen sind hilfsbereit, mitfühlend und kooperativ. Sie vermeiden Konflikte, zeigen Altruismus und handeln rücksichtsvoll. Eine geringe Verträglichkeit hingegen steht für Durchsetzungsfähigkeit und Wettbewerbsorientierung – Eigenschaften, die in hierarchischen oder leistungsorientierten Umfeldern vorteilhaft sein können. Studien zeigen jedoch, dass übermässige Freundlichkeit zu einer „Karrierebremse" werden kann: Sie erhöht zwar die Zufriedenheit, kann aber den objektiven Erfolg (z. B. Einkommen oder Beförderung) mindern',
                'high': 'Hilfsbereit, vertrauensvoll, mitfühlend',
                'low': 'Skeptisch, wettbewerbsorientiert, direkt'
            },
            'N': {
                'name': 'Neurotizismus',
                'description': 'Diese Dimension beschreibt die Anfälligkeit für negative Emotionen wie Angst, Nervosität oder Unsicherheit. Ein hoher Neurotizismus geht oft mit emotionaler Labilität und Stressanfälligkeit einher, während ein niedriger Wert auf emotionale Stabilität und Resilienz hinweist. Wichtig ist: Neurotizismus ist veränderbar. Achtsamkeitstraining, Emotionsregulation oder das Training emotionaler Kompetenzen können helfen, den Umgang mit Stress zu verbessern und innere Stabilität zu fördern. Gleichzeitig hat diese Sensibilität auch positive Seiten: Menschen mit höherem Neurotizismus nehmen Stimmungen, Spannungen und Risiken frühzeitig wahr und reflektieren ihr eigenes Verhalten oft besonders gründlich. Ihre emotionale Tiefe kann zu hoher Empathie, Verantwortlichkeit und kreativer Ausdruckskraft führen – vorausgesetzt, sie lernen, mit ihrer inneren Intensität bewusst umzugehen.',
                'high': 'Emotional, sensibel, besorgt',
                'low': 'Gelassen, emotional stabil, resilient'
            }
        }
        
        for dim, info in dimensions_info.items():
            with st.expander(f"{info['name']} ({dim})"):
                st.write(f"**Beschreibung:** {info['description']}")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%); 
                                padding: 15px; border-radius: 10px; border-left: 4px solid #27ae60;">
                        <strong>Hohe Ausprägung:</strong><br>{info['high']}
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); 
                                padding: 15px; border-radius: 10px; border-left: 4px solid #3498db;">
                        <strong>Niedrige Ausprägung:</strong><br>{info['low']}
                    </div>
                    """, unsafe_allow_html=True)

    def show_nature_nurture(self):
        """Anlage, Umwelt und Veränderbarkeit - KORRIGIERT"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">🧬 Wissenschaft - Genetik & Veränderbarkeit</h2>
            
            <p>Persönlichkeitsmerkmale sind teils genetisch, teils umweltbedingt.</p>
            
            <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>🔬 Wissenschaftliche Evidenz:</strong><br>
                • Zwillingsstudien zeigen, dass die Big-Five-Dimensionen zu etwa <strong>40–60 % erblich</strong> sind<br>
                • Den restlichen Anteil erklären <strong>individuelle Umwelteinflüsse</strong> – also persönliche Erfahrungen, Bildung, Freundschaften oder Lebensereignisse
            </div>
            
            <h3 style="color: #34495e;">Neuroplastizität und Veränderbarkeit</h3>
            <p>Lange galt Persönlichkeit als weitgehend stabil, doch moderne Forschung zur Neuroplastizität zeigt:</p>
            <p><strong>Unser Gehirn bleibt formbar.</strong> Neue Gewohnheiten, Denkmuster und Verhaltensweisen lassen sich durch intentionale Aktivitäten gezielt trainieren.</p>
            
            <div style="background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>💪 Praktische Konsequenz:</strong><br>
                Sie haben etwa <strong>40-50% Ihrer Persönlichkeit aktiv in der Hand</strong> und können diese durch bewusstes Training und neue Erfahrungen formen.
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_structure_measurement(self):
        """Aufbau und Messung - KORRIGIERT"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">🧩 Methodik - Aufbau & Messung</h2>
            
            <h3 style="color: #34495e;">Hierarchische Struktur</h3>
            <p>Das Big-Five-Modell ist hierarchisch aufgebaut:</p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 20px 0;">
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;">
                    <strong>5 Hauptdimensionen</strong><br>OCEAN
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;">
                    <strong>2 Aspekte pro Dimension</strong><br>z.B. Enthusiasmus & Geselligkeit
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;">
                    <strong>6 Facetten pro Dimension</strong><br>Spezifische Subskalen
                </div>
            </div>
            
            <h3 style="color: #34495e;">Wissenschaftliche Messung</h3>
            <p>Zur wissenschaftlichen Erfassung gilt das <strong>NEO-PI-R (Costa & McCrae)</strong> als Goldstandard.</p>
            <p>Es misst jede der fünf Dimensionen anhand von <strong>30 Facetten</strong> und erlaubt damit eine sehr präzise Beschreibung der Persönlichkeit.</p>
            
            <div style="background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>📊 Total Items:</strong> 240 Fragen (6 Facetten × 8 Items × 5 Dimensionen)<br>
                <strong>🎯 Genauigkeit:</strong> Hochdetaillierte Persönlichkeitsprofile
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_application_science(self):
        """Anwendung und wissenschaftliche Grundlagen - KORRIGIERT"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">🎓 Anwendung - Beruf & Forschung</h2>
            
            <h3 style="color: #34495e;">Eignungsdiagnostik</h3>
            <p>In der Eignungsdiagnostik ist die Persönlichkeit neben Intelligenz einer der wichtigsten Prädiktoren für Berufserfolg.</p>
            
            <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>📈 Validitätsbefunde:</strong><br>
                • Persönlichkeitstests zeigen eine <strong>moderate Validität (r ≈ 0.3)</strong>, insbesondere Gewissenhaftigkeit<br>
                • Die Kombination mit kognitiven Tests erhöht die Vorhersagekraft um etwa <strong>18 %</strong> – dieser Effekt wird <strong>inkrementelle Validität</strong> genannt
            </div>
            
            <h3 style="color: #34495e;">Wichtige Konzepte</h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px;">
                    <strong>📏 Bandbreiten-Fidelitäts-Dilemma</strong><br>
                    Je breiter ein Test konstruiert ist, desto weniger präzise ist er – und umgekehrt. Die Kunst wissenschaftlicher Diagnostik besteht also darin, zwischen Breite (Bandbreite) und Genauigkeit (Fidelität) das richtige Gleichgewicht zu finden.
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px;">
                    <strong>🎯 Kriteriumsvalidität</strong><br>
                    Beschreibt den Zusammenhang zwischen Testergebnissen und externen Erfolgskriterien – etwa Arbeitsleistung oder Zufriedenheit.
                </div>
            </div>
            
            <h3 style="color: #34495e;">Praktische Anwendungen</h3>
            
            <div style="background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>💼 Berufliche Anwendungsbereiche:</strong><br>
                • Personalauswahl und Recruiting<br>
                • Teamentwicklung und Teamzusammensetzung<br>
                • Karriereberatung und Laufbahnplanung<br>
                • Führungskräfteentwicklung und Coaching
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_limitations_critique(self):
        """Grenzen und Kritik - KORRIGIERT"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">⚖️ Reflexion - Kritik & Grenzen</h2>
            
            <h3 style="color: #34495e;">Inhaltliche Kritik</h3>
            <p>Der Persönlichkeitspsychologe <strong>Dan McAdams</strong> kritisiert, dass die Big Five zwar beschreiben, <em>wie</em> Menschen sind, aber nicht <em>warum</em>.</p>
            <p>Das Modell vernachlässige die Rolle von Lebenserfahrungen und situativen Einflüssen.</p>
            
            <h3 style="color: #34495e;">Methodische Probleme</h3>
            
            <div style="background: linear-gradient(135deg, #fde8e8 0%, #f9d6d6 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>⚠️ Bekannte methodische Herausforderungen:</strong><br>
                • <strong>Soziale Erwünschtheit</strong> kann Antworten verzerren<br>
                • <strong>Kulturelle Unterschiede</strong> beeinflussen Item-Interpretationen<br>
                • <strong>Selbstauskünfte</strong> spiegeln nicht immer objektive Realität wider
            </div>
            
            <div style="background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>✅ Trotzdem wissenschaftlich wertvoll:</strong><br>
                Dennoch bleibt das Modell das <strong>verlässlichste Fundament</strong> moderner Persönlichkeitsforschung, da es komplexe menschliche Unterschiede einfach, reproduzierbar und interkulturell erfassbar macht.
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_conclusion(self):
        """Fazit - KORRIGIERT"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">💡 Fazit - Zusammenfassung & Umsetzung</h2>
            
            <p>Die Big Five bieten ein <strong>wissenschaftlich fundiertes Raster</strong>, um Persönlichkeit zu verstehen und Verhalten besser zu interpretieren.</p>
            
            <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>🎯 Zentrale Erkenntnisse:</strong><br>
                • Unsere Persönlichkeit ist <strong>teils veranlagt, teils formbar</strong><br>
                • <strong>Bewusste Gewohnheiten, Reflexion und Training</strong> haben einen erheblichen Einfluss auf Erfolg und Wohlbefinden<br>
                • Wer die Dynamik zwischen Anlage, Umwelt und bewusster Veränderung versteht, kann seine persönliche Entwicklung gezielt gestalten
            </div>
            
            <h3 style="color: #34495e;">Praktische Umsetzung</h3>
            <p><strong>Wie gehen wir das am besten an?</strong></p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px;">
                    <strong>🔍 Selbstreflexion</strong><br>
                    Nutzen Sie Ihre Big-Five-Ergebnisse als Ausgangspunkt für bewusste Selbstwahrnehmung und persönliche Entwicklung.
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px;">
                    <strong>🚀 Gezieltes Training</strong><br>
                    Arbeiten Sie mit den Empfehlungen dieser App an spezifischen Entwicklungsbereichen.
                </div>
            </div>
            
            <div style="background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%); padding: 20px; border-radius: 12px; margin: 20px 0; text-align: center;">
                <strong>Ihre Persönlichkeit ist kein Schicksal – sondern eine dynamische Ressource, die Sie aktiv gestalten können.</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)

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
        """Über-Seite mit Informationen zur App"""
        if st.button("← Zurück zur Übersicht"):
            st.session_state.current_page = "overview"
            st.rerun()
            
        st.header("Über diese Anwendung")
        
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h3 style="color: #2c3e50; margin-top: 0;">Wissenschaftliche Grundlage</h3>
            
            <p>Diese Anwendung basiert auf dem <strong>Fünf-Faktoren-Modell</strong> (Big Five), 
            dem international anerkannten Standardmodell der Persönlichkeitsforschung.</p>
            
            <div style="background: #f8f9fa; padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>Wichtige Quellen:</strong><br>
                • Costa, P. T., & McCrae, R. R. (1992). NEO-PI-R Professional Manual<br>
                • Goldberg, L. R. (1993). The structure of phenotypic personality traits<br>
                • John, O. P., & Srivastava, S. (1999). The Big Five trait taxonomy
            </div>
            
            <h3 style="color: #2c3e50;">Technische Umsetzung</h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
                <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); padding: 15px; border-radius: 10px;">
                    <strong>Funktionen:</strong><br>
                    • Screening mit Fragebögen<br>
                    • Profilanalyse<br>
                    • Wissenschaftliches Training<br>
                    • Personalisierte Empfehlungen
                </div>
                <div style="background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%); padding: 15px; border-radius: 10px;">
                    <strong>Hinweis:</strong><br>
                    Diese Anwendung dient Bildungszwecken und ersetzt keine professionelle psychologische Beratung.
                </div>
            </div>
            
            <h3 style="color: #2c3e50;">Entwickler</h3>
            <p>Diese Streamlit-Anwendung wurde entwickelt, um das Big-five-Modell 
            zugänglich und anwendbar zu machen.</p>
        </div>
        """, unsafe_allow_html=True)

# Hauptanwendung ausführen
if __name__ == "__main__":
    app = BigFiveApp()
    app.run()
