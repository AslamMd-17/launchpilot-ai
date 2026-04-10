from analyzer.llm import ask_gemini

def positioning_agent(idea, competitor_output, sentiment_output, trends_output):
    print("💡 Positioning Agent: Analyzing positioning strategy...")
    
    prompt = f"""
You are a startup positioning strategist.

A founder has this startup idea:
"{idea}"

Here is what our research agents found:

COMPETITOR RESEARCH:
{competitor_output}

MARKET SENTIMENT RESEARCH:
{sentiment_output}

MARKET TRENDS RESEARCH:
{trends_output}

Based on ALL of the above research, develop a positioning strategy for this startup.

Respond in EXACTLY this format, no extra text:

TARGET AUDIENCE:
- Primary: [Specific primary audience with details]
- Secondary: [Specific secondary audience with details]

UNIQUE SELLING POINT:
- [One clear, compelling sentence that differentiates this product]

DIFFERENTIATION STRATEGY:
- vs Competitors: [How to stand out from the competitors identified above]
- vs Market: [How to position against the broader market]

POSITIONING STATEMENT:
- "[Product name] is for [target audience] who [pain point]. Unlike [competitor], our product [key differentiator]."

GO TO MARKET ANGLE:
- [The single best channel or approach to reach the target audience first]
"""
    
    result = ask_gemini(prompt)
    return result