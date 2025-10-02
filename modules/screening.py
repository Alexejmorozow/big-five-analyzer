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
        
        # Beispielhafte Trainingsdaten für ML-Modell
        self.setup_sample_data()
    
    def setup_sample_data(self):
        """Erstellt Beispieldaten für das ML-Modell"""
        np.random.seed(42)
        n_samples = 1000
        
        # Simulierte Persönlichkeitsprofile
        self.sample_profiles = pd.DataFrame({
            'O': np.random.normal(50, 15, n_samples),
            'C': np.random.normal(50, 15, n_samples),
            'E': np.random.normal(50, 15, n_samples),
            'A': np.random.normal(50, 15, n_samples),
            'N': np.random.normal(50, 15, n_samples)
        })
        
        # Skalierung
        self.scaler = StandardScaler()
        self.scaler.fit(self.sample_profiles)
    
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
        """Berechnet Ähnlichkeit mit typischen Profilen"""
        user_array = np.array([user_scores[dim] for dim in self.dimensions]).reshape(1, -1)
        user_scaled = self.scaler.transform(user_array)
        
        # Beispielhafte Ähnlichkeitsberechnung
        similarities = {}
        typical_profiles = {
            "Kreativer Innovator": [80, 60, 65, 55, 45],
            "Zuverlässiger Organisator": [45, 85, 50, 60, 40],
            "Sozialer Netzwerker": [60, 50, 80, 70, 35],
            "Teamplayer": [50, 60, 55, 80, 45],
            "Stabiler Problemlöser": [55, 65, 45, 60, 25]
        }
        
        for profile_name, typical_scores in typical_profiles.items():
            typical_array = np.array(typical_scores).reshape(1, -1)
            typical_scaled = self.scaler.transform(typical_array)
            similarity = 1 - np.abs(user_scaled - typical_scaled).mean()
            similarities[profile_name] = max(0, similarity * 100)
        
        return similarities
