SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T15:21:29Z.
attacking: the punctured true-near-coloop ultra-collar; couple the order-one indefinite hub-pair packet to a genuinely disjoint bordered-triple packet before any local-minor inversion.

# account01/B10 — disjoint pair-times-triple packing in the punctured near-coloop collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T152129Z-account01-B10-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / NEW_EXACT_AGGREGATE_PACKING / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full arbitrary exact-rank-three theorem and the owner-level three-large-eigenvalue conjecture remain **OPEN / NOT PROVED / NOT DISPROVED**. This run advances the first unpaid implication from the preceding account01/B10 report: the two separately known currencies — negative hub--leaf pair determinant mass and bordered principal three-volume — can always be packed **simultaneously into three disjoint original-coordinate banks**, with a universal multiplicative lower bound. Thus fragmentation cannot force the pair resource and the third-rank resource to live on incompatible coordinates.

## 1. Source state and inherited hard chamber

Fresh control source: `yspennstate/math-research-brain@63c79bd8f5831cb7523e01fc6e2f2173b7f51f3b`, OWNER CONTROL revision `2026-09-22.15`. The current programme state still records the full conjecture as open. The live corrections consumed include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, the false arbitrary-joint coarea gate, the false positive conditional-projection-moment gate, and `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`.

Use the exact-rank-three representation

\[
A=UMU^T,\qquad U^TU=I_3,
\]

where every eigenvalue of the real symmetric `M` has modulus at least one. Put

\[
D:=|\det M|\ge1.
\]

For the physical hub row write

\[
u_0=\sqrt h\,r,\qquad \|r\|=1,
\]

and for every leaf

\[
u_i=\alpha_i r+z_i,\qquad z_i\perp r.
\]

Then

\[
\sum_{i>0}z_i z_i^T=I_{r^\perp},\qquad
\tau_i:=\|z_i\|^2.
\tag{1.1}
\]

The already-paid branches allow the current hard chamber to be restricted to

\[
0<|a|D<2^{-12},\qquad a=r^TMr,\qquad h>\frac{63}{64},
\tag{1.2}
\]

and

\[
\tau_i<\frac14\quad(i>0).
\tag{1.3}
\]

Define the physical bordered pair determinants

\[
\Delta_i:=\det A[\{0,i\}],
\]

and the negative-pair index set and mass

\[
B:=\{i>0:\Delta_i<0\},\qquad
w_i:=-\Delta_i\ (i\in B),\qquad
W:=\sum_{i\in B}w_i.
\tag{1.4}
\]

The preceding account01/B10 exact signed identity gives in this chamber

\[
W>c_*:=\frac{63}{64}\frac{4093}{4096}
=\frac{257859}{262144}>0.983654.
\tag{1.5}
\]

Also, for every pair of distinct leaves,

\[
|\det A[\{0,j,k\}]|
=Dh\,\det(z_j,z_k)^2.
\tag{1.6}
\]

The problem left by the preceding run was that (1.5) and the total version of (1.6) were not yet known to coexist on disjoint product banks.

## 2. Exact leave-one-out transverse-volume identity

For a fixed leaf `i`, Cauchy--Binet in the transverse plane gives

\[
\sum_{\substack{j<k\\j,k\ne i}}
\det(z_j,z_k)^2
=
\det\!\left(\sum_{j\ne i}z_jz_j^T\right).
\tag{2.1}
\]

Using (1.1), the matrix in the determinant is `I-z_i z_i^T`. The rank-one determinant lemma therefore gives the exact identity

\[
\boxed{
\sum_{\substack{j<k\\j,k\ne i}}
\det(z_j,z_k)^2
=1-\tau_i.
}
\tag{2.2}
\]

Because of (1.3), every negative-pair leaf has at least three quarters of the full transverse two-volume still available **away from that same original coordinate**:

\[
1-\tau_i>\frac34.
\tag{2.3}
\]

Multiplying (2.2) by `w_i` and summing over `B` gives

\[
\boxed{
\sum_{i\in B}w_i
\sum_{\substack{j<k\\j,k\ne i}}
\det(z_j,z_k)^2
=
\sum_{i\in B}w_i(1-\tau_i)
>\frac34 W.
}
\tag{2.4}
\]

This already shows that the third-rank resource cannot be supported only on the same leaf responsible for an indefinite hub pair.

## 3. Three-colour product-preserving packing theorem

Colour every leaf independently and uniformly with one of three colours `H,J,K`. Define

\[
W_H:=\sum_{i\in B\cap H} w_i,
\tag{3.1}
\]

and

\[
V_{JK}:=\sum_{j\in J,\ k\in K}\det(z_j,z_k)^2.
\tag{3.2}
\]

The banks are literal disjoint sets of original coordinates. Expanding `W_HV_{JK}`, a fixed term indexed by a negative leaf `i` and an unordered pair `{j,k}` disjoint from `i` is present precisely when `i` receives colour `H` and `j,k` receive the two colours `J,K` in either order. That probability is

