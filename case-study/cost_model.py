"""Month-by-month cost and savings model behind the case study's business case.

All inputs are assumptions stated in the case study (A2, A3, A6, A12) and are
meant to be re-baselined in week 4 with the firm's real figures.

Run:  python3 cost_model.py
"""
import math

# ---- Baseline (A2, A12) -------------------------------------------------
TENANTS = 4200
LEGACY_INFRA_EUR_YEAR = 3.1e6        # brief
LEGACY_FIXED_SHARE = 0.20            # part of legacy cost that does not fall per tenant
TICKETS_PER_MONTH = 6500             # brief
TICKET_COST_EUR = 12                 # A12
TICKET_REDUCTION = 0.40              # migrated tenants raise 40% fewer tickets

# ---- Migration plan: new tenants live per programme month ---------------
NEW_PER_MONTH = {5: 10, 6: 70, 7: 240, 8: 400, 9: 450, 10: 550, 11: 600,
                 12: 650, 13: 300, 14: 150, 15: 0, 16: 100, 17: 350, 18: 330}
ARCHIVE_LAG_MONTHS = 2               # legacy DB removed from hosting after G4
LEGACY_SWITCH_OFF_MONTH = 20           # last cutovers in month 18, archived by month 20

# ---- Cloud run cost (bottom-up, A1/A3) ---------------------------------
SHARED_EUR_MONTH = 25_000            # edge, identity, observability, control plane, non-prod
CELL_EUR_MONTH = 6_300               # PostgreSQL HA + replica, app containers, storage
TENANTS_PER_CELL = 600
DEDICATED_SHARE = 0.03               # largest tenants on their own database
DEDICATED_EUR_MONTH = 150
AI_EUR_TENANT_MONTH = 4.0            # extraction, assistant, NL reporting inference

# ---- Investment (A6) ----------------------------------------------------
FTE_EUR_MONTH = 7_300                # blended delivery rate
TEAM_Y1, TEAM_Y2_H1 = 32, 10
TOOLING_EUR = 250_000
CONTINGENCY_Y1 = 0.15

# ---- Freed engineering capacity (not cash) -------------------------------
ENGINEERS, ENGINEER_EUR_YEAR = 30, 60_000
MAINT_FROM, MAINT_TO = 0.62, 0.30    # reached linearly over months 13-24


def run(cloud_mult=1.0, slip=0, team_mult=1.0, months=60):
    new = {m + slip: v for m, v in NEW_PER_MONTH.items()}
    cum, c = {}, 0
    for m in range(1, months + 30):
        c += new.get(m, 0)
        cum[m] = c

    legacy_fixed = LEGACY_INFRA_EUR_YEAR * LEGACY_FIXED_SHARE / 12
    legacy_var = LEGACY_INFRA_EUR_YEAR * (1 - LEGACY_FIXED_SHARE) / TENANTS / 12
    ticket_save = TICKETS_PER_MONTH / TENANTS * TICKET_REDUCTION * TICKET_COST_EUR

    def cloud(m):
        t = cum[m]
        if m < 3:
            return 0.0
        cost = SHARED_EUR_MONTH
        if m >= 4:
            cost += max(1, math.ceil(t / TENANTS_PER_CELL)) * CELL_EUR_MONTH
        cost += DEDICATED_SHARE * t * DEDICATED_EUR_MONTH + AI_EUR_TENANT_MONTH * t
        return cost * cloud_mult

    def legacy(m):
        if m > LEGACY_SWITCH_OFF_MONTH + slip:
            return 0.0
        hosted = TENANTS - cum.get(m - ARCHIVE_LAG_MONTHS, 0)
        return legacy_fixed + hosted * legacy_var

    def support(m):
        return cum.get(m - 2, 0) * ticket_save

    def programme(m):
        if m <= 12:
            return (TEAM_Y1 * FTE_EUR_MONTH * team_mult + TOOLING_EUR / 12) * (1 + CONTINGENCY_Y1)
        if m <= 18 + slip:
            return TEAM_Y2_H1 * FTE_EUR_MONTH * team_mult
        return 0.0

    def capacity(m):
        if m <= 12:
            return 0.0
        share = MAINT_FROM - (MAINT_FROM - MAINT_TO) * min(1, (m - 12) / 12)
        return (MAINT_FROM - share) * ENGINEERS * ENGINEER_EUR_YEAR / 12

    rows, cash, alls = [], 0.0, 0.0
    payback_cash = payback_all = None
    for m in range(1, months + 1):
        net = LEGACY_INFRA_EUR_YEAR / 12 - (cloud(m) + legacy(m)) + support(m) - programme(m)
        cash += net
        alls += net + capacity(m)
        if payback_cash is None and m > 12 and cash >= 0:
            payback_cash = m
        if payback_all is None and m > 12 and alls >= 0:
            payback_all = m
        rows.append(dict(month=m, tenants=cum[m], cloud=cloud(m), legacy=legacy(m),
                         support=support(m), programme=programme(m),
                         capacity=capacity(m), cum_cash=cash, cum_all=alls))
    return rows, payback_cash, payback_all


def yearly(rows):
    out = []
    for y in range(1, len(rows) // 12 + 1):
        ms = rows[12 * (y - 1):12 * y]
        s = lambda k: sum(r[k] for r in ms) / 1e6
        infra_saving = LEGACY_INFRA_EUR_YEAR / 1e6 - s('cloud') - s('legacy')
        net = infra_saving + s('support') - s('programme')
        out.append((y, s('cloud'), s('legacy'), infra_saving, s('support'), s('programme'), net, s('capacity')))
    return out


if __name__ == '__main__':
    rows, pc, pa = run()
    print('Year  cloud  legacy  infra_saving  support  programme  net_cash  capacity (M EUR)')
    for y in yearly(rows):
        print('%d    %5.2f  %6.2f  %12.2f  %7.2f  %9.2f  %8.2f  %8.2f' % y)
    print('Payback month: cash %s, including freed capacity %s' % (pc, pa))
    for m in (6, 9, 12, 18, 30):
        r = rows[m - 1]
        per = r['cloud'] * 12 / r['tenants'] if r['tenants'] else float('nan')
        print('Month %2d: %4d tenants in cloud, cloud run cost per tenant %5.0f EUR/yr' % (m, r['tenants'], per))
    print('\nSensitivity (payback cash month, 5-year net cash M EUR):')
    for label, kw in [('base', {}), ('cloud +35%', dict(cloud_mult=1.35)),
                      ('waves slip 3 months', dict(slip=3)), ('team cost +25%', dict(team_mult=1.25))]:
        r, p, _ = run(**kw)
        print('  %-20s month %s, %.2f' % (label, p, r[-1]['cum_cash'] / 1e6))
