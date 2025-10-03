# BlogAgentic

Autonomously generate, edit, and draft blog content using LangGraph-powered agent workflows and LangChain LLMs, now with support for multi-language blog generation (English, Hindi, and French).

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

**BlogAgentic** is a Python application designed to autonomously handle end-to-end blog content workflows.
It leverages LangChain for LLM interaction and LangGraph for orchestrating agentic flows, enabling stateful workflows, branching, and iterative editing loops.

The system can:

-Generate initial drafts.

-Revise and refine blog content.

-Produce blogs in multiple languages (English, Hindi, and French) with minimal prompting.

-This makes BlogAgentic ideal for users, teams, or organizations looking to automate    multilingual blog generation and editing.

---

## Features

- Agentic workflows for content generation and revision  
- Stateful orchestration via LangGraph (e.g. loops, branching)
- Multi-language support: generate blogs in English, Hindi, and French
- Seamless integration with LLMs using LangChain
- Automated drafting and editing steps (as implemented)
- Customizable graph definition (langgraph.json) for extending workflows

---

## Architecture & Components

- **LangChain**: Provides the abstraction for interacting with language models, prompt templating, tool execution, etc. 
- **LangGraph**: Orchestration framework on top of LangChain for defining directed workflows, handling state, branching, loops, and coordinating agents. 
- **Agent Nodes / Workflow Graph**: The core logic is split into nodes (e.g. generation, revision, etc.) and edges that control transitions.
- **Multi-language capability**: Translation and generation nodes allow outputs in Hindi and French.
- **State Management**: The application retains context across steps, enabling more coherent multi-step operations.  
- **Entry point**: `app.py`  set up and run the agentic workflows.  

---

## Installation & Setup

1. **Clone the repo**  
   ```sh
   git clone https://github.com/daanyal-23/BlogAgentic.git
   cd BlogAgentic
   ```
2. **Create a virtual environment (recommended)**
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # macOS / Linux  
   or
   venv\Scripts\activate      # Windows
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment / API keys**

## Usage

Basic run:
```sh 
   python app.py
  ```
By default, the system will run through the defined workflow and generate/edit a blog draft.

To specify language output (English, Hindi, French), update the workflow configuration or pass parameters accordingly.

## Project Structure

```sh
   BlogAgentic/
    ├── src/                  # Supporting modules or agent components  
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

-app.py / main.py – Where the agentic workflows are initialized and executed.

-langgraph.json – Defines the graph structure (nodes, edges, states) used by LangGraph.

-src/ – Contains modular code for agent logic, utility functions, etc.

-requirements.txt – All Python dependencies required by the project.

-pyproject.toml – Metadata and build configuration.

-uv.lock – Lock file.

## Requirements & Dependencies
-Python (version as specified in .python-version)

-Key Python libraries (from requirements.txt) such as LangChain, LangGraph, and any LLM client libraries

-Access to a compatible LLM backend (refers to Groq here.)

## Contributing
Thank you for considering contributing! While this is your personal project, here are some tips if you wish to grow it:

-Fork the repo and work on feature branches.

-Maintain tests (if you add them) and ensure existing functionality isn’t broken.

-Follow consistent coding style (PEP8 / black / isort).

-Document new functionality in README or inline comments.



