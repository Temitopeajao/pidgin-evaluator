# 🌍 Pidgin-Evaluator  
## LLM-as-a-Judge for West African Languages

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)
![NLP](https://img.shields.io/badge/Focus-NLP-orange)
![Domain](https://img.shields.io/badge/Domain-African%20Languages-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

> Automated semantic evaluation and quality control for English → Nigerian Pidgin translations using LLM judges.

---

## 📋 Overview

**Pidgin-Evaluator** is a Python pipeline that uses the **LLM-as-a-Judge** methodology to automatically assess translation quality for **low-resource African languages**, specifically **Nigerian Pidgin**.

Traditional metrics like **BLEU**, **ROUGE**, or **chrF** fail to capture:

- Cultural nuance  
- Code-switching  
- Informal grammar  
- Conversational tone  

Instead of surface-level token matching, this tool performs **semantic reasoning-based evaluation** using a stronger LLM — similar to how a human reviewer would judge quality.

It effectively simulates an **RLHF-style feedback loop** for translation systems.

---

## ✨ Features

### 🔁 Synthetic Translation Loop
Simulates base models (Llama, GPT-4o-mini, etc.) generating Pidgin translations.

### 🧠 LLM-as-a-Judge Scoring
A stronger judge model evaluates outputs on:
- Lexical accuracy
- Grammar
- Cultural authenticity
- Tone

### 📊 Likert Scale Grading
Scores each sample from **1–5** with structured reasoning.

### 🗣️ Explainable Feedback
Returns **why** a translation failed — not just numbers.

### 📦 Structured JSON Outputs
Plug directly into:
- Training pipelines
- SFT filtering
- RLHF datasets
- Analytics dashboards

---

## 🛠️ Why This Matters

### The Problem
African languages face:

- Limited datasets  
- Heavy code-switching  
- Sparse evaluation tools  
- High hallucination rates in LLMs  

### The Result
Poor training data → poor models.

### The Solution
**Pidgin-Evaluator = Automatic quality gate**

✔ Filters weak samples  
✔ Improves fine-tuning data  
✔ Reduces manual review  
✔ Boosts downstream performance  

---

## 🧱 Architecture

```
                ┌──────────────────┐
                │ English Sentence │
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ Base Translator  │  (Llama / GPT-4o-mini)
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ Judge Model      │  (GPT-4o)
                │ LLM-as-a-Judge   │
                └─────────┬────────┘
                          │
                          ▼
                ┌──────────────────┐
                │ JSON Output      │
                │ score + reason   │
                └──────────────────┘
```

---

## ⚙️ Installation

### 1. Clone repo

```bash
git clone https://github.com/yourusername/pidgin-evaluator.git
cd pidgin-evaluator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set API key

Mac/Linux:
```bash
export OPENAI_API_KEY=your_key_here
```

Windows:
```bash
setx OPENAI_API_KEY "your_key_here"
```

---

## ▶️ Quick Start

```python
from evaluator import evaluate_translation

result = evaluate_translation(
    source="How are you today?",
    translation="How you dey today?"
)

print(result)
```

### Example Output

```json
{
  "score": 5,
  "reasoning": "Accurate lexical choice and natural conversational tone."
}
```

---

## 🧪 Example Use Cases

- SFT dataset filtering  
- RLHF feedback simulation  
- Translation benchmarking  
- Linguistic research  
- African NLP tools  
- Model regression testing  

---

## 🧰 Built With

- Python
- OpenAI API (GPT-4o)
- Prompt Engineering
- JSON pipelines
- LLM Evaluation techniques
- NLP / Low-resource language research

---

## 📂 Project Structure

```
pidgin-evaluator/
│
├── evaluator/          # Core scoring engine
├── prompts/            # Judge prompts
├── data/               # Sample translation sets
├── scripts/            # Pipeline automation
├── notebooks/          # Experiments
├── requirements.txt
└── README.md
```

---

## 🔬 Future Roadmap

- [ ] Yoruba evaluation support  
- [ ] Hausa support  
- [ ] Igbo support  
- [ ] Batch scoring  
- [ ] Web dashboard  
- [ ] HuggingFace integration  
- [ ] Human + LLM hybrid scoring  

---

## 🤝 Contributing

Contributions are welcome.

Ideas:
- Better judge prompts
- More African languages
- Performance improvements
- Benchmark datasets

Open an issue or PR.

---

## 👤 Author

**Temitope Ajao**  
AI Engineer & LLM Specialist  

([LinkedIn](www.linkedin.com/in/temitope-ajao-4a8670302) • [Email](mailto:topekele@email.com)
)

---

## 📜 License

MIT License

---

## ⭐ If this project helps you
Give it a star — it helps visibility for African NLP research ✨




