# Apskaita5 codebase facts (for the case study and the panel)

Read from this repository at commit `2320f1c`. Paths are relative to `Source/`.
Counts come from `find`, `grep` and `wc`.

## Size and stack

| Project | .vb files | Lines | Notes |
| --- | --- | --- | --- |
| `Apskaita5/Apskaita5` (ApskaitaObjects) | 537 | 304,727 | Business objects; about 82K lines are generated (resources, SAF-T, camt/pain XSD classes) |
| `Apskaita5/AccDataBindingsWinForms` | 332 | 147,860 | 129 forms; 101,658 lines are designer code |
| `Apskaita5/AccControlsWinForms` | 82 | 32,624 | Custom controls, report printing |
| `AccDataAccessLayer/AccDataAccessLayer` | 68 | 16,625 | Named-SQL dictionary, transactions, schema compare and fix |
| `Apskaita5/Apskaita3/Apskaita` (exe) | 34 | 11,939 | MDI shell, 68 RDLC reports, 24 FFData and 24 MXFD templates |
| Remoting server, web service, plugin manager, plugin interface | 22 | about 1,100 | CSLA data portal over Remoting or ASMX; small REST endpoint for invoices |

- .NET Framework 2.0 (business, data and server layers) and 3.5 (client); CSLA 2.1.4; MySql.Data 6.7.8; ReportViewer 8.0; ObjectListView 2.9. No NuGet.
- No test project and no test framework anywhere.

## Business layer

- CSLA classes: 128 BusinessBase, 102 ReadOnlyBase, 74 ReadOnlyListBase, 63 BusinessListBase, 10 CommandBase (377 in total).
- 425 data-portal methods, 797 `ValidationRules.AddRule` registrations, 328 custom rule methods, 343 `IsInRole` checks, 117 roles.
- Field attributes that carry validation and rounding metadata: `DoubleField` 1,133, `StringField` 238, `AccountField` 82, `IntegerField` 62.
- Global company context `GetCurrentCompany()` (`Apskaita5/Apskaita5/Utilities.vb:40`) is used 321 times in 74 files.

## Data

- Schema in `Apskaita5/Apskaita5/DbStructure/DatabaseStructureGauge.xml`: 67 tables, 829 columns, 228 DOUBLE money columns, no DECIMAL, no foreign keys, 36 indexes, no tenant column.
- One MySQL database (or SQLite file) per company, plus a separate security database for users and roles.
- No schema version table. The user upgrades by hand with "check and fix", a diff of the XML schema against the live database (`AccDataAccessLayer/AccDataAccessLayer/DatabaseAccess/DatabaseStructure/DatabaseStructureErrorList.vb`).
- SQL lives in `AccDataAccessLayer/AccDataAccessLayer/SqlDepositories/*.sqld`: 770 MySQL and 761 SQLite statements, 24 keys differ between them. Code uses 672 distinct keys and one raw SQL call.

## Money and rounding

- 3,295 `As Double` against 199 `As Decimal` (all Decimals are in generated XSD classes).
- `CRound` (half up) is called 3,876 times in 219 files. Five implementations exist: three VB copies, a SQLite function, and a MySQL stored function.
- The VB and MySQL versions disagree on 6.6% of exact half-cent values and on about 1 in 560 random 21% VAT amounts. See `rounding_check.py`.

## Statutory

- 28 declaration classes in `Apskaita5/Apskaita5/ActiveReports/Declarations/`, 13 form families, one class per version (SAM has seven), with hardcoded `ValidFrom` and `ValidTo`.
- The declaration list is hardcoded in the forms layer (`Apskaita5/AccDataBindingsWinForms/CommonMethods.vb:577-621`).
- FFData templates are filled by table and row position, for example `formDataSet.Tables(8).Rows(i-1).Item(1)`.
- 20 hardcoded year comparisons, including the 2019 social-insurance gross-up `* 1.289` (`ActiveReports/WageVDUInfo.vb:151`).
- Tax rates (VAT, Sodra, PSD, income tax) are typed in per company and copied onto each wage sheet. The non-taxable income formula is a per-company editable string (`General/CompanyObjects/Company.vb:49`).
- Electronic outputs: FFData (ABBYY e-form) files, i.SAF 1.2 XML and SAF-T 2.0/2.01 XML.

## UI and reports

- 156 forms, 114 ObjectListView grids with 1,846 columns, 13 DataGridViews (mostly admin forms).
- Keyboard: Insert or numpad + adds a grid row, Delete or numpad − removes one; Enter and Tab move across cells and rows; pickers filter as you type; Ctrl+Insert adds a list item; dates accept shorthand ("5", "-5", "+5", yyMMdd). Almost no menu shortcuts (only F1).
- Lithuanian only, hardcoded: 3,657 `.Text = "..."` literals in designer files.
- 68 RDLC reports (RDL 2005) bound to a generic data set with 345 positional `ColumnN` fields; 17 reports referenced in code are missing from the repository.
- Bank formats: ISO 20022 camt.052 and camt.053, LITAS-ESIS, custom tab-delimited; payments export as pain.001.

## Security notes

- Plaintext database password in `Apskaita5/AccWebService/Web.config:58` and in the shipped `Bin/Apskaita5Web.zip`.
- MD5 is still an allowed password hash option.
