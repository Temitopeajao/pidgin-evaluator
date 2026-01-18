# Pidgin-Evaluator: LLM-as-a-Judge for West African Languages

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![OpenAI](https://img.shields.io/badge/API-OpenAI-green)
![Domain](https://img.shields.io/badge/Domain-NLP%20%2F%20African%20Languages-orange)

## 📋 Overview
**Pidgin-Evaluator** is a Python-based pipeline designed to automate the quality assessment of English-to-Nigerian-Pidgin translations. 

In the context of training Large Language Models (LLMs) for low-resource languages, standard metrics like BLEU or ROUGE are often insufficient because they fail to capture cultural nuance, code-switching syntax, and tonal context. This project implements the **"LLM-as-a-Judge"** methodology to provide semantic evaluation and reasoning, simulating an RLHF (Reinforcement Learning from Human Feedback) loop.

## 🚀 Key Features
*   **Synthetic Translation Loop:** Simulates a base model (e.g., Llama-3 or GPT-4o-mini) attempting to translate English to Pidgin.
*   **Automated Scoring:** Uses a stronger "Judge" model to grade outputs on a 1-5 Likert scale based on lexical accuracy, tone, and grammar.
*   **Reasoning Extraction:** Unlike numerical metrics, this pipeline extracts *qualitative reasoning* for every score, helping engineers understand *why* a model failed.
*   **JSON Output:** Structured data return for easy integration into larger data processing pipelines.

## 🛠️ The Engineering Challenge
Training models on West African languages presents unique challenges:
1.  **Low-Resource Data:** High-quality parallel corpora for Pidgin are scarce.
2.  **Code-Switching:** Pidgin fluidly mixes English and local dialects (Yoruba, Igbo, Hausa).
3.  **Hallucination:** Base models often revert to standard "Queen's English" or hallucinate fake slang when unsure.

This tool helps solve these issues by automating the **Supervised Fine-Tuning (SFT)** data validation process, ensuring only high-quality pairs enter the training set.

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pidgin-evaluator.git
   cd pidgin-evaluator
