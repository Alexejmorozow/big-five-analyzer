def show_training(self):
    """Training-Seite - OPTIMIERT & REDUZIERT"""
    if st.button("← Zurück zur Übersicht"):
        st.session_state.current_page = "overview"
        st.rerun()
        
    st.header("Big Five Training")
    
    training_topic = st.selectbox(
        "Wählen Sie ein Thema:",
        [
            "📖 Überblick - Grundlagen & Dimensionen",
            "🧬 Wissenschaft - Genetik & Veränderbarkeit",
            "🧩 Methodik - Aufbau & Messung", 
            "🎓 Anwendung - Beruf & Forschung",
            "⚖️ Reflexion - Kritik & Grenzen",
            "💡 Fazit - Zusammenfassung & Umsetzung"
        ]
    )
    
    if training_topic == "📖 Überblick - Grundlagen & Dimensionen":
        self.training.show_model_overview()  # Aufruf der TrainingModule Methode
    elif training_topic == "🧬 Wissenschaft - Genetik & Veränderbarkeit":
        self.training.show_nature_nurture()  # Aufruf der TrainingModule Methode
    elif training_topic == "🧩 Methodik - Aufbau & Messung":
        self.training.show_structure_measurement()  # Aufruf der TrainingModule Methode
    elif training_topic == "🎓 Anwendung - Beruf & Forschung":
        self.training.show_application_science()  # Aufruf der TrainingModule Methode
    elif training_topic == "⚖️ Reflexion - Kritik & Grenzen":
        self.training.show_limitations_critique()  # Aufruf der TrainingModule Methode
    elif training_topic == "💡 Fazit - Zusammenfassung & Umsetzung":
        self.training.show_conclusion()  # Aufruf der TrainingModule Methode
