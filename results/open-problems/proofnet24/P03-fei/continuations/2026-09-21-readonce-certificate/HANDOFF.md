# FEI handoff: the read-once constant is certified, and fourteen routes into the full conjecture

21 September 2026. **Full FEI remains OPEN / NOT PROVED.** What changed: the read-once subclass is settled to
within 3e-3 by a computer-assisted theorem, the general-case numerics that any new attempt should know are
recorded, and the owner has redirected the fleet to creative attempts only.

Read, in this order:

1. [TASKS_2026-09-21.md](TASKS_2026-09-21.md): the owner's instruction (seven scheduled tasks per account on FEI,
   no audits, creative out-of-the-box approaches only) and what a run should deliver.
2. [REPORT.md](REPORT.md): the theorem H <= 6.4573 I for read-once formulas over AND, OR, NOT (reduction to one
   two-variable inequality plus an interval-arithmetic certificate), the numerical identification of the sharp
   constant with Hod's beta(1/2) = 6.4547837, the fan-in-three check, and the general-case facts: the restriction
   identity Delta_i H = JS + sum m(S) h(q), the potential-free step constant (4.8677 exhaustively through n = 5,
   6.0037 on width-2 tribes, bounded on every family tried), and the potentials that buy nothing. Update of 14:2x the
   same day (section 4): the region-1 enclosure now keeps the cancellation in G(x) + G(y) - G(x+y), verifies the
   margin c = 0.003 on the M = 96 candidate in 34 minutes where the old bound could not finish; region 3 then verified
   at that margin in 48 minutes, and the same cure was carried into region 2, whose A term holds 83 per cent of its
   width (the failing fraction drops from 7.8 to 3.5 per cent and the worst bound from -8.16 to -0.28, cross-checked
   at 40 digits). Region 2 then FAILED at that margin, at the degenerate cell x = 4, v = 1.584632 with bound
   -9.949e-04, which is the candidate's own violation and not slack in the bound; so the certified constant
   stays H <= 6.4573 I and a finer certificate candidate, not a sharper enclosure, is what a smaller margin needs.
3. [APPROACHES.md](APPROACHES.md): fourteen routes, each with its first computation and what would kill it.
4. `code/` and `data/`: every script, the two certificate candidates (npz), the verification logs and summaries.
   To reproduce the theorem run `python fei_cert_vi.py` and then `python run_cert_all.py cert_vi_h24k40.npz 0.01 60
   h24_c001` (about two hours on eight cores).

Not claimed: any progress on FEI beyond the read-once class; any rigorous statement for fan-in three; the exact
value of the read-once constant (the certificate stops at 6.4573, the gap to beta(1/2) is explained in REPORT.md
section 4).
