# Job Agent for Indeed — standing rules

These rules apply to every job search, resume and application for the candidate
(Mohammad Anowarul Kabir). Follow them without being reminded.

## Hard exclusions (never recommend, tailor a resume for, or apply to)
- **The candidate is NOT a U.S. citizen.** Exclude any job whose posting requires
  U.S. citizenship (e.g. "U.S. citizenship is required", "must be a U.S. citizen",
  roles needing a security clearance that only citizens can hold). Check the full
  job description with `get_job_details` before recommending a job, because the
  requirement is often only in the body text.
- Jobs that say "U.S. Person" (citizen, permanent resident, refugee or asylee) or
  "no visa sponsorship" are NOT automatically excluded. Flag them so the candidate
  can confirm their own work authorization.

## Search filters (the candidate's defaults)
- Posted within the last 24 hours.
- Easy apply process preferred.
- Salary above $90K per year.
- Target: AI automation in supply chain, procurement, marketing, or data analytics roles.

## Resume rules
- Tailor one resume per job with that posting's top 10 keywords
  (`tools/build_resumes.py`, profiles in `tools/job_profiles.py`).
- Never invent experience. Requirements the candidate lacks go in the job's `gaps`
  list, not on the resume.
- Generated resumes in `applications/` contain personal contact details and are
  git-ignored. Do not commit or push them without asking.

## Applying
- Claude cannot submit applications from this environment; the candidate applies.
