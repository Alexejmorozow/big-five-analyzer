import streamlit as st
import random
import time

class QuizModule:
    def __init__(self):
        self.all_questions = self.load_questions()
    
    def load_questions(self):
        """Lädt alle Fragen inklusive der neuen Erweiterungen"""
        return [
            # 📊 BASIS-FRAGEN (bestehende Typen)
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
            
            # 🔮 PHÄNOMEN-DEUTUNG (Konjunktivisch)
            {
                "id": 101, "difficulty": 2,
                "type": "phenomenon_interpretation",
                "question": "Wie könnte dieses Verhalten im Rahmen der Big Five gedeutet werden?",
                "scenario": "Eine Patientin in der Therapie vermeidet Blickkontakt, spricht sehr leise und zögert lange vor Antworten. Sie wirkt angespannt, aber kooperativ.",
                "phenomenon": "Sozialer Rückzug + gehemmte Kommunikation",
                "possible_interpretations": [
                    "Hoher Neurotizismus (soziale Ängstlichkeit, Unsicherheit)",
                    "Niedrige Extraversion (introvertierte Grundtendenz)", 
                    "Hohe Verträglichkeit (unterwürfiges, konfliktscheues Verhalten)",
                    "Situative Reaktion (Scham, akute Belastung, Therapieangst)",
                    "Kombination aus Neurotizismus und niedriger Extraversion"
                ],
                "valid_hypotheses": [0, 1, 2, 3, 4],
                "most_plausible": [0, 4, 3],
                "explanation": "🔍 **Mehrdeutige Phänomendeutung:** Dieses Verhaltensmuster könnte auf soziale Ängstlichkeit (Neurotizismus) ODER introvertierte Grundtendenz ODER situative Scham hindeuten. Entscheidend: Wie verhält sich die Person in anderen Kontexten?",
                "learning_point": "Identische Verhaltensmuster können unterschiedliche Ursachen haben - Kontext und Verlaufsbeobachtung sind entscheidend."
            },
            
            # ⏱️ FALLVERLÄUFE (Trait vs. State)
            {
                "id": 102, "difficulty": 3,
                "type": "case_progression",
                "question": "Handelt es sich um einen Persönlichkeitsstil oder einen situativen Zustand?",
                "scenario": "**Woche 1-4:** Herr Meyer wirkt im Team ruhig, aber kompetent. Er spricht wenig, aber wenn, dann präzise.\n\n**Woche 5-8:** Seit einem gescheiterten Projekt wirkt er zunehmend gereizt, kritisiert Kollegen, wirkt misstrauisch.\n\n**Woche 9-12:** Das Verhalten normalisiert sich langsam, aber die grundlegende Zurückhaltung bleibt.",
                "timeline": [
                    {"phase": "Baseline", "verhalten": "Ruhig, kompetent, präzise"},
                    {"phase": "Akutphase", "verhalten": "Gereizt, kritisch, misstrauisch"}, 
                    {"phase": "Erholung", "verhalten": "Normalisierung, aber grundsätzlich zurückhaltend"}
                ],
                "interpretation_task": "Bewerten Sie die Stabilität vs. Situativität:",
                "options": [
                    "Stabiler Persönlichkeitsstil (niedrige Extraversion) mit situativer Überlagerung",
                    "Primär situative Reaktion (Projektstress) auf normalerweise extravertierter Basis",
                    "Entwicklung einer Persönlichkeitsänderung (erhöhter Neurotizismus)",
                    "Kombination aus stabiler Introversion + akuter Belastungsreaktion"
                ],
                "correct_interpretation": [0, 3],
                "explanation": "⏱️ **Verlaufsdiagnostik:** Die stabile Grundtendenz (Zurückhaltung) spricht für niedrige Extraversion. Die akute Veränderung deutet auf situative Überlagerung (Stressreaktion) hin. Die Rückkehr zur Baseline spricht gegen dauerhafte Persönlichkeitsänderung.",
                "learning_point": "Verlaufsbeobachtung unterscheidet stabile Traits von state-abhängigen Reaktionen."
            },
            
            # ⚠️ DIAGNOSTISCHE FEHLERFALLEN
            {
                "id": 103, "difficulty": 3, 
                "type": "diagnostic_pitfall",
                "question": "Welche diagnostische Fehlerfalle wird hier provoziert?",
                "scenario": "Ein Therapeut liest im Assessment: 'Hohe Offenheit, niedrige Verträglichkeit'. In der Sitzung berichtet der Klient von Konflikten mit Autoritätspersonen. Der Therapeut interpretiert: 'Typisch bei niedriger Verträglichkeit - da müssen wir an Ihrer Kooperationsfähigkeit arbeiten.'",
                "pitfall_type": "Confirmation Bias + Overpathologizing",
                "critical_elements": [
                    "Vorschnelle Verknüpfung von Assessment und Einzelverhalten",
                    "Ignorieren situativer Faktoren (berechtigte Kritik?)", 
                    "Pathologisierung normaler Verhaltensvarianz",
                    "Fehlende Berücksichtigung des Kontexts"
                ],
                "options": [
                    "Confirmation Bias (Suche nach bestätigenden Informationen)",
                    "Overpathologizing (Normalvariation als Problem sehen)",
                    "Fundamental Attribution Error (dispositional überschätzen)",
                    "Alle genannten Fehlerfallen"
                ],
                "correct_answers": [3],
                "explanation": "🎯 **Diagnostische Fallstricke:** Hier wirken mehrere Biases: Confirmation Bias (Assessment-Daten dominieren), Overpathologizing (Konfliktverhalten ≠ Störung), Fundamental Attribution Error (situative Faktoren ignorieren). Wichtig: Assessment-Daten sind Hypothesen, keine Diagnosen!",
                "learning_point": "Assessment-Daten generieren Hypothesen - keine vorschnellen Kausalzuschreibungen!"
            },
            
            # 📈 INTERAKTIVE LIKELIHOOD-SCHÄTZUNGEN  
            {
                "id": 104, "difficulty": 2,
                "type": "probability_estimation",
                "question": "Schätzen Sie die Wahrscheinlichkeit jeder Hypothese (in %):",
                "scenario": "Ein sonst zuverlässiger Mitarbeiter liefert plötzlich unvollständige Arbeiten ab, wirkt unkonzentriert und vergesslich. Dies seit 3 Wochen.",
                "hypotheses": [
                    "Akute private Belastung (Familie, Gesundheit)",
                    "Beginnendes Burnout (berufliche Überlastung)",
                    "Nachlassende Gewissenhaftigkeit (Persönlichkeitsänderung)", 
                    "Situative Demotivation (Konflikte, fehlende Anerkennung)"
                ],
                "expert_probabilities": [45, 25, 10, 20],
                "tolerance_range": 15,
                "explanation": "📈 **Probabilistisches Reasoning:** Akute private Belastung ist am wahrscheinlichsten (plötzliche Veränderung bei vorher stabiler Person). Burnout und situative Faktoren sind möglich. Reine Persönlichkeitsänderung ist unwahrscheinlich (zu kurzer Zeitraum).",
                "learning_point": "Klinisches Urteilen erfordert Wahrscheinlichkeitsabwägungen, nicht binäre Entscheidungen."
            },
            
            # 💡 STRATEGIE-FRAGEN (Umgangsleitlinien)
            {
                "id": 105, "difficulty": 2,
                "type": "intervention_strategy", 
                "question": "Welche Reaktion wäre hier am angemessensten?",
                "scenario": "Im Team fällt eine Mitarbeiterin durch extrem detaillierte, aber sehr langsame Arbeit auf. Projekte verzögern sich, Kollegen werden ungeduldig. Die Mitarbeiterin wirkt dabei nicht ängstlich, sondern konzentriert und zufrieden.",
                "personality_profile": "Hohe Gewissenhaftigkeit (Perfektionismus) bei normalem Neurotizismus",
                "strategic_options": [
                    "Klare Deadlines setzen + Qualitätskriterien definieren (Struktur geben)",
                    "Perfektionismus thematisieren + psychologische Unterstützung anbieten",
                    "Aufgaben an Stärken anpassen (Qualitätskontrolle statt Zeitdruck)",
                    "Team-Feedback einholen + Gruppendruck nutzen"
                ],
                "recommended_strategies": [0, 2],
                "explanation": "💼 **Personzentrierte Intervention:** Da kein Leidensdruck (kein Neurotizismus) besteht, sind strukturelle Lösungen besser als Pathologisierung. Deadlines setzen + Stärken nutzen (Qualitätsarbeit) statt 'Therapieren' eines funktionalen Persönlichkeitsmerkmals.",
                "learning_point": "Interventionen sollten zum Persönlichkeitsprofil passen - nicht jedes Merkmal muss 'behandelt' werden."
            },
            
            # 🧩 ERWEITERTE KOMBINATIONSFRAGEN
            {
                "id": 106, "difficulty": 3,
                "type": "complex_combination", 
                "question": "Welche Dimensionen-Kombination erklärt dieses komplexe Muster?",
                "scenario": "Eine Person initiiert intensiven philosophischen Austausch (tiefe Gespräche), zeigt aber wenig Interesse an oberflächlichem Smalltalk. In Gruppen dominant bei intellektuellen Themen, aber zurückhaltend bei persönlichen Themen. Sehr wertorientiert in Entscheidungen.",
                "behavior_pattern": "Selektive Soziabilität + intellektuelle Dominanz + Wertorientierung",
                "dimension_combinations": [
                    "Hohe Offenheit + niedrige Extraversion (intellektuell interessierter Introvertierter)",
                    "Hohe Offenheit + hohe Gewissenhaftigkeit (prinzipienorientierter Intellektueller)", 
                    "Hohe Offenheit + niedrige Verträglichkeit (egozentrischer Denker)",
                    "Hohe Offenheit + hohe Extraversion + hohe Gewissenhaftigkeit (komplexes Profil)"
                ],
                "correct_combination": [0, 1],
                "explanation": "🎭 **Komplexes Interaktionsmuster:** Hohe Offenheit erklärt das intellektuelle Interesse. Die selektive Soziabilität (tiefe vs. oberflächliche Gespräche) deutet auf introvertierte Tendenzen hin. Die Wertorientierung spricht für Gewissenhaftigkeit. Keine Hinweise auf niedrige Verträglichkeit.",
                "learning_point": "Komplexe Verhaltensmuster erfordern oft Mehrfach-Kombinationen von Dimensionen."
            }
        ]
    
    def display_quiz(self):
        """Zeigt das Quiz mit Auswahlmöglichkeit für Größe"""
        st.header("🧠 Big Five Clinical Reasoning Master Quiz")
        
        # Initialisierung des Session States
        if 'quiz_initialized' not in st.session_state:
            st.session_state.quiz_initialized = True
            st.session_state.quiz_configurated = False
            st.session_state.quiz_started = False
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.user_answers = {}
            st.session_state.show_results = False
        
        if not st.session_state.quiz_configurated:
            self.show_quiz_configuration()
            return
        
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
            - **4 Fragen** (ca. 10 Minuten)
            - **Gemischt**: Verschiedene Fragetypen
            """)
            if st.button("Kleines Quiz starten", use_container_width=True, key="btn_small"):
                self.setup_quiz("small")
        
        with col2:
            st.subheader("🎓 Großes Quiz") 
            st.markdown("""
            - **8 Fragen** (ca. 20 Minuten)
            - **Vollständig**: Alle Fragetypen
            """)
            if st.button("Großes Quiz starten", use_container_width=True, key="btn_large"):
                self.setup_quiz("large")
    
    def setup_quiz(self, quiz_size):
        """Bereitet das Quiz mit zufälliger Fragenauswahl vor"""
        all_questions = self.all_questions.copy()
        random.shuffle(all_questions)
        
        if quiz_size == "small":
            questions = all_questions[:4]
        else:
            questions = all_questions[:8]
        
        random.shuffle(questions)
        st.session_state.quiz_questions = questions
        st.session_state.quiz_configurated = True
        st.session_state.quiz_size = quiz_size
        st.rerun()
    
    def show_quiz_intro(self):
        """Zeigt die Quiz-Einleitung"""
        question_count = len(st.session_state.quiz_questions)
        
        st.success(f"**🎯 Quiz konfiguriert: {question_count} Fragen**")
        st.info("""
        **📚 Denken Sie in:**
        - Wahrscheinlichkeiten, nicht Gewissheiten
        - Mehreren Interpretationen, nicht einer Wahrheit  
        - Konjunktiv: *"könnte hindeuten auf..."*
        """)
        
        if st.button("🎯 Quiz jetzt starten", type="primary", use_container_width=True, key="btn_start_quiz"):
            st.session_state.quiz_started = True
            st.session_state.start_time = time.time()
            st.rerun()
    
    def show_question(self):
        """Zeigt die aktuelle Frage - KORRIGIERTE VERSION"""
        question_data = st.session_state.quiz_questions[st.session_state.current_question]
        
        # Fortschrittsanzeige
        progress = (st.session_state.current_question + 1) / len(st.session_state.quiz_questions)
        st.progress(progress)
        st.caption(f"Frage {st.session_state.current_question + 1} von {len(st.session_state.quiz_questions)}")
        
        # Schwierigkeitsgrad
        difficulty_icons = {1: "🟢", 2: "🟡", 3: "🔴"}
        st.write(f"{difficulty_icons[question_data['difficulty']]} **Schwierigkeitsgrad {question_data['difficulty']}/3**")
        
        st.markdown(f"### {question_data['question']}")
        
        if question_data.get('scenario'):
            with st.expander("📋 Fallvignette anzeigen", expanded=True):
                st.write(question_data['scenario'])
        
        # Fragetyp-spezifische Anzeige
        question_type_handlers = {
            'likert_interpretation': self.show_likert_question,
            'multiple_correct': self.show_multiple_correct_question,
            'phenomenon_interpretation': self.show_phenomenon_interpretation,
            'case_progression': self.show_case_progression,
            'diagnostic_pitfall': self.show_diagnostic_pitfall,
            'probability_estimation': self.show_probability_estimation,
            'intervention_strategy': self.show_intervention_strategy,
            'complex_combination': self.show_complex_combination
        }
        
        handler = question_type_handlers.get(question_data['type'])
        if handler:
            handler(question_data)
        else:
            st.error(f"Unbekannter Fragetyp: {question_data['type']}")
    
    # ========== FRAGETYP-METHODEN ==========
    
    def show_likert_question(self, question_data):
        """Zeigt Likert-Skalen Fragen"""
        st.write("**Bewerten Sie auf einer Skala von 1-5:**")
        st.caption("1 = sehr unwahrscheinlich, 3 = neutral, 5 = sehr wahrscheinlich")
        
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
    
    def show_phenomenon_interpretation(self, question_data):
        """Zeigt Phänomen-Deutungs-Fragen"""
        st.write("**Welche Interpretationen sind wissenschaftlich plausibel?**")
        st.caption("Mehrere Antworten können richtig sein - denken Sie im Konjunktiv!")
        
        user_answers = st.multiselect(
            "Wählen Sie plausible Hypothesen:",
            question_data["possible_interpretations"],
            key=f"phenomenon_{question_data['id']}"
        )
        
        if st.button("🔮 Hypothesen bewerten", type="primary", key=f"btn_phenomenon_{question_data['id']}"):
            self.evaluate_phenomenon_interpretation(user_answers, question_data)
    
    def show_case_progression(self, question_data):
        """Zeigt Fallverlaufs-Fragen"""
        st.write("**Analyse des Verhaltens über Zeit:**")
        
        # Timeline anzeigen
        for event in question_data["timeline"]:
            st.write(f"**{event['phase']}:** {event['verhalten']}")
        
        st.write(f"**{question_data['interpretation_task']}**")
        
        user_answers = st.multiselect(
            "Wählen Sie zutreffende Interpretationen:",
            question_data["options"],
            key=f"case_{question_data['id']}"
        )
        
        if st.button("⏱️ Verlaufsanalyse", type="primary", key=f"btn_case_{question_data['id']}"):
            self.evaluate_case_progression(user_answers, question_data)
    
    def show_diagnostic_pitfall(self, question_data):
        """Zeigt diagnostische Fehlerfallen"""
        st.warning("⚠️ **Achtung - diese Frage testet Ihre methodische Kritikfähigkeit!**")
        
        st.write("**Kritische Elemente in dieser Situation:**")
        for element in question_data["critical_elements"]:
            st.write(f"• {element}")
        
        user_answers = st.multiselect(
            "Welche Fehlerfallen wirken hier?",
            question_data["options"],
            key=f"pitfall_{question_data['id']}"
        )
        
        if st.button("🎯 Fallen analysieren", type="primary", key=f"btn_pitfall_{question_data['id']}"):
            self.evaluate_diagnostic_pitfall(user_answers, question_data)
    
    def show_probability_estimation(self, question_data):
        """Zeigt Likelihood-Schätzungen"""
        st.write("**Schätzen Sie die Wahrscheinlichkeit jeder Hypothese (0-100%):**")
        
        user_probabilities = []
        for i, hypothesis in enumerate(question_data["hypotheses"]):
            prob = st.slider(
                f"{hypothesis}",
                min_value=0, max_value=100, value=25,
                key=f"prob_{question_data['id']}_{i}"
            )
            user_probabilities.append(prob)
        
        # Prüfen ob Summe ~100%
        total = sum(user_probabilities)
        if total != 100:
            st.warning(f"⚠️ Summe: {total}% (sollte 100% ergeben)")
        
        if st.button("📈 Schätzung analysieren", type="primary", key=f"btn_prob_{question_data['id']}"):
            self.evaluate_probability_estimation(user_probabilities, question_data)
    
    def show_intervention_strategy(self, question_data):
        """Zeigt Strategie-Fragen"""
        st.write("**Welche Umgangsstrategie wäre angemessen?**")
        st.info(f"**Persönlichkeitsprofil:** {question_data['personality_profile']}")
        
        user_answers = st.multiselect(
            "Wählen Sie passende Interventionen:",
            question_data["strategic_options"],
            key=f"strategy_{question_data['id']}"
        )
        
        if st.button("💡 Strategien bewerten", type="primary", key=f"btn_strategy_{question_data['id']}"):
            self.evaluate_intervention_strategy(user_answers, question_data)
    
    def show_complex_combination(self, question_data):
        """Zeigt erweiterte Kombinationsfragen"""
        st.write("**Komplexes Verhaltensmuster analysieren:**")
        st.info(f"**Muster:** {question_data['behavior_pattern']}")
        
        user_answers = st.multiselect(
            "Welche Dimensionen-Kombinationen erklären dieses Muster?",
            question_data["dimension_combinations"],
            key=f"complex_{question_data['id']}"
        )
        
        if st.button("🧩 Kombination analysieren", type="primary", key=f"btn_complex_{question_data['id']}"):
            self.evaluate_complex_combination(user_answers, question_data)

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
    
    def evaluate_phenomenon_interpretation(self, user_answers, question_data):
        """Bewertet Phänomen-Deutungen"""
        user_indices = [question_data["possible_interpretations"].index(ans) for ans in user_answers]
        correct_selections = len(set(user_indices) & set(question_data["valid_hypotheses"]))
        
        st.subheader("🔮 Mehrdeutige Phänomendeutung")
        
        if correct_selections == len(question_data["valid_hypotheses"]):
            st.success("🎉 Vollständiges Hypothesenspektrum erkannt!")
            st.session_state.score += 1
        else:
            st.warning("👍 Gute Auswahl - mehrere Perspektiven bedacht")
        
        st.write("**Wahrscheinlichste Hypothesen:**")
        for idx in question_data["most_plausible"]:
            st.write(f"• {question_data['possible_interpretations'][idx]}")
        
        with st.expander("📚 Wissenschaftliche Einordnung", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_case_progression(self, user_answers, question_data):
        """Bewertet Fallverlaufs-Analysen"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_interpretation"]
        
        st.subheader("⏱️ Verlaufsdiagnostik")
        
        if set(user_indices) == set(correct_indices):
            st.success("🎉 Exzellente Verlaufsanalyse!")
            st.session_state.score += 1
        else:
            st.error("❌ Differenzierung zwischen Trait und State verbesserungsfähig")
        
        with st.expander("📚 Verlaufsinterpretation", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_diagnostic_pitfall(self, user_answers, question_data):
        """Bewertet Fehlerfallen-Erkennung"""
        user_indices = [question_data["options"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_answers"]
        
        st.subheader("⚠️ Methodenkritische Reflexion")
        
        if set(user_indices) == set(correct_indices):
            st.success("🎉 Exzellente Fehlerfallen-Erkennung!")
            st.session_state.score += 1
        else:
            st.warning("📚 Diagnostische Biases nicht vollständig erkannt")
        
        with st.expander("📚 Kritische Reflexion", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_probability_estimation(self, user_probabilities, question_data):
        """Bewertet Wahrscheinlichkeitsschätzungen"""
        expert_probs = question_data["expert_probabilities"]
        tolerance = question_data["tolerance_range"]
        
        deviations = [abs(user - expert) for user, expert in zip(user_probabilities, expert_probs)]
        within_tolerance = sum(1 for dev in deviations if dev <= tolerance)
        accuracy = (within_tolerance / len(deviations)) * 100
        
        st.subheader("📈 Probabilistisches Clinical Reasoning")
        
        if accuracy >= 80:
            st.success(f"🎉 Exzellente Wahrscheinlichkeitseinschätzung! ({accuracy:.1f}%)")
            st.session_state.score += 1
        elif accuracy >= 60:
            st.warning(f"👍 Gute Einschätzung ({accuracy:.1f}%)")
        else:
            st.error(f"📚 Deutliche Abweichungen ({accuracy:.1f}%)")
        
        # Vergleich anzeigen
        st.write("**Vergleich mit Experteneinschätzung:**")
        for i, (user, expert) in enumerate(zip(user_probabilities, expert_probs)):
            diff = abs(user - expert)
            marker = "✅" if diff <= tolerance else "❌"
            st.write(f"{marker} **{question_data['hypotheses'][i]}** - Sie: {user}% | Experte: {expert}%")
        
        with st.expander("📚 Probabilistische Begründung", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_intervention_strategy(self, user_answers, question_data):
        """Bewertet Interventions-Strategien"""
        user_indices = [question_data["strategic_options"].index(ans) for ans in user_answers]
        correct_indices = question_data["recommended_strategies"]
        
        st.subheader("💡 Personzentrierte Intervention")
        
        if set(user_indices) == set(correct_indices):
            st.success("🎉 Optimales Interventionsverständnis!")
            st.session_state.score += 1
        else:
            st.warning("👍 Gute Ansätze - Feinabstimmung möglich")
        
        with st.expander("📚 Interventionslogik", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def evaluate_complex_combination(self, user_answers, question_data):
        """Bewertet komplexe Kombinationsfragen"""
        user_indices = [question_data["dimension_combinations"].index(ans) for ans in user_answers]
        correct_indices = question_data["correct_combination"]
        
        st.subheader("🧩 Komplexe Dimensions-Interaktion")
        
        if set(user_indices) == set(correct_indices):
            st.success("🎉 Exzellente Analyse komplexer Muster!")
            st.session_state.score += 1
        else:
            st.warning("📚 Interaktionseffekte noch vertiefen")
        
        with st.expander("📚 Interaktionsanalyse", expanded=True):
            st.info(question_data["explanation"])
        
        self.show_next_button(question_data)
    
    def show_next_button(self, question_data):
        """Zeigt den Next-Button - KORRIGIERTE UND FUNKTIONIERENDE VERSION"""
        st.markdown("---")
        
        # WICHTIG: Ein eindeutiger Key für jeden Next-Button
        next_key = f"next_btn_{question_data['id']}_{st.session_state.current_question}"
        
        if st.button("➡️ **Weiter zur nächsten Frage**", type="primary", use_container_width=True, key=next_key):
            # Zustand sicher aktualisieren
            st.session_state.current_question += 1
            
            # Expliziter Rerun - das ist der Schlüssel!
            st.rerun()
    
    def show_results(self):
        """Zeigt die Quiz-Ergebnisse"""
        st.header("📊 Quiz abgeschlossen!")
        
        total = len(st.session_state.quiz_questions)
        score = st.session_state.score
        percentage = (score / total) * 100
        
        # Zeitberechnung
        if 'start_time' in st.session_state:
            time_used = time.time() - st.session_state.start_time
            minutes = int(time_used // 60)
            seconds = int(time_used % 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
        else:
            time_str = "Unbekannt"
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Richtige Antworten", f"{score}/{total}")
        with col2:
            st.metric("Erfolgsquote", f"{percentage:.1f}%")
        with col3:
            st.metric("Bearbeitungszeit", time_str)
        
        # Qualitatives Feedback
        st.subheader("🎯 Diagnostische Urteilsfähigkeit")
        
        if percentage >= 80:
            st.success("""
            **🏆 Exzellente diagnostische Kompetenz!**
            - Sie denken in Wahrscheinlichkeiten und Mehrdeutigkeiten
            - Berücksichtigen situative Faktoren systematisch  
            - Haben ein differenziertes Verständnis komplexer Muster
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
        
        # Neustart-Button
        st.markdown("---")
        if st.button("🔄 Quiz neu starten", type="primary", use_container_width=True, key="btn_restart"):
            # Session State komplett zurücksetzen
            for key in list(st.session_state.keys()):
                if key != 'quiz_initialized':
                    del st.session_state[key]
            st.rerun()
