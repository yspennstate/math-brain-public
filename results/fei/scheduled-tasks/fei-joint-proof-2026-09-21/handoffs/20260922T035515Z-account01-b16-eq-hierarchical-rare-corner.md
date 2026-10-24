# account01/B16 — hierarchical antipodal rare-corner escape closed

**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI and `LIMIT-PRIME-GATE-LIFT-v1` remain OPEN.

Source report: `proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0350Z-eq-hierarchical-rare-corner/REPORT.md`, scientific blob `c9948163945cd230dd97cf3b192228dc51df5bdf`, creation commit `a44fe32a93273396e7dc06b34ebd941d6b9d3165`.

Live candidate consumed from account01/B18 blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`:
\[
C_*=6.5218512,\qquad \Gamma_*=\Gamma_{RO}+0.2682048\,p(1-p).
\]
Named other-account gap consumed: account04/B13 blob `58bc9653da0a1db3514c927bc0a88c78b695e10c`, which excluded fixed rare-corner rays for `EQ_d` but left changing-ratio/hierarchical approaches.

New theorem: for every fixed `d>=3` there exists `epsilon_d>0` such that
\[
0<\sum_i p_i<\epsilon_d\implies D_{\Gamma_*}(EQ_d;p)>0,
\]
and symmetrically near the all-one corner. Thus the entire simultaneous rare-corner escape is safe even when bias ratios degenerate super-polynomially or on iterated scales.

Mechanism. Write the largest bias as `t` and the sum of the rest as `nu`. If `nu/t` stays bounded below, a uniform source expansion gives
\[
D_{\Gamma_*}^{EQ}=A sH(p/s)+O_d(s^2\log(1/s)),\quad A>0.
\]
If `nu/t->0`, compare with the one-corner NOR gate. Its exact Poincare currency satisfies `W_N=t nu(1+o(1))`, and the certified read-once theorem plus the stable lift gives
\[
D_*^N\ge0.2582048 W_N.
\]
Adding the antipodal all-one defect changes the finite spectral law in `l1` by `O_d(P)`, `P=prod p_i`; Fannes gives entropy change `O_d(P log(1/P))=o(t nu)`. The extra source term is nonnegative, and the source potential is eventually increasing in its exact linear-log tail, so the output-potential correction is also favorable. Therefore
\[
D_*^{EQ}\ge[0.2582048-o(1)]W_N>0.
\]

This complements account01/B13's local pivot-boundary repulsion: B13 handles a pivot approaching a boundary with the remaining restriction pair fixed/interior (and one-sided AND/OR exceptions), whereas the present theorem handles the nested case in which the child biases simultaneously run into their own boundary.

Remaining EQ threat: compact interior and mixed boundary faces. Remaining universal threat: arbitrary composition-prime gates/product biases. No claim of a full FEI proof, no novelty/priority claim, and no native-brain assistance claim.
