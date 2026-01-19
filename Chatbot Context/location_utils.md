# Location Utils Context

## Ambiguous Locations (Disambiguation Required)

When these locations are mentioned without "city" or "state" qualifier, clarification is needed:

| Location | Clarification Question |
|----------|----------------------|
| Arkansas | Do you mean Arkansas State or Arkansas City? |
| California | Do you mean California State or California City? |
| Delaware | Do you mean Delaware State or Delaware City? |
| Florida | Do you mean Florida State or Florida City? |
| Indiana | Do you mean Indiana State or Indiana City? |
| Iowa | Do you mean Iowa State or Iowa City? |
| Kansas | Do you mean Kansas State or Kansas City? |
| Louisiana | Do you mean Louisiana State or Louisiana City? |
| Michigan | Do you mean Michigan State or Michigan City? |
| Missouri | Do you mean Missouri State or Missouri City? |
| Nebraska | Do you mean Nebraska State or Nebraska City? |
| Nevada | Do you mean Nevada State or Nevada City? |
| New York | Do you mean New York State or New York City? |
| Oklahoma | Do you mean Oklahoma State or Oklahoma City? |
| Oregon | Do you mean Oregon State or Oregon City? |
| Texas | Do you mean Texas State or Texas City? |
| Washington | Do you mean Washington State or Washington City? |
| Wyoming | Do you mean Wyoming State or Wyoming City? |

---

## Query Classification Rules

### 1. General Question (Descriptive)
- Direct, factual, or descriptive requests seeking specific data points or rankings
- Questions asking for top/bottom performers, specific metrics, or factual information
- Questions that can be answered with data retrieval without needing causal analysis
- Examples:
  - "What is the gross sales?"
  - "Show me the top 5 products leading to the decline in sales"
  - "Give me the total trade investment for H1 2025"
  - "Which retailer experienced the largest decline in gross sales in June 2025 compared to the previous month?"
  - "Who are the top 5 performers in Q2 2025?"
  - "What are the bottom 3 brands by revenue?"

### 2. RCA Question (Diagnostic / Root Cause Analysis)
- Investigative queries seeking to understand underlying reasons, causes, or drivers behind a trend
- Must contain explicit causal inquiry words like: "why", "reason", "cause", "what caused", "how come", "what's driving", "what's behind"
- Questions containing "rca" when used in context of requesting analysis (not just mentioning it)
- The intent is to analyze patterns, drivers, or contributing factors behind observed changes
- Examples:
  - "Why is the gross sales for Lysol for Walmart declining?"
  - "Why did trade investment drop in Feb 2025 compared to Jan 2025?"
  - "What caused the revenue dip in Q2 2024?"
  - "Perform RCA on declining gross margins"
  - "I need RCA analysis for gross sales drop"

### 3. Performance_Summary (Executive / Holistic View)
- Questions seeking an overall performance view for a brand, retailer etc.
- User is not focused on a single KPI or ranking, but rather a broad summary across multiple KPIs
- Examples:
  - "Give me the performance summary for Lysol for 2024"
  - "How did Walmart perform in H1 2025?"
  - "Give a brand summary report for Lysol and Airwick for Q1 2025"
  - "Provide overall business performance for Health & Hygiene category YTD"

### 4. Chat_History_Report (Chat History/Transcript/Conversation Report)
- Questions asking for a report, summary, or export of the chat history, transcript, or previous conversation
- Must contain words like: "chat history", "conversation report", "transcript", "export chat", "download chat", "show my previous questions", "show my chat log", "summarize my chat", "give me a report of my chat", "show my chat summary"
- Examples:
  - "Can you give me a report of my chat history?"
  - "Can you summarize my recent conversation?"
  - "Show me the transcript of my previous questions."
  - "Export my chat log."

### Important Classification Rules
- Questions asking "which", "who", "what" followed by superlatives (largest, smallest, top, bottom) are ALWAYS General, not RCA
- Questions seeking to identify the best/worst performers are descriptive, not diagnostic
- RCA questions must explicitly seek causal explanations, not just identification of outliers
- If a question asks for factual identification without seeking underlying causes, classify as General
- Only classify as RCA if the question explicitly seeks to understand the "why" behind a phenomenon
- If a question asks for overall performance or summary across multiple KPIs without asking for reasons → classify as Performance_Summary
- Focus on the intent: seeking explanation/analysis (RCA) vs seeking data/facts/identification (General) vs summary (Performance_Summary)

