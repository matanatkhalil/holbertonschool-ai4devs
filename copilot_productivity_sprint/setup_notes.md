# Setup Notes – Copilot Productivity Sprint

## 1. Development Environment

| Component | Tool | Version |
|---|---|---|
| Operating System | Windows 10 | 22H2 |
| Code Editor | Visual Studio Code | 1.146.0 |
| AI Coding Assistant | GitHub Copilot Free | Free plan |
| AI Chat Extension | Copilot SDK in VS Code | Version not exposed | 
| Version Control | Git | 2.53.0.windows.1 |
| Runtime Environment | Node.js | 24.12.0 |
| Package Manager | npm | 11.6.2 |

## 2. Installation and Configuration

### Step 1: Install Visual Studio Code

1. Download Visual Studio Code from https://code.visualstudio.com/.
2. Run the installer and follow the installation instructions.
3. Open VS Code and verify that it works correctly.

### Step 2: Install GitHub Copilot

1. Open Visual Studio Code.
2. Navigate to the Extensions panel (`Ctrl + Shift + X`).
3. Search for **GitHub Copilot**.
4. Install the official GitHub Copilot extension published by GitHub.
5. Install GitHub Copilot Chat if it is not already included.
6. Sign in using your GitHub account and authorize VS Code.
7. Verify that GitHub Copilot is enabled.

### Step 3: Configure GitHub Copilot

The following features were configured for the productivity sprint:

- **Inline Code Completions:** Provides AI-generated code suggestions while typing.
- **Copilot Chat:** Allows interaction with the AI assistant through natural-language prompts.
- **Agent Mode:** Allows Copilot to inspect the project and perform multi-file code changes.
- **Ask Mode:** Allows asking questions and receiving explanations without requesting automatic implementation.

Inline suggestions can be triggered manually using `Alt + \` on Windows.

### Step 4: Configure VS Code Settings

The following settings were checked:

- Editor: Inline Suggest Enabled.
- GitHub Copilot: Enabled.
- GitHub Copilot Chat: Available.
- GitHub account: Successfully authenticated.

### Step 5: Verify the Installation

The following checks were performed:

1. Opened a JavaScript file in VS Code.
2. Tested inline code suggestions.
3. Opened GitHub Copilot Chat.
4. Tested sending a natural-language coding prompt.
5. Verified that Copilot could suggest code modifications.

## 3. Additional Tools

| Tool | Purpose |
|---|---|
| Git | Tracking code changes and maintaining checkpoints |
| GitHub | Hosting the project repository |
| VS Code Source Control | Reviewing modified files and diffs |
| Stopwatch | Measuring task completion time |
| GitHub Copilot | AI-assisted code generation and development |

## 4. Version Verification Commands

The following commands can be executed in the VS Code integrated terminal (PowerShell) to check installed tool versions.

```powershell
# Visual Studio Code
code --version

# Git
git --version

# Node.js
node --version

# npm
npm --version
```

GitHub Copilot and GitHub Copilot Chat extension versions can be checked in the VS Code Extensions panel.

## 5. Version Control and Safety Measures

Git was used to maintain a record of project changes and provide recovery points during AI-assisted development.

The following practices are recommended:

- Create a Git commit before starting an AI-assisted task.
- Use a separate Git branch for experimental AI changes.
- Review modifications using VS Code Source Control.
- Inspect AI-generated code before accepting or committing changes.
- Run relevant tests after implementation.
- Avoid automatically approving potentially destructive terminal commands.

## 6. Conclusion

The development environment was prepared using Windows 10, Visual Studio Code, and GitHub Copilot Free.

The setup provides access to AI-powered code completion, conversational assistance, and agent-based code modifications. Git and VS Code Source Control provide tools for tracking and reviewing changes throughout the productivity sprint.
