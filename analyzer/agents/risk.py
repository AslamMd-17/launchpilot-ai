from analyzer.llm import ask_gemini

def risk_agent(idea, competitor_output, sentiment_output, trends_output, positioning_output):
    print("⚠️ Risk Agent: Analyzing risks...")
    
    prompt = f"""
You are a startup risk analyst with expertise in market validation.

A founder has this startup idea:
"{idea}"

Here is the full research from our analysis pipeline:

COMPETITOR RESEARCH:
{competitor_output}

MARKET SENTIMENT RESEARCH:
{sentiment_output}

MARKET TRENDS RESEARCH:
{trends_output}

POSITIONING STRATEGY:
{positioning_output}

Based on ALL of the above research, identify the real risks this startup faces.
Every risk must be traceable to a specific finding from the research above.

Respond in EXACTLY this format, no extra text:

MARKET RISKS:
- [Risk based on trends data above]
- [Risk based on trends data above]

COMPETITIVE RISKS:
- [Risk based on specific competitors identified above]
- [Risk based on specific competitors identified above]

POSITIONING RISKS:
- [Risk based on the positioning strategy above]
- [Risk based on the positioning strategy above]

OVERALL RISK LEVEL:
- Level: [High / Medium / Low]
- Reason: [One sentence summary of the overall risk profile]

VALIDATION SUGGESTIONS:
- [Concrete action the founder can take this week to validate]
- [Concrete action the founder can take this week to validate]
- [Concrete action the founder can take this week to validate]
"""
    
    result = ask_gemini(prompt)
    return result