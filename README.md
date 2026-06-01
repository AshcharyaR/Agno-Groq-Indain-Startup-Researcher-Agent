# Agno Groq India Startup Research Agent

This repository contains a multi-agent research workflow built with **Agno** and **Groq** for analyzing the Indian startup ecosystem, with a specific focus on AI-driven companies.

---

## Overview

The project implements a two-agent team that:

- Collects up-to-date information about Indian startups, founders, and funding activity using web and news search.
- Synthesizes the collected information into a concise, structured insight brief suitable for analysts, founders, and investors.

The workflow is designed to be a clear, reproducible example of how to build research-oriented AI agents and teams using Agno and Groq.

---

## Architecture

The solution is composed of the following core components:

### 1. `startup_researcher` (Agent)

- **Role:** `Indian Startup Researcher`  
- **Model:** `Groq(id="llama-3.1-8b-instant")`  
- **Tools:** `DuckDuckGoTools(enable_search=True, enable_news=True)`  
- **Responsibility:**  
  - Research Indian startups, funding rounds, and founders.  
  - Prioritize current and India-specific sources for higher relevance.

### 2. `summary_writer` (Agent)

- **Role:** `Insight Summarizer`  
- **Model:** `Groq(id="llama-3.3-70b-versatile")`  
- **Responsibility:**  
  - Transform raw research output into a one-page summary.  
  - Organize content into sections: **Overview**, **Key Players**, **Funding**, and **Opportunities**.

### 3. `startup_team` (Team)

- **Model:** `Groq(id="llama-3.3-70b-versatile")`  
- **Members:** `startup_researcher`, `summary_writer`  
- **Name:** `"india_startup_team"`  
- **Team Instructions:**  
  - First, use `startup_researcher` to collect data on the topic.  
  - Then, use `summary_writer` to synthesize the findings into a structured brief.

The entry point executes the team with a predefined query:

```python
startup_team.print_response(
    "Research notable Indian AI startups and summarize their focus areas.",
    stream=True,
)
```



---

## Technology Stack

- **Agno** – Python framework for building and orchestrating agents and teams.  
- **Groq** – High-performance LLM gateway; Llama 3.x models are used for both research and summarization.  
- **DuckDuckGoTools** – Agno toolkit enabling web and news search via DuckDuckGo.  
- **Python** (with `python-dotenv`) – For environment and configuration management.

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

A typical `requirements.txt` could include:

```txt
agno
python-dotenv
duckduckgo-search
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```bash
touch .env
```

Add your Groq API key:

```env
GROQ_API_KEY="your_groq_api_key_here"
```

---

## Usage

Run the startup research team script:

```bash
python India_focused_Startup_Research_team.py
```

On execution, the team will:

1. Use `startup_researcher` to discover notable Indian AI startups and their focus areas via web and news search.  
2. Pass the findings to `summary_writer` to generate a structured, one-page analytical summary.  
3. Stream the final response to the console.

You can modify the query passed to `print_response` to target different verticals or geographies (e.g., Indian fintech, edtech, or climate-tech startups).[]file:40]

---

## Customization

Potential extensions include:

- **Additional Agents**  
  - A fact-checking agent to validate critical funding and valuation data.  
  - An insights agent to generate investment notes or opportunity assessments.

- **Different Queries and Sectors**  
  - Replace the default query with domain-specific prompts (e.g., “early-stage Indian AI healthcare startups”).

- **Integration with Other Systems**  
  - Persist results in a database or data warehouse.  
  - Expose the workflow via a REST API or simple UI (e.g., FastAPI, Streamlit).

---

## Motivation

This project is intended as a portfolio-friendly, production-lean example of:

- Applying **agentic AI patterns** to real-world research workflows.  
- Combining **Groq-hosted LLMs** with **Agno teams** for orchestrated multi-step reasoning.  
- Building reusable components for startup/market analysis that can be adapted to other domains.

It is particularly suitable as a demonstration of skills in **LLM tooling, multi-agent orchestration, and applied AI for market research**.
