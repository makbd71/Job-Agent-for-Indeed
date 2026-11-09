"""Build one tailored, ATS-friendly resume (.docx + .pdf) per job profile,
plus a keyword-match report.

Usage:  python3 tools/build_resumes.py            # build every job
        python3 tools/build_resumes.py 09 10      # build only folders starting with 09, 10
Output: applications/<NN>_<company>/  (resume .docx, resume .pdf)
        applications/KEYWORD_MATCH_REPORT.md
"""
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

sys.path.insert(0, str(Path(__file__).parent))
import base_resume as B  # noqa: E402
from job_profiles import JOBS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "applications"
FONT = "Calibri"
ACCENT = RGBColor(0x1F, 0x3A, 0x5F)


def _bottom_border(paragraph):
    p_pr = paragraph._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    for k, v in {"w:val": "single", "w:sz": "6", "w:space": "1", "w:color": "1F3A5F"}.items():
        bottom.set(qn(k), v)
    bdr.append(bottom)
    p_pr.append(bdr)


def _para(doc, text="", size=10, bold=False, align=None, after=0, before=0, color=None, italic=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(after)
    pf.space_before = Pt(before)
    pf.line_spacing = 1.0
    if align:
        p.alignment = align
    if text:
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.name = FONT
        if color:
            r.font.color.rgb = color
    return p


def _hyperlink(paragraph, text, url, size):
    """Append a clickable hyperlink run (blue, underlined) to a paragraph."""
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        fonts.set(qn(a), FONT)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int(size * 2)))
    for el in (fonts, color, u, sz):
        rpr.append(el)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


def _link_for(item):
    if "@" in item:
        return f"mailto:{item}"
    if item.startswith(("linkedin.com", "github.com")):
        return f"https://{item}"
    return None


def _contact_line(doc, contact, size=9):
    """Contact line with email / LinkedIn / GitHub as clickable links, like the original resume."""
    p = _para(doc, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
    for i, item in enumerate(contact.split(" | ")):
        if i:
            r = p.add_run(" | ")
            r.font.size = Pt(size)
            r.font.name = FONT
        url = _link_for(item)
        if url:
            _hyperlink(p, item, url, size)
        else:
            r = p.add_run(item)
            r.font.size = Pt(size)
            r.font.name = FONT


def _section(doc, title):
    p = _para(doc, title, size=11, bold=True, before=6, after=2, color=ACCENT)
    _bottom_border(p)


def _bullet(doc, text, size=9.5):
    p = doc.add_paragraph(style="List Bullet")
    pf = p.paragraph_format
    pf.space_after = Pt(1)
    pf.line_spacing = 1.0
    pf.left_indent = Inches(0.22)
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.name = FONT
    return p


def _role_line(doc, title, org, dates):
    p = _para(doc, before=4, after=1)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(7.3), alignment=2)  # right tab
    r1 = p.add_run(f"{title} — ")
    r1.font.bold = True
    r1.font.size = Pt(10)
    r1.font.name = FONT
    r2 = p.add_run(org)
    r2.font.size = Pt(10)
    r2.font.name = FONT
    r3 = p.add_run(f"\t{dates}")
    r3.font.size = Pt(10)
    r3.font.name = FONT
    r3.font.italic = True


