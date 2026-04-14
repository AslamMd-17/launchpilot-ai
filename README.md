# ⚡ LaunchPilot AI

LaunchPilot AI is a multi-agent system that validates startup ideas. You give it an idea, and 6 AI agents research it from different angles — competitors, market sentiment, trends, positioning, risks — and a final reviewer critiques everything and gives you an honest verdict.

Built as a student project to learn multi-agent AI systems from scratch.

---

## How it works

When you submit an idea, 6 agents run in sequence:

- **Competitor Agent** searches the web for real competitors and identifies market gaps
- **Sentiment Agent** finds real user opinions and pain points from across the web
- **Trends Agent** pulls Google Trends data to assess whether the market is growing or declining
- **Positioning Agent** uses all 3 outputs above to build a differentiation strategy
- **Risk Agent** identifies market, competitive, and positioning risks grounded in real data
- **Reviewer Agent** reads all 5 outputs, scores each one, finds contradictions, and gives a final recommendation

Each agent passes its output to the next one — so the final analysis is built on real research, not just a single prompt.

---

## Tech stack

- Backend — Django
- LLM — Groq API running LLaMA 3.3 70B
- Web Search — Tavily API
- Market Trends — pytrends
- Database — SQLite
- Frontend — HTML + Bootstrap
- Deployed on — Render

---

## Running locally

1. Clone the repo
2. Create and activate a virtual environment
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Create a `.env` file in the root folder
 GROQ_API_KEY=your_key_here
 TAVILY_API_KEY=your_key_here

5. Run migrations
```bash
python manage.py migrate
```
6. Start the server
```bash
python manage.py runserver
```
7. Go to `http://127.0.0.1:8000`

---

## API keys needed

Both are free with no credit card required:

- Groq API — get it at console.groq.com
- Tavily API — get it at tavily.com

---

## What you get

Submit any startup idea and within 60 seconds you get a full report with:

- Real competitors found on the web
- Market sentiment based on actual user discussions
- Google Trends analysis for the space
- A positioning strategy built from the research
- A risk assessment with validation suggestions
- An overall verdict with confidence scores per agent

---

## Project structure
launchpilot/
├── analyzer/
│   ├── agents/
│   │   ├── competitor.py
│   │   ├── sentiment.py
│   │   ├── trends.py
│   │   ├── positioning.py
│   │   ├── risk.py
│   │   └── reviewer.py
│   ├── orchestrator.py
│   ├── models.py
│   ├── views.py
│   └── llm.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── loading.html
│   ├── result.html
│   └── history.html
└── README.md