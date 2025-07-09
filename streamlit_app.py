
import streamlit as st
from cultural_pricing_algorithm import CulturalPricingTranslator

# Sample cultural profiles
cultural_profiles = {
    'USA': {
        'power_distance': 0.40,
        'individualism': 0.91,
        'uncertainty_avoidance': 0.46,
        'masculinity': 0.62,
        'long_term_orientation': 0.26,
        'indulgence': 0.68
    },
    'Germany': {
        'power_distance': 0.35,
        'individualism': 0.67,
        'uncertainty_avoidance': 0.65,
        'masculinity': 0.66,
        'long_term_orientation': 0.83,
        'indulgence': 0.40
    },
    'France': {
        'power_distance': 0.68,
        'individualism': 0.71,
        'uncertainty_avoidance': 0.86,
        'masculinity': 0.43,
        'long_term_orientation': 0.63,
        'indulgence': 0.48
    }
}

translator = CulturalPricingTranslator(cultural_profiles)

st.title("🌍 Cultural Pricing Translation Tool")
st.markdown("Translate Hofstede's dimensions into pricing communication strategies.")

# Country selector
country = st.selectbox("Select a Country", list(cultural_profiles.keys()))

# Generate recommendations
if st.button("Generate Recommendations"):
    trace = translator.explain_trace(country)
    st.subheader(f"📋 Pricing Strategy for {country}")
    for dim, explanation in trace.items():
        st.markdown(f"**{dim.replace('_', ' ').title()}**: {explanation}")
