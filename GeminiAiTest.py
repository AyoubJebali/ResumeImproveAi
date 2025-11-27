from google import genai
from dotenv import load_dotenv
import os
import json

# System prompt for the AI
SYSTEM_PROMPT = """
You are an expert AI specializing in résumé rewriting, HR optimization, and job-description alignment. 
Your task is to tailor an existing résumé (provided in JSON format) to a job description.

RULES (very important):
1. You MUST output ONLY valid JSON. No commentary, no explanations, no markdown.
2. You MUST NOT invent any new experience, job titles, dates, companies, or degrees.
3. You MAY rewrite wording, reorganize bullet points, and adjust phrasing to improve clarity and relevance.
4. You MUST preserve the overall structure of the original résumé unless changes significantly improve alignment.
5. You MUST emphasize achievements and skills relevant to the job description.
6. You MUST downplay or remove content irrelevant to the role, but without deleting major life events (e.g., education).
7. You MUST NOT alter factual details such as employment dates, locations, or titles.
8. You MUST ensure all rewritten content stays truthful and grounded in the original résumé.

OUTPUT FORMAT (strict):
{
  "tailored_resume": { ... },      // same structure as input unless changes are needed
  "match_score_before": number,           // 0–100 estimated alignment level before tailoring
  "match_score_after": number,           // 0–100 estimated alignment level after tailoring
  "improvements_summary": "string" // describe what was changed and why
}

Make sure the JSON is syntactically valid and contains no trailing commas.

"""

def tailor_resume_streaming(resume_json: dict, job_description: str):
    """
    Tailors a resume to match a job description using AI.

    Args:
        resume_json (dict): The original resume data in JSON format.
        job_description (str): The job description text.

    Returns:
        dict: The parsed JSON object returned by the AI.
    """
    # Combine the system prompt and user prompt into a single string
    prompt = f"""
    {SYSTEM_PROMPT}

    Here is the resume JSON:

    {json.dumps(resume_json)}

    Here is the job description:

    {job_description}

    Tailor the resume using the rules in the system prompt.
    Return JSON only.
    """

    # Request to the AI model
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt  # Pass the combined prompt as a single string
    )

    # Remove the first occurrence of the word "json" from the response
    raw_response = response.text.replace("json", "", 1).strip("`")

    # Parse the cleaned response as JSON
    try:
        result = json.loads(raw_response)
    except json.JSONDecodeError:
        print("Raw response from the model (after cleaning):")
        print(raw_response)
        raise ValueError("Model returned invalid JSON. Please check the cleaned response.")

    return result

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the client with the API key
client = genai.Client(api_key=api_key)

# Load resume data from a JSON file
input_file = "resume.json"  # Path to the input JSON file
output_file = "tailored_resume.json"  # Path to the output JSON file

try:
    # Read the resume data from the input file
    with open(input_file, "r") as file:
        resume_data = json.load(file)

    # Define the job description
    job_description = """
    We are looking for a Python Developer with experience in Django and Machine Learning.
    The ideal candidate should have strong problem-solving skills and the ability to work in a team.
    """

    # Call the function to tailor the resume
    tailored_result = tailor_resume_streaming(resume_data, job_description)

    # Save the tailored resume to the output file
    with open(output_file, "w") as file:
        json.dump(tailored_result["tailored_resume"], file, indent=4)

    print(f"Tailored resume saved to {output_file}")
    # Print the match score and improvements summary
    match_score_before = tailored_result.get("match_score_before")
    match_score_after = tailored_result.get("match_score_after")
    improvements = tailored_result.get("improvements_summary")

    if match_score_before is not None:
        print(f"Match score before tailoring: {match_score_before}")
    else:
        print("Match score before tailoring not found in the result.")

    if match_score_after is not None:
        print(f"Match score after tailoring: {match_score_after}")
    else:
        print("Match score not found in the result.")

    if improvements is not None:
        print("Improvements summary:")
        print(improvements)
    else:
        print("Improvements summary not found in the result.")
except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from the file {input_file}.")
except Exception as e:
    print(f"Error: {e}")