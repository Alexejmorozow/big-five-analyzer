import streamlit as st

class PersonalityScreener:
    def __init__(self):
        self.dimensions = ['O', 'C', 'E', 'A', 'N']
        self.dimension_names = {
            'O': 'Offenheit für Erfahrungen',
            'C': 'Gewissenhaftigkeit', 
            'E': 'Extraversion',
            'A': 'Verträglichkeit',
            'N': 'Neurotizismus'
        }
        
        # Vereinfachte Initialisierung
        self.setup_sample_data()
    
    def setup_sample_data(self):
        """Vereinfachte Dateninitialisierung - ohne numpy/pandas"""
        # Keine komplexen Datenstrukturen mehr nötig
        # Die Similarity-Berechnung verwendet jetzt einfache Logik
        pass
    
    def behavioral_questionnaire(self):
        """Fragebogen für verhaltensbasierte Einschätzung"""
        st.subheader("Verhaltensbasierte Persönlichkeitseinschätzung")
        
        questions = {
            'O': [
                "Ich probiere gerne neue Aktivitäten aus",
                "Ich habe eine lebhafte Vorstellungskraft",
                "Ich schätze Kunst und Ästhetik"
            ],
            'C': [
                "Ich erledige Aufgaben gründlich und genau",
                "Ich plane meine Aktivitäten im Voraus",
                "Ich halte mich an Fristen und Verpflichtungen"
            ],
            'E': [
                "Ich fühle mich in Gesellschaft anderer wohl",
                "Ich übernehme gerne die Führung in Gruppen",
                "Ich bin gesprächig und kontaktfreudig"
            ],
            'A': [
                "Ich helfe anderen gerne ohne Gegenleistung",
                "Ich vertraue anderen Menschen",
                "Ich vermeide Konflikte, wenn möglich"
            ],
            'N': [
                "Ich mache mir oft Sorgen",
                "Ich fühle mich häufig gestresst",
                "Meine Stimmung schwankt leicht"
            ]
        }
        
        scores = {dim: 0 for dim in self.dimensions}
        
        for dim, dim_questions in questions.items():
            st.write(f"**{self.dimension_names[dim]}**")
            for i, question in enumerate(dim_questions):
                response = st.slider(
                    f"{question}",
                    min_value=1,
                    max_value=5,
                    value=3,
                    key=f"{dim}_{i}"
                )
                scores[dim] += (response - 3) * 10  # Skalierung auf 0-100
        
        return scores
    
    def quick_screening(self):
        """Schnelles Screening mit minimalen Fragen"""
        st.subheader("Schnelles Screening (10 Fragen)")
        
        quick_questions = [
            ("Ich bin offen für neue Erfahrungen und Ideen", "O"),
            ("Ich bin organisiert und methodisch", "C"),
            ("Ich bin gesellig und energiegeladen", "E"),
            ("Ich bin kooperativ und hilfsbereit", "A"),
            ("Ich bin emotional stabil und gelassen", "N"),
            ("Ich habe eine lebhafte Fantasie", "O"),
            ("Ich bin zuverlässig und verantwortungsbewusst", "C"),
            ("Ich fühle mich in großen Gruppen wohl", "E"),
            ("Ich vertraue anderen leicht", "A"),
            ("Ich werde leicht nervös oder ängstlich", "N")
        ]
        
        scores = {dim: 50 for dim in self.dimensions}  # Start bei Mittelwert
        
        for i, (question, dimension) in enumerate(quick_questions):
            response = st.slider(
                question,
                min_value=1,
                max_value=5,
                value=3,
                key=f"quick_{i}"
            )
            # Anpassung basierend auf Antwort
            adjustment = (response - 3) * 8
            scores[dimension] += adjustment
        
        return scores
    
    def classify_profile(self, scores):
        """Klassifiziert das Persönlichkeitsprofil"""
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
        """Berechnet Ähnlichkeit mit typischen Profilen - vereinfachte Version"""
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
            for dim in self.dimensions:
                diff = abs(user_scores[dim] - typical_scores[dim])
                total_diff += diff
            # Umrechnung in Ähnlichkeit (0-100%)
            similarity = max(0, 100 - (total_diff / 5))
            similarities[profile_name] = similarity
        
        return similarities
