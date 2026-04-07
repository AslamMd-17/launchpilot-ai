from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query, max_results=5):
    try:
        response = client.search(
            query=query,
            max_results=max_results,
            search_depth="basic"
        )
        
        results = []
        for r in response.get("results", []):
            results.append({
                "title": r.get("title", ""),
                "content": r.get("content", ""),
                "url": r.get("url", "")
            })
        
        return results
    
    except Exception as e:
        return f"ERROR: {str(e)}"


def format_search_results(results):
    if isinstance(results, str):
        return results
    
    formatted = ""
    for i, r in enumerate(results, 1):
        formatted += f"{i}. {r['title']}\n"
        formatted += f"   {r['content'][:300]}\n"
        formatted += f"   Source: {r['url']}\n\n"
    
    return formatted.strip()