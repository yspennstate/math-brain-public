# P0347 (Aldous-Janson OP10, balance indices of DTCS(n)) - independent check of the Codex draft report

Final report (39,655 bytes, run ended ~23:3x Mac time) re-read: same claims as the draft, plus a C++ Monte Carlo
(n=10^5: Sackin mean 5.01-5.03e6 against 5.02e6 from the proved expansion, within ~1.5 s.e.; skewness 0.78-0.81).
Verdict: the proved statements check out on every number I could test. Full Sackin/Colless limit law stays open (§9).

Checked 12 Nov 2026 ~23:30 Mac time (21:30 laptop) by an agent against the draft REPORT.md (11,540 bytes) while the run
(mini1 ~/agent_run/P0347, pid 21945) was still in its Monte Carlo stage. Final report to be re-read.

Own code, written separately: indep_moments.py (float64, law of total variance), fit.py, consts.py (Fractions + mpmath), third.py.

1. Means and variances at n=4000 agree with the Codex 45-digit values to every printed digit
   (ES 113146.538835208, EC 82980.6524601348, EQC 99729322.178039; VarS 191887490.9587, VarC 209966508.8575, VarQC 2.3427186e15).
2. Mean expansions (1): the O(n) remainder (ES - nL^2/2z - b nL)/n is flat at 0.7772, 0.7795, 0.7808, 0.7815 (n=500..4000);
   Colless with b - 2log2/z: 0.226..0.230. Consistent with O(n).
3. Limits from the exact recursion to n=16000, fitted in powers of 1/log n (deg 1-3; lever arm L = 6.9..9.7 only, so
   corroboration, not proof): VarS/(n^2L^2) c0 = 0.272-0.288, VarC 0.271-0.286 (claim kappa = 0.28057);
   VarQC/(n^4L^2) 0.180-0.185 (claim 2/11 = 0.18182); EQC/(n^2L) 0.994-1.013 (claim 1).
4. Third central moment recursed to n=12000: u3/(n^3L^3) c0 = 0.102-0.111 (S), 0.103-0.111 (C), claim a3 = 0.10760;
   finite-n skewness at n=12000 already 0.794 (S), 0.767 (C), extrapolations 0.70-0.76, claim 0.7240. Non-normality is
   visible at finite n.
5. Rational constants recomputed from recurrence (24): m = 1, 1, 13/11, 2457/1507, 5188313/2005817 (match);
   QC skew 1.0955715643, kurtosis 4.7182843699 (match).
6. Integrals by quadrature (30 digits): J2 = 2zeta(3) - zeta(2) and J3 = 6zeta(4) - 3zeta(3) - 1.5zeta(2) agree to 29-30 digits;
   kappa, a3, a4, skew 0.7240346817, kurt 3.9126659234 match every printed digit.
7. Exact tolls rechecked by hand: E(m-2I)^2 = m^2 - 2m(m-1)/h_{m-1}; pathwise QC_n = sum |v|^2 - 2n(n-1).
8. Literature (12 Nov): Kolesnik 2404.16021 (leaf-height CLT via contraction), Chorbadzhiyska-Minchev-Savov 2608.18320
   (fragmentations; continuous length, heights), Heng Ma 2609.14329 (height): full texts contain no Sackin, Colless,
   path length or balance index. BCM 2505.24821 and INY 2510.17343 checked by Codex: neither treats them.

Proof sections 4-8 read once: transfer lemma by sub/super-solutions with Kn and n - sqrt n, moment recursions with
uniform-error arguments, moment determinacy via m_k <= k!. No gap found on one reading; a second careful reading of
§6 (the error bookkeeping in the cubic/quartic tolls) is owed before a paper.
Open, as the report itself says: a limit law for Sackin/Colless (only moments 2-4 and non-normality proved).
