# Directive: Indeed job pipeline (search → tailor → submit)

Run **once a day**. Three stages, in order. Stage 2 follows `directives/build_tailored_resumes.md`.

## Daily limit: top 10 jobs, no more

* Each daily run picks the **top 10** jobs, ranked by fit (see "Ranking" below). Never more than 10 per day.
* Only those 10 go on to Stage 2 (tailor) and Stage 3 (submit). Don't build resumes or apply for anything outside the day's 10.
* Fewer than 10 is fine if not enough postings pass screening. Don't lower the bar to fill the list.
* Skip any job already in `tools/job_profiles.py` or `applications/KEYWORD_MATCH_REPORT.md` (same company + role or same URL).
* Leftover good matches can be listed for the user as "next in line", but they are not tailored or submitted that day.

### Ranking (best first)
1. Domain match: procurement / SCM / ERP experience plus analytics, automation or AI.
2. Required years: ≤ 7 years in SCM/procurement/ERP (candidate has 7+).
3. Few gaps: no hard requirement the candidate lacks.
4. Easy Apply.
5. Freshness: newer postings first.
6. Pay, as a tie-breaker.

## Stage 1: Search (find matching jobs)
Tool: Indeed MCP (`search_jobs`, `get_job_details`). Runs in the cloud and needs no login.

Target profile:
* Domain: supply chain (SCM), procurement, ERP systems, plus AI automation of those processes.
* Experience: roles asking for 5+ years in SCM, procurement or ERP. Short AI-automation experience (about 1 year) is fine.
* Skills: SQL, Python (about 1 year), an understanding of AI automation.
* Easy Apply preferred.
* Location: US roles only; candidate will work or relocate anywhere in the USA, so search "remote" and any US city.

Search queries that worked (Nov 2026): "procurement systems ERP AI automation" (remote), "ERP procurement analyst"
(remote), "supply chain systems analyst" (Ohio), "supply chain AI automation analyst" (Columbus, OH). Long
multi-keyword queries often return nothing, so use 3–4 words and run several queries.

The Indeed MCP is rate-limited per account. If it returns "Rate limit exceeded", wait and retry; don't fire
many calls in parallel.

For each hit, call `get_job_details` and screen it:
* Keep: posting wants procurement/SCM/ERP experience plus analytics, automation or AI.
* Skip: hard requirements the candidate lacks (e.g. 5 years of SAP configuration, 8 years of QAD, FAR/DFARS,
  security clearance).
* Note location constraints (e.g. remote limited to certain time zones).

Then rank the kept jobs and take the top 10.

## Stage 2: Tailor the resume
Add one profile per selected job (max 10) to `tools/job_profiles.py` (next number in `folder`), then:
`python3 tools/build_resumes.py <NN> [<NN> ...]` → must print `All keywords present.`
The format matches the master resume: same sections, Calibri font, navy rules, and clickable email, LinkedIn and
GitHub links. Facts come only from `tools/base_resume.py`; unmet requirements go to `gaps`.

## Stage 3: Submit
* Needs the user's own logged-in Indeed session in Chrome (Claude in Chrome on the user's machine). A cloud
  session cannot log in to Indeed or drive the user's browser.
* Get the user's confirmation for each application before clicking Submit. An application is sent to an employer
  and can't be withdrawn.
* Screening answers the candidate has confirmed live in `applications/SCREENING_ANSWERS.md` (git-ignored; never
  commit them). Use only those; ask about anything marked ASK or missing.
* On the Easy Apply form, upload the PDF from `applications/<NN>_<company>/`, answer screening questions only with
  facts the user has confirmed, and stop to ask if a question isn't covered by the resume (sponsorship, salary,
  start date, clearance).
* After submitting, log it in the job's row of `applications/KEYWORD_MATCH_REPORT.md` or tell the user.
* At most 10 submissions per day, all from that day's top 10.
