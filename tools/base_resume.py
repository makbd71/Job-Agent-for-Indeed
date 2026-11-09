"""Base resume content for Mohammad Anowarul Kabir.

Every bullet has an ID so each job profile can rewrite a bullet to use that
job's keywords without changing the facts behind it.
"""

HEADER = {
    "name": "MOHAMMAD ANOWARUL KABIR",
    "contact": "Fairborn, OH (Open to Relocate) | +1 (937) 608-8115 | kabir.15@wright.edu | "
               "linkedin.com/in/anowarul-kabir-007 | github.com/makbd71",
}

EXPERIENCE = [
    {
        "title": "Supply Chain Systems Analyst (Infor FSM)",
        "org": "Premier Health, Dayton, OH",
        "dates": "Feb 2025 – Present",
        "bullets": {
            "ph1": "Extract and analyze spend and purchase price variance (PPV) data to build recurring KPI reports "
                   "for management, surfacing recurring cost issues and supporting cost-reduction decisions across a "
                   "multi-hospital health system.",
            "ph2": "Translate procurement, inventory and logistics needs into Infor FSM requirements, configuration and "
                   "enhancements; maintain item master, vendor, pricing and purchasing data.",
            "ph3": "Supported the enterprise ERP transformation from Infor Lawson to Infor FSM through data migration, "
                   "validation, system testing, go-live support and user training; wrote SOPs and support guides that "
                   "drove adoption of new procurement processes.",
            "ph4": "Write SQL against the ERP data warehouse to extract, validate and report procurement data; traced a "
                   "duplicate-record issue to a join fan-out across vendor address and location tables and resolved it.",
            "ph5": "Implement and test AI tools (Google Gemini, Claude) for supply chain planning and reporting and "
                   "prototype an agent workflow from requisition to RFQ to quote analysis to work order.",
        },
    },
    {
        "title": "Strategic Sourcing / Supply Chain Analyst (NPI Project)",
        "org": "Schneider Electric, Fairfield, OH",
        "dates": "Sep – Dec 2024",
        "bullets": {
            "se1": "Ran supplier sourcing and RFQs for OEM parts against engineering drawings, technical requirements and "
                   "cost targets; analyzed supplier quotations and cost breakdowns to support award decisions on the "
                   "Made in America (MIA) industrial automation program.",
            "se2": "Led supplier onboarding and audits across North America, integrating 35 suppliers for 75+ interior and "
                   "packaging parts and tracking readiness against quality, capacity, lead-time and delivery requirements "
                   "before production launch.",
            "se3": "Contributed to a 100% on-time delivery rate; tracked supplier KPIs (delivery, quality, compliance) and "
                   "resolved GR/IR discrepancies and blocked invoices.",
            "se4": "Partnered with Engineering, Quality, Program Management and Logistics to validate supplier readiness "
                   "and resolve commercial and delivery issues before pre-production and mass production.",
            "se5": "Recognized by Schneider Electric CEO Olivier Blum for outstanding contribution to the Made in America "
                   "project (2024).",
        },
    },
    {
        "title": "SAP MM & Supply Chain Business Analyst (Intern)",
        "org": "BWI Group (Automotive), Moraine, OH",
        "dates": "Feb – Aug 2024",
        "bullets": {
            "bw1": "Improved SAP MM and BOM data accuracy by 32%; collaborated with engineering on PLM-to-SAP data flow "
                   "and created global work instructions that standardized procurement processes.",
            "bw2": "Supported a USA-to-Mexico operations transition through SAP data migration and validation and the "
                   "setup and onboarding of suppliers for the new plant.",
            "bw3": "Analyzed material shortages, late deliveries and lead-time constraints to identify root causes and "
                   "mitigate risk, driving corrective actions with suppliers and cross-functional teams.",
            "bw4": "Used SQL and Excel for supplier data analysis and metric validation; performed cost and pricing "
                   "variance analysis to identify savings and support inventory-policy adjustments.",
        },
    },
    {
        "title": "Procurement and Supply Chain Analyst",
        "org": "Action Against Hunger, Dhaka, Bangladesh",
        "dates": "Apr 2018 – Dec 2022",
        "bullets": {
            "ah1": "Managed RFQ/RFP, competitive bid evaluation and contracting, and led supplier negotiations on pricing, "
                   "quality and delivery in time-critical environments.",
            "ah2": "Led end-to-end procure-to-pay for 15+ emergency response projects, from requisition and approvals "
                   "through delivery tracking and invoice reconciliation.",
            "ah3": "Monitored on-time delivery and contract compliance for 120+ suppliers using quality, cost and delivery "
                   "KPIs; reported trends and recommendations to leadership.",
            "ah4": "Cut lead times 29% by streamlining supplier onboarding and enforcing contract terms, while maintaining "
                   "96% procurement accuracy across categories.",
            "ah5": "Led implementation of an ERP-based procurement system replacing manual processes and automating "
                   "approval workflows (73% less paperwork).",
        },
    },
    {
        "title": "Founder",
        "org": "K&K Event Management, Dhaka, Bangladesh",
        "dates": "Aug 2017 – Dec 2022",
        "bullets": {
            "kk1": "Managed vendor sourcing, purchase negotiations and delivery logistics across 170+ events, generating "
                   "$30K in revenue while building supplier and process documentation.",
        },
    },
    {
        "title": "Financial Analyst – 401(k) Retirement Plan",
        "org": "Datapath Limited, Dhaka, Bangladesh",
        "dates": "Oct 2014 – Mar 2018",
        "bullets": {
            "dp1": "Performed financial reconciliations, variance analysis and financial modeling supporting IRS and "
                   "fiduciary compliance, building a foundation in controls, documentation and data accuracy.",
        },
    },
]

EDUCATION = [
    "M.S., Business Analytics — Wright State University, Fairborn, OH (2023 – 2025)",
    "MBA, Finance — American International University (2012 – 2014)",
    "BBA, Supply Chain Management — American International University (2008 – 2011)",
]

CERTIFICATIONS = [
    "Agentic AI — DeepLearning.AI (2026)",
    "Six Sigma Green Belt — LinkedIn (2025)",
    "Foundations of Project Management — Google (2026)",
    "Python for Data Engineering — LinkedIn Learning (2026)",
    "SAP ERP Essential Training — LinkedIn (2024); MySQL Bootcamp — Udemy (2024); "
    "Introduction to Data Analytics — Meta (2024)",
    "Supply Chain & Logistics in the Humanitarian Sector — Kühne Foundation (2021)",
    "Emerging Leader Scholarship, Wright State University (2024)",
]

PUBLICATIONS = [
    "Python for Data Analytics: A Systematic Literature Review of Tools, Techniques, and Applications — "
    "AJSTEME, 2024 (co-author)",
    "Revolutionizing Business Analytics: The Impact of Artificial Intelligence and Machine Learning — "
    "AJATES, 2025 (co-author)",
]
