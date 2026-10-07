# ERP modernization case study: supporting material

This folder holds the working material behind the case study
"Apskaita5 ERP Modernization" (Persistent FDE case study, Assignment 1).
The case study itself is written as a Claude Doc and exported to PDF.

| File | What it is |
| --- | --- |
| `Apskaita5-ERP-Modernization-Case-Study.pdf` | The case study, exported to PDF (A4, 21 pages) |
| `Apskaita5-ERP-Modernization-Reference.pdf` | Reference tab: code evidence, full stack, cost inputs, KPI trajectory, glossary (7 pages) |
| `One-Pager-Plain-English.pdf` | One-page explanation for a non-technical reader |
| `One-Pager-What-Not-To-Do.pdf` | One page on rejected paths and the traps caught in review |
| `Panel-Study-Sheet.pdf` | One-page study sheet for the panel: pitch, key numbers, tight spots, hard questions |
| `codebase-facts.md` | Facts read from this repository (sizes, stack, schema, rules, statutory code, UI, security), with file paths, for the panel discussion |
| `cost_model.py` | Month-by-month cost and savings model behind the business case, with sensitivity cases |
| `rounding_check.py` | Emulation showing the VB.NET and MySQL rounding functions disagree on half-cent values |

Run the scripts with Python 3 and no extra packages:

```
python3 cost_model.py
python3 rounding_check.py
```

Every number in the case study's business impact section, KPI targets and
charts comes from `cost_model.py`. Change an input there, rerun it, and update
the document from its output.