\[
\frac13\cdot\frac{2}{9}=\frac{2}{27}.
\tag{3.3}
\]

Therefore (2.4) gives

\[
\mathbb E[W_HV_{JK}]
=
\frac{2}{27}
\sum_{i\in B}w_i(1-\tau_i)
>
\frac{W}{18}.
\tag{3.4}
\]

Hence there exists a deterministic partition into three disjoint original-coordinate banks for which

\[
\boxed{
W_HV_{JK}>\frac{W}{18}>\frac{c_*}{18}
=0.0546474456\ldots .
}
\tag{3.5}
\]

Now convert the transverse wedge bank into actual physical bordered principal-three-volume:

\[
T_{JK}:=
\sum_{j\in J,\ k\in K}
|\det A[\{0,j,k\}]|
=Dh\,V_{JK}.
\tag{3.6}
\]

Combining (1.2), (1.5), and (3.5),

\[
\boxed{
W_H T_{JK}
>
\frac{Dh\,c_*}{18}
\ge
\frac{63}{64}\frac{c_*}{18}
=
\frac{1805013}{33554432}
>0.05379357.
}
\tag{3.7}
\]

### Interpretation

Equation (3.7) is the new structural certificate. It is stronger than separately knowing `W>c_*` and total bordered triple mass `Dh`: it says a **single deterministic product-preserving decomposition** carries both currencies at once.

- bank `H` carries a fixed aggregate of genuinely indefinite physical hub--leaf `2x2` determinants;
- banks `J,K` jointly carry a fixed transverse wedge packet, equivalently a fixed bordered principal-triple packet;
- `H,J,K` are disjoint original-coordinate sets, so no independence is inferred after a spectral rotation;
- no reciprocal of a local determinant is introduced, so arbitrary fragmentation is allowed.

The live two-slope correction is respected: (3.7) does **not** claim that the hub plus two strong slopes alone suffices. The extra factor `T_{JK}` is exactly the third-rank resource that the previous two-bank compiler lacked.

## 4. Designated account02/B10 result applied to an actual inequality

The newest completed designated-partner report available at the start of this run is

`yspennstate/math-open-problems@ebceb50f1e0c2589cb7599f57c4deb4a3ffd0f2b`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260923T141719Z-account02-B10-QFORM-r11/REPORT.md`.

Its theorem `QFORM-COLOOP-RANKONE-TRANSVERSE-MF-v1` treats a pure original-coordinate coloop `h=1` whose actual transverse compression has rank one, provided every transverse leaf leverage is at most `1/2`. It proves a continuous density and

\[
\|p_Q\|_\infty
\le 3\,2^{4/3}D^{-1/3}.
\tag{4.1}
\]

In the present normalization `D\ge1`, so this gives the concrete payment

\[
\boxed{
\|p_Q\|_\infty
\le3\,2^{4/3}<7.560.
}
\tag{4.2}
\]

Moreover, after the already-paid transverse-heavy branch is removed, (1.3) implies the partner leverage hypothesis automatically on the exact-coloop face. Thus the rank-one transverse exact-coloop endpoint is fully paid, including continuity; the unresolved punctured chamber is genuinely the nonzero/rank-two interpolation state for which (3.7) was derived.

The same partner report also records the ruled one-sheet estimate `p_Q(s)<=pi*sqrt(2)` on the appropriate one-sheet side of an indefinite exact-rank-three form. Since (1.2) forces the near-null state to be indefinite, that side is already paid; the receiver sought below only has to handle the opposite two-sheet side without the invalid square-peel majorant.

## 5. First unpaid implication after this run

The first unpaid implication is now

`QFORM-DISJOINT-BORDERED-PAIR-TRIPLE-RECEIVER-v1`:

> Given a near-coloop exact-rank-three form in the chamber (1.2)--(1.3), and disjoint original-coordinate banks `H,J,K` satisfying the scale-free product certificate (3.7), prove a dimension-free density bound while allowing arbitrary within-bank quadratic curvature, arbitrary longitudinal leakage, and at most the already-localized finite set of normalized-leverage exceptions. The proof must spend the indefinite hub-pair packet and the bordered-triple packet jointly, before any local-minor inversion or conditional fiber supremum.

A natural analytic target is a bank-level mixed-Fresnel / hyperbolic receiver whose constant depends on `(W_HT_{JK})^{-theta}` for some fixed positive `theta`; (3.7) would then close the ultra-collar uniformly. What is *not* valid is to select one local pair or one local triple by pigeonhole, or to replace the three banks by dependent spectral coordinates.

## 6. Status and continuity

- New theorem (3.7): exact structural/product-preserving certificate; no density regularity by itself.
- Partner rank-one exact-coloop branch (4.2): continuous density, universal bound `<7.560`.
- Ruled one-sheet side: bounded as stated in the partner source.
- Remaining punctured two-sheet bank receiver: **OPEN**.
- Arbitrary exact-rank-three theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.

No Gaussianity, log-concavity, moments, support regularity, diagonal-basis independence, or pointwise van-der-Corput decay is used.
