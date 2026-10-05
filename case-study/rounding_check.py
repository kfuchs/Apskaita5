"""Emulates the two legacy rounding implementations and counts disagreements.

VB.NET  (Source/Apskaita5/AccCommon/CommonMethods.vb, CRound):
    i = Floor(d * 10^r); if i + 0.5 > CType(d * 10^r, Decimal) -> i / 10^r else (i + 1) / 10^r
    The Double -> Decimal conversion keeps 15 significant digits, which hides
    binary representation error (267.49999999999997 becomes 267.5).

MySQL   (DbStructure/DatabaseStructureGauge.xml, stored function CROUND):
    s = FLOOR(d * POW(10, r)); if s + 0.5 > d * POW(10, r) -> s / 10^r else (s + 1) / 10^r
    The comparison stays in DOUBLE, so the representation error decides.

This is an emulation in Python; the L3 harness confirms it on the real runtimes.
Run:  python3 rounding_check.py
"""
import math
import random
from decimal import Decimal


def vb_cround(d, r=2):
    p = math.pow(10, r)
    x = d * p
    i = math.floor(x)
    as_decimal = Decimal('%.15g' % x)          # .NET Double -> Decimal semantics
    return i / p if Decimal(i) + Decimal('0.5') > as_decimal else (i + 1) / p


def mysql_cround(d, r=2):
    p = math.pow(10, r)
    x = d * p
    s = math.floor(x)
    return s / p if s + 0.5 > x else (s + 1) / p


if __name__ == '__main__':
    for v in (1.005, 0.285, 2.675, 10.235):
        print('%-7s VB %-5s MySQL %-5s' % (v, vb_cround(v), mysql_cround(v)))

    n = diff = 0
    for cents in range(1_000_000):                # every half-cent 0.005 .. 9,999.995
        v = (cents + 0.5) / 100
        n += 1
        diff += vb_cround(v) != mysql_cround(v)
    print('Half-cent values: %d of %d disagree (%.1f%%)' % (diff, n, 100 * diff / n))

    random.seed(1)
    trials, d2 = 200_000, 0
    for _ in range(trials):
        vat = round(random.uniform(1, 5000), 2) * 0.21
        d2 += vb_cround(vat) != mysql_cround(vat)
    print('Random 21%% VAT amounts: %d of %d disagree (1 in %d)' % (d2, trials, trials // max(d2, 1)))
