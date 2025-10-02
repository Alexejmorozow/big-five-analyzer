import streamlit as st
import random
import time

class QuizModule:
    def __init__(self):
        self.all_questions = self.load_questions()
    
    def load_questions(self):
        """Lädt alle Fragen mit verschiedenen Schwierigkeitsgraden und Fragetypen"""
        return [
            # 📊 EINFACH - Eindeutige Fälle (Schwierigkeitsgrad 1)
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
                "probabilistic_feedback": {
                    "Gewissenhaftigkeit": "85%",
                    "Neurotizismus": "45%", 
                    "Situativ": "35%",
                    "Offenheit": "15%"
                },
                "explanation": "🔍 **Klassischer Fall hoher Gewissenhaftigkeit:** Struktur und Pünktlichkeit sind Kernmerkmale. Neurotizismus wäre nur bei ängstlicher Überkontrolle wahrscheinlicher.",
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
                "explanation": "💃 **Extraversions-Muster:** Soziale Initiative + Energiegewinn = klassische Extraversion. Geringe soziale Ängste (niedriger Neurotizismus) unterstützen dieses Verhalten.",
                "learning_point": "Extraversion ≠ nur Geselligkeit, sondern auch Energiegewinn aus Sozialkontakten."
            },
            
            # 📈 MITTEL - Mehrdeutige Fälle (Schwierigkeitsgrad 2)
            {
                "id": 3, "difficulty": 2, 
                "type": "behavioral_interpretation",
                "question": "Eine Person zieht sich in sozialen Situationen häufig zurück und spricht wenig. Wie könnte dieses Verhalten gedeutet werden?",
                "scenario": "Team-Meeting: Maria sitzt meist still in der Ecke, spricht nur wenn direkt angesprochen, und verlässt die Räumlichkeiten schnell nach dem Meeting.",
                "options": [
                    "Könnte auf niedrige Extraversion hindeuten (introvertierte Tendenzen)",
                    "Könnte Ausdruck hoher Verträglichkeit sein (Konfliktvermeidung)", 
                    "Könnte durch hohen Neurotizismus erklärbar sein (soziale Ängstlichkeit)",
                    "Könnte schlicht situativ bedingt sein (Müdigkeit, Kontext)"
                ],
                "valid_interpretations": [0, 1, 2, 3],
                "most_likely": [0, 2],
                "probabilistic_feedback": {
                    "Extraversion": "70%",
                    "Neurotizismus": "65%",
                    "Situativ": "40%", 
                    "Verträglichkeit": "25%"
                },
                "explanation": "🔍 **Mehrdeutige Verhaltensdeutung:** Sozialer Rückzug kann verschiedene Ursachen haben. Bei häufiger Wiederholung deutet es am ehesten auf niedrige Extraversion oder hohen Neurotizismus hin.",
                "learning_point": "Verhalten ist selten monokausal - die Big Five bieten Interpretationsrahmen, keine absoluten Wahrheiten."
            },
            {
                "id": 4, "difficulty": 2,
                "type": "combination_question", 
                "question": "Welche 2 Dimensionen zusammengenommen erklären das Verhalten am besten?",
                "scenario": "Ein Mitarbeiter arbeitet extrem detailversessen, korrigiert ständig Kleinigkeiten, wirkt dabei aber angespannt und unzufrieden.",
                "options": [
                    "Gewissenhaftigkeit + Neurotizismus (ängstlicher Perfektionismus)",
                    "Gewissenhaftigkeit + niedrige Offenheit (Rigidität)",
                    "Neurotizismus + niedrige Verträglichkeit (Reizbarkeit)", 
                    "Gewissenhaftigkeit + Extraversion (sichtbare Leistung)"
                ],
                "correct_combination": [0],
                "explanation": "💼 **Interaktive Wirkung:** Gewissenhaftigkeit allein erklärt die Sorgfalt, aber erst mit Neurotizismus wird daraus ängstlicher Perfektionismus mit innerer Anspannung.",
                "learning_point": "Dimensionen wirken oft interaktiv - Kombinationen können qualitativ neue Muster erzeugen."
            },
            
            # 🎯 SCHWER - Ambivalente Fälle (Schwierigkeitsgrad 3)
            {
                "id": 5, "difficulty": 3,
                "type": "trick_scenario", 
                "question": "Trick-Frage: Warum verhält sich diese normalerweise extrovertierte Person heute so zurückgezogen?",
                "scenario": "Die sonst sehr gesellige und energische Teamleiterin Sarah wirkt heute abwesend, spricht kaum und meidet Blickkontakt. Das Team ist besorgt.",
                "options": [
                    "Akute situative Belastung (privater Stress, Krankheit)",
                    "Längerfristige Persönlichkeitsänderung", 
                    "Strategisches Verhalten (bewusste Zurückhaltung)",
                    "Burnout-Entwicklung"
                ],
                "correct_interpretation": 0,
                "explanation": "🎭 **Situative Überlagerung:** Wenn etablierte Persönlichkeitsmuster plötzlich brechen, sind fast immer akute situative Faktoren verantwortlich. Erst bei längerer Dauer wäre eine Persönlichkeitsänderung zu erwägen.",
                "learning_point": "Situative Faktoren können etablierte Persönlichkeitsmuster kurzfristig komplett überlagern."
            },
            {
                "id": 6, "difficulty": 3,
                "type": "ranking_task",
                "question": "Ordnen Sie die Erklärungen nach ihrer wissenschaftlichen Plausibilität:",
                "scenario": "Eine Person wechselt häufig den Job, beginnt viele Projekte aber vollendet wenige, und hat unkonventionelle Lebensvorstellungen.",
                "options": [
                    "Hohe Offenheit + niedrige Gewissenhaftigkeit (kreativer Unruhegeist)",
                    "Hoher Neurotizismus + niedrige Verträglichkeit (soziale Instabilität)",
                    "Niedrige Gewissenhaftigkeit + hohe Extraversion (Stimulationssuche)",
                    "Hohe Offenheit + hoher Neurotizismus (ängstliche Kreativität)"
                ],
                "correct_ranking": [0, 2, 3, 1],
                "probabilistic_feedback": {
                    "Offenheit+Gewissenhaftigkeit": "75%",
                    "Gewissenhaftigkeit+Extraversion": "60%", 
                    "Offenheit+Neurotizismus": "45%",
                    "Neurotizismus+Verträglichkeit": "20%"
                },
                "explanation": "📊 **Komplexes Profil:** Offenheit erklärt die Neugier und Unkonventionalität, niedrige Gewissenhaftigkeit die mangelnde Durchhaltefähigkeit. Extraversion könnte zusätzlich Stimulationssuche erklären.",
                "learning_point": "Bei komplexen Verhaltensmustern sind Interaktionen zwischen 2-3 Dimensionen oft die beste Erklärung."
            },
            
            # 🧠 FORSCHUNGSFRAGEN (Schwierigkeitsgrad 3)
            {
                "id": 7, "difficulty": 3,
                "type": "research_question", 
                "question": "Welche methodischen Probleme können bei Big-Five-Screenings auftreten?",
                "scenario": "Kritische Reflexion der diagnostischen Praxis...",
                "options": [
                    "Soziale Erwünschtheit (response bias)",
                    "Kulturelle Fairness der Items",
                    "Situative Stimmungsabhängigkeit",
                    "Übergeneralisierung von Laborbefunden"
                ],
                "correct_answers": [0, 1, 2, 3],
                "explanation": "🔬 **Methodenkritik:** Alle genannten Probleme sind wissenschaftlich belegt. Big-Five-Messung ist robust, aber nicht fehlerfrei. Kulturelle Fairness und soziale Erwünschtheit sind besonders relevante Limitationen.",
                "learning_point": "Wissenschaftliche Diagnostik erfordert methodenkritisches Bewusstsein."
            },
            {
                "id": 8, "difficulty": 3,
                "type": "combination_question",
                "question": "Welche Dimensionen-Kombination würde dieses ungewöhnliche Muster am besten erklären?",
                "scenario": "Jemand ist sehr kreativ und ideenreich, aber gleichzeitig extrem pingelig und regelorientiert - scheinbar ein Widerspruch?",
                "options": [
                    "Hohe Offenheit + hohe Gewissenhaftigkeit (kreativer Perfektionist)",
                    "Hohe Offenheit + niedrige Verträglichkeit (egozentrischer Innovator)", 
                    "Hohe Gewissenhaftigkeit + niedrige Extraversion (introvertierter Systematiker)",
                    "Neurotizismus + Offenheit (ängstliche Kreativität)"
                ],
                "correct_combination": [0],
                "explanation": "🎨 **Scheinbarer Widerspruch:** Offenheit (Kreativität) und Gewissenhaftigkeit (Struktur) sind statistisch unabhängig und können gemeinsam auftreten. Dies ergibt das Profil des 'kreativen Perfektionisten'.",
                "learning_point": "Big Five sind orthogonal - scheinbare Widersprüche sind oft Kombinationen unabhängiger Dimensionen."
            }
        ]
    
    def display_quiz(self):
        """Zeigt das Quiz mit Auswahlmöglichkeit für Größe"""
        st.header("🧠 Big Five Clinical Reasoning Quiz")
        
        if 'quiz_configurated' not in st.session_state:
            self.show_quiz_configuration()
            return
        
        if 'quiz_started' not in st.session_state:
            st.session_state.quiz_started = False
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.user_answers = {}
            st.session_state.show_results = False
            st.session_state.start_time = time.time()
        
        if not st.session_state.quiz_started:
            self.show_quiz_intro()
            return
        
        if st.session_state.show_results:
            self.show_results()
        elif st.session_state.current_question < len(st.session_state.quiz_questions):
            self.show_question()
        else:
            st.session_state.show_results = True
            st.rerun()
    
    def show_quiz_configuration(self):
        """Zeigt die Konfiguration für Quiz-Größe"""
        st.markdown("## 🎯 Quiz konfigurieren")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔬 Kleines Quiz")
            st.markdown("""
            - **8 Fragen** (ca. 15 Minuten)
            - **Gemischt**: Einfach + Mittel + Schwer
            """)
            if st.button("Kleines Quiz starten", use_container_width=True):
                self.setup_quiz("small")
        
        with col2:
            st.subheader("🎓 Großes Quiz") 
            st.markdown("""
            - **12 Fragen** (ca. 25 Minuten)
            - **Vollständig**: Alle Fragetypen
            """)
            if st.button("Großes Quiz starten", use_container_width=True):
                self.setup_quiz("large")
    
    def setup_quiz(self, quiz_size):
        """Bereitet das Quiz mit zufälliger Fragenauswahl vor"""
        all_questions = self.all_questions.copy()
        random.shuffle(all_questions)
        
        if quiz_size == "small":
            questions = all_questions[:8]
        else:
            questions = all_questions[:12]
        
        random.shuffle(questions)
        st.session_state.quiz_questions = questions
        st.session_state.quiz_configurated = True
        st.session_state.quiz_size = quiz_size
        st.rerun()
    
    def show_quiz_intro(self):
        """Zeigt die Quiz-Einleitung"""
        question_count = len(st.session_state.quiz_questions)
        
        st.success(f"**🎯 Quiz konfiguriert: {question_count} Fragen**")
        st.info("**📚 Denken Sie in Wahrscheinlichkeiten, nicht in Gewissheiten**")
        
        if st.button("🎯 Quiz jetzt starten", type="primary", use_container_width=True):
            st.session_state.quiz_started = True
            st.rerun()
    
    def show_question(self):
        """Zeigt die aktuelle Frage"""
        question_data = st.session_state.quiz_questions[st.session_state.current_question]
        
        # Fortschrittsanzeige
        progress = (st.session_state.current_question + 1) / len(st.session_state.quiz_questions)
        st.progress(progress)
        st.caption(f"Frage {st.session_state.current_question + 1} von {len(st.session_state.quiz_questions)}")
        
        st.markdown(f"**{question_data['question']}**")
        
        if question_data.get('scenario'):
            with st.expander("📋 Fallvignette anzeigen", expanded=True):
                st.write(question_data['scenario'])
        
        # Fragetyp-spezifische Anzeige
        if question_data['type'] == 'likert_interpretation':
            self.show_likert_question(question_data)
        elif question_data['type'] == 'behavioral_interpretation':
            self.show_behavioral_question(question_data)
        elif question_data['type'] == 'combination_question':
            self.show_combination_question(question_data)
        elif question_data['type'] == 'trick_scenario':
            self.show_trick_question(question_data)
        elif question_data['type'] == 'ranking_task':
            self.show_ranking_question(question_data)
        elif question_data['type'] == 'multiple_correct':
            self.show_multiple_correct_question(question_data)
        elif question_data['type'] == 'research_question':
            self.show_research_question(question_data)
    
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
        
        if st.button("📊 Bewertungen analysieren", type="primary", key=f"btn_likert_{question_data['id']}"):
            self.evaluate_likert_question(user_ratings, question_data)
    
    def show_behavioral_question(self, question_data):
        """Zeigt Verhaltensdeutungs-Fragen"""
        st.write("**Welche Deutungen sind plausibel?**")
        
        user_answers = st.multiselect(
            "Mehrfachauswahl:",
            question_data["options"],
            key=f"behavioral_{question_data['id']}"
        )
        
        if st.button("🔍 Interpretationen bewerten", type="primary", key=f"btn_behavioral_{question_data['id']}"):
            self.evaluate_behavioral_question(user_answers, question_data)
    
    def show_combination_question(self, question_data):
        """Zeigt Kombinations-Fragen"""
        st.write("**Wählen Sie die beste Kombination:**")
        
        user_answer = st.radio(
            "Auswahl:",
            question_data["options"],
            key=f"combo_{question_data['id']}"
        )
        
        if st.button("🔗 Kombination bewerten", type="primary", key=f"btn_combo_{question_data['id']}"):
            self.evaluate_combination_question(user_answer, question_data)
    
    def show_trick_question(self, question_data):
        """Zeigt Trick-Fragen"""
        st.write("**Achtung - situatives Bewusstsein!**")
        
        user_answer = st.radio(
            "Auswahl:",
            question_data["options"],
            key=f"trick_{question_data['id']}"
        )
        
        if st.button("🎭 Lösung analysieren", type="primary", key=f"btn_trick_{question_data['id']}"):
            self.evaluate_trick_question(user_answer, question_data)
    
    def show_ranking_question(self, question_data):
        """Zeigt Ranking-Aufgaben"""
        st.write("**Ordnen Sie nach Wahrscheinlichkeit:**")
        
        options = question_data["options"].copy()
        ranked_options = []
        
        for i in range(len(options)):
            available_options = [opt for opt in options if opt not in ranked_options]
            selected = st.selectbox(
                f"Platz {i+1}:",
                available_options,
                key=f"rank_{question_data['id']}_{i}"
            )
            ranked_options.append(selected)
        
        if st.button("📊 Ranking bewerten", type="primary", key=f"btn_rank_{question_data['id']}"):
            self.evaluate_ranking_question(ranked_options, question_data)
    
    def show_multiple_correct_question(self, question_data):
        """Zeigt Multiple-Choice-Fragen"""
        st.write("**Wählen Sie alle korrekten Aussagen:**")
        
        user_answers = st.multiselect(
            "Mehrfachauswahl:",
            question_data["options"],
            key=f"multiple_{question_data['id']}"
        )
        
        if st.button("✅ Antworten prüfen", type="primary", key=f"btn_multiple_{question_data['id']}"):
            self.evaluate_multiple_correct_question(user_answers, question_data)
    
    def show_research_question(self, question_data):
        """Zeigt Forschungsfragen"""
        st.write("**Kritische Reflexion:**")
        
        user_answers = st.multiselect(
            "Mehrfachauswahl:",
            question_data["options"],
            key=f"research_{question_data['id']}"
        )
        
        if st.button("🔬 Antworten prüfen", type="primary", key=f"btn_research_{question_data['id']}"):
            self.evaluate_research_question(user_answers, question_data)

    # ========== EVALUATION METHODS ==========
    
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
        
        self.show_next_button(question_data)
    
    def evaluate_behavioral_question(self, user_answers, question_data):
        """Bewertet Verhaltensdeutungs-Fragen"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_selections = len(set(user_indices) & set(question_data["valid_interpretations"]))
        
        st.subheader("🔍 Auswertung")
        
        if correct_selections == len(question_data["valid_interpretations"]):
            st.success("🎉 Vollständiges Interpretationsspektrum!")
        else:
            st.warning("👍 Gute Auswahl")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_combination_question(self, user_answer, question_data):
        """Bewertet Kombinations-Fragen"""
        user_index = question_data["options"].index(user_answer)
        correct_index = question_data["correct_combination"][0]
        
        st.subheader("🔗 Auswertung")
        
        if user_index == correct_index:
            st.success("🎉 Perfekte Kombinationswahl!")
            st.session_state.score += 1
        else:
            st.error("❌ Nicht die optimale Kombination.")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_trick_question(self, user_answer, question_data):
        """Bewertet Trick-Fragen"""
        user_index = question_data["options"].index(user_answer)
        correct_index = question_data["correct_interpretation"]
        
        st.subheader("🎭 Auswertung")
        
        if user_index == correct_index:
            st.success("🎉 Situative Überlagerung erkannt!")
            st.session_state.score += 1
        else:
            st.error("❌ Situative Dynamik unterschätzt.")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_ranking_question(self, ranked_options, question_data):
        """Bewertet Ranking-Aufgaben"""
        user_ranking = [question_data["options"].index(opt) for opt in ranked_options]
        correct_ranking = question_data["correct_ranking"]
        matches = sum(1 for i, (user, correct) in enumerate(zip(user_ranking, correct_ranking)) if user == correct)
        similarity = matches / len(correct_ranking)
        
        st.subheader("📊 Auswertung")
        
        if similarity >= 0.8:
            st.success(f"🎉 Nahezu perfekte Rangfolge! ({similarity*100:.1f}%)")
        elif similarity >= 0.6:
            st.warning(f"👍 Gute Einschätzung ({similarity*100:.1f}%)")
        else:
            st.error(f"📚 Abweichung ({similarity*100:.1f}%)")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_multiple_correct_question(self, user_answers, question_data):
        """Bewertet Multiple-Choice-Fragen"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_answers"]
        correct_selected = len(set(user_indices) & set(correct_indices))
        incorrect_selected = len(set(user_indices) - set(correct_indices))
        
        st.subheader("✅ Auswertung")
        
        if correct_selected == len(correct_indices) and incorrect_selected == 0:
            st.success("🎉 Perfekt! Vollständiges Wissen.")
            st.session_state.score += 1
        elif incorrect_selected == 0:
            st.warning("👍 Korrekt, aber nicht vollständig.")
        else:
            st.error("📚 Enthält Fehler.")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_research_question(self, user_answers, question_data):
        """Bewertet Forschungsfragen"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_answers"]
        correct_selected = len(set(user_indices) & set(correct_indices))
        
        st.subheader("🔬 Auswertung")
        
        if correct_selected == len(correct_indices):
            st.success("🎉 Ausgezeichnete Kompetenz!")
            st.session_state.score += 1
        else:
            st.warning("👍 Gutes Bewusstsein.")
        
        with st.expander("📚 Erklärung", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def show_next_button(self, question_data):
        """Zeigt den Next-Button - KORRIGIERTE VERSION"""
        st.markdown("---")
        if st.button("➡️ **Weiter zur nächsten Frage**", type="primary", use_container_width=True, key=f"next_{question_data['id']}"):
            st.session_state.current_question += 1
            st.rerun()
    
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
        
        if percentage >= 80:
            st.success("**🏆 Exzellente diagnostische Kompetenz!**")
        elif percentage >= 60:
            st.warning("**⭐ Gute Urteilsfähigkeit!**")
        else:
            st.error("**📚 Entwicklungsbereich**")
        
        if st.button("🔄 Quiz neu starten", type="primary", use_container_width=True):
            for key in ['quiz_configurated', 'quiz_started', 'current_question', 'score', 'user_answers', 'show_results']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()
