# Directive: Indeed job pipeline (search → tailor → submit)

Three stages, run in order. Stage 2 follows `directives/build_tailored_resumes.md`.

## Stage 1: Search (find matching jobs)
**Tool:** Indeed MCP (`search_jobs`, `get_job_details`). Runs in the cloud and needs no login.

Target profile:
- Domain: supply chain (SCM), procurement, ERP systems, plus AI automation of those processes.
- Experience: roles asking for **5+ years** in SCM, procurement or ERP. Short AI-automation experience (about 1 year) is fine.
- Skills: SQL, Python (about 1 year), an understanding of AI automation.
- Easy Apply preferred.
- Location: US roles only; candidate will work or relocate anywhere in the USA, so search "remote" and any US city.

Search queries that worked (Nov 2026): "procurement systems ERP AI automation" (remote),
"ERP procurement analyst" (remote), "supply chain systems analyst" (Ohio), "supply chain AI automation analyst" (Columbus, OH).
Long multi-keyword queries often return nothing, so use 3–4 words and run several queries in parallel.

For each hit, call `get_job_details` and screen it:
- **Keep**: posting wants procurement/SCM/ERP experience plus analytics, automation or AI.
- **Skip**: hard requirements the candidate lacks (e.g. 5 years of SAP configuration, 8 years of QAD, FAR/DFARS, security clearance).
- Note location constraints (e.g. remote limited to certain time zones).

## Stage 2: Tailor the resume
Add one profile per kept job to `tools/job_profiles.py` (next number in `folder`), then:
`python3 tools/build_resumes.py <NN> [<NN> ...]` → must print `All keywords present.`
The format matches the master resume: same sections, Calibri font, navy rules, and clickable email, LinkedIn and GitHub links.
Facts come only from `tools/base_resume.py`; unmet requirements go to `gaps`.

## Stage 3: Submit
- Needs the user's own logged-in Indeed session in Chrome (Claude in Chrome on the user's machine). A cloud session cannot log in to Indeed or drive the user's browser.
- **Get the user's confirmation for each application before clicking Submit.** An application is sent to an employer and can't be withdrawn.
- Screening answers the candidate has confirmed live in `applications/SCREENING_ANSWERS.md` (git-ignored; never commit them). Use only those; ask about anything marked ASK or missing.
- On the Easy Apply form, upload the PDF from `applications/<NN>_<company>/`, answer screening questions only with facts the user has confirmed, and stop to ask if a question isn't covered by the resume (sponsorship, salary, start date, clearance).
- After submitting, log it in the job's row of `applications/KEYWORD_MATCH_REPORT.md` or tell the user.
