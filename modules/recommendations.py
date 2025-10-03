import streamlit as st
import json

class RecommendationEngine:
    def __init__(self):
        self.recommendations = self.load_evidence_based_recommendations()
        self.scientific_evidence = self.load_scientific_evidence()
    
    def load_evidence_based_recommendations(self):
        """Lädt evidenzbasierte Handlungsempfehlungen basierend auf den Papers"""
        return {
            "O": {
                "high": {
                    "stärken": [
                        "Innovativ & visionär: Entwickelt originelle Ideen für komplexe Probleme",
                        "Vielseitig interessiert: Schnelle Aneignung neuer Themen",
                        "Anpassungsfähig: Offen für Veränderungen und neue Gegebenheiten",
                        "Fantasievoll & kreativ: Reiche Vorstellungskraft für kreative Prozesse"
                    ],
                    "risiken": [
                        "Schwierigkeiten beim Abschluss: Breites Interesse kann Projektfertigstellung behindern",
                        "Wird als chaotisch wahrgenommen: Unkonventionelle Arbeitsweise wirkt unstrukturiert",
                        "Festlegungsprobleme: Faszination für Vieles erschwert Karriereentscheidungen"
                    ],
                    "entwicklung": [
                        "🎯 **Kreativität kanalisieren**: Nutzen Sie 'Ideen-Parking' - Liste für neue Einfälle, während Sie priorisierte Projekte abschließen",
                        "🔄 **Interessen kombinieren**: Suchen Sie Nischen, die vielseitige Interessen verbinden (z.B. Technologie-Journalismus)",
                        "⏰ **Projekte finalisieren**: Setzen Sie Meilensteine und Deadlines für erfolgreiche Abschlüsse",
                        "🧠 **Wissenschaftlicher Hinweis**: Nutzen Sie Ihre Neuroplastizität - wiederholtes Üben von Fokussierung stärkt entsprechende neuronale Bahnen"
                    ],
                    "berufe": [
                        "Kreative Berufe (Design, Forschung, Kunst)",
                        "Innovationsmanagement",
                        "Strategische Planung",
                        "Content Creation"
                    ]
                },
                "low": {
                    "stärken": [
                        "Pragmatisch & bodenständig: Fokussiert auf bewährte, praktische Lösungen",
                        "Fokussiert & beständig: Verfolgt Ziele konsequent ohne Ablenkung",
                        "Sachlich & konventionell: Bietet Stabilität und Verlässlichkeit",
                        "Effizient in Routinen: Optimiert bekannte Prozesse für hohe Qualität"
                    ],
                    "risiken": [
                        "Unflexibel in Denkmustern: Hält an bekannten Methoden fest, auch wenn neue besser wären",
                        "Schwierigkeiten bei Veränderungen: Langsame Anpassung an neuartige Situationen",
                        "Geringere Risikobereitschaft: Kann Innovationen hemmen"
                    ],
                    "entwicklung": [
                        "🌱 **Neues in kleinen Dosen**: Integrieren Sie schrittweise kleine Veränderungen (neues Tool, fachfremder Artikel)",
                        "💪 **Beständigkeit als Stärke nutzen**: Positionieren Sie sich als Experte für Prozessoptimierung",
                        "🔍 **Vorteile von Veränderungen suchen**: Konzentrieren Sie sich auf praktische Vorteile neuer Ansätze",
                        "📚 **Wissenschaftlicher Hinweis**: Das 50/50-Prinzip zeigt - 50% Ihrer Persönlichkeit sind durch intentionale Aktivitäten formbar"
                    ],
                    "berufe": [
                        "Prozessoptimierung",
                        "Qualitätssicherung", 
                        "Administrative Führung",
                        "Operationelles Management"
                    ]
                }
            },
            "C": {
                "high": {
                    "stärken": [
                        "Organisiert & zielstrebig: Plant vorausschauend und erreicht Ziele zuverlässig",
                        "Zuverlässig & pflichtbewusst: Hält Vorgaben und Fristen ein",
                        "Diszipliniert & ehrgeizig: Hohe Selbstkontrolle für unangenehme Aufgaben",
                        "Effektiv & fokussiert: Arbeitet konzentriert ohne Ablenkung"
                    ],
                    "risiken": [
                        "Neigung zu Perfektionismus: Verliert sich in Details (Schwarz-Weiss-Denken)",
                        "Unflexibel: Langsame Reaktion auf unerwartete Änderungen",
                        "Wird als pedantisch wahrgenommen: Hohe Ansprüche wirken kontrollierend"
                    ],
                    "entwicklung": [
                        "📊 **80/20-Regel anwenden**: Oft werden 80% des Ergebnisses mit 20% Aufwand erreicht",
                        "🔄 **Flexibilität einplanen**: Bauen Sie Pufferzeiten und alternative Szenarien ein",
                        "🤝 **Delegieren und vertrauen**: Akzeptieren Sie, dass andere Aufgaben anders erledigen",
                        "⭐ **Wissenschaftlicher Hinweis**: Gewissenhaftigkeit ist der stärkste Prädiktor für beruflichen Erfolg (r=0.23) - nutzen Sie diese Superkraft!"
                    ],
                    "berufe": [
                        "Projektmanagement",
                        "Buchhaltung & Finanzen",
                        "Qualitätsmanagement", 
                        "Strategische Planung"
                    ]
                },
                "low": {
                    "stärken": [
                        "Spontan & flexibel: Schnelle Anpassung an neue Situationen",
                        "Entspannt & sorgenfrei: Gelassenheit auch unter Druck",
                        "Kreativ bei Problemlösung: Unkonventionelle Wege durch Improvisation",
                        "Anpassungsfähig: Guter Umgang mit Ambiguität und Unklarheiten"
                    ],
                    "risiken": [
                        "Neigt zu Prokrastination: Schiebt unangenehme Aufgaben auf",
                        "Unzuverlässig: Fristen und Zusagen werden möglicherweise nicht eingehalten",
                        "Leicht ablenkbar: Beginnt viele Dinge ohne Abschluss"
                    ],
                    "entwicklung": [
                        "📅 **Tägliche 3-Punkte-Planung**: Nehmen Sie sich 5 Minuten für die wichtigsten Aufgaben des nächsten Tages",
                        "🔨 **Aufgaben zerlegen**: Brechen Sie große Aufgaben in kleine, machbare Schritte",
                        "🎯 **Spontaneität als Stärke nutzen**: Suchen Sie Umfelder, die Flexibilität schätzen",
                        "🧠 **Wissenschaftlicher Hinweis**: Selbstregulation ist trainierbar - beginnen Sie mit kleinen, konsistenten Gewohnheiten"
                    ],
                    "berufe": [
                        "Kreative Berufe",
                        "Journalismus",
                        "Improvisations-intensive Rollen",
                        "Start-Up Umgebungen"
                    ]
                }
            },
            "E": {
                "high": {
                    "stärken": [
                        "Herzlich & gesellig: Knüpft leicht Kontakte, wird als offen wahrgenommen",
                        "Energetisch & fröhlich: Wirkt motivierend, strahlt positive Energie aus", 
                        "Gesprächig: Gute Kommunikation komplexer Sachverhalte",
                        "Empfänglich für positive Emotionen: Findet leicht Freude und Begeisterung"
                    ],
                    "risiken": [
                        "Dominant: Kann Gespräche dominieren und andere übergehen",
                        "Hohe Risikobereitschaft: Sucht belohnende Situationen, oft risikofreudiger",
                        "Geringere Reflexionstiefe: Vorschnelles Handeln ohne Durchdachtheit"
                    ],
                    "entwicklung": [
                        "👂 **Aktiv zuhören**: Nehmen Sie sich in Gruppen bewusst zurück, fragen Sie gezielt ruhigere Kollegen",
                        "🧘 **Ruhephasen einplanen**: Blocken Sie 'Deep Work'-Zeiten ohne Benachrichtigungen",
                        "⚖️ **Risiken reflektieren**: Wägen Sie vor Entscheidungen bewusst Nachteile ab",
                        "🔬 **Wissenschaftlicher Hinweis**: Extraversion korreliert mit Führungspositionen - nutzen Sie Ihre soziale Energie strategisch"
                    ],
                    "berufe": [
                        "Vertrieb & Verkauf",
                        "Unternehmensführung",
                        "Personalwesen",
                        "Öffentlichkeitsarbeit"
                    ]
                },
                "low": {
                    "stärken": [
                        "Selbst-reflektierend: Tiefgründige Gedanken und fundierte Entscheidungen",
                        "Ruhig & ausgeglichen: Bewahrt in hektischen Situationen kühlen Kopf", 
                        "Guter Zuhörer: Konzentration auf Einzelgespräche, Verständnis für Perspektiven",
                        "Unabhängig: Gute Einzelarbeit ohne externe Bestätigung"
                    ],
                    "risiken": [
                        "Wirkt reserviert: Kann als unnahbar oder desinteressiert wahrgenommen werden",
                        "Soziale Interaktionen kräftezehrend: Intensive Kontakte führen zu Erschöpfung",
                        "Weniger sichtbar: Eigene Beiträge werden in großen Runden seltener gehört"
                    ],
                    "entwicklung": [
                        "💡 **Stärken gezielt einsetzen**: Nutzen Sie konzentrierte Einzelarbeit für komplexe Aufgaben",
                        "🎯 **Soziale Anlässe strategisch gestalten**: Bereiten Sie 1-2 Kernpunkte für Meetings vor",
                        "🤝 **Qualität vor Quantität**: Bauen Sie wenige, aber tiefgehende berufliche Beziehungen auf",
                        "🧠 **Wissenschaftlicher Hinweis**: Introversion ist keine Schwäche - viele innovative Führungskräfte sind introvertiert"
                    ],
                    "berufe": [
                        "Forschung & Entwicklung",
                        "IT & Programmierung",
                        "Analytische Rollen",
                        "Fachspezialisten"
                    ]
                }
            },
            "A": {
                "high": {
                    "stärken": [
                        "Einfühlsam & mitfühlend: Nimmt Emotionen anderer stark wahr",
                        "Hilfsbereit & kooperativ: Fördert positives Arbeitsklima",
                        "Vertrauensvoll & gutmütig: Schafft Basis für vertrauensvolle Beziehungen",
                        "Bescheiden & nachgiebig: Stellt eigene Interessen für gemeinsame Ziele zurück"
                    ],
                    "risiken": [
                        "Schwierigkeiten beim 'Nein'-Sagen: Vernachlässigung eigener Bedürfnisse",
                        "Gefahr der Ausnutzung: Nachgiebigkeit wird als Schwäche interpretiert",
                        "Vermeidung notwendiger Konflikte: Wichtige Probleme werden nicht angesprochen"
                    ],
                    "entwicklung": [
                        "🚫 **Lernen, 'Nein' zu sagen**: Üben Sie freundliche, aber bestimmte Absagen",
                        "🎯 **Eigene Bedürfnisse formulieren**: Bringen Sie vor Meetings Ihre Ziele aktiv ein",
                        "⚡ **Konflikte als Chance sehen**: Meinungsverschiedenheiten führen zu besseren Lösungen",
                        "⚠️ **Wissenschaftlicher Hinweis**: Hohe Verträglichkeit korreliert mit höherer Zufriedenheit aber potenziell geringerem Einkommen - entwickeln Sie Verhandlungsfähigkeiten!"
                    ],
                    "berufe": [
                        "Sozialarbeit & Pflege",
                        "Teamkoordination",
                        "Kundenbetreuung",
                        "Mentoring & Coaching"
                    ]
                },
                "low": {
                    "stärken": [
                        "Durchsetzungsstark: Klare Kommunikation eigener Vorstellungen",
                        "Kritisch & analytisch: Hinterfragt Status quo, deckt Schwachstellen auf",
                        "Eigenständig & rational: Entscheidungen basierend auf eigenen Überlegungen",
                        "Wettbewerbsorientiert: Motivation, besser als andere zu sein"
                    ],
                    "risiken": [
                        "Wird als kühl empfunden: Rationales Verhalten belastet Beziehungen",
                        "Eher Einzelkämpfer: Erschwert Teamzusammenarbeit",
                        "Misstrauisch: Untergräbt vertrauensvolle Atmosphäre"
                    ],
                    "entwicklung": [
                        "💬 **Kritik konstruktiv formulieren**: Nutzen Sie 'Ich-Botschaften' und sachliches Feedback",
                        "👀 **Perspektiven wechseln**: Betrachten Sie Situationen aus Sicht anderer vor Konfrontationen",
                        "🤝 **Beziehungen aktiv pflegen**: Investieren Sie Zeit in persönliche Gespräche ohne eigenes Ziel",
                        "🔬 **Wissenschaftlicher Hinweis**: Ihre Durchsetzungsfähigkeit ist in Verhandlungen wertvoll - kanalisieren Sie sie konstruktiv"
                    ],
                    "berufe": [
                        "Recht & Verhandlungen",
                        "Unternehmensberatung",
                        "Strategische Entwicklung",
                        "Wettbewerbsintensive Branchen"
                    ]
                }
            },
            "N": {
                "high": {
                    "stärken": [
                        "Frühwarnsystem: Sensitivität für potenzielle Probleme erkennt Risiken früh",
                        "Hohe Empathie: Gutes Verständnis für Sorgen und Ängste anderer",
                        "Gewissenhafte Vorbereitung: Sorgfältige Aufgabenvorbereitung aus Angst vor Fehlern",
                        "Sensitivität für Stimmungen: Nimmt atmosphärische Spannungen schnell wahr"
                    ],
                    "risiken": [
                        "Hohe Stressanfälligkeit: Starke Reaktion auf Belastungen",
                        "Neigung zu Pessimismus: Fokus auf was schiefgehen könnte",
                        "Emotionale Instabilität: Stimmungsschwankungen und Reizbarkeit"
                    ],
                    "entwicklung": [
                        "🌬️ **Stressregulationstechniken**: Praktizieren Sie Achtsamkeit, Meditation oder Atemübungen (4s ein, 6s aus)",
                        "📝 **Sorgen produktiv nutzen**: Wandeln Sie diffuse Sorgen in konkrete 'Wenn-Dann'-Pläne um",
                        "🔍 **Realitätscheck durchführen**: Holen Sie Perspektiven gelassener Personen ein",
                        "🧠 **Wissenschaftlicher Hinweis**: Neurotizismus ist trainierbar! Achtsamkeitsbasierte Stressreduktion (MBSR) zeigt Effektstärken von d=0.97"
                    ],
                    "berufe": [
                        "Qualitätssicherung",
                        "Risikomanagement",
                        "Detaillierte Analysetätigkeiten",
                        "Umgebungen mit klaren Strukturen"
                    ]
                },
                "low": {
                    "stärken": [
                        "Ruhig in Krisen: Gelassenheit und Handlungsfähigkeit unter Druck",
                        "Emotional stabil & ausgeglichen: Schnelle Erholung von Rückschlägen",
                        "Optimistisch & unbeschwert: Positive Grundhaltung ohne Lähmung durch Sorgen",
                        "Belastbar & resilient: Bewältigung hoher Arbeitslasten"
                    ],
                    "risiken": [
                        "Unterschätzt Risiken: Übersieht potenzielle Gefahren durch Gelassenheit",
                        "Geringe Sensibilität: Nimmt emotionale Reaktionen anderer als übertrieben wahr",
                        "Ignoriert Warnsignale: Übersieht subtile Problemzeichen"
                    ],
                    "entwicklung": [
                        "👂 **Sensibilität schärfen**: Hören Sie aktiv zu, wenn Kollegen Sorgen äußern",
                        "🛡️ **Stabilität als Ressource nutzen**: Bieten Sie in Stressphasen als Anker für das Team",
                        "🔎 **Bewusste Risiko-Analyse**: Führen Sie systematische Schwachstellenanalysen durch",
                        "⭐ **Wissenschaftlicher Hinweis**: Ihre emotionale Stabilität ist eine wertvolle Ressource - teilen Sie diese Gelassenheit mit dem Team"
                    ],
                    "berufe": [
                        "Notfallmanagement",
                        "Krisenintervention",
                        "Führung in Hochdruckumgebungen",
                        "Börsenhandel & Trading"
                    ]
                }
            }
        }
    
    def load_scientific_evidence(self):
        """Lädt wissenschaftliche Evidenz und Studienreferenzen"""
        return {
            "general_principles": {
                "50_50_principle": "50% genetische Komponente, 50% durch intentionale Aktivitäten formbar",
                "neuroplasticity": "Gehirn ist bis ins hohe Alter formbar - 'Use it or lose it'",
                "trainability": "Persönlichkeitsmerkmale sind durch systematisches Training veränderbar"
            },
            "intervention_studies": {
                "mindfulness": {
                    "name": "Achtsamkeitsbasierte Stressreduktion (MBSR)",
                    "effect": "d=0.97 für Stressreduktion",
                    "study": "Hofmann et al. (2010)"
                },
                "cognitive_restructuring": {
                    "name": "Kognitive Umstrukturierung", 
                    "effect": "Signifikante Reduktion von Ängstlichkeit",
                    "study": "Butler et al. (2006)"
                }
            }
        }
    
    def generate_recommendations(self, profile, scores):
        """Generiert evidenzbasierte personalisierte Handlungsempfehlungen"""
        st.header("🧠 Evidenzbasiertes Personalisiertes Feedback")
        
        # Wissenschaftliche Einleitung
        st.info("""
        **Wissenschaftliche Grundlage**: Ihre Persönlichkeit ist zu ~50% genetisch und zu ~50% durch intentionale Aktivitäten formbar. 
        Die folgenden Empfehlungen basieren auf Forschung zu den Big Five Persönlichkeitsdimensionen.
        """)
        
        # Detaillierte Empfehlungen für jede Dimension
        for dim, level in profile.items():
            dim_name = self.get_dimension_name(dim)
            
            with st.expander(f"📊 {dim_name} - {level.capitalize()} Ausprägung", expanded=True):
                if level in self.recommendations[dim]:
                    data = self.recommendations[dim][level]
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("✅ Ihre Stärken")
                        for strength in data["stärken"]:
                            st.success(f"• {strength}")
                        
                        st.subheader("🎯 Entwicklungsempfehlungen")
                        for empfehlung in data["entwicklung"]:
                            # Hervorhebung von wissenschaftlichen Hinweisen
                            if "Wissenschaftlicher Hinweis" in empfehlung:
                                st.info(empfehlung)
                            else:
                                st.write(f"• {empfehlung}")
                    
                    with col2:
                        st.subheader("⚠️ Mögliche Risiken")
                        for risiko in data["risiken"]:
                            st.warning(f"• {risiko}")
                        
                        st.subheader("💼 Passende Berufsfelder")
                        for beruf in data["berufe"]:
                            st.write(f"• {beruf}")
        
        # Berufliche Gesamtempfehlungen
        self.show_evidence_based_career_recommendations(profile, scores)
        
        # Wissenschaftliches Fazit
        st.subheader("🧪 Wissenschaftliches Fazit")
        st.markdown("""
        - **Neuroplastizität**: Ihr Gehirn kann sich durch gezieltes Training verändern
        - **50/50-Prinzip**: Fast die Hälfte Ihrer Persönlichkeit ist formbar  
        - **Evidenzbasierte Interventionen**: Methoden wie Achtsamkeit zeigen messbare Effekte
        - **Berufliche Passung**: Persönlichkeitsmerkmale prädizieren Berufserfolg
        """)
    
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
    
    def show_evidence_based_career_recommendations(self, profile, scores):
        """Zeigt evidenzbasierte berufliche Passungsempfehlungen"""
        st.subheader("🎯 Berufliche Passungsanalyse mit Wissenschaftlicher Evidenz")
        
        career_analysis = []
        
        # Evidenzbasierte Berufsempfehlungen
        for dim, level in profile.items():
            if level in ["hoch", "niedrig"]:  # Nur bei ausgeprägten Werten
                dim_data = self.recommendations[dim][level]
                
                career_analysis.append({
                    "dimension": self.get_dimension_name(dim),
                    "ausprägung": level,
                    "berufe": dim_data["berufe"],
                    "wissenschaftliche_notiz": self.get_scientific_note(dim, level)
                })
        
        # Darstellung der Berufsempfehlungen
        for analysis in career_analysis:
            with st.expander(f"💼 {analysis['dimension']} ({analysis['ausprägung']})"):
                st.write("**Passende Berufsfelder:**")
                for beruf in analysis["berufe"]:
                    st.info(f"• {beruf}")
                
                if analysis["wissenschaftliche_notiz"]:
                    st.warning(f"**Wissenschaftlicher Hinweis:** {analysis['wissenschaftliche_notiz']}")
        
        # Besondere Hinweise basierend auf Forschung
        st.subheader("⚠️ Forschungsbasierte Karrierehinweise")
        
        if profile.get('A') == 'hoch':
            st.warning("""
            **Verträglichkeits-Paradoxon**: Forschung zeigt, dass hohe Verträglichkeit mit höherer Arbeitszufriedenheit 
            aber potenziell geringerem Einkommen korreliert. Entwickeln Sie gezielt Verhandlungsfähigkeiten!
            """)
        
        if profile.get('C') == 'hoch':
            st.success("""
            **Gewissenhaftigkeit als Superkraft**: Ihre Ausprägung ist der stärkste Prädiktor für beruflichen Erfolg 
            (r=0.23). Nutzen Sie diese Stärke in strukturierten Umgebungen!
            """)
        
        if profile.get('N') == 'hoch':
            st.info("""
            **Neurotizismus ist trainierbar**: Evidenzbasierte Methoden wie Achtsamkeitstraining (MBSR) zeigen 
            Effektstärken von d=0.97. Systematisches Training kann emotionale Stabilität signifikant verbessern.
            """)
    
    def get_scientific_note(self, dimension, level):
        """Gibt wissenschaftliche Hinweise für bestimmte Dimensionen zurück"""
        notes = {
            'C': {
                'hoch': 'Gewissenhaftigkeit korreliert mit beruflichem Erfolg (r=0.23) und Gesundheit',
                'niedrig': 'Selbstregulation ist trainierbar - beginnen Sie mit kleinen Gewohnheiten'
            },
            'A': {
                'hoch': 'Hohe Verträglichkeit korreliert mit Zufriedenheit, aber potenziell geringerem Einkommen',
                'niedrig': 'Durchsetzungsfähigkeit ist in Verhandlungen vorteilhaft'
            },
            'N': {
                'hoch': 'Emotionsregulation ist trainierbar (Achtsamkeit: d=0.97)',
                'niedrig': 'Emotionale Stabilität ist eine wertvolle Ressource in Krisensituationen'
            }
        }
        
        return notes.get(dimension, {}).get(level, "")
