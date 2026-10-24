# POS3 handoff — account02/B11 articulation-corridor reduction

Source run: `20260922T075311Z-b11-pos3-r18-aa069b32`. Scientific report: `yspennstate/math-open-problems/proofnet24/collective-POS3/account02/B11/20260922T075311Z-b11-pos3-r18-aa069b32/REPORT.md`, creation commit `4577781a2de11deed905caa16db4e6f980d1b223`. Status: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN.

Let P be a cardinality-minimal width-at-most-three no-balanced candidate with connected incomparability graph, and let v be a cut vertex of Inc(P). If Q1,...,Qk are the incomparability components of P-v in ordinal order, then Pred(v) is contained in Q1, Succ(v) is contained in Qk, and v is incomparable with every interior Qi. The full-extension marginal on each interior Qi is exactly uniform: insertion multiplicity for v depends only on the two boundary extensions and the fixed interior sizes. Minimality therefore forces every interior Qi to be a singleton.

Hence
`P-v = Q1 ⊕ {z1} ⊕ ... ⊕ {zm} ⊕ Qk`, m=k-2,
and each zj is an incomparability leaf adjacent only to v. Put W=e(Q1)e(Qk), E=e(P), pj=Pr(v<zj). Exact full-extension counting gives
`p_{j+1}-p_j = W/E`
and `E >= (m+1)W`.
In a no-balanced candidate the strong-majority orientation is a transitive total order. If m>=2, v cannot lie between consecutive zj in that order, because then the probability jump would be >1/3 but W/E<=1/(m+1)<=1/3. Thus all zj lie on one strong-majority side of v.

Apply account02/B11 r17's incomparability-leaf terminal theorem. In the orientation v≺*z1<...<zm, the leaf z2 has `max(Pred(z2)\Pred(v))={z1}`; the terminal no-span leaf theorem requires exactly two maximal Hasse channels, so strict span descent is forced. The dual applies in the reverse orientation. Therefore, **after strict span descent is exhausted, every incomparability articulation has k<=3**: only `P-v=Q1⊕Q2` or `P-v=Q1⊕{z}⊕Q3` remains.

Applied OTHER-account result: account03/B19 `20260922T070336Z-b19-pos3-r11-same-ray-export` leaves `CROSS-ENVELOPE REUSE EXCLUSION`. The new reduction shows articulation-mediated cross-envelope reuse cannot hide in a multi-level ordinal corridor; it is confined to the two residual interfaces above, or else propagation occurs inside a 2-connected incomparability block. Lead account04/B10 r17's coherent three-antichain gate is narrowed in the same way whenever it meets an articulation.

First unpaid implication: **ONE-LEAF / TWO-BOUNDARY ARTICULATION EXIT** — exclude those two residual cut shapes in the series/parallel-indecomposable span-descent-exhausted hard core, or prove all surviving coherent/cross-envelope reuse lies in a 2-connected incomparability block.

Exact regression: verifier SHA-256 `db9c3b9cd195a2e257220755a77c0e09e5aea20b88410e98b36a8ff3459d8cad`; stdout SHA-256 `49dce621a54e1ccc1b437d0ad5f8ab82ae20ec8cc862b5979ee05737b2f0bbac`; enumerated 5,230 naturally labelled transitive closures through n=6, 3,701 width<=3, 2,236 incomparability-cut states; PASS. Finite verification is regression only, not closure.

A five-point width-two adversary with covers `(0,3),(0,4),(1,2),(1,4),(2,3)` shows a cut vertex need not itself have a balanced incident pair: E=8, N(2<0)=2 and N(2<4)=6, while balanced pairs occur elsewhere with count 3/8. Thus the residual boundary interfaces are genuine.
