# B17 FEI interface-C adversary — fixed-order moment-credit barrier and critical-core replacement

**Date:** 21 September 2026  
**Scope:** account03/B17, exact Boolean adversary for joint interface C  
**Execution:** WITHOUT_VERIFIED_BRAIN  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact theorem about a specific admissible Boolean family and a class of proposed positive-credit repairs. It is not a counterexample to FEI and is not a novelty claim.

## 0. New route and peer result consumed

This run changes mechanism. It does not repeat the preceding Holevo/Gram or scalar-kernel adversary. The route is:

> **C-MOMENT-ORDER BARRIER.** After a positive live-window current estimate has failed, test whether adding finitely many ordinary spectral factorial-moment / entropy credits can repair it. If not, quantify how much moment order would be required and replace the universal positive-current target by a signed or high-ratio-critical-core target.

The primary completed other-account result consumed substantively is

`account02/interactive/20260921T204926Z-threshold-contraction/HALFBAND_COLLISION_EXTENSION.md`

at scientific commit `98dc4d163ea7bd0375387cd0a99e6560bf44942b`, blob `2efc5dedf145a262700649c6e711c6a6fb91d622`. It proves for an exact Boolean four-point family, at the authentic half-band cutoff and for every `D >= 128`,

\[
\mathcal C_D:=\int_{40}^{S_f}\mathcal E_{\rm cur}(s)\,\frac{ds}{s^3}
\ge \frac{7}{3145728(D-1)^3},
\tag{0.1}
\]
while `J(f)=I(f)=8(D-1)/2^D` and `H(f)<4I(f)`. The lower bound is on the genuine positive live current with the actual active law and retained code, not an abstract surrogate.

I also consume account01/B16

`account01/B16/20260921T204046Z-terminal-shell-feature-projector/REPORT.md`, blob `6fd80765ed5b10f52b8aaf2464d671bd29c41892`.

That result proves the terminal subtraction is exactly the retained-shell projector and that the authentic Brownian/Laplace source is a same-syndrome square. Thus the obstruction below is applied *after* the terminal/syndrome structure is known; it does not rely on deleting those signs by hand.

## 1. Exact Boolean adversary and its spectral law

Use the exact account02 construction. Let `N=2^D`, `n=D-1`. On the original `n`-cube choose two negative points `u` and `v=u+e_2+e_3`, make the function `-1` there and `+1` elsewhere, and append one dummy coordinate. The negative set in the `D`-cube is an affine two-plane of four points.

The peer computation gives that the Fourier support is

\[
L^\perp,\qquad L=\operatorname{span}(e_2+e_3,e_D),
\]
with

\[
\widehat f(\varnothing)=1-\frac8N,
\qquad
|\widehat f(S)|=\frac8N\quad(S\in L^\perp\setminus\{\varnothing\}),
\tag{1.1}
\]
and zero otherwise. Hence the spectral probabilities are

\[
p_\varnothing=(1-8/N)^2,
\qquad
p_S=64/N^2\quad(S\in L^\perp\setminus\{\varnothing\}).
\tag{1.2}
\]

The conditions defining `L^perp` are `S_2=S_3` and `S_D=0`. If `S` is uniform on `L^perp`, then

\[
|S|\overset d=B+2Z,
\qquad B\sim\mathrm{Bin}(D-3,1/2),\quad Z\sim\mathrm{Bernoulli}(1/2),
\tag{1.3}
\]
with `B,Z` independent.

This is an admissible Boolean spectrum, not a relaxed probability-law witness.

## 2. PROVED — exact factorial-moment formula

For `k>=1` define the ordinary falling-factorial spectral moment

\[
M_k(f)=\mathbb E_{S\sim\widehat f^2} (|S|)_k.
\]

Because the empty coefficient contributes zero to `M_k` and `|L^perp|=N/4`, (1.2)-(1.3) give

\[
M_k(f)=\frac{16}{N}\,\mathbb E(B+2Z)_k.
\tag{2.1}
\]

Using the binomial identity for falling factorials, `E(B)_j=(D-3)_j/2^j`, and

\[
\mathbb E(2Z)_0=1,\qquad \mathbb E(2Z)_1=1,\qquad
\mathbb E(2Z)_2=1,\qquad \mathbb E(2Z)_j=0\ (j\ge3),
\]
we obtain the exact formula

\[
\boxed{
M_k(f)=\frac{16}{N}\left[
\frac{(D-3)_k}{2^k}
+k\frac{(D-3)_{k-1}}{2^{k-1}}
+\binom{k}{2}\frac{(D-3)_{k-2}}{2^{k-2}}
\right],
}
\tag{2.2}
\]
where terms with negative subscripts are zero.

At `k=1`, (2.2) gives

\[
M_1(f)=\frac{8(D-1)}N=I(f)=J(f),
\tag{2.3}
\]
so the normalization matches the exact influence computation.

For each fixed `k`, and more generally uniformly for `k<=D`, the crude estimate

\[
M_k(f)\le \frac{16D^k}{N}\,\mathrm{poly}(k)
\tag{2.4}
\]
is enough for the asymptotic barrier below.

## 3. REFUTED — finitely many polynomially weighted positive moment credits cannot pay interface C

Consider any proposed positive repair of the form

