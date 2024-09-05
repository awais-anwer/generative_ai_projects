🧮 Text to Math Problem Solver and Data Search Assistant
This project is a Streamlit-based web application that solves math problems and answers general data search queries using the power of LangChain and Groq. It combines tools like a calculator for mathematical queries, logical reasoning capabilities, and a Wikipedia search assistant to deliver an all-in-one problem-solving and data retrieval solution.

Features
Math Problem Solving: Input mathematical expressions, and the app will solve them using an LLM-based calculator powered by the Groq LLM (Gemma2-9b-It).
Logic and Reasoning: Ask reasoning-based questions, and the app will provide step-by-step explanations with detailed logic using a custom prompt template.
Wikipedia Search Assistant: Ask any question requiring information from the web, and the app will search Wikipedia for relevant information.
User-Friendly Interface: Built using Streamlit, the app has an intuitive chat-based interface that handles user queries with ease.

Usage
Math Problem Solving: Enter any math problem, and the app will provide the solution and detailed steps.
Logic and Reasoning Questions: For complex reasoning questions, the app uses a pre-defined prompt to generate answers logically.
Wikipedia Search: If the question is data-based, the app will utilize Wikipedia to fetch information and provide relevant answers.

How It Works
LLM: The app uses the Gemma2-9b-It model from Groq to handle both text-based reasoning and mathematical calculations.
Tools: Three tools—Calculator, Reasoning Tool, and Wikipedia Search—are integrated into the app.
Streamlit Interface: The app utilizes Streamlit to create a simple and interactive UI.
