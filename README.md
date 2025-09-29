# BlogAgentic

Autonomously generate, edit, and draft blog content using LangGraph-powered agent workflows and LangChain LLMs.

---

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Architecture & Components](#architecture--components)  
- [Installation & Setup](#installation--setup)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Requirements & Dependencies](#requirements--dependencies)  
- [Contributing](#contributing)  
- [License](#license)  

---

## About

**BlogAgentic** is a Python application designed to autonomously handle blog content workflows. It uses **LangChain** as the foundation for interacting with LLMs, layered with **LangGraph** to orchestrate agentic flows—allowing for branching, stateful control and more advanced workflow logic.

It is suited for users who want an automated system that can draft, revise, and iterate on blog posts with minimal manual prompting.

---

## Features

- Agentic workflows for content generation and revision  
- Stateful orchestration via LangGraph (e.g. loops, branching)  
- Integration with LLMs via LangChain  
- Automated drafting and editing steps (as implemented)  

---

## Architecture & Components

- **LangChain**: Provides the abstraction for interacting with language models, prompt templating, tool execution, etc. :contentReference[oaicite:0]{index=0}  
- **LangGraph**: Orchestration framework on top of LangChain for defining directed workflows, handling state, branching, loops, and coordinating agents. :contentReference[oaicite:1]{index=1}  
- **Agent Nodes / Workflow Graph**: The core logic is split into nodes (e.g. generation, revision, etc.) and edges that control transitions.  
- **State Management**: The application retains context across steps, enabling more coherent multi-step operations.  
- **Entry point**: `app.py`  set up and run the agentic workflows.  

---

## Installation & Setup

1. **Clone the repo**  
   ```sh
   git clone https://github.com/daanyal-23/BlogAgentic.git
   cd BlogAgentic
   ```
2.Create a virtual environment (recommended)
```sh
   python3 -m venv venv
   source venv/bin/activate   # macOS / Linux  
   or
   venv\Scripts\activate      # Windows
  ```
3.Install dependencies
```sh
   pip install -r requirements.txt
  ```
4.Set up environment / API keys

## Usage

Here is a basic usage example:
```sh 
   python app.py
  ```
Once running, the system will proceed through a workflow that generates and edits blog drafts using your configured LLM agentic logic.

You may also pass specific prompts or parameters via CLI or modify the workflow graph as needed

## Project Structure

```sh
   BlogAgentic/
    ├── src/                  # (If present) Supporting modules or agent components  
    ├── app.py                # Application entry point  
    ├── main.py               # Main orchestration runner  
    ├── langgraph.json        # Graph definition / configuration  
    ├── pyproject.toml        # Project configuration  
    ├── requirements.txt      # Dependency list  
    ├── .python-version        # Python version lock  
    ├── .gitignore             # Files to ignore in version control  
    └── uv.lock                # Dependency lock (if using `uv` / lock tool)
```

Here’s a short explanation of key files:

app.py / main.py – Where the agentic workflows are initialized and executed.

langgraph.json – Defines the graph structure (nodes, edges, states) used by LangGraph.

src/ – Contains modular code for agent logic, utility functions, etc.

requirements.txt – All Python dependencies required by the project.

pyproject.toml – Metadata and build configuration.

uv.lock – Lock file.

## Requirements & Dependencies
-Python (version as specified in .python-version)

-Key Python libraries (from requirements.txt) such as LangChain, LangGraph, and any LLM client libraries

-Access to a compatible LLM backend (refers to Groq here.)

## Contributing
Thank you for considering contributing! While this is your personal project, here are some tips if you wish to grow it:

Fork the repo and work on feature branches.

Maintain tests (if you add them) and ensure existing functionality isn’t broken.

Follow consistent coding style (PEP8 / black / isort).

Document new functionality in README or inline comments.
