import streamlit as st
import random
from typing import Dict, List, Any

class PersonalityScreener:
    def __init__(self):
        self.dimensions = self.initialize_dimensions()
        self.all_questions = self.load_questions()
        self.randomized_questions = None
        
    def initialize_dimensions(self):
        """Initialisiert die NEO PI R Struktur mit 30 Facetten"""
        return {
            'N': {
                'name': 'Neurotizismus',
                'facets': {
                    'N1': {'name': 'Ängstlichkeit', 'questions': [1, 2], 'score': 0},
                    'N2': {'name': 'Reizbarkeit', 'questions': [3, 4], 'score': 0},
                    'N3': {'name': 'Depression', 'questions': [5, 6], 'score': 0},
                    'N4': {'name': 'Soziale Befangenheit', 'questions': [7, 8], 'score': 0},
                    'N5': {'name': 'Impulsivität', 'questions': [9, 10], 'score': 0},
                    'N6': {'name': 'Verletzlichkeit', 'questions': [11, 12], 'score': 0}
                },
                'total_score': 0
            },
            'E': {
                'name': 'Extraversion',
                'facets': {
                    'E1': {'name': 'Herzlichkeit', 'questions': [13, 14], 'score': 0},
                    'E2': {'name': 'Geselligkeit', 'questions': [15, 16], 'score': 0},
                    'E3': {'name': 'Durchsetzungsfähigkeit', 'questions': [17, 18], 'score': 0},
                    'E4': {'name': 'Aktivität', 'questions': [19, 20], 'score': 0},
                    'E5': {'name': 'Erlebnishunger', 'questions': [21, 22], 'score': 0},
                    'E6': {'name': 'Frohsinn', 'questions': [23, 24], 'score': 0}
                },
                'total_score': 0
            },
            'O': {
                'name': 'Offenheit für Erfahrungen',
                'facets': {
                    'O1': {'name': 'Fantasie', 'questions': [25, 26], 'score': 0},
                    'O2': {'name': 'Ästhetik', 'questions': [27, 28], 'score': 0},
                    'O3': {'name': 'Gefühle', 'questions': [29, 30], 'score': 0},
                    'O4': {'name': 'Handlungen', 'questions': [31, 32], 'score': 0},
                    'O5': {'name': 'Ideen', 'questions': [33, 34], 'score': 0},
                    'O6': {'name': 'Normen und Werte', 'questions': [35, 36], 'score': 0}
                },
                'total_score': 0
            },
            'A': {
                'name': 'Verträglichkeit',
                'facets': {
                    'A1': {'name': 'Vertrauen', 'questions': [37, 38], 'score': 0},
                    'A2': {'name': 'Freimütigkeit', 'questions': [39, 40], 'score': 0},
                    'A3': {'name': 'Altruismus', 'questions': [41, 42], 'score': 0},
                    'A4': {'name': 'Entgegenkommen', 'questions': [43, 44], 'score': 0},
                    'A5': {'name': 'Bescheidenheit', 'questions': [45, 46], 'score': 0},
                    'A6': {'name': 'Gutherzigkeit', 'questions': [47, 48], 'score': 0}
                },
                'total_score': 0
            },
            'C': {
                'name': 'Gewissenhaftigkeit',
                'facets': {
                    'C1': {'name': 'Kompetenz', 'questions': [49, 50], 'score': 0},
                    'C2': {'name': 'Ordnungsliebe', 'questions': [51, 52], 'score': 0},
                    'C3': {'name': 'Pflichtbewusstsein', 'questions': [53, 54], 'score': 0},
                    'C4': {'name': 'Leistungsstreben', 'questions': [55, 56], 'score': 0},
                    'C5': {'name': 'Selbstdisziplin', 'questions': [57, 58], 'score': 0},
                    'C6': {'name': 'Besonnenheit', 'questions': [59, 60], 'score': 0}
                },
                'total_score': 0
            }
        }
    
    def load_questions(self):
        """Lädt alle 60 Fragen korrekt nach Facetten verteilt"""
        questions = [
            # Neurotizismus (N) - Fragen 1-12
            {"id": 1, "text": "Ich mache mir oft Sorgen über Dinge, die schiefgehen könnten.", "dimension": "N", "facet": "N1"},
            {"id": 2, "text": "Ich fühle mich häufig nervös oder angespannt.", "dimension": "N", "facet": "N1"},
            {"id": 3, "text": "Ich ärgere mich leicht über Kleinigkeiten.", "dimension": "N", "facet": "N2"},
            {"id": 4, "text": "Ich reagiere oft empfindlich auf Kritik oder Frustrationen.", "dimension": "N", "facet": "N2"},
            {"id": 5, "text": "Ich fühle mich gelegentlich traurig oder niedergeschlagen.", "dimension": "N", "facet": "N3"},
            {"id": 6, "text": "Ich verliere manchmal die Motivation, Dinge zu erledigen.", "dimension": "N", "facet": "N3"},
            {"id": 7, "text": "Ich fühle mich in neuen sozialen Situationen unsicher.", "dimension": "N", "facet": "N4"},
            {"id": 8, "text": "Ich meide manchmal Begegnungen mit fremden Menschen.", "dimension": "N", "facet": "N4"},
            {"id": 9, "text": "Ich handle oft spontan, ohne vorher über die Folgen nachzudenken.", "dimension": "N", "facet": "N5"},
            {"id": 10, "text": "Ich habe Schwierigkeiten, mich in stressigen Momenten zu beherrschen.", "dimension": "N", "facet": "N5"},
            {"id": 11, "text": "Ich fühle mich schnell überfordert, wenn viel auf einmal passiert.", "dimension": "N", "facet": "N6"},
            {"id": 12, "text": "Stresssituationen setzen mir stark zu.", "dimension": "N", "facet": "N6"},
            
            # Extraversion (E) - Fragen 13-24
            {"id": 13, "text": "Es fällt mir leicht, Freundschaften zu schließen.", "dimension": "E", "facet": "E1"},
            {"id": 14, "text": "Ich gehe offen auf andere Menschen zu.", "dimension": "E", "facet": "E1"},
            {"id": 15, "text": "Ich verbringe gerne Zeit mit anderen Menschen.", "dimension": "E", "facet": "E2"},
            {"id": 16, "text": "Ich genieße es, Teil einer Gruppe zu sein.", "dimension": "E", "facet": "E2"},
            {"id": 17, "text": "Ich übernehme oft die Leitung in Gruppenprojekten.", "dimension": "E", "facet": "E3"},
            {"id": 18, "text": "Ich äußere meine Meinung klar, auch wenn sie von anderen abweicht.", "dimension": "E", "facet": "E3"},
            {"id": 19, "text": "Ich bin gern beschäftigt und immer aktiv.", "dimension": "E", "facet": "E4"},
            {"id": 20, "text": "Ich erledige Aufgaben lieber frühzeitig als auf den letzten Drücker.", "dimension": "E", "facet": "E4"},
            {"id": 21, "text": "Ich probiere gerne neue Aktivitäten und Erfahrungen aus.", "dimension": "E", "facet": "E5"},
            {"id": 22, "text": "Ich suche oft nach Abwechslung in meinem Alltag.", "dimension": "E", "facet": "E5"},
            {"id": 23, "text": "Ich bin häufig gut gelaunt und optimistisch.", "dimension": "E", "facet": "E6"},
            {"id": 24, "text": "Ich lache leicht über kleine Dinge.", "dimension": "E", "facet": "E6"},
            
            # Offenheit (O) - Fragen 25-36
            {"id": 25, "text": "Ich verliere mich oft in Tagträumen.", "dimension": "O", "facet": "O1"},
            {"id": 26, "text": "Ich stelle mir gerne alternative Szenarien oder Möglichkeiten vor.", "dimension": "O", "facet": "O1"},
            {"id": 27, "text": "Ich interessiere mich stark für Kunst, Musik oder Literatur.", "dimension": "O", "facet": "O2"},
            {"id": 28, "text": "Ich achte auf Schönheit in meiner Umgebung.", "dimension": "O", "facet": "O2"},
            {"id": 29, "text": "Ich bin mir meiner eigenen Gefühle oft bewusst.", "dimension": "O", "facet": "O3"},
            {"id": 30, "text": "Ich empfinde Emotionen intensiv.", "dimension": "O", "facet": "O3"},
            {"id": 31, "text": "Ich probiere gerne neue Aktivitäten oder Hobbys aus.", "dimension": "O", "facet": "O4"},
            {"id": 32, "text": "Ich reise gerne an unbekannte Orte, um Neues zu entdecken.", "dimension": "O", "facet": "O4"},
            {"id": 33, "text": "Ich beschäftige mich gern mit abstrakten oder komplexen Ideen.", "dimension": "O", "facet": "O5"},
            {"id": 34, "text": "Ich interessiere mich für wissenschaftliche, philosophische oder theoretische Themen.", "dimension": "O", "facet": "O5"},
            {"id": 35, "text": "Ich hinterfrage oft gesellschaftliche Normen und Regeln.", "dimension": "O", "facet": "O6"},
            {"id": 36, "text": "Ich entwickle eigene Wertvorstellungen und halte an ihnen fest.", "dimension": "O", "facet": "O6"},
            
            # Verträglichkeit (A) - Fragen 37-48
            {"id": 37, "text": "Ich gehe davon aus, dass die meisten Menschen gute Absichten haben.", "dimension": "A", "facet": "A1"},
            {"id": 38, "text": "Ich vertraue anderen meist von Natur aus.", "dimension": "A", "facet": "A1"},
            {"id": 39, "text": "Ich teile offen meine Gedanken und Gefühle mit anderen.", "dimension": "A", "facet": "A2"},
            {"id": 40, "text": "Ich bin bereit, meine Meinung ehrlich zu äußern, auch wenn sie nicht populär ist.", "dimension": "A", "facet": "A2"},
            {"id": 41, "text": "Ich helfe anderen gern, auch wenn es mich Zeit oder Mühe kostet.", "dimension": "A", "facet": "A3"},
            {"id": 42, "text": "Ich setze die Bedürfnisse anderer manchmal über meine eigenen.", "dimension": "A", "facet": "A3"},
            {"id": 43, "text": "Ich versuche, Konflikte durch Kompromisse zu lösen.", "dimension": "A", "facet": "A4"},
            {"id": 44, "text": "Ich gehe flexibel auf Wünsche und Vorschläge anderer ein.", "dimension": "A", "facet": "A4"},
            {"id": 45, "text": "Ich halte mich in Gruppen eher zurück, wenn andere sich präsentieren.", "dimension": "A", "facet": "A5"},
            {"id": 46, "text": "Ich betone meine eigenen Leistungen selten.", "dimension": "A", "facet": "A5"},
            {"id": 47, "text": "Ich empfinde Mitgefühl für Menschen in Not.", "dimension": "A", "facet": "A6"},
            {"id": 48, "text": "Ich bemühe mich, freundlich und hilfsbereit zu sein.", "dimension": "A", "facet": "A6"},
            
            # Gewissenhaftigkeit (C) - Fragen 49-60
            {"id": 49, "text": "Ich fühle mich in der Regel gut vorbereitet auf meine Aufgaben.", "dimension": "C", "facet": "C1"},
            {"id": 50, "text": "Ich bin überzeugt davon, meine Aufgaben erfolgreich erledigen zu können.", "dimension": "C", "facet": "C1"},
            {"id": 51, "text": "Ich lege Wert auf ein ordentliches und strukturiertes Umfeld.", "dimension": "C", "facet": "C2"},
            {"id": 52, "text": "Ich plane meine Aktivitäten sorgfältig.", "dimension": "C", "facet": "C2"},
            {"id": 53, "text": "Ich halte mich gewissenhaft an Regeln und Verpflichtungen.", "dimension": "C", "facet": "C3"},
            {"id": 54, "text": "Ich erledige Aufgaben zuverlässig und termingerecht.", "dimension": "C", "facet": "C3"},
            {"id": 55, "text": "Ich setze mir hohe Ziele und arbeite zielstrebig darauf hin.", "dimension": "C", "facet": "C4"},
            {"id": 56, "text": "Ich bemühe mich, in allem, was ich tue, mein Bestes zu geben.", "dimension": "C", "facet": "C4"},
            {"id": 57, "text": "Ich bleibe auch bei unangenehmen Aufgaben dran, bis sie erledigt sind.", "dimension": "C", "facet": "C5"},
            {"id": 58, "text": "Ich kann mich gut motivieren, auch wenn ich keine unmittelbare Belohnung erwarte.", "dimension": "C", "facet": "C5"},
            {"id": 59, "text": "Ich überlege, bevor ich Entscheidungen treffe.", "dimension": "C", "facet": "C6"},
            {"id": 60, "text": "Ich handle bedacht und vermeide impulsive Entscheidungen.", "dimension": "C", "facet": "C6"}
        ]
        
        return questions

    # KOMPATIBILITÄTS-METHODEN für alte app.py (FEHLERFREI)
    def quick_screening(self):
        """Kompatibilitätsmethode für alte app.py - Kurzversion mit 10 Fragen"""
        st.info("🚀 **Schnelles Screening mit 10 Fragen**")
        
        # Erstelle einfache Fragen für Kompatibilität
        questions = self.create_short_version()
        responses = {}
        
        for i, question in enumerate(questions):
            st.write(f"**{question['text']}**")
            
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
                key=f"quick_{question['id']}_{i}"  # EINDEUTIGE Keys
            )
            responses[question['id']] = response
        
        # EINDEUTIGER Button-Key
        if st.button("Auswerten", type="primary", key="quick_evaluate"):
            scores = self._calculate_short_scores(responses)
            return scores
        
        return None  # Keine Default-Werte mehr
    
    def behavioral_questionnaire(self):
        """Kompatibilitätsmethode für alte app.py - Vollversion"""
        st.info("🔬 **Detaillierter Fragebogen mit 60 Fragen**")
        
        questions = self.all_questions
        responses = {}
        
        for i, question in enumerate(questions):
            st.write(f"**{question['text']}**")
            
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
                key=f"full_{question['id']}_{i}"  # EINDEUTIGE Keys
            )
            responses[question['id']] = response
        
        # EINDEUTIGER Button-Key
        if st.button("Auswerten", type="primary", key="full_evaluate"):
            scores = self._calculate_full_scores(responses)
            return scores
        
        return None  # Keine Default-Werte mehr

    def _calculate_short_scores(self, responses):
        """Berechnet Scores für Kurzversion"""
        dimension_scores = {dim: 0 for dim in ['O', 'C', 'E', 'A', 'N']}
        dimension_counts = {dim: 0 for dim in ['O', 'C', 'E', 'A', 'N']}
        
        for question in self.create_short_version():
            if question['id'] in responses:
                dimension = question['dimension']
                dimension_scores[dimension] += responses[question['id']]
                dimension_counts[dimension] += 1
        
        # Normalisiere auf 0-100 Skala
        final_scores = {}
        for dim in dimension_scores:
            if dimension_counts[dim] > 0:
                final_scores[dim] = (dimension_scores[dim] / dimension_counts[dim]) * 20
            else:
                final_scores[dim] = 50
        
        return final_scores

    def _calculate_full_scores(self, responses):
        """Berechnet Scores für Vollversion"""
        # Reset Scores
        for dim in self.dimensions.values():
            dim['total_score'] = 0
            for facet in dim['facets'].values():
                facet['score'] = 0
        
        # Berechne Facet-Scores
        for question in self.all_questions:
            if question['id'] in responses:
                response = responses[question['id']]
                dimension = question['dimension']
                facet = question['facet']
                
                self.dimensions[dimension]['facets'][facet]['score'] += response
        
        # Berechne Dimension-Scores
        dimension_scores = {}
        for dim_code, dim_data in self.dimensions.items():
            facet_scores = [facet['score'] for facet in dim_data['facets'].values()]
            dim_data['total_score'] = sum(facet_scores) / len(facet_scores) * 10
            dimension_scores[dim_code] = dim_data['total_score']
        
        return dimension_scores

    def create_short_version(self):
        """Erstellt eine Kurzversion mit 10 Fragen (2 pro Dimension)"""
        short_questions = []
        
        dimension_representatives = {
            'O': [31, 33],  # Handlungen + Ideen
            'C': [49, 55],  # Kompetenz + Leistungsstreben  
            'E': [13, 19],  # Herzlichkeit + Aktivität
            'A': [37, 41],  # Vertrauen + Altruismus
            'N': [1, 7]     # Ängstlichkeit + Soziale Befangenheit
        }
        
        for dim, question_ids in dimension_representatives.items():
            for q_id in question_ids:
                question = next(q for q in self.all_questions if q['id'] == q_id)
                short_questions.append(question)
        
        return short_questions

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
        """Kompatibilitätsmethode für Ähnlichkeitsanalyse"""
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

# Hauptprogramm
if __name__ == "__main__":
    screener = PersonalityScreener()
