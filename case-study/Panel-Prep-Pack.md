# Apskaita5 panel prep pack

Every answer was checked against the submitted case study, Reference, cost model and code facts. The panel has the submitted version: handle the weak spots out loud, don't change the document.

## Weak spots: say them first

1. **70% of customers by month 12 is cleared by only 30 customers (2,970 against 2,940), and the month-12 gate also needs every guardrail green.**
    - Why it hurts: It's the brief's headline goal and anyone can read the margin off the goals table. If Kirill sounds surprised by it, the plan looks reverse-engineered to the target.
    - Handle it: Say it first, on the goals slide and again on migration: '30 customers of slack; a slip moves 70% about month for month, and up to two months more if it hits the winter freeze.' Then the mechanism: capacity is about 1,000 a month against a 650 peak, so readiness is the limit, and month 9 (all nine modules, 1,170 customers) is the early warning. Do not say there's hidden buffer, do not offer to loosen a gate, and do not promise to 'catch up'.
2. **Cash payback is year 4 (month 44). The sensitivity line says a 35% cloud overrun 'lands exactly on the 406 EUR target', but that's only true at full scale (299 x 1.35 is about 404). At month 12 it's about 445 EUR, which misses the month-12 KPI. Cloud +35% and team +25% together turn five-year cash slightly negative.**
    - Why it hurts: A CFO compares year 4 with a two-year cloud payback, and anyone who multiplies 330 by 1.35 catches the 'exactly on 406' claim. One caught number undercuts all the others.
    - Handle it: Lead with 'cash isn't the main case; risk and speed are', then give month 44 and about 2.5M EUR five-year cash without apology. Every time you quote the +35% case, say 'at full scale'. If pushed on combined downsides, admit it isn't a named case and is slightly negative at five years, then point to the week-4 bill check before big money is spent. Do not count freed time as cash, do not quote decimals, and do not claim cloud won't overrun.
3. **The goals table says 'run cost down 55% per migrated customer at month 12', but realized savings at month 12 is only break-even and year 1 is negative.**
    - Why it hurts: Finance and skeptic panelists will call it a choice of denominator. Defending it as a company saving costs credibility on the whole business case.
    - Handle it: Say: 'It's a definition, and I show both. 330 EUR is cloud cost per migrated customer, which shows the unit economics, as a planning estimate until the week-4 bill. The company bill breaks even around month 12 because we pay for two estates; the full saving, about 1.8M EUR a year, starts in month 21.' Know the model mechanics: legacy still hosts about 2,480 databases at month 12 because of a two-month archive lag, and about 0.6M EUR a year of legacy cost is fixed until switch-off in month 20 (these are cost-model settings, not in the case study: say 'in the model' when you quote them). Do not argue the definition.
4. **The 'today' slide and case study say 'the five copies of the rounding code disagree on about 1 in 560 VAT calculations'. Only two copies (the VB helper and the MySQL function) were emulated, and neither has run on the real runtimes.**
    - Why it hurts: An architect or skeptic who reads the Reference will see the overstatement, and 'zero regression' is the goal where sloppy claims hurt most.
    - Handle it: Say it precisely every time: 'Five copies exist; the two we emulated, VB and MySQL, disagree on about 1 in 560; the harness confirms it on the real runtimes in weeks 2 to 4.' Then: whatever the real rate, half-cent cases are approved once, as a class. Do not say 'measured', and do not say 'the five copies disagree'.
5. **'20 days at most for every customer, cloud or legacy, from month 4' depends on automatically rebuilding all 310 legacy forks. The Reference KPI trajectory only targets the first pack change by month 6 and every change by month 9, and the hand-patch fallback appears only in the speaker notes.**
    - Why it hurts: It's the boldest promise in the plan, and a panelist holding the appendix can show the proof arrives later than the headline.
    - Handle it: Say first: 'Rebuilding all 310 legacy forks by month 4 is the boldest promise here.' Then: 'Month 4 is the commitment; the dashboard proves it in steps, first pack change by month 6, every change by month 9. Biggest forks first; the tail is hand-patched, and those could miss 20 days, which the legacy turnaround KPI would show.' Do not insist all 310 will build, and do not quietly narrow the promise to cloud customers.
6. **The KPI mock-up is headed 'month 9 plan values' and shows '60% accepted' AI code, but the case study says acceptance is never a quota or target.**
    - Why it hurts: An AI panelist will ask where 60% comes from. It reads like a target the schedule depends on, which contradicts the 'no quota' line.
    - Handle it: On the KPI slide, say it before anyone asks: 'The AI tile is illustrative; acceptance is tracked to steer the method, never a target. The real baseline comes from the ledger work by month 6.' If asked what low acceptance does: dates or staffing move, never the gates; a 25% higher team cost moves payback from month 44 to 50. Do not defend 60% as a plan number.
7. **The week-8 go or no-go has only three written criteria (assumptions confirmed, 95% inventory precision on ledger and VAT, harness running). The week-4 cloud bill has no pass or fail threshold, module teams start in month 2 before the gate, and after week 8 the plan has pauses, not stop criteria.**
    - Why it hurts: 'Fund about 0.6M EUR and decide on evidence' is the entire ask. A CTO who finds the gate thin, or money spent before it, questions the ask itself.
    - Handle it: Name the three criteria crisply, then: 'I'd add one in writing: if the real bill puts cost per customer at full scale above the 406 EUR target, about a third over my estimate, I recommend no full rollout.' Admit early module work starts in month 2 and sits inside the about 0.6M EUR. Say the steering committee makes the stop call. Do not present the cost threshold as already in the document, and do not confuse 'pause new cutovers' with 'stop the program'.
8. **Wave 0 includes 'the firm's own books', but payroll doesn't pass equivalence until mid-month 7, and the one-writer rule means payroll can't be split off.**
    - Why it hurts: A delivery or domain panelist can catch the plan breaking its own ordering rule in the very first wave.
    - Handle it: If raised, own it at once: 'Fair catch. If our own payroll runs in Apskaita5 today, our books move with payroll in wave 2, and the 19 volunteers carry wave 0. I confirm that in discovery.' Do not argue that the firm probably doesn't run payroll in the product.
9. **The roadmap speaker notes say the platform 'is not on the critical path'. That's true for first customers (about six weeks of slack to mid-month 5), but the weekly rehearsal of all 4,200 databases starts in month 4, right after the platform gate. The cloud contract, the EU AI agreement and the outside penetration test are external dependencies.**
    - Why it hurts: A delivery lead who has seen procurement and security sign-off take a quarter will push on 'platform in three months', and an unqualified 'not on the critical path' sounds naive.
    - Handle it: Say: 'AI builds the platform fast; contracts and the outside security test set the pace, so both start in week 1. It's off the critical path for first customers, not for the fleet rehearsal, where every week late is a week less to find data surprises.' Do not call the platform trivial.
10. **'We'd split a module out if teams pass about 50 people.' During the program, the firm's roughly 30 engineers plus a dedicated team of about 30 already pass 50.**
    - Why it hurts: A sharp architect can say he's past his own trigger on day one, which makes the monolith defense sound like a slogan.
    - Handle it: Scope it every time: 'when the teams working on one module's code pass about 50 people, or its load diverges.' Then name the likeliest first split, statements and e-filing: it only reads the books, its reports already run on the read replica, it spikes in filing week, and splitting it needs no distributed transaction. Do not say 'we'd never split'.

## If they raise it

- **Week-8 gate is thin** (CTO). The written go or no-go has only three criteria: assumptions confirmed, the rule inventory at 95% on ledger and VAT, the harness running. The week-4 cloud bill check has no pass or fail threshold, module pods A and B start in month 2 before the gate, and after week 8 the plan defines pauses, not stop criteria. Say: 'I'd add a cost criterion in writing: if the real bill puts cost per customer at full scale above the 406 EUR target, about a third over my estimate, I recommend no full rollout. Early module work sits inside the about 0.6M EUR. After week 8, guardrails pause cutovers; stopping is always a steering decision.' Don't claim the cost threshold is already in the document.
- **Cell sizing rests on unconfirmed numbers** (Architect). 600 tenants per cell rests on the median-database-under-2-GB assumption; the 3% dedicated cut has no stated basis (the assumption only covers the largest 5% being under 50 GB); and the month-3 platform gate has no load or noisy-neighbor test, although cells are sized for 3 times filing-week load. Say: 'Both are planning numbers confirmed at week 8 and measured by the weekly fleet rehearsal from month 4. I'd add a three-times-filing-week load test on the two live cells to the month-3 gate.'
- **Disaster recovery is not fully costed or consistent** (Architect). The 15-minute, 4-hour regional target needs a standby copy in a second EU region, but the cloud cost inputs have no line for it, and backups alone won't meet 15 minutes. Also, the 1-hour in-region recovery is looser than the availability budget: 99.9% allows about 43 minutes a month, and 99.95% across the 15th to 25th about 8 minutes. Say: 'The standby isn't its own line yet; the week-4 bill settles it. My rough estimate is up to about 80 EUR per customer, inside the 35% overrun case at full scale, which would move cash payback toward the low 50s. The hour is a worst-case ceiling; automatic failover typically takes minutes. A regional disaster would break that month's target, and we'd report it.'
- **'Cloud +35% lands exactly on 406' is only true at full scale** (Architect, Skeptic, Hiring manager). 299 x 1.35 is about 404, but at month 12, the brief's deadline, 330 x 1.35 is about 445 EUR. That misses the month-12 KPI of 406 and gives roughly a 40% cut, not 45%; month-12 headroom is about 23%, not 35%. Say: 'At full scale it lands about on 406; at month 12, while cells are still filling, it would be about 445, so the 45% goal lands at full scale rather than month 12. That's why the bill is checked in week 4.' Always say 'at full scale'.
- **Combined downside turns cash negative** (CFO). Re-running the cost model with cloud +35% and team +25% together gives five-year net cash of about minus 0.3M EUR, cash payback around year 6, and a cash low point of about 5M EUR. The documents show only single-variable cases. Say: 'I didn't show it as a named case. The two effects add, so five-year cash is slightly negative and payback slips into year 6. Both inputs are checked before big money: the bill in week 4, team size in discovery. If both come in high, you hear it at week 8 and decide on risk and speed, not savings.'
- **Support assistant's ticket pool can leak across tenants** (Security lead). The assistant answers from resolved tickets drawn from every customer, and the plan never says those tickets are redacted or scoped; the AI data assumption calls for redaction in general but never applies it to the assistant's ticket pool. Tickets often hold company names, amounts and payroll details. Say: 'I'd index the assistant only on redacted tickets, rewritten as generic problem-and-fix entries; anything about the user's own data goes through the app with their rights. I'd add that to the plan explicitly.'
- **Fork-analysis consent is a hidden critical-path item** (Security lead). The plan requires customer consent before AI analyzes a fork, and all 310 forks must be classified by week 6, but no consent step appears on the roadmap. Collecting up to 310 sign-offs in under six weeks feeds the fork wave and the misfit tail. Say: 'I'd start consent requests in week 1. If a customer refuses, the firm's own people classify that fork by hand, since they already maintain it; that costs time, not safety, and refusals are reported at week 8.'
- **AI kill switch has no owner and only per-tenant scope** (Head of AI). Each AI feature has a per-tenant kill switch but no named owner; an auto-post guardrail breach pauses new cutovers but doesn't itself stop auto-posting; and a large supplier's layout change hits many tenants at once. Say: 'I'd name the on-call owner of the AI features as the one who pulls it. I'd add a per-supplier switch back to drafts, and use the model gateway plus feature flags to put every tenant back to drafts-only in one change.'
- **Auto-post launch gate is statistically weak** (Head of AI). '99.5% correct on 1,000+ invoices' passes with 5 misses in 1,000, which only shows about 99% accuracy at 95% confidence. Proving 99.5% needs at most 1 miss at 1,000, or at most 4 at 2,000. Say: 'On its own it doesn't prove 99.5%; 1,000 is the minimum, not the proof. I'd reword the gate as a 95% lower bound of 99.5%. The design caps the damage: per-tenant opt-in, known suppliers only, a per-tenant limit, fixed checks first, one-click reversal and the 0.5% error guardrail.'
- **KPI mock-up shows '60% accepted' as a plan value** (Head of AI). The dashboard image is headed 'month 9 plan values' and shows 60% accepted, 25% reworked, 15% rewritten, while the case study says AI acceptance is never a quota or target. Say: 'It's an illustrative number on a mock-up, not a target and not a measurement; the real baseline comes from the ledger work by month 6. I'd relabel that tile.'
- **Wave 0 includes the firm's own books, but payroll isn't ready** (Delivery head). A customer moves only when every module it uses has passed equivalence, payroll passes only at mid-month 7, and one writer per customer rules out keeping payroll on legacy. Say: 'If our own payroll runs in Apskaita5 today, our books move with payroll in wave 2, and the 19 volunteers carry wave 0. I confirm that in discovery.'
- **'20 days for every customer from month 4' is proven later than promised** (Tax and accounting, Skeptic). The executive summary and statutory section promise it from month 4, but the Reference KPI trajectory only targets the first pack change within 20 days at month 6 and every change at month 9. The hand-patch fallback for forks lives only in the speaker notes and could miss 20 days. Say: 'Month 4 is the commitment; the dashboard proves it in steps at months 6 and 9. Until then, a form not yet on packs ships as reviewed code: a cloud release on any day, and the fast lane for legacy customers. Hand-patched forks are the ones that could miss, and the legacy turnaround KPI would show it.' Consider wording the headline as 'from month 4, proven on every change by month 9'.
- **'The five rounding copies disagree on about 1 in 560' overstates the evidence** (Skeptic). Only two implementations were emulated, the VB helper and the MySQL function; the other two VB copies and the SQLite function were not. The 1-in-560 figure comes from 354 of 200,000 random 21% VAT amounts; the half-cent sweep gives 6.6%. Say: 'Five copies exist; the two we emulated, VB and MySQL, disagree on about 1 in 560 random VAT amounts. The harness confirms it on the real runtimes in weeks 2 to 4, and whatever the rate, half-cent cases are approved once, as a class.'

## Opening (cover slide)

Thank you for having me. I'll present this the way I'd present it to the firm's CTO and CFO, and I'll start with the ask, so you can judge everything else against it.

My recommendation: rebuild Apskaita5 as one multi-tenant cloud product, with AI drafting and people signing, and move customers one at a time, each one only once every ledger, VAT and payroll number matches the old system to the cent.

Three numbers frame it. One: about 4M EUR over two years, paying back in year 4 on infrastructure savings alone. Two: first customers in month 5, 70% of customers by month 12, everyone by month 18. Three: tax-law changes in 20 days at most, against 10 to 14 weeks today and a 6-week legal window.

But the decision I'm actually asking for is small: fund an eight-week foundation phase, about 0.6M EUR, with a go or no-go at week 8 on evidence, not slides.

In the next 25 minutes you'll see what I found in the code, the target architecture, how AI is used at four layers with a human gate on each, how customers move and how they move back, and the money. I'll flag the tight spots myself as we go, starting with the fact that two of the five goals have very little slack.

## Talk track (25 minutes)

1. **Cover**, from 00:00, 1.5 min. Use the opening below, word for word. It takes about 1.5 minutes. *Point at:* The three numbers along the bottom.
2. **Five goals**, from 01:30, 1.5 min. Here are the five goals from the brief and what the plan delivers against each. Run cost has about 23% headroom at month 12: 330 EUR per migrated customer against a 406 target, and more at full scale. Two goals have almost no slack, and I'd rather say it than have you find it: 70% is cleared by just 30 customers, and tax changes come in at 20 days at worst against under 3 weeks. To see why the plan is shaped this way, here's what I found in the code. *Point at:* The 70% row and the tax-change row. Say the slack before anyone spots it.
3. **Today's system**, from 03:00, 2 min. Three findings from reading the code shaped this plan. Money is stored as floating point, and our emulation of two of the five rounding copies suggests they disagree on about 1 in 560 VAT calculations, so we test equivalence to the cent and confirm that figure on the real runtimes in weeks 2 to 4. Customers upgrade their own database schema by hand and desktop users can write straight to MySQL, so all 4,200 databases are brought to one structure first and legacy writers are locked out at cutover. The good news is that business logic is separate from the UI, so the old code should run headless as our answer key, and proving that is part of the week-8 gate. Here's what replaces it. *Point at:* The stack of 310 forks, then the 4,200 databases along the bottom.
4. **Target architecture**, from 05:00, 2.5 min. One code base for every customer: a modular monolith on .NET 10, in cells of about 600 tenants, seven at full scale, with the largest 3% on a dedicated database running the same code. Isolation is forced row-level security, the tenant in every key, queue, cache and log, and hourly cross-tenant probes that block a release. It's a monolith on purpose: posting one invoice touches four modules in one transaction, so we scale by adding cells, and anything slow or external runs outside through the outbox. Legacy runs alongside until month 20. Two parts of this design carry most of the business value, starting with tax changes. *Point at:* Trace one invoice: web client, edge, the cell, the monolith, PostgreSQL, then the outbox arrow down to the filing gateway.
5. **Tax-change pipeline**, from 07:30, 2 min. Tax changes ship as data: signed, effective-dated rule packs, about 10 working days and 20 calendar days at worst, against 10 to 14 weeks today and a 6-week legal window. A chartered accountant signs every pack, no AI executes tax rules, and every calculation records its pack version, so history is never silently recalculated. From month 4 a legacy fast lane gives legacy customers the same speed, and I'll say it first: rebuilding all 310 legacy forks for that is the boldest promise in this plan, with biggest forks first and the tail patched by hand as the fallback. Those forks are the second part. *Point at:* Walk the five boxes left to right, then the dashed 'New formula (rare)' path.
6. **Forks into tiers**, from 09:30, 1.5 min. AI diffs each of the 310 forks against the release it branched from and classifies every change, all by week 6. Each change lands in one of three tiers: a setting, a template or rule, or an out-of-process extension through the API that never writes to ledger tables. A change many forks share is promoted to the core for everyone; one that fits nowhere goes on the backlog, and that customer moves in the last wave. No customer keeps a code fork in the cloud, and getting there depends on how we use AI, which is next. *Point at:* 310 forks, AI analysis, the three tiers, the extension manifest; then the dashed 'No fit yet' box.
7. **AI layers L0 to L3**, from 11:00, 2.5 min. The same pattern runs through every layer: AI drafts, deterministic tools verify, and a named person signs a gate with a threshold. The rule inventory must reach 95% precision with every money rule reviewed by the legacy engineers and an accountant; translated money code needs the compiler, tests and differential suite green plus two reviewers; migrated data must match every control total to the cent; and equivalence must be 100% on ledger, VAT and payroll, with legacy as the answer key. Mutation tests flip a sign or a rate on purpose to prove the harness catches it. AI never moves money and never approves its own work. Here's how that lands on a calendar. *Point at:* Read one column top to bottom (L3: test cases, legacy as the answer key, accountant signs at 100%), then the bottom row of gates.
8. **Roadmap and gates**, from 13:30, 2 min. I'll talk to the gates, not every bar. Week 8 is the go or no-go; the platform is ready in month 3, where contracts and the outside security test set the pace; first customers come mid-month 5, once five modules pass equivalence and keyboard speed matches the desktop. Payroll follows mid-month 7 after two matching shadow payrolls, and full scope mid-month 8. The date I watch hardest is month 12, and that's the next slide. *Point at:* Only the six diamonds: week 8, month 3, mid-month 5, mid-month 7, mid-month 8, month 12.
9. **Migration waves**, from 15:30, 2 min. Five waves take 2,970 customers, 70.7%, to the cloud by month 12, and the last 1,230 by month 18. Lowest complexity first, bureaus as a portfolio, and no cutovers from the 10th to the 25th or from mid-December to mid-February. I'll say it first: that clears 70% by only 30 customers, so a slip moves the date about month for month. Capacity isn't the limit, about 1,000 a month against a 650 peak; module readiness is, and every move has a rehearsed way back until the customer's first cloud filing. *Point at:* The gap between the 2,970 point and the dashed 70% line at month 12.
10. **Rollback**, from 17:30, 1.5 min. Only one system writes a customer's books at any moment: an authority stamp says which, and legacy writers are locked out at cutover, not asked to stop. Before go-live a failed gate changes nothing; during hypercare, up to 35 days, we can put a customer back on legacy in hours with nothing lost; once the tax authority accepts a cloud filing, we fix forward. Rollback above 2%, or any correctness incident, pauses all new cutovers. Here's how the steering committee sees all of this. *Point at:* The middle card (hypercare), then the circuit-breaker bar at the bottom.
11. **KPI dashboard**, from 19:00, 1.5 min. These are the seven KPIs the brief named, refreshed weekly and reviewed monthly, shown with month-9 plan values, not actuals. Five guardrails sit underneath, and any breach pauses new cutovers; correctness and isolation always outrank speed. The AI tile is illustrative: acceptance is tracked to steer the method, never a target for reviewers. And realized savings is honestly negative at month 9, about minus 0.4M EUR a year run rate, because we pay for two systems, which brings me to the money. *Point at:* The AI tile (illustrative, not a target) and the realized-savings tile (negative at month 9, as planned).
12. **Payback**, from 20:30, 2 min. About 4M EUR over two years, mostly a dedicated team of about 30 for a year, with about 0.6M EUR in the first eight weeks. Cash counts infrastructure savings only, about 1.8M EUR a year from year 3, so cash payback is month 44; counting freed support and engineering time it's month 35, but I don't count that as cash. These are planning estimates, re-checked against a real cloud bill in week 4. So the case is risk and speed, not just savings, and here's what I deliberately chose not to do. *Point at:* The low point (about minus 3.9M in quarter 6), then the two payback circles.
13. **What we rejected**, from 22:30, 1.5 min. Every choice here favors financial correctness and one code base over the speed of the first release. Rehosting keeps 4,200 databases, a manual rewrite of 522,000 untested lines doesn't fit 12 months, and strangling module by module means two systems writing one set of books, so we strangle by customer instead. Microservices would split one posting across services; we'd split a module out later if its own teams or load outgrow the monolith. Which brings me to the decision. *Point at:* The Architecture and Migration rows.
14. **Close**, from 24:00, 1 min. Four lines carry the plan: one writer per customer's books, match to the cent before moving, roll back until the first cloud filing, and AI drafts, tools check, people sign. The ask is eight weeks and about 0.6M EUR, then a go or no-go on evidence. Then I open it up for questions. *Point at:* The decision box.

## Close

Let me close where I started. Four lines carry this plan: one writer per customer's books; every number matches to the cent before a customer moves; a way back until their first cloud filing; and AI drafts, tools check, people sign.

I've shown you the tight spots myself: 30 customers of slack on the 70%, cash payback in year 4, and all 310 legacy forks by month 4. That's exactly why the ask is small and gated. Fund eight weeks, about 0.6M EUR, and at week 8 you decide go or no-go on evidence: the assumptions confirmed, the rule inventory at 95% precision, and the legacy test harness running.

I'd welcome your questions.

## Top 20 questions

### Cash payback in month 44 on about 4M EUR. Most cloud programs pay back in two years. Why should anyone fund this instead of keeping what we have?

*Asked by: CTO, CFO, Skeptic, Hiring manager*

I'd fund it because this is about risk and speed, not just savings, and the cash case still stands on its own. On infrastructure savings alone, about 4M EUR pays back in year 4, around month 44, with about 2.5M EUR net cash over five years. Counting freed support and engineering time it's month 35, but I don't count that as cash unless spending falls. What the money buys: tax changes in 20 days at most instead of 10 to 14 weeks, against a 6-week legal window; the 310 forks gone; and engineers off a frozen 2006 stack, with maintenance falling from 62% of their time to 30% or less. And the first commitment is about 0.6M EUR, not 4M.

**Follow-up:** What's your downside case?

The worst single case is cloud costing 35% more than planned: payback moves to about month 56 and five-year net cash falls to about 0.6M EUR. At full scale that still lands on the 406 EUR target, though at month 12 it would be about 445 EUR. Waves slipping three months gives about month 49; team costs 25% higher, about month 50. None of those alone turns five-year cash negative. Cloud and team overruns together would push cash payback into year 6, which is exactly why the cloud estimate is checked against a real bill in week 4, before the go or no-go.

**Trap:** Counting freed time as cash to flatter payback; quoting decimals; getting defensive about year 4; saying the +35% case 'lands on 406' without 'at full scale'.

Source: Business impact, p.18-20 (month 44 and 35, 2.48M EUR five-year cash, 62% to 30%); cost-model-output (sensitivity 56/49/50, 0.58M EUR); Reference cost inputs, p.4 (real bill in week 4); speaker notes 'payback'. Month-12 figure (330 x 1.35) and the combined downside come from re-running the cost model, not in documents.

### You clear 70% by just 30 customers. Be straight with me: how confident are you in month 12, and what's most likely to slip?

*Asked by: CTO, Skeptic, CFO, Delivery head, Architect, Hiring manager*

I'm confident in the method, least confident in the 70% date, and I put that on my slide. The plan moves 2,970 customers by month 12 against a 2,940 target, so there are 30 customers of slack. A slip moves 70% out about month for month, and one that reaches the mid-December to mid-February freeze adds up to two months more. Capacity isn't the risk: the migration factory can move about 1,000 customers a month against a planned peak of 650. Readiness is: a customer moves only when every module it uses has passed equivalence testing, so if payroll or inventory passes late, everyone who uses it waits. A three-month slip moves cash payback from month 44 to about 49.

**Follow-up:** It's month 8 and you're six weeks behind. What do you cut to hold month 12?

Never the correctness gates; I'd let the date move first. I'd tell the steering committee that week that 70% moves out about six weeks, and why. The levers that don't touch correctness: the factory has spare capacity, so once the cause is fixed I add ready, simple customers to the nights we have, and push heavy-fork customers to the last wave so they don't hold others up. The warning comes well before month 11: the plan has all nine modules live and 1,170 customers by month 9.

