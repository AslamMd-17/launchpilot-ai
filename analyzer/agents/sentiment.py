from analyzer.llm import ask_gemini
from analyzer.search import web_search, format_search_results

def sentiment_agent(idea):
    print("🔍 Sentiment Agent: Searching for user opinions...")
    
    search_results = web_search(f"{idea} problems complaints user feedback forum")
    formatted_results = format_search_results(search_results)
    
    prompt = f"""
You are a market research analyst specializing in consumer sentiment.

A founder has this startup idea:
"{idea}"

Here is real data from the web showing what users are saying about this problem space:
{formatted_results}

Analyze the market sentiment for this idea based on the research above.

Respond in EXACTLY this format, no extra text:

DEMAND LEVEL:
- Level: [High / Medium / Low]
- Reason: [One sentence explaining why]

PAIN POINTS:
- [Specific pain point real users experience]
- [Specific pain point real users experience]
- [Specific pain point real users experience]

USER SENTIMENTS:
- [What users feel about current solutions]
- [What users wish existed]
- [What users complain about most]

MARKET OPPORTUNITY:
- [One clear opportunity based on the sentiment data above]
"""
    
    print("🤖 Sentiment Agent: Analyzing with LLM...")
    result = ask_gemini(prompt)
    return result