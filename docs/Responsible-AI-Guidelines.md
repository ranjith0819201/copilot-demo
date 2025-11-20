# Responsible AI Guidelines

This checklist outlines the essential practices for responsible use of AI-assisted tools such as GitHub Copilot.

---

## ✅ 1. Review and Validate AI-Generated Code
- Always manually review Copilot suggestions before accepting them.
- Check for logic errors, security risks, and performance issues.
- Verify that generated code follows project style and best practices.
- Add tests to confirm correctness of AI-generated functions.
- Do not blindly copy long or complex code blocks without understanding them.

---

## ✅ 2. Handle Sensitive Data Securely
- Never hard-code API keys, passwords, tokens, or secret URLs.
- Use environment variables (`.env`) or secret managers (GitHub Secrets, AWS Secrets Manager).
- Avoid pasting sensitive information into prompts used for AI tools.
- Ensure that AI-generated code does not log or expose private data.
- Follow encryption and data protection standards when handling personal information.

---

## ✅ 3. Acknowledge AI Contributions Ethically
- Clearly indicate when code or documentation is AI-assisted.
- Maintain transparency in commit messages when Copilot contributed (e.g., “Generated with GitHub Copilot”).
- Ensure that AI-generated code complies with open-source licenses.
- Do not claim full authorship of large AI-generated code sections.
- Use AI tools as assistants—not replacements—for human judgement.

---

## Summary
Following these guidelines ensures that AI tools are used responsibly, securely, and ethically.  
These practices protect user data, prevent legal or licensing problems, and maintain transparency in code authorship.
