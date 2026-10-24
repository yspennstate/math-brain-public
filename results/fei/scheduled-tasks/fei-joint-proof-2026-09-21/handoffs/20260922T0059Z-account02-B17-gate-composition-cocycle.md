# FEI gate handoff — exact composition cocycle and prime-gate reduction

Source-bound scientific report:
`yspennstate/math-open-problems` at `proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`, first report commit `d1277d4acccafbd93b9703359626e740a5a8347a`; checker/output/manifest follow in the same immutable directory.

Status: full FEI OPEN / NOT PROVED. This is a same-target structural reduction after account01/B14's genuine-Boolean refutation of AND/decomposable extremality.

For the current all-gate inequality, write the gate slack
`D_Gamma(G;p)=sum_i (It_i/V_pi)(Gamma(p_i)+h2(V_pi))-Gamma(p_out)-Ht_G`
and Poincare defect
`M(G;p)=sum_i It_i/4-p_out(1-p_out)`.
For any disjoint composition `K=F(G_1,...,G_m)`, with induced output biases `q_j` and `b_j=It_j(F;q)/V_qj`, the report proves analytically

`D_Gamma(K)=D_Gamma(F;q)+sum_j b_j D_Gamma(G_j)`

and

`M(K)=M(F;q)+sum_j b_j M(G_j)`.

Therefore, where `M>0`, the required scalar margin `c=-D/M` is an exact convex average of factor margins. In zero-denominator cases the corrected slack `D+cM` itself composes additively. Consequences:

1. decomposable gates cannot amplify the normalized margin;
2. every violating gate has a composition-prime violating Boolean factor;
3. account01/B14's 18-input obstruction forces an actual composition-prime gate (arity <=18, at an induced product bias) with margin at least `0.2681828436921863026...`;
4. the 162-input shared-core record forces a prime factor margin at least `0.2682003346344497745...` for `C0=6.4548`;
5. recursive majority, tensors and arbitrary biased disjoint compositions cannot manufacture a worse margin than a primitive component.

Same-run successor: lift the read-once potential by `Gamma_a(p)=Gamma_RO(p)+a p(1-p)`. Every gate slack increases by `aM>=0`. The current 162-bit certified balanced obstruction forces
`a>=0.2682003346344497745...`; equality raises the center cap to the current certified balanced lower bound `6.521850083658612...`. The remaining universal target is the same owner gate inequality but only on composition-prime gates. This is OPEN; a later prime obstruction can force a larger lift without refuting FEI.

Finite sanity checker: 3,136 biased small-gate compositions, 2,520 convex-margin checks and 216 balanced uniform compositions passed; finite scope only. No novelty/publication-priority claim is made; O'Donnell–Tan composition is the primary structural input.
