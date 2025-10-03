import streamlit as st
import pandas as pd
import plotly.express as px
from modules.screening import PersonalityScreener
from modules.training import TrainingModule
from modules.quiz import QuizModule
from modules.recommendations import RecommendationEngine

# Streamlit Konfiguration MUSS als erstes nach Imports kommen
st.set_page_config(
    page_title="Big Five Personality Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS für modernes Design
def inject_custom_css():
    st.markdown("""
    <style>
    /* Hauptfarben */
    :root {
        --primary: #4B7BEC;
        --secondary: #6C63FF;
        --success: #00C9A7;
        --warning: #FF8066;
        --info: #00B4D8;
        --dark: #2D3748;
        --light: #F8F9FA;
    }
    
    /* Global Styles */
    .main {
        background-color: var(--light);
    }
    
    /* Hero Header */
    .hero-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(75, 123, 236, 0.3);
    }
    
    .hero-title {
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    
    .hero-subtitle {
        font-size: 1.3rem !important;
        opacity: 0.9;
        font-weight: 300;
    }
    
    /* Cards */
    .custom-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border-left: 5px solid var(--primary);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    }
    
    /* Buttons */
    .stButton > button {
        border-radius: 25px !important;
        border: none !important;
        background: linear-gradient(45deg, var(--primary), var(--secondary)) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(75, 123, 236, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(75, 123, 236, 0.4) !important;
    }
    
    /* Secondary Buttons */
    .secondary-button {
        border-radius: 25px !important;
        border: 2px solid var(--primary) !important;
        background: transparent !important;
        color: var(--primary) !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
    }
    
    .secondary-button:hover {
        background: var(--primary) !important;
        color: white !important;
    }
    
    /* Metrics/KPI Cards */
    [data-testid="metric-container"] {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        border-left: 4px solid var(--success);
        text-align: center;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--light) 0%, #e9ecef 100%);
        border-right: 1px solid #e0e0e0;
    }
    
    .sidebar-title {
        color: var(--primary) !important;
        font-weight: 700 !important;
        font-size: 1.5rem !important;
        text-align: center;
        margin-bottom: 2rem !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: white !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        border: 1px solid #e0e0e0 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .streamlit-expanderContent {
        background-color: white;
        border-radius: 0 0 10px 10px;
        padding: 1.5rem;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(45deg, var(--primary), var(--secondary));
    }
    
    /* Radio Buttons */
    .st-bb {
        background-color: white;
    }
    
    /* Success/Warning/Info Boxes */
    .stAlert {
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08) !important;
    }
    
    /* Columns spacing */
    .css-1r6slb0 {
        gap: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

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
        # Custom CSS injecten
        inject_custom_css()
        
        # Hero Section
        st.markdown("""
        <div class="hero-header">
            <div class="hero-title">🧠 Big Five Personality Analyzer</div>
            <div class="hero-subtitle">Wissenschaftlich fundierte Persönlichkeitsanalyse basierend auf dem NEO-PI-R Modell</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Seitenauswahl in der Sidebar
        st.sidebar.markdown('<div class="sidebar-title">🧭 Navigation</div>', unsafe_allow_html=True)
        app_mode = st.sidebar.selectbox(
            "",
            ["🏠 Übersicht", "🔍 Screening", "📚 Training", "❓ Quiz", "💡 Empfehlungen", "ℹ️ Über"],
            label_visibility="collapsed"
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
        st.markdown("""
        <div style='text-align: center; margin-bottom: 3rem;'>
            <h2 style='color: #2D3748; margin-bottom: 1rem;'>Willkommen beim Big Five Personality Analyzer</h2>
            <p style='font-size: 1.2rem; color: #666; max-width: 800px; margin: 0 auto;'>
                Entdecken Sie die Wissenschaft hinter Ihrer Persönlichkeit und erhalten Sie evidenzbasierte Einblicke für Ihre persönliche Entwicklung.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            <div class="custom-card">
                <h3>🎯 Was sind die Big Five?</h3>
                <p>Das <strong>Fünf-Faktoren-Modell</strong> (Big Five) ist das international anerkannte Standardmodell 
                in der Persönlichkeitsforschung. Es beschreibt die menschliche Persönlichkeit anhand 
                von fünf Hauptdimensionen:</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Big Five Dimensionen als Grid
            st.markdown("""
            <div style='background: #F7FAFC; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;'>
                <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;'>
                    <div style='text-align: center; padding: 1rem; background: white; border-radius: 8px;'>
                        <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🧠</div>
                        <strong>O</strong>ffenheit
                    </div>
                    <div style='text-align: center; padding: 1rem; background: white; border-radius: 8px;'>
                        <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📊</div>
                        <strong>G</strong>ewissenhaftigkeit
                    </div>
                    <div style='text-align: center; padding: 1rem; background: white; border-radius: 8px;'>
                        <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🌟</div>
                        <strong>E</strong>xtraversion
                    </div>
                    <div style='text-align: center; padding: 1rem; background: white; border-radius: 8px;'>
                        <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🤝</div>
                        <strong>V</strong>erträglichkeit
                    </div>
                </div>
                <div style='text-align: center; padding: 1rem; background: white; border-radius: 8px; margin-top: 1rem;'>
                    <div style='font-size: 2rem; margin-bottom: 0.5rem;'>⚡</div>
                    <strong>N</strong>eurotizismus
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="custom-card">
                <h4>🔬 Wissenschaftliche Grundlage</h4>
                <ul style='color: #666;'>
                    <li>Basierend auf dem lexikalischen Ansatz</li>
                    <li>Über 3.000 wissenschaftliche Studien</li>
                    <li>40-60% genetische Komponente</li>
                    <li>Kulturübergreifend validiert</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="custom-card">
                <h3>🚀 App Funktionen</h3>
                <div style='margin: 1.5rem 0;'>
                    <div style='display: flex; align-items: center; margin-bottom: 1rem; padding: 1rem; background: #F0F7FF; border-radius: 10px;'>
                        <div style='font-size: 2rem; margin-right: 1rem;'>🔍</div>
                        <div>
                            <strong>Persönlichkeitsscreening</strong><br>
                            <small style='color: #666;'>60 Fragen basierend auf NEO-PI-R</small>
                        </div>
                    </div>
                    <div style='display: flex; align-items: center; margin-bottom: 1rem; padding: 1rem; background: #F0F7FF; border-radius: 10px;'>
                        <div style='font-size: 2rem; margin-right: 1rem;'>📚</div>
                        <div>
                            <strong>Wissenschaftliches Training</strong><br>
                            <small style='color: #666;'>Evidenzbasierte Inhalte</small>
                        </div>
                    </div>
                    <div style='display: flex; align-items: center; margin-bottom: 1rem; padding: 1rem; background: #F0F7FF; border-radius: 10px;'>
                        <div style='font-size: 2rem; margin-right: 1rem;'>❓</div>
                        <div>
                            <strong>Interaktives Quiz</strong><br>
                            <small style='color: #666;'>Testen Sie Ihr Wissen</small>
                        </div>
                    </div>
                    <div style='display: flex; align-items: center; padding: 1rem; background: #F0F7FF; border-radius: 10px;'>
                        <div style='font-size: 2rem; margin-right: 1rem;'>💡</div>
                        <div>
                            <strong>Personalisierte Empfehlungen</strong><br>
                            <small style='color: #666;'>Individuelle Entwicklungspläne</small>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Schnellstart-Bereich
        st.markdown("""
        <div style='text-align: center; margin: 3rem 0 2rem 0;'>
            <h3 style='color: #2D3748;'>🎯 Starten Sie jetzt Ihre Reise</h3>
            <p style='color: #666;'>Wählen Sie einen der folgenden Bereiche, um direkt einzusteigen:</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎯 **Schnelles Screening starten**\n\n30 Fragen - 10 Minuten", use_container_width=True):
                st.session_state.app_mode = "🔍 Screening"
                st.rerun()
        
        with col2:
            if st.button("📚 **Training beginnen**\n\nWissenschaftliche Grundlagen", use_container_width=True):
                st.session_state.app_mode = "📚 Training"
                st.rerun()
        
        with col3:
            if st.button("❓ **Quiz testen**\n\nWissen überprüfen", use_container_width=True):
                st.session_state.app_mode = "❓ Quiz"
                st.rerun()
    
    def show_screening(self):
        """Screening-Seite"""
        st.markdown("""
        <div class="custom-card">
            <h2>🔍 Persönlichkeitsscreening</h2>
            <p style='color: #666; margin-bottom: 2rem;'>
                Wählen Sie eine der folgenden Screening-Methoden, um Ihre Persönlichkeitsdimensionen 
                basierend auf dem wissenschaftlich validierten NEO-PI-R Modell zu erfassen.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Screening Methoden als Cards
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="custom-card" style='text-align: center; height: 100%;'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>⚡</div>
                <h3>Schnelles Screening</h3>
                <p style='color: #666;'>30 Fragen - Ca. 10 Minuten</p>
                <div style='background: #F0F7FF; padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
                    <small>Ideal für einen ersten Überblick</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("⚡ Schnelles Screening starten", use_container_width=True, key="quick_btn"):
                scores = self.screener.quick_screening()
                if scores is not None:
                    profile = self.screener.classify_profile(scores)
                    st.session_state.scores = scores
                    st.session_state.profile = profile
                    st.rerun()
        
        with col2:
            st.markdown("""
            <div class="custom-card" style='text-align: center; height: 100%;'>
                <div style='font-size: 3rem; margin-bottom: 1rem;'>🔬</div>
                <h3>Ausführlicher Fragebogen</h3>
                <p style='color: #666;'>60 Fragen - Ca. 20 Minuten</p>
                <div style='background: #F0F7FF; padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
                    <small>Detaillierte Analyse aller Facetten</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔬 Vollständiges Screening starten", use_container_width=True, key="full_btn"):
                scores = self.screener.behavioral_questionnaire()
                if scores is not None:
                    profile = self.screener.classify_profile(scores)
                    st.session_state.scores = scores
                    st.session_state.profile = profile
                    st.rerun()
        
        # Ergebnisse anzeigen wenn vorhanden
        if st.session_state.scores is not None:
            self.show_screening_results(st.session_state.scores, st.session_state.profile)
    
    def show_screening_results(self, scores, profile):
        """Zeigt die Screening-Ergebnisse"""
        st.markdown("""
        <div class="custom-card" style='background: linear-gradient(135deg, #00C9A7, #00B4D8); color: white;'>
            <div style='text-align: center;'>
                <h2 style='color: white; margin-bottom: 0.5rem;'>🎉 Auswertung abgeschlossen!</h2>
                <p style='color: white; opacity: 0.9;'>Ihr persönliches Big Five Profil wurde erfolgreich erstellt.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Radar-Diagramm
        fig = self.screener.create_radar_chart(scores)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Radar-Diagramm konnte nicht erstellt werden.")
        
        # Detaillierte Ergebnisse
        st.markdown("""
        <div class="custom-card">
            <h3>📊 Detaillierte Auswertung</h3>
            <p style='color: #666;'>Ihre Werte in den fünf Hauptdimensionen:</p>
        </div>
        """, unsafe_allow_html=True)
        
        cols = st.columns(5)
        dimension_names = {
            'O': 'Offenheit', 'C': 'Gewissenhaftigkeit', 'E': 'Extraversion',
            'A': 'Verträglichkeit', 'N': 'Neurotizismus'
        }
        
        for i, (dim, score) in enumerate(scores.items()):
            with cols[i]:
                level = profile[dim]
                # Farbe basierend auf Dimension und Level
                if level == "hoch" and dim != "N":
                    bg_color = "#00C9A7"
                    emoji = "📈"
                elif level == "niedrig" and dim != "N":
                    bg_color = "#FF8066" 
                    emoji = "📉"
                elif level == "hoch" and dim == "N":
                    bg_color = "#FF8066"
                    emoji = "📈"
                else:
                    bg_color = "#00B4D8"
                    emoji = "📉"
                
                st.markdown(f"""
                <div style='background: {bg_color}; color: white; padding: 1.5rem; border-radius: 15px; text-align: center;'>
                    <div style='font-size: 2rem; margin-bottom: 0.5rem;'>{emoji}</div>
                    <h4 style='color: white; margin: 0;'>{dimension_names[dim]}</h4>
                    <div style='font-size: 2rem; font-weight: bold; margin: 0.5rem 0;'>{score:.0f}</div>
                    <div style='background: rgba(255,255,255,0.2); padding: 0.3rem 1rem; border-radius: 20px; font-size: 0.9rem;'>
                        {level.capitalize()}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Ähnlichkeitsanalyse
        st.markdown("""
        <div class="custom-card">
            <h3>👥 Ähnlichkeitsanalyse</h3>
            <p style='color: #666;'>Vergleich mit typischen Persönlichkeitsprofilen:</p>
        </div>
        """, unsafe_allow_html=True)
        
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
                title="",
                color='Ähnlichkeit (%)',
                color_continuous_scale='viridis'
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(size=12),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Nächste Schritte
        st.markdown("""
        <div class="custom-card">
            <h3>🚀 Nächste Schritte</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1rem; margin-top: 1rem;'>
                <div style='text-align: center; padding: 1.5rem; background: #F0F7FF; border-radius: 10px;'>
                    <div style='font-size: 2rem; margin-bottom: 0.5rem;'>📚</div>
                    <strong>Training</strong>
                    <p style='font-size: 0.9rem; color: #666; margin: 0.5rem 0 0 0;'>Mehr über die Big Five lernen</p>
                </div>
                <div style='text-align: center; padding: 1.5rem; background: #F0F7FF; border-radius: 10px;'>
                    <div style='font-size: 2rem; margin-bottom: 0.5rem;'>❓</div>
                    <strong>Quiz</strong>
                    <p style='font-size: 0.9rem; color: #666; margin: 0.5rem 0 0 0;'>Wissen testen</p>
                </div>
                <div style='text-align: center; padding: 1.5rem; background: #F0F7FF; border-radius: 10px;'>
                    <div style='font-size: 2rem; margin-bottom: 0.5rem;'>💡</div>
                    <strong>Empfehlungen</strong>
                    <p style='font-size: 0.9rem; color: #666; margin: 0.5rem 0 0 0;'>Personalisierte Tipps</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def show_training(self):
        """Training-Seite"""
        st.markdown("""
        <div class="custom-card">
            <h2>📚 Big Five Training</h2>
            <p style='color: #666;'>
                Vertiefen Sie Ihr Wissen über das Fünf-Faktoren-Modell mit wissenschaftlich fundierten Inhalten.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
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
        <div class="custom-card">
            <h2>🎯 Das Fünf-Faktoren-Modell (Big Five)</h2>
            
            <h3>📜 Historische Entwicklung</h3>
            <p>Das Big-Five-Modell entwickelte sich aus dem <strong>lexikalischen Ansatz</strong>, der besagt, 
            dass alle wichtigen Persönlichkeitsmerkmale in der natürlichen Sprache kodiert sind.</p>
            
            <div style='background: #F7FAFC; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;'>
                <h4>🕰️ Wichtige Meilensteine:</h4>
                <ul>
                    <li><strong>1936:</strong> Allport & Odbert identifizieren 18.000 Persönlichkeitsbegriffe</li>
                    <li><strong>1960er:</strong> Cattell reduziert auf 16 Faktoren</li>
                    <li><strong>1980er:</strong> Fünf stabile Faktoren werden international bestätigt</li>
                    <li><strong>1990er:</strong> NEO-PI-R etabliert standardisiertes Messinstrument</li>
                </ul>
            </div>
            
            <h3>🌟 Die fünf Dimensionen</h3>
        </div>
        """, unsafe_allow_html=True)
        
        dimensions_info = {
            'O': {
                'name': 'Offenheit für Erfahrungen',
                'description': 'Beschreibt die Offenheit für neue Erfahrungen, Kreativität und intellektuelle Neugier',
                'high': 'Kreativ, neugierig, vielseitig',
                'low': 'Praktisch, konventionell, traditionell',
                'icon': '🧠'
            },
            'C': {
                'name': 'Gewissenhaftigkeit', 
                'description': 'Bezieht sich auf Organisation, Zuverlässigkeit und Zielstrebigkeit',
                'high': 'Organisiert, verantwortungsbewusst, zuverlässig',
                'low': 'Spontan, flexibel, ungezwungen',
                'icon': '📊'
            },
            'E': {
                'name': 'Extraversion',
                'description': 'Beschreibt Geselligkeit, Energie und positive Emotionalität',
                'high': 'Gesellig, energisch, gesprächig',
                'low': 'Zurückhaltend, ruhig, reserviert',
                'icon': '🌟'
            },
            'A': {
                'name': 'Verträglichkeit',
                'description': 'Bezieht sich auf Mitgefühl, Kooperationsbereitschaft und Vertrauen',
                'high': 'Hilfsbereit, vertrauensvoll, mitfühlend',
                'low': 'Skeptisch, wettbewerbsorientiert, direkt',
                'icon': '🤝'
            },
            'N': {
                'name': 'Neurotizismus',
                'description': 'Beschreibt emotionale Stabilität und Anfälligkeit für negative Emotionen',
                'high': 'Emotional, sensibel, besorgt',
                'low': 'Gelassen, emotional stabil, resilient',
                'icon': '⚡'
            }
        }
        
        for dim, info in dimensions_info.items():
            with st.expander(f"{info['icon']} {info['name']} ({dim})"):
                st.write(f"**Beschreibung:** {info['description']}")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div style='background: #E8F5E8; padding: 1rem; border-radius: 10px; border-left: 4px solid #00C9A7;'>
                        <strong>✅ Hohe Ausprägung:</strong><br>
                        {info['high']}
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div style='background: #E3F2FD; padding: 1rem; border-radius: 10px; border-left: 4px solid #00B4D8;'>
                        <strong>💡 Niedrige Ausprägung:</strong><br>
                        {info['low']}
                    </div>
                    """, unsafe_allow_html=True)
    
    def show_quiz(self):
        """Quiz-Seite"""
        self.quiz.display_quiz()
    
    def show_recommendations(self):
        """Empfehlungs-Seite"""
        st.markdown("""
        <div class="custom-card">
            <h2>💡 Personalisiertes Feedback</h2>
            <p style='color: #666;'>
                Basierend auf Ihren Screening-Ergebnissen erhalten Sie evidenzbasierte Empfehlungen 
                für Ihre persönliche und berufliche Entwicklung.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.scores is None:
            st.markdown("""
            <div class="custom-card" style='text-align: center; background: #FFF3E0; border-left: 5px solid #FF8066;'>
                <div style='font-size: 4rem; margin-bottom: 1rem;'>🔍</div>
                <h3 style='color: #E65100;'>Screening erforderlich</h3>
                <p style='color: #666;'>
                    Bitte führen Sie zuerst ein Screening durch, um personalisierte Empfehlungen zu erhalten.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                if st.button("🎯 Jetzt Screening starten", use_container_width=True):
                    st.session_state.app_mode = "🔍 Screening"
                    st.rerun()
            return
        
        # Empfehlungen generieren
        self.recommendations.generate_recommendations(
            st.session_state.profile, 
            st.session_state.scores
        )
        
        # Entwicklungsplan
        st.markdown("""
        <div class="custom-card">
            <h3>📈 Persönlicher Entwicklungsplan</h3>
            <p style='color: #666;'>Konkrete Schritte für Ihre persönliche Entwicklung:</p>
        </div>
        """, unsafe_allow_html=True)
        
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
        st.markdown("""
        <div class="custom-card">
            <h2>ℹ️ Über diese Anwendung</h2>
            
            <h3>🔬 Wissenschaftliche Grundlage</h3>
            <p>Diese Anwendung basiert auf dem <strong>Fünf-Faktoren-Modell</strong> (Big Five), 
            dem international anerkannten Standardmodell der Persönlichkeitsforschung.</p>
            
            <div style='background: #F7FAFC; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;'>
                <h4>📚 Wichtige Quellen:</h4>
                <ul>
                    <li>Costa, P. T., & McCrae, R. R. (1992). NEO-PI-R Professional Manual</li>
                    <li>Goldberg, L. R. (1993). The structure of phenotypic personality traits</li>
                    <li>John, O. P., & Srivastava, S. (1999). The Big Five trait taxonomy</li>
                </ul>
            </div>
            
            <h3>⚙️ Technische Umsetzung</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;'>
                <div style='background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e0e0e0;'>
                    <strong>🔍 Screening</strong><br>
                    <small>Verhaltensbasierte Fragebögen</small>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e0e0e0;'>
                    <strong>📊 Profilanalyse</strong><br>
                    <small>Wissenschaftlich validierte Auswertung</small>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e0e0e0;'>
                    <strong>🎓 Training</strong><br>
                    <small>Evidenzbasierte Inhalte</small>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border: 1px solid #e0e0e0;'>
                    <strong>💡 Empfehlungen</strong><br>
                    <small>Personalisierte Entwicklungspläne</small>
                </div>
            </div>
            
            <div style='background: #E3F2FD; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; border-left: 4px solid #00B4D8;'>
                <h4>⚠️ Wichtiger Hinweis</h4>
                <p style='margin: 0;'>Diese Anwendung dient <strong>Bildungszwecken</strong> und ersetzt keine 
                professionelle psychologische Beratung.</p>
            </div>
            
            <h3>👨‍💻 Entwickler</h3>
            <p>Diese Streamlit-Anwendung wurde entwickelt, um das Big-five-Modell 
            zugänglich und anwendbar zu machen.</p>
        </div>
        """, unsafe_allow_html=True)

# Hauptanwendung ausführen
if __name__ == "__main__":
    app = BigFiveApp()
    app.run()
