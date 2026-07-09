# Resume Maker AI Agent (crewAI)

made this for my AI agent assignment. it uses 3 agents to fix up a resume based on a job description.

## how it works
1. Analyzer agent - reads resume + job description, finds gaps
2. Writer agent - rewrites resume to match the job
3. Reviewer agent - polishes the final version

uses Groq (free) to run the agents, with the llama-3.3-70b model.

## how to run it

1. install the requirements:
```
pip install -r requirements.txt
```

2. get a free Groq API key:
   - go to https://console.groq.com/keys
   - sign up / log in (free, no credit card needed)
   - click "Create API Key", copy it

3. create a `.env` file in this folder (same folder as main.py / main.ipynb)
   and add your key like this:
```
GROQ_API_KEY=your_key_here
```
(there's a `.env.example` file here too, just rename it to `.env` and paste your key in)

4. put your own resume text in `resume.txt` and the job posting in `job_description.txt`
(there are sample ones already in there, just replace with your own)

5. run it:
   - for the .py file: `python main.py`
   - for the notebook: open `main.ipynb` in Jupyter and run all cells top to bottom

6. the final resume will print in the terminal/notebook and also get saved to `final_resume.txt`

## files in this project
- `main.py` / `main.ipynb` - the actual agent code (same thing, two formats)
- `utils.py` - small helper that reads the api key from .env
- `resume.txt` - your resume (input)
- `job_description.txt` - the job posting (input)
- `.env` - your api key goes here (you create this, not included for safety)
- `final_resume.txt` - gets created after you run it (output)

## notes
- Groq is free but has rate limits, if you hit one just wait a minute and try again
- if `groq/llama-3.3-70b-versatile` stops working (models get deprecated sometimes), check
  https://console.groq.com/docs/models for the current list of available model names
