# Directive: Build tailored resumes

## Goal
Produce one ATS-friendly resume (.docx + .pdf) per target job, plus a keyword-match report.

## Inputs
- `tools/base_resume.py` — source-of-truth facts. Do not add claims here unless the user supplies them.
- `tools/job_profiles.py` — one entry in `JOBS` per posting (headline, summary, competencies, `keywords`, bullet rewrites, `gaps`).

## Steps
1. For a new posting, add a profile to `JOBS` in `tools/job_profiles.py`, following the existing entries.
   - `keywords`: `(keyword, how the candidate matches it, substring that must appear in the resume)`.
   - Rewrites change wording only; every fact must trace back to a bullet in `base_resume.py`.
   - Requirements the candidate doesn't meet go in `gaps`, never on the resume.
2. Run: `python3 tools/build_resumes.py` (all jobs) or `python3 tools/build_resumes.py 09 10` (only those folders)
3. Confirm the script prints `All keywords present.` If a probe is missing, fix the profile wording (not the facts) and re-run.

## Outputs
- `applications/<NN>_<company>/` — resume .docx and .pdf
- `applications/KEYWORD_MATCH_REPORT.md`

## Dependencies / edge cases
- Keep each headline at or under about 113 characters so it fits on one line, like the master resume.
- Email, LinkedIn and GitHub in the contact line are rendered as clickable links.
- Needs `python-docx` and LibreOffice (`soffice`) on PATH for PDF conversion.
