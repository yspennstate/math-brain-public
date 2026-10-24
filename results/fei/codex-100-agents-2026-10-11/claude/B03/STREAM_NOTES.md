# B03 stream notes (Claude lead) - v2, 2026-10-11 23:2xZ

Read at the start of every stage. Full FEI is OPEN. Units: bits; f is +-1; p(S)=fhat(S)^2.

## Established this stage (lead run 20261011T223500Z-claude-B03-pp-congestion, review pending A086/A094)
- Theorem R: C003's 7 log k has three sources, kept exact: (L) log k * E|F(A)| labels; (S) (6/5) E sum_l
  s_l log(kappa_l/s_l) subset choice; (R) sum_j Inf_j E_{nu_j} G_j rank+rarity. C003 = R + |F|<=|A| + logsum + Gmean.
- PP_q (OR over lines of PG(2,q) of AND(line), read q+1 in EVERY DNF): d_j g = S + r, S = sum of the q+1 line
  pieces with DISJOINT Fourier supports (only the empty set overlaps), ||r||^2 <= 2q(q+1)^2 4^{-q}. So the k-fold
  Cauchy-Schwarz loss of union:Gtail disappears; (L),(S),(R) are all O(I); H(PP_q) <= C(q) I for q >= 10 with
  C(q) -> 26.95 (C(12)=32.4) against 41+7log2(q+1). sup_q H/I < 66.1.
- Exact q=2,3,4: H/I = 2.483, 3.198, 3.710. Small q is NOT the asymptotic regime (||r||^2 > Inf_j, most mass off
  the lines, realised CS loss ~ k). Never quote small-q data as a test of the large-q theorem.
- A012 activation ledger re-derived and machine-checked (1,536 assertions).

## Not to repeat / refuted
- Rarity or small I alone is not a simplification (C013). Distinct-label subcube covers are C011 baseline.
- H(fg) <= H(f)+H(g) with shared variables is false (C030). Selector identities need disjoint leaf supports (C029).
- A read-once local claim cannot absorb a repeated selector x (A012: M = OR(AND(x,y),AND(-x,z))).
- Do not re-prove the K_eff multiplier estimate; equal piece masses (PP_q) make K_eff = k useless - use supports.
- Do not redo PP_q. A constant below 6.278 for read-once AND/OR would contradict Hod's lexicographic functions.

## Targets (one each, next stage)
- A014: Lemma I for an ARBITRARY union: d_j f = sum_l u_l + r with cross term sum_{l!=l'} <P_E u_l, P_E u_l'>.
  Prove an absolute constant for read-k unions of ANDs on linear hypergraphs (two gates share <= 1 variable),
  then for gate intersections of size <= t with cost O(t). State the first unproved line.
- A015: label term for majority, tribes T_{w,s}, rare activated core: E|F| log k of the DNF witness vs I exactly;
  then the same with threshold (regular) gates. This is where the universal bridge fails today.
- A011: a class with REPEATED variables where I_sel >= gamma D is proved, or the posterior-erased code on the comb.
- A012: posterior-erased witness cost for control-first activation, exact small r, analytic all r.
- A013: show (L),(S),(R) do not increase under restriction, using Theorem R's exact functionals.

## Universal bridge (CONDITIONAL)
Every f is a union of ANDs (its DNF). FEI follows if every f has a gate cover with (L)+(S)+(R) <= C I.
First unsupported line: existence of that cover. False for DNF of majority (labels); open for regular gates (C020).
