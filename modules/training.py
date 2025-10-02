import streamlit as st
import plotly.graph_objects as go
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
    
    def show_dimension_details(self, dimension):
        """Zeigt detaillierte Informationen zu einer Dimension"""
        dim_info = self.dimensions[dimension]
        
        st.header(dim_info['name'])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Hohe Ausprägung")
            st.info(dim_info['high_desc'])
            
        with col2:
            st.subheader("Niedrige Ausprägung") 
            st.info(dim_info['low_desc'])
        
        st.subheader("Facetten (nach NEO-PI-R)")
        for facet in dim_info['facets']:
            st.write(f"• {facet}")
    
    def create_radar_chart(self, scores):
        """Erstellt ein Radar-Diagramm der Persönlichkeitswerte"""
        categories = [self.dimensions[dim]['name'] for dim in scores.keys()]
        values = list(scores.values())
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Persönlichkeitsprofil'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=False,
            title="Big Five Persönlichkeitsprofil"
        )
        
        return fig
    
    def show_hierarchical_structure(self):
        """Zeigt die hierarchische Struktur des Big-Five-Modells"""
        st.header("Hierarchische Struktur des Big-Five-Modells")
        
        st.subheader("Dimensionen → Aspekte → Facetten")
        
        aspects = {
            'O': ['Intellekt', 'Offenheit'],
            'C': ['Fleiß', 'Ordnung'],
            'E': ['Enthusiasmus', 'Durchsetzungsfähigkeit'],
            'A': ['Mitgefühl', 'Höflichkeit'],
            'N': ['Unbeständigkeit', 'Sensitivität']
        }
        
        for dim, aspect_pair in aspects.items():
            with st.expander(f"{self.dimensions[dim]['name']} ({dim})"):
                st.write(f"**Aspekte:** {aspect_pair[0]}, {aspect_pair[1]}")
                st.write(f"**Facetten:** {', '.join(self.dimensions[dim]['facets'])}")
    
    def show_genetic_information(self):
        """Zeigt Informationen zur Erblichkeit"""
        st.header("Genetische und Entwicklungsaspekte")
        
        heritability_data = {
            'Dimension': ['Offenheit', 'Gewissenhaftigkeit', 'Extraversion', 'Verträglichkeit', 'Neurotizismus'],
            'Erblichkeit (%)': [57, 49, 54, 42, 48]
        }
        
        fig = px.bar(
            heritability_data, 
            x='Dimension', 
            y='Erblichkeit (%)',
            title="Geschätzte Erblichkeit der Big-Five-Dimensionen",
            color='Erblichkeit (%)'
        )
        
        st.plotly_chart(fig)
        
        st.info("""
        **Wichtige Erkenntnisse:**
        - 40-60% der Persönlichkeitsunterschiede sind genetisch bedingt
        - Individuelle Umwelteinflüsse haben größeren Einfluss als geteilte Umwelt
        - Persönlichkeit entwickelt sich über die gesamte Lebensspanne
        """)
