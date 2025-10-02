import streamlit as st
import json

class RecommendationEngine:
    def __init__(self):
        self.recommendations = self.load_recommendations()
    
    def load_recommendations(self):
        """Lädt die Handlungsempfehlungen"""
        # In einer echten Implementierung würde dies aus einer Datei geladen
        return {
            "O": {
                "high": [
                    "Bieten Sie kreative Freiheit und Experimentiermöglichkeiten",
                    "Ermutigen Sie zu Innovation und neuen Ideen",
                    "Geben Sie abwechslungsreiche und komplexe Aufgaben"
                ],
                "low": [
                    "Geben Sie klare Strukturen und bewährte Prozesse",
                    "Vermeiden Sie unnötige Veränderungen",
                    "Bieten Sie stabile, vorhersehbare Arbeitsbedingungen"
                ]
            },
            "C": {
                "high": [
                    "Übertragen Sie verantwortungsvolle Aufgaben mit klaren Deadlines",
                    "Nutzen Sie ihre Organisationsstärke für Planungsaufgaben",
                    "Vertrauen Sie ihnen wichtige Projekte an"
                ],
                "low": [
                    "Bieten Sie enge Betreuung und regelmäßige Check-ins",
                    "Setzen Sie klare, kurzfristige Ziele",
                    "Brechen Sie große Aufgaben in kleine Schritte auf"
                ]
            },
            "E": {
                "high": [
                    "Ermöglichen Sie Teamarbeit und soziale Interaktion",
                    "Geben Sie Möglichkeiten zur Präsentation und Kommunikation",
                    "Nutzen Sie ihre Energie für Kundenkontakte"
                ],
                "low": [
                    "Respektieren Sie Rückzugsräume und ungestörte Arbeitszeiten",
                    "Kommunizieren Sie schriftlich, wenn möglich",
                    "Bieten Sie fokussierte Einzelarbeit"
                ]
            },
            "A": {
                "high": [
                    "Fördern Sie Teamarbeit und kooperative Projekte",
                    "Schätzen Sie ihre Hilfsbereitschaft wert",
                    "Nutzen Sie ihre Fähigkeit zur Konfliktlösung"
                ],
                "low": [
                    "Nutzen Sie ihre Durchsetzungsfähigkeit in Verhandlungen",
                    "Geben Sie klare Wettbewerbsziele",
                    "Setzen Sie sie in herausfordernden Verkaufssituationen ein"
                ]
            },
            "N": {
                "high": [
                    "Bieten Sie emotionale Unterstützung und klare Rückmeldungen",
                    "Minimieren Sie Stressfaktoren und Ungewissheit",
                    "Geben Sie konstruktives, nicht kritisches Feedback"
                ],
                "low": [
                    "Vertrauen Sie ihnen verantwortungsvolle Aufgaben an",
                    "Nutzen Sie ihre Gelassenheit in Krisensituationen",
                    "Setzen Sie sie unter Druck ein, wo Stabilität benötigt wird"
                ]
            }
        }
    
    def generate_recommendations(self, profile, scores):
        """Generiert personalisierte Handlungsempfehlungen"""
        st.header("Personalisiertes Feedback & Handlungsempfehlungen")
        
        # Hauptempfehlungen basierend auf Profil
        st.subheader("Ihre Hauptstärken und Entwicklungsbereiche")
        
        strengths = []
        development_areas = []
        
        for dim, level in profile.items():
            if level == "hoch" and dim != "N":  # Neurotizismus ist anders zu bewerten
                strengths.append(dim)
            elif level == "niedrig" and dim == "C":  # Niedrige Gewissenhaftigkeit ist oft entwicklungsbedürftig
                development_areas.append(dim)
            elif level == "hoch" and dim == "N":  # Hoher Neurotizismus kann entwicklungsbedürftig sein
                development_areas.append(dim)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Ihre Stärken:**")
            for strength in strengths:
                st.success(f"• {self.get_dimension_name(strength)}")
        
        with col2:
            st.write("**Entwicklungsbereiche:**")
            for area in development_areas:
                st.warning(f"• {self.get_dimension_name(area)}")
        
        # Detaillierte Empfehlungen pro Dimension
        st.subheader("Detaillierte Handlungsempfehlungen")
        
        for dim, level in profile.items():
            with st.expander(f"Empfehlungen für {self.get_dimension_name(dim)} ({level})"):
                if level in self.recommendations[dim]:
                    for recommendation in self.recommendations[dim][level]:
                        st.write(f"• {recommendation}")
        
        # Berufliche Passungsempfehlungen
        self.show_career_recommendations(profile, scores)
    
    def get_dimension_name(self, dimension_code):
        """Gibt den vollständigen Namen einer Dimension zurück"""
        names = {
            'O': 'Offenheit für Erfahrungen',
            'C': 'Gewissenhaftigkeit',
            'E': 'Extraversion', 
            'A': 'Verträglichkeit',
            'N': 'Neurotizismus'
        }
        return names.get(dimension_code, dimension_code)
    
    def show_career_recommendations(self, profile, scores):
        """Zeigt berufliche Passungsempfehlungen"""
        st.subheader("Berufliche Passungsempfehlungen")
        
        career_suggestions = []
        
        # Einfache Logik für Berufsempfehlungen
        if profile.get('O') == 'hoch' and scores['O'] > 70:
            career_suggestions.append("Kreative Berufe (Design, Forschung, Kunst)")
        
        if profile.get('C') == 'hoch' and scores['C'] > 70:
            career_suggestions.append("Strukturierte Berufe (Projektmanagement, Buchhaltung, Qualitätssicherung)")
        
        if profile.get('E') == 'hoch' and scores['E'] > 70:
            career_suggestions.append("Soziale Berufe (Vertrieb, Personalwesen, Führung)")
        
        if profile.get('A') == 'hoch' and scores['A'] > 70:
            career_suggestions.append("Hilfsberufe (Sozialarbeit, Pflege, Teaching)")
        
        if profile.get('N') == 'niedrig' and scores['N'] < 30:
            career_suggestions.append("Stressresistente Berufe (Notfallmanagement, Börsenhandel)")
        
        if career_suggestions:
            st.write("Basierend auf Ihrem Profil könnten diese Bereiche gut zu Ihnen passen:")
            for suggestion in career_suggestions:
                st.info(f"• {suggestion}")
        else:
            st.info("Ihr Profil ist vielseitig - Sie könnten in verschiedenen Bereichen erfolgreich sein!")
        
        # Teamrollen-Empfehlungen
        st.subheader("Empfohlene Teamrollen")
        
        if profile.get('O') == 'hoch':
            st.write("• **Innovator**: Bringt neue Ideen und kreative Lösungen ein")
        if profile.get('C') == 'hoch':
            st.write("• **Organisator**: Kümmert sich um Planung und Struktur")
        if profile.get('E') == 'hoch':
            st.write("• **Kommunikator**: Übernimmt Moderation und Teambindung")
        if profile.get('A') == 'hoch':
            st.write("• **Teamplayer**: Fördert Harmonie und Zusammenarbeit")
