from analyzer.llm import ask_gemini
from pytrends.request import TrendReq
import pandas as pd

def get_trends_data(keyword):
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([keyword], cat=0, timeframe='today 12-m')
        
        interest_over_time = pytrends.interest_over_time()
        
        if interest_over_time.empty:
            return None
        
        interest_over_time = interest_over_time.drop(columns=['isPartial'], errors='ignore')
        
        avg_interest = int(interest_over_time[keyword].mean())
        max_interest = int(interest_over_time[keyword].max())
        min_interest = int(interest_over_time[keyword].min())
        
        recent = interest_over_time[keyword].tail(4).mean()
        older = interest_over_time[keyword].head(4).mean()
        
        if recent > older * 1.1:
            trend_direction = "Growing"
        elif recent < older * 0.9:
            trend_direction = "Declining"
        else:
            trend_direction = "Stable"
        
        return {
            "keyword": keyword,
            "avg_interest": avg_interest,
            "max_interest": max_interest,
            "min_interest": min_interest,
            "trend_direction": trend_direction
        }
    
    except Exception as e:
        return None


def trends_agent(idea):
    print("📈 Trends Agent: Fetching Google Trends data...")
    
    keywords = idea.split()[:3]
    keyword = " ".join(keywords)
    
    trends_data = get_trends_data(keyword)
    
    if trends_data:
        trends_summary = f"""
Keyword analyzed: {trends_data['keyword']}
Average interest score (0-100): {trends_data['avg_interest']}
Peak interest score: {trends_data['max_interest']}
Lowest interest score: {trends_data['min_interest']}
Trend direction over last 12 months: {trends_data['trend_direction']}
"""
    else:
        trends_summary = "Google Trends data not available for this keyword."
    
    prompt = f"""
You are a market trends analyst.

A founder has this startup idea:
"{idea}"

Here is real Google Trends data for this market:
{trends_summary}

Analyze the market trends for this idea.

Respond in EXACTLY this format, no extra text:

TREND DIRECTION:
- Direction: [Growing / Stable / Declining]
- Reason: [One sentence explaining the trend]

MARKET TIMING:
- Assessment: [Good time to enter / Neutral / Bad time to enter]
- Reason: [One sentence explaining why]

OPPORTUNITIES FROM TRENDS:
- [Specific opportunity based on trend data]
- [Specific opportunity based on trend data]

RISKS FROM TRENDS:
- [Specific risk based on trend data]
- [Specific risk based on trend data]
"""
    
    print("🤖 Trends Agent: Analyzing with LLM...")
    result = ask_gemini(prompt)
    return result