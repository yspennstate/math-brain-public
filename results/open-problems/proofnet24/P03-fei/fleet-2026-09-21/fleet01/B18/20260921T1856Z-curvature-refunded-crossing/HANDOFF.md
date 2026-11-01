# B18 handoff — curvature-refunded physical crossing

Status: **PARTIAL; full FEI remains OPEN / NOT PROVED.** Execution: `WITHOUT_VERIFIED_BRAIN`.

Use the complete proof in `REPORT.md`. The new object is

\[
\mathcal P(f)=\sum_i \mathfrak j(\min(\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f))),
\qquad
\mathcal F=H-\mathcal P,
\]

with

\[
\mathfrak j(p)=1-h_2\!\left(\frac12+\sqrt{p(1-p)}\right).
\]

The scalar reflected-tangent lemma is

\[
\mathfrak j(p)-E\mathfrak j(U)
\ge \mathfrak j'(p)E(2U-1)_+,
\qquad EU=p\le\frac12.
\]

Consequently, after median-centering and physically restricting a block `A`,

\[
\Delta_A(H-\mathcal P)
\le H(X_A\mid X_{A^c})
-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
\]

where `c_j(A)=E(2 Inf_j(f_{A=z})-1)_+` is the B14 posterior-threshold crossing.

Choose a physical descendant maximizing

\[
\rho={H-\mathcal P\over J},
\qquad J=\sum_i\min(p_i,1-p_i).
\]

In its centered gauge, for every block `A`,

\[
\boxed{
H(X_A\mid X_{A^c})
\ge \rho I_A+
\sum_{j\notin A}(\rho+\mathfrak j'(p_j))c_j(A).
}
\]

Thus

\[
\boxed{
\sum_{j\notin A}(\rho+\mathfrak j'(p_j))c_j(A)
\le\sum_{i\in A}[h_2(p_i)-\rho p_i].
}
\]

If `sigma(rho)` solves `h_2(sigma)/sigma=rho`, then `p_i<=sigma(rho)` and the crossing coefficient is at least

\[
\rho+\kappa(\rho),\qquad \kappa(\rho)=\mathfrak j'(\sigma(\rho))>0.
\]

Fixed-cardinality averaging preserves this nonmodular credit:

\[
E_{|B|=q}\sum_{j\in B}(\rho+\mathfrak j'(p_j))c_j(B^c)
\le(1-q/n)\mathcal P-A_q.
\]

At `q=n-1`,

\[
\boxed{
\sum_i\sum_{j\ne i}(\rho+\mathfrak j'(p_j))c_j(\{i\})
\le \mathcal P-\operatorname{DTC}(X)
\le {2\over\ln2}I.
}
\]

This is the main reusable advance: a high corrected-ratio core has a **dimension-free total budget for all one-bit-induced posterior majority crossings**, and unlike modular tangent centering this term survives fixed-cardinality averaging.

Calibration only: at the inherited unrestricted scale `C0=6.521845710923046575`, the corrected target is `rho0=C0-2/ln2≈3.636455629145120`; then `sigma≈0.196692512551412`, `kappa≈2.388515187682460`, and the effective crossing coefficient is `rho0+kappa≈6.024970816827580`.

Next target: combine the global crossing budget with the fresh transverse/near-subcube derivative-support geometry. Either (i) prove every non-affine corrected critical core produces a dimension-free amount of crossing, exhausting `P-DTC`, or (ii) prove the crossing-poor regime admits a physical restriction/block with corrected ratio below `rho`. Do not treat the calibration as a proof of a 6.025 universal bound.