**Trap:** Saying 'very confident' or inventing a probability; mixing factory capacity with customer readiness; hinting a gate could be loosened to make the number; promising to 'catch up'.

Source: Migration plan, p.13-14 (wave plan, 30 tenants of slack, freeze, ordering rule, factory capacity); Business impact sensitivity, p.19; Reference KPI trajectory, p.5 (9 of 9 modules and 1,170 at month 9); speaker notes 'goals' and 'migration'; study sheet 'Say it first'. The reorder lever is reasoning, not in documents.

### Why rebuild at all? Why not rehost it in the cloud, refactor it module by module, or buy an off-the-shelf cloud ERP with a Lithuanian localization?

*Asked by: CTO, Skeptic, Hiring manager*

I chose a rebuild because it's the only option that fixes cost, tax-change speed and the 310 forks at once. Rehosting keeps 4,200 databases, so cost still grows per customer, and tax changes stay slow because every tax-form version is a copied class. Refactoring module by module means old and new systems both write one ledger, which is where financial errors hide. And it isn't a blank-page rewrite: we translate the calculation kernels and rebuild the shell. Buying is a business-model question: this firm is the vendor, so it would resell someone else's product and still migrate 4,200 customers and 310 customizations. I didn't evaluate a specific cloud ERP in depth, and I'd test that option before the week-8 gate.

**Follow-up:** Big ERP rewrites usually run late or get abandoned. Why is yours the exception?

I don't assume it is; I designed against the three ways rewrites die. The old system keeps moving: here forks freeze in month 3 and features in month 6. Unwritten rules get lost: here legacy runs headless as the answer key, so a missed rule shows up as a difference in nightly tests, replayed history from 300 customers plus a million generated cases, before anyone moves. Everyone cuts over on one night: here customers move one at a time, with a rehearsed way back until their first cloud filing. And only about 0.6M EUR is at risk before we have evidence.

**Trap:** Waving off 'buy' as obviously wrong, or pretending he did a vendor evaluation; calling the plan a blank-page rewrite; making 'AI changes everything' the main argument.

Source: Trade-off analysis 'Strategy', p.18; L1 'translate the kernel, rebuild the shell', p.10-11; Current-state findings, p.3; L3 test sets, p.11; Legacy end of life, p.16; what-not-to-do (rehost, manual rewrite, two live systems). The 'buy' option is not in documents.

### You're asking for about 0.6M EUR for eight weeks. What exactly do I own at week 8, and what would make you tell us to stop?

*Asked by: CTO, CFO, Delivery head*

At week 8 you own evidence, not slides. The 13 assumptions confirmed, including what the 3.1M EUR really covers, plus the cloud estimate checked against a real bill in week 4. A rule inventory for ledger and VAT at 95% precision, reviewed by the four legacy engineers and an accountant. The old system running headless, without its screens, as the automated answer key. And all 310 forks classified. I'd recommend no full rollout if the old code can't run headless, if the inventory can't reach 95%, or, a criterion I'd add in writing, if the real bill puts cost per customer at full scale above the 406 EUR target, about a third over my estimate. Even then, you keep the rule inventory and the fork map.

**Follow-up:** Who makes the stop call, you? And isn't some build money spent before week 8?

No, the steering committee makes the call, against criteria written down before we start, so money already spent doesn't make the decision. My job is to make the gate show real evidence, not a status color. And yes, both module teams, the rules engine, the web client and the migration factory start in month 2, before the gate, but that spend sits inside the 0.6M EUR. After week 8, a guardrail breach pauses new cutovers; stopping the program is always a steering decision.

**Trap:** Describing the eight weeks as open-ended discovery; giving no concrete stop condition; presenting the cost threshold as already in the document; confusing 'pause cutovers' with 'stop the program'.

Source: Executive summary 'Decision requested', p.2; gate P1, p.20; A12, p.4; Forks (week 6), p.7; Reference cost inputs (real bill in week 4), p.4; roadmap diagram (module pods from month 2); Guardrails, p.17. The cost stop criterion and what you keep if you stop are not in documents.

### Legacy stores money as floating point and its rounding copies disagree on about 1 in 560 VAT calculations. If you match legacy to the cent, aren't you certifying its bugs? Isn't 'zero regression' really 'zero unsigned deviations'?

*Asked by: Head of AI, Tax and accounting, Skeptic, Architect*

Yes, it's zero unsigned deviations, which is the only honest definition of zero. Every ledger, VAT and payroll number must match legacy to the cent, and a legacy bug is fixed only through a signed deviation register, never silently. A written tolerance policy has three parts: noise below a field's declared precision is ignored; half-cent boundary cases are approved once, as a class, by an accountant; any real logic difference is fixed or signed off one by one. History moves as legacy computed it, never recalculated. The 'about 1 in 560' figure comes from emulating two of the five rounding copies, the VB helper and the MySQL function. The test harness confirms it on the real runtimes in weeks 2 to 4.

**Follow-up:** How do you know the harness catches anything?

Mutation tests flip a sign or a rate on purpose to prove the harness catches it. The plan doesn't set a score; my bar for money code is that every planted change is caught or shown unable to change any result. A survivor means a missing test, and that module doesn't pass. Underneath sit four test sets: replayed history from 300 customers, a million generated edge cases a night, official golden files and one test per rule.

**Trap:** Saying the cloud will be identical to legacy; presenting 1 in 560 as measured; saying 'the five copies disagree' when only two were emulated; offering to recalculate history to clean it up.

Source: A10, p.4; L3 tolerance policy, four test sets and mutation tests, p.11; L2 'history is never recalculated', p.11; Current-state, p.2; Reference rounding note (354 of 200,000; weeks 2-4), p.3; codebase-facts (five implementations, VB vs MySQL emulated). The mutation-score bar is not in documents.

### Your timeline rests on AI translating half a million lines of 2006 VB.NET. What evidence do you have that works at this scale, how does AI really change the economics, and what if it underdelivers?

*Asked by: CTO, Skeptic, Delivery head*

Honestly, nobody can show proof at exactly this scale, so the plan doesn't depend on trusting it. First, we translate at most about 140,000 lines, the money logic; the 180,000-line desktop UI, bank import, statements and e-filing are rebuilt. Second, AI changes the calendar more than the bill: it speeds up reading and drafting, not proof. AI tooling and usage is only about 0.25M EUR of the 4M; the team is most of the cost. Third, nothing merges unless the compiler, tests and the differential suite against legacy are green, with two reviewers on money code. If a module's acceptance stays low for two sprints, engineers take it over, and the schedule moves, not the gates.

**Follow-up:** If I took AI out, what happens to cost and timeline?

I didn't model a no-AI version, so I won't quote a number. What I can say: rewriting 522,000 untested lines by hand doesn't fit 12 months, and the unwritten rules get lost on the way, which is why I rejected it. With AI, a parser maps 377 business classes and about 800 rule registrations, AI turns that into a reviewed inventory, all 310 forks are classified by week 6, and AI drafts the C# and screens. The pace is still set by the harness, the reviewers and overnight moves.

**Trap:** Accepting the '522,000 lines translated' framing; quoting AI accuracy figures or a no-AI savings number he doesn't have; selling AI as a big cost cutter.

Source: L1 module table and gate, p.9-11; Reference codebase at a glance, p.1; Reference investment (0.25M EUR tooling and AI), p.5; Trade-off 'Strategy', p.18; what-not-to-do (manual rewrite); L0, p.10. Proof at scale and the no-AI counterfactual are not in documents.

### About 600 companies' books in one shared PostgreSQL schema. Prove to me, not just assert, that tenant A can never read tenant B, including with connection pooling and background workers.

*Asked by: Architect, Security lead*

I prove it with layers that each fail closed, meaning they refuse when anything is missing. Row-level security, a database rule that filters every row by tenant, is forced, so even the app's own role can't bypass it; migrations use a separate role. The tenant is set inside each transaction, never on the session, so it vanishes at commit and can't leak to the next request on a pooled connection; a request with no tenant is refused. Workers take the tenant from the message itself. The tenant is in every key, queue, cache, document path, search and log. Evidence: hourly cross-tenant probes that block a release, an outside penetration test passed by the month-3 platform gate, and an isolation probe at every go-live.

**Follow-up:** What do the hourly probes actually do, and who sees a failure?

The plan commits to hourly probes that block a release; this is how I'd build them. Each cell gets fake canary tenants seeded with marker records. Every hour a probe signs in as one and tries to reach another's markers through the API, reports, search, exports, files and cache, and a database check with no tenant set must be refused. Any hit pages on-call and the security lead, blocks releases and pauses new cutovers.

**Trap:** Treating RLS as the whole answer; saying the tenant is set when the connection opens (it leaks across pooled connections); forgetting owner or superuser bypass and the paths outside the database; saying 'guaranteed'.

Source: Tenant isolation, p.5-6; Cutover runbook (isolation probe), p.14; Guardrails, p.17; gate P2, p.20; Reference glossary (RLS), p.6. The separate migration role and the probe design are not in documents.

### A modular monolith for a SaaS product in 2026? Why not microservices, and what stops nine modules in one deployable becoming the big ball of mud you're replacing?

*Asked by: Architect, Skeptic, Hiring manager*

I chose a modular monolith because the domain demands it. Posting one invoice touches four modules and must commit as one transaction. Split into services, every posting becomes a saga, a chain of steps that each need an undo, which is where cents go missing. What stops the mud: each of nine modules owns its schema, and architecture tests fail the build if anyone crosses a boundary. Anything slow, external or untrusted runs outside through the outbox, events saved in the same transaction as the data: extraction, filing, analytics and migration. We scale by cells of about 600 tenants, not by splitting code. I'd split a module out later if its teams pass about 50 people or its load diverges.

**Follow-up:** The client CTO, who's paying, says 'I want microservices, do it my way.' What then?

Then it's his call, and my job is to make it an informed one. I'd agree with his goal, independent scaling and teams that don't block each other, and write down the price: postings spread across services, a bigger team to run it, likely a later first wave. I'd ask for it as a steering decision, then deliver it well, and fight to keep the financial core, the ledger and everything that posts to it, in one transaction inside one service.

**Trap:** Calling microservices 'overkill' dogmatically or saying he'd never split; no answer for how boundaries are enforced; caving instantly to the buyer; saying '50 people' without scoping it to one module's teams (the program team already passes 50).

Source: Modular monolith and financial core, p.6; Trade-off 'Architecture', p.18; Reference glossary (transactional outbox), p.6; speaker notes 'rejected' (50-person trigger). Build-failing tests and handling an overrule are not in documents.

### Be candid: how much of this case study did AI produce, and how did you verify what it gave you?

*Asked by: Hiring manager*

A lot of the drafting and analysis was AI-assisted, and every number and decision in it is mine to defend. I used AI the way the plan does: it drafts, tools check, I sign. Every code count comes from plain command-line tools on the real repository at one fixed commit, so anyone can re-run it. The money figures come from re-running the cost model, so the deck, case study and study sheet agree. A review pass caught real mistakes in the first draft: 50 moves a night that ignored tax-deadline blackouts, 'under three weeks' written as 21 days, one saving counted twice. And I label what's unproven: the rounding gap is emulated, not yet run on the real runtimes.

**Follow-up:** Give me one concrete thing in the first draft that was wrong and that you caught.

The calendar. The first draft scheduled 50 customer moves a night as if every night were usable. But you can't cut a customer over between the 10th and the 25th, when filings fall due, or from mid-December to mid-February. Redone properly, it's 100 a night on about 10 usable nights a month, roughly 1,000 a month against a planned peak of 650.

**Trap:** Downplaying AI use (dishonest and easy to spot), or over-crediting it ('the AI worked that out') so he can't explain a number when probed.

Source: Not in documents (his own process). Supporting: codebase-facts.md (counts from find, grep, wc at commit 2320f1c); what-not-to-do 'Traps a reviewer caught'; Reference p.3 (rounding emulated) and p.5 (cost model script); Migration plan, p.14. CHECK BEFORE SAYING: make every process detail (who reviewed, what AI drafted) match what Kirill actually did.

### Say we put you on site Monday. Walk me through the first weeks: what do you do in week 1, and what do I see at day 30, 60 and 90?

*Asked by: Hiring manager, CTO, Delivery head*

Evidence first, then a platform. Week 1: we rotate the plaintext database password, start the legacy test harness and the rule-inventory parse, and ask customers for consent to analyze their forks. From week 2 the delivery team takes over the four legacy engineers' maintenance so they can review money rules. By day 30, the harness confirms or kills the emulated rounding finding, and the cost model is checked against a real cloud bill. By week 6, all 310 forks are classified. Around day 60 comes the week-8 go or no-go. By day 90, forks are frozen, two cells are live with isolation probes and an outside penetration test passed, and module teams are building.

**Follow-up:** Which single item in those 90 days worries you most?

The legacy harness. The plan assumes the old business objects run without the desktop screens. The code makes that likely, because business logic is separate from the UI and a server already runs those objects with no screens, but until it runs on the real runtimes, the to-the-cent safety net is a design, not a fact. That's why it starts in week 1. Commercially, the riskiest assumption is that accountants accept a browser app if keyboard speed matches.

**Trap:** Generic kickoff activities ('stakeholder interviews, onboarding'); forgetting the week-8 go or no-go; implying customers move in the first 90 days; reciting assumption or gate codes.

Source: Current-state, p.3 ('rotate it now'); L0, p.10; A13 (consent), p.4; Forks, p.7; Reference p.3-4 (rounding weeks 2-4; real bill week 4); gates P1-P2, p.20; Legacy end of life (forks frozen month 3), p.16; roadmap diagram; A9 and A12, p.4; codebase-facts (data portal server). Day-by-day sequence not in documents.

### Month 4: VAT equivalence is stuck below 100%, and first customers in month 5 won't happen. How do you tell the steering committee, and what do you ask them for?

*Asked by: Hiring manager, Delivery head, CTO*

I tell them the day I know, not at the next meeting, and I bring options, not just news. One page: what slipped and why, what it moves, what it doesn't touch. The impact: 70% has only 30 customers of slack, so a one-month slip moves 70% about a month, and into the mid-December freeze up to two months more; a three-month slip takes cash payback from month 44 to about 49. Then three options: add capacity on VAT; if the gap is half-cent cases, have the accountants approve them once, as a class, under the tolerance policy; or accept the new date. What I won't offer is a lower gate. No customer moves until their numbers match to the cent.

**Follow-up:** The CEO says: move the simple customers anyway, VAT can wait. Or just override a red guardrail to make 70%.

I'd say no, and explain it isn't stubbornness. The first-customer gate itself needs VAT to pass, because almost every customer invoices with VAT, and once the tax authority accepts a cloud filing we can only fix forward. The committee can change dates, scope or wave order, but not waive a mismatch to the cent, and I'd ask the board to agree that rule at week 8, before anyone is under pressure. Meanwhile I'd pull other ready work forward, like mapping forks to extension manifests.

**Trap:** Softening or delaying the news; blaming the client team; offering to relax the to-the-cent gate to save the date; saying 'the steering committee decides' about isolation or correctness.

Source: Migration plan, p.13-14; sensitivity (slip: month 49), p.19; L3 tolerance policy, p.11; KPI dashboard, p.16; gate P3, p.20; Rollback, p.16. How to communicate a slip and the no-override rule are not in documents.

### First customers in month 5 on a rewrite of 522,000 untested lines. Why should I believe that, and what single item is most likely to make you miss it?

*Asked by: Delivery head, Skeptic*

I believe it because month 5 is a narrow first step, not the whole product. The first wave is the firm's own books plus 19 volunteers on five pieces: ledger, invoicing and VAT, payables, bank import and VAT filing. Ledger, invoicing and payables are about 53,000 lines, not 522,000; bank import is rebuilt on standard libraries. And it's a gate, not a promise: if those five don't match to the cent, or power users aren't as fast on 90% of their top 25 workflows, the wave waits. The item most likely to bite is the harness: if the old business objects won't run without their desktop screens, I have no answer key. That's why it has to run by week 8.

**Follow-up:** The firm's own books in wave 0? The firm surely runs payroll, and payroll isn't ready until month 7.

Fair catch, and I'd confirm it in discovery. A customer moves only when every module it uses has passed equivalence, and only one system may write its books, so we can't split payroll off. If our own payroll runs in Apskaita5 today, our books move with payroll in wave 2, and the volunteers carry wave 0.

**Trap:** 'AI makes it fast'; implying the whole product ships in month 5; naming the cloud platform as the critical path; presenting the date as a commitment rather than a gate.

Source: Migration plan wave table and ordering rules, p.13; L1 module table (17,035 + 24,704 + 11,475 lines), p.10-11; gate P3 and P4, p.20; web client speed parity, p.6; A12, p.4; G0, p.15. The wave-0 payroll conflict is a fact-checker flag, not in documents.

### You promise 20 days for every customer from month 4, legacy included. That means automatically building all 310 hand-maintained forks. You called it your boldest promise. What happens when 60 of them won't build?

*Asked by: Tax and accounting, Skeptic, Hiring manager*

Then those customers get the change by hand patch, as they do today, and some may miss 20 days; I'd report that, not average it away. It is the boldest promise in the plan, which is why I say it first. Why it's plausible: all 310 forks are diffed and classified by week 6, they freeze in month 3, and the fast lane reuses the same analysis and golden test files as the cloud pipeline, so each change is analyzed once, not 310 times. The fallback is ordered: biggest forks first, the tail patched by hand. And turnaround is measured for legacy customers too, so the dashboard shows it if the fast lane falls behind.

**Follow-up:** So honestly, is the 3-week target met for every customer from month 4?

It's the plan from month 4, but it's proven in steps, and the dashboard says so: the first pack change measured within 20 days is the month-6 target, and every change within 20 days is the month-9 target. Until then, a form not yet on packs ships as reviewed code: a cloud release on any day, and the fast lane for legacy customers. If anything misses, it's the small forks at the end of the list, and they get hand patches meanwhile.

**Trap:** Insisting all 310 forks will build; quietly narrowing the promise to cloud customers; not knowing the KPI trajectory only proves it at months 6 and 9.

Source: Statutory variability, legacy fast lane, p.6-7; Forks, p.7; Legacy end of life, p.16; KPI dashboard (turnaround for cloud and legacy), p.17; Reference KPI trajectory, p.5-6; speaker notes 'statutory' (fallback); study sheet 'Say it first'.

### Your whole savings case rests on the 3.1M EUR being hosting only. That's an assumption. What if half of it is people or licenses?

*Asked by: CFO*

You're right, it's the assumption the cash case leans on most, which is why it's one of the 13 we confirm in the first eight weeks. Every euro of the 3.1M that isn't hosting is a euro a year off the savings, because the cloud side, about 1.3M EUR a year at full scale, doesn't change. A baseline about 0.45M EUR lower looks roughly like our cloud-plus-35% case: payback in year 5. If half of it were people or licenses we keep paying, savings would shrink to around 0.3M EUR a year and the cash case would be gone. I'd tell you that at week 8, and we'd decide on risk and speed alone, or stop.

**Follow-up:** And the 1.26M EUR cloud figure, isn't that just list prices too?

Yes, a planning estimate from list prices, checked against a real cloud bill in week 4. About 40% is the seven cells, a quarter is the shared platform, and the rest is dedicated databases for the largest customers and AI. One honest gap: the standby copy in a second EU region for disaster recovery has no line of its own yet. The week-4 bill settles it; my rough estimate, up to about 80 EUR per customer, fits inside the 35% overrun case at full scale.

**Trap:** Treating 3.1M as a known fact; not knowing that cloud cost stays the same whatever the baseline turns out to be, so every euro of baseline error comes straight off the savings.

Source: A2, p.3; Business impact, p.18-19; Reference cloud cost inputs, p.4-5. Baseline scenarios derived by re-running the cost model; the DR standby estimate is not in documents.

### When does your 20-day statutory clock start? In real life VMI or Sodra publish the final form or XML schema days before it takes effect. What then?

*Asked by: Tax and accounting*

The clock starts at official publication and stops when the signed rule pack, our bundle of tax settings, is live in production. The pipeline takes about 10 working days: AI compares the law, form and XML schema, an analyst writes the pack, we test it against golden files and a sample of real customers, and a chartered accountant signs. Worst case is 20 calendar days against a target of under 3 weeks, so the margin is about a day. If the final form lands days before the effective date, that date is the real limit, not our 20 days. So we build the pack from the draft, and the final schema becomes a small change that still goes through test and sign-off.

**Follow-up:** Where's the line between a rule pack and code? Take the 2019 social-insurance reform, the 1.289 gross-up hardcoded in legacy payroll.

Both. The 1.289 factor is data, but the 2019 reform changed how the calculation works, so that part ships as reviewed code, versioned with the pack and releasable on any day, so it meets the same 20-day limit. A pack holds dated rates and thresholds, form mappings, rounding policies and golden test files. We rejected a scripting engine on purpose: it's code a non-engineer can change outside code review, and that's hard to govern.

**Trap:** Claiming 20 days covers every case; mixing up 10 working days with 20 calendar days; calling the target '21 days'; hiding that the worst case leaves about a day of margin.

Source: Statutory variability, p.6-7; A11, p.4; statutory pipeline diagram, p.7; KPI dashboard (median 14), p.17; Trade-off 'Statutory', p.18; Reference code evidence (WageVDUInfo.vb, 1.289), p.2. Building the pack from a draft form is not in documents.

### Your accountants have lived in this desktop app's keyboard for fifteen years. They'll hate a browser. How do you reach speed parity, who decides it's met, and what if a big bureau refuses?

*Asked by: Architect, Delivery head, Tax and accounting*

I make speed parity a release gate, not a hope. The firm's heaviest users, bureau accountants included, time the 25 most frequent workflows side by side on legacy and web, and a module ships only when 90% are as fast or faster; the slower ones get a named owner and are re-timed. The key map copies what we read in the legacy code: Insert and Delete for rows, Enter and Tab across cells, type-ahead pickers, date shorthand like '5'. None of those are keys the browser reserves. The grid runs locally, targeting under 50 milliseconds from keystroke to screen. If a big bureau still refuses, it moves in the last wave; legacy's last tax update is month 18.

**Follow-up:** Doesn't one big bureau holding out eat your 30-customer margin?

It could: bureaus move as a portfolio, so one large bureau waiting could use up the 30 customers of slack at month 12. That's why every bureau gets a champion, early movers keep their price for 12 months, and I'd get bureau commitments early. If keyboard parity still isn't reachable for a module, the fallback is a thin desktop wrapper around the same web client.

**Trap:** Promising it will 'feel just like the desktop' without a measurement; treating the slower 10% as acceptable losses; claiming an installed web app unlocks browser-reserved keys; leading with training instead of the gate.

Source: Web client, p.6; A9, p.4; gate P3, p.20; Reference stack (Playwright keyboard tests) and non-functional targets (50 ms), p.3-4; codebase-facts (grid keys; almost no menu shortcuts); Migration plan and change management, p.13-14; Legacy end of life, p.16. Who times the workflows and bureau commitments are not in documents.

### Is a team of about 30 enough, and what happens when your four legacy engineers, who hold the knowledge and review every money rule, become the bottleneck, or two of them leave in month 2?

*Asked by: CTO, Delivery head, Skeptic*

I think about 30 is right, but it's an assumption: about 30 for a year, then about 10 for six months, alongside the firm's own engineers, with the exact size set in discovery from measured throughput. Most of them build new things, the platform, web client, migration factory and test harness, that don't need tribal knowledge. That knowledge funnels into one bottleneck we protect: the four engineers and an accountant review every money rule, and from week 2 the delivery team takes over their maintenance. If two left in month 2, it would hurt, but part of the inventory would already be written down, and the harness runs the old code as the answer key without anyone's memory.

**Follow-up:** Would you put retention bonuses on those four?

I'd recommend the firm consider it, but that's a leadership call, not mine, and the plan shouldn't depend on it. The real protection is guarding their review time and getting the money rules written down and reviewed early, ledger and VAT first by week 8, while they're fully engaged. If two did leave, the other two and the accountants carry the review, and you'd hear the schedule impact from me that week.

**Trap:** Defending 30 as a precise, validated number; brushing off the key-person risk; claiming AI replaces their knowledge; naming who supplies the delivery team.

Source: A6, p.4; L0, p.10; Business impact (investment), p.19; gate P1, p.20; Team and Top risks, p.21; L3 legacy oracle, p.11; study sheet (model 32, then 10). The departure scenario is not in documents.

### Your week-8 go or no-go depends on 95% precision for the rule inventory. Precision against what? And precision is the easy half: how do you know you haven't missed rules?

*Asked by: Head of AI*

Precision is measured against human review; completeness is checked mechanically and then by testing, never by the model. A Roslyn parser, the .NET compiler platform, maps 377 business classes, 797 rule registrations and all 770 SQL statements, and the gate requires every class, method and SQL statement mapped. Precision is the share of AI-written rule records the four legacy engineers and an accountant accept without a real correction, on ledger and VAT for week 8. But coverage isn't recall, since a rule can hide inside a method body. So the backstop is equivalence testing: legacy is the answer key, and replayed history plus a million generated cases a night surface a missed rule wherever they exercise it.

**Follow-up:** Both passes use the same model. Aren't their errors correlated?

Yes, they can share blind spots, which is why agreement between the two passes is never the gate; it only decides what reviewers look at first. The gate is human review of every money rule, a mechanical check that rejects any record citing source lines that don't exist, and equivalence testing against running legacy. Running the second pass on a different model family is a cheap option I'd test in discovery.

**Trap:** Treating 95% precision as proof the inventory is complete; implying the AI checks its own work; dodging the recall question.

Source: Layered AI gate table, L0, p.9; L0 comprehension and rule inventory, p.10; L3 test sets, p.11; gate P1, p.20; Reference codebase at a glance, p.1. The precision definition and the second-model option are not in documents.