---

## KPI Type Identification Rules

### Sales Execution Based
Query mentions:
- sales volume, sales total, out of stock, display compliance, broker performance, out of stock opportunity, OOS, LOOS, COOS, TOOS, POOS, phantom / low/total/complete out of stock, number of broker visits, task completion rate, number of planned displays, number of planned activities

### Finance Based
Query mentions:
- gross sales, trade investment, gross margin, net revenue, gross margin percentage/%

### Shipment Based
Query mentions:
- LV Sales Call, Open Previous Month, Total Open, Shipped not invoiced, invoiced, Op+Sh+Inv, Op+Sh+Inv with PFR, GS Projection, Credit/Debit GS Value, GS Projection + Credit/Debit, Last Order Data, PFR_L4WK (GS), Avg Weekly Order Entry Trend, Run rate * Remaining Wks, Open On hold, Open No Product, Open, Unplanned, Planned, Confirmed, Picked, Shipped, Invoiced, Total without PF

### Default Rule
- If no KPI is explicitly mentioned -> assume sales execution

---

## Available Reference Lists

### Brand List
Airborne, Airwick, Amope, Big Boy, Biofreeze, BodiOme, Bonjela, Botanica, Botanical Origin, Brasso, Brasso MPC, Calgon, Cepacol, Clearasil, Cling Free, d-Con, Delsym, Dettol, Digestive Advantage, Durex, Easy Off, Easy Off Bam, Easy On, Enfamil, Finish, Flor, French's, Glass Plus, Glen 10/20, Harpic, Jik, K-Y, Lanacane, Lice MD, Lime-A-Way, Little Lucifer, Luftal, Lysol/Lizol, MegaRed, Micostatin V, Moov, Mop and Glo, Move Free, Mucinex, Naldecon, Neuriva, Not Applicable, Not Applicable - Health, Not Applicable - HyHo, Noxon, Nugget, null, Nurofen, Old English, Optrex, Oscal, Other, Own Label, Picot, Pine O Cleen, Private Label, Queen V, Resolv, Resolve (Fabric/Carpet), Rid-X, Sani, Scalpicin, Schiff, Scholl, Spray 'N Wash, St Marc, Strepsils, Tempra, Therapearl, Unbranded, Unknown, Vanish, Vani-Sol, Veet, Veja, Vitalmins, Woolite

### Retailer List (Finance)
Amazon, Caribbean, Closeout, Hardware, House Account, Institutional/Hospital, Price Smart, Professional, Target, Total Club - BJS, Total Club - COSTCO, Total Club - SAMS, Total Dollar - Other, Total Dollar - DG, Total Dollar - Family, Total Drug - Other, Total Drug - CVS, Total Drug - Walgreens, Total Food - Other, Total Food - Albertsons, Kroger, Total Food - Publix, Unallocated, Walmart, e commerce

### Retailer List (Sales Execution)
Walmart, Kroger

---

## RCA Drill-Down Logic (Finance KPIs)

### Extraction Rules
Given a user query, identify:
- **KPI**: The business metric being asked about (e.g., Gross Sales, Net Revenue, Trade Investment, Gross Margin). If no KPI is extracted, take "Gross sales" by default.
- **Brand/segment**: The brand or segment mentioned. If none provided, return "overall brands".
- **Retailer**: The retailer mentioned. If none provided, return "overall retailers".
- **Period of Analysis**: The most recent time period mentioned. Convert relative expressions:
  - "this year" → Current year (e.g., 2025)
  - "last year" → Previous year (e.g., 2024)
  - "this quarter" → Current quarter (e.g., Q3 2025)
  - "previous quarter" → Last quarter (e.g., Q2 2025)
  - "this month" → Current month
  - "previous month" → Last month
- **Period of Comparison**: The earlier time period, converted similarly.
- **Trend**: Whether the query is about "Growth", "Decline", or another type of change.

### Drill-Down Dimension Rules

