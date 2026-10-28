SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-24T06:20:05Z.
attacking: `QFORM-MIXED-LAYER-NORMAL-INNOVATION-RECEIVER-v1`; retain the r52 curved two-row tail plane, aggregate the true normal innovation with the full rank-two cross determinant before inversion, and prove a compensated cross-volume identity.

# account03/B06 — normal-innovation compensation inside the localized three-hub packet

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.  
Immediate B06 predecessor: `yspennstate/math-open-problems@74520bfd95aaeff165f530b70e86d00419d2c411`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260924T042233Z-account03-B06-qform-r52/REPORT.md`.  
Designated partner actually applied below: account04/B06 `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`, `yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`.  
Execution label: `WITHOUT_VERIFIED_BRAIN`; authenticated repository access is not native learned-memory ingestion.

The full QFORM conjecture remains OPEN. The new result is a scoped product-preserving compiler for the low-Pluecker-disjointness three-hub branch.

## 1. Input from r52 and first missing implication

The predecessor reduces the low-disjointness rank-three core to a literal physical hub triple and a tail matrix

\[
R=R_H[I_3,Z],\qquad G=ZZ^T,
\]

with a selected hub row `h` and the other two rows `J` such that, writing

\[
E:=Z_J,\qquad G_2:=EE^T,\qquad W:=\det G_2>0,
\]

and decomposing

\[
z_h=qE+n,\qquad n\perp\operatorname{rowspan}(E),\qquad \nu:=\|n\|^2,
\]

one has

\[
W\ge \frac13s_1s_2\ge \frac19e_2(G),\qquad \nu\le3s_3<\frac15.
\]

The same run proves the mixed Pluecker-layer identity

\[
P=P_0+P_1+P_2+P_3,
\]

with `max(P0,P1,P2)>5P/16`. Its unresolved point is that a literal diagonal perturbation on the selected hub leaves a true normal shared-bank term proportional to `n`; smallness of that term cannot simply be treated as a perturbation because of the live indefinite-arbitrary-remainder correction.

This run attacks that exact point without taking any fiber supremum.

## 2. Exact compensated cross-volume identity

Write the rank-three core coefficient in the selected literal hub basis as

\[
B=\begin{pmatrix}a_0&b^T\\ b&C\end{pmatrix},
\qquad C=C^T\in\mathbb R^{2\times2},\qquad D:=\det B\ne0.
\]

Let `d` be the coordinate-separable diagonal coefficient on the selected hub, and let

\[
a:=a_0+d.
\]

Assume `a\ne0`, so this physical scalar is a legal literal pivot. The exact post-pivot cross matrix from the two remaining hub coordinates to the whole tail bank, as established in r52, is

\[
N=\frac da\,b z_h+\left(C-\frac{bb^T}{a}\right)E. \tag{2.1}
\]

Define

\[
K:=\det C,\qquad c:=\operatorname{adj}(C)b,\qquad
\theta:=K+q c, \tag{2.2}
\]

and the normal-energy currency

\[
H:=\nu\,c^T\operatorname{adj}(G_2)c\ge0. \tag{2.3}
\]

### Theorem 2.1 — `QFORM-NORMAL-INNOVATION-COMPENSATED-CROSS-VOLUME-v1`

One has the exact identity

\[
\boxed{
 a^2\det(NN^T)
 =W(D+d\theta)^2+d^2H.
} \tag{2.4}
\]

Thus the tangential determinant cancellation and the true normal innovation enter as an orthogonal sum of squares. In particular an adversarial diagonal coefficient `d` cannot cancel the tangential rank-two determinant without paying the normal volume whenever `H>0`.

### Proof

Put

\[
S:=C-\frac{bb^T}{a},\qquad u:=\frac da b.
\]

Then (2.1) and `z_h=qE+n` give

\[
N=(S+u q)E+u n. \tag{2.5}
\]

The two rows of `(S+uq)E` lie in `rowspan(E)`, whereas `n` is orthogonal to that entire plane. Therefore the two-row exterior product splits orthogonally. If `u^\perp=(u_2,-u_1)^T`,

\[
\det(NN^T)
 =\det(S+uq)^2W
  +\nu\,(u^\perp)^T S G_2 S^T u^\perp. \tag{2.6}
\]

Indeed the `uq` part disappears from the second term because `(u^\perp)^Tu=0`.

For a `2 x 2` matrix the adjugate is linear in the matrix entries, and

\[
\operatorname{adj}(bb^T)b=0.
\]

Hence

\[
\operatorname{adj}(S)b=\operatorname{adj}(C)b=c. \tag{2.7}
\]

Since `S` is symmetric,

\[
(b_2,-b_1)S=(c_2,-c_1). \tag{2.8}
\]

For symmetric `2 x 2` `G_2`, rotation by ninety degrees changes its quadratic form into the adjugate quadratic form, so (2.8) gives

\[
\nu\,(u^\perp)^T S G_2S^Tu^\perp
 =\frac{d^2}{a^2}\nu c^T\operatorname{adj}(G_2)c
 =\frac{d^2}{a^2}H. \tag{2.9}
\]

Next,

\[
\det S
 =\det C-\frac1a b^T\operatorname{adj}(C)b
 =\frac{D+dK}{a}, \tag{2.10}
\]

because `D=a_0K-b^T adj(C)b`. The rank-one determinant identity and (2.7) then give

\[
\det(S+uq)
 =\det S+q\operatorname{adj}(S)u
 =\frac{D+dK+dqc}{a}
 =\frac{D+d\theta}{a}. \tag{2.11}
\]

Substituting (2.9) and (2.11) into (2.6) proves (2.4). QED.

## 3. Coordinate-free curvature interpretation

Let

\[
t:=\operatorname{adj}(B)e_h.
\]

In the `(h,J)` ordering one has exactly

\[
t=(K,-c_1,-c_2)^T.
\]

### Theorem 3.1 — `QFORM-NORMAL-TANGENTIAL-ADJUGATE-SPLIT-v1`

For the full three-row tail Gram matrix `G=ZZ^T`,

\[
\boxed{
 t^T\operatorname{adj}(G)t=W\theta^2+H.
} \tag{3.1}
\]

### Proof

The row decomposition `z_h=qE+n` gives

\[
G=
\begin{pmatrix}
qG_2q^T+\nu&qG_2\\
G_2q^T&G_2
\end{pmatrix}. \tag{3.2}
\]

Direct `3 x 3` cofactor expansion of (3.2), followed by insertion of `t=(K,-c)`, yields

\[
W(K+qc)^2+\nu c^T\operatorname{adj}(G_2)c,
\]

which is (3.1). Equivalently, for `nu>0` factor (3.2) as a unitriangular congruence of `diag(nu,G_2)` and use `adj(G)=det(G)G^{-1}`; the singular endpoint follows by polynomial continuity. QED.

Thus `H` is not an arbitrary norm of a leftover vector. It is precisely the normal share of the physical Pluecker/adjugate curvature associated with the selected hub cofactor direction.

## 4. A cancellation-proof quantitative dichotomy

If `theta != 0`, define

\[
\chi:=\frac{H}{W\theta^2}; \tag{4.1}
\]

if `theta=0`, set `chi=+infinity`. From (2.4), either

\[
|D+d\theta|\ge\frac{|D|}{2},
\]

or else `|d theta|>|D|/2`. Hence in all cases

\[
\boxed{
W(D+d\theta)^2+d^2H
\ge \frac{WD^2}{4}\min\{1,\chi\}.
} \tag{4.2}
\]

Let

\[
\Delta:=\sigma_1(N)\sigma_2(N)=\sqrt{\det(NN^T)}.
\]

Then

\[
\boxed{
|a|^2\Delta
\ge
\frac{|a|\,|D|\sqrt W}{2}\min\{1,\chi\}^{1/2}.
} \tag{4.3}
\]

The completed physical scalar-pivot/rank-two-cross receiver used already in r52 has the form

\[
\|p_Q\|_\infty\le 8\,[|a|^2\Delta]^{-1/4}. \tag{4.4}
\]

Combining (4.3) and (4.4) proves the full-scalar bound in this scoped branch:

\[
\boxed{
\|p_Q\|_\infty
\le
8\,2^{1/4}
[|a|\,|D|\sqrt W]^{-1/4}
\min\{1,\chi\}^{-1/8}.
} \tag{4.5}
\]

No dimension-dependent fiber maximum occurs: the entire normal/tangential cross volume is combined before its reciprocal is paid.

A useful fixed gate is

\[
\chi\ge\frac1{64}.
\]

Then (4.5) simplifies exactly to

\[
\boxed{
\|p_Q\|_\infty
\le16\,[|a|\,|D|\sqrt W]^{-1/4}.
} \tag{4.6}
\]

This establishes absolute continuity and an essentially bounded density on that branch. Continuity is not claimed from receiver (4.4).

Using the r52 lower bound `W>=e_2(G)/9` and `P_0=|D|`, `P_2=|D|e_2(G)`,

\[
|D|\sqrt W\ge\frac13\sqrt{P_0P_2}, \tag{4.7}
\]

so the same paid branch also satisfies

\[
\boxed{
\|p_Q\|_\infty
\le16\,3^{1/4}
[|a|\sqrt{P_0P_2}]^{-1/4}.
} \tag{4.8}
\]

This does not by itself lower-bound `P0*P2` from the r52 statement `max(P0,P1,P2)>5P/16`; that is an explicitly retained structural debt.

## 5. The only unpaid positive-normal branch is a 1/65 adjugate collar

If

\[
0<\chi<\frac1{64},
\]

then (3.1) yields

\[
\boxed{
\frac{H}{t^T\operatorname{adj}(G)t}<\frac1{65},
\qquad
\frac{W\theta^2}{t^T\operatorname{adj}(G)t}>\frac{64}{65}.
} \tag{5.1}
\]

Thus failure of the new compensated receiver does not leave an arbitrary shared-bank innovation. More than `64/65` of the selected hub's adjugate-weighted third-curvature currency is tangential to the two strong rows; less than `1/65` is genuinely normal.

There is also a sharp exact-endpoint description. Since `B` is invertible, `c=adj(C)b=0` implies `b=0`: indeed `D=a_0 det(C)-b^T adj(C)b`, so `c=0` and `D!=0` force `det(C)!=0`, after which `b=0`. Since `G_2` is positive definite,

\[
\boxed{H=0\iff (\nu=0)\ \text{or}\ (b=0).} \tag{5.2}
\]

Therefore exact zero normal energy means either the tail row is literally in the two-row curved plane, or the hub-to-two-hub coupling generating the normal leakage vanishes. There is no hidden third case.

## 6. Actual designated-partner application

The current designated partner account04/B06 theorem `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1` proves that, for an orthonormal curved two-frame whose physical column leverages are at most `1/2`, a shared-bank transverse statistic lying exactly in that plane is removed by fold recentering and a determinant-one output shear. At off-fold radius `r`, its two-output density is at most `4/(|lambda_*|r)`.

Apply this to the exact endpoint `H=0` above, using the same whitening of `E` as in r52. If

\[
\max_k\ell_k\le\frac12,
\]

then every surviving shared-bank term from (2.5) is tangential to the curved two-frame (or is absent). At the actual scale `r=1/64`, the partner theorem gives the concrete inequality

\[
\boxed{
\|g_{\rm off}\|_\infty\le\frac{256}{|\lambda_*|}.
} \tag{6.1}
\]

This density is continuous and `C_0` in the partner theorem's two-output off-fold scope. I do not promote (6.1) through the same-bank diagonal phase or through a positive normal innovation, which are outside that theorem. If the leverage gate fails, because the two-frame leverages sum to two there are at most three literal heavy tail coordinates, exactly the finite-hub certificate recorded in r52.

This is an actual use of the designated partner theorem at a live inequality, not merely a citation.

## 7. What has changed in the branch tree

Before this run, an arbitrary hub diagonal coefficient `d` could apparently make the tangential rank-two cross determinant small while leaving a small but nonzero normal innovation, with no safe way to discard that innovation. The exact identity (2.4) removes that ambiguity:

- if the normalized normal share `chi>=1/64`, the complete scalar output is paid by (4.6);
- if `chi=0`, the exact shared leakage is tangential/absent, and the designated partner gives (6.1) under its diffuse leverage gate;
- if `0<chi<1/64`, the remaining packet is quantitatively confined to the `>64/65` tangential adjugate-curvature collar (5.1);
- if the two-frame diffuse leverage gate fails, at most three literal heavy tail coordinates remain.

No Gaussian, moment, compact-support, log-concavity, connected-support, diagonal-basis, or post-rotation independence assumption is introduced.

## 8. Symbolic verification

A separate deterministic SymPy checker expands both exact polynomial identities:

1. `a^2 det(NN^T) - [W(D+d theta)^2+d^2 H]`;
2. `t^T adj(G)t - [W theta^2+H]`.

Both simplify identically to zero. This is a diagnostic verification only; Sections 2 and 3 contain the proofs.

## 9. Remaining implication

The next B06 debt is

`QFORM-ADJUGATE-6465-TANGENTIAL-COLLAR-RECEIVER-v1`:

consume the branch `0<chi<1/64`, where more than `64/65` of the selected hub adjugate curvature is tangential but the normal innovation is genuinely nonzero. The proof must combine the partner's exact tangential fold shear with the retained layer-0/1/2 third-curvature mass before any inverse normal coefficient is paid. The zero-pivot case `a=0`, the `rank Z<=1` lower-rank endpoint, and finite heavy-tail-hub certificates remain separate explicit branches and must not be silently dropped.

## Global status

**FULL QFORM: OPEN / NOT PROVED / NOT DISPROVED.**

**GLOBAL CONTINUITY: OPEN.**
