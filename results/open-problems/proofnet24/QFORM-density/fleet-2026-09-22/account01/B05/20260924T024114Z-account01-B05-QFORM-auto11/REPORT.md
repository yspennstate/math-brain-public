SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B05, 2026-09-24T02:41:14Z.
attacking: QFORM-WITT-SHARED-MULTIPLIER-ENDPOINT-v1 by reducing it to one product-preserving Borel tube estimate before any fiber maximum, and testing the first tempting generic-joint replacement.

# account01/B05 — shared-shear Borel reduction and exact missing factor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bound preserving arbitrary product densities.  
**Status:** `NEW_CONDITIONAL_END_TO_END_REDUCTION / GENERIC_JOINT_TUBE_REFUTED / PARTNER_RESULT_APPLIED / FULL_QFORM_OPEN`.  
**Regularity:** essential boundedness only on the paid endpoint below; full-target continuity remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh state and the first unpaid implication

Fresh control was read from `math-research-brain` main. OWNER CONTROL is revision `2026-09-22.15`; all eighty slots remain QFORM-only, and the continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` remains active. The live correction inbox was reread. In particular, this report does **not** replace independence by a conditional density cap, does not use an arbitrary-joint 3D coarea inequality, and does not discard a small coefficient as a small random error.

The preceding B05 run put the exact-rank-three high-leverage zero-pivot survivor into the physical Witt form

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,                 \tag{1.1}
\]

where

- `H` is one literal original coordinate and is genuinely independent of the residual product bank;
- `(U,V,W)` are three orthonormal projections of that residual product bank, and are **not** asserted independent;
- `a\ne0`, `delta\ne0`;
- in the near-coloop chamber, `0<=kappa<1/sqrt(7)`;
- the aggregate determinant star is exactly

\[
S_i=a^2|\delta|=c\Delta_3.                                          \tag{1.2}
\]

At target normalization, the high-leverage branch has `S_i>=1/2`.

The exact endpoint `kappa=0` is already paid. The unpaid operation is to retain the same residual product bank while paying the shared term `2a kappa U V` **before** a fiber supremum or conditional-density replacement.

This run gives a compact conditional end-to-end implication: one explicit Borel tube estimate, stated below, would close the whole near-coloop Witt endpoint with the correct scale `(a^2|delta|)^(-1/3)`. It also proves that the same tube estimate is false for arbitrary joint density-one triples, so the missing factor is precisely the orthogonal-product-projection provenance.

## 2. Exact square completion and shell geometry

Complete the transverse square without rotating random coordinates. Put

\[
Z=W+\frac{\gamma}{\delta}V,\qquad
A=\alpha-\frac{\gamma^2}{\delta}.                                  \tag{2.1}
\]

Then the determinant-one shear `(V,W)->(V,Z)` gives

\[
\boxed{
Q=2aVH+2a\kappa UV+A V^2+\delta Z^2.
}                                                                    \tag{2.2}
\]

Fix an output centre `t`. For `v\ne0` define

\[
\Psi_t(u,v,z)
 =\kappa u+\frac{A}{2a}v+\frac{\delta z^2-t}{2av}.                  \tag{2.3}
\]

The exact identity is

\[
\boxed{Q-t=2aV\,[H+\Psi_t(U,V,Z)].}                                \tag{2.4}
\]

For `r>0`, let `nu_{r,t}` be the subprobability law of `Psi_t(U,V,Z)` restricted to the shell

\[
r\le |V|\le2r.                                                     \tag{2.5}
\]

If an interval `I` of length `h` is centred at `t`, then on this shell

\[
Q\in I\quad\Longrightarrow\quad
|H+\Psi_t|\le \frac{h}{4|a|r}.                                    \tag{2.6}
\]

No approximation is present in (2.1)--(2.6).

## 3. A Borel-profile-to-density compiler

### Lemma 3.1 — `QFORM-WITT-BOREL-PROFILE-COMPILER-v1`

Assume `H` is independent of the residual bank and has density cap `m`. Suppose there is an absolute `K_T` such that, for every `r>0`, `t in R` and every Borel set `E` of finite Lebesgue measure,

\[
\boxed{
\nu_{r,t}(E)
\le K_T\sqrt{\frac{|a|}{|\delta|}}\,r^{3/2}|E|^{1/2}.
}                                                                    \tag{3.1}
\]

Then the law of (2.2) has an essentially bounded density and

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le C(K_T)m^{2/3}(a^2|\delta|)^{-1/3},
\qquad
C(K_T)=3\,2^{-5/3}[K_T(1+\sqrt2)]^{2/3}.
}                                                                    \tag{3.2}
\]

#### Proof

First use the following elementary convolution fact. If a finite Borel measure `nu` satisfies

\[
\nu(E)\le B|E|^{1/2}\quad\hbox{for all Borel }E,                   \tag{3.3}
\]

and `f` is a probability density with `0<=f<=m`, then `f*nu` has essential supremum at most `B sqrt(m)`. Indeed, layer cake gives

\[
(f*\nu)(x)
=\int_0^m \nu\{z:f(x-z)>s\}\,ds
\le B\int_0^m |\{f>s\}|^{1/2}ds
\le B\sqrt{m\int_0^m|\{f>s\}|ds}
=B\sqrt m.                                                         \tag{3.4}
\]

Apply this to the shell measure `nu_{r,t}` and the genuinely independent density of `H`. By (2.6), (3.1) and (3.4),

\[
\Pr\{Q\in I,\ r\le|V|\le2r\}
\le \frac{K_T}{2}\sqrt m\,|a\delta|^{-1/2}\,h\sqrt r.            \tag{3.5}
\]

Fix `R>0` and sum (3.5) on the dyadic shells

\[
2^{-k-1}R\le|V|\le2^{-k}R,\qquad k\ge0.
\]

Since `sum_{k>=0} sqrt(2^{-k-1})=1+sqrt(2)`, the contribution of `|V|<=R` is at most

\[
\frac{K_T}{2}(1+\sqrt2)\sqrt m\,|a\delta|^{-1/2}\,h\sqrt R.       \tag{3.6}
\]

On `|V|>R`, condition on the entire residual bank. The map in the literal original coordinate `H` has slope `2aV`, hence

\[
\Pr\{Q\in I,\ |V|>R\}
\le \frac{mh}{2|a|R}.                                               \tag{3.7}
\]

Optimising `A sqrt(R)+B/R` with

\[
A=\frac{K_T}{2}(1+\sqrt2)\sqrt m\,|a\delta|^{-1/2},
\qquad
B=\frac{m}{2|a|}
\]

gives `R^{3/2}=2B/A` and minimum `3*2^{-2/3}A^{2/3}B^{1/3}`. This is exactly (3.2). The interval estimate is uniform in `I`, so it gives absolute continuity and the stated essential density bound. QED.

### Consequence

The entire near-coloop Witt endpoint is therefore reduced to proving (3.1) with an absolute `K_T`, uniformly for

\[
0\le\kappa<1/\sqrt7,                                               \tag{3.8}
\]

for `(U,V,W)` arising as an orthonormal projection of the **same original-coordinate product law**. By (1.2), a universal `K_T` would immediately give a universal target bound in this branch.

This is more precise than saying that a generic coarea estimate is missing: the exact missing gain is the factor

\[
\boxed{r^{1/2}|E|^{1/2}}                                           \tag{3.9}
\]

beyond the trivial shell mass `O(r)`.

## 4. Designated account02/B05 result applied at an actual inequality

At `kappa=0`, `nu_{r,t}` depends only on `(V,Z)`. Because `(V,W)` is a two-dimensional orthogonal projection of a cap-one product law, its joint density is at most `2`; the shear `(V,W)->(V,Z)` has determinant one and preserves that cap.

Scale

\[
z'=\sqrt{|\delta/a|}\,z.
\]

Then the partner theorem account02/B05 `QFORM-AFFINE-SHEAR-BOREL-TUBE-v1` applies exactly to the map in (2.3), with joint cap

\[
M_2\le2\sqrt{|a/\delta|}.
\]

Its constant

\[
K_0=\frac83(4-\sqrt2)=6.895430500338\ldots
\]

gives the actual shell inequality

\[
\boxed{
\nu_{r,t}(E)
\le 2K_0\sqrt{|a/\delta|}\,r^{3/2}|E|^{1/2}
\qquad(\kappa=0).
}                                                                    \tag{4.1}
\]

Thus Lemma 3.1 applies with `K_T=2K_0`. Keeping the sharp large-`|V|` factor `1/(2|a|R)` in (3.7) gives the slightly sharpened endpoint constant

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le 9.779484731488\,(a^2|\delta|)^{-1/3}
\qquad(\kappa=0,m\le1).
}                                                                    \tag{4.2}
\]

At target normalization `a^2|delta|=S_i>=1/2`,

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<12.322.}                     \tag{4.3}
\]

This is an equation-level use of the designated partner theorem, not a citation-only use. It also confirms that the correct shell exponent in (3.1) reproduces the determinant-star scale exactly.

## 5. New obstruction: the shared-shear tube is false for arbitrary joint density-one triples

The first tempting implication after (3.1) is to forget product provenance and try to prove the same Borel profile from a three-dimensional density cap. That implication is false in the strongest possible way.

### Proposition 5.1 — `QFORM-WITT-GENERIC-JOINT-TUBE-FALSE-v1`

Fix any `kappa>0`, any shell radius `r>0`, and any proposed constant `C<infinity`. There is a probability density `rho<=1` on `(U,V,W) in R^3` such that, with

\[
F(U,V,W)=\kappa U+\frac{W^2}{2V},                                  \tag{5.1}
\]

one has `r<=V<=2r` almost surely and, for some interval `E` of arbitrarily small length `epsilon`,

\[
\Pr\{F\in E\}=1.                                                    \tag{5.2}
\]

Consequently no universal estimate

\[
\Pr\{r\le|V|\le2r,\ F\in E\}
\le C r^{3/2}|E|^{1/2}                                             \tag{5.3}
\]

can follow from a joint density cap alone.

#### Proof

Choose `epsilon>0` and put

\[
L=\frac{\kappa}{r\epsilon}.
\]

Let `D` be the set

\[
D=\left\{
 r\le v\le2r,\ 0\le w\le L,\
 -\frac{w^2}{2\kappa v}\le u\le
 -\frac{w^2}{2\kappa v}+\frac{\epsilon}{\kappa}
\right\}.                                                          \tag{5.4}
\]

Its volume is exactly

\[
r\cdot L\cdot\frac{\epsilon}{\kappa}=1.                           \tag{5.5}
\]

Therefore `rho=1_D` is a probability density bounded by one. On `D`,

\[
0\le \kappa u+\frac{w^2}{2v}\le\epsilon,                           \tag{5.6}
\]

so (5.2) holds with `E=[0,epsilon]`. But the right-hand side of (5.3) is `C r^{3/2} sqrt(epsilon)`, which is less than one for sufficiently small `epsilon`. QED.

This proposition is **not** a counterexample to QFORM: the engineered joint law (5.4) is not asserted to be an orthogonal projection of independent cap-one coordinates. Its role is to identify the exact missing factor. Any proof of (3.1) has to use the original product representation before taking the curved trace; an `L^infinity` cap on the projected triple cannot suffice.

## 6. Exact relation to the current single-hub source

The current Claude continuation `single_hub_core/REPORT.md` contains a proved theorem for

\[
2X_h(L+\beta)+\lambda V_0^2+2V_0 g(L,Z_0)+F(L,Z_0)                 \tag{6.1}
\]

in terms of the maximal slice quantity

\[
M_k=\sup_l\int\sup_u\rho_{L,V_0,Z_0}(l,u,z)\,dz.                  \tag{6.2}
\]

Our Witt form (1.1) is exactly of this structural type after taking the source's `L` to be our `V`, its transverse square variable to be our `W`, and its one-dimensional hidden projection `Z_0` to be our `U`; the term `2a kappa U V` is absorbed into the arbitrary `F(L,Z_0)`.

However, the same source explicitly leaves a universal rough-law bound for the relevant maximal/curved-section quantity open and records comb-law growth of the maximal functional. Thus Theorem 3.2 of that source does **not** close the present endpoint. Proposition 5.1 above gives the corresponding target-specific geometric reason: maximizing a moving curved trace before using product provenance destroys the needed `r^{1/2}|E|^{1/2}` gain.

The useful synthesis is therefore:

- the current source proves that a suitable Borel square-root slice profile is sufficient;
- Lemma 3.1 compiles the **specific Witt shell profile** into the exact determinant-star scale `(a^2|delta|)^(-1/3)`;
- the account02/B05 partner theorem supplies this profile at `kappa=0`;
- Proposition 5.1 rules out proving the `kappa>0` profile from a generic projected density cap.

No source-matching proved theorem was found that already supplies (3.1) for arbitrary rough product laws.

## 7. First unpaid implication after this run

The precise next statement is

`QFORM-WITT-PRODUCT-PROJECTION-BOREL-TUBE-v1`:

> Let independent original coordinates have densities at most one, and let `(U,V,W)` be any three orthonormal linear projections of that product law. Put `Z=W+theta V`. Prove that for every `0<=kappa<1/sqrt(7)`, every real `d,theta,t`, every `r>0`, every nonzero scale pair `a,delta`, and every Borel `E`,
> \[
> P\{r\le|V|\le2r,\ \kappa U+dV+(\delta Z^2-t)/(2aV)\in E\}
> \le K_T\sqrt{|a/delta|}\,r^{3/2}|E|^{1/2}
> \]
> with one absolute `K_T`, **or** replace this profile by another product-preserving estimate that yields the same dyadic `sqrt(r)` gain after convolution with the literal independent hub.

A proof gives the whole near-coloop Witt endpoint immediately by Lemma 3.1 and `a^2|delta|>=1/2`. A counterexample must be built from an actual product law and orthonormal projection; Proposition 5.1 shows only that arbitrary dependent triples are too broad.

## 8. Scope audit

**Proved in this run:** exact shell identity (2.4); the Borel-profile compiler (3.2); a sharpened `kappa=0` bound (4.2) by an actual account02/B05 application; and the generic-joint shared-shear tube counterexample (5.4)--(5.6).

**Not proved:** the product-projection Borel tube for `kappa>0`; the residual-heavy branch outside the current Witt reduction; arbitrary extra spectrum; the full QFORM theorem; or full-target continuity.

No Gaussianity, log-concavity, moment, compact-support, connected-support, diagonal-basis assumption, post-rotation independence, conditional-cap-as-independence, unrestricted fiber supremum, or small-random-tail deletion is used.

Independent end-to-end review of the new conditional compiler and counterexample is PENDING.
