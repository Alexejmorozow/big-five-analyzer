import streamlit as st
import random
import plotly.graph_objects as go
from typing import Dict, List, Any

class PersonalityScreener:
    def __init__(self):
        self.dimensions = self.initialize_dimensions()
        self.all_questions = self.load_questions()
        
        # Session State für Screening initialisieren
        if 'screening_responses' not in st.session_state:
            st.session_state.screening_responses = {}
        if 'screening_completed' not in st.session_state:
            st.session_state.screening_completed = False
        if 'current_screening_type' not in st.session_state:
            st.session_state.current_screening_type = None
        
    def initialize_dimensions(self):
        """Initialisiert die NEO PI R Struktur mit 30 Facetten"""
        return {
            'N': {'name': 'Neurotizismus'},
            'E': {'name': 'Extraversion'},
            'O': {'name': 'Offenheit für Erfahrungen'},
            'A': {'name': 'Verträglichkeit'},
            'C': {'name': 'Gewissenhaftigkeit'}
        }
    
    def load_questions(self):
        """Lädt alle 60 Fragen"""
        questions = [
            # Neurotizismus (N) - Fragen 1-12
            {"id": 1, "text": "Ich mache mir oft Sorgen über Dinge, die schiefgehen könnten.", "dimension": "N"},
            {"id": 2, "text": "Ich fühle mich häufig nervös oder angespannt.", "dimension": "N"},
            {"id": 3, "text": "Ich ärgere mich leicht über Kleinigkeiten.", "dimension": "N"},
            {"id": 4, "text": "Ich reagiere oft empfindlich auf Kritik oder Frustrationen.", "dimension": "N"},
            {"id": 5, "text": "Ich fühle mich gelegentlich traurig oder niedergeschlagen.", "dimension": "N"},
            {"id": 6, "text": "Ich verliere manchmal die Motivation, Dinge zu erledigen.", "dimension": "N"},
            {"id": 7, "text": "Ich fühle mich in neuen sozialen Situationen unsicher.", "dimension": "N"},
            {"id": 8, "text": "Ich meide manchmal Begegnungen mit fremden Menschen.", "dimension": "N"},
            {"id": 9, "text": "Ich handle oft spontan, ohne vorher über die Folgen nachzudenken.", "dimension": "N"},
            {"id": 10, "text": "Ich habe Schwierigkeiten, mich in stressigen Momenten zu beherrschen.", "dimension": "N"},
            {"id": 11, "text": "Ich fühle mich schnell überfordert, wenn viel auf einmal passiert.", "dimension": "N"},
            {"id": 12, "text": "Stresssituationen setzen mir stark zu.", "dimension": "N"},
            
            # Extraversion (E) - Fragen 13-24
            {"id": 13, "text": "Es fällt mir leicht, Freundschaften zu schließen.", "dimension": "E"},
            {"id": 14, "text": "Ich gehe offen auf andere Menschen zu.", "dimension": "E"},
            {"id": 15, "text": "Ich verbringe gerne Zeit mit anderen Menschen.", "dimension": "E"},
            {"id": 16, "text": "Ich genieße es, Teil einer Gruppe zu sein.", "dimension": "E"},
            {"id": 17, "text": "Ich übernehme oft die Leitung in Gruppenprojekten.", "dimension": "E"},
            {"id": 18, "text": "Ich äußere meine Meinung klar, auch wenn sie von anderen abweicht.", "dimension": "E"},
            {"id": 19, "text": "Ich bin gern beschäftigt und immer aktiv.", "dimension": "E"},
            {"id": 20, "text": "Ich erledige Aufgaben lieber frühzeitig als auf den letzten Drücker.", "dimension": "E"},
            {"id": 21, "text": "Ich probiere gerne neue Aktivitäten und Erfahrungen aus.", "dimension": "E"},
            {"id": 22, "text": "Ich suche oft nach Abwechslung in meinem Alltag.", "dimension": "E"},
            {"id": 23, "text": "Ich bin häufig gut gelaunt und optimistisch.", "dimension": "E"},
            {"id": 24, "text": "Ich lache leicht über kleine Dinge.", "dimension": "E"},
            
            # Offenheit (O) - Fragen 25-36
            {"id": 25, "text": "Ich verliere mich oft in Tagträumen.", "dimension": "O"},
            {"id": 26, "text": "Ich stelle mir gerne alternative Szenarien oder Möglichkeiten vor.", "dimension": "O"},
            {"id": 27, "text": "Ich interessiere mich stark für Kunst, Musik oder Literatur.", "dimension": "O"},
            {"id": 28, "text": "Ich achte auf Schönheit in meiner Umgebung.", "dimension": "O"},
            {"id": 29, "text": "Ich bin mir meiner eigenen Gefühle oft bewusst.", "dimension": "O"},
            {"id": 30, "text": "Ich empfinde Emotionen intensiv.", "dimension": "O"},
            {"id": 31, "text": "Ich probiere gerne neue Aktivitäten oder Hobbys aus.", "dimension": "O"},
            {"id": 32, "text": "Ich reise gerne an unbekannte Orte, um Neues zu entdecken.", "dimension": "O"},
            {"id": 33, "text": "Ich beschäftige mich gern mit abstrakten oder komplexen Ideen.", "dimension": "O"},
            {"id": 34, "text": "Ich interessiere mich für wissenschaftliche, philosophische oder theoretische Themen.", "dimension": "O"},
            {"id": 35, "text": "Ich hinterfrage oft gesellschaftliche Normen und Regeln.", "dimension": "O"},
            {"id": 36, "text": "Ich entwickle eigene Wertvorstellungen und halte an ihnen fest.", "dimension": "O"},
            
            # Verträglichkeit (A) - Fragen 37-48
            {"id": 37, "text": "Ich gehe davon aus, dass die meisten Menschen gute Absichten haben.", "dimension": "A"},
            {"id": 38, "text": "Ich vertraue anderen meist von Natur aus.", "dimension": "A"},
            {"id": 39, "text": "Ich teile offen meine Gedanken und Gefühle mit anderen.", "dimension": "A"},
            {"id": 40, "text": "Ich bin bereit, meine Meinung ehrlich zu äußern, auch wenn sie nicht populär ist.", "dimension": "A"},
            {"id": 41, "text": "Ich helfe anderen gern, auch wenn es mich Zeit oder Mühe kostet.", "dimension": "A"},
            {"id": 42, "text": "Ich setze die Bedürfnisse anderer manchmal über meine eigenen.", "dimension": "A"},
            {"id": 43, "text": "Ich versuche, Konflikte durch Kompromisse zu lösen.", "dimension": "A"},
            {"id": 44, "text": "Ich gehe flexibel auf Wünsche und Vorschläge anderer ein.", "dimension": "A"},
            {"id": 45, "text": "Ich halte mich in Gruppen eher zurück, wenn andere sich präsentieren.", "dimension": "A"},
            {"id": 46, "text": "Ich betone meine eigenen Leistungen selten.", "dimension": "A"},
            {"id": 47, "text": "Ich empfinde Mitgefühl für Menschen in Not.", "dimension": "A"},
            {"id": 48, "text": "Ich bemühe mich, freundlich und hilfsbereit zu sein.", "dimension": "A"},
            
            # Gewissenhaftigkeit (C) - Fragen 49-60
            {"id": 49, "text": "Ich fühle mich in der Regel gut vorbereitet auf meine Aufgaben.", "dimension": "C"},
            {"id": 50, "text": "Ich bin überzeugt davon, meine Aufgaben erfolgreich erledigen zu können.", "dimension": "C"},
            {"id": 51, "text": "Ich lege Wert auf ein ordentliches und strukturiertes Umfeld.", "dimension": "C"},
            {"id": 52, "text": "Ich plane meine Aktivitäten sorgfältig.", "dimension": "C"},
            {"id": 53, "text": "Ich halte mich gewissenhaft an Regeln und Verpflichtungen.", "dimension": "C"},
            {"id": 54, "text": "Ich erledige Aufgaben zuverlässig und termingerecht.", "dimension": "C"},
            {"id": 55, "text": "Ich setze mir hohe Ziele und arbeite zielstrebig darauf hin.", "dimension": "C"},
            {"id": 56, "text": "Ich bemühe mich, in allem, was ich tue, mein Bestes zu geben.", "dimension": "C"},
            {"id": 57, "text": "Ich bleibe auch bei unangenehmen Aufgaben dran, bis sie erledigt sind.", "dimension": "C"},
            {"id": 58, "text": "Ich kann mich gut motivieren, auch wenn ich keine unmittelbare Belohnung erwarte.", "dimension": "C"},
            {"id": 59, "text": "Ich überlege, bevor ich Entscheidungen treffe.", "dimension": "C"},
            {"id": 60, "text": "Ich handle bedacht und vermeide impulsive Entscheidungen.", "dimension": "C"}
        ]
        
        return questions

    def quick_screening(self):
        """Kurzversion mit 30 Fragen"""
        st.info("🚀 **Schnelles Screening mit 30 Fragen**")
        
        # Screening State setzen
        st.session_state.current_screening_type = "quick"
        
        # Erste 30 Fragen für Kurzversion
        short_questions = self.all_questions[:30]
        
        # Fortschrittsbalken
        completed_questions = len([qid for qid in st.session_state.screening_responses.keys() if qid <= 30])
        progress = completed_questions / 30
        st.progress(progress)
        st.write(f"Fortschritt: {completed_questions}/30 Fragen beantwortet")
        
        for i, question in enumerate(short_questions):
            st.write(f"**Frage {i+1}/30:** {question['text']}")
            
            # Antwort aus Session State laden oder Standardwert setzen
            current_response = st.session_state.screening_responses.get(question['id'], 3)
            
            response = st.radio(
                "Wie sehr stimmen Sie zu?",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: [
                    "Stimme überhaupt nicht zu",
                    "Stimme eher nicht zu", 
                    "Neutral / teils-teils",
                    "Stimme eher zu",
                    "Stimme völlig zu"
                ][x-1],
                key=f"quick_{question['id']}",
                index=current_response-1  # Index basierend auf gespeicherter Antwort
            )
            
            # Antwort sofort in Session State speichern
            st.session_state.screening_responses[question['id']] = response
        
        # Auswerten-Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔍 Screening Auswerten", type="primary", use_container_width=True):
                if len(st.session_state.screening_responses) >= 30:
                    scores = self._calculate_scores(st.session_state.screening_responses, is_short=True)
                    st.session_state.screening_completed = True
                    return scores
                else:
                    st.warning("Bitte beantworten Sie alle 30 Fragen bevor Sie auswerten.")
        
        return None

    def behavioral_questionnaire(self):
        """Vollversion mit 60 Fragen"""
        st.info("🔬 **Detaillierter Fragebogen mit 60 Fragen**")
        
        # Screening State setzen
        st.session_state.current_screening_type = "full"
        
        questions = self.all_questions
        
        # Fortschrittsbalken
        completed_questions = len(st.session_state.screening_responses)
        progress = completed_questions / 60
        st.progress(progress)
        st.write(f"Fortschritt: {completed_questions}/60 Fragen beantwortet")
        
        for i, question in enumerate(questions):
            st.write(f"**Frage {i+1}/60:** {question['text']}")
            
            # Antwort aus Session State laden oder Standardwert setzen
            current_response = st.session_state.screening_responses.get(question['id'], 3)
            
            response = st.radio(
                "Wie sehr stimmen Sie zu?",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: [
                    "Stimme überhaupt nicht zu",
                    "Stimme eher nicht zu", 
                    "Neutral / teils-teils",
                    "Stimme eher zu",
                    "Stimme völlig zu"
                ][x-1],
                key=f"full_{question['id']}",
                index=current_response-1  # Index basierend auf gespeicherter Antwort
            )
            
            # Antwort sofort in Session State speichern
            st.session_state.screening_responses[question['id']] = response
        
        # Auswerten-Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔍 Vollständiges Screening Auswerten", type="primary", use_container_width=True):
                if len(st.session_state.screening_responses) >= 60:
                    scores = self._calculate_scores(st.session_state.screening_responses, is_short=False)
                    st.session_state.screening_completed = True
                    return scores
                else:
                    st.warning("Bitte beantworten Sie alle 60 Fragen bevor Sie auswerten.")
        
        return None

    def _calculate_scores(self, responses, is_short=True):
        """Berechnet Scores für beide Versionen"""
        dimension_scores = {dim: 0 for dim in ['O', 'C', 'E', 'A', 'N']}
        dimension_counts = {dim: 0 for dim in ['O', 'C', 'E', 'A', 'N']}
        
        questions_to_use = self.all_questions[:30] if is_short else self.all_questions
        
        for question in questions_to_use:
            if question['id'] in responses:
                dimension = question['dimension']
                dimension_scores[dimension] += responses[question['id']]
                dimension_counts[dimension] += 1
        
        # Normalisiere auf 0-100 Skala
        final_scores = {}
        for dim in dimension_scores:
            if dimension_counts[dim] > 0:
                if is_short:
                    # 30 Fragen: 6 Fragen pro Dimension × 5 Punkte max = 30, ×3.33 ≈ 100
                    final_scores[dim] = (dimension_scores[dim] / dimension_counts[dim]) * 20
                else:
                    # 60 Fragen: 12 Fragen pro Dimension × 5 Punkte max = 60, ×1.67 ≈ 100
                    final_scores[dim] = (dimension_scores[dim] / dimension_counts[dim]) * 20
            else:
                final_scores[dim] = 50
        
        return final_scores

    def create_radar_chart(self, scores):
        """Erstellt ein Radar-Diagramm für die Big Five Scores"""
        if scores is None:
            return None
            
        import plotly.graph_objects as go
        
        # Feste Dimension-Namen
        dimension_names = {
            'O': 'Offenheit', 
            'C': 'Gewissenhaftigkeit', 
            'E': 'Extraversion',
            'A': 'Verträglichkeit', 
            'N': 'Neurotizismus'
        }
        
        # Sicherstellen, dass alle Dimensionen in korrekter Reihenfolge sind
        categories = ['Offenheit', 'Gewissenhaftigkeit', 'Extraversion', 'Verträglichkeit', 'Neurotizismus']
        values = [
            scores.get('O', 50),
            scores.get('C', 50), 
            scores.get('E', 50),
            scores.get('A', 50),
            scores.get('N', 50)
        ]
        
        # Radar Chart erstellen
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Ihr Profil',
            line=dict(color='blue'),
            fillcolor='rgba(0, 115, 230, 0.3)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickvals=[0, 25, 50, 75, 100],
                    ticktext=['0', '25', '50', '75', '100']
                ),
                angularaxis=dict(
                    direction="clockwise"
                )
            ),
            showlegend=True,
            title="Big Five Persönlichkeitsprofil",
            height=400
        )
        
        return fig

    def classify_profile(self, scores):
        """Klassifiziert das Persönlichkeitsprofil"""
        if scores is None:
            return {dim: "durchschnittlich" for dim in ['O', 'C', 'E', 'A', 'N']}
            
        profile = {}
        for dim, score in scores.items():
            if score >= 70:
                profile[dim] = "hoch"
            elif score <= 30:
                profile[dim] = "niedrig" 
            else:
                profile[dim] = "durchschnittlich"
        return profile

    def calculate_similarity(self, user_scores):
        """Berechnet Ähnlichkeit mit typischen Profilen"""
        if user_scores is None:
            return {}
            
        similarities = {}
        typical_profiles = {
            "Kreativer Innovator": {"O": 80, "C": 60, "E": 65, "A": 55, "N": 45},
            "Zuverlässiger Organisator": {"O": 45, "C": 85, "E": 50, "A": 60, "N": 40},
            "Sozialer Netzwerker": {"O": 60, "C": 50, "E": 80, "A": 70, "N": 35},
            "Teamplayer": {"O": 50, "C": 60, "E": 55, "A": 80, "N": 45},
            "Stabiler Problemlöser": {"O": 55, "C": 65, "E": 45, "A": 60, "N": 25}
        }
        
        for profile_name, typical_scores in typical_profiles.items():
            total_diff = 0
            for dim in ['O', 'C', 'E', 'A', 'N']:
                diff = abs(user_scores.get(dim, 50) - typical_scores[dim])
                total_diff += diff
            similarity = max(0, 100 - (total_diff / 5))
            similarities[profile_name] = similarity
        
        return similarities

    def reset_screening(self):
        """Setzt das Screening zurück"""
        st.session_state.screening_responses = {}
        st.session_state.screening_completed = False
        st.session_state.current_screening_type = None
