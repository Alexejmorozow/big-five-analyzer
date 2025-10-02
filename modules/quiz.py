import streamlit as st
import random
import time

class QuizModule:
    def __init__(self):
        self.all_questions = self.load_questions()
    
    def load_questions(self):
        """Lädt alle Fragen inklusive der neuen Erweiterungen"""
        return [
            # 📊 BASIS-FRAGEN
            {
                "id": 1, "difficulty": 1,
                "type": "likert_interpretation",
                "question": "Wie wahrscheinlich ist diese Interpretation des Verhaltens?",
                "scenario": "Eine Person beginnt jeden Tag um 7:00 Uhr, arbeitet strukturiert mit To-Do-Listen, und erledigt alle Aufgaben termingerecht.",
                "interpretations": [
                    "Hohe Gewissenhaftigkeit (strukturierte Arbeitsweise)",
                    "Niedrige Offenheit (Angst vor Spontaneität)", 
                    "Hoher Neurotizismus (Kontrollzwang)",
                    "Situative Anpassung (Probezeit)"
                ],
                "correct_likert": [4, 2, 3, 3],
                "explanation": "🔍 **Klassischer Fall hoher Gewissenhaftigkeit:** Struktur und Pünktlichkeit sind Kernmerkmale.",
                "learning_point": "Gewissenhaftigkeit zeigt sich in konsistenter Organisation über Zeit hinweg."
            },
            {
                "id": 2, "difficulty": 1,
                "type": "multiple_correct",
                "question": "Welche Dimensionen erklären dieses Verhalten am besten?",
                "scenario": "Jemand geht auf Partys auf fremde Menschen zu, initiiert Gespräche und scheint Energie aus sozialen Kontakten zu ziehen.",
                "options": [
                    "Hohe Extraversion (Geselligkeit, Energiegewinn)",
                    "Niedrige Verträglichkeit (Aufdringlichkeit)",
                    "Hohe Offenheit (Interesse an neuen Menschen)",
                    "Niedriger Neurotizismus (soziale Sicherheit)"
                ],
                "correct_answers": [0, 3],
                "explanation": "💃 **Extraversions-Muster:** Soziale Initiative + Energiegewinn = klassische Extraversion.",
                "learning_point": "Extraversion ≠ nur Geselligkeit, sondern auch Energiegewinn aus Sozialkontakten."
            },
            
            # 🔮 PHÄNOMEN-DEUTUNG
            {
                "id": 101, "difficulty": 2,
                "type": "phenomenon_interpretation",
                "question": "Wie könnte dieses Verhalten im Rahmen der Big Five gedeutet werden?",
                "scenario": "Eine Patientin in der Therapie vermeidet Blickkontakt, spricht sehr leise und zögert lange vor Antworten.",
                "possible_interpretations": [
                    "Hoher Neurotizismus (soziale Ängstlichkeit)",
                    "Niedrige Extraversion (introvertierte Grundtendenz)", 
                    "Hohe Verträglichkeit (konfliktscheues Verhalten)",
                    "Situative Reaktion (akute Belastung)",
                    "Kombination aus Neurotizismus und niedriger Extraversion"
                ],
                "valid_hypotheses": [0, 1, 2, 3, 4],
                "most_plausible": [0, 4, 3],
                "explanation": "🔍 **Mehrdeutige Phänomendeutung:** Verhaltensmuster können unterschiedliche Ursachen haben.",
                "learning_point": "Identische Verhaltensmuster können unterschiedliche Ursachen haben."
            },
            
            # ⏱️ FALLVERLÄUFE
            {
                "id": 102, "difficulty": 3,
                "type": "case_progression", 
                "question": "Handelt es sich um einen Persönlichkeitsstil oder einen situativen Zustand?",
                "scenario": "**Woche 1-4:** Ruhig, aber kompetent. **Woche 5-8:** Gereizt und kritisch. **Woche 9-12:** Normalisierung mit grundlegender Zurückhaltung.",
                "options": [
                    "Stabiler Persönlichkeitsstil mit situativer Überlagerung",
                    "Primär situative Reaktion auf extravertierter Basis",
                    "Entwicklung einer Persönlichkeitsänderung",
                    "Kombination aus stabiler Introversion + Belastungsreaktion"
                ],
                "correct_interpretation": [0, 3],
                "explanation": "⏱️ **Verlaufsdiagnostik:** Stabile Grundtendenz + situative Überlagerung.",
                "learning_point": "Verlaufsbeobachtung unterscheidet stabile Traits von state-abhängigen Reaktionen."
            }
        ]
    
    def display_quiz(self):
        """Hauptmethode zur Anzeige des Quizzes"""
        st.header("🧠 Big Five Clinical Reasoning Quiz")
        
        # Session State initialisieren
        if 'quiz_initialized' not in st.session_state:
            self._initialize_session_state()
        
        if not st.session_state.quiz_configurated:
            self.show_quiz_configuration()
            return
        
        if not st.session_state.quiz_started:
            self.show_quiz_intro()
            return
        
        if st.session_state.show_results:
            self.show_results()
        else:
            self.show_question()
    
    def _initialize_session_state(self):
        """Initialisiert den Session State komplett"""
        st.session_state.quiz_initialized = True
        st.session_state.quiz_configurated = False
        st.session_state.quiz_started = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.show_results = False
        st.session_state.last_action = None
    
    def show_quiz_configuration(self):
        """Zeigt die Quiz-Konfiguration"""
        st.markdown("## 🎯 Quiz konfigurieren")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔬 Kleines Quiz (2 Fragen)", use_container_width=True, key="btn_small"):
                self.setup_quiz("small")
        
        with col2:
            if st.button("🎓 Großes Quiz (4 Fragen)", use_container_width=True, key="btn_large"):
                self.setup_quiz("large")
    
    def setup_quiz(self, quiz_size):
        """Bereitet das Quiz vor"""
        all_questions = self.all_questions.copy()
        random.shuffle(all_questions)
        
        if quiz_size == "small":
            questions = all_questions[:2]
        else:
            questions = all_questions[:4]
        
        st.session_state.quiz_questions = questions
        st.session_state.quiz_configurated = True
        st.session_state.quiz_size = quiz_size
        st.rerun()
    
    def show_quiz_intro(self):
        """Zeigt die Quiz-Einleitung"""
        question_count = len(st.session_state.quiz_questions)
        st.success(f"**🎯 Quiz konfiguriert: {question_count} Fragen**")
        
        if st.button("🎯 Quiz starten", type="primary", use_container_width=True, key="btn_start"):
            st.session_state.quiz_started = True
            st.session_state.start_time = time.time()
            st.rerun()
    
    def show_question(self):
        """Zeigt die aktuelle Frage - KOMPLETT KORRIGIERT"""
        question_data = st.session_state.quiz_questions[st.session_state.current_question]
        
        # Fortschrittsanzeige
        progress = (st.session_state.current_question + 1) / len(st.session_state.quiz_questions)
        st.progress(progress)
        st.caption(f"Frage {st.session_state.current_question + 1} von {len(st.session_state.quiz_questions)}")
        
        st.markdown(f"### {question_data['question']}")
        
        if question_data.get('scenario'):
            with st.expander("📋 Fallvignette anzeigen", expanded=True):
                st.write(question_data['scenario'])
        
        # Fragetyp anzeigen
        if question_data['type'] == 'likert_interpretation':
            self.show_likert_question(question_data)
        elif question_data['type'] == 'multiple_correct':
            self.show_multiple_correct_question(question_data)
        elif question_data['type'] == 'phenomenon_interpretation':
            self.show_phenomenon_interpretation(question_data)
        elif question_data['type'] == 'case_progression':
            self.show_case_progression(question_data)
    
    def show_likert_question(self, question_data):
        """Zeigt Likert-Skalen Fragen"""
        st.write("**Bewerten Sie auf einer Skala von 1-5:**")
        
        user_ratings = []
        for i, interpretation in enumerate(question_data['interpretations']):
            rating = st.slider(
                f"{interpretation}",
                min_value=1, max_value=5, value=3,
                key=f"likert_{question_data['id']}_{i}"
            )
            user_ratings.append(rating)
        
        # WICHTIG: Nur einen Button pro Frage!
        if st.button("📊 Antwort auswerten", type="primary", key=f"eval_{question_data['id']}"):
            self.evaluate_likert_question(user_ratings, question_data)
            # Direkt nach der Auswertung den Next-Button zeigen
            self._show_next_button(question_data)
    
    def show_multiple_correct_question(self, question_data):
        """Zeigt Multiple-Choice-Fragen"""
        st.write("**Wählen Sie alle korrekten Aussagen:**")
        
        user_answers = st.multiselect(
            "Mehrfachauswahl:",
            question_data["options"],
            key=f"multiple_{question_data['id']}"
        )
        
        if st.button("✅ Antwort auswerten", type="primary", key=f"eval_{question_data['id']}"):
            self.evaluate_multiple_correct_question(user_answers, question_data)
            self._show_next_button(question_data)
    
    def show_phenomenon_interpretation(self, question_data):
        """Zeigt Phänomen-Deutungs-Fragen"""
        st.write("**Welche Interpretationen sind plausibel?**")
        
        user_answers = st.multiselect(
            "Mehrfachauswahl:",
            question_data["possible_interpretations"],
            key=f"phenomenon_{question_data['id']}"
        )
        
        if st.button("🔮 Antwort auswerten", type="primary", key=f"eval_{question_data['id']}"):
            self.evaluate_phenomenon_interpretation(user_answers, question_data)
            self._show_next_button(question_data)
    
    def show_case_progression(self, question_data):
        """Zeigt Fallverlaufs-Fragen"""
        st.write("**Analyse des Verhaltens über Zeit:**")
        
        user_answers = st.multiselect(
            "Wählen Sie zutreffende Interpretationen:",
            question_data["options"],
            key=f"case_{question_data['id']}"
        )
        
        if st.button("⏱️ Antwort auswerten", type="primary", key=f"eval_{question_data['id']}"):
            self.evaluate_case_progression(user_answers, question_data)
            self._show_next_button(question_data)
    
    def _show_next_button(self, question_data):
        """Zeigt den Next-Button - EINFACHE UND FUNKTIONIERENDE VERSION"""
        st.markdown("---")
        
        # WICHTIG: Ein ganz einfacher Button ohne komplexe Logik
        if st.button("➡️ **Nächste Frage**", type="primary", use_container_width=True, 
                    key=f"next_{question_data['id']}_{st.session_state.current_question}"):
            
            # Zur nächsten Frage oder zu den Ergebnissen
            if st.session_state.current_question + 1 < len(st.session_state.quiz_questions):
                st.session_state.current_question += 1
            else:
                st.session_state.show_results = True
            
            # Rerun erzwingen
            st.rerun()

    # ========== EVALUATIONS-METHODEN ==========
    
    def evaluate_likert_question(self, user_ratings, question_data):
        """Bewertet Likert-Skalen Fragen"""
        correct_ratings = question_data['correct_likert']
        deviations = [abs(user - correct) for user, correct in zip(user_ratings, correct_ratings)]
        accuracy = max(0, 100 - (sum(deviations) / (len(correct_ratings) * 4)) * 100)
        
        st.subheader("📊 Auswertung")
        
        if accuracy >= 80:
            st.success(f"🎉 Exzellente Einschätzung! ({accuracy:.1f}%)")
        elif accuracy >= 60:
            st.warning(f"👍 Gute Einschätzung ({accuracy:.1f}%)")
        else:
            st.error(f"📚 Abweichungen ({accuracy:.1f}%)")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
    
    def evaluate_multiple_correct_question(self, user_answers, question_data):
        """Bewertet Multiple-Choice-Fragen"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_answers"]
        correct_selected = len(set(user_indices) & set(correct_indices))
        
        st.subheader("✅ Auswertung")
        
        if correct_selected == len(correct_indices):
            st.success("🎉 Perfekt! Vollständiges Wissen.")
            st.session_state.score += 1
        else:
            st.warning("👍 Korrekt, aber nicht vollständig.")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
    
    def evaluate_phenomenon_interpretation(self, user_answers, question_data):
        """Bewertet Phänomen-Deutungen"""
        user_indices = [question_data["possible_interpretations"].index(ans) for ans in user_answers]
        correct_selections = len(set(user_indices) & set(question_data["valid_hypotheses"]))
        
        st.subheader("🔮 Auswertung")
        
        if correct_selections == len(question_data["valid_hypotheses"]):
            st.success("🎉 Vollständiges Hypothesenspektrum erkannt!")
            st.session_state.score += 1
        else:
            st.warning("👍 Gute Auswahl")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
    
    def evaluate_case_progression(self, user_answers, question_data):
        """Bewertet Fallverlaufs-Analysen"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_interpretation"]
        
        st.subheader("⏱️ Auswertung")
        
        if set(user_indices) == set(correct_indices):
            st.success("🎉 Exzellente Verlaufsanalyse!")
            st.session_state.score += 1
        else:
            st.error("❌ Verbesserungsfähig")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
    
    def show_results(self):
        """Zeigt die Quiz-Ergebnisse"""
        st.header("📊 Quiz abgeschlossen!")
        
        total = len(st.session_state.quiz_questions)
        score = st.session_state.score
        percentage = (score / total) * 100
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Richtige Antworten", f"{score}/{total}")
        with col2:
            st.metric("Erfolgsquote", f"{percentage:.1f}%")
        
        # Neustart-Button
        st.markdown("---")
        if st.button("🔄 Neues Quiz starten", type="primary", use_container_width=True, key="restart"):
            # Session State komplett zurücksetzen
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
