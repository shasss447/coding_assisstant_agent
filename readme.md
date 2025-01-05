# Simple Code Assistant Agent

This project is a simple code assistant agent designed to help user generate and test Python code based on natural language prompts. The system employs **Microsoft's AutoGen framework** to coordinate two specialized agents: one for code generation and another for code execution and feedback. It leverages **LM Studio** to host Hugging Face models on a local server for code generation, ensuring high performance and privacy.

## Features

- **Two-Agent System:**
  - **Code Generation Agent:** Writes Python code snippets based on user queries.
  - **Code Execution Agent:** Executes the generated code, validates its functionality, and provides feedback.
- **Local Model Hosting:** Utilizes **LM Studio** to host Hugging Face models locally, ensuring fast and secure processing.
- **Persistent Output Storage:** Saves all generated code and corresponding outputs in a text file for reference.
- **Natural Language Understanding:** Accepts and processes user queries written in plain language.
- **Interactive Workflow:** Provides user-centric feedback and asks for additional inputs when required.

## How It Works

1. **User Query:** The user provides a natural language query, such as:
2. **Code Generation Agent:**
   - Generates a Python code snippet using a locally hosted model via **LM Studio**.
3. **Code Execution Agent:**
   - Executes the generated code and validates its functionality.
4. **Output Storage:** All generated code and feedback are saved in a text file for easy access.

## Installation

1. Clone the repository:
  ```bash
       git clone https://github.com/shasss447/coding_assisstant_agent.git
   ```
2. Install the AutoGen framework
3. Download and install LM Studio from LM Studio's official site.
4. Use LM Studio to download and configure the desired Hugging Face models (e.g., `Llama-2`) for local hosting.

## Usage

1. Configure the Model in LM Studio
   - Open LM Studio and load the desired model (e.g., Llama-2).
   - Host the model locally by following the on-screen instructions in LM Studio.
2. Run the Agents
   - You can choose to run the project using either the provided Jupyter notebook or the main script.
3. Interact with the Agent
   - Enter your query in plain language, such as *"Write a Python function to calculate the factorial of a number"*
   - The agents will generate code, test it, and provide feedback. Outputs will be saved in a .txt file.