| User Input | Drill Down |
|------------|------------|
| Brand + Retailer | Segments |
| Segment + Retailer | Products |
| Brand Only | Segments & Retailers |
| Segment Only | Products & Retailers |
| Retailer Only | Brands |
| No Filters | Brands & Retailers |

### Follow-Up Question Design Rules

1. If user mentioned **both brand and retailer** → ask for top 5 segments for that brand and retailer for the same time period checking for growth/decline

2. If user mentioned **both segment and retailer** → ask for top 5 products for that segment and retailer for the same time period checking for growth/decline

3. If user mentioned **only brand** (no retailer) → drill down into BOTH dimensions: ask for top 5 segments AND top 5 retailers for that brand

4. If user mentioned **only segment** → ask for top 5 products and retailers for that segment

5. If user mentioned **only retailer** → ask for top 5 brands for that retailer

6. If user mentioned **neither brand nor retailer** → ask for top 5 brands and retailers

7. If user has given other KPI (not gross sales, gross margin, net revenue or trade investment) → return message: "RCA can only be performed on Gross Sales, Net Revenue, Trade Investment or Gross Margin"

---

## RCA Drill-Down Logic (Sales Execution KPIs)

### Drill-Down Convention (Cases 1–16)

| Case | User Input | Drill Down |
|------|------------|------------|
| Case 1 | KPI @ Overall | Segment |
| Case 2 | KPI @ Segment | Brand |
| Case 3 | KPI @ Brand | Product |
| Case 4 | KPI @ Retailer | Segment level AND Region level |
| Case 5 | KPI @ Brand + Retailer | Product level AND Region level |
| Case 6 | KPI @ Segment + Retailer | Brand level AND Region level |
| Case 7 | KPI @ Product + Retailer | Region level |
| Case 9 | KPI @ Brand + Region | Product level AND market level |
| Case 10 | KPI @ Segment + Region | Brand level AND market level |
| Case 11 | KPI @ Region + Product | market level |
| Case 12 | KPI @ Region | Segment level AND market level |
| Case 13 | KPI @ brand + market | product and store_id level |
| Case 14 | KPI @ segment + market | brand and store_id level |
| Case 15 | KPI @ product + market | store_id level |
| Case 16 | KPI @ market | segment and store_id level |

### Required KPIs for Sales Execution RCA
For BOTH questions, ask to generate these KPIs for the TOP 5:
- OOS% (TOOS%, COOS%, POOS%, LOOS%)
- Display compliance %

**MUST**: Generate the KPIs for both time periods - period of interest and period of comparison

**IMPORTANT**:
- If sales is increasing → ask the Total OOS opportunity trend for decrease
- If sales is decreasing → ask the Total OOS opportunity trend for increase

---

## Performance Summary Question Generation

When user asks for overall performance summary, generate exactly 5 questions covering:

1. **Sales Volume (Units) and Sales Value (Dollars)** - (Sales Execution)
2. **Gross Sales, Net Revenue, Trade Investment and Gross Margin** - (Finance)
3. **OOS% (Total, TOOS, LOOS, COOS, POOS)** - (Sales Execution)
4. **OOS Opportunity (lost sales due to OOS)** - (Sales Execution)
5. **Display Compliance %** - (Sales Execution)

### Guidelines
- Questions must be direct and metric-focused
- Do NOT ask about reasons, causes, impact, correlation, spikes, or performance drivers
- Use the brand(s), retailer(s) and time period from the user request
- If comparison baseline is missing, assume comparison vs previous period and year-ago
- If retailer is other than "Walmart" or "Kroger", generate questions only for "Gross Sales, Net Revenue, Trade Investment and Gross Margin"

### Example

**User request**: "Give me the performance summary for Lysol for 2024 for Walmart"

**Generated Questions**:
1. What was the sales volume and sales value for Lysol in 2024 compared to the previous year for Walmart? - (Sales Execution)
2. What was the gross sales, net revenue, gross margin and trade investment for Lysol for 2024 for Walmart? - (Finance)
3. What were the OOS%, TOOS%, LOOS%, COOS%, and POOS for Lysol in 2024 for Walmart? - (Sales Execution)
4. What was the total OOS Opportunity (lost sales due to OOS) for Lysol in 2024 for Walmart? - (Sales Execution)
5. What was the display compliance percentage for Lysol in 2024 for Walmart? - (Sales Execution)
