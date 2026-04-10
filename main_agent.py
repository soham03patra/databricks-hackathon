# main_agent.py

from llm_extractor import (
    extract_organizations,
    extract_basic_info,
    extract_free_form,
    extract_specialties
)

def run_full_pipeline(text):

    orgs = extract_organizations(text)

    results = []

    for org in orgs:
        basic = extract_basic_info(text, org)
        free = extract_free_form(text, org)
        spec = extract_specialties(text, org)

        results.append({
            "organization": org,
            "basic_info": basic,
            "free_form": free,
            "specialties": spec
        })

    return results


def agent(query, spark, df):

    if "how many" in query:
        return spark.sql("SELECT COUNT(*) FROM facilities")

    elif "region" in query:
        return spark.sql("""
            SELECT address_stateOrRegion, COUNT(*) 
            FROM facilities GROUP BY address_stateOrRegion
        """)

    elif "anomaly" in query:
        return spark.sql("""
            SELECT * FROM facilities
            WHERE size(split(procedure, ',')) > 20 
            AND size(split(equipment, ',')) < 3
        """)

    elif "extract" in query:
        text = df.select("description").first()[0]
        return run_full_pipeline(text)

    else:
        return "Query not supported"