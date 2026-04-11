from analyzer.llm import ask_gemini

def reviewer_agent(idea, competitor_output, sentiment_output, trends_output, positioning_output, risk_output):
    print("🔎 Reviewer Agent: Reviewing all agent outputs...")
    
    prompt = f"""
You are a senior startup analyst and critical reviewer.

A founder has this startup idea:
"{idea}"

Below are the outputs from 5 specialized AI agents that analyzed this idea.
Your job is to critically review ALL of them, identify contradictions, weak reasoning, and gaps.
Be honest and constructive — this review will help the founder make better decisions.

COMPETITOR RESEARCH:
{competitor_output}

MARKET SENTIMENT RESEARCH:
{sentiment_output}

MARKET TRENDS RESEARCH:
{trends_output}

POSITIONING STRATEGY:
{positioning_output}

RISK ANALYSIS:
{risk_output}

Review all of the above critically and thoroughly.

Respond in EXACTLY this format, no extra text:

OVERALL ASSESSMENT:
- Verdict: [Strong Idea / Promising Idea / Needs Work / High Risk]
- Summary: [2-3 sentences summarizing the overall picture]

CONFIDENCE SCORES:
- Competitor Analysis: [1-10] — [One sentence reason]
- Sentiment Analysis: [1-10] — [One sentence reason]
- Trends Analysis: [1-10] — [One sentence reason]
- Positioning Strategy: [1-10] — [One sentence reason]
- Risk Analysis: [1-10] — [One sentence reason]

CONTRADICTIONS FOUND:
- [Any contradiction between agent outputs, or "None found"]
- [Any contradiction between agent outputs, or "None found"]

WEAK POINTS:
- [Weakest part of the overall analysis and why]
- [Second weakest part of the overall analysis and why]

GAPS IN RESEARCH:
- [Important question that none of the agents answered]
- [Important question that none of the agents answered]

FINAL RECOMMENDATION:
- [One clear, honest recommendation for the founder on whether and how to proceed]
"""
    
    result = ask_gemini(prompt)
    return result