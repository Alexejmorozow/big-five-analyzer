import streamlit as st
import json
import random

class QuizModule:
    def __init__(self):
        self.questions = self.load_questions()
        self.user_answers = {}
    
    def load_questions(self):
        """Lädt die Quiz-Fragen"""
        # In einer echten Implementierung würde dies aus einer Datei geladen
        return [
            {
                "id": 1,
                "question": "Was ist das Fünf-Faktoren-Modell (Big Five) und warum gilt es als Standardmodell?",
                "answer": "Das FFM postuliert fünf Hauptdimensionen der Persönlichkeit und gilt als Standardmodell aufgrund umfangreicher wissenschaftlicher Validierung in über 3.000 Studien."
            },
            {
                "id": 2, 
                "question": "Beschreiben Sie den lexikalischen Ansatz.",
                "answer": "Der lexikalische Ansatz basiert auf der Annahme, dass sich wichtige Persönlichkeitsmerkmale in der Sprache niederschlagen. Aus 18.000 Begriffen wurden fünf stabile Faktoren extrahiert."
            },
            {
                "id": 3,
                "question": "Welche Kritikpunkte hat Dan McAdams am Big-Five-Modell?",
                "answer": "McAdams kritisiert die mangelnde Erklärungstiefe, Vernachlässigung von Erfahrungen, unzureichende Verhaltensvorhersage und fehlende Berücksichtigung situativer Aspekte."
            }
        ]
    
    def display_quiz(self):
        """Zeigt das Quiz an"""
        st.header("Big Five Wissensquiz")
        
        if 'quiz_started' not in st.session_state:
            st.session_state.quiz_started = False
            st.session_state.current_question = 0
            st.session_state.score = 0
        
        if not st.session_state.quiz_started:
            if st.button("Quiz starten"):
                st.session_state.quiz_started = True
                st.rerun()
            return
        
        if st.session_state.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()
    
    def show_question(self):
        """Zeigt die aktuelle Frage"""
        question_data = self.questions[st.session_state.current_question]
        
        st.subheader(f"Frage {st.session_state.current_question + 1}")
        st.write(question_data["question"])
        
        user_answer = st.text_area(
            "Ihre Antwort:",
            key=f"answer_{st.session_state.current_question}",
            height=100
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Antwort überprüfen"):
                self.check_answer(user_answer, question_data["answer"])
        
        with col2:
            if st.button("Überspringen"):
                st.session_state.current_question += 1
                st.rerun()
    
    def check_answer(self, user_answer, correct_answer):
        """Überprüft die Antwort des Nutzers"""
        # Einfache Ähnlichkeitsprüfung (in einer echten App würde man NLP verwenden)
        user_words = set(user_answer.lower().split())
        correct_words = set(correct_answer.lower().split())
        
        common_words = user_words.intersection(correct_words)
        similarity = len(common_words) / len(correct_words) if correct_words else 0
        
        if similarity > 0.3:  # Schwellenwert für korrekte Antwort
            st.session_state.score += 1
            st.success("Richtige Antwort! 🎉")
        else:
            st.error("Das war nicht ganz korrekt.")
            
        with st.expander("Korrekte Antwort anzeigen"):
            st.write(correct_answer)
        
        if st.button("Nächste Frage"):
            st.session_state.current_question += 1
            st.rerun()
    
    def show_results(self):
        """Zeigt die Quiz-Ergebnisse"""
        st.header("Quiz abgeschlossen!")
        
        score = st.session_state.score
        total = len(self.questions)
        percentage = (score / total) * 100
        
        st.metric("Punktzahl", f"{score}/{total} ({percentage:.1f}%)")
        
        if percentage >= 80:
            st.success("Ausgezeichnet! Sie haben ein sehr gutes Verständnis der Big Five.")
        elif percentage >= 60:
            st.warning("Gut! Sie haben die Grundlagen verstanden.")
        else:
            st.error("Empfehlung: Wiederholen Sie das Trainingsmodul.")
        
        if st.button("Quiz neu starten"):
            st.session_state.quiz_started = False
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.rerun()
