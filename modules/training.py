import streamlit as st
import plotly.express as px

class TrainingModule:
    def __init__(self):
        self.dimensions = {
            'O': {
                'name': 'Offenheit für Erfahrungen',
                'high_desc': 'Kreativ, neugierig, vielseitig interessiert, offen für neue Ideen',
                'low_desc': 'Praktisch, konventionell, bevorzugt Bewährtes, konservativ',
                'facets': ['Fantasiereichtum', 'Ästhetik', 'Gefühle', 'Handlungen', 'Ideen', 'Werte']
            },
            'C': {
                'name': 'Gewissenhaftigkeit', 
                'high_desc': 'Organisiert, zuverlässig, pflichtbewusst, zielstrebig',
                'low_desc': 'Spontan, flexibel, ungezwungen, nachlässig',
                'facets': ['Kompetenz', 'Ordnung', 'Pflichtbewusstsein', 'Leistungsstreben', 'Selbstdisziplin', 'Besonnenheit']
            },
            'E': {
                'name': 'Extraversion',
                'high_desc': 'Gesellig, energisch, gesprächig, durchsetzungsfähig',
                'low_desc': 'Zurückhaltend, ruhig, unabhängig, reserviert',
                'facets': ['Herzlichkeit', 'Geselligkeit', 'Durchsetzungsvermögen', 'Aktivität', 'Erlebnishunger', 'Frohsinn']
            },
            'A': {
                'name': 'Verträglichkeit',
                'high_desc': 'Mitfühlend, kooperativ, vertrauensvoll, hilfsbereit',
                'low_desc': 'Skeptisch, wettbewerbsorientiert, direkt, kritisch',
                'facets': ['Vertrauen', 'Freimütigkeit', 'Altruismus', 'Entgegenkommen', 'Bescheidenheit', 'Weichherzigkeit']
            },
            'N': {
                'name': 'Neurotizismus',
                'high_desc': 'Emotional, sensibel, besorgt, stressanfällig',
                'low_desc': 'Gelassen, emotional stabil, resilient, selbstsicher',
                'facets': ['Ängstlichkeit', 'Reizbarkeit', 'Depression', 'Soziale Befangenheit', 'Impulsivität', 'Verletzlichkeit']
            }
        }
    
    def show_model_overview(self):
        """Zeigt einen Überblick über das Big-Five-Modell"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">📖 Überblick - Grundlagen & Dimensionen</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Historische Entwicklung
        st.markdown("### Historische Entwicklung")
        st.markdown("""
        Die Big Five basieren auf dem sogenannten lexikalischen Ansatz. 
        Dieser geht davon aus, dass sich alle wichtigen Merkmale menschlicher Persönlichkeit in der Sprache niedergeschlagen haben.
        Bereits in den 1930er-Jahren identifizierten Allport und Odbert über 18'000 persönlichkeitsrelevante Begriffe. 
        Durch statistische Analysen (Faktorenanalysen) kristallisierten sich daraus die fünf stabilen Dimensionen heraus, die kulturübergreifend bestätigt wurden.
        """)
        
        st.markdown("""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 12px; margin: 20px 0;">
            <strong>Wichtige Meilensteine:</strong><br>
            • 1936: Allport & Odbert identifizieren 18.000 Persönlichkeitsbegriffe<br>
            • 1960er: Cattell reduziert auf 16 Faktoren<br>
            • 1980er: Fünf stabile Faktoren werden international bestätigt<br>
            • 1990er: NEO-PI-R etabliert standardisiertes Messinstrument
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Die fünf Dimensionen")
        
        dimensions_info = {
            'O': {
                'name': 'Offenheit für Erfahrungen',
                'description': 'Offene Menschen sind neugierig, kreativ, fantasievoll und interessieren sich für Kunst, Philosophie oder neue Ideen. Sie hinterfragen Konventionen, suchen Abwechslung und zeigen eine hohe intellektuelle Neugier. Wenig offene Menschen bevorzugen hingegen Stabilität, Routinen und Bekanntes. Hohe Offenheit steht in der modernen Arbeitswelt mit Innovationsfähigkeit, Lernbereitschaft und kognitiver Flexibilität in Verbindung',
                'high': 'Kreativ, neugierig, vielseitig',
                'low': 'Praktisch, konventionell, traditionell'
            },
            'C': {
                'name': 'Gewissenhaftigkeit', 
                'description': 'Dieser Faktor beschreibt Zielstrebigkeit, Organisation und Verantwortungsbewusstsein. Menschen mit hoher Gewissenhaftigkeit planen ihren Tag sorgfältig, handeln überlegt, dokumentieren gewissenhaft und verfolgen ihre Ziele diszipliniert. Forschungsergebnisse zeigen, dass Gewissenhaftigkeit der beste Prädiktor für beruflichen und akademischen Erfolg ist – über alle Branchen hinweg. Sie wirkt sich zudem positiv auf die Gesundheit und Lebenszufriedenheit aus',
                'high': 'Organisiert, verantwortungsbewusst, zuverlässig',
                'low': 'Spontan, flexibel, ungezwungen'
            },
            'E': {
                'name': 'Extraversion',
                'description': 'Extravertierte Personen sind gesellig, aktiv, kontaktfreudig und energiegeladen. Sie initiieren Gespräche, fühlen sich in Gruppen wohl und suchen den Austausch. Introvertierte Personen sind dagegen eher zurückhaltend, beobachtend und ruhig, was jedoch keineswegs mit Schüchternheit gleichzusetzen ist. Je nach Situation können beide Ausprägungen Vorteile bieten.',
                'high': 'Gesellig, energisch, gesprächig',
                'low': 'Zurückhaltend, ruhig, reserviert'
            },
            'A': {
                'name': 'Verträglichkeit',
                'description': 'Verträgliche Menschen sind hilfsbereit, mitfühlend und kooperativ. Sie vermeiden Konflikte, zeigen Altruismus und handeln rücksichtsvoll. Eine geringe Verträglichkeit hingegen steht für Durchsetzungsfähigkeit und Wettbewerbsorientierung – Eigenschaften, die in hierarchischen oder leistungsorientierten Umfeldern vorteilhaft sein können. Studien zeigen jedoch, dass übermässige Freundlichkeit zu einer „Karrierebremse" werden kann: Sie erhöht zwar die Zufriedenheit, kann aber den objektiven Erfolg (z. B. Einkommen oder Beförderung) mindern',
                'high': 'Hilfsbereit, vertrauensvoll, mitfühlend',
                'low': 'Skeptisch, wettbewerbsorientiert, direkt'
            },
            'N': {
                'name': 'Neurotizismus',
                'description': 'Diese Dimension beschreibt die Anfälligkeit für negative Emotionen wie Angst, Nervosität oder Unsicherheit. Ein hoher Neurotizismus geht oft mit emotionaler Labilität und Stressanfälligkeit einher, während ein niedriger Wert auf emotionale Stabilität und Resilienz hinweist. Wichtig ist: Neurotizismus ist veränderbar. Achtsamkeitstraining, Emotionsregulation oder das Training emotionaler Kompetenzen können helfen, den Umgang mit Stress zu verbessern und innere Stabilität zu fördern. Gleichzeitig hat diese Sensibilität auch positive Seiten: Menschen mit höherem Neurotizismus nehmen Stimmungen, Spannungen und Risiken frühzeitig wahr und reflektieren ihr eigenes Verhalten oft besonders gründlich. Ihre emotionale Tiefe kann zu hoher Empathie, Verantwortlichkeit und kreativer Ausdruckskraft führen – vorausgesetzt, sie lernen, mit ihrer inneren Intensität bewusst umzugehen.',
                'high': 'Emotional, sensibel, besorgt',
                'low': 'Gelassen, emotional stabil, resilient'
            }
        }
        
        for dim, info in dimensions_info.items():
            with st.expander(f"{info['name']} ({dim})"):
                st.write(f"**Beschreibung:** {info['description']}")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%); 
                                padding: 15px; border-radius: 10px; border-left: 4px solid #27ae60;">
                        <strong>Hohe Ausprägung:</strong><br>{info['high']}
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); 
                                padding: 15px; border-radius: 10px; border-left: 4px solid #3498db;">
                        <strong>Niedrige Ausprägung:</strong><br>{info['low']}
                    </div>
                    """, unsafe_allow_html=True)

    def show_nature_nurture(self):
        """Anlage, Umwelt und Veränderbarkeit"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">🧬 Wissenschaft - Genetik & Veränderbarkeit</h2>
            
            <p>Persönlichkeitsmerkmale sind teils genetisch, teils umweltbedingt.</p>
            
            <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>🔬 Wissenschaftliche Evidenz:</strong><br>
                • Zwillingsstudien zeigen, dass die Big-Five-Dimensionen zu etwa <strong>40–60 % erblich</strong> sind<br>
                • Den restlichen Anteil erklären <strong>individuelle Umwelteinflüsse</strong> – also persönliche Erfahrungen, Bildung, Freundschaften oder Lebensereignisse
            </div>
            
            <h3 style="color: #34495e;">Neuroplastizität und Veränderbarkeit</h3>
            <p>Lange galt Persönlichkeit als weitgehend stabil, doch moderne Forschung zur Neuroplastizität zeigt:</p>
            <p><strong>Unser Gehirn bleibt formbar.</strong> Neue Gewohnheiten, Denkmuster und Verhaltensweisen lassen sich durch intentionale Aktivitäten gezielt trainieren.</p>
            
            <div style="background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>💪 Praktische Konsequenz:</strong><br>
                Sie haben etwa <strong>40-50% Ihrer Persönlichkeit aktiv in der Hand</strong> und können diese durch bewusstes Training und neue Erfahrungen formen.
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_structure_measurement(self):
        """Aufbau und Messung"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">🧩 Methodik - Aufbau & Messung</h2>
            
            <h3 style="color: #34495e;">Hierarchische Struktur</h3>
            <p>Das Big-Five-Modell ist hierarchisch aufgebaut:</p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 20px 0;">
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;">
                    <strong>5 Hauptdimensionen</strong><br>OCEAN
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;">
                    <strong>2 Aspekte pro Dimension</strong><br>z.B. Enthusiasmus & Geselligkeit
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; text-align: center;">
                    <strong>6 Facetten pro Dimension</strong><br>Spezifische Subskalen
                </div>
            </div>
            
            <h3 style="color: #34495e;">Wissenschaftliche Messung</h3>
            <p>Zur wissenschaftlichen Erfassung gilt das <strong>NEO-PI-R (Costa & McCrae)</strong> als Goldstandard.</p>
            <p>Es misst jede der fünf Dimensionen anhand von <strong>30 Facetten</strong> und erlaubt damit eine sehr präzise Beschreibung der Persönlichkeit.</p>
            
            <div style="background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>📊 Total Items:</strong> 240 Fragen (6 Facetten × 8 Items × 5 Dimensionen)<br>
                <strong>🎯 Genauigkeit:</strong> Hochdetaillierte Persönlichkeitsprofile
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_application_science(self):
        """Anwendung und wissenschaftliche Grundlagen"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">🎓 Anwendung - Beruf & Forschung</h2>
            
            <h3 style="color: #34495e;">Eignungsdiagnostik</h3>
            <p>In der Eignungsdiagnostik ist die Persönlichkeit neben Intelligenz einer der wichtigsten Prädiktoren für Berufserfolg.</p>
            
            <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>📈 Validitätsbefunde:</strong><br>
                • Persönlichkeitstests zeigen eine <strong>moderate Validität (r ≈ 0.3)</strong>, insbesondere Gewissenhaftigkeit<br>
                • Die Kombination mit kognitiven Tests erhöht die Vorhersagekraft um etwa <strong>18 %</strong> – dieser Effekt wird <strong>inkrementelle Validität</strong> genannt
            </div>
            
            <h3 style="color: #34495e;">Wichtige Konzepte</h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px;">
                    <strong>📏 Bandbreiten-Fidelitäts-Dilemma</strong><br>
                    Je breiter ein Test konstruiert ist, desto weniger präzise ist er – und umgekehrt. Die Kunst wissenschaftlicher Diagnostik besteht also darin, zwischen Breite (Bandbreite) und Genauigkeit (Fidelität) das richtige Gleichgewicht zu finden.
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px;">
                    <strong>🎯 Kriteriumsvalidität</strong><br>
                    Beschreibt den Zusammenhang zwischen Testergebnissen und externen Erfolgskriterien – etwa Arbeitsleistung oder Zufriedenheit.
                </div>
            </div>
            
            <h3 style="color: #34495e;">Praktische Anwendungen</h3>
            
            <div style="background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>💼 Berufliche Anwendungsbereiche:</strong><br>
                • Personalauswahl und Recruiting<br>
                • Teamentwicklung und Teamzusammensetzung<br>
                • Karriereberatung und Laufbahnplanung<br>
                • Führungskräfteentwicklung und Coaching
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_limitations_critique(self):
        """Grenzen und Kritik"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">⚖️ Reflexion - Kritik & Grenzen</h2>
            
            <h3 style="color: #34495e;">Inhaltliche Kritik</h3>
            <p>Der Persönlichkeitspsychologe <strong>Dan McAdams</strong> kritisiert, dass die Big Five zwar beschreiben, <em>wie</em> Menschen sind, aber nicht <em>warum</em>.</p>
            <p>Das Modell vernachlässige die Rolle von Lebenserfahrungen und situativen Einflüssen.</p>
            
            <h3 style="color: #34495e;">Methodische Probleme</h3>
            
            <div style="background: linear-gradient(135deg, #fde8e8 0%, #f9d6d6 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>⚠️ Bekannte methodische Herausforderungen:</strong><br>
                • <strong>Soziale Erwünschtheit</strong> kann Antworten verzerren<br>
                • <strong>Kulturelle Unterschiede</strong> beeinflussen Item-Interpretationen<br>
                • <strong>Selbstauskünfte</strong> spiegeln nicht immer objektive Realität wider
            </div>
            
            <div style="background: linear-gradient(135deg, #e8f6ef 0%, #d4f0e4 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>✅ Trotzdem wissenschaftlich wertvoll:</strong><br>
                Dennoch bleibt das Modell das <strong>verlässlichste Fundament</strong> moderner Persönlichkeitsforschung, da es komplexe menschliche Unterschiede einfach, reproduzierbar und interkulturell erfassbar macht.
            </div>
        </div>
        """, unsafe_allow_html=True)

    def show_conclusion(self):
        """Fazit"""
        st.markdown("""
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            <h2 style="color: #2c3e50; margin-top: 0;">💡 Fazit - Zusammenfassung & Umsetzung</h2>
            
            <p>Die Big Five bieten ein <strong>wissenschaftlich fundiertes Raster</strong>, um Persönlichkeit zu verstehen und Verhalten besser zu interpretieren.</p>
            
            <div style="background: linear-gradient(135deg, #e8f4fd 0%, #d4e7f8 100%); padding: 20px; border-radius: 12px; margin: 20px 0;">
                <strong>🎯 Zentrale Erkenntnisse:</strong><br>
                • Unsere Persönlichkeit ist <strong>teils veranlagt, teils formbar</strong><br>
                • <strong>Bewusste Gewohnheiten, Reflexion und Training</strong> haben einen erheblichen Einfluss auf Erfolg und Wohlbefinden<br>
                • Wer die Dynamik zwischen Anlage, Umwelt und bewusster Veränderung versteht, kann seine persönliche Entwicklung gezielt gestalten
            </div>
            
            <h3 style="color: #34495e;">Praktische Umsetzung</h3>
            <p><strong>Wie gehen wir das am besten an?</strong></p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px;">
                    <strong>🔍 Selbstreflexion</strong><br>
                    Nutzen Sie Ihre Big-Five-Ergebnisse als Ausgangspunkt für bewusste Selbstwahrnehmung und persönliche Entwicklung.
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px;">
                    <strong>🚀 Gezieltes Training</strong><br>
                    Arbeiten Sie mit den Empfehlungen dieser App an spezifischen Entwicklungsbereichen.
                </div>
            </div>
            
            <div style="background: linear-gradient(135deg, #fff9e6 0%, #fff2cc 100%); padding: 20px; border-radius: 12px; margin: 20px 0; text-align: center;">
                <strong>Ihre Persönlichkeit ist kein Schicksal – sondern eine dynamische Ressource, die Sie aktiv gestalten können.</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