def build_docx(job, path):
    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Inches(0.5)
        s.left_margin = s.right_margin = Inches(0.6)
    st = doc.styles["Normal"]
    st.font.name = FONT
    st.font.size = Pt(10)

    _para(doc, B.HEADER["name"], size=17, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, color=ACCENT)
    _para(doc, job["headline"], size=10.5, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=1)
    _contact_line(doc, B.HEADER["contact"])

    _section(doc, "PROFESSIONAL SUMMARY")
    _para(doc, job["summary"], size=9.5, after=2)

    _section(doc, "CORE COMPETENCIES")
    comps = job["competencies"]
    tbl = doc.add_table(rows=(len(comps) + 1) // 2, cols=2)
    for i, c in enumerate(comps):
        cell = tbl.cell(i // 2, i % 2)
        cell.paragraphs[0].text = ""
        r = cell.paragraphs[0].add_run(f"• {c}")
        r.font.size = Pt(9.5)
        r.font.name = FONT
        cell.paragraphs[0].paragraph_format.space_after = Pt(0)

    _section(doc, "PROFESSIONAL EXPERIENCE")
    overrides = job.get("bullet_overrides", {})
    order = job.get("bullet_order", {})
    for role in B.EXPERIENCE:
        _role_line(doc, role["title"], role["org"], role["dates"])
        ids = list(role["bullets"].keys())
        key = ids[0][:2]
        if key in order:
            ids = order[key] + [i for i in ids if i not in order[key]]
        for bid in ids:
            _bullet(doc, overrides.get(bid, role["bullets"][bid]))

    _section(doc, "EDUCATION")
    for e in B.EDUCATION:
        _bullet(doc, e)

    _section(doc, "CERTIFICATIONS & AWARDS")
    for c in B.CERTIFICATIONS:
        _bullet(doc, c)

    _section(doc, "PUBLICATIONS")
    for p in B.PUBLICATIONS:
        _bullet(doc, p)

    doc.core_properties.author = "Mohammad Anowarul Kabir"
    doc.core_properties.title = f"Resume — {job['role']} — {job['company']}"
    doc.save(path)


def to_pdf(docx_path):
    subprocess.run(
        ["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(docx_path.parent), str(docx_path)],
        check=True, capture_output=True,
    )


def resume_text(job):
    parts = [job["headline"], job["summary"], " ".join(job["competencies"])]
    for role in B.EXPERIENCE:
        for bid, txt in role["bullets"].items():
            parts.append(job.get("bullet_overrides", {}).get(bid, txt))
    parts += B.CERTIFICATIONS
    return " ".join(parts).lower()


def report(jobs):
    lines = [
        "# Keyword Match Report",
        "",
        "For each job: the top 10 keywords from the posting, how your experience matches each one, and where the "
        "keyword now appears in the tailored resume. The **Gaps** list covers requirements the resume does **not** "
        "claim because they aren't in your background. Be ready to address them in an interview or cover letter.",
        "",
    ]
    for n, job in enumerate(jobs, 1):
        text = resume_text(job)
        lines += [
            f"## {n}. {job['role']} — {job['company']}",
            "",
            f"**Location:** {job['location']} · **Pay:** {job['pay']} · **Posted:** {job['posted']}  ",
            f"**Apply:** [{job['role']}]({job['url']})  ",
            f"**Resume:** `applications/{job['folder']}/`  ",
            f"**Fit:** {job['fit']}",
            "",
            "| # | Keyword | Your matching experience | In resume? |",
            "|---|---|---|---|",
        ]
        for i, (kw, match, probe) in enumerate(job["keywords"], 1):
            present = "✅" if probe.lower() in text else "⚠️ check"
            lines.append(f"| {i} | {kw} | {match} | {present} |")
        lines += ["", "**Gaps (not claimed on the resume):** " + "; ".join(job["gaps"]), ""]
    (OUT / "KEYWORD_MATCH_REPORT.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    OUT.mkdir(exist_ok=True)
    missing = []
    only = sys.argv[1:]
    for job in JOBS:
        if only and not job["folder"].startswith(tuple(only)):
            continue
        folder = OUT / job["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        stem = f"Mohammad_Kabir_Resume_{job['file_tag']}"
        docx_path = folder / f"{stem}.docx"
        build_docx(job, docx_path)
        to_pdf(docx_path)
        text = resume_text(job)
        for kw, _, probe in job["keywords"]:
            if probe.lower() not in text:
                missing.append(f"{job['company']}: {kw} (probe '{probe}')")
        print(f"built {docx_path.relative_to(ROOT)}")
    report(JOBS)
    if missing:
        print("\nKEYWORDS NOT FOUND IN RESUME TEXT:")
        print("\n".join(missing))
        sys.exit(1)
    print("\nAll keywords present.")


if __name__ == "__main__":
    main()
