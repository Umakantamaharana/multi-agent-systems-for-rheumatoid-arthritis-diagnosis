# Multi-Agent Systems for Rheumatoid Arthritis Diagnosis (RPWR)

**Right Prediction Wrong Reasoning** - A research project exploring multi-agent LLM systems for medical diagnosis, specifically focused on Rheumatoid Arthritis screening and diagnosis.

## 🎯 Project Overview

This project implements and evaluates different multi-agent architectures using Large Language Models (LLMs) to diagnose Rheumatoid Arthritis from patient symptom data. The system explores various agent configurations with and without knowledge base integration.

### Key Features

- **Multiple Agent Architectures**: Single agent, dual agent, and three-agent systems
- **Knowledge Base Integration**: RAG (Retrieval-Augmented Generation) using ChromaDB
- **Multi-Model Support**: Compatible with OpenAI (GPT-4, O1, O3-mini), Google Gemini (2.0, 2.5), and local models via Ollama (DeepSeek, Qwen)
- **Comprehensive Evaluation**: Automated testing and result analysis across different model configurations

## 📁 Project Structure

```
multi-agent-systems-for-rheumatoid-arthritis-diagnosis/
├── .env                    # Environment variables (API keys)
├── .env.example           # Template for environment setup
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── run.sh                 # Main execution script
├── data/                  # Dataset files
│   ├── knowledge_base_280.csv      # Medical knowledge base
│   ├── preprocessed_data_350.csv   # Preprocessed patient data
│   ├── test_70.csv                 # Test dataset
│   └── test_data.csv               # Additional test data
├── knowledge_base/        # ChromaDB vector database
│   ├── chroma.sqlite3
│   └── f0eede21-c8e5-4813-91e1-93fb19985e5d/
├── notebooks/             # Jupyter notebooks for analysis
│   └── data_processing.ipynb       # Data cleaning and processing
├── results/               # Experiment results
│   ├── agent_kb/          # Results with knowledge base
│   ├── agent_wkb/         # Results without knowledge base
│   └── two_agent_kb/      # Two-agent system results
└── scripts/               # Python scripts
    ├── agent_without_kb.py         # Single agent without KB
    ├── dataset.py                  # Dataset utilities
    ├── one_agent_with_kb.py        # Single agent with KB
    ├── three_agent_with_kb.py      # Three-agent system
    └── two_agent_with_kb.py        # Two-agent system
```

## 🚀 Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)
- API keys for OpenAI and/or Google Gemini (or Ollama for local models)

### Installation

1. **Clone or navigate to the repository**:
   ```bash
   cd multi-agent-systems-for-rheumatoid-arthritis-diagnosis
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

## 💻 Usage

### Running Individual Scripts

#### 1. Agent Without Knowledge Base
```bash
python scripts/agent_without_kb.py --provider GOOGLE --model gemini-2.0-flash --results_dir results/agent_wkb
```

#### 2. Agent With Knowledge Base
```bash
python scripts/one_agent_with_kb.py --provider GOOGLE --model gemini-2.5-pro-preview-03-25 --results_dir results/agent_kb
```

#### 3. Two-Agent System
```bash
python scripts/two_agent_with_kb.py --provider OPENAI --model o1 --results_dir results/two_agent_kb
```

### Using the Run Script

The `run.sh` script provides a convenient way to run multiple experiments:

```bash
chmod +x run.sh
./run.sh
```

Edit `run.sh` to configure which models and providers to test.

### Supported Providers and Models

| Provider | Models | Notes |
|----------|--------|-------|
| **OPENAI** | `o1`, `o3-mini`, `gpt-4` | Requires OpenAI API key |
| **GOOGLE** | `gemini-2.0-flash`, `gemini-2.5-pro-preview-03-25` | Requires Google API key |
| **OLLAMA** | `deepseek-r1:70b`, `qwq` | Requires local Ollama installation |

## 🏗️ Agent Architectures

### 1. Single Agent Without Knowledge Base
- Direct diagnosis from patient symptoms
- No external medical knowledge integration
- Baseline for comparison

### 2. Single Agent With Knowledge Base
- RAG-enhanced diagnosis
- Retrieves relevant medical information from ChromaDB
- Improved accuracy with domain knowledge

### 3. Two-Agent System
- **Agent 1**: Diagnosis agent
- **Agent 2**: Reasoning agent
- Collaborative decision-making process

### 4. Three-Agent System
- Extended multi-agent collaboration
- More complex reasoning chains
- (Implementation in progress)

## 📊 Results

Results are saved in CSV format in the `results/` directory, organized by agent architecture and model:

```
results/
├── agent_kb/
│   ├── gemini-2.0-flash.csv
│   └── o1.csv
├── agent_wkb/
│   ├── gemini-2.5-pro-preview-03-25.csv
│   └── deepseek-r1:70b.csv
└── two_agent_kb/
    └── o3-mini.csv
```

Each CSV contains:
- Patient symptoms
- Predicted diagnosis
- Reasoning/explanation
- Actual diagnosis (ground truth)
- Model metadata

## 🔬 Research Context

This project investigates the phenomenon of "Right Prediction, Wrong Reasoning" in LLM-based medical diagnosis systems. Key research questions include:

- How do different agent architectures affect diagnostic accuracy?
- Does knowledge base integration improve reasoning quality?
- Can multi-agent systems provide better explanations?
- How do different LLM models compare in medical reasoning tasks?

## 📝 Dependencies

Key dependencies (see `requirements.txt` for full list):
- `langchain-chroma`: Vector database for knowledge base
- `langchain-openai`: OpenAI model integration
- `langchain-google-genai`: Google Gemini integration
- `langchain-ollama`: Local model support
- `langgraph`: Multi-agent orchestration
- `pandas`: Data processing
- `scikit-learn`: ML utilities
- `matplotlib`: Visualization

## 🤝 Contributing

This is a research project. If you'd like to contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

[Add your license information here]

## 📧 Contact

[Add contact information here]

## 🙏 Acknowledgments

This project uses:
- LangChain for LLM orchestration
- ChromaDB for vector storage
- OpenAI, Google, and Ollama for LLM inference

---

**Note**: This is a research project for educational and experimental purposes. It should not be used for actual medical diagnosis without proper validation and regulatory approval.