\[
\mathcal L_D(f)
=a_H(D)H(f)+\sum_{k=1}^{K}a_k(D)M_k(f),
\tag{3.1}
\]
where `K` is fixed, all coefficients are nonnegative, and for some fixed `A,C`,

\[
a_H(D),a_k(D)\le C D^A.
\tag{3.2}
\]

### Theorem 3.1 — fixed-order positive-credit barrier

For every fixed `K,A,C`, the exact Boolean family above satisfies

\[
\frac{\mathcal C_D}{\mathcal L_D(f_D)}\longrightarrow\infty.
\tag{3.3}
\]

Therefore there is no dimension-independent universal implication

\[
\mathcal C_D\le C'\mathcal L_D(f)
\tag{3.4}
\]
for all Boolean `f` using a fixed finite list of ordinary factorial spectral moments and polynomially growing positive weights.

### Proof

The consumed peer result gives `H(f_D)<4I(f_D)=32(D-1)/N`. Formula (2.2) gives, for fixed `K`,

\[
\mathcal L_D(f_D)=O(D^{A+K}/2^D).
\]

But (0.1) gives `C_D >= c D^{-3}` for an absolute `c>0`. Their ratio tends to infinity exponentially. QED.

### Stronger order consequence

The same proof does not require `K` fixed. If the number and coefficients of the positive moment credits are subexponential in `D` and the largest moment order satisfies

\[
K(D)=o(D/\log D),
\]
then `D^{K(D)}=e^{o(D)}`, so their total contribution is still

\[
e^{-D\ln2+o(D)},
\]
while the exact live current is only polynomially small. Thus a purely positive ordinary-moment repair requires moment order at least on the scale `D/log D` (or exponentially large weights), unless it uses additional signed/structural information.

This statement is deliberately narrow: it does **not** refute sign-sensitive compiler moments, a dimension-growing exact expansion, negative entropy/R16 credits, or a valid high-ratio-core reduction.

## 4. Exact targeted computation

The companion standard-library checker evaluates (2.2) with exact rational arithmetic and compares it with the analytic half-band lower bound. Selected displays:

- `D=128`: `C_D >= 1.0863398454e-12`; `M_12 = 1.1920616560e-16`, `M_14 = 3.9190899927e-13`, `M_15 = 2.2181167902e-11`. Unit moment weight first crosses the current lower bound at order 15.
- `D=256`: first crossing at order 31.
- `D=512`: first crossing at order 59.
- `D=1024`: first crossing at order 109.

These finite numbers are diagnostics of the proved asymptotic theorem, not an exhaustive Boolean sweep and not evidence for full FEI.

Boundary checks: `M_1` is exactly `I`; all moments vanish appropriately on a character concentrated at one Fourier set above its degree; the adversarial source itself satisfies `H/I<4`, so none of the current lower bounds is an FEI counterexample.

## 5. Replacement mechanism — conditional critical-core / signed-pre-square target

The failed target was too strong because it tried to make a **positive** live-current functional universally `O(J)` even on functions already satisfying a much stronger entropy bound. The four-point family has `H<4J`; there is no reason a contradiction proof of FEI must pay its positive current separately.

A source-valid replacement has two possible forms, both materially different from adding another positive low-order credit:

1. **Critical-core conditional interface C.** In a contradiction proof at a candidate FEI constant `C>4`, invoke the interface-C payment only after reducing to a centered primitive/minimum-dimensional function satisfying `H(f)>C J(f)`. The low-ratio family here is then excluded by an actual hypothesis rather than by wishful cancellation. What remains to prove is that the compiler/window inequality survives this legitimate critical-core reduction with all terminal and negative credits counted once.
2. **Signed pre-square cancellation.** Keep the retained terminal/R16/negative-entropy terms coupled to the live current *before* positive squaring. Theorem 3.1 shows that no fixed collection of positive low-order spectral moments can replace this signed information. A concrete next lemma should cancel or transfer the low-order relation sector in the signed ledger first, and only then apply a positive tail estimate.

The present run does not prove either universal replacement. It proves that one of these genuinely structural changes (or an equally strong alternative) is necessary for this interface-C route.

## 6. Joint handoff

- **consumed_peer_artifact:** account02 interactive `HALFBAND_COLLISION_EXTENSION.md`, blob `2efc5dedf145a262700649c6e711c6a6fb91d622`; account01/B16 terminal-shell projector report, blob `6fd80765ed5b10f52b8aaf2464d671bd29c41892`.
- **applied_to_claim:** test whether the refuted universal positive half-band current payment can be repaired by finitely many positive ordinary spectral factorial-moment/entropy credits.
- **result:** **REFUTED** for every fixed finite list with polynomial weights; more generally any subexponentially weighted moment-only repair with maximum order `o(D/log D)` fails on the exact admissible Boolean family.
- **remaining_implication:** prove a high-ratio-critical-core conditional signed window contraction, or prove a signed pre-square cancellation theorem that removes the low-order retained sector before positive estimation. Do not retry a universal positive-current `O(J)` inequality or a fixed finite positive moment ledger.
- **next_recipient:** account03/B16 (live-window signed transfer) and account03/B18 (interface-C integration); account02/B16 can use the order barrier when choosing authentic-parent credits.

**Full FEI remains OPEN / NOT PROVED.**
