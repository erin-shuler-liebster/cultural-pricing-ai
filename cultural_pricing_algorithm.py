
# ✅ FILE: cultural_pricing_algorithm.py
# This is the core logic file for the Cultural Pricing Translation Algorithm
# It translates Hofstede's cultural dimensions into pricing communication recommendations

from typing import Dict
import numpy as np

class CulturalPricingTranslator:
    def __init__(self, cultural_profiles: Dict[str, Dict[str, float]]):
        self.country_profiles = cultural_profiles
        self.thresholds = {
            'low': 0.33,
            'medium': 0.67,
            'high': 1.0
        }

    def categorize_score(self, score: float) -> str:
        if score <= self.thresholds['low']:
            return 'low'
        elif score <= self.thresholds['medium']:
            return 'medium'
        else:
            return 'high'

    def cultural_logic_trace(self, dimension: str, value: float) -> str:
        category = self.categorize_score(value)
        logic = {
            'power_distance': {
                'low': "Flat pricing; peer justification",
                'medium': "Balanced pricing tiers",
                'high': "Hierarchical tiers; expert justification"
            },
            'individualism': {
                'low': "Collective framing; standard offers",
                'medium': "Moderate personalization",
                'high': "Highly personalized; autonomy"
            },
            'uncertainty_avoidance': {
                'low': "Minimal info display",
                'medium': "Transparent, but flexible",
                'high': "Highly transparent with guarantees"
            },
            'masculinity': {
                'low': "Care/empathy driven",
                'medium': "Balanced emotion and results",
                'high': "Competitive, performance-driven"
            },
            'long_term_orientation': {
                'low': "Immediate gratification",
                'medium': "Blend short- and long-term value",
                'high': "Deferred rewards, future benefits"
            },
            'indulgence': {
                'low': "Rational tone",
                'medium': "Balanced emotional messaging",
                'high': "Impulse/personal joy messaging"
            }
        }
        return logic[dimension][category]

    def translate(self, country: str) -> Dict[str, str]:
        profile = self.country_profiles[country]
        recommendations = {}
        for dim, value in profile.items():
            recommendations[dim] = self.cultural_logic_trace(dim, value)
        return recommendations

    def explain_trace(self, country: str) -> Dict[str, str]:
        profile = self.country_profiles[country]
        trace = {}
        for dim, value in profile.items():
            cat = self.categorize_score(value)
            explanation = self.cultural_logic_trace(dim, value)
            trace[dim] = f"{dim.title()} ({cat}): {explanation}"
        return trace

    def compare(self, country1: str, country2: str) -> float:
        p1 = self.country_profiles[country1]
        p2 = self.country_profiles[country2]
        return np.sqrt(sum((p1[k] - p2[k])**2 for k in p1))
