import streamlit as st
import random
import time
import pandas as pd
import plotly.graph_objects as go
from typing import List, Dict, Any

class QuizModule:
    def __init__(self):
        self.all_questions = self.load_questions()
    
    def load_questions(self) -> List[Dict[str, Any]]:
        """Lädt alle Fragen für das Clinical Reasoning Training"""
        return [
            # 📊 LIKERT-INTERPRETATION
            {
                "id": 1,
                "type": "likert_interpretation",
                "difficulty": 2,
                "question": "Bewerten Sie die Plausibilität jeder Interpretation auf einer Skala von 1-5:",
                "scenario": "Ein Mitarbeiter beginnt pünktlich um 8:00, plant seine Arbeit minutiös durch, dokumentiert akribisch und korrigiert selbst kleinste Unstimmigkeiten. Wirkt dabei nicht gestresst, sondern zufrieden.",
                "interpretations": [
                    "Hohe Gewissenhaftigkeit (strukturierte Arbeitsweise)",
                    "Ängstlicher Perfektionismus (hoher Neurotizismus)",
                    "Berufliche Sozialisation (erlerntes Verhalten)",
                    "Kompetenzdemonstration (Streben nach Anerkennung)"
                ],
                "expert_ratings": [4, 2, 3, 2],
                "tolerance": 1,
                "explanation": "🔍 **Abwägende Deutung:** Die Zufriedenheit spricht stark für hohe Gewissenhaftigkeit als Kernmerkmal. Fehlende Stresssymptome machen Neurotizismus unwahrscheinlicher.",
                "learning_point": "Gewissenhaftigkeit muss nicht mit Stress verbunden sein - Struktur kann Sicherheit geben."
            },
            
            # ✅ MULTIPLE-CORRECT BEHAVIORAL INTERPRETATION
            {
                "id": 2,
                "type": "multiple_correct_behavioral",
                "difficulty": 2,
                "question": "Welche Interpretationen sind wissenschaftlich plausibel?",
                "scenario": "Maria sitzt in Teammeetings meist still, spricht nur wenn direkt gefragt, beobachtet intensiv und macht sich detaillierte Notizen. In Einzelgesprächen wirkt sie jedoch kompetent und reflektiert.",
                "interpretations": [
                    "Introversion (niedrige Extraversion)",
                    "Soziale Ängstlichkeit (hoher Neurotizismus)",
                    "Beobachtende Lernstrategie (kognitive Präferenz)",
                    "Geringe Verträglichkeit (Desinteresse an anderen)",
                    "Hohe Gewissenhaftigkeit (gründliche Vorbereitung)"
                ],
                "correct_answers": [0, 2, 4],
                "explanation": "👥 **Mehrdeutiges Verhalten:** Das Verhalten könnte Introversion, beobachtende Lernpräferenz oder Gewissenhaftigkeit spiegeln.",
                "learning_point": "Ruhiges Verhalten kann verschiedene Ursachen haben - Kontext ist entscheidend."
            },
            
            # 🧩 COMBINATION QUESTION
            {
                "id": 3,
                "type": "combination_question",
                "difficulty": 3,
                "question": "Welche 2 Dimensionen-Kombination erklärt dieses komplexe Muster am besten?",
                "scenario": "Eine Person zeigt intensive Begeisterung für philosophische Diskussionen und künstlerische Projekte, wirkt aber gleichzeitig sehr diszipliniert und strukturiert in der Umsetzung.",
                "behavior_pattern": "Kreativität + Strukturiertheit + selektive Soziabilität",
                "combinations": [
                    "Hohe Offenheit + hohe Gewissenhaftigkeit",
                    "Hohe Offenheit + niedrige Extraversion", 
                    "Niedrige Verträglichkeit + hohe Gewissenhaftigkeit",
                    "Hohe Offenheit + hohe Gewissenhaftigkeit + niedrige Extraversion"
                ],
                "correct_combination": 3,
                "explanation": "🎭 **Komplexes Interaktionsmuster:** Die Kombination aus hoher Offenheit (Kreativität), hoher Gewissenhaftigkeit (Struktur) und niedriger Extraversion erklärt das Verhaltensmuster.",
                "learning_point": "Scheinbare Widersprüche werden durch Kombinationen orthogonaler Dimensionen erklärt."
            },
            
            # ⚠️ TRICK SCENARIO
            {
                "id": 4,
                "type": "trick_scenario", 
                "difficulty": 3,
                "question": "Warum verhält sich diese normalerweise extrovertierte Person plötzlich zurückgezogen?",
                "scenario": "Lisa ist normalerweise gesellig, initiiert Gespräche und wirkt in Gruppen energisch. Seit 3 Wochen wirkt sie jedoch zurückgezogen, meidet soziale Interaktionen und wirkt erschöpft.",
                "options": [
                    "Persönlichkeitsänderung (dauerhafte Introversion)",
                    "Akute private Belastung (Situativer State)", 
                    "Burnout-Entwicklung (berufliche Überlastung)",
                    "Strategische Anpassung (bewusste Verhaltensänderung)"
                ],
                "correct_answers": [1, 2],
                "explanation": "⏱️ **Trait vs. State:** Plötzliche Verhaltensänderungen deuten auf akute Zustände (States) als auf Persönlichkeitsänderungen (Traits) hin.",
                "learning_point": "Plötzliche Verhaltensänderungen = situative Faktoren; stabile Muster = Persönlichkeitsfaktoren."
            },
            
            # 📈 RANKING TASK
            {
                "id": 5,
                "type": "ranking_task",
                "difficulty": 3, 
                "question": "Ordnen Sie die Hypothesen nach wissenschaftlicher Plausibilität (1 = am plausibelsten):",
                "scenario": "Ein bisher zuverlässiger Mitarbeiter beginnt plötzlich, Deadlines zu verpassen, wirkt unkonzentriert und emotional labil. Kollegen berichten von Stimmungsschwankungen.",
                "hypotheses": [
                    "Akute private Belastung (Familienkrise, Gesundheit)",
                    "Beginndes Burnout-Syndrom (berufliche Überlastung)",
                    "Entwicklung einer depressiven Episode", 
                    "Nachlassende Arbeitsmotivation (innere Kündigung)"
                ],
                "correct_ranking": [0, 1, 2, 3],
                "explanation": "📈 **Probabilistisches Reasoning:** Akute private Belastung ist am wahrscheinlichsten (plötzlicher Beginn, emotionale Labilität).",
                "learning_point": "Bei plötzlichen Veränderungen: Akute States vor Persönlichkeitsänderungen priorisieren."
            },
            
            # 🔬 RESEARCH CRITICAL THINKING
            {
                "id": 6,
                "type": "research_critical",
                "difficulty": 3,
                "question": "Welche methodischen Probleme können bei Big-Five-Assessments auftreten?",
                "scenario": "Ein Unternehmen führt Big-Five-Tests in der Personalauswahl ein. Die Tests werden online ohne Aufsicht durchgeführt.",
                "critical_issues": [
                    "Soziale Erwünschtheit (response bias)",
                    "Kulturelle Unterschiede in der Item-Interpretation", 
                    "Fehlende situative Validität (Labor vs. Realität)",
                    "Überbetonung dispositionaler Faktoren",
                    "Probleme der Selbstauskunft (limited self-knowledge)"
                ],
                "correct_answers": [0, 1, 2, 3, 4],
                "explanation": "🎯 **Methodenkritik:** Big-Five-Assessments haben mehrere Limitationen: Response Biases, kulturelle Variabilität, eingeschränkte ökologische Validität.",
                "learning_point": "Wissenschaftliche Diagnostik erfordert kritische Reflexion methodischer Grenzen."
            }
        ]
    
    def display_quiz(self):
        """Hauptmethode zur Anzeige des Clinical Reasoning Trainings"""
        st.header("🧠 Big Five Clinical Reasoning Training")
        st.markdown("**Training des diagnostischen Urteilsvermögens in mehrdeutigen Situationen**")
        
        self._initialize_session_state()
        
        if not st.session_state.quiz_configurated:
            self.show_training_configuration()
            return
        
        if not st.session_state.training_started:
            self.show_training_intro()
            return
        
        if st.session_state.show_results:
            self.show_training_results()
        else:
            self.show_current_exercise()
    
    def _initialize_session_state(self):
        """Initialisiert Session State Variablen"""
        if 'clinical_initialized' not in st.session_state:
            st.session_state.clinical_initialized = True
            st.session_state.quiz_configurated = False
            st.session_state.training_started = False
            st.session_state.current_exercise = 0
            st.session_state.reasoning_score = 0
            st.session_state.show_results = False
            st.session_state.answer_evaluated = False
            st.session_state.exercise_questions = []
            st.session_state.user_responses = []
    
    def show_training_configuration(self):
        """Zeigt die Trainings-Konfiguration"""
        st.markdown("## 🎯 Clinical Reasoning Training konfigurieren")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔬 Grundlagen-Training")
            st.markdown("""
            - **3 Übungen** (ca. 10-15 Minuten)
            - **Fokus:** Basis-Interpretationen und einfache Muster
            - **Perfekt für:** Einstieg in klinisches Reasoning
            """)
            if st.button("Grundlagen starten", use_container_width=True, key="btn_basic"):
                self.setup_training("basic")
        
        with col2:
            st.subheader("🎓 Experten-Training") 
            st.markdown("""
            - **6 Übungen** (ca. 20-25 Minuten)
            - **Umfassend:** Komplexe Muster und kritische Reflexion
            - **Vertieft:** Probabilistisches Denken und Methodenkritik
            """)
            if st.button("Experten starten", use_container_width=True, key="btn_expert"):
                self.setup_training("expert")
    
    def setup_training(self, training_level):
        """Bereitet das Training vor"""
        all_exercises = self.all_questions.copy()
        random.shuffle(all_exercises)
        
        if training_level == "basic":
            exercises = all_exercises[:3]
        else:
            exercises = all_exercises[:6]
        
        st.session_state.exercise_questions = exercises
        st.session_state.quiz_configurated = True
        st.session_state.training_level = training_level
        st.rerun()
    
    def show_training_intro(self):
        """Zeigt die Trainingseinleitung"""
        exercise_count = len(st.session_state.exercise_questions)
        
        st.success(f"**🎯 {st.session_state.training_level.capitalize()}-Training konfiguriert: {exercise_count} Übungen**")
        
        st.info("""
        **📚 Clinical Reasoning Kompetenzen trainieren:**
        
        🎯 **Ziele dieses Trainings:**
        - Mehrdeutige Verhaltensmuster interpretieren lernen
        - Probabilistisches statt binäres Denken entwickeln  
        - Dimensions-Kombinationen verstehen
        - Situative vs. dispositionale Faktoren unterscheiden
        
        💡 **Lernphilosophie:**
        - Es gibt selten eine einzige "richtige" Antwort
        - Verschiedene Interpretationen können gleichzeitig plausibel sein
        - Kontext verändert die Bedeutung von Verhalten
        """)
        
        if st.button("🎯 Training beginnen", type="primary", use_container_width=True):
            st.session_state.training_started = True
            st.session_state.start_time = time.time()
            st.session_state.answer_evaluated = False
            st.rerun()
    
    def show_current_exercise(self):
        """Zeigt die aktuelle Übung"""
        if st.session_state.current_exercise >= len(st.session_state.exercise_questions):
            st.session_state.show_results = True
            st.rerun()
            return
            
        exercise_data = st.session_state.exercise_questions[st.session_state.current_exercise]
        
        # Fortschrittsanzeige
        progress = (st.session_state.current_exercise + 1) / len(st.session_state.exercise_questions)
        st.progress(progress)
        st.caption(f"Übung {st.session_state.current_exercise + 1} von {len(st.session_state.exercise_questions)}")
        
        # Schwierigkeitsgrad
        difficulty_icons = {1: "🟢", 2: "🟡", 3: "🔴"}
        st.write(f"{difficulty_icons[exercise_data['difficulty']]} **Schwierigkeitsgrad {exercise_data['difficulty']}/3**")
        
        # Übungstyp-spezifische Anzeige
        exercise_handlers = {
            'likert_interpretation': self.show_likert_exercise,
            'multiple_correct_behavioral': self.show_multiple_behavioral_exercise,
            'combination_question': self.show_combination_exercise,
            'trick_scenario': self.show_trick_scenario_exercise,
            'ranking_task': self.show_ranking_exercise,
            'research_critical': self.show_research_critical_exercise
        }
        
        handler = exercise_handlers.get(exercise_data['type'])
        if handler:
            handler(exercise_data)
        else:
            st.error(f"Unbekannter Übungstyp: {exercise_data['type']}")
    
    def show_likert_exercise(self, exercise_data):
        """Zeigt Likert-Skalen Übung"""
        st.markdown(f"### 📊 {exercise_data['question']}")
        
        with st.expander("📋 Verhaltensbeschreibung anzeigen", expanded=True):
            st.write(exercise_data['scenario'])
        
        st.write("**Bewerten Sie auf einer Skala von 1-5:**")
        st.caption("1 = sehr unwahrscheinlich, 3 = neutral, 5 = sehr wahrscheinlich")
        
        if not st.session_state.answer_evaluated:
            user_ratings = []
            for i, interpretation in enumerate(exercise_data['interpretations']):
                rating = st.slider(
                    f"{interpretation}",
                    min_value=1, max_value=5, value=3,
                    key=f"likert_{exercise_data['id']}_{i}"
                )
                user_ratings.append(rating)
            
            if st.button("📈 Einschätzung auswerten", type="primary", key=f"submit_{exercise_data['id']}"):
                self.evaluate_likert_ratings(user_ratings, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_likert_ratings(self, user_ratings, exercise_data):
        """Bewertet Likert-Einschätzungen mit Plotly Visualisierung"""
        expert_ratings = exercise_data['expert_ratings']
        tolerance = exercise_data['tolerance']
        
        deviations = [abs(user - expert) for user, expert in zip(user_ratings, expert_ratings)]
        within_tolerance = sum(1 for dev in deviations if dev <= tolerance)
        accuracy = (within_tolerance / len(deviations)) * 100
        
        st.subheader("📊 Auswertung Ihrer Einschätzung")
        
        if accuracy >= 80:
            st.success(f"🎉 Exzellente probabilistische Einschätzung! ({accuracy:.1f}% im Toleranzbereich)")
            st.session_state.reasoning_score += 1
        elif accuracy >= 60:
            st.warning(f"👍 Gute Einschätzung ({accuracy:.1f}% im Toleranzbereich)")
        else:
            st.error(f"📚 Deutliche Abweichungen von Experteneinschätzungen ({accuracy:.1f}% im Toleranzbereich)")
        
        # Plotly Visualisierung
        fig = go.Figure()
        
        # Ihre Einschätzungen
        fig.add_trace(go.Scatter(
            x=exercise_data['interpretations'],
            y=user_ratings,
            mode='markers+lines',
            name='Ihre Einschätzung',
            marker=dict(size=12, color='blue'),
            line=dict(color='blue', width=2)
        ))
        
        # Experteneinschätzungen
        fig.add_trace(go.Scatter(
            x=exercise_data['interpretations'],
            y=expert_ratings,
            mode='markers+lines',
            name='Experteneinschätzung',
            marker=dict(size=12, color='red'),
            line=dict(color='red', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title="Vergleich Ihrer Einschätzung mit Expertenrating",
            xaxis_title="Interpretationen",
            yaxis_title="Plausibilität (1-5)",
            yaxis=dict(range=[0.5, 5.5]),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("📚 Klinische Einordnung", expanded=True):
            st.info(exercise_data["explanation"])
            st.caption(f"**Lernpunkt:** {exercise_data['learning_point']}")
    
    def show_multiple_behavioral_exercise(self, exercise_data):
        """Zeigt Multiple-Choice Behavioral Interpretation"""
        st.markdown(f"### 👥 {exercise_data['question']}")
        
        with st.expander("📋 Verhaltensbeobachtung anzeigen", expanded=True):
            st.write(exercise_data['scenario'])
        
        if not st.session_state.answer_evaluated:
            user_answers = st.multiselect(
                "Wählen Sie alle plausiblen Interpretationen:",
                exercise_data["interpretations"],
                key=f"multiple_{exercise_data['id']}"
            )
            
            if st.button("🔮 Interpretationen bewerten", type="primary", key=f"submit_{exercise_data['id']}"):
                self.evaluate_behavioral_interpretation(user_answers, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_behavioral_interpretation(self, user_answers, exercise_data):
        """Bewertet behavioral Interpretationen mit Plotly"""
        user_indices = [exercise_data["interpretations"].index(ans) for ans in user_answers]
        correct_indices = exercise_data["correct_answers"]
        
        correct_selected = len(set(user_indices) & set(correct_indices))
        incorrect_selected = len(set(user_indices) - set(correct_indices))
        missed_correct = len(set(correct_indices) - set(user_indices))
        
        st.subheader("👥 Auswertung Verhaltensinterpretation")
        
        if correct_selected == len(correct_indices) and incorrect_selected == 0:
            st.success("🎉 Vollständiges und akkurates Interpretationsspektrum!")
            st.session_state.reasoning_score += 1
        elif incorrect_selected == 0:
            st.warning("👍 Korrekte Auswahl, aber nicht vollständig.")
        else:
            st.error("📚 Enthält fehlerhafte oder unplausible Interpretationen.")
        
        # Plotly Donut Chart für die Auswertung
        labels = ['Korrekt gewählt', 'Übersehen', 'Falsch gewählt']
        values = [correct_selected, missed_correct, incorrect_selected]
        colors = ['#00cc96', '#ffa15a', '#ef553b']
        
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=.3,
            marker_colors=colors
        )])
        
        fig.update_layout(
            title="Zusammenfassung Ihrer Interpretationen",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("📚 Wissenschaftliche Einordnung", expanded=True):
            st.info(exercise_data["explanation"])
            st.caption(f"**Lernpunkt:** {exercise_data['learning_point']}")
    
    def show_combination_exercise(self, exercise_data):
        """Zeigt Kombinations-Übung"""
        st.markdown(f"### 🧩 {exercise_data['question']}")
        
        with st.expander("📋 Komplexes Verhaltensmuster anzeigen", expanded=True):
            st.write(exercise_data['scenario'])
            st.info(f"**Muster:** {exercise_data['behavior_pattern']}")
        
        if not st.session_state.answer_evaluated:
            user_choice = st.radio(
                "Wählen Sie die beste Erklärung:",
                exercise_data["combinations"],
                key=f"combination_{exercise_data['id']}"
            )
            
            if st.button("🎭 Kombination bewerten", type="primary", key=f"submit_{exercise_data['id']}"):
                user_index = exercise_data["combinations"].index(user_choice)
                self.evaluate_combination_choice(user_index, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_combination_choice(self, user_index, exercise_data):
        """Bewertet Kombinations-Auswahl"""
        correct_index = exercise_data["correct_combination"]
        
        st.subheader("🎭 Auswertung Dimensions-Kombination")
        
        if user_index == correct_index:
            st.success("🎉 Exzellente Analyse des komplexen Musters!")
            st.session_state.reasoning_score += 1
        else:
            st.error("❌ Die gewählte Kombination erklärt das Muster nicht vollständig.")
            st.info(f"💡 **Optimale Erklärung:** {exercise_data['combinations'][correct_index]}")
        
        with st.expander("📚 Interaktionsanalyse", expanded=True):
            st.info(exercise_data["explanation"])
            st.caption(f"**Lernpunkt:** {exercise_data['learning_point']}")
    
    def show_trick_scenario_exercise(self, exercise_data):
        """Zeigt Trick-Scenario Übung"""
        st.markdown(f"### ⚠️ {exercise_data['question']}")
        
        with st.expander("📋 Situationsbeschreibung anzeigen", expanded=True):
            st.write(exercise_data['scenario'])
        
        if not st.session_state.answer_evaluated:
            st.write("**Wählen Sie die plausiblen Erklärungen:**")
            user_answers = st.multiselect(
                "Mehrfachauswahl möglich:",
                exercise_data["options"],
                key=f"trick_{exercise_data['id']}"
            )
            
            if st.button("⏱️ Trait vs. State analysieren", type="primary", key=f"submit_{exercise_data['id']}"):
                user_indices = [exercise_data["options"].index(ans) for ans in user_answers]
                self.evaluate_trick_scenario(user_indices, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_trick_scenario(self, user_indices, exercise_data):
        """Bewertet Trick-Scenario"""
        correct_indices = exercise_data["correct_answers"]
        
        st.subheader("⏱️ Auswertung Trait vs. State Analyse")
        
        if set(user_indices) == set(correct_indices):
            st.success("🎉 Exzellente Unterscheidung zwischen Persönlichkeit und situativen Faktoren!")
            st.session_state.reasoning_score += 1
        else:
            st.warning("📚 Differenzierung zwischen stabilen Traits und akuten States verbesserungsfähig")
        
        with st.expander("📚 Situative vs. Dispositionale Faktoren", expanded=True):
            st.info(exercise_data["explanation"])
            st.caption(f"**Lernpunkt:** {exercise_data['learning_point']}")
    
    def show_ranking_exercise(self, exercise_data):
        """Zeigt Ranking-Übung"""
        st.markdown(f"### 📈 {exercise_data['question']}")
        
        with st.expander("📋 Fallbeschreibung anzeigen", expanded=True):
            st.write(exercise_data['scenario'])
        
        if not st.session_state.answer_evaluated:
            st.write("**Ziehen Sie die Hypothesen in die richtige Reihenfolge (1 = am plausibelsten):**")
            
            # Drag-and-drop Simulation mit selectboxen
            hypotheses = exercise_data["hypotheses"].copy()
            user_ranking = []
            
            for i in range(len(hypotheses)):
                available_options = [h for h in hypotheses if h not in user_ranking]
                rank_choice = st.selectbox(
                    f"Platz {i+1}:",
                    available_options,
                    key=f"rank_{exercise_data['id']}_{i}"
                )
                user_ranking.append(rank_choice)
            
            if st.button("🎯 Ranking bewerten", type="primary", key=f"submit_{exercise_data['id']}"):
                user_indices = [exercise_data["hypotheses"].index(ans) for ans in user_ranking]
                self.evaluate_ranking(user_indices, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_ranking(self, user_ranking, exercise_data):
        """Bewertet Ranking-Aufgabe mit Plotly"""
        correct_ranking = exercise_data["correct_ranking"]
        
        # Berechne Ranking-Korrelation
        ranking_distance = sum(abs(user - correct) for user, correct in zip(user_ranking, correct_ranking))
        max_distance = len(user_ranking) * (len(user_ranking) - 1) / 2
        accuracy = max(0, 100 - (ranking_distance / max_distance) * 100)
        
        st.subheader("📈 Auswertung Hypothesen-Priorisierung")
        
        if accuracy >= 90:
            st.success(f"🎉 Exzellente probabilistische Priorisierung! ({accuracy:.1f}% Übereinstimmung)")
            st.session_state.reasoning_score += 1
        elif accuracy >= 70:
            st.warning(f"👍 Gute Einschätzung ({accuracy:.1f}% Übereinstimmung)")
        else:
            st.error(f"📚 Deutliche Abweichungen in der Wahrscheinlichkeitseinschätzung ({accuracy:.1f}% Übereinstimmung)")
        
        # Plotly Balkendiagramm für Ranking-Vergleich
        positions = list(range(1, len(user_ranking) + 1))
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Ihre Rangfolge',
            x=positions,
            y=[exercise_data['hypotheses'][idx] for idx in user_ranking],
            orientation='h',
            marker_color='blue'
        ))
        
        fig.add_trace(go.Bar(
            name='Klinische Rangfolge', 
            x=positions,
            y=[exercise_data['hypotheses'][idx] for idx in correct_ranking],
            orientation='h',
            marker_color='red'
        ))
        
        fig.update_layout(
            title="Vergleich Ihrer Rangfolge mit klinischer Einschätzung",
            xaxis_title="Rangplatz (1 = am plausibelsten)",
            yaxis_title="Hypothesen",
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("📚 Probabilistische Begründung", expanded=True):
            st.info(exercise_data["explanation"])
            st.caption(f"**Lernpunkt:** {exercise_data['learning_point']}")
    
    def show_research_critical_exercise(self, exercise_data):
        """Zeigt Forschungs-Kritik Übung"""
        st.markdown(f"### 🔬 {exercise_data['question']}")
        
        with st.expander("📋 Kontext anzeigen", expanded=True):
            st.write(exercise_data['scenario'])
        
        if not st.session_state.answer_evaluated:
            st.write("**Welche methodischen Probleme sind relevant?**")
            user_answers = st.multiselect(
                "Wählen Sie alle zutreffenden Probleme:",
                exercise_data["critical_issues"],
                key=f"research_{exercise_data['id']}"
            )
            
            if st.button("🎯 Methodenkritik bewerten", type="primary", key=f"submit_{exercise_data['id']}"):
                user_indices = [exercise_data["critical_issues"].index(ans) for ans in user_answers]
                self.evaluate_research_critical(user_indices, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_research_critical(self, user_indices, exercise_data):
        """Bewertet Forschungs-Kritik"""
        correct_indices = exercise_data["correct_answers"]
        
        st.subheader("🔬 Auswertung Methodenkritik")
        
        if set(user_indices) == set(correct_indices):
            st.success("🎉 Umfassende methodenkritische Reflexion!")
            st.session_state.reasoning_score += 1
        else:
            st.warning("📚 Methodische Limitationen nicht vollständig erkannt")
        
        with st.expander("📚 Kritische Reflexion", expanded=True):
            st.info(exercise_data["explanation"])
            st.caption(f"**Lernpunkt:** {exercise_data['learning_point']}")
    
def show_exercise_feedback(self, exercise_data):
    """Zeigt Feedback zur Antwort und Weiter-Button - VOLLSTÄNDIGE LÖSUNG"""
    
    # Feedback zur letzten Antwort anzeigen
    st.subheader("🎯 Auswertung Ihrer Antwort")
    
    # Hier könnten wir die gespeicherten Ergebnisse anzeigen
    # Für jetzt zeigen wir allgemeines Feedback
    st.success("✅ Antwort erfolgreich ausgewertet!")
    
    # Wichtige Lernpunkte hervorheben
    st.info(f"**Lernpunkt:** {exercise_data['learning_point']}")
    
    # Detaillierte Erklärung
    with st.expander("📚 Detaillierte Erklärung anzeigen", expanded=True):
        st.write(exercise_data["explanation"])
    
    # Visualisierung der Ergebnisse (falls vorhanden)
    if hasattr(self, 'last_evaluation_results'):
        self.show_evaluation_visualization(exercise_data)
    
    st.markdown("---")
    st.write("**Wenn Sie bereit für die nächste Übung sind:**")
    
    # Weiter-Button
    if st.button("➡️ **Weiter zur nächsten Übung**", type="primary", use_container_width=True, 
                key=f"next_{exercise_data['id']}"):
        
        st.session_state.current_exercise += 1
        st.session_state.answer_evaluated = False
        
        if st.session_state.current_exercise >= len(st.session_state.exercise_questions):
            st.session_state.show_results = True
        
        st.rerun()

def show_evaluation_visualization(self, exercise_data):
    """Zeigt Visualisierungen der Auswertung"""
    # Platzhalter für spätere Visualisierungen
    st.write("📊 **Ergebnisvisualisierung**")
    # Hier könnten die Plotly-Diagramme aus den Evaluate-Methoden wieder angezeigt werden
    
    def show_training_results(self):
        """Zeigt die Trainingsergebnisse mit Plotly Visualisierungen"""
        st.header("📊 Clinical Reasoning Training abgeschlossen!")
        
        total = len(st.session_state.exercise_questions)
        score = st.session_state.reasoning_score
        percentage = (score / total) * 100
        
        # Zeitberechnung
        if 'start_time' in st.session_state:
            time_used = time.time() - st.session_state.start_time
            minutes = int(time_used // 60)
            seconds = int(time_used % 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
        else:
            time_str = "Unbekannt"
        
        # Metriken in Columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Gelöste Übungen", f"{score}/{total}")
        
        with col2:
            st.metric("Clinical Reasoning Score", f"{percentage:.1f}%")
        
        with col3:
            st.metric("Trainingsdauer", time_str)
        
        # Plotly Score Visualisierung
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = percentage,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Clinical Reasoning Score"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "gray"},
                    {'range': [80, 100], 'color': "lightblue"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        # Kompetenzeinschätzung
        st.markdown("---")
        st.subheader("🎯 Entwickelte Clinical Reasoning Kompetenzen")
        
        competencies = [
            "✅ Mehrdeutige Verhaltensmuster interpretieren",
            "✅ Probabilistisches Denken anwenden", 
            "✅ Dimensions-Kombinationen analysieren",
            "✅ Trait vs. State unterscheiden",
            "✅ Methodische Limitationen reflektieren"
        ]
        
        for competency in competencies:
            st.write(competency)
        
        # Entwicklungsempfehlungen
        st.markdown("---")
        st.subheader("🚀 Empfohlene Weiterentwicklung")
        
        if percentage >= 85:
            st.success("**🎉 Exzellentes Clinical Reasoning!** Nächste Schritte: Supervision komplexer Fälle")
        elif percentage >= 70:
            st.success("**👍 Sehr gutes Clinical Reasoning!** Nächste Schritte: Komplexere Fälle")
        elif percentage >= 50:
            st.warning("**📚 Gute Grundlagen - Entwicklungspotenzial!** Nächste Schritte: Mehr Übung mit komplexen Mustern")
        else:
            st.info("**💡 Grundverständnis - Weiteres Training empfohlen!** Nächste Schritte: Basis-Übungen wiederholen")
        
        st.markdown("---")
        st.subheader("🔁 Training wiederholen oder vertiefen")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 Neues Training starten", use_container_width=True):
                for key in list(st.session_state.keys()):
                    if key != 'clinical_initialized':
                        del st.session_state[key]
                st.rerun()
        
        with col2:
            if st.button("📚 Theorie vertiefen", use_container_width=True):
                st.info("Studieren Sie die bereitgestellten Dokumente zur Vertiefung Ihrer Kenntnisse.")
