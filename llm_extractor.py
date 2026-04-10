# llm_extractor.py

import openai

# ✅ IMPORTS (correct)
from facility_and_ngo_fields import ORGANIZATION_INFORMATION_SYSTEM_PROMPT
from free_form import FREE_FORM_SYSTEM_PROMPT
from medical_specialties import MEDICAL_SPECIALTIES_SYSTEM_PROMPT
from organization_extraction import ORGANIZATION_EXTRACTION_SYSTEM_PROMPT


# 🔹 Helper function (avoid repetition)
def call_llm(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",   # ✅ safe model
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        return f"Error: {str(e)}"


# 🔹 1. Extract organization names
def extract_organizations(text):
    prompt = ORGANIZATION_EXTRACTION_SYSTEM_PROMPT + "\n\nTEXT:\n" + text
    return call_llm(prompt)


# 🔹 2. Extract basic facility info
def extract_basic_info(text, org):
    prompt = ORGANIZATION_INFORMATION_SYSTEM_PROMPT.format(
        organization=org
    ) + "\n\nTEXT:\n" + text
    return call_llm(prompt)


# 🔹 3. Extract procedure/equipment/capability
def extract_free_form(text, org):
    prompt = FREE_FORM_SYSTEM_PROMPT.format(
        organization=org
    ) + "\n\nTEXT:\n" + text
    return call_llm(prompt)


# 🔹 4. Extract medical specialties
def extract_specialties(text, org):
    prompt = MEDICAL_SPECIALTIES_SYSTEM_PROMPT.format(
        organization=org
    ) + "\n\nTEXT:\n" + text
    return call_llm(prompt)