### Your AI features read invoices, bank statements and ledgers. Where does that data go, is any of it used for training, and what has the provider committed to in writing?

*Asked by: Security lead, Head of AI*

Customer data goes only to EU-hosted models through one model gateway we control, and the plan requires no training on it. But I won't pretend that's signed yet: it's an assumption we confirm in the contract at the week-8 gate. The models are Azure OpenAI in the EU Data Zone and Document Intelligence, every feature has a per-tenant kill switch, and AI audit records are kept with the ledger. Extraction does see full invoice content, so it stays in the EU. Elsewhere the models see less than you'd think: the reporting model never writes SQL or produces a number, and the support assistant answers only from the manual, release notes and resolved tickets, which I'd index only after redaction.

**Follow-up:** Those resolved tickets are full of other customers' data. How do you stop the assistant leaking one tenant's details to another?

I'd clean tickets before they're indexed, so the shared index holds no one's books. I'd go further than redaction and rewrite each resolved ticket as a generic problem-and-fix entry. Anything about the user's own data goes through the app with their rights and row-level security, and search carries the tenant like everything else, under the hourly cross-tenant probes. I'll own that the plan calls for redaction in general but doesn't say the assistant's ticket pool is redacted or limited to the asking tenant; I'd make that explicit.

**Trap:** 'Microsoft guarantees it' or 'the data is anonymized'; stating the no-training term as already signed; claiming the assistant is harmless because it never reads books.

Source: Assumptions intro and A13, p.3-4; Platform and service levels, p.8; AI in the product and guardrails, p.12; Reference stack and data residency, p.3-4; Tenant isolation, p.5-6. Redacting the assistant's ticket pool is not in documents.

### This is a business-facing lead role. Why do you want it, and in this program what would you personally own, and what would you refuse to own?

*Asked by: CTO, Hiring manager*

I want it because the hardest part of this program isn't the architecture; it's getting a CTO, a CFO and thousands of accountants to trust it, and I want to own both halves. I'd own the technical case and the honesty of the numbers: architecture decisions, the week-8 gate evidence, the equivalence harness and its tolerance policy, and the steering dashboard, so when a number turns red you hear it from me first. I'd spend time with leadership and bureau customers, because 70% is as much adoption as engineering. What I wouldn't own is signing money rules or the go or no-go. The legacy engineers and accountants sign every money rule, and the steering committee makes the gate call.

**Follow-up:** How much code would you actually write?

Roughly a third of my time, more during discovery, where the risk is highest: the equivalence harness, money-code reviews and the cost model, so I can open a failing VAT comparison myself and explain it to the CFO in plain words. Pod leads own module features. My test: if I'm the bottleneck on a pull request, I'm too deep; if I can't answer a technical question in steering without phoning someone, I'm too shallow.

**Trap:** Generic lines about loving customers; claiming to own everything, including money-rule sign-off; wanting to escape either code or clients; naming who supplies the delivery team.

Source: Not in documents; consistent with Team, p.21; L0 review, p.10; tolerance policy, p.11; KPI dashboard, p.16-17; Executive summary decision request, p.2; L1 gate (two reviewers on money code), p.9.

## Ten more the panel may ask

### The firm has never run a 24/7 multi-tenant SaaS. When your delivery team rolls off after month 18, who operates this, and how do about 30 VB.NET engineers become a cloud and C# team?

The firm's own engineers run it, and the handover starts in month 1, not month 18. The dedicated team works alongside the firm's roughly 30 engineers from the start, pairing with them on the new C# code. Moving from VB.NET to C# is the smaller step; running a 24/7 cloud service is the bigger one, so the firm's people join releases and on-call during the waves, while the delivery team is still there. As maintenance falls from 62% of engineering time to 30% or less, about 10 engineers come free, and some of that capacity staffs the platform. In the last six months the smaller team is backup, not owner. Operations also get simpler: seven cells and about 126 dedicated databases on one release, instead of 4,200 databases upgraded by hand. My exit test: the firm ships a release and handles an incident on its own.

