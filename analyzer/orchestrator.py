from analyzer.agents.competitor import competitor_agent
from analyzer.agents.sentiment import sentiment_agent
from analyzer.agents.trends import trends_agent
from analyzer.agents.positioning import positioning_agent
from analyzer.agents.risk import risk_agent
from analyzer.agents.reviewer import reviewer_agent
from analyzer.models import Analysis


def run_agents(analysis_id):
    try:
        analysis = Analysis.objects.get(id=analysis_id)
        idea = analysis.idea

        analysis.status = 'running'
        analysis.save()

        print(f"\n Starting analysis for: {idea}\n")

        print("Step 1/6: Running Competitor Agent.")
        competitor_output = competitor_agent(idea)

        print("Step 2/6: Running Sentiment Agent.")
        sentiment_output = sentiment_agent(idea)

        print("Step 3/6: Running Trends Agent.")
        trends_output = trends_agent(idea)

        print("Step 4/6: Running Positioning Agent.")
        positioning_output = positioning_agent(
            idea,
            competitor_output,
            sentiment_output,
            trends_output
        )

        print("Step 5/6: Running Risk Agent.")
        risk_output = risk_agent(
            idea,
            competitor_output,
            sentiment_output,
            trends_output,
            positioning_output
        )

        print("Step 6/6: Running Reviewer Agent.")
        reviewer_output = reviewer_agent(
            idea,
            competitor_output,
            sentiment_output,
            trends_output,
            positioning_output,
            risk_output
        )

        result = {
            "competitor": competitor_output,
            "sentiment": sentiment_output,
            "trends": trends_output,
            "positioning": positioning_output,
            "risk": risk_output,
            "reviewer": reviewer_output
        }

        analysis.result = str(result)
        analysis.status = 'completed'
        analysis.save()

        print("\nAnalysis complete\n")
        return result

    except Exception as e:
        analysis = Analysis.objects.get(id=analysis_id)
        analysis.status = 'failed'
        analysis.save()
        print(f"Analysis failed: {str(e)}")
        return None