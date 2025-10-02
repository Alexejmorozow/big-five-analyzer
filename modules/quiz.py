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
        basic_questions = [
            # 🎯 BASISWISSEN FRAGEN (NEU)
            {
                "id": 101,
                "type": "basic_knowledge",
                "difficulty": 1,
                "question": "Wofür steht das Akronym OCEAN im Big-Five-Modell?",
                "options": [
                    "Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism",
                    "Organization, Creativity, Energy, Ambition, Nervousness", 
                    "Optimism, Confidence, Empathy, Awareness, Normality",
                    "Observation, Concentration, Efficiency, Adaptation, Neutrality"
                ],
                "correct_answer": 0,
                "explanation": "✅ **OCEAN** steht für die fünf Hauptdimensionen: Openness (Offenheit), Conscientiousness (Gewissenhaftigkeit), Extraversion, Agreeableness (Verträglichkeit), Neuroticism (Neurotizismus).",
                "learning_point": "Das OCEAN-Modell ist die internationale Bezeichnung für das Fünf-Faktoren-Modell."
            },
            {
                "id": 102,
                "type": "basic_knowledge", 
                "difficulty": 1,
                "question": "Welche Dimension beschreibt emotionale Stabilität und Resilienz?",
                "options": [
                    "Niedriger Neurotizismus",
                    "Hohe Gewissenhaftigkeit",
                    "Hohe Extraversion", 
                    "Hohe Verträglichkeit"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Niedriger Neurotizismus** bedeutet emotionale Stabilität. Der Gegenpol (hoher Neurotizismus) beschreibt emotionale Labilität.",
                "learning_point": "Neurotizismus = emotionale Labilität; niedriger Neurotizismus = emotionale Stabilität"
            },
            {
                "id": 103,
                "type": "basic_knowledge",
                "difficulty": 1, 
                "question": "Auf welchem wissenschaftlichen Ansatz basiert die Entwicklung der Big Five?",
                "options": [
                    "Lexikalischer Ansatz",
                    "Behavioristischer Ansatz",
                    "Psychoanalytischer Ansatz",
                    "Humanistischer Ansatz"
                ],
                "correct_answer": 0,
                "explanation": "✅ Der **lexikalische Ansatz** geht davon aus, dass sich alle wichtigen Persönlichkeitsmerkmale in der Sprache niedergeschlagen haben.",
                "learning_point": "Allport & Odbert identifizierten 1936 über 18.000 Persönlichkeitsbegriffe als Grundlage."
            },
            {
                "id": 104,
                "type": "basic_knowledge",
                "difficulty": 1,
                "question": "Welche Big-Five-Dimension korreliert am stärksten mit beruflichem Erfolg?",
                "options": [
                    "Gewissenhaftigkeit",
                    "Extraversion", 
                    "Offenheit für Erfahrungen",
                    "Verträglichkeit"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Gewissenhaftigkeit** ist der robusteste Prädiktor für Arbeitsleistung über fast alle Berufsgruppen hinweg.",
                "learning_point": "Strukturiertheit, Zuverlässigkeit und Zielstrebigkeit führen zu besserer Arbeitsleistung."
            },
            {
                "id": 105, 
                "type": "basic_knowledge",
                "difficulty": 1,
                "question": "Was bedeutet hohe Ausprägung in 'Offenheit für Erfahrungen'?",
                "options": [
                    "Kreativ, neugierig, vielseitig interessiert",
                    "Pünktlich, organisiert, zuverlässig",
                    "Gesellig, energisch, gesprächig", 
                    "Hilfsbereit, mitfühlend, vertrauensvoll"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Hohe Offenheit** charakterisiert kreative, neugierige Personen, die offen für neue Ideen und Erfahrungen sind.",
                "learning_point": "Offenheit = Intellektuelle Neugier + Kreativität + Experimentierfreude"
            },
            {
                "id": 106,
                "type": "basic_knowledge",
                "difficulty": 1,
                "question": "Welches Instrument gilt als Goldstandard in der Big-Five-Forschung?",
                "options": [
                    "NEO-PI-R (NEO Persönlichkeitsinventar)",
                    "Myers-Briggs Typenindikator (MBTI)",
                    "DISG-Persönlichkeitsmodell", 
                    "Big-Five-Inventory-10 (BFI-10)"
                ],
                "correct_answer": 0,
                "explanation": "✅ Der **NEO-PI-R** von Costa & McCrae ist der wissenschaftliche Goldstandard mit 240 Items und 30 Facetten.",
                "learning_point": "NEO-PI-R erfasst 5 Domänen + 6 Facetten pro Domäne = umfassendste Erfassung"
            },
            {
                "id": 107,
                "type": "basic_knowledge", 
                "difficulty": 1,
                "question": "Welcher genetische Einfluss wird für die Big Five angenommen?",
                "options": [
                    "40-60% Erblichkeit",
                    "10-20% Erblichkeit", 
                    "70-80% Erblichkeit",
                    "90-100% Erblichkeit"
                ],
                "correct_answer": 0,
                "explanation": "✅ Zwillingsstudien zeigen **40-60% Erblichkeit** für Persönlichkeitsmerkmale, der Rest durch individuelle Umwelt.",
                "learning_point": "Persönlichkeit ist etwa zur Hälfte genetisch, zur Hälfte umweltbedingt."
            },
            {
                "id": 108,
                "type": "basic_knowledge",
                "difficulty": 1,
                "question": "Was beschreibt die Dimension 'Verträglichkeit'?",
                "options": [
                    "Kooperationsbereitschaft, Mitgefühl, Altruismus",
                    "Emotionale Stabilität, Gelassenheit, Resilienz", 
                    "Strukturiertheit, Organisation, Zielstrebigkeit",
                    "Geselligkeit, Energie, positive Emotionalität"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Verträglichkeit** umfasst Altruismus, Mitgefühl, Kooperationsbereitschaft und zwischenmenschliches Vertrauen.",
                "learning_point": "Hohe Verträglichkeit = hilfsbereit, mitfühlend; niedrige Verträglichkeit = wettbewerbsorientiert, skeptisch"
            },
            {
                "id": 109,
                "type": "basic_knowledge",
                "difficulty": 1,
                "question": "Welche Aussage zu Geschlechterstereotypen ist korrekt?",
                "options": [
                    "Frauen werden höhere Verträglichkeit zugeschrieben",
                    "Männer werden höhere emotionale Labilität zugeschrieben",
                    "Frauen werden niedrigere Gewissenhaftigkeit zugeschrieben", 
                    "Männer werden höhere Offenheit zugeschrieben"
                ],
                "correct_answer": 0,
                "explanation": "✅ Studien zeigen: Frauen wird stereotypisch **höhere Verträglichkeit** zugeschrieben (Löckenhoff et al., 2014).",
                "learning_point": "Geschlechterstereotype entsprechen oft tatsächlichen, kleinen Geschlechtsunterschieden."
            },
            {
                "id": 110,
                "type": "basic_knowledge",
                "difficulty": 1, 
                "question": "Was kritisierte Dan McAdams am Big-Five-Modell?",
                "options": [
                    "Es erklärt menschliches Verhalten nur unzureichend",
                    "Es hat zu viele Dimensionen",
                    "Es ist kulturell nicht übertragbar", 
                    "Es misst nur vorübergehende Zustände"
                ],
                "correct_answer": 0,
                "explanation": "✅ **McAdams** kritisiert die geringe Erklärungstiefe: Das Modell könne Verhalten weder umfassend erklären noch vorhersagen.",
                "learning_point": "Big Five beschreiben WAS jemand ist, aber nicht WIE oder WARUM jemand so handelt."
            },
            # 🎯 ANWENDUNGSFRAGEN (NEU)
            {
                "id": 111,
                "type": "application_basic", 
                "difficulty": 1,
                "question": "Eine Person geht gerne auf Partys, ist gesellig und initiiert Gespräche. Welche Dimension?",
                "options": [
                    "Hohe Extraversion",
                    "Hohe Offenheit",
                    "Niedriger Neurotizismus",
                    "Hohe Verträglichkeit"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Hohe Extraversion** zeigt sich in Geselligkeit, Gesprächigkeit und Energie in sozialen Situationen.",
                "learning_point": "Extraversion = Soziale Energie, Geselligkeit, positive Emotionalität"
            },
            {
                "id": 112,
                "type": "application_basic",
                "difficulty": 1,
                "question": "Jemand plant seinen Tag minutiös durch, dokumentiert akribisch und korrigiert Fehler. Welche Dimension?",
                "options": [
                    "Hohe Gewissenhaftigkeit", 
                    "Hohe Offenheit",
                    "Niedriger Neurotizismus", 
                    "Hohe Verträglichkeit"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Hohe Gewissenhaftigkeit** äußert sich in Strukturiertheit, Organisation und Sorgfalt.",
                "learning_point": "Gewissenhaftigkeit = Organisation + Zuverlässigkeit + Zielstrebigkeit"
            },
            {
                "id": 113,
                "type": "application_basic",
                "difficulty": 1,
                "question": "Eine Person ist leicht gestresst, besorgt und emotional. Welche Dimension?",
                "options": [
                    "Hoher Neurotizismus",
                    "Niedrige Extraversion", 
                    "Niedrige Verträglichkeit",
                    "Hohe Offenheit"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Hoher Neurotizismus** bedeutet emotionale Labilität mit häufigen negativen Emotionen wie Angst und Besorgnis.",
                "learning_point": "Neurotizismus = Anfälligkeit für negative Emotionen + emotionale Labilität"
            },
            {
                "id": 114, 
                "type": "application_basic",
                "difficulty": 1,
                "question": "Eine Person hilft Kollegen, zeigt Mitgefühl und vermeidet Konflikte. Welche Dimension?",
                "options": [
                    "Hohe Verträglichkeit",
                    "Hohe Gewissenhaftigkeit",
                    "Niedrige Extraversion",
                    "Hohe Offenheit" 
                ],
                "correct_answer": 0,
                "explanation": "✅ **Hohe Verträglichkeit** zeigt sich in Altruismus, Kooperation und Konfliktvermeidung.",
                "learning_point": "Verträglichkeit = Mitgefühl + Hilfsbereitschaft + Kooperationsorientierung"
            },
            {
                "id": 115,
                "type": "application_basic",
                "difficulty": 1,
                "question": "Jemand liest gerne Science-Fiction, besucht Museen und diskutiert philosophische Themen. Welche Dimension?",
                "options": [
                    "Hohe Offenheit für Erfahrungen",
                    "Hohe Extraversion",
                    "Hohe Gewissenhaftigkeit",
                    "Niedrige Verträglichkeit"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Hohe Offenheit** charakterisiert intellektuelle Neugier, Fantasie und Interesse an abstrakten Ideen.",
                "learning_point": "Offenheit = Intellektuelle Neugier + Ästhetisches Empfinden + Fantasie"
            },
            # 🎯 WISSENSCHAFTLICHE GRUNDLAGEN (NEU)
            {
                "id": 116,
                "type": "science_basic", 
                "difficulty": 1,
                "question": "Was bedeutet 'kriteriumsvalidität' bei Persönlichkeitstests?",
                "options": [
                    "Zusammenhang mit externen Erfolgskriterien",
                    "Interne Konsistenz der Items",
                    "Kulturelle Fairness des Tests",
                    "Objektive Auswertbarkeit"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Kriteriumsvalidität** misst den Zusammenhang zwischen Testergebnissen und externen Kriterien wie Berufserfolg.",
                "learning_point": "Validität = Misst der Test das, was er messen soll?"
            },
            {
                "id": 117,
                "type": "science_basic",
                "difficulty": 1,
                "question": "Welche Aussage zur hierarchischen Struktur der Big Five ist korrekt?",
                "options": [
                    "Jede Dimension hat multiple Facetten",
                    "Es gibt nur die 5 Hauptdimensionen",
                    "Facetten sind wichtiger als Dimensionen", 
                    "Die Struktur ist flach ohne Ebenen"
                ],
                "correct_answer": 0,
                "explanation": "✅ Das Big-Five-Modell ist **hierarchisch**: 5 Domänen → 2 Aspekte pro Domäne → 6 Facetten pro Domäne.",
                "learning_point": "Hierarchie ermöglicht differenzierte Persönlichkeitsbeschreibung"
            },
            {
                "id": 118,
                "type": "science_basic", 
                "difficulty": 1,
                "question": "Was ist das 'Bandbreiten-Fidelitäts-Dilemma'?",
                "options": [
                    "Kompromiss zwischen Breite und Genauigkeit der Messung",
                    "Konflikt zwischen Validität und Reliabilität",
                    "Widerspruch zwischen Theorie und Praxis", 
                    "Dilemma bei kultureller Anpassung"
                ],
                "correct_answer": 0,
                "explanation": "✅ Das **Bandbreiten-Fidelitäts-Dilemma** beschreibt den Zielkonflikt zwischen breiter Erfassung (Bandbreite) und präziser Messung (Fidelität).",
                "learning_point": "Breite vs. Tiefe: Soll der Test allgemein oder spezifisch sein?"
            },
            {
                "id": 119,
                "type": "science_basic",
                "difficulty": 1,
                "question": "Welche Validität haben Persönlichkeitstests für Berufserfolg?",
                "options": [
                    "Moderate Validität (r ≈ 0.3)",
                    "Sehr hohe Validität (r ≈ 0.8)", 
                    "Keine Validität (r ≈ 0.0)",
                    "Negative Validität (r ≈ -0.2)"
                ],
                "correct_answer": 0,
                "explanation": "✅ Persönlichkeitstests zeigen **moderate Validität** um r=0.3, besonders Gewissenhaftigkeit für Arbeitsleistung.",
                "learning_point": "Kombination mit Intelligenztests erhöht Vorhersagekraft um 18%"
            },
            {
                "id": 120,
                "type": "science_basic",
                "difficulty": 1,
                "question": "Was bedeutet 'inkrementelle Validität'?",
                "options": [
                    "Mehrwert zusätzlicher Testverfahren",
                    "Verbesserung der Reliabilität",
                    "Kulturelle Anpassung von Tests", 
                    "Automatisierte Testauswertung"
                ],
                "correct_answer": 0,
                "explanation": "✅ **Inkrementelle Validität** beschreibt, wie sehr ein zusätzliches Verfahren die Vorhersagekraft verbessert.",
                "learning_point": "Multimodale Diagnostik (Test + Interview) ist besser als einzelne Verfahren"
            }
        ]

        # Antworten shufflen für jede Basis-Frage
        for question in basic_questions:
            if 'options' in question and 'correct_answer' in question:
                correct_index = question['correct_answer']
                correct_answer = question['options'][correct_index]
                
                # Options mischen
                random.shuffle(question['options'])
                
                # Neuen Index der korrekten Antwort finden
                new_correct_index = question['options'].index(correct_answer)
                question['correct_answer'] = new_correct_index

        advanced_questions = [
            # 📊 LIKERT-INTERPRETATION (ALTE FRAGEN - KOMPLETT)
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
                    "Strategische Anpassung (bewusste Verhaltensänderation)"
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

        return basic_questions + advanced_questions

    # NEUE METHODEN FÜR BASIS-FRAGEN
    def show_basic_knowledge_exercise(self, exercise_data):
        """Zeigt Basis-Wissensfragen (Single Choice)"""
        st.markdown(f"### 🎯 {exercise_data['question']}")
        
        if not st.session_state.answer_evaluated:
            user_choice = st.radio(
                "Wählen Sie die richtige Antwort:",
                exercise_data["options"],
                key=f"basic_{exercise_data['id']}"
            )
            
            if st.button("📝 Antwort überprüfen", type="primary", key=f"submit_{exercise_data['id']}"):
                user_index = exercise_data["options"].index(user_choice)
                # Speichere Benutzerantwort
                st.session_state.user_responses.append({
                    'exercise_id': exercise_data['id'],
                    'type': exercise_data['type'],
                    'user_choice': user_index,
                    'timestamp': time.time()
                })
                self.evaluate_basic_question(user_index, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)

    def show_application_basic_exercise(self, exercise_data):
        """Zeigt Basis-Anwendungsfragen"""
        self.show_basic_knowledge_exercise(exercise_data)  # Gleiches Format

    def show_science_basic_exercise(self, exercise_data):
        """Zeigt Basis-Wissenschaftsfragen""" 
        self.show_basic_knowledge_exercise(exercise_data)  # Gleiches Format

    def evaluate_basic_question(self, user_index, exercise_data):
        """Bewertet Basis-Fragen"""
        correct_index = exercise_data["correct_answer"]
        
        # Scoring für Gesamtergebnis
        if user_index == correct_index:
            st.session_state.reasoning_score += 1

    # VERGLEICHSMETHODEN MÜSSEN VOR show_exercise_feedback KOMMEN!
    def _show_basic_comparison(self, user_response, exercise_data):
        """Vergleich für Basis-Fragen (Single Choice)"""
        if not user_response or 'user_choice' not in user_response:
            st.error("Keine Benutzerantwort gefunden")
            return
            
        user_choice = user_response['user_choice']
        correct_choice = exercise_data['correct_answer']
        
        if user_choice == correct_choice:
            evaluation = "✅ **RICHTIG**"
            color = "green"
        else:
            evaluation = "❌ **FALSCH**"
            color = "red"
        
        st.markdown(f"### {evaluation}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🎯 Deine Antwort:**")
            st.write(f"**{exercise_data['options'][user_choice]}**")
            if user_choice != correct_choice:
                st.error("❌ Diese Antwort ist nicht korrekt")
        
        with col2:
            st.markdown("**🏆 Richtige Antwort:**")
            st.write(f"**{exercise_data['options'][correct_choice]}**")
            st.success("✅ Das ist die korrekte Antwort")

    def _show_multiple_choice_comparison(self, user_response, exercise_data):
        """Vergleich für Multiple-Choice Fragen"""
        if not user_response or 'user_answers' not in user_response:
            st.error("Keine Benutzerantwort gefunden")
            return
            
        user_choices = user_response['user_answers']
        correct_choices = exercise_data['correct_answers']
        
        # Bewertung
        correct_selected = set(user_choices) & set(correct_choices)
        incorrect_selected = set(user_choices) - set(correct_choices)
        missed_correct = set(correct_choices) - set(user_choices)
        
        # Gesamtbewertung
        if not incorrect_selected and not missed_correct:
            evaluation = "✅ **VOLLSTÄNDIG RICHTIG**"
            color = "green"
        elif not incorrect_selected:
            evaluation = "⚠️ **TEILWEISE RICHTIG** (Einige plausible Interpretationen übersehen)"
            color = "orange"
        else:
            evaluation = "❌ **ENTHÄLT FEHLER** (Unplausible Interpretationen gewählt)"
            color = "red"
        
        st.markdown(f"### {evaluation}")
        
        # Gegenüberstellung in Columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🎯 Deine Auswahl:**")
            for i, interpretation in enumerate(exercise_data['interpretations']):
                if i in user_choices:
                    status = "✅" if i in correct_choices else "❌"
                    st.write(f"{status} {interpretation}")
        
        with col2:
            st.markdown("**🏆 Optimale Auswahl:**")
            for i, interpretation in enumerate(exercise_data['interpretations']):
                if i in correct_choices:
                    status = "✅" if i in user_choices else "🔸"
                    st.write(f"{status} {interpretation}")

    def _show_likert_comparison(self, user_response, exercise_data):
        """Vergleich für Likert-Skalen Fragen"""
        if not user_response or 'user_ratings' not in user_response:
            st.error("Keine Benutzerantwort gefunden")
            return
            
        user_ratings = user_response['user_ratings']
        expert_ratings = exercise_data['expert_ratings']
        tolerance = exercise_data['tolerance']
        
        # Bewertung berechnen
        deviations = [abs(user - expert) for user, expert in zip(user_ratings, expert_ratings)]
        within_tolerance = sum(1 for dev in deviations if dev <= tolerance)
        accuracy = (within_tolerance / len(deviations)) * 100
        
        if accuracy >= 80:
            evaluation = "✅ **SEHR GUTE EINSCHÄTZUNG**"
        elif accuracy >= 60:
            evaluation = "⚠️ **GUTE EINSCHÄTZUNG** (Leichte Abweichungen)"
        else:
            evaluation = "❌ **DEUTLICHE ABWEICHUNGEN**"
        
        st.markdown(f"### {evaluation} ({accuracy:.1f}% im Toleranzbereich)")
        
        # Detailierter Vergleich
        for i, (interpretation, user_rating, expert_rating) in enumerate(zip(
            exercise_data['interpretations'], user_ratings, expert_ratings
        )):
            deviation = abs(user_rating - expert_rating)
            status = "✅" if deviation <= tolerance else "❌"
            
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{interpretation}**")
            with col2:
                st.write(f"Deine Bewertung: **{user_rating}**")
            with col3:
                st.write(f"Experten: **{expert_rating}** {status}")

    def _show_combination_comparison(self, user_response, exercise_data):
        """Vergleich für Kombinations-Fragen"""
        if not user_response or 'user_choice' not in user_response:
            st.error("Keine Benutzerantwort gefunden")
            return
            
        user_choice = user_response['user_choice']
        correct_choice = exercise_data['correct_combination']
        
        if user_choice == correct_choice:
            evaluation = "✅ **RICHTIGE KOMBINATION**"
        else:
            evaluation = "❌ **SUBOPTIMALE KOMBINATION**"
        
        st.markdown(f"### {evaluation}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🎯 Deine Wahl:**")
            st.write(f"**{exercise_data['combinations'][user_choice]}**")
        
        with col2:
            st.markdown("**🏆 Optimale Erklärung:**")
            st.write(f"**{exercise_data['combinations'][correct_choice]}**")

    def _show_trick_comparison(self, user_response, exercise_data):
        """Vergleich für Trick-Szenario Fragen"""
        if not user_response or 'user_answers' not in user_response:
            st.error("Keine Benutzerantwort gefunden")
            return
            
        user_choices = set(user_response['user_answers'])
        correct_choices = set(exercise_data['correct_answers'])
        
        if user_choices == correct_choices:
            evaluation = "✅ **VOLLSTÄNDIG RICHTIG**"
        elif user_choices.issubset(correct_choices):
            evaluation = "⚠️ **TEILWEISE RICHTIG** (Einige States übersehen)"
        elif correct_choices.issubset(user_choices):
            evaluation = "⚠️ **ZUVEL AUSGEWÄHLT** (Auch Traits gewählt)"
        else:
            evaluation = "❌ **FEHLERHAFTE ANALYSE**"
        
        st.markdown(f"### {evaluation}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🎯 Deine Analyse:**")
            for i, option in enumerate(exercise_data['options']):
                if i in user_choices:
                    status = "✅" if i in correct_choices else "❌"
                    st.write(f"{status} {option}")
        
        with col2:
            st.markdown("**🏆 Korrekte Analyse:**")
            for i, option in enumerate(exercise_data['options']):
                if i in correct_choices:
                    status = "✅" if i in user_choices else "🔸"
                    st.write(f"{status} {option}")

    def _show_ranking_comparison(self, user_response, exercise_data):
        """Vergleich für Ranking-Fragen"""
        if not user_response or 'user_ranking' not in user_response:
            st.error("Keine Benutzerantwort gefunden")
            return
            
        user_ranking = user_response['user_ranking']
        correct_ranking = exercise_data['correct_ranking']
        
        # Berechne Ranking-Korrelation
        ranking_distance = sum(abs(user - correct) for user, correct in zip(user_ranking, correct_ranking))
        max_distance = len(user_ranking) * (len(user_ranking) - 1) / 2
        accuracy = max(0, 100 - (ranking_distance / max_distance) * 100)
        
        if accuracy >= 90:
            evaluation = "✅ **EXZELLENTE PRIORISIERUNG**"
        elif accuracy >= 70:
            evaluation = "⚠️ **GUTE PRIORISIERUNG** (Leichte Abweichungen)"
        else:
            evaluation = "❌ **DEUTLICHE ABWEICHUNGEN**"
        
        st.markdown(f"### {evaluation} ({accuracy:.1f}% Übereinstimmung)")
        
        # Detailierter Vergleich
        st.markdown("**📊 Rangfolgen-Vergleich:**")
        for i, (user_idx, correct_idx) in enumerate(zip(user_ranking, correct_ranking)):
            user_hyp = exercise_data['hypotheses'][user_idx]
            correct_hyp = exercise_data['hypotheses'][correct_idx]
            status = "✅" if user_idx == correct_idx else "❌"
            
            col1, col2, col3 = st.columns([1, 3, 3])
            with col1:
                st.write(f"**Platz {i+1}:** {status}")
            with col2:
                st.write(f"Deine Wahl: {user_hyp}")
            with col3:
                if user_idx != correct_idx:
                    st.write(f"Optimal: {correct_hyp}")

    def _show_research_comparison(self, user_response, exercise_data):
        """Vergleich für Forschungs-Kritik Fragen"""
        if not user_response or 'user_answers' not in user_response:
            st.error("Keine Benutzerantwort gefunden")
            return
            
        user_choices = set(user_response['user_answers'])
        correct_choices = set(exercise_data['correct_answers'])
        
        if user_choices == correct_choices:
            evaluation = "✅ **UMFASSENDE METHODENKRITIK**"
        elif user_choices.issubset(correct_choices):
            evaluation = "⚠️ **TEILWEISE KRITISCH** (Einige Probleme übersehen)"
        else:
            evaluation = "❌ **UNVOLLSTÄNDIGE ANALYSE**"
        
        st.markdown(f"### {evaluation}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🎯 Deine Kritikpunkte:**")
            for i, issue in enumerate(exercise_data['critical_issues']):
                if i in user_choices:
                    status = "✅" if i in correct_choices else "❌"
                    st.write(f"{status} {issue}")
        
        with col2:
            st.markdown("**🏆 Alle relevanten Probleme:**")
            for i, issue in enumerate(exercise_data['critical_issues']):
                if i in correct_choices:
                    status = "✅" if i in user_choices else "🔸"
                    st.write(f"{status} {issue}")

    # JETZT ERST show_exercise_feedback (nach allen Vergleichsmethoden)
    def show_exercise_feedback(self, exercise_data):
        """Zeigt klare Gegenüberstellung der Antworten mit Bewertung"""
        
        # Hole die gespeicherte Benutzerantwort
        user_response = st.session_state.user_responses[-1] if st.session_state.user_responses else None
        
        st.subheader("📊 Deine Auswertung")
        
        # Übungstyp-spezifische Auswertung
        if exercise_data['type'] in ['basic_knowledge', 'application_basic', 'science_basic']:
            self._show_basic_comparison(user_response, exercise_data)
        elif exercise_data['type'] == 'multiple_correct_behavioral':
            self._show_multiple_choice_comparison(user_response, exercise_data)
        elif exercise_data['type'] == 'likert_interpretation':
            self._show_likert_comparison(user_response, exercise_data)
        elif exercise_data['type'] == 'combination_question':
            self._show_combination_comparison(user_response, exercise_data)
        elif exercise_data['type'] == 'trick_scenario':
            self._show_trick_comparison(user_response, exercise_data)
        elif exercise_data['type'] == 'ranking_task':
            self._show_ranking_comparison(user_response, exercise_data)
        elif exercise_data['type'] == 'research_critical':
            self._show_research_comparison(user_response, exercise_data)
        
        # Wissenschaftliche Begründung
        st.markdown("---")
        st.subheader("🔬 Wissenschaftliche Einordnung")
        
        with st.expander("📚 **Detaillierte Erklärung**", expanded=True):
            st.info(exercise_data["explanation"])
            st.caption(f"💡 **Lernpunkt:** {exercise_data['learning_point']}")
        
        # Weiter-Button
        st.markdown("---")
        if st.button("➡️ **Weiter zur nächsten Übung**", 
                    type="primary", 
                    use_container_width=True,
                    key=f"next_{exercise_data['id']}"):
            
            st.session_state.current_exercise += 1
            st.session_state.answer_evaluated = False
            
            if st.session_state.current_exercise >= len(st.session_state.exercise_questions):
                st.session_state.show_results = True
            
            st.rerun()

    # REST DES CODES (unverändert)
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
        
        # Übungstyp-Handler
        exercise_handlers = {
            'likert_interpretation': self.show_likert_exercise,
            'multiple_correct_behavioral': self.show_multiple_behavioral_exercise,
            'combination_question': self.show_combination_exercise,
            'trick_scenario': self.show_trick_scenario_exercise,
            'ranking_task': self.show_ranking_exercise,
            'research_critical': self.show_research_critical_exercise,
            'basic_knowledge': self.show_basic_knowledge_exercise,
            'application_basic': self.show_application_basic_exercise,
            'science_basic': self.show_science_basic_exercise
        }
        
        handler = exercise_handlers.get(exercise_data['type'])
        if handler:
            handler(exercise_data)
        else:
            st.error(f"Unbekannter Übungstyp: {exercise_data['type']}")

    def setup_training(self, training_level):
        """Bereitet das Training vor"""
        all_exercises = self.all_questions.copy()
        random.shuffle(all_exercises)
        
        if training_level == "basic":
            # Für Basic-Training: 8 einfache + 2 komplexe Fragen
            basic_questions = [q for q in all_exercises if q['difficulty'] == 1]
            advanced_questions = [q for q in all_exercises if q['difficulty'] > 1]
            exercises = basic_questions[:8] + advanced_questions[:2]
        else:
            # Für Expert-Training: 5 einfache + 10 komplexe Fragen  
            basic_questions = [q for q in all_exercises if q['difficulty'] == 1]
            advanced_questions = [q for q in all_exercises if q['difficulty'] > 1]
            exercises = basic_questions[:5] + advanced_questions[:10]
        
        st.session_state.exercise_questions = exercises
        st.session_state.quiz_configurated = True
        st.session_state.training_level = training_level
        st.rerun()

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
            - **10 Übungen** (ca. 15-20 Minuten)
            - **Fokus:** Basiswissen + einfache Clinical Reasoning Fälle
            - **Perfekt für:** Einstieg in klinisches Reasoning
            """)
            if st.button("Grundlagen starten", use_container_width=True, key="btn_basic"):
                self.setup_training("basic")
        
        with col2:
            st.subheader("🎓 Experten-Training") 
            st.markdown("""
            - **15 Übungen** (ca. 25-30 Minuten)
            - **Umfassend:** Basiswissen + komplexe Clinical Reasoning Fälle
            - **Vertieft:** Probabilistisches Denken und Methodenkritik
            """)
            if st.button("Experten starten", use_container_width=True, key="btn_expert"):
                self.setup_training("expert")
    
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

    # ALTE COMPLEX FRAGEN METHODEN (UNVERÄNDERT)
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
                # Speichere Benutzerantwort vor der Auswertung
                st.session_state.user_responses.append({
                    'exercise_id': exercise_data['id'],
                    'type': exercise_data['type'],
                    'user_ratings': user_ratings.copy(),
                    'timestamp': time.time()
                })
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
        
        # Scoring für Gesamtergebnis
        if accuracy >= 80:
            st.session_state.reasoning_score += 1
        
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
                user_indices = [exercise_data["interpretations"].index(ans) for ans in user_answers]
                # Speichere Benutzerantwort vor der Auswertung
                st.session_state.user_responses.append({
                    'exercise_id': exercise_data['id'],
                    'type': exercise_data['type'],
                    'user_answers': user_indices.copy(),
                    'timestamp': time.time()
                })
                self.evaluate_behavioral_interpretation(user_indices, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_behavioral_interpretation(self, user_indices, exercise_data):
        """Bewertet behavioral Interpretationen mit Plotly"""
        correct_indices = exercise_data["correct_answers"]
        
        correct_selected = len(set(user_indices) & set(correct_indices))
        incorrect_selected = len(set(user_indices) - set(correct_indices))
        missed_correct = len(set(correct_indices) - set(user_indices))
        
        # Scoring für Gesamtergebnis
        if correct_selected == len(correct_indices) and incorrect_selected == 0:
            st.session_state.reasoning_score += 1
        
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
                # Speichere Benutzerantwort vor der Auswertung
                st.session_state.user_responses.append({
                    'exercise_id': exercise_data['id'],
                    'type': exercise_data['type'],
                    'user_choice': user_index,
                    'timestamp': time.time()
                })
                self.evaluate_combination_choice(user_index, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_combination_choice(self, user_index, exercise_data):
        """Bewertet Kombinations-Auswahl"""
        correct_index = exercise_data["correct_combination"]
        
        # Scoring für Gesamtergebnis
        if user_index == correct_index:
            st.session_state.reasoning_score += 1
    
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
                # Speichere Benutzerantwort vor der Auswertung
                st.session_state.user_responses.append({
                    'exercise_id': exercise_data['id'],
                    'type': exercise_data['type'],
                    'user_answers': user_indices.copy(),
                    'timestamp': time.time()
                })
                self.evaluate_trick_scenario(user_indices, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_trick_scenario(self, user_indices, exercise_data):
        """Bewertet Trick-Scenario"""
        correct_indices = exercise_data["correct_answers"]
        
        # Scoring für Gesamtergebnis
        if set(user_indices) == set(correct_indices):
            st.session_state.reasoning_score += 1
    
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
                # Speichere Benutzerantwort vor der Auswertung
                st.session_state.user_responses.append({
                    'exercise_id': exercise_data['id'],
                    'type': exercise_data['type'],
                    'user_ranking': user_indices.copy(),
                    'timestamp': time.time()
                })
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
        
        # Scoring für Gesamtergebnis
        if accuracy >= 90:
            st.session_state.reasoning_score += 1
        
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
                # Speichere Benutzerantwort vor der Auswertung
                st.session_state.user_responses.append({
                    'exercise_id': exercise_data['id'],
                    'type': exercise_data['type'],
                    'user_answers': user_indices.copy(),
                    'timestamp': time.time()
                })
                self.evaluate_research_critical(user_indices, exercise_data)
                st.session_state.answer_evaluated = True
                st.rerun()
        else:
            self.show_exercise_feedback(exercise_data)
    
    def evaluate_research_critical(self, user_indices, exercise_data):
        """Bewertet Forschungs-Kritik"""
        correct_indices = exercise_data["correct_answers"]
        
        # Scoring für Gesamtergebnis
        if set(user_indices) == set(correct_indices):
            st.session_state.reasoning_score += 1

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
                # Nur die Quiz-spezifischen Variablen zurücksetzen
                st.session_state.quiz_configurated = False
                st.session_state.training_started = False  
                st.session_state.current_exercise = 0
                st.session_state.reasoning_score = 0
                st.session_state.show_results = False
                st.session_state.answer_evaluated = False
                st.session_state.exercise_questions = []
                st.session_state.user_responses = []
                
                # Optionale Variablen löschen falls vorhanden
                if 'start_time' in st.session_state:
                    del st.session_state.start_time
                if 'training_level' in st.session_state:
                    del st.session_state.training_level
                    
                st.rerun()
        
        with col2:
            if st.button("📚 Theorie vertiefen", use_container_width=True):
                st.info("Studieren Sie die bereitgestellten Dokumente zur Vertiefung Ihrer Kenntnisse.")

# Am ENDE der Datei:
if __name__ == "__main__":
    quiz = QuizModule()
    quiz.display_quiz()
