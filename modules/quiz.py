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
                "correct_likert": [4, 2, 3, 3],  # 1-5 Skala für jede Interpretation
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
            },
            
            # 🔄 WEITERE FRAGEN FÜR DAS GROSSE QUIZ
            {
                "id": 9, "difficulty": 2,
                "type": "likert_interpretation",
                "question": "Bewerten Sie die Wahrscheinlichkeit jeder Interpretation:",
                "scenario": "Eine Führungskraft konsultiert vor Entscheidungen immer das gesamte Team, sucht Konsens und vermeidet Hierarchie.",
                "interpretations": [
                    "Hohe Verträglichkeit (kooperativer Stil)",
                    "Niedrige Extraversion (Vermeidung von Führungsrolle)", 
                    "Hohe Offenheit (demokratische Werte)",
                    "Situative Anpassung (Unternehmenskultur)"
                ],
                "correct_likert": [4, 2, 3, 4],
                "explanation": "👑 **Führungsstil-Analyse:** Partizipativer Führungsstil korreliert stark mit Verträglichkeit. Situative Faktoren (Unternehmenskultur) können diesen Stil zusätzlich verstärken.",
                "learning_point": "Führungsverhalten wird durch Persönlichkeit UND situative Anforderungen geprägt."
            },
            {
                "id": 10, "difficulty": 1,
                "type": "multiple_correct", 
                "question": "Welche Aussagen zur Erblichkeit der Big Five sind korrekt?",
                "options": [
                    "40-60% der Varianz ist genetisch bedingt",
                    "Individuelle Umwelt > geteilte Familie",
                    "Persönlichkeit ist nach 30 stabil",
                    "Alle Dimensionen sind ähnlich vererbbar"
                ],
                "correct_answers": [0, 1],
                "explanation": "🧬 **Genetik & Umwelt:** Korrekt sind die 40-60% Erblichkeit und der größere Einfluss individueller Umwelt. Persönlichkeit bleibt lebenslang veränderbar, die Erblichkeit variiert leicht zwischen Dimensionen.",
                "learning_point": "Persönlichkeit entsteht durch komplexe Gen-Umwelt-Interaktionen."
            },
            {
                "id": 11, "difficulty": 2,
                "type": "trick_scenario",
                "question": "Trick-Frage: Warum widerspricht dieses Verhalten der ersten Einschätzung?",
                "scenario": "Der als sehr gewissenhaft eingeschätzte Kollege vergisst plötzlich wichtige Deadlines und wirkt desorganisiert - seit 2 Wochen.",
                "options": [
                    "Akute Überlastung / private Krisensituation", 
                    "Längerfristiger Persönlichkeitswandel",
                    "Mangelnde Motivation / innere Kündigung",
                    "Strategisches Verhalten (Protest)"
                ],
                "correct_interpretation": 0,
                "explanation": "🔄 **Akute vs. chronische Veränderung:** Plötzliche Brüche in stabilen Persönlichkeitsmustern deuten fast immer auf akute situative Belastungen hin. Erst bei längerer Dauer wäre eine echte Persönlichkeitsänderung zu erwägen.",
                "learning_point": "Akute situative Faktoren können etablierte Persönlichkeitsmuster vorübergehend überlagern."
            },
            {
                "id": 12, "difficulty": 3,
                "type": "research_question",
                "question": "Welche kritischen Einwände gibt es gegen die universelle Gültigkeit der Big Five?",
                "options": [
                    "Kulturelle Variation in Faktorenstruktur",
                    "Sprachliche Limitierung des lexikalischen Ansatzes",
                    "Vernachlässigung moralischer/charakterlicher Dimensionen", 
                    "Überbetonung dispositionaler vs. dynamischer Aspekte"
                ],
                "correct_answers": [0, 1, 2, 3],
                "explanation": "🌍 **Kultur & Kritik:** Alle Einwände sind wissenschaftlich diskutiert. Besonders die kulturelle Variation und die Vernachlässigung dynamischer Aspekte sind wichtige Limitationen des Modells.",
                "learning_point": "Wissenschaftliche Modelle sind immer Approximationen - kritische Reflexion ist essentiell."
            }
        ]
    
    def display_quiz(self):
        """Zeigt das Quiz mit Auswahlmöglichkeit für Größe"""
        st.header("🧠 Big Five Clinical Reasoning Master Quiz")
        
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
        """Zeigt die Konfiguration für Quiz-Größe und Schwierigkeit"""
        st.markdown("""
        ## 🎯 Quiz konfigurieren
        Wählen Sie Ihre bevorzugte Quiz-Form:
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔬 Kleines Quiz")
            st.markdown("""
            - **8 Fragen** (ca. 15 Minuten)
            - **Gemischt**: Einfach + Mittel + Schwer
            - **Perfekt für**: Schnelles Training, Wiederholung
            """)
            if st.button("Kleines Quiz starten", use_container_width=True):
                self.setup_quiz("small")
        
        with col2:
            st.subheader("🎓 Großes Quiz") 
            st.markdown("""
            - **12 Fragen** (ca. 25 Minuten)
            - **Vollständig**: Alle Fragetypen + Forschungsfragen
            - **Perfekt für**: Umfassendes Training, Vertiefung
            """)
            if st.button("Großes Quiz starten", use_container_width=True):
                self.setup_quiz("large")
        
        st.markdown("---")
        st.info("""
        **📚 Beide Varianten bieten:**
        - Zufällige Fragenreihenfolge (keine feste Reihenfolge)
        - Progressiver Schwierigkeitsgrad
        - Probabilistisches Feedback  
        - Wissenschaftliche Vertiefung
        """)
    
    def setup_quiz(self, quiz_size):
        """Bereitet das Quiz mit zufälliger Fragenauswahl vor"""
        all_questions = self.all_questions.copy()
        random.shuffle(all_questions)  # Zufällige Reihenfolge
        
        if quiz_size == "small":
            # 8 Fragen: 3 einfach, 3 mittel, 2 schwer
            easy = [q for q in all_questions if q['difficulty'] == 1][:3]
            medium = [q for q in all_questions if q['difficulty'] == 2][:3] 
            hard = [q for q in all_questions if q['difficulty'] == 3][:2]
            st.session_state.quiz_questions = easy + medium + hard
        else:  # large
            # 12 Fragen: 4 einfach, 4 mittel, 4 schwer
            easy = [q for q in all_questions if q['difficulty'] == 1][:4]
            medium = [q for q in all_questions if q['difficulty'] == 2][:4]
            hard = [q for q in all_questions if q['difficulty'] == 3][:4]
            st.session_state.quiz_questions = easy + medium + hard
        
        # Nochmal mischen für maximale Zufälligkeit
        random.shuffle(st.session_state.quiz_questions)
        st.session_state.quiz_configurated = True
        st.session_state.quiz_size = quiz_size
        st.rerun()
    
    def show_quiz_intro(self):
        """Zeigt die Quiz-Einleitung"""
        question_count = len(st.session_state.quiz_questions)
        duration = "15-20" if st.session_state.quiz_size == "small" else "25-30"
        
        st.success(f"""
        **🎯 Quiz konfiguriert: {question_count} Fragen** ({duration} Minuten)
        
        **Enthaltene Fragetypen:**
        ✓ Likert-Skalen & probabilistisches Feedback  
        ✓ Kombinationsfragen & Interaktionen
        ✓ Trick-Szenarien & situative Überlagerungen
        ✓ Forschungsfragen & Methodenkritik
        """)
        
        st.info("""
        **📚 Quiz-Philosophie:**  
        - Denken Sie in Wahrscheinlichkeiten, nicht in Gewissheiten  
        - Berücksichtigen Sie immer situative Faktoren  
        - Mehrere Interpretationen können gleichzeitig plausibel sein  
        - Im Konjunktiv formulieren: *"könnte hindeuten auf..."*
        """)
        
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
        
        # Schwierigkeits-Indikator
        difficulty_icons = {1: "🟢", 2: "🟡", 3: "🔴"}
        st.write(f"{difficulty_icons[question_data['difficulty']]} **Schwierigkeitsgrad {question_data['difficulty']}/3**")
        
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
        st.write("**Bewerten Sie auf einer Skala von 1-5 wie wahrscheinlich jede Interpretation ist:**")
        st.caption("1 = sehr unwahrscheinlich, 3 = neutral, 5 = sehr wahrscheinlich")
        
        user_ratings = []
        for i, interpretation in enumerate(question_data['interpretations']):
            rating = st.slider(
                f"{interpretation}",
                min_value=1, max_value=5, value=3,
                key=f"likert_{question_data['id']}_{i}"
            )
            user_ratings.append(rating)
        
        if st.button("📊 Bewertungen analysieren", type="primary"):
            self.evaluate_likert_question(user_ratings, question_data)
    
    def show_behavioral_question(self, question_data):
        """Zeigt Verhaltensdeutungs-Fragen"""
        st.write("**Welche Deutungen sind plausibel?** (Mehrfachauswahl möglich)")
        
        user_answers = st.multiselect(
            "Wählen Sie alle zutreffenden Interpretationen:",
            question_data["options"],
            key=f"behavioral_{question_data['id']}"
        )
        
        if st.button("🔍 Interpretationen bewerten", type="primary"):
            self.evaluate_behavioral_question(user_answers, question_data)
    
    def show_combination_question(self, question_data):
        """Zeigt Kombinations-Fragen"""
        st.write("**Wählen Sie die beste Kombination von 2 Dimensionen:**")
        
        user_answer = st.radio(
            "Welche Kombination erklärt das Verhalten am besten?",
            question_data["options"],
            key=f"combo_{question_data['id']}"
        )
        
        if st.button("🔗 Kombination bewerten", type="primary"):
            self.evaluate_combination_question(user_answer, question_data)
    
    def show_trick_question(self, question_data):
        """Zeigt Trick-Fragen"""
        st.write("**Achtung - diese Frage testet Ihr situatives Bewusstsein!**")
        
        user_answer = st.radio(
            "Wählen Sie die plausibelste Erklärung:",
            question_data["options"],
            key=f"trick_{question_data['id']}"
        )
        
        if st.button("🎭 Lösung analysieren", type="primary"):
            self.evaluate_trick_question(user_answer, question_data)
    
    def show_ranking_question(self, question_data):
        """Zeigt Ranking-Aufgaben"""
        st.write("**Ordnen Sie nach absteigender Wahrscheinlichkeit:**")
        
        # Simple Ranking-Simulation
        options = question_data["options"].copy()
        ranked_options = []
        
        for i in range(len(options)):
            available_options = [opt for opt in options if opt not in ranked_options]
            selected = st.selectbox(
                f"Platz {i+1} (wahrscheinlichste Erklärung):",
                available_options,
                key=f"rank_{question_data['id']}_{i}"
            )
            ranked_options.append(selected)
        
        if st.button("📊 Ranking bewerten", type="primary"):
            self.evaluate_ranking_question(ranked_options, question_data)
    
    def show_multiple_correct_question(self, question_data):
        """Zeigt Multiple-Choice-Fragen mit mehreren richtigen Antworten"""
        st.write("**Wählen Sie alle korrekten Aussagen:**")
        
        user_answers = st.multiselect(
            "Mehrfachauswahl:",
            question_data["options"],
            key=f"multiple_{question_data['id']}"
        )
        
        if st.button("✅ Antworten prüfen", type="primary"):
            self.evaluate_multiple_correct_question(user_answers, question_data)
    
    def show_research_question(self, question_data):
        """Zeigt Forschungsfragen"""
        st.write("**Kritische Reflexion - wählen Sie alle zutreffenden Antworten:**")
        
        user_answers = st.multiselect(
            "Mehrfachauswahl:",
            question_data["options"],
            key=f"research_{question_data['id']}"
        )
        
        if st.button("🔬 Antworten prüfen", type="primary"):
            self.evaluate_research_question(user_answers, question_data)

    # ========== EVALUATION METHODS ==========
    
    def evaluate_likert_question(self, user_ratings, question_data):
        """Bewertet Likert-Skalen Fragen"""
        correct_ratings = question_data['correct_likert']
        
        # Berechne Abweichung
        deviations = [abs(user - correct) for user, correct in zip(user_ratings, correct_ratings)]
        total_deviation = sum(deviations)
        max_deviation = len(correct_ratings) * 4  # Maximale Abweichung
        accuracy = max(0, 100 - (total_deviation / max_deviation) * 100)
        
        st.subheader("📊 Probabilistische Auswertung")
        
        # Accuracy-Bewertung
        if accuracy >= 80:
            st.success(f"🎉 Exzellente Einschätzung! ({accuracy:.1f}% Übereinstimmung)")
        elif accuracy >= 60:
            st.warning(f"👍 Gute Einschätzung ({accuracy:.1f}% Übereinstimmung)")
        else:
            st.error(f"📚 Deutliche Abweichungen ({accuracy:.1f}% Übereinstimmung)")
        
        # Detailliertes probabilistisches Feedback
        st.write("**Wahrscheinlichkeitsverteilung (wissenschaftliche Einschätzung):**")
        for dimension, probability in question_data.get('probabilistic_feedback', {}).items():
            st.write(f"• **{dimension}**: {probability} Wahrscheinlichkeit")
        
        with st.expander("📚 Wissenschaftliche Einordnung", expanded=True):
            st.info(question_data["explanation"])
            st.caption(f"**Lernpunkt:** {question_data['learning_point']}")
        
        self.next_question_button()
    
    def evaluate_behavioral_question(self, user_answers, question_data):
        """Bewertet Verhaltensdeutungs-Fragen"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        
        # Bewertungskriterien
        correct_selections = len(set(user_indices) & set(question_data["valid_interpretations"]))
        missed_important = len(set(question_data["most_likely"]) - set(user_indices))
        false_selections = len(set(user_indices) - set(question_data["valid_interpretations"]))
        
        st.subheader("🔍 Mehrdimensionale Auswertung")
        
        if correct_selections == len(question_data["valid_interpretations"]) and false_selections == 0:
            st.success("🎉 Exzellent! Vollständiges und akkurates Interpretationsspektrum.")
        elif false_selections == 0:
            st.warning("👍 Gute Auswahl - alle gewählten Interpretationen sind plausibel.")
        else:
            st.error("📚 Enthält weniger plausible Interpretationen.")
        
        if missed_important > 0:
            st.warning(f"⚠️ {missed_important} der wahrscheinlichsten Interpretationen nicht gewählt.")
        
        # Probabilistisches Feedback falls vorhanden
        if question_data.get('probabilistic_feedback'):
            st.write("**Wahrscheinlichkeitsverteilung:**")
            for dimension, probability in question_data['probabilistic_feedback'].items():
                st.write(f"• **{dimension}**: {probability} Wahrscheinlichkeit")
        
        with st.expander("📚 Wissenschaftliche Einordnung", expanded=True):
            st.info(question_data["explanation"])
            st.caption(f"**Lernpunkt:** {question_data['learning_point']}")
        
        self.next_question_button()
    
    def evaluate_combination_question(self, user_answer, question_data):
        """Bewertet Kombinations-Fragen"""
        user_index = question_data["options"].index(user_answer)
        correct_index = question_data["correct_combination"][0]
        
        st.subheader("🔗 Interaktions-Analyse")
        
        if user_index == correct_index:
            st.success("🎉 Perfekte Kombinationswahl! Sie haben die interaktive Wirkung erkannt.")
            st.session_state.score += 1
        else:
            st.error("❌ Nicht die optimale Kombination für dieses Verhaltensmuster.")
            st.info(f"**Beste Erklärung:** {question_data['options'][correct_index]}")
        
        with st.expander("📚 Interaktions-Effekt erklären", expanded=True):
            st.info(question_data["explanation"])
            st.caption(f"**Lernpunkt:** {question_data['learning_point']}")
        
        self.next_question_button()
    
    def evaluate_trick_question(self, user_answer, question_data):
        """Bewertet Trick-Fragen"""
        user_index = question_data["options"].index(user_answer)
        correct_index = question_data["correct_interpretation"]
        
        st.subheader("🎭 Situationsanalyse")
        
        if user_index == correct_index:
            st.success("🎉 Exzellent! Sie haben die situative Überlagerung erkannt.")
            st.session_state.score += 1
        else:
            st.error("❌ Die situative Dynamik wurde unterschätzt.")
            st.info(f"**Plausibelste Erklärung:** {question_data['options'][correct_index]}")
        
        with st.expander("📚 Situative vs. dispositionale Faktoren", expanded=True):
            st.info(question_data["explanation"])
            st.caption(f"**Lernpunkt:** {question_data['learning_point']}")
        
        self.next_question_button()
    
    def evaluate_ranking_question(self, ranked_options, question_data):
        """Bewertet Ranking-Aufgaben"""
        user_ranking = [question_data["options"].index(opt) for opt in ranked_options]
        correct_ranking = question_data["correct_ranking"]
        
        # Rangkorrelations-ähnliche Bewertung
        matches = sum(1 for i, (user, correct) in enumerate(zip(user_ranking, correct_ranking)) if user == correct)
        rank_similarity = matches / len(correct_ranking)
        
        st.subheader("📊 Rangfolgen-Analyse")
        
        if rank_similarity >= 0.8:
            st.success(f"🎉 Nahezu perfekte Rangfolge! ({rank_similarity*100:.1f}% Übereinstimmung)")
        elif rank_similarity >= 0.6:
            st.warning(f"👍 Gute Einschätzung ({rank_similarity*100:.1f}% Übereinstimmung)")
        else:
            st.error(f"📚 Deutliche Abweichung ({rank_similarity*100:.1f}% Übereinstimmung)")
        
        # Probabilistisches Feedback falls vorhanden
        if question_data.get('probabilistic_feedback'):
            st.write("**Wahrscheinlichkeitsverteilung:**")
            for combination, probability in question_data['probabilistic_feedback'].items():
                st.write(f"• **{combination}**: {probability} Wahrscheinlichkeit")
        
        with st.expander("📚 Begründung der Rangfolge", expanded=True):
            st.info(question_data["explanation"])
            st.caption(f"**Lernpunkt:** {question_data['learning_point']}")
        
        self.next_question_button()
    
    def evaluate_multiple_correct_question(self, user_answers, question_data):
        """Bewertet Multiple-Choice-Fragen mit mehreren richtigen Antworten"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_answers"]
        
        correct_selected = len(set(user_indices) & set(correct_indices))
        incorrect_selected = len(set(user_indices) - set(correct_indices))
        missed_correct = len(set(correct_indices) - set(user_indices))
        
        st.subheader("✅ Komplexe Wissensabfrage")
        
        if correct_selected == len(correct_indices) and incorrect_selected == 0:
            st.success("🎉 Perfekt! Vollständiges und akkurates Wissen.")
            st.session_state.score += 1
        elif incorrect_selected == 0:
            st.warning("👍 Korrekt, aber nicht vollständig.")
        else:
            st.error("📚 Enthält fehlerhafte Aussagen.")
        
        if missed_correct > 0:
            st.warning(f"⚠️ {missed_correct} richtige Antwort(en) übersehen.")
        if incorrect_selected > 0:
            st.error(f"❌ {incorrect_selected} falsche Antwort(en) gewählt.")
        
        with st.expander("📚 Ausführliche Erklärung", expanded=True):
            st.info(question_data["explanation"])
            st.caption(f"**Lernpunkt:** {question_data['learning_point']}")
        
        self.next_question_button()
    
    def evaluate_research_question(self, user_answers, question_data):
        """Bewertet Forschungsfragen"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_answers"]
        
        correct_selected = len(set(user_indices) & set(correct_indices))
        incorrect_selected = len(set(user_indices) - set(correct_indices))
        missed_correct = len(set(correct_indices) - set(user_indices))
        
        st.subheader("🔬 Methodenkritische Reflexion")
        
        if correct_selected == len(correct_indices) and incorrect_selected == 0:
            st.success("🎉 Ausgezeichnete methodenkritische Kompetenz!")
            st.session_state.score += 1
        elif incorrect_selected == 0:
            st.warning("👍 Gutes kritisches Bewusstsein.")
        else:
            st.error("📚 Methodische Limitationen nicht vollständig erkannt.")
        
        if missed_correct > 0:
            st.warning(f"⚠️ {missed_correct} wichtige methodische Probleme übersehen.")
        
        with st.expander("📚 Wissenschaftstheoretische Einordnung", expanded=True):
            st.info(question_data["explanation"])
            st.caption(f"**Lernpunkt:** {question_data['learning_point']}")
        
        self.next_question_button()
    
    def next_question_button(self):
        """Zeigt den Button für die nächste Frage"""
        if st.button("➡️ Nächster Fall", type="primary"):
            st.session_state.current_question += 1
            st.rerun()
    
    def show_results(self):
        """Zeigt die detaillierten Quiz-Ergebnisse"""
        st.header("📊 Clinical Reasoning Master Quiz abgeschlossen!")
        
        total_questions = len(st.session_state.quiz_questions)
        correct_answers = st.session_state.score
        percentage = (correct_answers / total_questions) * 100
        time_used = time.time() - st.session_state.start_time
        minutes = int(time_used // 60)
        seconds = int(time_used % 60)
        
        # Ergebnis-Übersicht
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Richtige Antworten", f"{correct_answers}/{total_questions}")
        
        with col2:
            st.metric("Erfolgsquote", f"{percentage:.1f}%")
        
        with col3:
            st.metric("Bearbeitungszeit", f"{minutes:02d}:{seconds:02d}")
        
        # Qualitatives Feedback
        st.subheader("🎯 Diagnostische Urteilsfähigkeit")
        
        if percentage >= 80:
            st.success("""
            **🏆 Exzellente diagnostische Kompetenz!**
            - Sie denken in Wahrscheinlichkeiten und Mehrdeutigkeiten
            - Berücksichtigen situative Faktoren systematisch  
            - Haben ein differenziertes Verständnis der Big-Five-Interaktionen
            """)
        elif percentage >= 60:
            st.warning("""
            **⭐ Gute klinische Urteilsfähigkeit!**
            - Sie erkennen multiple Interpretationsmöglichkeiten
            - Haben Grundverständnis für Person-Situation-Interaktionen
            - Vertiefen Sie sich in komplexere Fallkonstellationen
            """)
        else:
            st.error("""
            **📚 Entwicklungsbereich: Differenzierte Verhaltensdeutung**
            - Üben Sie, in Wahrscheinlichkeiten statt Gewissheiten zu denken
            - Achten Sie stärker auf situative Überlagerungen
            - Trainieren Sie das Erkennen von Dimensions-Interaktionen
            """)
        
        # Reflexion der diagnostischen Kompetenz
        st.subheader("🧠 Reflexion Ihrer Urteilsbildung")
        
        reflection_aspects = [
            "Bei welchen Falltypen fiel Ihnen die mehrdeutige Deutung besonders schwer?",
            "Wie haben Sie situative vs. dispositionale Faktoren abgewogen?",
            "Wo haben Sie Interaktionen zwischen Dimensionen übersehen?", 
            "Wie könnten Sie Ihre diagnostische Urteilsfähigkeit weiter verbessern?"
        ]
        
        for i, question in enumerate(reflection_aspects):
            with st.expander(f"Reflexion {i+1}: {question}"):
                st.text_area("Ihre Gedanken:", key=f"reflection_{i}", height=80, placeholder="Notieren Sie hier Ihre Lerninsights...")
        
        # Empfehlungen für die Weiterentwicklung
        st.subheader("📚 Empfohlene Vertiefungen")
        
        tab1, tab2, tab3 = st.tabs(["🧩 Theoretisch", "🔬 Methodisch", "💡 Praktisch"])
        
        with tab1:
            st.markdown("""
            **Theoretische Vertiefung:**
            - McAdams' Drei-Ebenen-Modell der Persönlichkeit
            - Person-Situation-Interaktionsmodelle
            - Dynamische Persönlichkeitstheorien
            - Kulturelle Variation der Big Five
            """)
        
        with tab2:
            st.markdown("""
            **Methodische Kompetenz:**
            - Kritische Testtheorie & Messprobleme
            - Interview- und Beobachtungsmethoden
            - Multimethodale Diagnostik
            - Ethik psychologischer Diagnostik
            """)
        
        with tab3:
            st.markdown("""
            **Praktische Anwendung:**
            - Fallkonferenzen & kollegiale Beratung
            - Eigene Urteilsheuristiken reflektieren
            - Verhaltensbeobachtung systematisch trainieren
            - Feedback-Kultur entwickeln
            """)
        
        # Neustart-Buttons
        st.subheader("🔄 Weiter lernen")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔁 Gleiche Quiz-Größe wiederholen", use_container_width=True):
                self.restart_quiz(same_size=True)
        
        with col2:
            if st.button("🔄 Andere Quiz-Größe wählen", use_container_width=True):
                self.restart_quiz(same_size=False)
    
    def restart_quiz(self, same_size=True):
        """Startet das Quiz neu"""
        if same_size:
            # Behalte die gleiche Quiz-Größe bei
            quiz_size = st.session_state.quiz_size
            self.setup_quiz(quiz_size)
        else:
            # Zurück zur Konfiguration
            for key in ['quiz_configurated', 'quiz_started', 'current_question', 
                       'score', 'user_answers', 'show_results', 'quiz_questions', 'quiz_size']:
                if key in st.session_state:
                    del st.session_state[key]
        
        st.session_state.quiz_started = False
        st.rerun()