Source: Team, p.21 (team of about 30 for a year, then a smaller one for six months, alongside the firm's people); Assumption A6, p.4 (about 30 engineers in-house); Business impact, p.19 (62% to 30% or less, about 10 engineers back on the roadmap); Reference cost inputs, p.5 (7 cells, about 126 dedicated databases); Current state, p.2 (customers upgrade their own database by hand). Pairing, on-call during waves, the reskilling view and the exit test are not in documents.

### You're a .NET shop moving to Azure. Why PostgreSQL rather than Azure SQL, which also has row-level security? And what changes if the client turns out to be on AWS?

PostgreSQL, mainly for cost per cell and portability, not because SQL Server can't do the job. SQL Server has row-level security; MySQL, which they run today, doesn't, so staying on MySQL was out. The trade-off: SQL Server adds license cost in every cell, and we'd run seven cells plus about 126 dedicated databases. PostgreSQL works well with .NET through EF Core and Npgsql, and runs the same on Azure or AWS. Azure is an assumption: no cloud was named, the stack is .NET, and GDPR means EU regions, two for disaster recovery. On AWS the core maps to ECS Fargate, RDS PostgreSQL, SQS, S3 and KMS; identity, edge and AI need equivalents too, with EU-hosted models under the same no-training terms. We'd re-run the cost model, and I'd settle the cloud in week 1, since the platform build and the week-4 bill check depend on it.

Source: Trade-off analysis 'Database' row, p.18 (MySQL has no RLS; SQL Server adds license cost per cell); Assumption A1, p.3 (Azure, two EU regions, AWS works equally; no cloud named, .NET, GDPR); Reference stack, p.3-4 (EF Core with Npgsql; AWS equivalents ECS Fargate, RDS PostgreSQL, SQS, S3, KMS); Reference non-functional targets, p.4 (standby copy in a second EU region); Reference cost inputs, p.4-5 (7 cells, about 126 dedicated; real bill in week 4); A13, p.4 (EU-hosted AI, no training). SQL Server having RLS, portability as a reason, identity/edge/AI equivalents and the week-1 decision are not in documents.

### Make it concrete. Take one real business rule from the code and walk it through L0, L1, L2 and L3.

Take the 2019 social-insurance gross-up: a hardcoded year check at line 151 of the payroll code that grosses wages up by 1.289. At L0, the parser maps that class, and AI writes one record in two independent passes: what the rule does, its source lines, its inputs and its effective dates. A script checks the cited line really exists, and a legacy engineer and an accountant review it, because it's a money rule. At L1, the payroll kernel is translated to C#, while the factor and its dates move into the payroll rule pack; two reviewers approve the code. At L2, old payslips move exactly as legacy computed them, and payroll year to date reconciles to the cent. At L3, the rule gets its own test, replayed history from 300 customers exercises it, and a mutation test changes 1.289 on purpose to prove the harness catches it.

Source: Reference code evidence, p.2 (WageVDUInfo.vb line 151, 2019 gross-up of 1.289); codebase-facts (20 hardcoded year comparisons, including the gross-up); L0, p.10 (two independent passes; statement, source lines, inputs, effective dates; mechanical line check; engineers and an accountant review every money rule); L1 gate p.9 (two reviewers on money code) and payroll row p.10 (kernel translated; rates and 20 year-specific rules to rule packs); L2, p.11 (payroll year to date reconciled to the cent; history never recalculated); L3, p.11 (300 tenants' replayed history, one test per rule, mutation tests). Checked in the repo: line 151 is `If calculationDate.Year > 2018 AndAlso _Year < 2019 Then _Wage = CRound(_Wage * 1.289, 2)`.

### Where do your thresholds come from? 95% at L0, 100% at L2 and L3, 97% for extraction, 99.5% for auto-posting, 60% for anomaly flags. They look picked to sound good.

They follow one rule: the closer a step gets to changing someone's books without a person, the higher the bar. Migrated totals and equivalence are 100%, because a miss there is a wrong number in a customer's books. L0 is 95% because every money rule gets human review anyway; the threshold tests whether AI drafts save reviewers time, and L3 catches what review misses. Extraction drafts launch at 97% field accuracy because a person approves every posting. Auto-posting acts alone, so it needs 99.5% of complete entries correct on 1,000 or more reviewed invoices in shadow mode, plus a per-tenant limit, one-click reversal, and a 0.5% error guardrail after launch. Anomaly flags only ask for attention, so 60% useful is enough to launch. I'll be honest: the non-100% figures are planning choices that discovery data could move. The 100% gates on money don't move.

Source: Layered AI gate table, p.9-10 (95%, 100% control totals, 100% equivalence); AI in the product, p.12 (97% field accuracy; a person approves every posting at launch; 99.5% of complete entries on 1,000+ reviewed invoices in shadow mode; tenant limit and one-click reversal; 60% useful flags); KPI guardrails, p.17 (AI auto-post errors under 0.5%). The unifying rule and the L3 backstop reasoning are not in documents.

### Walk me through your target architecture with one transaction: an accountant posts a sales invoice, and later the VAT return goes to VMI.

Only the posting itself is synchronous; everything slow happens afterward. The accountant types in the browser grid, which runs locally, so keystrokes don't wait on the network. Saving goes through the edge, which checks the firewall rules and the user's identity and routes the request to that tenant's cell. Inside the monolith, one database transaction sets the tenant, validates the command, and posts across the four modules involved, with a unique key so a retry never posts twice; the target is under 300 milliseconds. In that same transaction, an event goes into the outbox. Workers pick it up afterward, and heavy reports read from the cell's read replica. For the VAT return, the engine uses the rule pack in force for that period and records its version; a person submits it, and the filing gateway sends it to VMI.

Source: Target-architecture diagram, p.5 (edge with WAF, identity and tenant routing; cells; read replica for reports; filing gateway to VMI and Sodra); Tenant isolation, p.5-6 (tenant set per transaction); Modular monolith and ledger rules, p.6 (four modules in one transaction; outbox; unique posting key); Statutory variability, p.6 (effective-dated packs; pack version recorded); Trade-off 'Language and UI', p.18 (Blazor Server sends every keystroke over the network); AI in the product, p.12 (nothing AI-driven files); Reference non-functional targets, p.4 (API under 300 ms at the 95th percentile). 'A person submits' is not stated in documents.

### Those four legacy engineers will see this as the program that replaces them. How do you get them on your side in week one?

I'd make them the most important people in the program, because in this design they are. Their knowledge becomes the rule inventory, and every money rule moves only after one of them and an accountant review it. From week 2 the delivery team takes over their maintenance work, so their week shifts from firefighting to review. In week one I'd sit with them, show them my code findings, including the rounding mismatch I've only emulated, and ask them to correct me before anything is locked in. And I'd be straight about their future. The plan frees about 10 engineers for product work, and these four are the obvious people to own the new financial core, not to retire with the old one. Retention terms are the firm's call, but protecting their time and making their judgment visible is mine.

Source: L0, p.10 (four engineers and an accountant review every money rule; delivery team takes over their maintenance from week 2); Current state, p.2, and Reference, p.2 (rounding disagreement found by emulation, confirmed on real runtimes in weeks 2 to 4); Team and Top risks, p.21; Business impact, p.19 (about 10 engineers back on the roadmap). How to win them over and their future role are not in documents.

### Your hypercare rollback replays cloud documents back into legacy, a schema with DOUBLE money and no foreign keys. Isn't the way back as risky as the way forward?

It's narrower than the way forward, and it's rehearsed before anyone needs it. Going back, we don't move a customer's history: their legacy database was set read-only at cutover and is still there. We only replay documents they entered in the cloud since go-live, at most 35 days of work, and restore legacy write access. The round trip back to legacy is proven lossless in the full rehearsal a week before every cutover, with control totals checked to the cent, so a customer whose way back fails rehearsal doesn't move. The honest limit: rehearsal proves the mapping on their existing data, not on documents typed after go-live, and writing exact decimals back into floating point is the delicate step. So I'd reconcile each replay to the cent before legacy reopens. Impact is a few hours offline with no entered data lost, and rollback above 2% pauses new cutovers.

Source: Rollback paths diagram, p.15 (reverse ETL replays cloud documents into legacy; write access restored; a few hours offline, no entered data lost; at most 35 days; 2% circuit breaker); Coexistence, p.14 (database set read-only at cutover); Cutover runbook, p.14 (T-7 full rehearsal, round trip proven lossless); Validation gate G1, p.15; reverse path rehearsed at every G1, p.16; guardrails, p.17. The rehearsal's limit, the decimal-to-floating-point point and per-replay reconciliation are not in documents.

### Today the desktop app works without internet, and the code even supports a local SQLite file instead of a MySQL server. What happens to an accountant on a bad connection at month end, and to customers on SQLite?

The web client needs a connection to save, and I'd say that plainly rather than promise offline posting. Offline writes would mean two copies of the books that later have to merge, which is exactly what one writer per customer rules out. What I can do: the grid runs locally, so typing never waits on the network, saves target under 300 milliseconds, and availability rises to 99.95% from the 15th to the 25th, when filings fall due. I'd also keep an unsaved draft in the browser until it saves. On SQLite: some customers may keep books in a local file outside the hosted fleet, and I'd count them in discovery. A local file also escapes our cutover lockout, so I'd first convert it to hosted MySQL with the converter the old app already has, then move it like everyone else, likely in a later wave.

Source: codebase-facts (one MySQL database or SQLite file per company); Reference code evidence, p.2 (770 MySQL and 761 SQLite statements); Coexistence, p.14 (one writer; MySQL grants revoked and database set read-only at cutover); Trade-off 'Migration', p.18 (two-way sync lets books drift); Reference non-functional targets, p.4 (API under 300 ms, 99.95% from the 15th to the 25th); Web client, p.6. Checked in the repo, not in documents: AccDataAccessLayer/.../DatabaseStructure/MigrationMethods.vb line 202, ConvertSQLiteToMySql. Offline drafts, the SQLite count and the conversion step are not in documents.

### What's in it for the 4,200 customers? Why would a bureau want to move, and what happens to their price after your 12-month hold?

For customers, the move removes chores and risk. No more upgrading their own database by hand, supplier invoices drafted by AI instead of typed, and for bureaus one login across all their companies with nothing to install or maintain. Faster tax changes aren't the reason to move, because legacy customers get those too from month 4. The honest push is the calendar: end of life is announced in month 9, and legacy's last tax update is in month 18. The 12-month price hold rewards going early; what happens after it is the firm's pricing decision. My business case doesn't model revenue at all; cash counts only infrastructure savings. I'd want the firm's commercial lead to set post-hold pricing before wave 3 in month 8, when bureau portfolios move, because a price surprise there would hit the 70% target hardest.

Source: Current state, p.2 (customers upgrade their own database by hand); Assumption A4, p.3 (one login across companies); L1 Payables row, p.10, and AI in the product, p.12 (AI extraction of invoices); Executive summary, p.1, and legacy fast lane, p.7 (20 days at most for every customer, cloud or legacy, from month 4); Legacy end of life, p.16 (announced month 9; last statutory update month 18); Change management, p.14 (early movers keep their price for 12 months); W3, p.13 (months 8 to 10, bureau portfolios); Business impact, p.18-19 (cash counts infrastructure savings; freed time not cash). 'Nothing to install', post-hold pricing and its timing are not in documents.

### Beyond this client, what from this engagement is reusable? If we had three more legacy .NET ERPs next quarter, what would carry over?

The method carries over almost entirely; the domain content doesn't. Four pieces are reusable. First, the comprehension pipeline: Roslyn reads both VB.NET and C#, so any legacy .NET code becomes a map, AI writes rule records with cited source lines, and any record whose lines don't exist is rejected. Second, the headless legacy harness and differential testing, with mutation tests that prove the harness catches errors; any system whose logic is separate from its UI can be its own answer key. Third, the migration factory: control totals to the cent per tenant, weekly fleet rehearsal, and a rehearsed way back. Fourth, the gate pattern: AI drafts, tools check, a named person signs against a threshold. What doesn't transfer is what's inside the rule packs: the Lithuanian payroll and VAT knowledge. I'd expect a second engagement to start faster, but I wouldn't quote a number before measuring one.

Source: Not in documents as a reuse claim; consistent with Reference technology stack, p.4 (Roslyn analyzers for VB.NET and C#), L0-L3, p.9-11, and Migration plan, gates and rollback, p.13-16.

## Questions to ask the panel

1. On an engagement like this, does the forward-deployed lead own the client's business case and steering-committee relationship end to end, or does that sit with an account or engagement lead while the FDE owns the technical case? Where does that line fall in practice?
2. When the FDE's honest read is that a date or number already sold to the client is at risk, how does Persistent want that raised, to whom first, and how fast? What happened the last time it came up?
3. In the modernization deals you're seeing now, what actually stalls clients: funding the first gate, trusting AI-generated code in money paths, or security and data-residency sign-off? Which of those would hit a plan like mine first?
4. What AI-assisted modernization tooling does Persistent already run in production, for code comprehension, translation or equivalence testing, and where would you expect an FDE to build versus reuse?
5. Six months in, what would make you say this hire was clearly the right one? Do you measure an FDE on client outcomes, follow-on work, or reusable assets the delivery teams pick up?

## Full bank by panelist

## CTO

### Let's start with the big bet. Why rebuild at all? Why not rehost it in the cloud, refactor it in place, or just buy an off-the-shelf cloud ERP with a Lithuanian localization?

I chose a rebuild because it's the only option that fixes cost, tax-change speed and the 310 forks at the same time. Rehosting lifts 4,200 separate databases into the cloud, so the bill still grows with every customer, and tax changes stay slow because every tax-form version is still a copied class. Refactoring module by module means the old and new systems both write one ledger during the transition, and that's where financial errors hide. It also isn't a blank-page rewrite: we translate the calculation kernels and rebuild the shell around them. Buying is really a business-model question. This firm is the vendor, so buying means reselling someone else's product, still migrating all 4,200 customers, and rebuilding Lithuanian tax depth and 310 customizations on a platform it doesn't control. AI is what makes the rebuild fit in 12 months.

**Follow-up:** Did you actually evaluate a cloud ERP like that? What would make buying the right answer?

Not in depth in this case study, and I'd say so plainly. Buying becomes the right answer if the firm decides its value is services and bureau relationships rather than owning the product. I'd test that before the week-8 gate with one comparison: run cost per customer and tax-change turnaround on a localized off-the-shelf ERP, measured against our targets of 406 EUR per customer a year and 20 days.

**Trap:** Waving off 'buy' as obviously wrong, or pretending he did a full vendor evaluation he didn't do; also calling the plan a blank-page rewrite when it translates the kernels.

Source: Trade-off analysis, 'Strategy' row, p.18; L1 'translate the kernel, rebuild the shell' table, p.10-11; Current-state findings (copied tax-form classes), p.3; what-not-to-do (rejected paths: rehost, manual rewrite); study sheet ('By module? Two systems would write one ledger'). The 'buy' option is not in documents.

### Cash payback in year 4 on about 4 million euros. Most of my cloud programs pay back in two. Why should anyone fund this?

Because this is about risk and speed, not just savings. Infrastructure savings alone pay back about 4M EUR in year 4, around month 44, with about 2.5M EUR net cash over five years. If you count freed support and engineering time it's closer to month 35, but I don't count that as cash unless spending actually falls. What the money really buys: tax changes in 20 days instead of 10 to 14 weeks, against a 6-week legal window, so the firm stops missing statutory deadlines. The 310 forks go away. Engineers get off a frozen 2006 stack, and maintenance drops from 62% of their time to 30% or less, which puts about 10 engineers back on the roadmap. These are planning estimates, and I re-check them against a real cloud bill in week 4.

**Follow-up:** What's your downside case?

The worst single case is cloud costing 35% more than planned. That lands exactly on the 406 EUR target, pushes payback to about month 56 and cuts five-year net cash to about 0.6M EUR. Waves slipping three months gives about month 49, and team costs 25% higher about month 50. None of these turns five-year net cash negative. Cloud cost is the one I watch most, which is why the bill check sits in week 4.

**Trap:** Counting freed time as cash to make payback look better, quoting decimals, or getting defensive about year 4.

Source: Business impact, p.18-20 (month 44, month 35, 2.48M EUR five-year net cash, 62% to 30%, about 10 engineers); cost-model-output (payback months, sensitivity); Reference cost inputs, p.4 (validated against a real bill in week 4); speaker notes, 'payback' slide

### Be straight with me. How confident are you in this 12-month plan, and what's most likely to slip?

Honestly, I'm confident in the method and least confident in the 70% date. The plan moves 2,970 customers by month 12 against a 2,940 target, so there are only 30 customers of slack. A slip moves 70% out month for month, and if it runs into the mid-December to mid-February cutover freeze, it adds up to two more months. Capacity isn't the risk: the migration factory can move about 1,000 customers a month against a planned peak of 650. Readiness is the risk. If payroll or inventory passes equivalence testing late, every customer who uses that module waits. Separately, rebuilding all 310 legacy forks by month 4 for the tax fast lane is the boldest promise in the plan. The fallback is to rebuild the biggest forks first and patch the long tail by hand. I'd rather tell you that now than in month 10.

**Follow-up:** If you start slipping, what do you cut to hold month 12?

I don't cut the correctness gates; I'd let the date move before I did that. What I can change is order and pace. The factory has room for about 1,000 customers a month against 650 planned, so I'd pull ready, simpler customers forward and push customers with heavy forks to the last wave. If 70% still slips, you hear it early as a month-for-month slip, not as a surprise in month 11.

**Trap:** Saying 'very confident' or making up a probability; or hedging so much that it sounds like there's no plan.

Source: Migration plan, p.13-14 (wave plan, 30-tenant slack, freeze, ordering rule, factory capacity); Statutory variability, legacy fast lane, p.7; speaker notes, 'goals', 'statutory' and 'migration' slides; study sheet ('biggest forks first')

### What would make you stop this program? Give me your kill criteria.

I'd recommend no full rollout at the week-8 gate if any of three things fails. First, the old code can't run headless as the answer key for testing; the whole to-the-cent safety net depends on it. Second, the AI rule inventory can't reach 95% precision on ledger and VAT, which would mean AI-assisted code reading doesn't scale. Third, one I'd write into the gate explicitly: the week-4 cloud bill puts cost per customer above the 406 EUR target, about a third over my estimate, which misses the brief's 45% cost goal. That's why the ask is about 0.6M EUR first, not 4M. After week 8, guardrail breaches pause new cutovers rather than stop the program: a correctness incident, rollback above 2%, or a failed isolation probe. Even if we stop, the firm keeps the inventory, the classified forks and the test harness.

**Follow-up:** Who makes the stop call? You?

No. I bring the evidence, and the steering committee makes the call against criteria written down before we start. Writing them down in advance is the whole point: it stops money already spent from making the decision. My job is to make sure the gate shows real evidence, not a status color.

**Trap:** Saying nothing would make him stop, or giving vague criteria; mixing up pausing cutovers with stopping the program.

Source: Executive summary, 'Decision requested', p.2; P1 gate, p.20; Assumption A12, p.4; sensitivity (cloud +35% lands on 406 EUR), p.19; Guardrails, p.17; Reference cost inputs, p.4. The cost threshold as a stop rule and any post-week-8 stop criteria are not in documents.

### How does AI actually change the economics here? If I took AI out, what happens to cost and timeline, and what if it underdelivers?

AI changes the calendar more than the bill: it speeds up reading and drafting, not proof. Rewriting 522,000 untested lines by hand doesn't fit in 12 months, and the unwritten rules get lost along the way. With AI, a parser's map of 377 business classes and about 800 rules becomes a reviewed rule inventory, all 310 forks are classified by week 6, and AI drafts the C# translations and web screens. But the pace is still set by things AI doesn't shorten: the equivalence harness, two reviewers on every money change, and overnight customer moves. AI tooling and usage is only about 0.25M EUR of the 4M; the team is most of the cost. If AI underdelivers, there's a set fallback: if acceptance stays low for two sprints, engineers take over that module. I didn't model a no-AI version, so I won't quote you a number for one.

**Follow-up:** And AI in the product: does it make money or just cost money?

Mostly it saves support cost; I didn't book any new revenue from it. It runs at about 4 EUR per customer a month. Tickets fall from 6,500 to about 3,900 a month, partly because the assistant aims to resolve 30% of contacts without an agent, and that freed support time, about 0.4M EUR a year from year 3, isn't counted as cash. And nothing AI-driven files a return, pays a salary or touches a closed period.

**Trap:** Selling AI as a big cost cutter, or making up a no-AI savings number the documents don't contain.

Source: Layered AI, p.9-11 (L0 parser counts, L1 fallback rule, two reviewers on money code); Forks, p.7; Trade-off analysis, 'Strategy', p.18; what-not-to-do (manual rewrite); Reference, investment breakdown, p.5. Follow-up: AI in the product, p.12; tickets, p.20; freed support time, p.19; Reference AI cost 4 EUR per tenant a month, p.5. The no-AI counterfactual and any product AI revenue are not in documents.

### Walk me through the first 90 days. What will I actually see at day 30, day 60 and day 90?

The first 90 days buy evidence first, then a platform. In week 1 we rotate the plain-text database password and start the legacy test harness and the AI rule inventory. From week 2 the delivery team takes over the four legacy engineers' maintenance, so they can review money rules. By day 30, the harness confirms or kills our rounding-mismatch finding, which so far comes only from emulation, and the cost model is checked against a real cloud bill. By week 6, all 310 forks are classified. Around day 60 comes the week-8 go or no-go: assumptions confirmed, the inventory at 95% precision on ledger and VAT, the harness running. By day 90, forks are frozen, two cells are live, isolation probes and an outside penetration test have passed, and the module teams are building ledger, VAT, payables, bank import and payroll.

**Follow-up:** What's the single riskiest item in those 90 days?

The legacy harness. The plan assumes the old business objects run without the desktop UI. The code suggests they do, because logic is separate from the UI, but until it runs on the real runtimes, the to-the-cent safety net is a design, not a fact. That's why it's in the first weeks, not month 3.

**Trap:** Listing activities with nothing an executive can check, forgetting the week-8 go or no-go, or implying customers move in the first 90 days.

Source: Current-state assessment, p.3 ('rotate it now'); L0, p.10; Forks, p.7; Reference code evidence, p.3 (rounding confirmed in weeks 2-4); Reference cost inputs, p.4 (real bill in week 4); gates P1-P2, p.20; Legacy end of life, p.16 (forks frozen month 3); roadmap diagram (module pods A and B from month 2)

### This is a business-facing lead role. In this program, what would you personally own, and what would you refuse to own?

I'd own the technical case end to end and the honesty of the numbers. That means the architecture decisions, the week-8 gate evidence, the equivalence harness and its tolerance policy, and the steering-committee dashboard, so when a number turns red you hear it from me first. I'd also spend real time with the firm's leadership and bureau customers, because hitting 70% is as much adoption as engineering. What I wouldn't own is sign-off on money rules, or the go or no-go itself. The firm's four legacy engineers and its accountants sign every money rule and every deviation from legacy behavior, and the steering committee makes the gate call. That's deliberate: AI drafts, tools check, people sign, and the people who sign should be the ones accountable for the books.

**Follow-up:** How would you split your time between the executives and the engineers?

I'd spend most of the first eight weeks on engineering, because that gate is about evidence. From the first customers in month 5, I'd spend more time with the firm and its bureaus, because adoption and cutover calendars become the limit. The weekly dashboard keeps both sides on one set of numbers.

**Trap:** Claiming to own everything, including money-rule sign-off, or staying vague; naming who supplies the delivery team.

Source: Not in documents (consistent with Team, p.21; L0 review, p.10; tolerance policy, p.11; KPI dashboard, p.16-17; plain-English summary: 'any difference is fixed or signed off by an accountant')

### How would you report progress to me and my board? What do I look at every month?

One page, refreshed weekly from live data and reviewed monthly by the steering committee: seven KPIs against plan, with five guardrails underneath. For the board, I'd lead with four: customers migrated against plan, run cost per customer, tax-change turnaround in days, and realized savings. The guardrails are correctness incidents, rollback rate, tickets per customer, isolation probes and AI auto-post errors. If any one turns red, new cutovers pause. I'd show realized savings honestly. The run rate sits at about minus 0.4M EUR a year through month 9, while we pay for both systems, breaks even around month 12, and reaches 1.84M EUR a year from month 21. I'd rather you see that dip coming than be surprised by it. AI code acceptance is tracked to steer the method, never as a target.

**Follow-up:** What's the earliest warning sign that we're in trouble?

The equivalence pass rate per module and the weekly fleet rehearsal. If a module isn't at 100% equivalence weeks before its wave, or the weekly rehearsal of all 4,200 databases keeps failing on the same data problems, the wave date is at risk long before customer numbers show it.

**Trap:** Leading with activity metrics, or treating AI acceptance as a success measure; hiding the negative savings dip before month 12.

Source: KPI dashboard and guardrails, p.16-17; Reference KPI trajectory, p.5-6 (realized savings -0.38M EUR at months 6 and 9, break-even at month 12, 1.84M EUR from month 21); KPI dashboard diagram

### Your rollback ends once a customer files from the cloud. Say in month 8 you find a VAT error affecting a few hundred customers who've already filed. Walk me through it.

We stop, contain, fix forward and correct the filings. First, a correctness incident is a guardrail breach, so all new cutovers pause right away. Second, every calculation records the rule-pack version it used, so we can name exactly which customers, periods and documents are affected instead of guessing. Third, we fix forward. The fix goes through the same equivalence tests, and posted entries are never edited: corrections go in as reversals, so the audit trail stays intact. Then each affected customer gets corrected returns prepared for their review. Nothing AI-driven files on its own. The plan makes this unlikely, with 100% equivalence on ledger, VAT and payroll before a module ships, and mutation tests that prove the harness catches a flipped rate. But I won't tell you it can't happen.

**Follow-up:** Why not keep rollback open after the first filing?

Because once the tax authority accepts a return produced in the cloud, legacy no longer holds the record of what was filed. Rolling back would mean two sets of books drifting apart, which is exactly what the design avoids. Before that point, during hypercare of up to 35 days, we can put a customer back on legacy within hours with nothing lost.

**Trap:** Claiming it can't happen because of 100% equivalence, or proposing a rollback to legacy after a filing was accepted.

Source: Rollback, p.15-16; Guardrails, p.17; ledger rules and rule-pack versions, p.6; L3, p.11; AI in the product, p.12; cutover runbook (hypercare to day 35), p.14. The corrected-filing process is not in documents.

### Your plan leans on four engineers who hold all the knowledge, plus a team of about 30 you haven't sized yet. What happens if two of those four leave in month 2?

It would hurt and cost time, but it shouldn't stop the program. The first eight weeks exist to move knowledge out of four heads into a checked inventory. AI drafts one record per rule with its source lines, a mechanical check rejects any record that cites lines that don't exist, and those engineers plus an accountant review every money rule. From week 2 the delivery team takes over their maintenance, so their time goes to review, not firefighting. If two left in month 2, much of the inventory would already be written down, the other two and the accountants would carry the review, and the legacy harness runs the old code as the answer key without anyone's memory. The team of about 30 is an assumption. I size it in discovery from measured delivery and migration speed, and if it comes out bigger, you hear it at week 8.

**Follow-up:** Would you put retention bonuses on those four?

I'd recommend the firm consider it, but that's a leadership call, not mine, and the plan shouldn't depend on it. The real protection is guarding their review time and getting the money rules written down and reviewed early, ledger and VAT first by week 8, while they're fully engaged.

**Trap:** Brushing off the risk, or presenting the team of 30 as a fixed, validated number.

Source: Top risks, p.21; L0, p.10; Assumption A6, p.4; Team, p.21; L3 legacy oracle, p.11; P1 gate (assumptions confirmed), p.20. The departure scenario itself is not in documents.

## Architect

### You're proposing a modular monolith for a cloud SaaS product in 2026. Why not services from day one? And what stops nine modules in one deployable from turning back into the big ball of mud you're replacing?

A modular monolith, because the domain demands it. Posting one invoice touches four modules, and it has to commit as one transaction. Split those into services and every posting becomes a saga, a chain of steps that each need an undo, which is exactly where cents go missing. What stops the mud: each of the nine modules owns its own schema, modules talk only through published interfaces, and architecture tests fail the build if anyone crosses a boundary. Anything slow, external or untrusted already runs outside, fed by a transactional outbox, meaning events saved in the same transaction as the data: document extraction, the filing gateway, analytics and the migration factory. We scale by adding cells of about 600 tenants, not by splitting code. I'd split a module out later if teams pass about 50 people or its load diverges, and schema-per-module keeps that door open.

**Follow-up:** Which module would you split out first, and how would you do it without a distributed transaction?

Probably statements and e-filing. It only reads the books, its reports already run on the read replica, and its load spikes in filing week, so it's the likeliest to diverge. It sits off the posting path: it reads published data and hands filings to the gateway through the outbox, so splitting it needs no distributed transaction. The four modules an invoice posting touches stay together.

**Trap:** Calling microservices 'overkill' in general terms, or saying he would never split. Either sounds dogmatic. Also a trap: having no answer for how module boundaries are enforced.

Source: Target architecture: Modular monolith and financial core, p.6; Trade-off analysis (Architecture), p.18; target-architecture diagram (read replica for reports), p.5; speaker notes, slides 'target' and 'rejected'. 'Published interfaces' and the follow-up's choice of module are not in documents

### Forced row-level security on a pooled database. Walk me through exactly how the tenant gets onto a connection when connection pooling is involved. What happens when a developer forgets, or a background worker picks up a message without setting it?

The tenant is set inside every transaction, never on the session, so it can't leak across pooled connections. Concretely, the request pipeline opens a transaction and sets a transaction-local tenant value first; it vanishes at commit or rollback, so the next request that borrows that connection starts with no tenant. The row-level security policy reads that value; if it's missing, the policy fails closed and returns nothing, and the app refuses any request with no tenant before it reaches the database. Security is forced, and the app role isn't the table owner, isn't a superuser and has no bypass right; migrations use a separate role. Workers take the tenant from the message itself, since every event carries it, and set it the same way. Behind that, the tenant is in every key, and hourly cross-tenant probes block a release if anything leaks.

**Follow-up:** RLS adds a filter to every query. What does that do to performance on your biggest tables?

Very little, if the schema is built for it, and ours is: the tenant is part of every key, and every index leads with it, so the policy filter matches the index the database would use anyway. Policies stay a simple equality on the tenant, with no per-row function calls. And each cell is sized for three times filing-week load, which we load-test on the live cells before any customer moves.

**Trap:** Saying the tenant is set when the connection opens. A session-level setting leaks to the next request that reuses the pooled connection. Also a trap: claiming RLS alone is enough without addressing owner or superuser bypass.

Source: Target architecture: Tenant isolation, p.5-6 (forced RLS, app role cannot bypass, tenant set per transaction, no-tenant request refused, tenant in every key and queue message, hourly probes); Reference: Non-functional targets (3x filing-week load), p.4. Pooler, role and index details are not in documents

### Your legacy schema has 67 tables, no foreign keys, money stored as DOUBLE, and no schema version, and customers upgraded it by hand. How do you get 4,200 of those into a keyed, decimal, tenant-scoped schema without changing a single historical number?

In three steps, and AI only drafts. First, pre-flight: legacy already ships a check-and-fix that compares a live database with the expected schema, so we use it to bring all 4,200 to one structure, then profile every one. Orphan rows that would break the new foreign keys are fixed first; a tenant isn't eligible until its data is fixed. Second, AI drafts the column mappings and inferred keys, and deterministic, restartable pipelines move the data. Money becomes exact decimals at each field's legacy precision, and history moves exactly as legacy computed it, never recalculated. Third, we reconcile per tenant to the cent: trial balance, VAT by rate and period, open items, stock, assets and payroll year to date. From month 4 we rehearse all 4,200 every week, so surprises show up in rehearsal, not on cutover night.

**Follow-up:** You said the five rounding implementations disagree. When you convert DOUBLE to decimal, whose rounding is right?

For history, neither: it moves exactly as legacy stored it, at its declared precision, and reconciliation proves no total moved. For new calculations, each rule pack declares one rounding policy; the half-cent cases where that differs from legacy are approved once, as a class, in the signed deviation register. To be candid, the 1-in-560 figure comes from emulating the code; the test harness confirms it on the real runtimes in weeks 2 to 4.

**Trap:** Saying 'AI migrates the data', or implying that historical values get re-rounded or recalculated during the DOUBLE-to-decimal conversion.

Source: L2: schema, tenant keys and migration, p.11; L3 tolerance policy, p.11; Current-state assessment, p.2-3; Validation gates (G0 'data fixed'), p.15; Reference: Code evidence (DatabaseStructureGauge.xml, schema compare and fix), p.2, and rounding emulation note, p.3. Reusing legacy's check-and-fix for pre-flight is an inference, not stated

### Six hundred tenants on one 16-core Postgres. On the 24th, everyone is filing and running month-end reports. What stops one heavy tenant from hurting the other 599? And where do the 600, and the 3 percent who get dedicated databases, actually come from?

Three things: sizing, routing and moving the big ones out. Each cell is sized for three times its average load in filing week, and reports and queries go to the cell's read replica, so month-end reporting doesn't compete with posting. The largest 3 percent, about 126 tenants, get a dedicated database running the same code, so the likeliest noisy neighbors aren't in the pool at all. Honestly, both numbers are planning estimates. Six hundred is 4,200 across seven cells, resting on my assumption that the median database is under 2 GB; the 3 percent is my cut for tenants too big or too busy to pool. We confirm the size assumption at the week-8 gate, the weekly rehearsal of all 4,200 from month 4 measures it, and two cells are live in month 3, before any customer, so we can load-test them.

**Follow-up:** Doesn't the dedicated tier bring back per-customer databases, the very thing you said was the root problem?

Partly, and deliberately at small scale. It's about 126 databases, not 4,200, on the same code and schema, upgraded by the same automated pipeline in the same release, not by hand. Today's problem isn't the database count alone; it's 4,200 hand-upgraded schemas and 310 code forks. The dedicated tier keeps one code base.

**Trap:** Presenting 600 or 3 percent as a measured or optimal number. Also a trap: forgetting that the dedicated tier brings back per-database operations and needs a clear threshold.

Source: Tenant isolation, p.5-6; Assumption A3, p.3; Gates P1 and P2, p.20; L2 weekly fleet rehearsal, p.11; Reference: Non-functional targets (3x filing-week load), p.4, and Cloud cost inputs (16 vCores, 7 cells, about 126 dedicated), p.5; target-architecture diagram (read replica: reports, queries), p.5. The basis for 3 percent and the load test are not in documents

### A hundred tenants a night. What is that number based on, what's the real bottleneck, and what happens to your 70 percent if night one only does 60?

It's a planning number from my size assumption, and the machine isn't the real limit. With the median database under 2 GB, the final extract fits between the 8 pm lock and loading at about 9, and tenants run as parallel jobs. A hundred a night on about 10 usable nights is roughly 1,000 a month, against a planned peak of about 650. What really paces us is readiness and people: a customer moves only once every module it uses passes equivalence testing, and each needs opening-balance checks, training and hypercare. If rehearsal shows 60 a night, that's about 600 a month, below the peak, and with only 30 customers of slack, we'd miss 70 percent at month 12. But weekly rehearsal from month 4 tells us about six months before the peak, and the fix is more parallel jobs, never skipping a gate.

**Follow-up:** Why only about 10 usable nights a month?

Because we never cut over while customers are filing. No cutovers from the 10th to the 25th, when returns fall due, and none from mid-December to mid-February, around year-end. That leaves roughly two weeks a month, and I plan on about 10 of those nights so there's room to rerun a failed tenant.

**Trap:** Defending 100 a night as if it were proven, or hiding that the 70% target has only 30 customers of slack.

Source: Migration plan (wave plan, slack, ordering rules, factory throughput), p.13-14; Cutover runbook (T0 20:00 lock and final extract, about 21:00 load and reconcile), p.14; Assumption A3, p.3; L2 weekly fleet rehearsal, p.11; Reference: Technology stack (migration factory as Container Apps jobs), p.3; wave-plan chart. People as the pacing factor is not in documents

### Your accountants have used a WinForms grid for fifteen years. A browser grabs keys like F5 and Ctrl+W, and every save crosses the internet. How do you actually reach speed parity, and what happens if a module misses your 90 percent?

Parity is a release gate, not a hope: a module that misses it doesn't ship. We copied the key map from the legacy code itself: Insert and Delete for rows, Enter and Tab across cells, type-ahead pickers, date shorthand like "5" or "minus 5", and automated keyboard tests lock every shortcut in. None of those are keys the browser reserves, and legacy has almost no menu shortcuts, so we aren't fighting Ctrl+W. The grid is AG Grid in React, so typing and moving happen locally, with a target under 50 milliseconds from keystroke to screen; only saves go to the server, under 300 milliseconds. Power users time the 25 most frequent workflows on both systems, and a module ships when 90 percent are as fast or faster. If we can't get there, the fallback is a thin desktop wrapper around the same client.

**Follow-up:** Why not Blazor, given your whole stack is .NET?

Blazor Server sends every keystroke over the network, which is the wrong trade for heads-down data entry. Blazor WebAssembly avoids that, but its grids are less proven and its download is heavier. React with AG Grid gives us a mature spreadsheet-grade grid running entirely in the browser, and a bigger hiring pool. The back end stays C# on .NET 10, so the money logic is still .NET.

**Trap:** Promising it will 'feel just like the desktop' without a measurement, brushing off the keyboard concern as a change-management issue, or claiming that installing as an app unlocks browser-reserved keys.

Source: Target architecture: Web client for keyboard-heavy accountants, p.6; Assumption A9, p.4; Gate P3 (keyboard parity), p.20; Trade-off analysis (Language and UI), p.18; Reference: Technology stack (PWA, Playwright keyboard tests), p.3, and Non-functional targets (50 ms, 300 ms), p.4; codebase-facts.md (grid keys, almost no menu shortcuts). The Blazor WebAssembly point is not in documents

### Your filing gateway worker submits a VAT return, the tax authority accepts it, and the worker crashes before it records success. The outbox redelivers the event. Do you file twice?

No, but only because I handle that case explicitly; the outbox alone wouldn't save me. The outbox makes sure the event isn't lost, because it's written in the same transaction as the data. Delivery is at least once, so every worker records each event's unique key and applies it at most once. That record lives in our database, though, and the authority's acceptance doesn't. So for the filing gateway, an unclear result is its own state: outcome unknown. Before any resend, the worker checks whether our submission already landed and records the receipt. If it can't tell, it stops and a person decides. Inside our walls the same idea holds: every posting carries a unique key, so a retry never posts twice, and workers reject any command with a stale authority stamp.

**Follow-up:** How long do you keep the processed-event keys, and what about message ordering per tenant?

Posting keys live as long as the books, since the key sits on the posting itself; worker keys are kept well past the message bus's redelivery window. I don't rely on global ordering. Every event carries the tenant, and Service Bus sessions, a per-tenant lane, give in-order handling per tenant where order matters.

**Trap:** Claiming the outbox gives exactly-once delivery, or claiming idempotency keys cover an outside system he doesn't control.

Source: Modular monolith and financial core (outbox, at-most-once workers, posting keys), p.6; Coexistence (authority stamp), p.14; Reference: Technology stack (Service Bus with a transactional outbox), p.3, and glossary (transactional outbox, authority stamp), p.6. The 'outcome unknown' handling, key retention and per-tenant sessions are not in documents

### Tier 3 is 'out-of-process code extensions.' Whose code is it, where does it run, and what can it touch? And what about the fork that changes how something posts? A webhook can't do that.

Whoever wrote the customization owns it: the firm's team, a partner or the customer. It runs outside our process, in isolated functions, and can do only what a user could do through the API. It reaches us through the public API and webhooks, behind the same edge as everyone else, with a credential scoped to one tenant. It acts only through validated commands, the same validation a person typing gets, and never writes to ledger tables. That's why we rejected in-process plug-ins: they could reach another tenant's data. On posting logic, my assumption is that forks mostly change reports, fields, integrations and validations, not posting. A posting change many forks share is promoted to the core for everyone. One that fits nowhere goes on the backlog, and that customer moves in the last wave. All 310 are classified by week 6, so we'll know the real count early.

**Follow-up:** Who hosts Tier 3 code, you or the customer, and who supports it when it breaks?

My default is that we host isolated functions, so customers without their own IT can use them, each with a one-tenant identity and no network path to the database; a partner can host its own. Whoever writes it supports it, as the firm supports its forks today, while we own and version the API contract. It's pinned in the tenant's manifest, and if it fails, posting still works, because it sits outside the transaction.

**Trap:** Implying that Tier 3 code runs inside the platform or gets database access, or claiming every fork will fit the tiers.

Source: From 310 forks to extension points, p.7; fork consolidation diagram (Tier 3: API, webhooks, isolated functions; promoted to core; backlog, moves in W5), p.8; target-architecture diagram (public API and webhooks through the edge), p.5; Assumption A7, p.4; Trade-off analysis (Forks), p.18; Top risks, p.21. Ownership, the one-tenant credential and the support model are not in documents

### One deployable for 4,200 tenants means one bad release or one bad schema change hits everyone at once. How do you release, and how do you change the schema across seven cells and the dedicated databases without downtime?

Cells are my unit of release, so a bad release hits one cell first, not everyone. Every release goes to the canary cell, then the rest, and feature flags switch new behavior off per tenant without a redeploy. Schema changes are expand-then-contract: add the new column, deploy code that works with both, backfill, and drop the old one in a later release, so code can always roll back without undoing the schema. Dedicated databases run the same code and get the same scripted migration in the same pipeline: about 126 of them, automated, against 4,200 by hand today. Most tax changes don't need a release at all, because they ship as signed rule packs. And nothing ships unless the differential suite shows 100 percent equivalence on ledger, VAT and payroll, with every deviation signed.

**Follow-up:** With 600 tenants per cell, your canary is still 600 customers. Isn't that big?

It's about 14 percent of customers, so inside the canary cell new behavior goes first, behind a flag, to the firm's own books and volunteer tenants, the same idea as wave zero, then the whole cell, then the other six. A flag can't contain a plain code fault, though; that's what the 100 percent differential gate before release is for, and why a cell is the blast radius by design.

**Trap:** Ignoring how code and schema rollback are tied together, or answering 'we test thoroughly, so it won't happen'.

Source: Tenant isolation (cells as unit of canary release), p.6; Statutory variability as configuration, p.6; Layered AI L3 gate (release blocked), p.10; Reference: Technology stack (Delivery: feature flags, canary cell first), p.4, and Cloud cost inputs (about 126 dedicated), p.5. Expand-then-contract and the in-cell flag rollout are not in documents

### Your disaster recovery target is 15 minutes of data loss and 4 hours to recover. For an accounting system, what happens to those 15 minutes of postings, and to anything already sent to the tax authority or the bank in that window? And how does a 4-hour outage fit with 99.95 percent in filing week?

Those numbers apply only if we lose a whole EU region. A zone failure is the common case: databases are zone-redundant, so the target is no data lost, and automatic failover usually takes minutes, with an hour as the ceiling. A regional loss fails over to a standby copy in a second EU region: at most 15 minutes lost, service back within 4 hours. I won't pretend that fits 99.95 percent; a regional disaster would break that month's target, and we'd report it. In the lost window, entries made would need re-entering. We pull from the authority what it actually accepted, re-import bank statements, compare with the restored books, and tell each affected customer exactly which minutes to re-check. And we rehearse failover cell by cell before the first customer moves.

**Follow-up:** Is that cross-region standby actually in your 299 EUR per customer?

Not as its own line. The cell line covers a zone-redundant database, a read replica and backups; the cross-region standby is what the week-4 check against a real cloud bill settles. My rough estimate is up to about 80 EUR per customer for standby copies of every database. That's inside the 35 percent cloud overrun our sensitivity already covers: at full scale run cost stays under 406, but cash payback would slip from month 44 toward the low 50s.

**Trap:** Treating 15 minutes of lost postings as acceptable without a recovery procedure, claiming the 99.95% filing-week target also covers a full regional disaster, or claiming the cross-region standby is already costed.

Source: Platform and service levels (targets), p.8; Reference: Non-functional targets (zone: no loss, 1 hour; region: 15 minutes, 4 hours; 99.9% and 99.95%), p.4, and Cloud cost inputs, p.5; Business impact sensitivity (cloud +35 percent: payback month 56), p.19. Failover reconciliation, typical failover time, the standby cost estimate and the drill plan are not in documents

## Security lead

### You're putting about 600 companies' books in one shared PostgreSQL schema. One bad row-level security policy and that's a breach. How do you prove to me, not just assert, that tenant A can never read tenant B?

I prove it with several layers that each fail closed, meaning they refuse when anything is missing, plus tests that run every hour and can block a release. In the database, row-level security, a rule that filters every row by tenant, is forced, so even the app's own role can't bypass it. The tenant is set per transaction, so a pooled connection can't carry it into the next request, and a request with no tenant is refused. The tenant is also part of every key, so no row can point into another tenant. Outside the database, queue messages, cache keys, document paths, search, exports and logs all carry the tenant too. Then the evidence: hourly cross-tenant probes, where any leak blocks a release and pauses cutovers; an outside penetration test before the platform gate in month 3; and an isolation probe in every customer's go-live.

**Follow-up:** What do the hourly probes actually do, and who sees a failure?

The paper commits to hourly probes that block a release; this is how I'd build them. Every cell gets fake canary tenants, test companies seeded with marker records. Each hour a probe signs in as one and tries to reach another's markers through the API, reports, search, exports, files and cache. A database check also runs with no tenant set and must be refused. Any hit pages on-call and the security lead, blocks releases and pauses new cutovers.

**Trap:** Treating row-level security as the whole answer, or calling it guaranteed. A CISO knows the table owner bypasses it unless it is forced, and that pooled connections can leak a tenant setting between requests. Setting the tenant per transaction is the answer to that, so say it out loud. Forgetting the paths outside the database (cache, files, search, logs) also loses the point.

Source: Target architecture, Tenant isolation p.5-6; Cutover runbook p.14; Validation gates G3 p.15; KPI guardrails p.17; Roadmap gate P2 p.20; Top risks p.21. Probe design in the follow-up is not in documents

### Your AI features read invoices, bank statements and ledgers. Where does that data actually go, is any of it used to train models, and what has the provider committed to in writing?

Customer data goes only to EU-hosted models, through one model gateway we control, and the plan requires no training on it. But I won't pretend that's signed yet: 'EU agreement, no training' is assumption A13, and we confirm it in the contract at the week-8 gate. The models are Azure OpenAI in the EU Data Zone and Document Intelligence in EU regions. Every feature has a per-tenant kill switch, and AI audit records are kept with the ledger. Extraction does see full invoice content, since that's its job, so it stays in the EU. Elsewhere the models see less than you'd think. The reporting model never writes SQL or produces a number: it picks metrics from a finance-owned catalog and our engine runs the query. The support assistant answers only from the manual, release notes and resolved tickets, never from customer books.

**Follow-up:** What stops a crafted question or a poisoned invoice from pulling out another tenant's data?

The model can't leak what it can't reach. Report queries run under the user's own rights and row-level security, so a manipulated model still gets only that tenant's data. At launch, the worst a poisoned invoice can do is produce a bad draft: fixed-rule checks run first, and a person approves every posting. The one to watch is the support assistant, since it learns from resolved tickets, so I'd ground it only on redacted ones.

**Trap:** Saying 'Microsoft guarantees it' or 'the data is anonymized'. A13 stays an assumption until the contract is confirmed at week 8, and extraction has to send real invoice content to a model. Own both points. Also don't claim the support assistant is harmless because it never reads books: its pool of resolved tickets from every customer is the soft spot.

Source: Assumptions intro (confirmed at gate P1) p.3 and A13 p.4; Platform and service levels p.8; AI in the product, guardrails p.12; Reference technology stack p.3-4 and data residency p.4. Redacting the assistant's tickets (follow-up) is not in documents

### You found a plaintext database password in the web service config and in a shipped zip, in a public repo. What did you do about it, and what does that tell you about the rest of their estate?

I flagged it in the case study as 'rotate it now', and I treat it as compromised from the day it was found, not something to fix at migration. It sits in the web service's Web.config and in a shipped zip in the public code, so the repo can't tell me whether that value is live in the firm's estate. Checking that is a week-one job, along with reviewing database logs for any use of it and scanning the full repo history and shipped binaries for other secrets. It also tells me secrets were handled by hand, and MD5, an old password hash that's easy to crack, is still allowed. So hardening legacy starts now; it doesn't wait 18 months for the cloud. In the target, secrets stay out of config: Key Vault, managed identities, where services prove who they are without a password, and per-tenant data keys.

**Follow-up:** Is that a reportable breach?

Not automatically. A leaked credential is a security incident. It becomes a personal-data breach if it was used, or we can't rule out that it was used, to reach personal data. So the log review comes first. If it points that way, the firm, as processor, tells affected customers without undue delay, and they decide on notifying the regulator. Either way, the decision and its reasons get written down.

**Trap:** Three ways to lose here: brushing it off as an old open-source file, saying the migration fixes it (that's 18 months away), or claiming it's been exploited or is live in production. The repo is public code, and whether that password works anywhere is something to check, not assume.

Source: Current-state assessment p.3 ('Rotate it now'); Reference code evidence p.3 (Web.config line 58); Reference keys and secrets p.3; codebase-facts security notes (shipped zip, MD5). Week-one check, log review, history scan and breach handling not in documents

### Desktop users connect straight to MySQL with their own grants. You say writers are locked out at cutover. How do you know you got every one: a bureau's integration, a scheduled job, someone holding the admin password?

We don't depend on finding every client; we shut the door at the database. The legacy app can make each app user a MySQL user with grants it issues itself, from one place in the code, so we list every account from the server itself, not from guesses. At 20:00 on cutover night we stamp the tenant in the registry, revoke those grants, disable integrations and set the database read-only. Only then do we take the final extract. Then two checks. The authority stamp, a version number saying which system may write, makes workers and connectors reject any command carrying an old one. And nothing goes live until the cloud copy reconciles to the cent with that locked extract. A bureau's forgotten script just starts failing, loudly, and I'd rather have that than two sets of books.

**Follow-up:** What about admin or root accounts, and how do you know nothing wrote after the lock?

The paper commits to the lock itself; this detail is my design. Admin passwords for that database are rotated into the vault at the lock. Read-only goes on in the strict mode that also blocks admin accounts, where the server version supports it. At go-live we compare a checksum, a fingerprint of the data, of the locked database with the extract. Any difference fails go-live and we re-extract.

**Trap:** Relying on users or the app to stop writing. Also: forgetting admin accounts, forgetting that MySQL's ordinary read-only mode doesn't stop super users, and forgetting that a hypercare rollback must restore those grants, which is why the way back is rehearsed at G1.

Source: Coexistence and Cutover runbook p.14; Validation gates G3 p.15; Rollback p.15-16; Reference code evidence p.3 (MySqlGenerator.vb, grants issued by the app); Reference glossary, authority stamp p.6. Listing accounts from the server and the follow-up detail not in documents

### Month 10, about 2,000 customers live. A customer calls in: they can see another company's invoices. Walk me through the first 72 hours.

Contain first, then scope, then notify fast, and new cutovers stop automatically. In hour one we declare an isolation breach, which by rule pauses every new cutover. We switch off the exposing path with a feature flag, a switch that turns a feature off without a release, or roll that release back. Cells limit the spread: each cell of about 600 tenants has its own database, and releases reach a canary cell first. Next, scope: every log line carries the tenant, which lets us trace whose data was shown to whom. Then notify: affected customers hear from us without undue delay, because they're the controllers, and we support them in making their 72-hour notice to the regulator. Cutovers resume only after the root cause is fixed, a new probe that would have caught it is in place, and the firm's security lead signs off.

**Follow-up:** Would you roll those customers back to legacy?

No. Rollback is our tool for correctness problems during hypercare, and most of those customers are already past their first cloud filing, where we fix forward. Moving them back at anything like 100 a night would take weeks and add correctness risk, while switching off the leaking path closes the hole in hours. Fix it where it lives, prove the fix with a new probe, and keep new cutovers paused until then.

**Trap:** Saying it can't happen, promising 'no data was exposed' before scoping, offering to roll 2,000 customers back to legacy, or getting the GDPR roles backward. The firm, as processor, tells its customers; the customers notify the regulator.

Source: Tenant isolation p.5-6 (cells cap the blast radius, logs carry the tenant); KPI guardrails p.17; Rollback p.16 (fix forward after first cloud filing); Top risks p.21; Reference cost inputs, one database per cell p.5; Reference delivery, feature flags and canary cell first p.4. Incident response and notification steps not in documents

### Walk me through GDPR. Where does every copy of the data live, including backups, the disaster recovery region and logs? And who is controller and who is processor once you pool 4,200 databases into seven cells?

Every copy stays in the EU: the primary, the standby in the second EU region, backups, logs, legacy archives and AI processing. Pooling doesn't change who controls the data. Our customers stay the controllers of their books and their employees' payroll, the firm stays their processor, and the cloud provider is a sub-processor, a supplier working on our behalf, under an EU data processing agreement. What pooling does change is the risk: 4,200 separate databases become seven shared cells, plus dedicated databases for the largest 3%. So I'd deliver a data protection impact assessment, the formal GDPR risk review, by week 8 and share it with customers, who also get notice of the sub-processor before their wave. Residency is enforced, not just intended: the cloud account only allows resources in the two EU regions, and the AI gateway only routes to EU endpoints.

**Follow-up:** What personal data ends up in your logs and telemetry?

As little as possible. Logs carry the tenant and user IDs so we can trace and scope an incident, but not content: no names, personal codes, amounts or document bodies. Scrubbing happens in the logging layer, and a build check fails if a known personal-data field shows up. Logs stay in the EU and are kept for less time than the books.

**Trap:** 'Azure is GDPR compliant, so we are.' Compliance isn't inherited from the cloud provider. Forgetting backups or telemetry, or the sub-processor notice owed to 4,200 customers, is exactly the gap a CISO is looking for. Don't claim the firm becomes the controller.

Source: Assumptions A1 p.3 and A13 p.4; Tenant isolation, largest 3% dedicated and seven cells p.5-6; Legacy end of life p.16; Reference non-functional targets, data residency and disaster recovery p.4. Controller and processor roles, DPIA, sub-processor notice and region policy not in documents

### Who on your side can see a customer's payroll? How is support access controlled, and can the customer see who looked?

By default nobody on our side sees a customer's books: access is per tenant, needs a reason, expires, and is logged. The case study commits to scoped, logged support access; here's how I'd build it. An agent requests access to one tenant against a ticket. It's read-only by default, payroll is excluded unless the ticket needs it, and it expires on its own. It runs through the same row-level security as customers, never a support superuser that bypasses it, and database administrator access goes through a logged emergency path too. Every look lands in the audit trail kept with the ledger, and customers can see their own access log, which bureaus will ask for. The AI assistant doesn't read books at all: it answers from the manual, release notes and resolved tickets.

**Follow-up:** What about a Sev1 at 2 a.m., when there's no time for approvals?

There's an emergency 'break-glass' path, but it's loud. A second engineer has to approve it, it alerts security immediately, it expires within hours, and it's reviewed the next business day. The customer sees it in their access log, with the reason. If break-glass becomes routine, that's a process failure, and we'd track it as a metric.

**Trap:** Describing a shared support superuser, or any role that bypasses row-level security, which quietly undoes the whole isolation story. Also overclaiming: the documents only say 'scoped and logged', so present the detail as your design.

Source: Tenant isolation, 'Support access is scoped and logged' p.6; AI in the product, grounded assistant and audit records kept with the ledger p.12. Access workflow, admin path and customer-visible log not in documents

### Your delivery team and its AI agents touch real customer data: 310 forks, a year of support tickets, replayed history from 300 tenants, and weekly copies of all 4,200 databases. How do you stop the program itself from becoming the biggest exposure?

One rule: production data stays inside the production boundary, even for the delivery team. The plan already runs the weekly fleet rehearsal of all 4,200 databases inside the production security boundary, and I'd hold the replayed history from 300 tenants to the same rule. Engineers work from results, meaning control totals and mismatch reports, not by browsing raw books, and rehearsal copies are destroyed after each run. AI agents reach code and schema only through the EU model gateway, under the same no-training term we confirm in the contract at week 8. Support tickets are redacted before clustering, secrets like that plaintext password are stripped before code reaches a model, and a customer's fork goes to AI only after that customer consents.

**Follow-up:** What if a customer refuses consent for fork analysis?

Then our own people classify that fork by hand into the same three tiers. The firm already maintains those forks, so that needs no new consent. If it isn't ready in time, that customer moves in a later wave: it costs time, not safety. The real pressure is the calendar, since consent has to land before all 310 are classified by week 6, so I'd start asking in week 1 and report refusals at the week-8 gate.

**Trap:** Implying the delivery team gets copies in a development environment 'for testing', or forgetting that forks are customer code needing consent. Never name who supplies the delivery team.

Source: L0, forks and 12 months of tickets p.10; L2 weekly fleet rehearsal inside the production security boundary p.11; L3 replayed history p.11; Assumption A13 (redaction, consent before fork analysis) p.4; Forks classified by week 6 p.7 and p.21; Current-state assessment p.3. Where L3 replay runs, engineer access, copy destruction and secret stripping not in documents

### Lithuanian law wants records readable for 10 years, GDPR wants personal data deleted when it's no longer needed, and your ledger never changes. How do you reconcile retention, erasure and 4,200 legacy archives?

Legal retention wins for accounting records, and we handle erasure around it, not against it. GDPR doesn't require deleting records the law obliges us to keep. So the ledger stays append-only: posted entries never change, corrections are reversals, and documents sit in storage that can't be altered. Every calculation records its rule-pack version, so history is never silently recalculated. The legacy databases become encrypted, read-only archives for 10 years after hosting goes off in month 20. Personal data outside the legal record, like user accounts, support tickets and AI logs, gets its own shorter retention and real deletion. When a tenant's retention ends, its rows in the shared database are deleted, and destroying its per-tenant data key makes anything encrypted with it, like its documents and archive, unreadable. The 10 years is assumption A8; we confirm the full schedule, including any longer payroll periods, at week 8.

**Follow-up:** One of a customer's employees asks you to erase their data. What happens?

We route it to the customer, because they're the controller of their employees' data, and we help them act on it. Payroll records under legal retention are kept but restricted, meaning stored and not used for anything else. Anything the law doesn't require, like contact details, can be deleted. The posted ledger itself is never edited.

**Trap:** 'We delete on request' breaks the legal retention duty; 'we keep everything forever' breaks GDPR. Also, don't claim per-tenant keys can erase rows in the shared database by destroying the key. They only cover data actually encrypted with them.

Source: Assumption A8 p.4; Ledger rules p.6; Statutory variability as configuration p.6; Legacy end of life p.16; Reference keys and secrets p.3 and immutable document storage p.4. Erasure handling and key destruction not in documents

### Your gates say 'a named person signs'. Who signs the security gates, meaning isolation and the pen test at month 3 and each AI feature? And can the steering committee override a red isolation guardrail to protect the month-12 date?

The firm's own security lead signs the security gates, not the delivery team, because the people who build it shouldn't certify it. The paper has a named person sign each AI layer's gate; for security, here's who I'd name. The month-3 platform gate needs passing isolation probes and an outside penetration test, signed by that security lead with the tester's report attached. Each AI feature launches against its accuracy threshold, and the data protection officer signs anything touching personal data. And no, the steering committee can't override a red isolation guardrail. Any breach pauses new cutovers, and correctness and isolation outrank speed. The cost is real: the 70% target has only 30 customers of slack, so a pause moves that date out about month for month. I'd rather report a late 70% than a leak.

**Follow-up:** Who does the pen test, and what's in scope?

An independent firm with no part in the build. The scope is cross-tenant access through every path: API, web client, exports, files, search, extensions and the AI gateway, plus identity and the edge. It repeats before major releases and at least yearly, and I'd want high-severity findings closed before the month-3 gate.

**Trap:** Saying the delivery team signs its own security gate, naming the delivery supplier, or answering 'the steering committee decides', which signals that isolation is negotiable once the 70% date is at risk.

Source: Layered AI, 'a named person signs a gate' p.9; AI in the product, launch gates p.12; Migration plan slack p.13; KPI dashboard p.16 and guardrails p.17; Roadmap gate P2 p.20. Named signers and the no-override rule as a governance statement not in documents

## Head of AI

### Your week-8 go/no-go depends on 95% precision for the rule inventory. Precision against what ground truth? And precision is the easy half. How do you know you haven't missed rules?

Precision is measured against human review, and completeness is checked mechanically, not by the model. Roslyn, the .NET compiler platform, maps 377 CSLA classes, 425 data-portal methods, 797 rule registrations and all 770 SQL statements. The gate requires every class, method and SQL statement to be mapped, so a script lists anything nobody has read. AI writes each rule record in two independent passes, and a script rejects any record citing lines that don't exist. Precision is the share of records the four legacy engineers and an accountant accept without a real correction, measured on Ledger and VAT for week 8. Every money rule is reviewed, not sampled. Coverage still isn't recall, because a rule can hide inside a method body. So L3 is the backstop: legacy is the answer key, and replayed history plus a million generated cases a night surface a missed rule wherever they exercise it.

**Follow-up:** Both passes use the same model. Aren't their errors correlated?

Yes, they can share blind spots, which is why agreement between the passes is never the gate. Agreement only decides what reviewers look at first. The gate is human review of every money rule, plus L3, where differences against running legacy expose what both passes missed. Running the second pass on a different model family is a cheap option I'd test in discovery.

**Trap:** Treating 95% precision as proof the inventory is complete, implying the AI checks its own work, or dodging the recall question.

Source: Layered AI gate table, L0 row (page 9); L0 comprehension and rule inventory (page 10); L3 test sets (page 11); gate P1 (page 20); Reference, codebase at a glance (page 1). The precision definition and the second-model option are not in the documents.

### Legacy is your answer key, but it stores money as floating point and has five rounding implementations that disagree. If you match legacy to the cent, aren't you just certifying its bugs? And how do you know the harness catches anything? What mutation score do you require?

We match legacy on purpose, and every intended difference is a signed decision. 'Zero regression' means ledger, VAT and payroll match legacy to the cent, and a legacy bug is fixed only through a signed deviation register, never silently. Rounding follows a written tolerance policy: noise below the declared precision is ignored, half-cent boundary cases are approved once as a class, and every logic difference is fixed or signed off one by one. The 'about 1 in 560 VAT calculations' figure comes from our emulation; the harness confirms it on the real runtimes in weeks 2 to 4. To test the harness, mutation tests flip a sign or rate on purpose. The plan doesn't set a score. My bar for money code: every planted mutation is caught, or shown to be equivalent, meaning it can't change any result. A survivor means a missing test, and that module doesn't pass L3.

**Follow-up:** Which of the five rounding copies is the answer key, then?

Whichever one legacy actually ran on that path. History moves exactly as legacy computed it and is never recalculated. New calculations in the cloud use one rounding policy declared in the rule pack. Where that differs from legacy on half-cent cases, an accountant approves the difference once, as a class, and it goes in the deviation register.

**Trap:** Presenting the 1-in-560 figure as measured on real systems, calling legacy 'correct', or quoting a mutation score as if the plan already states one.

Source: L3 proving financial equivalence (page 11); Assumption A10 (page 4); Current-state assessment (page 2); Reference, rounding emulation note (page 3). The specific mutation bar is not in the documents.

### How do you know AI-translated C# behaves exactly like the VB.NET and CSLA code it replaces, especially when you're switching Double to decimal and removing CSLA's global company context at the same time?

I don't trust the translation; I trust the checks it must pass. Every AI change is one pull request that must clear the compiler, the tests and the differential suite against legacy running without its UI, and money code needs two reviewers. We translate only calculations where exact behavior matters: posting and closing, the VAT calculation, inventory costing, depreciation and the payroll kernel. We rebuild the rest, like bank import on ISO 20022 libraries and the UI from extracted screen specs. On your two specifics: exact decimals will change some results, mostly at half-cent boundaries, so the tolerance policy decides what's noise, what's approved as a class and what's a real logic difference. The global company context, used 321 times, becomes a tenant set per transaction. A request with no tenant is refused, and forced row-level security, a database rule that filters every row by tenant, backs that up.

**Follow-up:** What about VB-specific behavior a translator might silently change, like banker's rounding in CInt or integer division?

That's what the differential suite and property tests, which generate inputs automatically, are for. A million generated edge cases a night hit boundaries like half cents, negative amounts and rate changes, so a silently changed operator shows up as a difference before it ships. Roslyn analyzers, already in our tooling, can also flag known VB-to-C# hazards for the reviewer.

**Trap:** Saying the model is 'very accurate at VB to C#', relying on code review alone, or ignoring the behavior changes that come with Double to decimal.

Source: Layered AI gate table, L1 row (page 9); L1 translate the kernel, rebuild the shell (pages 10-11); L3 tolerance policy (page 11); Tenant isolation (page 5); Reference, code evidence: global company context, 321 uses (page 3); Reference glossary, row-level security (page 6)

### Tell me exactly what any AI feature may do without a human. Then: a large supplier changes its invoice layout overnight. How do you find out before wrong entries hit the books, and who pulls the plug?

Very little acts alone: read-only reports within the user's rights, cited support answers that can open the right screen, and flags. Later, per tenant, it can auto-post invoices from known suppliers under that tenant's limit, with one-click reversal. Nothing AI-driven files a return, pays a salary or touches a closed period. For the layout change, fixed checks run before anything posts: VAT arithmetic, the EU VAT-number lookup, duplicates and open period, so most misreads stop there. Low confidence sends the invoice to a person. I don't rely on the model knowing it's wrong, so every reversal or correction of an auto-posted entry counts against the 0.5% error guardrail. Any feature switches off per tenant at once, and I'd add a per-supplier switch back to drafts. The plan doesn't name who pulls it; I'd give that to the on-call owner of the AI features. A breach also pauses new cutovers.

**Follow-up:** Is the kill switch only per tenant? What if the model provider ships a bad update to everyone?

Per tenant is the documented switch. The model gateway, the single layer every AI call goes through, gives us the fleet-wide one. I'd pin model versions there, so a provider update doesn't reach customers until it passes the same evaluation sets. With feature flags, we can also put every tenant back to drafts-only in one change.

**Trap:** Describing autonomy vaguely ('AI assists'), claiming the model knows when it's wrong, having no concrete signal for drift, or leaving 'who pulls the plug' unanswered.

Source: AI in the product, table of what may act alone and guardrails (page 12); KPI guardrails (page 17). The kill-switch owner, the per-supplier switch and using reversals as the drift signal are not in the documents.

### You'll allow auto-posting at 99.5% correct on 1,000-plus invoices in shadow mode. With 1,000 samples, five misses is 99.5%, and the confidence interval is wide. What does that gate actually prove?

On its own, it doesn't prove 99.5%, and I'd say that plainly. With five misses in 1,000, you can only claim with 95% confidence that true accuracy is better than about 99%. At 1,000 invoices it proves 99.5% only with at most one miss; with a few misses you need about 2,000. So I treat 1,000 as the minimum, not the proof, and the design caps the cost of being wrong. Auto-post is switched on per tenant, only for known suppliers, under that tenant's own limit. Fixed checks run first, and every entry has one-click reversal. After launch, the 0.5% auto-post error guardrail keeps measuring; a breach pauses new cutovers, and I'd put auto-posting back to drafts. 'Correct' means the whole entry is right: accounts, VAT and amounts. The 97% field accuracy only gates drafts a person approves.

**Follow-up:** If a person approves every draft at launch, won't they rubber-stamp it, so your labels lean toward the model?

That's a real risk, called automation bias. So part of the shadow set is graded blind: a person posts the invoice without seeing the AI's proposal, and we compare the two. Corrections from normal approvals help with monitoring, but they don't count toward the gate, and nothing trains models on customer data.

**Trap:** Defending 1,000 as statistically enough, mixing up 97% field accuracy with whole-entry correctness, or claiming the guardrail switches auto-post off when the plan says a breach pauses cutovers.

Source: AI in the product, launch gates (page 12); KPI guardrails (page 17). The confidence-interval math and switching auto-post back to drafts are not in the documents.

### AI-code acceptance sits on the steering committee dashboard, and low acceptance for two sprints takes a module away from AI. Isn't that a quota by another name? How do you define 'major rework', and what happens to the 12-month plan if acceptance is low everywhere?

It's a steering signal for the method, not a target for reviewers, and gaming it buys little. Accepting a weak draft doesn't get it merged: it still has to clear the compiler, the tests, the differential suite and two reviewers on money code. I'd measure 'major rework' from the merge itself, how much of the AI draft survived, sorted into accepted, reworked and rewritten, with the reviewer confirming. So it's mechanical, not self-reported. We baseline it on Ledger by month 6 and track it from the first sprint. If it's low everywhere, the honest answer is that the schedule moves, not the gates. The team of about 30 is an assumption sized in discovery, and 70% by month 12 has only 30 customers of slack. We'd add people or accept a later date, and the steering committee would see that early.

**Follow-up:** Your dashboard shows 60% accepted. Where does that number come from?

It's an illustrative number on a mock-up. The slide header calls the tiles month-9 plan values, but this tile says tracked, no quota, so it's not a target and not a measurement. The real baseline comes from the Ledger work by month 6. If it's much lower, that changes staffing and dates, not the gates. For scale, a 25% higher team cost moves cash payback from month 44 to month 50.

**Trap:** Treating acceptance as a productivity target, quoting the 60% mock-up figure as a goal, claiming gaming is impossible, or implying the AI speed-up is assured.

Source: L1 gate and acceptance note (pages 9-11); KPI dashboard (pages 16-17); dashboard mock-up (v-007); Reference, KPI trajectory (page 5); Assumption A6 (page 4); wave-plan slack (page 13); sensitivity (page 19); Team (page 21). The definition of 'major rework' is not in the documents.

### Natural-language reporting where the model never writes SQL. Then what does it do? How do you get 95% exact on 500 questions, and what stops it confidently answering the wrong question with a correct number?

The model turns the question into a choice from a finance-owned catalog, and the engine does the rest. It picks metrics, filters and a period from a catalog of business metrics with fixed definitions. The engine builds and runs a read-only query inside the user's rights, so row-level security still applies. Every number on screen comes from the query result, never from the model. 'Exact' means the same number a finance analyst's reference query returns, on 500 questions taken from real accountant and ticket wording. For the wrong-question risk, the answer shows how it read the question, like 'VAT payable, Q3, by rate', with the metric definition one click away. If a question is ambiguous or outside the catalog, it asks for clarification or says it can't answer, rather than guessing.

**Follow-up:** Couldn't the model still put a made-up number in the sentence it writes around the result?

It could try, so the sentence gets checked. Every number in the text must match a value in the result, or the sentence is dropped and only the table is shown. Saving or sharing a report always needs a person.

**Trap:** Suggesting the model produces SQL in any form, treating validated text-to-SQL as the same thing, or having no answer for the model misreading the question.

Source: AI in the product, table and guardrails (page 12); Reference glossary, semantic layer (page 7). The source of the 500 questions and the interpretation display are not in the documents.

### Why Azure OpenAI and Document Intelligence rather than open models you host yourselves? What's your plan when a model version is retired or changes behavior? And is 4 euros per tenant per month believable?

Managed EU models are the fastest path that meets our data rules, and the gateway keeps us from getting locked in. We assume Azure, with AI processing in the EU under an agreement that rules out training on customer data. Azure OpenAI's EU Data Zone meets that, and hosting our own GPUs would add an operations job the plan doesn't staff. Every call goes through our model gateway, so swapping a model doesn't touch application code. A model change, forced or chosen, is treated like a release: it ships only after passing the same evaluation sets as the launch gates. On cost, 4 EUR a tenant a month is a planning estimate, re-checked against a real cloud bill in week 4. That's about 200K EUR a year, under a sixth of run cost. Even doubled, we'd stay under the 406 EUR target.

**Follow-up:** Which model for which feature?

The smallest model that passes each feature's gate. Document Intelligence handles invoice and bank-statement fields. A small model picks metrics and routes requests. A larger one only goes where reasoning pays off, like L0 rule extraction and support answers. The gateway lets us swap a model per feature without touching application code.

**Trap:** Giving a brand-loyalty answer with no exit plan, quoting precise per-token prices from memory as fact, or misquoting A13 as a requirement rather than an assumption.

Source: Platform and service levels (page 8); Assumptions A1 and A13 (pages 3-4); Reference, technology stack, non-functional targets and cloud cost inputs (pages 3-5); KPI run-cost target (page 17). Re-running evaluations on model changes and the self-hosting trade-off are not in the documents.

### Your support assistant answers from resolved tickets. Those tickets are full of other customers' data. How do you stop it leaking one tenant's details to another, and how do you measure '90% grounded'?

Tickets are cleaned before they're indexed, so the shared index holds no one's books. Our data assumption already calls for redaction; I'd go further and rewrite each resolved ticket as a generic problem-and-fix entry before it goes in. The manual and release notes aren't customer data anyway. Anything about the user's own data goes through the app with their rights, and search carries the tenant like everything else, under the hourly cross-tenant probes. 'Grounded' means every claim in an answer is backed by a passage it cites, scored on a labeled evaluation set, with 90% as the launch gate. Grounded isn't the same as correct, so we also track whether answers actually resolve contacts, against a target of 30% resolved without an agent. When unsure, it hands over to a person with a summary.

**Follow-up:** During coexistence, a bureau user has one company on legacy and one in the cloud. Which manual does the assistant answer from?

The tenant registry knows which system writes each company's books, so the assistant filters its sources by that system and version. The same question about a different company can get a different answer, each with its own citations.

**Trap:** Assuming search over shared tickets is safe because it 'only retrieves', or treating grounded as if it meant correct.

Source: AI in the product (page 12); Assumption A13 (page 4); Tenant isolation, isolation beyond the database (pages 5-6); Coexistence, tenant registry (page 14). Rewriting tickets before indexing and the evaluation method are not in the documents.

### 60% useful flags means four in ten are noise, yet a high-severity flag must be acknowledged before filing. Haven't you put a probabilistic model in the filing path and set accountants up for alert fatigue?

It's in the path only as a speed bump, never a block, and high severity is kept narrow. The model flags and explains, but a person always decides whether to file. Acknowledging takes one click with a reason, which leaves an audit record. High severity is reserved for things an auditor would ask about, like a likely duplicate payment or a VAT rate that doesn't match the item, so most flags are low-severity and informational. 60% useful is the launch bar. Accountants mark each flag useful or not, and we track it per tenant. If one tenant's flags get noisy, we raise its threshold or switch the feature off for that tenant. And migrated history moves exactly as legacy computed it, so every customer has a baseline from day one.

**Follow-up:** What actually detects the anomalies?

Per-tenant statistical baselines and a few fixed rules do the detecting. The language model only writes the explanation in plain words. That keeps every flag explainable and cheap, and we can test how much it catches by planting known anomalies in replayed history.

**Trap:** Defending 60% as high, or letting the model block or delay a filing on its own.

Source: AI in the product, table and kill switch (page 12); L2, history never recalculated (page 11). Severity rules, one-click acknowledgment and per-tenant tuning are not in the documents.

## CFO

### Cash payback is month 44, almost four years on a 4M euro program. Frankly, why wouldn't I just keep running what we have?

Because keeping what we have is neither free nor safe, and the cash case still stands on its own. On hosting savings alone it pays back in year 4 and returns about 2.5M EUR net over five years, about 1.2M in today's money at 8 percent. But the real case is risk and speed. Today a tax change takes 10 to 14 weeks against a 6-week legal window. 522,000 lines of 2006-era code have no tests, and the knowledge sits with four engineers. And cost grows with every customer: a new one adds about 590 EUR a year in run cost on legacy, about 230 in the cloud. Counting the support and engineering time we free up, payback is month 35. And you're not committing 4M today. You're committing about 600K for eight weeks, then deciding on evidence.

**Follow-up:** Have you put a number on the cost of doing nothing?

Not as a single number, and I didn't want to invent one. What I can say: hosting is 3.1M a year and grows with every customer, maintenance eats 62 percent of engineering, and every tax change that misses the legal window is exposure for 4,200 customers. Doing nothing keeps all of that, and the stack only gets older.

**Trap:** Selling year 4 as a great cash return, leaning on month 35 as if it were cash, or getting defensive instead of saying 'the case is risk and speed, not just savings'.

Source: Business impact, pages 18-20 (payback 44/35, 2.48M net, 1.2M NPV at 8%, 230 vs 590 EUR); Executive summary, pages 1-2; Current-state assessment, page 2; brief (10-14 weeks vs 6-week window); deck slide 'payback' speaker notes

### Your entire savings case rests on the 3.1M being hosting only. That's your assumption, not a fact. What if half of it is people or licenses?

You're right, it's the assumption the cash case leans on most, which is why it's one of the 13 we confirm in the first eight weeks, not later. The mechanism is simple: every euro of the 3.1M that turns out not to be hosting is a euro a year off the savings, because the cloud side, about 1.3M EUR a year at full scale, doesn't change. A baseline about 450K lower looks roughly like our cloud-plus-35-percent case: payback in year 5. If half of it were people or licenses we keep paying, savings would shrink to around 300K a year and the cash case would be gone. I'd tell you that at week 8, and we'd decide on risk and speed alone, or stop. That's exactly why the ask is 600K first, not 4M.

**Follow-up:** And the 1.26M cloud figure, isn't that just list prices too?

Yes, it's a planning estimate from list prices, and we check it against a real cloud bill in week 4. About 40 percent is the seven cells, a quarter is the shared platform, and the rest is dedicated databases for the largest customers and AI. If it runs 35 percent high, we still land on the 406 EUR target and pay back in month 56.

**Trap:** Treating the 3.1M as a known fact, or not knowing that the cloud cost stays the same whatever the baseline turns out to be, so every euro of baseline error comes straight off the savings.

Source: Assumptions A2, page 3; Business impact, pages 18-19; Reference, cloud cost inputs, pages 4-5; scenario figures derived by re-running the cost model (cost_model.py), not in the documents

### You're asking for about 600K for eight weeks. What exactly do I own at week 8, and what result would make you tell us to stop?

At week 8 you own evidence, not slides. Four things. The 13 assumptions confirmed, including the hosting baseline, plus the cloud estimate checked against a real bill in week 4. A rule inventory for ledger and VAT at 95 percent precision, reviewed by our legacy engineers and an accountant. The old system running headless, meaning without its desktop screens, as an automated answer key, which also checks on the real code the rounding mismatch we found by emulation. And all 310 forks classified by week 6. The first three are the go or no-go. If any fails, for example the old code won't run headless so we have no answer key, full rollout doesn't go ahead, and I'd recommend we stop or re-scope rather than spend the rest.

**Follow-up:** If we stop at week 8, is the 600K just gone?

The money is spent, but not wasted. You'd keep a reviewed inventory of the ledger and VAT rules in a system that has no tests today, the first automated test harness on the old code, and a map of what all 310 forks actually change. That's useful whatever you decide, including if you keep running the old system.

**Trap:** Describing the eight weeks as open-ended discovery with no hard deliverables, or having no condition under which he would recommend stopping.

Source: Executive summary (decision requested), page 2; Roadmap gate P1, page 20; Assumptions A12, page 4; L0, page 10; From 310 forks, page 7; Reference rounding note (harness confirms in weeks 2-4), page 3; Reference cloud cost inputs (real bill in week 4), page 4; stop/re-scope recommendation not in documents

### Walk me through the 4M. What's in it, is 15 percent contingency really enough for 522,000 lines with no tests, and what costs are not in it?

About 3.2M of the 4M is a dedicated delivery team: about 30 people for a year, then a smaller team for six months. About 250K is tooling and AI usage, and about 460K is 15 percent contingency on year 1. Two things sit outside it: our own staff's time, like the four legacy engineers and our accountants signing off money rules, because that's existing payroll; and about 260K of double hosting in year 1, which the cash case books as a negative saving. On contingency: 15 percent covers estimating error, not a wrong plan. The bigger protection is staging: about 600K before the go or no-go, and a gate before every wave. If the team costs 25 percent more, payback moves from month 44 to month 50. And the team size is set in discovery from measured throughput.

**Follow-up:** So what's the real cash low point?

About 3.9M EUR, in quarter 6. Year 1 is about 3.8M out: the program plus about 260K more hosting than today, because we pay for both systems while customers move. The line is roughly flat through quarters 5 and 6, while the smaller team is still on, then climbs from quarter 7 as legacy shrinks.

**Trap:** Implying the 4M is all-in when internal staff time and year-1 double running sit outside it, claiming 15 percent is plenty, or naming who supplies the team.

Source: Business impact table and investment note, pages 18-19; Reference, investment (3.24M team, 0.25M tooling, 0.46M contingency), page 5; Team, page 21; Assumption A6, page 4; Validation gates (wave gate), page 15; contingency adequacy is reasoning, not in documents

### At month 12 you claim run cost per customer is down 55 percent. But your own realized-savings tile says roughly break-even at month 12. Which number should I believe?

Both, because they measure different things, and the bill is the one that matters to you. 330 EUR is the cloud cost per migrated customer at month 12, against about 740 today and a 406 target. It proves the unit economics. Realized savings is the company's actual hosting bill against the 3.1M baseline, and at month 12 that's roughly break-even, because we're still paying for two systems. The bill really drops once legacy hosting goes off in month 20: about 1.8M EUR a year saved from month 21, and the blended cost falls to about 300 EUR per customer. That's why the dashboard shows the blended cost next to the cloud figure, so nobody declares victory at month 12.

**Follow-up:** Why does legacy cost fall so slowly when 70 percent of customers have already left?

Two reasons, both deliberate in the model. First, a moved customer's old database stays hosted for about two months, through hypercare, so we can put them back in hours with nothing lost. So at month 12 legacy still hosts about 2,480 databases, not 1,230. Second, about a fifth of legacy cost, roughly 600K a year, is shared and only goes when legacy switches off in month 20. We check both against the real contracts in the first eight weeks.

**Trap:** Presenting 330 EUR as a company-wide saving at month 12, or not knowing that the realized run rate is only break-even at that point.

Source: KPI dashboard, page 17; Executive summary, page 1; Reference, KPI trajectory, pages 5-6; cost-model output; follow-up mechanism from cost_model.py (2-month archive lag, 20% fixed legacy share), not in the case study or Reference

### You said yourself the plan clears 70 percent by just 30 customers. If the waves slip, what does that do to my money?

A three-month slip moves cash payback from month 44 to month 49 and cuts five-year net cash from about 2.5M to about 1.7M EUR, because savings start later, we run two systems longer, and the smaller team stays on three months more. And I'll say it plainly: 70 percent by month 12 has only 30 customers of slack, so a slip moves that target about month for month, and one that hits the mid-December to mid-February freeze adds up to two months more. Moving capacity isn't the constraint: the migration factory can do about 1,000 customers a month against a planned peak of 650. The real constraint is modules passing equivalence testing, and that's on the dashboard: all nine are due by month 9, so a slip shows well before month 12.

**Follow-up:** What would you do if month 9 shows you behind plan?

The lever is the order, not the safety gates. I'd pull forward simple customers whose modules have already passed and use the factory's spare capacity. I would not loosen the to-the-cent gates or cut over during filing weeks to hit a date. Correctness outranks the 70 percent.

**Trap:** Promising the 70 percent date is safe, or not knowing what a slip costs in payback and five-year cash.

Source: Migration plan, pages 13-14; Business impact sensitivity, page 19; Reference KPI trajectory (9 of 9 modules at month 9), page 5; cost-model output; cost_model.py (slip also extends the smaller team); 'real constraint' is reasoning

### Month 35 counts freed time. Freed time isn't cash. Why is it on the chart at all, and how would it ever reach my P&L?

You're right, which is why cash payback is month 44 and month 35 is shown separately, labeled as capacity. It's about 950K EUR a year from year 3: around 370K of support time, from tickets falling about 40 percent at 12 EUR a ticket, and around 580K of engineering time, from maintenance dropping from 62 percent to 30 percent or less, about 10 engineers back on the roadmap. It becomes cash only if spending actually falls, for example by not backfilling support attrition. Whether to bank it or reinvest it is your call. My recommendation is to put the engineers on product work. The dashboard reports freed time separately from realized savings, so it's never counted twice.

**Follow-up:** Where does the 40 percent ticket drop come from?

It's a planning estimate, and I'd call it that. The drivers are central rule packs ending the errors from every company typing in its own tax rates, the support assistant targeting 30 percent of contacts resolved without an agent, and fork-specific problems going away with the forks. We cluster 12 months of real tickets in the first weeks to test it, and a migrated customer only leaves hypercare when its tickets are at or below today's level.

**Trap:** Treating month 35 as the real payback, or blending freed time into the infrastructure savings and counting it twice.

Source: Business impact, pages 18-20; Business case chart, page 19; KPI dashboard (realized savings), page 17; Assumption A2 (12 EUR per ticket), page 3; L0 (12 months of tickets clustered), page 10

### Your sensitivities move one thing at a time. What happens if cloud comes in 35 percent high and the team costs 25 percent more, together?

Honestly, I haven't shown that as a named case, but the two effects add almost exactly, because one hits the running cost and the other the investment. Cloud plus 35 percent alone takes five-year net cash from about 2.5M to about 600K EUR. Team plus 25 percent takes about 900K off. Together that's slightly negative at five years, so cash payback slips into year 6. Two things soften it. Even at plus 35 percent the cloud lands on the 406 EUR target, the brief's 45 percent cut, so the run-cost goal still holds. And both numbers are checked before the big money is spent: the cloud bill in week 4, the team size in discovery. If both come in high, I'd bring you that at week 8, and we'd decide on risk and speed, not savings.

**Follow-up:** So in that bad case, would you still recommend going ahead?

Only if the risk case stands on its own for you: tax changes inside the legal window, off a frozen stack, no 310 forks. Counting freed capacity it still pays back inside five years, but that's capacity, not cash. It's a decision for you with real numbers at week 8, not one I'd pre-commit to today.

**Trap:** Quoting a precise combined figure as if it had been modeled, or claiming the combined downside still pays back comfortably on cash.

Source: not in documents (combined case); single-variable cases from Business impact sensitivity, page 19, and cost-model output; combined result verified by re-running cost_model.py

### How will I actually know the savings are real? Who measures them, against what, and how often?

Realized savings is a KPI on the steering dashboard, refreshed weekly from live data and reviewed monthly by the steering committee. It's defined as the 3.1M EUR baseline minus actual run cost, from the real cloud and legacy bills, not from the model. Freed support time is reported separately, so it's never mixed with cash. There's a planned trajectory to check against: a yearly run rate of about minus 380K at months 6 and 9, break-even at month 12, and about 1.8M a year from month 21. Run cost per customer sits next to it, both the cloud figure and the blended one. And both inputs are confirmed early: the cloud estimate against a real bill in week 4, the 3.1M baseline at the week-8 gate.

**Follow-up:** Who owns that number, engineering or finance?

Finance should own the baseline and the bills; the program owns delivering against them. I'd suggest finance signs off the 3.1M baseline at week 8 and the realized figure every month, the same way an accountant signs off every money rule in the build.

**Trap:** Describing the model's forecast as if it were measurement, or forgetting that the run rate is negative through month 9.

Source: KPI dashboard, pages 16-17; Reference, KPI trajectory and cloud cost inputs, pages 4-6; Business impact, page 18; Assumptions (confirmed at P1), page 3; follow-up (ownership) not in documents

### Your case counts only hosting. What did you leave out, upside and risk, and is there anything left out that cuts the other way, like customers leaving instead of moving?

Three upsides are left out on purpose, because none is certain enough to bank. Growth: a new customer adds about 230 EUR a year in run cost instead of about 590 on legacy. Expansion: Latvia and Estonia become rule packs, not forks. And risk avoided: tax changes stop missing the legal window, the four-engineer knowledge risk shrinks, and we get off a frozen 2006 stack. Freed support and engineering time, about 950K a year, I show but don't count as cash. On the downside, the model holds the customer count flat at 4,200, so it doesn't price churn, and losing customers during the move is the real revenue risk. That's why a module ships only when 90 percent of the top 25 workflows are as fast as the desktop, every bureau has a champion, and early movers keep their price for 12 months.

**Follow-up:** If 10 percent of customers leave rather than migrate, does the case still work?

On hosting it moves only a little: each customer who leaves takes about 360 EUR a year of savings, the gap between 590 on legacy and 230 in the cloud, so roughly 150K a year at 10 percent. The real hit is revenue, which this case doesn't model; I'd want finance to size it with us at week 8. Early warnings are on the dashboard: rollbacks over 2 percent or tickets above today's level pause new cutovers.

**Trap:** Putting a figure on revenue upside that was never modeled, or brushing off churn as if migration carried no revenue risk.

Source: Business impact (beyond the cash), pages 19-20; Assumption A5, page 3; Web client (speed parity), page 6; Change management, page 14; cost-model output (4,200 tenants held flat); churn and the follow-up arithmetic not in documents

## Delivery head

### First customers in month 5 on a rewrite of 522,000 lines with no tests. I've run these programs, and that number makes me nervous. Why should I believe month 5?

I believe it because month 5 is a narrow first step, not the whole product. The first wave is the firm's own books plus 19 volunteers, using five pieces only: ledger, invoicing and VAT, payables, bank import and VAT filing. No payroll, no inventory, no forks. The ledger, invoicing and payables code is about 53,000 lines, not 522,000. Bank import is rebuilt on standard libraries, and the desktop screens are rebuilt, not translated. AI drafts the translation, and the old system runs headless, without its screens, as the answer key, so every result is checked to the cent. And month 5 is a gate, not a promise: if those five don't match to the cent, or power users aren't as fast on 90% of their top 25 workflows, the first wave waits.

**Follow-up:** And if the equivalence tests show 99.9% on VAT in month 5, not 100%?

Then the first wave doesn't move until the gap is closed. Each remaining difference is fixed or signed off one by one by an accountant in the deviation register, our signed list of intended differences; half-cent boundary cases are approved once as a class. The first wave is our own books and volunteers, so a short slip costs schedule, not customers. But it eats into the 30-customer margin at month 12, and I'd say so.

**Trap:** Defending month 5 with 'AI makes it fast', implying the whole product ships in month 5, or presenting the date as a commitment instead of a gate that can hold.

Source: Migration plan wave table (p.13); L1 module table (p.10-11); P3 gate (p.20); Web client speed parity (p.6)

### You clear 70% by 30 customers. That's no margin at all. It's month 8 and you're six weeks behind. What do you tell the steering committee, and what are your levers?

I tell them early and plainly: 70% moves out by about the same six weeks, and if the slip runs into the mid-December freeze, up to two months more. I flagged that margin on day one. Then the levers, and none of them touch correctness. The migration factory isn't the constraint: it can handle about 1,000 customers a month against a planned peak of 650, so once the cause is fixed, I can add ready, simple customers to the nights we have. Bureau portfolios move many companies on one decision. Customers waiting on a fork feature go later so they don't hold up a wave. What I won't do is skip a wave gate. And the cost is known: a three-month slip moves cash payback from month 44 to about month 49.

**Follow-up:** Why didn't you just build in more slack?

Because the schedule is set by proof, not machines. A customer moves only once every module they use has passed the cent-level tests, and each wave waits until early movers from the previous wave have run 30 days cleanly. The only ways to add slack on paper were to move customers before their numbers match, or to shorten those checks. I'd rather show a true 30-customer margin and steer to it weekly than a comfortable number hiding the risk.

**Trap:** Promising to 'catch up' by compressing gates or running the factory harder, or getting defensive about the 30-customer margin instead of owning it.

Source: Migration plan (p.13-14); Business impact sensitivity (p.19); study sheet 'Say it first'

### Walk me through your critical path to the first wave. What actually gates the first customer, and which single item is most likely to make you miss mid-month 5?

The critical path runs through the test harness and the cent-level proof, not the cloud platform. By week 8, the rule inventory must be at 95% precision on ledger and VAT, and the old system must run headless, without its screens, as the answer key. In parallel from month 2, the first module team translates ledger, VAT and payables and rebuilds bank import, while the rules team builds the first VAT packs. By mid-month 5, all five pieces, VAT filing included, must match 100%, and power users must be as fast on the keyboard. The platform is ready at the end of month 3, about six weeks ahead of first customers. The item most likely to bite is the harness: if the old business objects won't run without the desktop screens, I have no answer key. I'd rather learn that at week 8 than in month 5.

**Follow-up:** What do you do in week 2 if the harness won't run headless?

I'd see it early: the rounding check runs on the real runtimes in weeks 2 to 4, and the harness must be running by week 8. There's a good sign already: the code ships a server that runs the business objects with no screens, through its data portal, its built-in remote-access layer. If parts still need the screens, I'd drive them through that server layer, at extra time and cost, and take it to the week-8 go or no-go.

**Trap:** Naming the cloud platform as the critical path (his own notes say it isn't), or listing every workstream instead of naming one long pole.

Source: Roadmap gate table (p.20-21) and roadmap diagram; L1 module table (p.10); L0 and L3 (p.11); assumption A12 (p.4); Reference rounding note (p.3); codebase-facts (data portal over Remoting/ASMX) for the follow-up

### You've costed a dedicated team of about 30 for a year. Realistically you won't have 30 productive people in week 3. What's the ramp, what are the roles, and what if you only get 20?

I don't need 30 on day one, and the roadmap is built as a ramp. Month 1 runs three workstreams: the platform, the rule inventory with the fork analysis, and the legacy test harness, plus taking over legacy maintenance from week 2. The two module teams, the tax-rule engine, the web client and the migration factory start in month 2, and the AI product features in month 4. The mix is engineers, migration, QA and accounting domain experts. Thirty is an assumption: the model says 32, and the real size is set in discovery from measured throughput. If I only get 20, I protect the critical path: the first module team, the harness and keyboard parity. AI product features and later modules slip first, and 70% at month 12 moves with them. I'd say that at week 8.

**Follow-up:** Are you counting on AI to make 30 people behave like 60?

Partly, and I say so openly: a manual rewrite this size doesn't fit 12 months, but I don't claim a multiplier. I measure it. The share of AI changes merged without major rework is tracked per module from the first ledger work. If acceptance stays low for two sprints, engineers take that module over, and the team is re-sized from measured throughput, not a hopeful estimate.

**Trap:** Naming who supplies the team, claiming 30 people are ready on day one, or not knowing which workstreams to cut first when understaffed.

Source: Assumption A6 (p.4); Team (p.21); roadmap diagram; Business impact (p.19); Reference cost inputs (p.5); study sheet (model: 32)

### Your four legacy engineers review every money rule, they're the only people who really know the system, and today they keep it alive. That's your bottleneck. How much of their time do you need, and what happens if one resigns in month 2?

I'd plan on most of their week for the first three months, while the rule inventory is built, and less after that, so I protect their time rather than add to it. From week 2 the delivery team takes over their maintenance work, so their week goes to reviewing rules, not fixing tickets. They also review cleaner material: a parser first maps all 377 business classes and 797 rule registrations, AI writes each rule record in two independent passes, and a mechanical check throws out any record citing source lines that don't exist. An accountant reviews the money rules with them. If one resigns in month 2, we lose speed, not the answer key: the cent-level comparison runs against the old code itself, running headless, not against anyone's memory. That's why capturing what they know starts in week 1.

**Follow-up:** And who keeps legacy running, including your promise to rebuild all 310 forks for fast tax patches by month 4?

The delivery team, from week 2, with the four engineers as escalation. The fast lane reuses the same fork analysis and golden test files, so building the 310 frozen forks is automated, not hand work. I'll be honest: rebuilding all 310 by month 4 is the boldest promise in the plan. The fallback is the biggest forks first, with the tail patched by hand.

**Trap:** Saying AI replaces their knowledge, or not knowing that the delivery team takes over their maintenance from week 2.

Source: Top risks (p.21); L0 comprehension (p.11); Team (p.21); assumption A12 (p.4); roadmap diagram (L0 inventory months 1-3); time share not in documents

### You have 38,000 users, many of them bureau accountants who've lived in this desktop app's keyboard shortcuts for years. They'll hate a browser app. How do you get them to move, and what if a large bureau refuses?

I make the web client earn the move before I ask anyone to make it. Speed is a release gate: we time the 25 most frequent workflows with power users on both systems, and a module ships only when 90% are as fast or faster. A classic key map keeps their habits, like Insert and Delete for rows and date shorthand such as '5'. Then the human side: in-app tours, a short live session per role, a one-page key sheet, a champion in every bureau, and early movers keep their price for 12 months. If a large bureau still refuses, it moves with the late adopters in the last wave: end of life is announced in month 9, and legacy's last tax update is month 18. But one big bureau could eat the 30-customer margin at month 12, so I'd get bureau commitments early.

**Follow-up:** At the peak you're moving about 650 customers a month. How do you train that many people that fast?

Mostly in the product, not in classrooms. In-app tours and the key sheet carry the basics, live sessions are per role rather than per customer, and bureau champions train their own colleagues. Training is booked two weeks before each cutover. If support load climbs above 1.55 tickets per customer a month, that guardrail pauses new cutovers until it comes back down.

**Trap:** Leading with training instead of the speed-parity gate, or implying customers will be forced across before the month-18 end of statutory updates.

Source: Web client for keyboard-heavy accountants (p.6); Migration plan wave table and change management (p.13-14); Legacy end of life (p.16); Top risks (p.21)

### Say the board funds the eight weeks on Friday. What do you personally do in week 1?

I start what has the longest lead time and what could kill the plan. Day one, I rotate the plaintext database password we found in the code. Then three starts: the legacy test harness, because the rounding gap is only emulated and I want it confirmed on the real runtimes in weeks 2 to 4; the code parse for the rule inventory; and customer consent for fork analysis, so all 310 forks are classified by week 6. In parallel I open the cloud contract and the EU AI data agreement, book the outside security test, and pull real database sizes so the cost model can be checked against a real cloud bill in week 4. And I set up the steering committee, with one owner for each of the 13 assumptions, all confirmed by week 8.

**Follow-up:** What would make you recommend no-go at week 8?

Three things. If the old business objects can't run headless, I have no answer key for the cent-level proof. If the rule inventory can't reach 95% precision on ledger and VAT. Or if real database sizes and the real cloud bill break the cost case. Any of those, I'd recommend no-go or a re-scope, and the firm has spent about 0.6M EUR, not 4M.

**Trap:** Answering with generic kickoff activities ('stakeholder interviews, team onboarding') instead of the specific unknowns the week-8 gate has to settle.

Source: Decision requested (p.2); P1 gate (p.20); current-state findings (p.3); Forks (p.7); assumption A13 (p.4); Reference rounding note (p.3) and cost inputs (p.4)

### Who sits on your steering committee, what do they see, and who has the authority to stop a wave? Could the CEO override a red guardrail to make the 70%?

Stopping is automatic; restarting is a committee decision once the cause is fixed. Five guardrails sit under the dashboard: no correctness incidents, rollback under 2%, support tickets at or below today's baseline, every cross-customer isolation check passing, and AI auto-posting errors under 0.5%. Any breach pauses new cutovers. The steering committee reviews the seven KPIs monthly, refreshed weekly from live data, and owns the program gates. I'd want the CEO or CFO as sponsor, the CTO, the head of support, a senior accountant, security, and me. On the override: no, and I'd ask the board to agree that rule at week 8, before anyone is under pressure. The committee can change dates, scope or wave order, but it can't waive a mismatch to the cent. Logic differences go through the signed deviation register, one by one.

**Follow-up:** Who signs the AI gates, a committee?

No. Each of the four AI layers has a named person signing against a threshold set in advance: legacy engineers and an accountant on the rule inventory, two reviewers on money code, a data lead and an accountant on migration totals, and an accountant with the product owner on equivalence. Committees review; individuals sign. AI never approves its own work.

**Trap:** Describing a committee with no decision rights, or suggesting the 70% target could ever justify waiving a correctness guardrail.

Source: KPI dashboard and guardrails (p.16-17); Validation gates (p.15); L3 tolerance policy (p.11); assumption A10 (p.4); L0-L3 diagram (signers); committee membership and decision rights not in documents

### Platform ready in month 3 means two live cells, a cloud contract, an EU data agreement for AI, and an outside penetration test passed. In a financial-data business, procurement and security sign-off alone can take a quarter. What if that's late?

Then the first wave waits, because no customer data goes into the cloud until the isolation checks and the outside penetration test pass. The build itself is fast with AI; contracts and the security test set the pace, so I start both in week 1. Platform ready is planned for the end of month 3 and first customers for mid-month 5, so there are about six weeks of slack to the first wave. But a late platform hurts something sooner: the weekly rehearsal that migrates all 4,200 databases from month 4 runs inside the production security boundary, and that's where data-quality surprises show up. Every week it's late is a week less to find them. If it runs past mid-month 5, the first wave and the 70% date move with it, so I track contract and test dates as closely as the code.

**Follow-up:** Can you start the AI tooling on the code before the EU data agreement is signed?

Partly. The parser that maps the classes, methods and SQL is deterministic and needs no hosted AI, so the inventory map starts regardless. Hosted AI on the firm's code waits for the EU agreement, and customer forks also need customer consent, with no training on customer data. That's a hard line, which is why the agreement starts in week 1.

**Trap:** Claiming the platform is trivial and so carries no risk, or ignoring that contracts and the penetration test are external dependencies he doesn't control.

Source: P2 gate (p.20); roadmap slide speaker notes; assumptions A1 and A13 (p.3-4); L2 weekly fleet rehearsal (p.11); Migration plan slip note (p.13); roadmap diagram

### Take me through a cutover from the customer's side. When do they hear about it, what happens on the night, and what does a bad night at 2 a.m. look like?

They hear at least two weeks ahead and confirm their own numbers before anything moves. Two weeks out we scan their database and book their training. A week out we run a full rehearsal, reconcile every control total, and prove the trip back to legacy loses nothing. They then check opening balances in a preview. On the night, at 8 p.m. we lock the legacy writers and take a final extract; from about 9 we load, reconcile, run quick checks and a cross-customer isolation check, and only then switch them over. Cutovers run only from the 26th to the 9th, never mid-December to mid-February. A bad night means a check fails: we don't switch, legacy stays primary, they work as usual next morning, and we re-queue them. After go-live we can still move them back in hours, nothing lost, until their first cloud filing is accepted.

**Follow-up:** Your blackout windows depend on the calendar. Does it matter which month we start?

Yes. The winter freeze has to fall in the build months, before first customers, not inside months 5 to 12. Roughly, a kickoff between October and early December does that. If the freeze lands inside the wave months, 70% moves out by up to two months, so I'd lock the start date before committing to the month-12 number.

**Trap:** Giving only the technical pipeline with no customer-facing steps, or implying rollback is always available (it closes once the first cloud filing is accepted).

Source: Cutover runbook and ordering rules (p.14); Validation gates (p.15); Rollback paths diagram and text (p.15-16)

## Tax and accounting

### Your headline is 20 days against 10 to 14 weeks today. When exactly does that clock start? In real life, VMI or Sodra often publishes the final form or XML schema only days before it takes effect. What happens then?

The clock starts at official publication and stops when the signed rule pack, our bundle of tax settings, is live in production; we confirm that definition at the week-8 gate. The pipeline takes about 10 working days: AI compares the law, form and XML schema with the last version, an analyst writes the pack, we test it against golden files, the official expected outputs, and a sample of real customers, then a chartered accountant signs. The worst case is 20 calendar days against a target of under 3 weeks, so the margin is about a day. The median target is 14. If the final form lands days before the effective date, that date is the real limit, not our 20 days. So we build the pack from the draft, and the final schema becomes a small change that still goes through test and sign-off, about four working days.

**Follow-up:** Your packs hold 'form mappings'. Today FFData is filled by table and row position. What actually changes when VMI inserts a row in a new form version?

Legacy fills FFData, the e-form data file, by table and row position. So when VMI inserts a row, everything below it shifts, which is a big reason every form version is a copied class today. We rebuild statements on typed report models with named fields. The pack maps each named field to that form version's field, with dates. A new form version is a new mapping, checked against the official schema and golden files before anyone signs.

**Trap:** Claiming 20 days covers every case, mixing up 10 working days with 20 calendar days, calling the target '21 days', or hiding that the worst case leaves only about a day of margin.

Source: Statutory variability as configuration, p.6-7; Assumption A11, p.4; statutory pipeline diagram, p.7 (10 working days; worst case 14 working / 20 calendar; test days 7-8, sign-off day 9, publish day 10 'live on effective date'); KPI dashboard (median 14), p.17. Building the pack from a draft form is not in documents

### You found that legacy stores money as floating point, with five rounding routines that disagree. So when cloud and legacy differ by a cent on a VAT line, which one is right? Are you certifying legacy's bugs as 'equivalent', or quietly changing my customers' VAT?

Neither. History stays exactly as legacy computed it. New numbers follow one written rounding rule, and an accountant signs every real difference from legacy. The cloud stores money as exact decimals and takes its rounding policy from the rule pack. The tolerance policy has three parts. Noise below a field's declared precision, like fractions of a cent, is ignored. Half-cent boundary cases, where legacy's own copies already disagree, are approved once, as a class. Any real logic difference is fixed, or signed off one by one in the deviation register, our signed list of intended differences. So 'match to the cent' means no cent we can't explain. One honest caveat: the 1-in-560 figure comes from emulating the two routines, not running them. The test harness confirms it on the real runtimes in weeks 2 to 4, well before the week-8 gate.

**Follow-up:** And who decides which rounding rule is correct? You?

An accountant decides, not an engineer. The rule is set per jurisdiction and written into the rule pack as its rounding policy, signed like any other tax setting. Legacy's rule is meant to be half up to the cent. The trouble today is that one copy compares in floating point, so some half-cents land on the wrong side. Engineers build the rule; they don't choose it.

**Trap:** Saying the cloud will be identical to legacy, presenting 1 in 560 as a measured rate, or offering to recalculate history to clean it up.

Source: Current-state assessment, p.2; L3 tolerance policy, p.11; L2 'history is never recalculated', p.11; Assumption A10, p.4; Reference code evidence (VB helper vs MySQL CROUND), p.2, and rounding emulation note (354 of 200,000; confirmed weeks 2-4), p.3

### Where exactly is the line between a rule pack and code? Take the 2019 social-insurance reform, the 1.289 gross-up hardcoded in legacy payroll. Is that data or code? And if formulas stay in code, why not a rules engine so analysts can change those too?

Both. The 1.289 factor is data, but the 2019 reform changed how the calculation works, so that part ships as reviewed code. A rule pack holds dated rates and thresholds, form mappings, rounding policies and golden test files. That covers most changes: a new rate, a new form version, a new schema field. When the law changes a formula, like moving contributions from employer to employee and grossing up wages, two people review the code. It's versioned with the pack and can ship on any day, so it meets the same 20-day limit. We rejected a scripting engine on purpose. Every script is code a non-engineer can change outside code review, and that's hard to govern. Today 20 year-specific rules like this one are hardcoded. Their dates and factors all move into packs.

**Follow-up:** Today every company types in its own rates and can even edit its NPD formula. When you switch to central packs, some payrolls will change. Isn't that a regression?

It's a difference we catch and sign off, not a silent change. Every payroll customer must match one shadow payroll of its own before it moves. So a company whose rates differ from the official pack shows up in that run. Either their setting was wrong and we fix it with them through the signed register, or it's a real special case and becomes a setting on their account. History is never recalculated.

**Trap:** Claiming every statutory change becomes configuration, proposing a scripting language or AI to run tax rules, or not recognizing the 1.289 gross-up.

Source: Statutory variability as configuration, p.6-7; Current-state assessment (20 year-specific rules), p.3; L1 module table (Payroll) and gate (two reviewers on money code), p.9-10; Trade-off analysis (Statutory row), p.18; Reference code evidence (WageVDUInfo.vb 1.289; Company.vb NPD formula), p.2. The details of the 2019 reform are not in documents

### My accountants have used this desktop app for fifteen years and type faster than the screen redraws. Who picks your 25 workflows, who are the 'power users', and what happens to the 10% that are slower?

Your own heaviest users time them, including bureau accountants, and the 25 come from what people actually do most, agreed with your support team, not our guesses. They time each workflow side by side on legacy and on the web, and a module ships only when at least 90% are as fast or faster. The key map copies today's habits, which we read from the legacy code. Insert and Delete add and remove rows, Enter and Tab move across cells, pickers filter as you type, and dates take shorthand like '5' or '-5'. The target is under 50 milliseconds from keystroke to screen, and automated tests replay key sequences on every build. We don't write off the slower 10%. Each one gets a name and an owner, and we re-time it before the next wave.

**Follow-up:** And if they still refuse to leave the desktop?

Then they move last, in months 13 to 18. Legacy still gets every tax change in under 3 weeks until month 18, and hosting ends in month 20, announced in month 9. But holding out isn't free for us: the 70% target clears by only 30 customers, so one large bureau waiting would use up that slack. That's why every bureau gets a champion, and early movers keep their price for 12 months.

**Trap:** Promising the web is faster everywhere, treating the slower 10% as acceptable losses, or brushing off keyboard habits as resistance to change.

Source: Web client for keyboard-heavy accountants, p.6; Assumption A9, p.4; Reference code evidence (grid keys, date shorthand), p.3; Reference non-functional targets (50 ms) and stack (Playwright keyboard tests), p.3-4. How the 25 and the timers are chosen is not in documents

### Two matching shadow payrolls, months 5 and 6, unlock payroll for everyone. But payroll's hard cases are annual and event-driven: sick pay, vacation pay on average earnings, terminations, year-end. Two ordinary months won't exercise those. Why is two enough?

Two shadow runs aren't the proof on their own. They're the last live check on top of four test sets. Replayed history from 300 customers covers the sick leave, vacation pay, terminations and year-ends those companies actually ran, compared payslip by payslip against legacy. A million generated edge cases a night cover the rare combinations. Official golden files and one test per payroll rule cover the legal side. The payroll gate also needs the Sodra and income-tax packs accepted in test. The shadow runs add real inputs from real users in a live month. Then every payroll customer must match one shadow payroll of its own before it moves. If the runs don't match, payroll customers stay on legacy and the gate slips. Nobody's payroll is the experiment.

**Follow-up:** What if a payroll error shows up after the first SAM or GPM313 has gone to Sodra or VMI from the cloud?

Then we're past the rollback point, so we fix it forward with a priority hotfix. Posted entries don't change, so the fix is a correction, and the customer files a corrected declaration. Every payslip records its pack version, so we know exactly which employees and months are affected. And any correctness Sev1, our top severity, pauses all new customer moves across the fleet.

**Trap:** Defending two months as enough on their own, or not knowing what else gates P4 and G0 require.

Source: L3 proving financial equivalence (four test sets, shadow payrolls), p.11; Roadmap gate P4, p.20; Validation gate G0, p.15; Rollback diagram and text, p.15-16. Which events the replayed history covers is not spelled out in documents

### Most of your customers stay on legacy for most of year one, and some until month 18. Today a change takes 10 to 14 weeks. How do legacy customers, including the 310 forks, get every change in under 3 weeks from month 4?

Through a legacy fast lane. I'll say it first: rebuilding all 310 legacy forks automatically by month 4 is the boldest promise in this plan. The fast lane reuses the cloud work: the same analysis of the change and the same golden test files. Forks are frozen at month 3, so each one is a fixed target. A pipeline builds it, tests it and ships an out-of-cycle patch. All 310 are classified by week 6, so we learn early which ones are hard. If automation doesn't reach all of them by month 4, the fallback is the biggest forks first and the rest patched by hand. Hand-patched forks are the ones at risk of missing 20 days, and you'd see it, because the turnaround KPI tracks legacy customers too.

**Follow-up:** Why not freeze legacy completely and push forked customers to migrate sooner?

Because the law doesn't wait for our plan. A forked customer still has to file correctly in month 6. And forked customers can't move sooner anyway: extension tiers go live in month 8, so most move in months 10 to 12, and forks that fit no tier move last, in months 13 to 18. We limit the burden another way: forks frozen at month 3, features at month 6, and the last tax update at month 18.

**Trap:** Presenting the fast lane as proven, forgetting that legacy customers count in the turnaround KPI, or saying forked customers just have to wait until they migrate.

Source: Statutory variability as configuration (legacy fast lane), p.7; From 310 forks to extension points, p.7; Legacy end of life, p.16; KPI dashboard (turnaround for cloud and legacy), p.17; Reference KPI trajectory (statutory turnaround), p.6; Roadmap gate P5, p.20; deck speaker notes (statutory slide, fallback)

### Who actually signs a statutory change? And when a signed pack is wrong, say a wrong PSD rate goes live and a thousand companies run payroll on it before anyone notices, what happens?

A named chartered accountant signs every pack, on day 9 of the pipeline, and only after golden files, schema checks and a sample of real customers have passed. If a signed pack is still wrong, that's a correctness Sev1, our top severity, so new customer moves pause while we fix it. We can size the damage exactly, because every calculation records its pack version. One query gives the companies, payslips and periods affected. A corrected pack goes through the same tests and sign-off. Affected payslips get corrections as reversals, never a silent recalculation. Anything already filed with Sodra or VMI needs a corrected declaration, which the product prepares and the customer's accountant submits. For context, every company types in its own rates today, so this kind of error can already happen. It's just scattered and invisible.

**Follow-up:** Is one signer enough for something that hits a thousand payrolls?

The named signer is the accountable owner but doesn't work alone. A pack can't reach them until golden files and the sample of real customers pass. For payroll packs, I'd add a second signer if discovery shows the risk calls for it. Both can sign on the same day, so it doesn't add time to the 20 days.

**Trap:** Saying a signed, tested pack can't be wrong, handing the decision to AI, or recalculating posted payslips in place.

Source: Statutory pipeline diagram (day 9 sign-off by a chartered accountant), p.7; Statutory variability (pack version on every calculation), p.6; ledger rules (corrections are reversals), p.6; KPI guardrails (correctness incidents pause cutovers), p.17; Reference glossary (Sev1), p.7; Current-state assessment (rates typed per company), p.3. The incident steps are not in documents

### Accountants reopen periods all the time: a late supplier invoice, an auditor's adjustment, an amended VAT return. If posted entries never change and a closed period is locked, how does my accountant correct March's VAT return in July?

With a correction, not an edit: a reversal and a new entry, posted now but dated March for tax. That works because every entry keeps its accounting, tax and effective dates separate. So the corrected March return is built from March's tax-dated lines, using the rule pack in force for March. Closing a period locks posting into it. When an accountant really needs to reopen one, it's an explicit action that needs permission and gets logged. It's never a quiet edit. The value is the audit trail. VMI and the auditor can see what was filed, what changed, when, and by whom. And AI never touches a closed period.

**Follow-up:** Isn't that a big habit change? Today they just open the invoice and fix it.

It is a change, and a deliberate one. A document edits freely until it's posted. After that, the correction is one action that creates the reversal and the new entry together, so it's designed to feel like an edit. It's on the one-page key sheet and in the role training. If it hurts, the ticket guardrail of 1.55 per customer a month shows us fast, and any breach pauses new moves.

**Trap:** Saying periods can never reopen, which accountants can't work with, or saying they can just edit, which breaks the design.

Source: Modular monolith and financial core (ledger rules: reversals, separate dates, period lock), p.6; Statutory variability (effective-dated packs, pack version recorded), p.6; AI in the product, p.12; KPI guardrails (1.55 tickets), p.17; Change management, p.14. The reopen procedure is not in documents

### A bureau accountant serves 40 companies. Some run payroll, some are on forks. 'Bureaus move as a portfolio', so does the slowest client hold up the other 39? And meanwhile the bureau works in two systems for weeks.

No. A client that isn't ready doesn't hold up the other 39; the portfolio moves together where it can. Bureaus move mostly in wave 3, months 8 to 10, after all nine modules have passed the equivalence test. So modules aren't the blocker; forks are. A forked client whose changes fit no setting, template or add-on follows in the last wave. Yes, for those clients the bureau works in two screens for a while, and I won't pretend otherwise. One sign-in portal keeps it to one login and sends each company to the right system, and each company's books still have exactly one writer. Capacity isn't the problem: we move 100 customers a night, so a 40-company bureau can go in one night.

**Follow-up:** Confirming 40 sets of opening balances is a week of work. When do they do it?

In the preview window, seven to two days before the move. For bureaus we'd book moves in the first days of the month, so that window falls after the filing rush; there are no moves from the 10th to the 25th anyway. The control totals already matched to the cent in rehearsal, so the bureau confirms a short list of balances; it doesn't re-audit the books. The bureau's champion coordinates it.

**Trap:** Ignoring the pain of working in two systems, or claiming a bureau never works in two systems at once.

Source: Migration plan (waves, ordering rules, 100 a night), p.13-14; Coexistence (one writer, one sign-in portal), p.14; Cutover runbook (T-7 to T-2 preview) and change management (bureau champion), p.14; Validation gate G2, p.15; Roadmap gate P5, p.20; Assumption A4, p.3. Splitting a portfolio and scheduling bureau moves early in the month are not in documents

### Lithuanian law says accounting records must be kept for ten years. You switch legacy off in month 20. If VMI audits a customer's 2019 VAT and payroll in 2029, what does the accountant actually open?

They open the cloud. A customer's history moves with them exactly as legacy computed it and is never recalculated, so the 2019 numbers match what legacy produced at the time. Documents sit in storage that blocks changes after the fact. Separately, every legacy database becomes an encrypted, read-only archive, kept for 10 years after hosting goes off. That's the original record if anyone questions the move. The 10-year rule is one of our written assumptions, and we confirm it at the week-8 gate. One gap I'd close in discovery: an archive only counts if someone can read it. So I'd keep a simple read-only viewer with the standard reports, not hand an auditor a database dump.

**Follow-up:** And GDPR? That's ten years of payroll personal data.

The legal duty to keep accounting records outweighs a request to erase them, but access has to be tight. Archives are encrypted with a separate key per customer, support access is limited and logged, and AI never trains on customer data. Anything the legal record doesn't need, like old session logs, would go on a shorter schedule.

**Trap:** Saying a database archive is enough with no way to read it, or implying history gets recalculated in the cloud.

Source: Legacy end of life (month 20, 10-year archives), p.16; Assumption A8, p.4; L2 (history moves as computed), p.11; Reference stack (immutable document storage, per-tenant keys), p.3-4; Tenant isolation (support access scoped and logged), p.6; Assumption A13, p.4. The archive viewer and GDPR handling are not in documents

## Skeptic

### You clear 70% by 30 customers out of 4,200, under 1%. And your hardest wave, forked customers and dedicated databases, is 1,400 tenants crammed into the last three months. Realistically, isn't month 12 already gone?

No, but it's tight, and I put that on the slide myself: 2,970 against 2,940 is 30 customers of slack. A slip moves 70% out about month for month, and one that hits the winter freeze adds up to two months more. The hardest wave goes late on purpose: lowest complexity first is how we learn safely. And moving capacity isn't the constraint. The factory handles about 1,000 customers a month against a planned peak of 650. The constraint is readiness, meaning modules passing the equivalence tests and fork manifests complete, and that shows early: the plan says 1,170 customers by month 9, three months before the deadline. The response to a gap is more ready customers, not weaker gates: bureaus move whole portfolios, and early movers keep their price for 12 months.

**Follow-up:** If you're 200 customers short in month 11, will you relax a gate to make the number?

No. Correctness and isolation always outrank speed, and that's built into the dashboard: any guardrail breach pauses new cutovers. If we're short, I'd tell the steering committee that 70% most likely lands in month 13, and why. Missing a date by a month is recoverable. Moving a customer whose numbers don't match breaks the one goal the brief sets at zero.

**Trap:** Claiming hidden buffer, getting defensive, mixing up factory capacity with customer readiness, or hinting that gates could be loosened to make the number.

Source: Migration plan: wave plan, ordering rules and factory capacity (pages 13-14); Change management (page 14); Validation gates, G0 and wave gate (page 15); P6 gate (page 21); Reference, KPI trajectory (page 5); migration curve diagram

### Your whole timeline rests on AI translating half a million lines of 2006 VB.NET and CSLA into working C# in about five months. What evidence do you have that works at this scale, and what happens when the output is wrong?

Honestly, nobody can show proof at exactly this scale yet, so the plan doesn't depend on trusting it. First, the scope is smaller than it sounds: we translate at most about 140,000 lines, not 522,000, the money logic in ledger, VAT, payables, inventory, fixed assets and payroll. The 180,000-line desktop UI, over half of it designer-generated, is rebuilt from specs, and so are bank import, statements and e-filing. VB.NET and C# compile to the same .NET types, so line-by-line translation is the mechanical part. The real risk is meaning: floating point to exact decimals, and a global company context used 321 times. So no AI change merges unless the compiler, tests and the differential suite, side-by-side tests against legacy, are green, with two reviewers on money code. If a module's acceptance stays low for two sprints, engineers take it over.

**Follow-up:** And the moment engineers take a module over by hand, your month-5 date is gone, isn't it?

Not the whole date, and we'd see it early. Module work starts in month 2 and acceptance is tracked every sprint, so two weak sprints show up well before month 5. Month 5 needs only ledger, VAT and its filing, payables and bank import; if inventory or payroll slips, the simple waves still go without them. A slow module moves only the waves that need it, roughly month for month. The fallback is a later date, never a weaker test.

**Trap:** Accepting the '522,000 lines translated' framing, quoting AI accuracy figures he doesn't have, or implying AI output is trusted without the differential tests.

Source: Layered AI: L1 module table and approach (pages 10-11), L1 gate and fallback (page 9); Reference, Codebase at a glance (page 1) and Code evidence, global company context (page 3); roadmap diagram (page 20)

### About 4M EUR to save under 2M a year, cash payback in month 44. And if cloud runs 35% over, which it usually does, it's month 56. Why would a CFO fund this instead of just optimizing today's hosting?

Because cash isn't the main case, and I won't pretend it is. On infrastructure alone, about 4M EUR buys about 1.8M EUR a year from year 3, so cash payback is year 4. The real case is risk and speed. Tax changes take 10 to 14 weeks against a 6-week legal window; the plan brings that to 20 days at most. The knowledge sits with four engineers on a frozen 2006 stack, and 310 forks multiply every change. Optimizing hosting keeps 4,200 databases and 4,200 upgrades per release, so cost stays per customer: a new customer adds about 590 EUR a year today against about 230 on the new platform. And I haven't counted freed support and engineering time, about 1M EUR a year. Counting it, payback is month 35.

**Follow-up:** Cloud overruns are common. What protects the company if the bill really comes in 35% high?

Two things. First, we find out early: the estimates are checked against a real cloud bill in week 4, before the week-8 go or no-go, when about 600,000 EUR is spent, not 4M. Second, there's headroom: at full scale, even 35% higher lands about on the 406 EUR per-customer target, though at month 12, while the platform is still filling up, the margin is about 20%. If the bill points to month 56, the board decides on evidence.

**Trap:** Counting freed time as cash, brushing off the sensitivity numbers, or claiming cloud costs won't overrun.

Source: Business impact, table, sensitivity and 'Beyond the cash' (pages 18-20); Executive summary, money (page 2); Trade-off analysis (page 18); what-not-to-do, 'Bigger servers, one database each'; Reference, Cloud cost inputs (page 4); cost-model output

### Big ERP rewrites have a long history of running years late or being abandoned. This is a rewrite. Why is yours the exception?

I don't assume it's an exception; I designed against the three ways rewrites usually die. One, the old system keeps moving, so you never catch up. Here, forks freeze in month 3 and features in month 6. Two, the unwritten rules get lost. Here, legacy runs headless, without its screens, as the answer key, so a rule we missed shows up as a difference in the nightly tests, replayed history from 300 customers plus a million generated cases, before anyone moves. Three, everyone cuts over on one night. Here, customers move one at a time, with a rehearsed way back until their first cloud filing. And the money at risk before we have evidence is about 600,000 EUR for eight weeks, not 4M EUR.

**Follow-up:** Your safety net depends on 2006 CSLA code running headless as the answer key. What if it won't run outside the desktop?

Then we learn it by week 8, because a running harness is a pass condition for the go or no-go. The code is favorable: business logic is already separate from the UI. If it still fails, replayed history partly works, since legacy's own results sit in each database, but I'd bring a re-plan to the gate rather than push on.

**Trap:** Making 'AI changes everything' the main argument, naming failed projects to look superior, or sounding certain instead of controlled.

Source: Trade-off analysis (page 18); L3 test sets (page 11); Migration plan, coexistence and rollback (pages 13-16); Legacy end of life (page 16); Executive summary, decision requested (page 2); Assumption A12 (page 4); roadmap diagram, nightly differential runs (page 20)

### You're building a modular monolith for a SaaS that wants three countries. Isn't that tomorrow's legacy system? And with 600 customers in one database, one runaway query in filing week takes down 600 sets of books.

I chose the monolith because of the domain, not convenience. Posting one invoice touches four modules in one transaction. Split into services, that becomes a saga, a chain of steps that can fail halfway, and books can end up half-posted. We scale out by cells: each is about 600 tenants with its own database and read replica, sized for three times average load in filing week. Seven cover everyone today; more customers means more cells, and a new country is a new rule pack. The largest 3% get a dedicated database, so they can't crowd out neighbors. Anything slow, external or untrusted, like document extraction and filing, runs in separate workers through the outbox, events saved in the same transaction as the data. Architecture tests enforce module boundaries, and we'd split a module out if teams pass about 50 people or its load diverges.

**Follow-up:** A bad release or schema change still hits 600 customers at once, though?

Yes, up to one cell, and that's what cells are for. Cells are the unit of release, and every release goes to a canary cell first, so a bad change reaches about 600 tenants at most, not 4,200, before it's stopped. Any failed cross-tenant probe blocks the release, and filing days, the 15th to the 25th, carry a higher availability target of 99.95%.

**Trap:** Dismissing microservices dogmatically, conceding the monolith is a stopgap, or ignoring the noisy-neighbor and blast-radius half of the question.

Source: Target architecture: Tenant isolation and Modular monolith (pages 5-6); Assumption A5 (page 3); Trade-off analysis (page 18); Reference, Technology stack, Non-functional targets and Glossary (pages 3-6); speaker notes, 'rejected' slide

### You promise zero financial regression, but your own code reading says legacy's rounding copies disagree with each other on about 1 in 560 VAT calculations. If legacy doesn't agree with itself, what exactly are you matching to the cent? Isn't 'zero regression' really 'zero unsigned deviations'?

Yes, it's zero unsigned deviations, and I think that's the only honest way to define zero. Every ledger, VAT and payroll number must match legacy to the cent, and any intended difference sits on a signed register approved by an accountant. Where legacy disagrees with itself, the harness compares against whatever legacy actually computed for those inputs. Half-cent boundary cases are approved once, as a class, under a written tolerance policy; every logic difference is fixed or signed off one by one. Two things stop that becoming a loophole: history moves exactly as legacy computed it, never recalculated, and mutation tests deliberately flip a sign or a rate to prove the harness catches it.

**Follow-up:** And that 1-in-560 comes from a Python emulation, not the real system. Why put an unverified number in front of a CTO?

Because it's worth knowing before we start, and I say 'our emulation suggests' for exactly that reason. I read the VB rounding helper and the MySQL rounding function and emulated both: over every half-cent value, and over 200,000 random VAT amounts, which gives about 1 in 560. The harness confirms it on the real runtimes in weeks 2 to 4. Whatever the real rate, the design doesn't change: half-cent cases are approved once, as a class.

**Trap:** Insisting 'zero' means mathematically no differences at all, making the tolerance policy sound like a loophole, or treating the 1-in-560 figure as confirmed.

Source: Assumption A10 (page 4); L3 tolerance policy and mutation tests (page 11); L2, history never recalculated (page 11); Current-state assessment (page 2); Reference, Code evidence rounding note (page 3); plain-English summary, accountant sign-off

### Is a team of about 30 enough for a platform, nine modules, a web client and 4,200 migrations in a year? Or is it too many people piling into code only four people understand, while those four review every money rule and hand their maintenance to newcomers in week 2?

I think it's about right, but it's an assumption and I label it as one: about 30 for a year, then about 10 for six months, working alongside the firm's own engineers, with the exact size set in discovery from measured throughput. It isn't 30 people learning old code. Most of them build new things, the platform, web client, migration factory and test harness, that don't need tribal knowledge. That knowledge funnels into one bottleneck we protect: the four legacy engineers and an accountant review every money rule, and the delivery team takes over their maintenance from week 2 to free their time. The week-8 gate tests this early: if the rule inventory isn't at 95% precision on ledger and VAT, we've learned that for about 600,000 EUR.

**Follow-up:** A new team taking over maintenance of untested 2006 code in week 2: isn't that the very knowledge problem you described?

It's a real risk, and it's the top one on my list: knowledge sitting with four engineers. The new team takes the routine load, triage and known fixes, with the four on call for hard cases. That load shrinks fast: forks freeze in month 3 and features in month 6. The point is protecting the four's review time, because that's the true critical path.

**Trap:** Defending 30 as a precise figure, ignoring the four-engineer bottleneck, or naming who supplies the delivery team.

Source: Assumption A6 (page 4); L0 rule inventory (page 10); Business impact, investment (page 19); Roadmap gate P1 (page 20); Team and Top risks (page 21); study sheet 'Numbers to know cold'

### Your statutory promise is 20 days for every customer from month 4, legacy included. That means automatically building all 310 hand-maintained forks, which probably haven't been built reproducibly in years. You called it your boldest promise. What happens when 60 of them won't build?

Then those customers get the change by hand patch, as they do today, and some may miss 20 days. I'd report that, not average it away. It is the boldest promise in the plan, which is why I say it first. Why it's plausible: all 310 forks are diffed and classified by week 6, they freeze in month 3, and the fast lane reuses the same analysis and golden test files as the cloud pipeline, so each change is analyzed once, not 310 times. The fallback is ordered: the biggest forks first, and the tail patched by hand. And turnaround is measured for legacy customers too, so the dashboard shows it if the fast lane falls behind.

**Follow-up:** So, honestly, is the 3-week target met for every customer from month 4?

It's the plan from month 4, but it's proven in steps, and the dashboard says so: the first pack change measured within 20 days is the month-6 target, and every change within 20 days is the month-9 target. The main legacy release and cloud customers are the easier part. If anything misses, it's the small forks at the end of the list, and they get hand patches meanwhile.

**Trap:** Insisting all 310 forks will build, or quietly narrowing the promise to cloud customers only.

Source: Statutory variability, legacy fast lane (pages 6-7); From 310 forks to extension points (page 7); Legacy end of life (page 16); KPI dashboard, statutory turnaround (page 17); Reference, KPI trajectory (pages 5-6); speaker notes, 'statutory' slide; study sheet 'Say it first'

### Every target lands just inside the line: 70.7% against 70, 20 days against 21, all nine modules live with three months to spare. Honestly, did you start from the answers and work backward?

Partly, yes, and that's what planning to a fixed target means: the brief set the dates, so I sized the waves and the team to them. The fair test is whether the inputs are real and the slack is shown. Where it's thin, I said so first: 30 customers on the 70%, one day on turnaround at worst. Where it isn't, that's visible too: run cost is 330 EUR per migrated customer against a 406 target, and the factory can move about 1,000 customers a month against a 650 peak. An earlier draft was corrected the other way: a reviewer caught 'under 3 weeks' written as 21 days, and a capacity plan that ignored tax-deadline blackouts. The week-8 gate swaps my assumptions for measurements.

**Follow-up:** Then which numbers in your plan are measured, not assumed?

The code facts are counted from the repository: 522,000 lines, 377 business classes, 770 SQL statements, 228 floating-point money columns, no tests. The baseline, 3.1M EUR, 6,500 tickets a month and 310 forks, comes from the brief. Cost, team size and throughput are planning estimates, and the rounding gap is emulated; I label all of those. The week-4 cloud bill and the week-8 gate turn them into measurements.

**Trap:** Flatly denying it, which isn't credible, or conceding the numbers are invented; failing to separate counted code facts from planning estimates.

Source: Executive summary (page 1); Migration plan, factory capacity (pages 13-14); KPI dashboard (page 17); Team (page 21); Reference, Codebase at a glance, Code evidence and Cloud cost inputs (pages 1-4); codebase-facts; what-not-to-do, 'Traps a reviewer caught in our first draft'

### Your summary says run cost per customer is down 55% at month 12. But your own KPI table shows realized savings at month 12 at break-even, and year-1 savings negative. So at month 12 the hosting bill hasn't moved. Isn't that 55% just a choice of denominator?

It's a definition, and I show both sides. The 55% is cloud run cost over cloud customers, about 330 EUR against 738: what a customer costs on the new platform, which is how I read the brief's per-customer target. You're right that the company's total bill at month 12 is still about where it is today, because we're running two estates and legacy hosting doesn't shrink customer by customer. That's why the dashboard shows blended cost alongside, and why the full saving, about 1.8M EUR a year, only arrives from month 21, after legacy is switched off. Across all customers, once legacy is off, it's about 300 EUR, down 59%.

**Follow-up:** Why does legacy cost stay that high with only 1,230 customers left on it?

In the model, legacy hosting comes down in steps as servers empty and contracts end, not per customer: about 700,000 EUR in year 2, then nothing once it's switched off in month 20. That's a planning assumption. I'd check it against the actual hosting contracts in discovery and shrink legacy hosting faster if they allow it.

**Trap:** Getting caught implying the company saves 55% at month 12, or arguing about the definition instead of admitting the double-running cost.

Source: Executive summary goals table (page 1); KPI dashboard, run cost and realized savings (page 17); Business impact table (page 19); Reference, Cloud cost inputs and KPI trajectory (pages 4-6); cost-model output

## Hiring manager

### Say we put you on site at this client on Monday. Walk me through your first two weeks: who do you talk to, what do you look at, and what do you hand the CTO at the end of week two?

By the end of week two I hand the CTO one page: each of my thirteen assumptions marked confirmed, wrong or still open, and what that changes in the plan. Week one is people. I sit with the four legacy engineers, watch bureau accountants work at their own desks, and confirm with finance what the 3.1M EUR really covers. From week two the delivery team takes over those engineers' maintenance, so they have time to review rules with me. Week two is data: profile a sample of customer databases for size and hand-made schema differences, cluster twelve months of tickets, and, with customer consent, pull the 310 forks together for AI diffing. The legacy test harness starts on day one, because my rounding finding is emulated and I want it confirmed on the real runtimes by week four. And on day one, we rotate that plaintext database password.

**Follow-up:** Which of those assumptions, if it turns out wrong, hurts the plan most?

A12: that the legacy business objects run without the desktop screens. Legacy is my answer key; every ledger, VAT and payroll number is compared against it. The code makes it likely, because business logic is separate from the UI, but it's unproven until it runs, which is why the harness starts on day one. Commercially, the riskiest is A9: that accountants accept a browser app if keyboard speed matches the desktop.

**Trap:** Treating his plan as settled and spending week one 'validating the architecture' or only reading code; or promising a finished design by week two instead of confirmed assumptions.

Source: Assumptions, pages 3-4 (13 assumptions, all confirmed at gate P1; A2 what the 3.1M EUR covers; A9; A12); Current-state assessment, page 3 (plaintext password, rotate now; logic separate from UI so legacy runs headless); L0, page 10 (tickets, fork diffs, delivery team takes over maintenance from week 2); A13, page 4 (consent before fork analysis); Reference page 3 (rounding confirmed on real runtimes in weeks 2-4). The day-by-day two-week sequence and the week-two one-pager are not in documents.

### Let's be candid: how much of this case study did AI produce, and how did you verify what it gave you?

A lot of the drafting and analysis was AI-assisted, and every number and decision in it is mine to defend. I used AI the way the plan does: it drafts, tools check, I sign. It helped draft text and diagrams, and wrote the rounding emulation and the cost model script. I set the questions and checked the outputs: every code count comes from plain command-line tools on the real repository at one fixed commit, so anyone can re-run it, and the money figures come from re-running the cost model, so the deck, case study and study sheet agree. A review pass caught real mistakes in the first draft: 50 moves a night that ignored tax-deadline blackouts, "under three weeks" quietly written as 21 days, one saving counted twice. And I label what's unproven: the rounding gap is emulated, not yet run on the real runtimes.

**Follow-up:** Give me one concrete thing in the first draft that was wrong and that you caught.

The calendar. The first draft scheduled 50 customer moves a night as if every night were usable. But you can't cut a customer over between the 10th and the 25th, when filings fall due, or from mid-December to mid-February. Redone properly, it's 100 a night on about 10 usable nights a month, roughly 1,000 a month against a planned peak of 650.

**Trap:** Downplaying AI use (dishonest and easy to spot), or over-crediting it ('the AI worked that out') so he cannot explain a number when the panel probes it.

Source: Not in documents (how AI was used to prepare the case study). Supporting: codebase-facts.md (counts from find, grep and wc at commit 2320f1c); Reference pages 3 and 5 (rounding emulation; cost model is a short Python script); what-not-to-do, 'Traps a reviewer caught in our first draft'; Migration plan, page 14 (blackouts 10th-25th and 15 Dec-15 Feb; 100 a night on about 10 usable nights, about 1,000 a month against a 650 peak).

### In week one the client CTO tells you, 'A monolith in 2026? We want microservices.' He's the buyer. What do you actually say to him?

I'd agree with his goal, independent scaling and teams that don't block each other, and show him a modular monolith gets there with less risk. One invoice posting touches four modules in one transaction. Split into services, that becomes a saga, a chain of compensating steps, and every failure in that chain is a chance for the books not to balance. We scale by cells of about 600 tenants instead, and anything slow, external or untrusted runs outside through the outbox, events written in the same transaction as the data: extraction, filing, analytics and migration. Architecture tests guard the module boundaries, so splitting one out later is cheaper. I'd put the trigger in writing: we split a module when the teams on the new code pass about 50 people or its load diverges. If he still disagrees, we write the decision down and settle it at the week-8 gate.

**Follow-up:** And if he says, 'I'm paying, do it my way'?

Then it's his call, and my job is to make it an informed one. I'd write down the price: one posting spread across services, a bigger team to run it, and likely a later first wave, and ask for it as a steering decision. Then I'd deliver it well, and fight to keep the financial core, the ledger and everything that posts to it in one transaction, inside one service.

**Trap:** Being dismissive ('he's wrong') or folding instantly to please the buyer; giving no condition under which he would split out a service.

Source: Target architecture, 'Modular monolith and financial core', page 6 (four modules in one transaction; outbox to four workers; architecture tests guard boundaries); Reference glossary, page 6 (transactional outbox); Trade-off analysis, page 18 (microservices split one posting and need a bigger team); deck speaker notes, 'rejected' slide (split a module out past about 50 people or diverging load). Settling it at the week-8 gate is not in documents.

### It's month 4. The VAT equivalence tests are stuck below 100%, and first customers in month 5 won't happen. How do you tell the steering committee, and what do you ask them for?

I tell them the day I know, not at the next scheduled meeting, and I bring options, not just news. One page: what slipped and why, here the VAT equivalence suite isn't at 100%; what it moves; and what it doesn't touch. The honest impact: the 70% target has only 30 customers of slack, so a one-month slip moves 70% about a month, and if it runs into the mid-December freeze, up to two months more. Payback moves too: a three-month slip takes cash payback from month 44 to about 49. Then three options: add capacity on VAT; if the gap is half-cent cases, have the accountants sign them off once, as a class, under the tolerance policy we already agreed; or accept the new date. What I won't offer is a lower gate. No customer moves until their numbers match to the cent.

**Follow-up:** The CEO says, 'Just move the simple customers anyway; VAT can wait.' What do you do?

I'd say no to that one, and explain it isn't stubbornness. The first-customer gate itself needs VAT to pass, because almost every customer invoices with VAT, and a customer moves only when every module they use has passed equivalence. Once the tax authority accepts a filing from the cloud, we can only fix forward, never roll back. I'd pull other ready work forward instead, like mapping forks to extension manifests.

**Trap:** Softening or delaying the news, blaming the client team, or offering to relax the to-the-cent gate to save the date.

Source: Migration plan, pages 13-14 (30 tenants of slack; winter freeze adds up to two months; a tenant moves only when every module it uses has passed L3); Business impact sensitivity, page 19 (waves slip 3 months, payback month 49); L3 tolerance policy, page 11 (half-cent cases approved once, as a class); KPI dashboard, page 16 (weekly refresh, monthly steering review); Roadmap gate P3, page 20 (Invoicing and VAT and VAT filing must pass L3); Rollback, page 16 (fix forward after the first accepted cloud filing). How to communicate a slip is not in documents.

### You can clearly do the architecture. Why do you want a forward-deployed, client-facing role rather than a pure architect or engineering-manager seat?

Because the hardest part of a program like this isn't the architecture, it's getting a CTO, a CFO and thousands of accountants to trust it, and I want to own both halves. This case study is how I like to work. I went into the code, the rounding helpers, the schema, the way tax forms are built, and turned what I found into a decision a steering committee can actually make: eight weeks, about 0.6M EUR, go or no-go on evidence. A pure architect hands that conversation off. An account lead usually can't take it down to the code. A forward-deployed role sits exactly where the business problem meets the system, and lets me adjust the plan fast when the client's reality turns out different from the slide. That's the work I'm best at and enjoy most.

**Follow-up:** What part of client-facing work do you find hardest?

Giving bad news before I have the full fix. My engineering instinct is to solve it first and report after. The discipline I hold myself to is the opposite: "here's the problem, here's what we know, options by Thursday." That's why the plan has weekly KPI refreshes and a monthly steering review, so bad news has a regular, early place to land.

**Trap:** Generic lines about 'loving customers' or the company's brand, implying he wants to escape coding or escape clients, or inventing credentials he cannot back up.

Source: Not in documents; draws on Executive summary decision request, page 2, and Current-state assessment, pages 2-3.

### Three months in, the client's head of sales wants AI cash-flow forecasting in the first release, and the CFO wants Latvia added this year. How do you push back without losing the room?

I don't say no; I say what it costs and let the steering committee choose. Every request goes through one change path: which of the five goals it serves, which gate it moves, and what it costs in people and weeks. Forecasting fails the first test. Scope is parity plus the four AI features the brief named, so forecasting goes on the backlog for after parity. Latvia is different: the design already allows it, because jurisdiction is part of every rule pack, our signed bundles of tax settings. But the same rule-pack team is building the remaining Lithuanian forms until about month 9, and the 70% target has only 30 customers of slack. So I'd show that trade and propose Latvia right after the 70% gate in month 12.

**Follow-up:** What if the CEO overrules you and says forecasting is in?

Then it's in, with a visible price. I re-plan, show the new date or the extra capacity on the dashboard, and log it as a steering decision, so nobody is surprised in month 11. My job is to make the trade-off visible and get a clear decision, not to win the argument.

**Trap:** A flat 'no' that alienates the client, or a 'yes' that quietly eats the 30-customer slack on the 70% target.

Source: Assumption A5, page 3 (Lithuania first, Latvia and Estonia later; jurisdiction in every rule pack); Statutory variability as configuration, page 6; AI in the product, page 12 (four AI features ship with the product); Migration plan, page 13 (30 tenants of slack); 12-month roadmap diagram, page 20 (statutory 'remaining forms' runs to about month 9); Reference glossary, page 7 (rule pack). The change-request process itself is not in documents.

### The client CTO pushes back on your timeline: 'Platform in three months, 310 forks rebuilt by month 4, 70% with 30 customers of slack. This is fantasy.' How do you hold your ground without overselling?

I'd agree with half of it out loud, because some of it is tight and I put that on my own slides. The 70% target has 30 customers of slack, and rebuilding all 310 legacy forks by month 4 is my boldest promise; the fallback is the biggest forks first and the tail patched by hand. What I'd defend is the structure: nobody is asked to bet 4M EUR on my timeline. The ask is eight weeks and about 0.6M EUR. By week 8 we have measured numbers: rule inventory precision, the harness running, real database sizes, the real cloud bill. If they say 70% by month 12 isn't reachable, I say so at week 8, not month 11, with a new date. And migration throughput isn't the constraint: the factory handles about 1,000 customers a month against a planned peak of 650.

**Follow-up:** Platform ready in three months. Really?

Yes, because the platform isn't the hard part. AI builds the scaffolding quickly; what sets the pace is contracts and the outside security test that gate month 3. And it's off the critical path: first customers depend on the first five modules passing equivalence, and the module teams start building those in month 2, alongside the platform.

**Trap:** Overselling ('it's very achievable, trust me') or folding ('you're right, call it 18 months'); not naming the tight spots before the CTO does.

Source: Executive summary, page 2 (0.6M EUR foundation phase, gate P1); Statutory variability, page 7 (legacy fast lane builds all 310 forks from month 4); Migration plan, pages 13-14 (30 tenants of slack; 100 a night, about 1,000 a month vs 650 peak); Roadmap gates and diagram, page 20 (P2 month 3: two cells live, isolation probes and penetration test; module pods start month 2); study sheet 'Say it first' and 'Hard questions'; deck speaker notes, 'statutory' and 'roadmap' slides.

### As the forward-deployed lead with a team of about 30 and a steering committee, how much code do you actually write, and where do you draw the line?

I stay hands-on where the risk is highest and delegate the rest; roughly a third of my time in the code, more during discovery. On this program that means the equivalence harness and the money rules: I want to open a failing VAT comparison myself and explain it to the CFO in plain words. I'd review money-code pull requests, which need two reviewers anyway, and I'd own the cost model so the steering numbers are mine. I wouldn't write module features; pod leads own those. The other two-thirds is people: weekly with the CTO, the four legacy engineers, bureau champions, and the monthly steering review. My test: if I'm the bottleneck on a pull request, I'm too deep; if I can't answer a technical question in steering without phoning someone, I'm too shallow.

**Follow-up:** When would you drop everything and go fully hands-on?

A correctness or isolation incident. Any correctness incident or failed cross-tenant probe pauses all new cutovers, and I'd be in the diff myself until we know the cause. I'd make the first call to the client's CTO myself, then a named deputy sends updates every few hours, so the steering committee hears from us before they have to ask.

**Trap:** Claiming he would code full time (ignores the role) or not at all (loses the engineers' respect); having no clear rule for where the line sits.

Source: Not in documents; draws on L1 gate (two reviewers on money code), page 9; L3 equivalence, page 11; KPI dashboard and guardrails (monthly steering review; any breach pauses cutovers), pages 16-17; Tenant isolation (hourly cross-tenant probes), page 6; Team, page 21; roadmap module pods, page 20.

### If you'd had three weeks instead of three days, what would be different in this submission?

Mostly I'd turn estimates into measurements, and that list is exactly what the first eight weeks are for. First, run the rounding check on the real .NET and MySQL runtimes; today the 1-in-560 VAT mismatch comes from emulating both implementations. Second, sit with power users and time the 25 most frequent workflows, because keyboard speed decides whether accountants accept a browser. Third, I only had the public repository, no customer forks, so "forks mostly change reports, fields and integrations" is still an assumption. Fourth, a bottom-up team estimate instead of "about 30". And fifth, price the cloud against a real bill instead of list prices. I'd rather show you those gaps than paper over them.

**Follow-up:** Which of those gaps worries you most?

The forks. Both the legacy fast lane and the extension tiers depend on forks I haven't seen yet. The mitigation is quick: all 310 classified by week 6, the biggest forks handled first, and any fork that fits no tier moves to the last wave rather than holding everyone else up.

**Trap:** Saying 'nothing', or listing so many gaps it undermines the plan; or naming new features instead of missing evidence.

Source: Reference page 3 (rounding emulated; harness confirms on real runtimes in weeks 2-4); Web client speed-parity gate, page 6 (25 most frequent workflows timed with power users); Assumptions A6 and A7, page 4; Reference cloud cost inputs, page 4 (list prices, validated against a real bill in week 4); Forks, page 7 and Top risks, page 21 (all 310 classified by week 6; misfits move to W5); deck speaker notes, 'statutory' slide (biggest forks first).

### Week 4, the real cloud bill comes in 35% above your estimate. Cash payback was already year 4. The CFO asks if the business case is dead. What do you say?

It's not dead, but it becomes a different case, and I'd say that plainly. Cash payback moves from month 44 to about month 56, and five-year net cash drops from about 2.5M to about 0.6M EUR. Once everyone has moved, run cost lands right on the 406 EUR target, so the 45% cut still holds; at month 12 it would be nearer 450 EUR, so that goal lands at full scale, not month 12. That's why we check a real bill in week 4: the CFO hears it before the week-8 go or no-go, not after 4M is spent. Then I'd tune the two biggest lines, shared services and the cell databases, about 0.3M EUR a year each. Beyond cash, the case rests on risk and speed: tax changes in weeks, not months, and 310 forks gone.

**Follow-up:** Then why not just rehost the old app in the cloud and save the 4M?

Because rehosting keeps 4,200 databases and 310 forks. Cost still grows with every customer, and every release is still 4,200 upgrades. Tax changes stay at 10 to 14 weeks against a six-week legal window; even releasing more often still needs an engineer per rate change, about 4 to 6 weeks, not under three. You'd spend less this year and keep paying every year after.

**Trap:** Defending the original numbers, counting freed staff time as cash to rescue the payback, or quoting decimals instead of round figures.

Source: Business impact and sensitivity, pages 18-19 (cloud +35%: payback month 56, 'lands exactly on the 406 EUR target'); cost-model-output.txt (5-year net cash 2.48M base, 0.58M at +35%; 330 EUR per tenant at month 12, 299 at full scale); KPI dashboard, page 17 (month-12 target 406 EUR, model 330); Reference cloud cost inputs, pages 4-5 (shared 25,000 EUR a month; cell database 3,500 EUR a month x 7 cells); Trade-off analysis, page 18 and what-not-to-do (rehost keeps 4,200 databases; faster releases still 4 to 6 weeks); deck speaker notes, 'payback' slide.

