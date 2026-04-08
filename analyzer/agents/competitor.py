from analyzer.llm import ask_gemini
from analyzer.search import web_search, format_search_results

def competitor_agent(idea):
    print("🔍 Competitor Agent: Searching the web...")
    
    search_results = web_search(f"{idea} competitors alternatives startups")
    formatted_results = format_search_results(search_results)
    
    prompt = f"""
You are a startup analyst specializing in competitive research.

A founder has this startup idea:
"{idea}"

Here is real data from the web about competitors in this space:
{formatted_results}

Based on this research, analyze the competitive landscape.

Respond in EXACTLY this format, no extra text:

COMPETITORS:
- Name: [competitor name]
  Features: [2-3 key features]
  Pricing: [pricing if known, or "Not publicly available"]
  Weakness: [one key weakness]

- Name: [competitor name]
  Features: [2-3 key features]
  Pricing: [pricing if known, or "Not publicly available"]
  Weakness: [one key weakness]

- Name: [competitor name]
  Features: [2-3 key features]
  Pricing: [pricing if known, or "Not publicly available"]
  Weakness: [one key weakness]

MARKET GAP:
- [One clear gap in the market that the founder's idea could fill]

COMPETITIVE ADVANTAGE NEEDED:
- [What this startup must do better than existing players to win]
"""
    
    print("🤖 Competitor Agent: Analyzing with LLM...")
    result = ask_gemini(prompt)
    return result