# 🤖 GenAI Chatbot — Local LLM with Ollama

A simple, interactive Generative AI chatbot built using **Python, Streamlit, and Ollama**. The application connects to a locally running Large Language Model (LLM) through Ollama's chat API and provides a conversational interface in the browser.

🚀 **Live Demo:** [Try the GenAI Chatbot](https://mysql-desperate-geology-bin.trycloudflare.com)

> **Note:** The live demo uses a temporary Cloudflare Quick Tunnel. It is accessible only while the tunnel, Streamlit application, and local Ollama service are running on the host computer.

## ✨ Features

- 💬 Interactive chat interface built with Streamlit
- 🧠 AI-generated responses using a local LLM
- 🔗 Integration with the Ollama Chat API
- 🖥️ Local model inference through Ollama
- 🌐 Temporary public access using Cloudflare Tunnel
- 🔐 No API key required for local Ollama inference

## 🛠️ Tech Stack

| Technology        | Purpose                                          |
| ----------------- | ------------------------------------------------ |
| Python            | Application logic                                |
| Streamlit         | Chatbot user interface                           |
| Ollama            | Running the local language model                 |
| Ollama Chat API   | Sending messages and receiving AI responses      |
| Cloudflare Tunnel | Temporary public access to the local application |
| Git & GitHub      | Version control and project hosting              |

## 🏗️ How It Works

1. The user enters a message in the Streamlit interface.
2. The Python application sends the conversation to Ollama's local Chat API.
3. Ollama processes the request using the configured language model.
4. The model generates a response.
5. The chatbot displays the response in the interface.
6. Cloudflare Tunnel forwards public web requests to the local Streamlit server.

```text
User
  |
  v
Streamlit Chat Interface
  |
  v
Python Application
  |
  v
Ollama Chat API
  |
  v
Local Language Model
  |
  v
AI Response
  |
  v
Streamlit UI
```

## 📋 Prerequisites

Before running the project, install:

- Python 3.10 or a compatible version for your dependencies
- Ollama for Windows
- Git (optional, for cloning the repository)

Downloads:

- [Python](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/download)
- [Git](https://git-scm.com/downloads)
- [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/downloads/)

## ⚙️ Installation and Setup

### 1. Clone the repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd GenAI-Chatbot
```

Alternatively, download the repository ZIP and extract it.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If the virtual environment is already created, activate it instead of creating another one.

### 3. Install dependencies

If your project contains a `requirements.txt` file:

```powershell
pip install -r requirements.txt
```

If not, install the dependencies required by your existing application. For a basic Streamlit chatbot, this may include:

```powershell
pip install streamlit requests
```

Do not reinstall packages unnecessarily if your existing environment already works.

### 4. Start Ollama

Install Ollama and make sure its local service is running.

Check the installed models:

```powershell
ollama list
```

If you have not downloaded a model yet, pull a compatible model, for example:

```powershell
ollama pull llama3.2
```

Use the model already configured in your application if it differs from this example.

Ollama's local API is typically available at:

```text
http://localhost:11434/api/chat
```

### 5. Run the Streamlit application

From the project directory, activate your virtual environment and run:

```powershell
streamlit run app.py
```

Open the local application:

```text
http://localhost:8501
```

Make sure the chatbot successfully generates AI responses before creating a public tunnel.

## 🌐 Access the Chatbot Publicly

Cloudflare Quick Tunnel allows temporary public access without deploying the application to a traditional hosting server.

### 1. Download cloudflared

Download the Windows executable from the [official Cloudflare documentation](https://developers.cloudflare.com/tunnel/downloads/).

### 2. Start the tunnel

Keep Streamlit running. Open a second PowerShell terminal and execute the following command, adjusting the executable path if necessary:

```powershell
& "$HOME\Downloads\cloudflared-windows-amd64.exe" tunnel --url http://localhost:8501
```

### 3. Open the public URL

Cloudflare will display a temporary URL similar to:

```text
https://your-generated-name.trycloudflare.com
```

Open that URL in your browser.

**Important:** The generated URL can change when you restart the Quick Tunnel. Your local computer, Streamlit application, and Ollama service must remain available for the demo to work.

## 📁 Project Structure

The exact structure depends on your repository. A basic setup may look like this:

```text
GenAI-Chatbot/
├── app.py
├── requirements.txt
├── README.md
└── venv/
```

The `venv/` directory is your local virtual environment and should generally not be committed to GitHub.

## 🧪 Testing Checklist

- [ ] Ollama starts successfully.
- [ ] The required model is available.
- [ ] Streamlit opens at `localhost:8501`.
- [ ] The chatbot returns AI-generated responses.
- [ ] Cloudflare Tunnel establishes a connection.
- [ ] The public URL opens on another device.
- [ ] The chatbot continues to respond through the public URL.

## 🔒 Security and Limitations

- The public Quick Tunnel is temporary and does not provide a permanent deployment URL.
- Anyone with access to the public link may be able to reach the exposed application unless additional access controls are configured.
- Do not enter passwords, API secrets, personal information, or confidential data into a publicly accessible demo.
- Local Ollama inference avoids the need for a paid model API, but the application still requires the host computer's resources.
- This project is intended as a learning and demonstration project, not a production-hardened service.

## 🎯 Learning Outcomes

Through this project, I explored:

- Building an interactive AI application with Streamlit
- Connecting a Python application to a local LLM
- Working with Ollama's Chat API
- Managing Python dependencies and virtual environments
- Exposing a locally running application through Cloudflare Tunnel
- Testing an AI application locally and through a public URL

## 👨‍💻 Author

**Aditya Singh**

B.Tech Student | Computer Science (Data Science)

Interested in Generative AI, Machine Learning, Python, and Data Science.

---

⭐ If you find this project useful, consider giving the repository a star.

**Note:** Replace the repository clone placeholder with your actual GitHub URL before publishing this README. Verify the dependency list and model name against your existing project.
