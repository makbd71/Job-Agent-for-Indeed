# Job Agent for Indeed

Builds one tailored, ATS-friendly resume (.docx + .pdf) per job profile, plus a keyword-match report.

## Setup

Requires Python 3.10+ and LibreOffice (for the PDF step).

    python3 -m venv .venv
    source .venv/bin/activate          # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

LibreOffice: `brew install --cask libreoffice` (Mac), `sudo apt install libreoffice` (Linux),
or install from libreoffice.org (Windows; make sure `soffice` is on PATH).

## Run

    python3 tools/build_resumes.py

Output goes to `applications/` (ignored by git).

## Files

- `tools/base_resume.py` - your facts: experience, education, certifications
- `tools/job_profiles.py` - per-job headline, summary, keywords, bullet rewrites
- `tools/build_resumes.py` - builds the files and the keyword report
