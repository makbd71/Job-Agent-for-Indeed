"""Per-job tailoring: headline, summary, competencies, keyword map and bullet rewrites.

Rule: rewrites change the wording to match each posting's language, but every fact
comes from the base resume. Requirements the candidate doesn't meet go in `gaps`
and are NOT written into the resume.

keywords = (keyword, how the candidate matches it, substring that must appear in the resume)
"""

JOBS = [
    # ------------------------------------------------------------------ 1
    {
        "folder": "01_Latham_Category_Manager",
        "file_tag": "Latham_Category_Manager",
        "company": "Latham Pool Products",
        "role": "Category Manager",
        "location": "Zephyrhills, FL",
        "pay": "$67.6K – $113.4K",
        "posted": "Nov 9, 2026",
        "url": "https://to.indeed.com/aatbvxwxfzfg",
        "fit": "Strong. 7+ yrs sourcing and category work vs. 5+ required; manufacturing experience (Schneider, BWI). "
               "Negotiate toward the top of the range.",
        "headline": "Category Management & Strategic Sourcing | RFQ/RFP & Contract Negotiation | Spend Analysis & "
                    "Cost Modeling | AI & Data Analytics (SQL, Excel, Python)",
        "summary": "Category management and strategic sourcing professional with 7+ years developing sourcing strategies, "
                   "leading RFQs, RFPs and competitive bidding events, negotiating pricing, payment terms and lead "
                   "times, and managing supplier relationships across manufacturing (industrial automation, "
                   "automotive), healthcare and humanitarian supply chains. Uses spend analysis, cost modeling and "
                   "PPV reporting (SQL, Advanced Excel, Power BI, Python) to find savings, drive cost reduction and "
                   "support total cost of ownership decisions. Delivered a 29% lead-time reduction and 96% "
                   "procurement accuracy across 120+ suppliers and integrated 35 suppliers for a 100% on-time NPI "
                   "launch at Schneider Electric. M.S. Business Analytics; MBA Finance; Six Sigma Green Belt.",
        "competencies": [
            "Category Strategy & Strategic Sourcing", "RFQ / RFP & Competitive Bidding",
            "Contract Negotiation & Supplier Agreements", "Supplier Relationship Management",
            "Spend Analysis & Market/Pricing Trends", "Cost Modeling & Total Cost of Ownership",
            "Cost Reduction & Savings Tracking", "Supplier Business Reviews & Scorecards",
            "Supply Risk Mitigation & Alternative Sourcing", "New Product Introduction (NPI) Support",
            "ERP: SAP MM, Infor FSM", "AI Automation, SQL, Advanced Excel, Power BI, Python",
        ],
        "keywords": [
            ("Category strategy", "Sourcing strategies across categories at Action Against Hunger & Schneider", "category strategy"),
            ("Strategic sourcing", "7+ yrs strategic sourcing; Schneider sourcing analyst", "strategic sourcing"),
            ("RFQs / RFPs / competitive bidding", "Led RFQ/RFP and bid evaluation (AAH, Schneider)", "competitive bidding"),
            ("Contract negotiation", "Negotiated price, quality and delivery terms; contracting at AAH", "contract negotiation"),
            ("Supplier relationship management", "Managed 120+ suppliers on KPIs", "supplier relationship"),
            ("Spend analysis", "Spend & PPV analysis at Premier Health", "spend analysis"),
            ("Cost modeling / TCO", "Analyzed supplier cost breakdowns vs. cost targets", "cost model"),
            ("Cost reduction", "PPV KPI reports driving cost-reduction decisions", "cost reduction"),
            ("Supply risk mitigation", "Root-cause analysis of shortages and late deliveries; risk mitigation at BWI", "risk mitigation"),
            ("Supplier performance evaluations", "Supplier KPI scorecards (delivery, quality, compliance)", "scorecard"),
        ],
        "gaps": ["CAPEX procurement (no direct CAPEX category ownership on record)",
                 "APICS/ASCM/CPSM/CPM certification (preferred, not held; worth starting CPSM)"],
        "bullet_overrides": {
            "ph1": "Perform spend analysis and purchase price variance (PPV) analysis to build recurring KPI reports for "
                   "management, surfacing pricing trends and recurring cost issues that drive cost reduction decisions "
                   "across a multi-hospital health system.",
            "se1": "Executed the category strategy for OEM parts through supplier sourcing and RFQs against engineering "
                   "drawings, technical requirements and cost targets; built cost models from supplier quotations and "
                   "cost breakdowns to support award decisions on the Made in America (MIA) program.",
            "se3": "Contributed to a 100% on-time delivery rate; ran supplier performance scorecards (delivery, quality, "
                   "compliance) and resolved GR/IR discrepancies and blocked invoices.",
            "bw3": "Analyzed material shortages, late deliveries and lead-time constraints to identify root causes; drove "
                   "supply risk mitigation and corrective actions with suppliers and cross-functional teams.",
            "ah1": "Led strategic sourcing through RFQ/RFP and competitive bidding events, bid evaluation and contract "
                   "negotiation on pricing, payment terms, quality and delivery in time-critical environments.",
            "ah3": "Managed supplier relationships and contract compliance for 120+ suppliers using quality, cost and "
                   "delivery KPIs; reported trends and recommendations to leadership.",
        },
    },
    # ------------------------------------------------------------------ 2
    {
        "folder": "02_Anduril_Product_Sourcing_Engineer",
        "file_tag": "Anduril_Product_Sourcing_Engineer",
        "company": "Anduril Industries",
        "role": "Product Sourcing Engineer, Fury",
        "location": "Ashville, OH (onsite)",
        "pay": "$114K – $152K + equity",
        "posted": "Nov 8, 2026",
        "url": "https://to.indeed.com/aa7rwwz6x4mh",
        "fit": "Stretch. Sourcing, production-ramp and BOM experience match well; composites and AS9100/AS9102 "
               "domain experience is the main gap.",
        "headline": "Product Sourcing & Supplier Development | Production Ramp & BOM Risk | Should-Cost Analysis | "
                    "AI & Data Analytics (SQL, Python)",
        "summary": "Sourcing and supply chain professional with 7+ years in supplier selection, supplier development and "
                   "cost engineering for manufacturing programs in industrial automation and automotive. At Schneider "
                   "Electric, ran RFQs against engineering drawings and cost targets, used supplier cost breakdowns for "
                   "should-cost comparisons, and onboarded 35 suppliers for 75+ parts with capacity and rate-readiness "
                   "checks before production ramp, contributing to 100% on-time delivery. Brings manufacturing BOM "
                   "data accuracy (+32% at BWI), BOM risk assessment and alternate sourcing, and lead-time reduction "
                   "(29%). Works cross-functionally with Engineering, Quality and Manufacturing, and uses SQL, Python "
                   "and AI agents to automate sourcing analysis. M.S. Business Analytics; Six Sigma Green Belt.",
        "competencies": [
            "Supplier Selection & Qualification", "Should-Cost / Cost Breakdown Analysis",
            "Production Ramp & Rate Readiness", "Supplier Capacity Planning",
            "Manufacturing BOM Development & Accuracy", "BOM Risk Assessment & Alternate Sourcing",
            "Lead-Time Reduction & Value-Stream Thinking", "Supplier Development & Audits",
            "Statements of Work & Technical Requirements", "Engineering / Quality / Manufacturing Partnership",
            "ERP & PLM: SAP MM, Infor FSM", "SQL, Python, AI Agent Automation",
        ],
        "keywords": [
            ("Supplier selection", "Selected and awarded suppliers for OEM parts at Schneider", "supplier selection"),
            ("Should-cost / clean-sheet models", "Compared supplier cost breakdowns to cost targets", "should-cost"),
            ("Production ramp / rate readiness", "Validated supplier readiness before pre-production and mass production", "rate-readiness"),
            ("Capacity planning", "Tracked supplier capacity and lead time before launch", "capacity"),
            ("Manufacturing BOM", "Improved SAP MM and BOM data accuracy 32% at BWI", "bom"),
            ("BOM risk assessment & alternate sourcing", "Shortage root-cause analysis and supplier risk mitigation at BWI", "alternate sourcing"),
            ("Supplier qualification", "Supplier onboarding and audits across North America", "qualification"),
            ("Lead-time optimization", "Cut lead times 29% at AAH", "lead time"),
            ("Cross-functional (Engineering, Quality, Manufacturing)", "Partnered with Engineering, Quality and Program Management", "engineering, quality"),
            ("Total cost of ownership / cost engineering", "Cost and pricing variance analysis; PPV reporting", "total cost"),
        ],
        "gaps": ["Composite manufacturing domain (layup, cure, NDI)", "AS9100 suppliers / AS9102 First Article Inspection",
                 "Tooling CAPEX management", "Secret clearance eligibility (preferred)"],
        "bullet_order": {"se": ["se1", "se2", "se4", "se3", "se5"]},
        "bullet_overrides": {
            "se1": "Led supplier selection and RFQs for OEM parts against engineering drawings, technical requirements and "
                   "cost targets; used supplier quotations and cost breakdowns for should-cost comparisons supporting "
                   "award decisions on the Made in America (MIA) industrial automation program.",
            "se2": "Drove supplier qualification, onboarding and audits across North America, integrating 35 suppliers for "
                   "75+ parts and checking capacity, rate-readiness, quality, lead time and delivery before production "
                   "ramp.",
            "se4": "Partnered with Engineering, Quality, Manufacturing/Program Management and Logistics to validate supplier "
                   "readiness and resolve commercial and delivery issues before pre-production and mass production.",
            "bw1": "Improved SAP MM and manufacturing BOM data accuracy by 32%; collaborated with engineering on PLM-to-SAP "
                   "BOM data flow and created global work instructions that standardized procurement processes.",
            "bw3": "Performed BOM risk assessment on material shortages, late deliveries and lead-time constraints; "
                   "identified root causes and drove corrective actions and alternate sourcing with suppliers.",
            "bw4": "Used SQL and Excel for supplier data analysis; performed cost and pricing variance analysis supporting "
                   "total cost and inventory-policy decisions.",
        },
    },
    # ------------------------------------------------------------------ 3
    {
        "folder": "03_Lineage_Sr_Business_Analyst_AI_COE",
        "file_tag": "Lineage_Sr_Business_Analyst_AI_COE",
        "company": "Lineage",
        "role": "Senior Business Analyst (AI COE)",
        "location": "Remote",
        "pay": "$97.2K – $136.6K",
        "posted": "Nov 1, 2026",
        "url": "https://to.indeed.com/aap7cfgqqxkw",
        "fit": "Excellent. They want a supply chain domain expert who maps workflows and feeds AI builds; that's "
               "your requisition-to-RFQ agent work. No visa sponsorship.",
        "headline": "Business Analyst — AI Automation & Process Improvement | Supply Chain & Procurement Domain Expert | "
                    "SQL · Python · Agentic AI",
        "summary": "Business analyst and supply chain domain expert with 7+ years of experience improving procurement, "
                   "inventory and logistics processes. Maps current-state workflows, finds manual steps, handoffs and "
                   "delays, and turns them into well-scoped requirements and AI automation opportunities. At Premier "
                   "Health, translates business needs into ERP requirements, supported user acceptance testing and "
                   "go-live, and prototyped an AI agent workflow (Claude, Gemini) from requisition to RFQ to quote "
                   "analysis. Builds business cases and ROI analyses with SQL, Excel and Python, led an approval-"
                   "workflow automation that cut paperwork 73%, and drives adoption through SOPs and training. Six Sigma "
                   "Green Belt; Agentic AI (DeepLearning.AI); M.S. Business Analytics.",
        "competencies": [
            "AI Automation & Agentic Workflows", "Business Analysis & Requirements Documentation",
            "Current-State Process Mapping", "Workflow Automation Opportunity Scoping",
            "Business Case & ROI Analysis", "User Acceptance Testing (UAT) & Go-Live",
            "Adoption, Training & SOPs", "Stakeholder Management (Technical & Executive)",
            "Lean / Six Sigma Process Improvement", "Data Analysis: SQL, Python, Excel, Power BI, Tableau",
            "Supply Chain, Procurement & Logistics Domain", "ERP: Infor FSM, SAP MM",
        ],
        "keywords": [
            ("AI Center of Excellence / AI automation", "Prototyped AI agent workflow; implement AI tools at Premier", "ai automation"),
            ("Business analysis", "Supply Chain Systems Analyst; SAP MM Business Analyst", "business analys"),
            ("Current-state process mapping", "Mapped procurement workflows for ERP transformation", "current-state"),
            ("Workflow automation", "Automated approval workflows (73% less paperwork)", "workflow"),
            ("Requirements documentation", "Translate needs into Infor FSM requirements", "requirements"),
            ("Business case & ROI analysis", "Built business case for sourcing decisions; cost-savings quantification", "roi"),
            ("User acceptance testing", "System testing and go-live support for Lawson→FSM", "user acceptance testing"),
            ("Adoption & training", "User training and SOPs that drove adoption", "adoption"),
            ("Stakeholder management", "Cross-functional work with Engineering, Quality, leadership", "stakeholder"),
            ("Lean / Six Sigma", "Six Sigma Green Belt; DMAIC", "six sigma"),
        ],
        "gaps": ["Jira / Asana / Aha! (preferred; worth a free Jira course)",
                 "Formal AI CoE membership (the prototype is your proof; describe it concretely)"],
        "bullet_order": {"ph": ["ph5", "ph2", "ph3", "ph1", "ph4"]},
        "bullet_overrides": {
            "ph5": "Drive AI automation for supply chain: implement and test AI tools (Google Gemini, Claude) for planning "
                   "and reporting, and prototyped an agentic workflow from requisition to RFQ to quote analysis to work "
                   "order, scoping where AI assists and where humans review.",
            "ph2": "Map current-state procurement, inventory and logistics workflows and translate pain points into "
                   "documented Infor FSM requirements, configuration and enhancements; maintain item master, vendor and "
                   "pricing data.",
            "ph3": "Supported the enterprise ERP transformation (Infor Lawson to FSM) through data migration, validation, "
                   "user acceptance testing, go-live support and user training; wrote SOPs that drove adoption of new "
                   "procurement processes.",
            "ph1": "Build recurring spend and PPV KPI reporting that quantifies value and cost issues for leadership, "
                   "supporting ROI-based cost-reduction decisions across a multi-hospital system.",
            "se4": "Managed stakeholder relationships across Engineering, Quality, Program Management and Logistics to "
                   "validate supplier readiness and resolve issues before production launch.",
            "ah5": "Led an ERP-based procurement system implementation that replaced manual processes and automated "
                   "approval workflows, cutting paperwork 73%.",
        },
    },
    # ------------------------------------------------------------------ 5
    {
        "folder": "05_Nortek_Electronics_Category_Manager",
        "file_tag": "Nortek_Electronics_Category_Manager",
        "company": "Nortek Data Center Cooling",
        "role": "Electronics Category Manager",
        "location": "Columbus, OH",
        "pay": "$87.8K – $126.2K",
        "posted": "Nov 6, 2026",
        "url": "https://to.indeed.com/aap2fwxlmpc9",
        "fit": "Good. Category, NPI, BOM, ERP/PLM and supplier-scorecard experience match; electronics components and "
               "UL 508A panel shops are the gaps. Apply through nortekdatacenter.com/careers.",
        "headline": "Category Management & Strategic Sourcing | NPI & BOM Standardization | Supplier Scorecards & "
                    "Cost Reduction | ERP/PLM Data | SQL · AI Automation",
        "summary": "Category and sourcing professional with 7+ years developing category strategies, qualifying and "
                   "negotiating with OEM suppliers, and managing supplier performance through KPIs and scorecards in "
                   "industrial automation (Schneider Electric), automotive (BWI) and healthcare. Partners with "
                   "Engineering on new product introductions, improved BOM and ERP/PLM master data accuracy by 32%, "
                   "and manages lead-time and supply risk through root-cause analysis and second sourcing. Builds "
                   "cost-reduction pipelines from spend and PPV data using SQL, Excel and AI automation. M.S. Business "
                   "Analytics; Six Sigma Green Belt.",
        "competencies": [
            "Category Strategy & Ownership", "Approved Vendor List (AVL) & Supplier Segmentation",
            "New Product Introduction (NPI)", "BOM Standardization & Costed BOMs",
            "Supplier Qualification (OEMs & Distributors)", "Supplier Scorecards & QBRs",
            "Cost-Reduction Pipeline & YoY Savings", "Lead-Time, Supply Risk & Second Sourcing",
            "ERP & PLM Master Data (SAP MM, Infor FSM)", "Negotiation & Commercial Agreements",
            "SQL, Advanced Excel, Power BI", "AI Automation for Sourcing Analytics",
        ],
        "keywords": [
            ("Category strategy", "Sourcing strategy for OEM parts at Schneider", "category strateg"),
            ("Approved Vendor List (AVL)", "Maintain vendor master data in Infor FSM; supplier onboarding", "approved vendor"),
            ("New product introduction (NPI)", "Schneider NPI program, 35 suppliers", "npi"),
            ("BOM standardization", "BOM accuracy +32%, global work instructions at BWI", "bom"),
            ("Supplier qualification (OEMs)", "Onboarding and audits across North America", "qualif"),
            ("Supplier scorecards / QBRs", "Supplier KPIs: delivery, quality, compliance", "scorecard"),
            ("Cost reduction / YoY savings", "PPV analysis and savings identification", "cost-reduction"),
            ("Lead-time & supply risk / second sourcing", "29% lead-time cut; shortage root-cause analysis", "second sourcing"),
            ("ERP & PLM master data", "PLM-to-SAP data flow; Infor FSM item/vendor master", "plm"),
            ("Negotiation & commercial agreements", "Negotiated pricing and terms at AAH; contracting", "commercial"),
        ],
        "gaps": ["Electrical/electronic components category (low-voltage, panels)", "UL 508A panel shops",
                 "EOL / last-time-buy management (adjacent to shortage risk work; don't overclaim)"],
        "bullet_overrides": {
            "se1": "Executed the category strategy for OEM parts on an NPI program: sourced and ran RFQs against engineering "
                   "drawings, technical requirements and cost targets, and analyzed costed quotations to support awards.",
            "se2": "Led supplier qualification, onboarding and audits across North America, adding 35 OEM suppliers for 75+ "
                   "parts to the approved vendor base and tracking quality, capacity, lead time and delivery.",
            "se3": "Contributed to a 100% on-time delivery rate; ran supplier scorecards (delivery, quality, compliance) and "
                   "resolved GR/IR discrepancies and blocked invoices.",
            "bw1": "Improved SAP MM and BOM data accuracy by 32%; collaborated with engineering on PLM-to-SAP data flow and "
                   "wrote global work instructions that drove BOM standardization.",
            "bw3": "Monitored lead-time constraints, shortages and late deliveries; identified root causes and drove "
                   "corrective actions and second sourcing to mitigate supply risk.",
            "ph1": "Analyze spend and PPV data to build KPI reports and a cost-reduction pipeline of recurring cost issues "
                   "for management across a multi-hospital system.",
            "ah1": "Managed RFQ/RFP, bid evaluation and commercial agreements; led supplier negotiations on pricing, "
                   "quality and delivery in time-critical environments.",
        },
    },
    # ------------------------------------------------------------------ 6
    {
        "folder": "06_Raytheon_Principal_Specialist_Procurement",
        "file_tag": "Raytheon_Principal_Specialist_Procurement",
        "company": "Raytheon (RTX)",
        "role": "Principal Specialist, Procurement",
        "location": "Remote (US-TX)",
        "pay": "$86.8K – $165.2K",
        "posted": "Nov 6, 2026",
        "url": "https://to.indeed.com/aabvpq79yy8l",
        "fit": "Moderate. Negotiation, price analysis and SAP match. Hard requirements: **U.S. citizenship** and "
               "DoD/FAR/DFARS/ITAR experience. Apply only if you're a U.S. citizen.",
        "headline": "Procurement & Supplier Negotiations | Cost/Price & Best-Value Analysis | Source Selection | "
                    "SAP Procurement | Data & AI Analytics",
        "summary": "Procurement professional with 7+ years leading supplier negotiations on pricing, schedules and terms "
                   "and conditions, performing cost/price and best-value analysis, and running source selection through "
                   "RFQ/RFP events. Experienced with purchase order management and procure-to-pay in SAP MM and Infor "
                   "FSM, supplier due diligence and qualification, and post-award supplier performance management "
                   "for 120+ suppliers. Has worked in regulated, compliance-driven settings (healthcare, "
                   "humanitarian donor-funded procurement, IRS/fiduciary compliance). Partners with Engineering, Quality, "
                   "Program Management and senior leadership to meet program milestones. M.S. Business Analytics; "
                   "MBA Finance.",
        "competencies": [
            "Supplier Negotiations: Price, Schedule, T&Cs", "Cost / Price & Best-Value Analysis",
            "Source Selection & Award Justification", "Supplier Due Diligence & Qualification",
            "Purchase Order Management & Procure-to-Pay", "Post-Award Supplier Performance",
            "Technical Requirements & Statements of Work Review", "Procurement Policy & Contract Compliance",
            "SAP MM Procurement, Infor FSM", "Cross-Functional & Senior Leadership Engagement",
            "SQL, Advanced Excel, Power BI", "AI Automation for Quote Analysis",
        ],
        "keywords": [
            ("Supplier negotiations (price, schedule, T&Cs)", "Led negotiations on pricing, quality and delivery at AAH", "terms and conditions"),
            ("Cost / price analysis", "Cost breakdowns, PPV, pricing variance analysis", "cost/price"),
            ("Best-value analysis", "Bid evaluation across price, quality and delivery", "best-value"),
            ("Source selection / justification", "Award decisions from quotation analysis (Schneider)", "source selection"),
            ("Supplier due diligence & qualification", "Supplier onboarding and audits", "due diligence"),
            ("Purchase order management", "End-to-end procure-to-pay for 15+ projects", "purchase order"),
            ("Post-award supplier performance", "On-time delivery & contract compliance KPIs, 120+ suppliers", "post-award"),
            ("Statements of Work (SOW) review", "Sourced against engineering drawings and technical requirements", "statements of work"),
            ("Procurement compliance", "Contract compliance; donor/IRS compliance background", "compliance"),
            ("SAP procurement tools", "SAP MM at BWI; Infor FSM", "sap mm"),
        ],
        "gaps": ["U.S. citizenship (required by this program)", "DoD procurement & FAR/DFARS, ITAR compliance",
                 "SAP PRISM / APEX", "Drafting NDAs and Proprietary Information Agreements"],
        "bullet_overrides": {
            "ah1": "Managed RFQ/RFP source selection, best-value bid evaluation and contracting; led supplier negotiations "
                   "on pricing, schedules, quality and terms and conditions in time-critical environments.",
            "ah2": "Led end-to-end procure-to-pay and purchase order management for 15+ emergency response projects, from "
                   "requisition and approvals through delivery tracking and invoice reconciliation.",
            "ah3": "Owned post-award supplier performance and contract compliance for 120+ suppliers using quality, cost "
                   "and delivery KPIs; reported trends and recommendations to leadership.",
            "se1": "Reviewed engineering drawings, technical requirements and statements of work for OEM parts; ran RFQs "
                   "and cost/price analysis of supplier quotations and cost breakdowns to support source selection.",
            "se2": "Conducted supplier due diligence, qualification audits and onboarding across North America, integrating "
                   "35 suppliers for 75+ parts against quality, capacity, lead-time and delivery requirements.",
        },
    },
    # ------------------------------------------------------------------ 7
    {
        "folder": "07_Dine_Development_Pricing_Manager",
        "file_tag": "DDC_Pricing_Manager",
        "company": "Diné Development Corporation",
        "role": "Pricing Manager",
        "location": "Dayton, OH",
        "pay": "$94.6K – $145.5K",
        "posted": "Nov 6, 2026",
        "url": "https://to.indeed.com/aaxtkvpcsd9f",
        "fit": "Low probability. Requires 10+ yrs GovCon and 5+ yrs federal proposal pricing. Your Excel modeling and "
               "AI-workflow experience are real pluses. Apply as a long shot or ask about a Pricing Analyst role.",
        "headline": "Pricing & Cost Analysis | Advanced Excel Financial Modeling | Scenario Analysis | "
                    "AI-Enabled Workflows & Agents | MBA Finance",
        "summary": "Pricing, cost and financial analyst with 7+ years in cost/price analysis, competitive bid "
                   "evaluation and financial modeling across procurement, healthcare and financial services. Builds "
                   "auditable Advanced Excel models with documented assumptions, scenario and sensitivity analysis, "
                   "and price benchmarking, and turns them into executive-ready recommendations. Analyzes RFP "
                   "solicitations from both buyer and supplier sides, keeps audit-ready documentation built on controls "
                   "and compliance, and develops AI-enabled workflows and agents (Claude, Gemini) for research, quote "
                   "comparison and analysis with human validation. MBA Finance; M.S. Business Analytics.",
        "competencies": [
            "Pricing Models & Cost/Price Analysis", "Advanced Excel: Scenario & Sensitivity Analysis",
            "Price Benchmarking & Competitive Analysis", "RFP / Solicitation Analysis",
            "Executive Recommendations & Summaries", "Audit-Ready Documentation & Version Control",
            "Compliance & Controls", "Templates, Checklists & SOPs",
            "AI-Enabled Workflows & Agents", "Financial Modeling & Variance Analysis",
            "SQL, Python, Power BI", "Cross-Functional Partnership (Finance, Contracts, Ops)",
        ],
        "keywords": [
            ("Pricing models", "Cost/pricing variance analysis; PPV models", "pricing model"),
            ("Advanced Excel modeling", "Advanced Excel daily", "advanced excel"),
            ("Scenario / sensitivity analysis", "Award-scenario comparison in bid evaluation", "scenario"),
            ("Cost / price analysis", "Supplier cost breakdowns; PPV", "cost/price"),
            ("RFP / solicitation analysis", "Ran RFQ/RFP events and bid evaluation", "solicitation"),
            ("Price-to-Win / competitive benchmarking", "Price benchmarking of supplier bids", "benchmark"),
            ("Executive recommendations", "KPI reports and recommendations to leadership", "executive"),
            ("AI-enabled workflows / agents", "Agent prototype requisition→RFQ→quote analysis", "agent"),
            ("Compliance & audit-ready files", "IRS/fiduciary compliance, controls, documentation", "audit-ready"),
            ("Templates, checklists, playbooks", "SOPs, global work instructions", "sop"),
        ],
        "gaps": ["10+ yrs GovCon / 5+ yrs federal proposal pricing", "FAR/DFARS, GSA MAS, IDIQ, Cost/Price Volumes, BOEs",
                 "Formal people management of pricing analysts", "JAMIS / DCAA estimating systems"],
        "bullet_overrides": {
            "ph1": "Build Excel and SQL pricing models of spend and purchase price variance (PPV) data, producing recurring "
                   "KPI reports and executive recommendations that support cost-reduction decisions.",
            "ph5": "Develop AI-enabled workflows and agents (Google Gemini, Claude) for research and reporting; prototyped "
                   "an agent from requisition to RFQ to quote analysis with human validation of outputs.",
            "ph3": "Supported the Infor Lawson to FSM transformation through data validation, testing and go-live; wrote "
                   "SOPs, checklists and support guides that standardized processes and cut rework.",
            "se1": "Ran RFQs and cost/price analysis of supplier quotations and cost breakdowns against cost targets, "
                   "comparing award scenarios for the Made in America (MIA) program.",
            "ah1": "Analyzed RFQ/RFP solicitations and ran competitive bid evaluation, benchmark price comparison and "
                   "contracting; led supplier negotiations in time-critical environments.",
            "dp1": "Built financial models and performed variance analysis and reconciliations supporting IRS and "
                   "fiduciary compliance; kept audit-ready files with strong controls and documentation.",
        },
    },
    # ------------------------------------------------------------------ 8
    {
        "folder": "08_Commons_Clinic_AI_Enabled_Operations",
        "file_tag": "Commons_Clinic_AI_Enabled_Operations",
        "company": "Commons Clinic",
        "role": "Business Operations Associate, AI-Enabled Operations",
        "location": "Remote",
        "pay": "$95K – $110K",
        "posted": "Oct 28, 2026",
        "url": "https://to.indeed.com/aabrnq79tvg6",
        "fit": "Strong AI fit, and they say 'apply even if not 100% qualified'. Healthcare operations background "
               "(Premier Health). They ask for 2–4 yrs, so frame the role as moving deliberately into AI operations.",
        "headline": "AI-Enabled Operations | Process Redesign & Workflow Automation | Claude / Agentic AI | "
                    "Healthcare Operations Analytics | SQL · Excel · Power BI",
        "summary": "Operations and analytics professional who takes a process apart step by step and decides what to "
                   "eliminate, automate, AI-assist or keep human. Led an approval-workflow redesign that automated a "
                   "manual process and cut paperwork 73%, reduced lead times 29%, and now builds AI-assisted "
                   "workflows with Claude and Gemini, using structured prompting, reusable instructions and human "
                   "review checkpoints, including an agent prototype from requisition to RFQ to quote analysis at "
                   "Premier Health. Builds executive roll-ups and dashboards from messy ERP data with SQL, Advanced "
                   "Excel and Power BI, works in regulated, deadline-critical healthcare operations, and documents "
                   "workflows as playbooks so they run without one person. Agentic AI (DeepLearning.AI); M.S. "
                   "Business Analytics.",
        "competencies": [
            "AI-Driven Process Redesign", "Workflow Automation (Eliminate / Automate / AI-Assist)",
            "Claude & ChatGPT: Structured Prompting", "Human Review Checkpoints & Output Validation",
            "Measuring Impact: Cycle Time, Error Rates, Hours Saved", "Executive Roll-Ups & Dashboards",
            "Advanced Excel & Google Sheets", "SQL, Power BI, Tableau, Python",
            "Playbooks, SOPs & Workflow Documentation", "Healthcare Operations (Multi-Hospital System)",
            "Vendor & Deadline Management", "Messy Data Cleanup & Validation",
        ],
        "keywords": [
            ("AI-driven process redesign", "Agent workflow prototype; ERP workflow redesign", "process redesign"),
            ("Workflow automation", "Automated approval workflows, 73% less paperwork", "automat"),
            ("Claude / ChatGPT, structured prompting", "Implement and test Claude & Gemini at Premier", "structured prompting"),
            ("Human review & output validation", "Data validation, testing; human checkpoints in agent design", "human review"),
            ("Measurable results (cycle time, errors)", "29% lead-time cut, 96% accuracy, 73% less paperwork", "cycle time"),
            ("Executive roll-ups & dashboards", "Recurring KPI reports for management", "dashboard"),
            ("Advanced Excel / Google Sheets", "Daily Excel use", "advanced excel"),
            ("SQL / BI tools (Tableau, Power BI)", "SQL against ERP warehouse; Power BI, Tableau", "power bi"),
            ("Documented workflows & playbooks", "SOPs, support guides, global work instructions", "playbook"),
            ("Healthcare / regulated operations", "Premier Health multi-hospital system", "healthcare"),
        ],
        "gaps": ["Revenue cycle, medical billing, payer/claims operations (they will teach it)",
                 "No-code automation tools (Zapier/Make/n8n): build one small workflow before interviewing"],
        "bullet_order": {"ph": ["ph5", "ph4", "ph1", "ph3", "ph2"]},
        "bullet_overrides": {
            "ph5": "Build AI-assisted workflows with Claude and Google Gemini using structured prompting and reusable "
                   "instructions; prototyped an agentic process redesign from requisition to RFQ to quote analysis to "
                   "work order, with human review checkpoints to validate AI outputs.",
            "ph4": "Write SQL against the ERP data warehouse to pull, clean and validate messy procurement data; traced a "
                   "duplicate-record issue to a join fan-out across vendor tables and fixed it, removing reporting errors.",
            "ph1": "Build executive KPI roll-ups and dashboards on spend and purchase price variance (PPV), surfacing "
                   "recurring cost issues and bottlenecks across a multi-hospital healthcare system.",
            "ph3": "Supported the Infor Lawson to FSM transformation (data migration, validation, testing, go-live, "
                   "training); wrote SOPs and playbooks so new procurement processes run without depending on one person.",
            "ah4": "Redesigned supplier onboarding and enforced contract terms, cutting lead-time cycle time 29% while "
                   "keeping 96% procurement accuracy.",
            "ah5": "Led a process redesign that replaced manual paperwork with an ERP-based procurement system and "
                   "automated approval workflows (73% less paperwork).",
        },
    },
    # ------------------------------------------------------------------ 9
    {
        "folder": "09_Symbotic_NPI_Procurement_Manager",
        "file_tag": "Symbotic_NPI_Procurement_Manager",
        "company": "Symbotic",
        "role": "NPI Procurement Manager",
        "location": "Remote (Wilmington, MA)",
        "pay": "$104,250 - $152,900",
        "posted": "Nov 12, 2026",
        "url": "https://to.indeed.com/aa89yx8pygzf",
        "fit": "Strong. NPI sourcing with Engineering and Program Management at Schneider Electric (industrial "
               "automation), 7+ yrs procurement, SAP and Advanced Excel. Aftersales/spare-parts sourcing is the gap. "
               "Easy Apply; asks about sponsorship (answer Yes, F-1 OPT).",
        "headline": "NPI Procurement & Strategic Sourcing | Engineering & Program Management Partnership | "
                    "Cost Model Support | PO Execution | SAP MM, Advanced Excel",
        "summary": "Procurement professional with 7+ years in sourcing, supplier management and new product "
                   "introduction (NPI) support for manufacturing programs in industrial automation and automotive. At "
                   "Schneider Electric, ran sourcing and RFQs against engineering drawings and cost targets, "
                   "analyzed supplier quotations and cost breakdowns, and onboarded 35 suppliers for 75+ parts with "
                   "readiness tracking before production launch, contributing to 100% on-time delivery. Works "
                   "daily with Engineering, Quality, Program Management and Logistics to manage supply risk and "
                   "keep purchase order execution on schedule. Uses SAP MM, Infor FSM, SQL and Advanced Excel to "
                   "report cost and schedule status. M.S. Business Analytics; Six Sigma Green Belt.",
        "competencies": [
            "NPI Procurement & Sourcing Plans", "Strategic Sourcing & Category Strategy",
            "Engineering & Program Management Partnership", "Purchase Order Execution & Delivery Tracking",
            "Cost Model Support & Supplier Quote Analysis", "Supply & Financial Risk Escalation",
            "Supplier Onboarding & Qualification", "Managing Multiple Concurrent Programs",
            "Program Status Reporting (Cost, Schedule, Risk)", "Supplier Relationship Management",
            "ERP/MRP: SAP MM, Infor FSM", "Advanced Excel, SQL, Power BI",
        ],
        "keywords": [
            ("NPI / new product development", "Schneider Electric NPI project", "npi"),
            ("Sourcing strategy / sourcing plans", "Sourcing and RFQs at Schneider; strategic sourcing at AAH", "sourcing plans"),
            ("Engineering and program management partnership", "Worked with Engineering, Quality, Program Mgmt at Schneider", "program management"),
            ("Purchase order execution", "P2P for 15+ projects; PO and delivery tracking", "purchase order"),
            ("Cost model / should-cost", "Analyzed supplier quotations and cost breakdowns", "cost breakdowns"),
            ("Risk identification and escalation", "Root-cause and risk mitigation at BWI; supplier readiness at Schneider", "risk"),
            ("Multiple concurrent programs", "15+ concurrent response projects at AAH", "concurrent"),
            ("Category management", "Sourcing across categories", "category strategy"),
            ("ERP/MRP (SAP preferred)", "SAP MM at BWI; Infor FSM at Premier", "sap mm"),
            ("Advanced Excel", "Daily Excel use", "advanced excel"),
        ],
        "gaps": ["Aftersales and spare-parts (RSPL) sourcing, warranty exposure (not on record)",
                 "Robotics / material handling industry experience (closest: industrial automation at Schneider)",
                 "Approved Vendor List (AVL) ownership during design (supplier onboarding is the closest match)"],
        "bullet_order": {"se": ["se1", "se4", "se2", "se3", "se5"]},
        "bullet_overrides": {
            "se1": "Supported NPI sourcing for the Made in America (MIA) industrial automation program: ran supplier "
                   "sourcing and RFQs against engineering drawings, technical requirements and cost targets, and "
                   "analyzed supplier quotations and cost breakdowns to support award decisions.",
            "se4": "Partnered with Engineering, Quality, Program Management and Logistics to validate supplier "
                   "readiness and resolve commercial and delivery issues before pre-production and mass production.",
            "se3": "Contributed to a 100% on-time delivery rate by tracking purchase order delivery and supplier KPIs "
                   "(delivery, quality, compliance); resolved GR/IR discrepancies and blocked invoices.",
            "ah2": "Managed 15+ concurrent emergency response projects end to end, from requisition and approvals "
                   "through purchase order execution, delivery tracking and invoice reconciliation.",
            "ph1": "Extract and analyze spend and purchase price variance (PPV) data to build recurring KPI reports "
                   "for management, surfacing recurring cost issues and supporting cost-reduction decisions across a "
                   "multi-hospital health system.",
        },
    },
]
