# AI-Powered Resume Tailoring

This project uses the Gemini AI API to tailor résumés to specific job descriptions. It takes an input résumé in JSON format, aligns it with a job description, and outputs a tailored résumé along with a match score and a summary of improvements.

## Features

- Tailors résumés to match job descriptions using AI.
- Outputs a tailored résumé in JSON format.
- Provides match scores (before and after tailoring) and a summary of changes.
- Ensures all changes are truthful and grounded in the original résumé.

## Project Structure

```
.env                     # Environment variables (e.g., API key)
.gitignore               # Git ignore file
GeminiAiTest.py          # Main Python script
resume.json              # Input résumé in JSON format
tailored_resume.json     # Output tailored résumé in JSON format
```

## Prerequisites

- Python 3.7+
- A valid Gemini AI API key.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AyoubJebali/ResumeImproveAi.git
   cd AiTestPython
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Place the input résumé in `resume.json`.

2. Update the job description in the `GeminiAiTest.py` file:
   ```python
   job_description = """
   We are looking for a Python Developer with experience in Django and Machine Learning.
   The ideal candidate should have strong problem-solving skills and the ability to work in a team.
   """
   ```

3. Run the script:
   ```bash
   python GeminiAiTest.py
   ```

4. The tailored résumé will be saved to `tailored_resume.json`.

## Example Output

- **Match Score Before Tailoring**: 65
- **Match Score After Tailoring**: 90
- **Improvements Summary**: Reorganized bullet points, emphasized Python and Machine Learning experience, and downplayed unrelated skills.

## Notes

- The AI strictly follows the rules defined in the system prompt to ensure truthful and relevant tailoring.
- Ensure the input résumé is in valid JSON format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Gemini AI](https://www.google.com/genai) for the AI-powered résumé tailoring.
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
