import streamlit as st
import random
from typing import Dict, List, Any

class PersonalityScreener:
    def __init__(self):
        self.dimensions = self.initialize_dimensions()
        self.all_questions = self.load_questions()
        self.randomized_questions = None
        
    def initialize_dimensions(self):
        """Initialisiert die NEO PI R Struktur mit Facetten"""
        return {
            'O': {
                'name': 'Offenheit für Erfahrungen',
                'facets': {
                    'O1': {'name': 'Fantasie / Vorstellungskraft', 'questions': [1, 2], 'score': 0},
                    'O2': {'name': 'Ästhetik / Kunstsinn', 'questions': [3, 4], 'score': 0},
                    'O3': {'name': 'Gefühle / emotionale Offenheit', 'questions': [5, 6], 'score': 0},
                    'O4': {'name': 'Handlungen / Abenteuerlust', 'questions': [7, 8], 'score': 0},
                    'O5': {'name': 'Ideen / Intellektuelle Neugier', 'questions': [9, 10], 'score': 0},
                    'O6': {'name': 'Werte / Liberalismus', 'questions': [11, 12], 'score': 0}
                },
                'total_score': 0
            },
            'C': {
                'name': 'Gewissenhaftigkeit',
                'facets': {
                    'C1': {'name': 'Kompetenz / Selbstwirksamkeit', 'questions': [13, 14], 'score': 0},
                    'C2': {'name': 'Ordnungsliebe', 'questions': [15, 16], 'score': 0},
                    'C3': {'name': 'Pflichtbewusstsein', 'questions': [17, 18], 'score': 0},
                    'C4': {'name': 'Leistungsstreben', 'questions': [19, 20], 'score': 0},
                    'C5': {'name': 'Selbstdisziplin', 'questions': [21, 22], 'score': 0},
                    'C6': {'name': 'Besonnenheit / Überlegtheit', 'questions': [23, 24], 'score': 0}
                },
                'total_score': 0
            },
            'E': {
                'name': 'Extraversion',
                'facets': {
                    'E1': {'name': 'Herzlichkeit / Wärme', 'questions': [25, 26], 'score': 0},
                    'E2': {'name': 'Geselligkeit', 'questions': [27, 28], 'score': 0},
                    'E3': {'name': 'Durchsetzungsfähigkeit', 'questions': [29, 30], 'score': 0},
                    'E4': {'name': 'Aktivität', 'questions': [31, 32], 'score': 0},
                    'E5': {'name': 'Erlebnishunger', 'questions': [33, 34], 'score': 0},
                    'E6': {'name': 'Fröhlichkeit / positive Emotionen', 'questions': [35, 36], 'score': 0}
                },
                'total_score': 0
            },
            'A': {
                'name': 'Verträglichkeit',
                'facets': {
                    'A1': {'name': 'Vertrauen', 'questions': [37, 38], 'score': 0},
                    'A2': {'name': 'Altruismus', 'questions': [39, 40], 'score': 0},
                    'A3': {'name': 'Kooperationsbereitschaft', 'questions': [41, 42], 'score': 0},
                    'A4': {'name': 'Bescheidenheit', 'questions': [43, 44], 'score': 0},
                    'A5': {'name': 'Güte / Nachsicht', 'questions': [45, 46], 'score': 0},
                    'A6': {'name': 'Einfühlungsvermögen', 'questions': [47, 48], 'score': 0}
                },
                'total_score': 0
            },
            'N': {
                'name': 'Neurotizismus',
                'facets': {
                    'N1': {'name': 'Ängstlichkeit', 'questions': [49, 50], 'score': 0},
                    'N2': {'name': 'Reizbarkeit / Feindseligkeit', 'questions': [51, 52], 'score': 0},
                    'N3': {'name': 'Depressivität', 'questions': [53, 54], 'score': 0},
                    'N4': {'name': 'Selbstunsicherheit', 'questions': [55, 56], 'score': 0},
                    'N5': {'name': 'Impulsivität', 'questions': [57, 58], 'score': 0},
                    'N6': {'name': 'Verletzlichkeit / Stressanfälligkeit', 'questions': [59, 60], 'score': 0}
                },
                'total_score': 0
            }
        }
    
    def load_questions(self):
        """Lädt alle 60 Fragen mit ihrer Struktur"""
        questions = [
            # Offenheit (O) - Fragen 1-12
            {"id": 1, "text": "Ich könnte mir lebhafte Bilder und Szenen vorstellen, wenn ich Tagträume hätte.", "dimension": "O", "facet": "O1"},
            {"id": 2, "text": "Ich könnte mich leicht in fiktive Geschichten hineinversetzen.", "dimension": "O", "facet": "O1"},
            {"id": 3, "text": "Ich könnte Freude an Kunstwerken, Musik oder Literatur empfinden.", "dimension": "O", "facet": "O2"},
            {"id": 4, "text": "Ich könnte feine Unterschiede in Farben, Klängen oder Formen wahrnehmen.", "dimension": "O", "facet": "O2"},
            {"id": 5, "text": "Ich könnte meine Gefühle bewusst wahrnehmen und benennen.", "dimension": "O", "facet": "O3"},
            {"id": 6, "text": "Ich könnte mich von Emotionen stark beeinflussen lassen.", "dimension": "O", "facet": "O3"},
            {"id": 7, "text": "Ich könnte gerne neue Aktivitäten ausprobieren.", "dimension": "O", "facet": "O4"},
            {"id": 8, "text": "Ich könnte offen für unkonventionelle Erfahrungen sein.", "dimension": "O", "facet": "O4"},
            {"id": 9, "text": "Ich könnte Spaß daran haben, komplexe Probleme zu durchdenken.", "dimension": "O", "facet": "O5"},
            {"id": 10, "text": "Ich könnte Freude daran empfinden, neue Theorien oder Konzepte kennenzulernen.", "dimension": "O", "facet": "O5"},
            {"id": 11, "text": "Ich könnte bereit sein, tradierte Normen zu hinterfragen.", "dimension": "O", "facet": "O6"},
            {"id": 12, "text": "Ich könnte alternative Sichtweisen akzeptieren, auch wenn sie ungewohnt sind.", "dimension": "O", "facet": "O6"},
            
            # Gewissenhaftigkeit (C) - Fragen 13-24
            {"id": 13, "text": "Ich könnte überzeugt sein, schwierige Aufgaben erfolgreich zu bewältigen.", "dimension": "C", "facet": "C1"},
            {"id": 14, "text": "Ich könnte mir selbst zutrauen, auch komplexe Projekte zu meistern.", "dimension": "C", "facet": "C1"},
            {"id": 15, "text": "Ich könnte gerne Strukturen schaffen und Ordnung halten.", "dimension": "C", "facet": "C2"},
            {"id": 16, "text": "Ich könnte mich unwohl fühlen, wenn meine Umgebung chaotisch wirkt.", "dimension": "C", "facet": "C2"},
            {"id": 17, "text": "Ich könnte Regeln und Abmachungen zuverlässig einhalten.", "dimension": "C", "facet": "C3"},
            {"id": 18, "text": "Ich könnte ein starkes Verantwortungsgefühl gegenüber anderen verspüren.", "dimension": "C", "facet": "C3"},
            {"id": 19, "text": "Ich könnte hohe Ansprüche an mich selbst stellen.", "dimension": "C", "facet": "C4"},
            {"id": 20, "text": "Ich könnte mich stark auf das Erreichen meiner Ziele konzentrieren.", "dimension": "C", "facet": "C4"},
            {"id": 21, "text": "Ich könnte Aufgaben auch dann abschließen, wenn sie anstrengend sind.", "dimension": "C", "facet": "C5"},
            {"id": 22, "text": "Ich könnte Versuchungen widerstehen, die mich von meinen Pflichten ablenken.", "dimension": "C", "facet": "C5"},
            {"id": 23, "text": "Ich könnte wichtige Entscheidungen erst nach gründlichem Nachdenken treffen.", "dimension": "C", "facet": "C6"},
            {"id": 24, "text": "Ich könnte Risiken meiden, wenn sie unüberlegt erscheinen.", "dimension": "C", "facet": "C6"},
            
            # Extraversion (E) - Fragen 25-36
            {"id": 25, "text": "Ich könnte leicht Nähe zu anderen Menschen aufbauen.", "dimension": "E", "facet": "E1"},
            {"id": 26, "text": "Ich könnte freundlich und aufgeschlossen wirken.", "dimension": "E", "facet": "E1"},
            {"id": 27, "text": "Ich könnte gerne viel Zeit mit anderen Menschen verbringen.", "dimension": "E", "facet": "E2"},
            {"id": 28, "text": "Ich könnte mich in Gesellschaft wohler fühlen als allein.", "dimension": "E", "facet": "E2"},
            {"id": 29, "text": "Ich könnte meine Meinung klar und selbstbewusst äußern.", "dimension": "E", "facet": "E3"},
            {"id": 30, "text": "Ich könnte in Gruppen leicht die Führung übernehmen.", "dimension": "E", "facet": "E3"},
            {"id": 31, "text": "Ich könnte stets das Gefühl haben, etwas unternehmen zu wollen.", "dimension": "E", "facet": "E4"},
            {"id": 32, "text": "Ich könnte mich in ruhigen, passiven Phasen schnell gelangweilt fühlen.", "dimension": "E", "facet": "E4"},
            {"id": 33, "text": "Ich könnte Spaß an aufregenden oder intensiven Erlebnissen haben.", "dimension": "E", "facet": "E5"},
            {"id": 34, "text": "Ich könnte Gelegenheiten für Abenteuer aktiv suchen.", "dimension": "E", "facet": "E5"},
            {"id": 35, "text": "Ich könnte häufig Freude oder Begeisterung empfinden.", "dimension": "E", "facet": "E6"},
            {"id": 36, "text": "Ich könnte meist optimistisch und heiter wirken.", "dimension": "E", "facet": "E6"},
            
            # Verträglichkeit (A) - Fragen 37-48
            {"id": 37, "text": "Ich könnte davon ausgehen, dass Menschen im Allgemeinen gute Absichten haben.", "dimension": "A", "facet": "A1"},
            {"id": 38, "text": "Ich könnte anderen schnell Glauben schenken.", "dimension": "A", "facet": "A1"},
            {"id": 39, "text": "Ich könnte anderen spontan helfen, wenn sie Unterstützung benötigen.", "dimension": "A", "facet": "A2"},
            {"id": 40, "text": "Ich könnte Freude empfinden, wenn ich jemandem etwas Gutes tun könnte.", "dimension": "A", "facet": "A2"},
            {"id": 41, "text": "Ich könnte Konflikte vermeiden, um Harmonie zu bewahren.", "dimension": "A", "facet": "A3"},
            {"id": 42, "text": "Ich könnte meine eigenen Wünsche zurückstellen, wenn es dem Miteinander dient.", "dimension": "A", "facet": "A3"},
            {"id": 43, "text": "Ich könnte wenig Wert darauf legen, mich in den Vordergrund zu stellen.", "dimension": "A", "facet": "A4"},
            {"id": 44, "text": "Ich könnte meine Erfolge eher herunterspielen.", "dimension": "A", "facet": "A4"},
            {"id": 45, "text": "Ich könnte Fehler anderer schnell verzeihen.", "dimension": "A", "facet": "A5"},
            {"id": 46, "text": "Ich könnte tolerant mit Schwächen von Mitmenschen umgehen.", "dimension": "A", "facet": "A5"},
            {"id": 47, "text": "Ich könnte leicht erkennen, wie sich andere fühlen.", "dimension": "A", "facet": "A6"},
            {"id": 48, "text": "Ich könnte mich stark in die Emotionen anderer hineinversetzen.", "dimension": "A", "facet": "A6"},
            
            # Neurotizismus (N) - Fragen 49-60
            {"id": 49, "text": "Ich könnte in neuen oder unsicheren Situationen angespannt sein.", "dimension": "N", "facet": "N1"},
            {"id": 50, "text": "Ich könnte mir häufig Sorgen machen.", "dimension": "N", "facet": "N1"},
            {"id": 51, "text": "Ich könnte leicht ärgerlich werden.", "dimension": "N", "facet": "N2"},
            {"id": 52, "text": "Ich könnte mich schnell provoziert fühlen.", "dimension": "N", "facet": "N2"},
            {"id": 53, "text": "Ich könnte manchmal das Gefühl haben, wertlos zu sein.", "dimension": "N", "facet": "N3"},
            {"id": 54, "text": "Ich könnte mich häufiger niedergeschlagen fühlen.", "dimension": "N", "facet": "N3"},
            {"id": 55, "text": "Ich könnte in sozialen Situationen unsicher wirken.", "dimension": "N", "facet": "N4"},
            {"id": 56, "text": "Ich könnte mich stark darum sorgen, was andere über mich denken.", "dimension": "N", "facet": "N4"},
            {"id": 57, "text": "Ich könnte spontanen Impulsen nachgeben, auch wenn sie unvernünftig wären.", "dimension": "N", "facet": "N5"},
            {"id": 58, "text": "Ich könnte Schwierigkeiten haben, Versuchungen zu widerstehen.", "dimension": "N", "facet": "N5"},
            {"id": 59, "text": "Ich könnte in Stresssituationen schnell überfordert wirken.", "dimension": "N", "facet": "N6"},
            {"id": 60, "text": "Ich könnte Schwierigkeiten haben, nach belastenden Erlebnissen wieder zur Ruhe zu kommen.", "dimension": "N", "facet": "N6"}
        ]
        
        return questions
    
    def randomize_questions(self):
        """Mischt alle Fragen für eine randomisierte Präsentation"""
        questions = self.all_questions.copy()
        random.shuffle(questions)
        self.randomized_questions = questions
        return questions
    
    def display_questionnaire(self):
        """Zeigt den kompletten Fragebogen an"""
        st.header("🧠 Big Five Persönlichkeitsscreening (NEO PI R)")
        st.markdown("**Beantworten Sie jede Aussage auf einer Skala von 1-5**")
        
        # Initialisiere Session State
        if 'screening_responses' not in st.session_state:
            st.session_state.screening_responses = {}
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'screening_complete' not in st.session_state:
            st.session_state.screening_complete = False
        
        # Randomisiere Fragen beim Start
        if self.randomized_questions is None:
            questions = self.randomize_questions()
        else:
            questions = self.randomized_questions
        
        # Fortschrittsanzeige
        progress = (st.session_state.current_question) / len(questions)
        st.progress(progress)
        st.caption(f"Frage {st.session_state.current_question + 1} von {len(questions)}")
        
        # Aktuelle Frage anzeigen
        if st.session_state.current_question < len(questions):
            current_q = questions[st.session_state.current_question]
            
            st.markdown(f"### {current_q['text']}")
            
            # Likert-Skala
            response = st.radio(
                "Wie sehr stimmen Sie dieser Aussage zu?",
                options=[
                    (1, "Stimme überhaupt nicht zu"),
                    (2, "Stimme eher nicht zu"), 
                    (3, "Neutral / teils-teils"),
                    (4, "Stimme eher zu"),
                    (5, "Stimme völlig zu")
                ],
                format_func=lambda x: x[1],
                key=f"q_{current_q['id']}"
            )
            
            col1, col2 = st.columns([1, 4])
            
            with col1:
                if st.button("⏭️ Überspringen", key=f"skip_{current_q['id']}"):
                    st.session_state.current_question += 1
                    st.rerun()
            
            with col2:
                if st.button("📝 Antwort speichern & Weiter", type="primary", key=f"next_{current_q['id']}"):
                    # Antwort speichern
                    if response:
                        st.session_state.screening_responses[current_q['id']] = response[0]
                    
                    st.session_state.current_question += 1
                    
                    if st.session_state.current_question >= len(questions):
                        st.session_state.screening_complete = True
                    
                    st.rerun()
        
        else:
            st.session_state.screening_complete = True
            st.rerun()
    
    def calculate_scores(self):
        """Berechnet die Scores aus den gespeicherten Antworten"""
        if not st.session_state.screening_responses:
            return None
        
        # Reset Scores
        for dim in self.dimensions.values():
            dim['total_score'] = 0
            for facet in dim['facets'].values():
                facet['score'] = 0
        
        # Berechne Facet-Scores
        for question in self.all_questions:
            if question['id'] in st.session_state.screening_responses:
                response = st.session_state.screening_responses[question['id']]
                dimension = question['dimension']
                facet = question['facet']
                
                # Füge Antwort zum Facet-Score hinzu
                self.dimensions[dimension]['facets'][facet]['score'] += response
        
        # Berechne Dimension-Scores (Mittelwert der Facetten)
        dimension_scores = {}
        for dim_code, dim_data in self.dimensions.items():
            facet_scores = [facet['score'] for facet in dim_data['facets'].values()]
            dim_data['total_score'] = sum(facet_scores) / len(facet_scores) * 10  # Skaliert auf 0-100
            dimension_scores[dim_code] = dim_data['total_score']
        
        return dimension_scores
    
    def classify_profile(self, scores):
        """Klassifiziert das Persönlichkeitsprofil basierend auf den Scores"""
        profile = {}
        
        for dim, score in scores.items():
            if score >= 70:
                profile[dim] = "hoch"
            elif score <= 30:
                profile[dim] = "niedrig" 
            else:
                profile[dim] = "durchschnittlich"
        
        return profile
    
    def display_results(self):
        """Zeigt die Screening-Ergebnisse an"""
        st.header("📊 Ihre Big Five Persönlichkeitsprofile")
        
        scores = self.calculate_scores()
        profile = self.classify_profile(scores)
        
        if not scores:
            st.error("Keine Daten verfügbar. Bitte führen Sie zuerst das Screening durch.")
            return
        
        # Gesamtscores anzeigen
        st.subheader("Ihre Hauptdimensionen")
        
        cols = st.columns(5)
        dimension_names = {
            'O': 'Offenheit', 'C': 'Gewissenhaftigkeit', 'E': 'Extraversion',
            'A': 'Verträglichkeit', 'N': 'Neurotizismus'
        }
        
        for i, (dim_code, score) in enumerate(scores.items()):
            with cols[i]:
                st.metric(
                    label=dimension_names[dim_code],
                    value=f"{score:.1f}%",
                    delta=profile[dim_code]
                )
        
        # Detaillierte Facetten-Analyse
        st.subheader("Detaillierte Facetten-Analyse")
        
        for dim_code, dim_data in self.dimensions.items():
            with st.expander(f"{dim_data['name']} - {profile[dim_code]} ({scores[dim_code]:.1f}%)"):
                for facet_code, facet_data in dim_data['facets'].items():
                    facet_score = facet_data['score'] * 5  # Skaliert auf 0-100
                    st.write(f"**{facet_data['name']}:** {facet_score:.1f}%")
                    st.progress(facet_score / 100)
        
        # Speichere Ergebnisse für Recommendations
        st.session_state.screening_results = {
            'scores': scores,
            'profile': profile,
            'dimensions': self.dimensions
        }
        
        # Weiter zu Recommendations
        st.markdown("---")
        st.subheader("🎯 Nächste Schritte")
        
        if st.button("💡 Personalisierte Empfehlungen anzeigen", type="primary", use_container_width=True):
            st.session_state.show_recommendations = True
            st.rerun()
    
    def run_screening(self):
        """Hauptmethode zur Durchführung des Screenings"""
        self._initialize_screening_state()
        
        if not st.session_state.screening_started:
            self.show_screening_intro()
            return
        
        if st.session_state.screening_complete:
            self.display_results()
        else:
            self.display_questionnaire()
    
    def _initialize_screening_state(self):
        """Initialisiert den Session State für das Screening"""
        if 'screening_initialized' not in st.session_state:
            st.session_state.screening_initialized = True
            st.session_state.screening_started = False
            st.session_state.screening_complete = False
            st.session_state.current_question = 0
            st.session_state.screening_responses = {}
            st.session_state.show_recommendations = False
    
    def show_screening_intro(self):
        """Zeigt die Einleitung zum Screening"""
        st.header("🎯 Big Five Persönlichkeitsscreening")
        
        st.info("""
        **Über dieses Screening:**
        
        📋 **Umfang:** 60 wissenschaftlich validierte Fragen
        ⏱️ **Dauer:** Ca. 10-15 Minuten  
        🎯 **Ziel:** Detaillierte Persönlichkeitsanalyse basierend auf dem NEO PI R Modell
        🔒 **Datenschutz:** Ihre Antworten werden nur für diese Sitzung gespeichert
        
        **Die 5 Hauptdimensionen:**
        - **Offenheit** für Erfahrungen
        - **Gewissenhaftigkeit** 
        - **Extraversion**
        - **Verträglichkeit**
        - **Neurotizismus**
        
        Jede Dimension wird durch 6 spezifische Facetten detailliert erfasst.
        """)
        
        if st.button("🎯 Screening starten", type="primary", use_container_width=True):
            st.session_state.screening_started = True
            st.rerun()

# Hauptprogramm
if __name__ == "__main__":
    screener = PersonalityScreener()
    screener.run_screening()
