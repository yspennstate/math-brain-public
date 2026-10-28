# account02/B15 — exact Gibbs-KL gate factorization and an explicit 4.4e-6 five-input prime tube

**Run:** `20260922T0704Z-account02-B15-r14`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_INFORMATION_CREDIT / EXPLICIT_PRIME_BIAS_TUBE`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Fresh target, peer inputs, and movement


`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T065506Z-prime-central-orbits/REPORT.md`

(report blob `bdbc1c2378da80c6a7d1b1dbb02ceafa2496cc96`).  It keeps the current source-exact candidate

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\tag{0.1}
\]

and the exact universal missing implication

\[
\boxed{
D_{\Gamma^\dagger}(P;p)\ge0
\quad\text{for every finite composition-prime Boolean gate }P
\text{ and every interior product bias }p.
}
\tag{0.2}
\]

Its new theorem identifies every equality case in the rigorous five-input central certificate with a read-once cube-automorphism orbit.  Consequently every essential composition-prime five-input gate has the strict central reserve

\[
\boxed{D_{\Gamma^\dagger}(P;1/2^5)\ge\delta_5},
\qquad
\delta_5=0.004906502214.
\tag{0.3}
\]

The B-lead explicitly leaves as its next obligation an **explicit certified radius** for the common prime-gate tube.

A second completed other-account result consumed substantively is account03/B15

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T052547Z-arity5-bias-tube/REPORT.md`.

It proves every five-input gate is safe for `max_i |p_i-1/2|<=10^-7` and, more importantly here, supplies source-valid regularity estimates for the committed potential and the actual biased Fourier transform: on the output interval whose smaller representative is at least `1/64`,

\[
| (\Gamma^\dagger)' |<85,
\tag{0.4}
\]

and for a five-input truth table the biased Fourier coefficient vectors obey

\[
\|a(p)-a(1/2^5)\|_2
\le {20\over\sqrt3}\,\|p-1/2^5\|_\infty
<12\,\|p-1/2^5\|_\infty.
\tag{0.5}
\]

I use those bounds rather than re-proving the potential certificate.

### Last three B15 reports

The last three substantive account02/B15 reports were:

1. `20260922T050513Z-sector-kl-character-split`: a high-posterior sector KL pays a complete local Boolean class;
2. `20260922T054027Z-packet-price-kl-numaro`: exact magnitude-packet plus original-coordinate-price KL is indispensable on the near-extremal Numaro source;
3. `20260922T060159Z-bent-nearisoclinic-sector-obstruction`: a genuine Boolean bent-carrier family has **no** high-posterior sector and only `O(d^2)` vertical KL, so local information credit without child slack cannot be universal.

Thus the local sector implication itself did not remain unchanged: the third report rigorously killed it.  In any event the later owner convergence now forces a materially different mechanism on the same FEI target.  This run moves from a one-pivot Shannon cocycle to a **gate-global Gibbs reference law**, identifies the full negative information credit exactly, and applies it to the B-lead's strict prime reserve to obtain an explicit off-center theorem.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.  
**MECHANISM CHANGE:** `pivot-local sector KL / child-subsidy obstruction -> exact all-gate Gibbs KL + dyadic-support stability credit`.  
**TARGET-LEVEL CHANGE:** the B-lead's qualitative five-input prime neighborhood `epsilon_5>0` is made explicit as `epsilon_5=4.4e-6` for the current candidate.

## 1. The first missing Shannon implication in exact form

For an arbitrary nonconstant Boolean gate `G` at an interior product-bias vector `p`, let

\[
w(S)=\widehat G_p(S)^2,
\qquad
q=\Pr[G=-1],
\qquad
v=V_q=4q(1-q).
\tag{1.1}
\]

Thus `w` is the actual biased spectral law and

\[
w(\varnothing)=(1-2q)^2=1-v.
\tag{1.2}
\]

Put

\[
A_i:=\Gamma(p_i)+h_2(V_{p_i}),
\qquad
a_i:={A_i\over V_{p_i}},
\qquad
x_i:=2^{-a_i},
\qquad
Z:=\prod_i(1+x_i).
\tag{1.3}
\]

Define the product Gibbs law on spectral subsets

\[
\nu_p(S):={1\over Z}\prod_{i\in S}x_i.
\tag{1.4}
\]

Equivalently, its coordinates are independent Bernoulli variables with success probabilities `x_i/(1+x_i)`.

The gate defect is

\[
D_\Gamma(G;p)
=\sum_i a_i\operatorname{It}_i(G;p)-\Gamma(q)-H(w).
\tag{1.5}
\]

The first missing Shannon implication is therefore not an auxiliary scalar occurrence bound.  It is the exact source statement obtained below:

\[
\boxed{
D_{\rm KL,2}(w^+\|\nu_p^+)
\ge
\log_2{Z-1\over x_q},
}
\tag{1.6}
\]

where `w^+` and `nu_p^+` are conditioned on `S nonempty` and

\[
x_q:=2^{-[\Gamma(q)+h_2(V_q)]/V_q}.
\tag{1.7}
\]

Equation (1.6) is equivalent to the all-gate inequality for this source, not merely sufficient.  The point of the next two sections is that its entire KL term has a source-exact packet/original-coordinate sufficient statistic, and on the five-input prime center the B-lead's finite theorem supplies a strict positive excess which can be transported off center while retaining another negative KL credit.

## 2. Exact all-gate Gibbs-KL factorization

### Theorem 2.1 — full gate defect is conditional Gibbs relative entropy minus one partition demand

For every nonconstant Boolean gate, every interior product bias, and every symmetric potential `Gamma`,

\[
\boxed{
D_\Gamma(G;p)
=D_{\rm KL,2}(w\|\nu_p)-\log_2 Z-\Gamma(q).
}
\tag{2.1}
\]

Moreover, conditioning on the exact empty spectral atom gives

\[
\boxed{
D_\Gamma(G;p)
=v\left[
D_{\rm KL,2}(w^+\|\nu_p^+)
-\log_2{Z-1\over x_q}
\right].
}
\tag{2.2}
\]

In particular `(G)` is exactly equivalent to (1.6).

### Proof

Since

\[
\log_2{1\over\nu_p(S)}
=\log_2Z+\sum_{i\in S}a_i,
\]

expanding relative entropy gives

\[
D_{\rm KL,2}(w\|\nu_p)
=-H(w)+\log_2Z+\sum_i a_i\Pr_w(i\in S).
\]

The spectral marginal is precisely

\[
\Pr_w(i\in S)=\operatorname{It}_i(G;p),
\]

so (2.1) is exactly (1.5).

Now `nu_p(empty)=1/Z`, while (1.2) gives `w(empty)=1-v`.  Apply the KL chain rule through the event `S=empty`:

\[
D(w\|\nu_p)
=D_{\rm KL,2}\!\left(
\operatorname{Bern}(v)
\middle\|
\operatorname{Bern}\!\left({Z-1\over Z}\right)
\right)
+vD(w^+\|\nu_p^+).
\tag{2.3}
\]

A direct simplification of the binary term gives

\[
D_{\rm KL,2}\!\left(
\operatorname{Bern}(v)
\middle\|
\operatorname{Bern}\!\left({Z-1\over Z}\right)
\right)
-\log_2Z-\Gamma(q)
\]

\[
=-h_2(v)-v\log_2(Z-1)-\Gamma(q)
=v\log_2{x_q\over Z-1},
\tag{2.4}
\]

which proves (2.2). `QED`.

Constants have `v=0` and are the standard exact base cases; no division by `v` is needed for them.

This factorization preserves the whole relative-entropy credit.  It makes transparent why a credit-free normalizer estimate is the wrong target: the partition demand `log((Z-1)/x_q)` is allowed to be positive precisely when Boolean spectral dependence creates enough conditional KL to pay it.

## 3. The full KL is exactly packet + original-coordinate price information

For a nonempty spectral set `S`, define its Gibbs price

\[
L_x(S):=\prod_{i\in S}x_i,
\qquad
-\log_2L_x(S)=\sum_{i\in S}a_i.
\tag{3.1}
\]

This is an additive cost in the **original input coordinates**.  Also retain the physical spectral magnitude

\[
M(S):=|\widehat G_p(S)|.
\tag{3.2}
\]

Let

\[
T(S)=(M(S),L_x(S)).
\tag{3.3}
\]

### Theorem 3.1 — biased packet/price sufficiency

For every source above,

\[
\boxed{
D_{\rm KL,2}(w^+\|\nu_p^+)
= D_{\rm KL,2}(T_\#w^+\|T_\#\nu_p^+).
}
\tag{3.4}
\]

Indeed

\[
{w^+(S)\over\nu_p^+(S)}
={ (Z-1)|\widehat G_p(S)|^2
   \over v\prod_{i\in S}x_i},
\tag{3.5}
\]

so the likelihood ratio is constant on every fibre of `T`.  The conditional KL in the chain rule is therefore exactly zero.

This is the arbitrary-bias all-gate analogue of the preceding B15 packet/coordinate-price theorem.  It does **not** assume that physical magnitude projections are integral, and it does not change coordinates by an invariant linear transformation.  The only arithmetic object is the actual source magnitude; the price is the literal sum of original-coordinate costs `a_i`.

At uniform input bias all prices are equal, so `L_x(S)` depends only on the Fourier level `|S|`.  Off center it automatically refines level by the actual coordinate costs.  Thus the common gate residual (1.6) can be attacked using packet/price cells without discarding any negative relative entropy.

## 4. Strict five-input prime reserve imported from the B lead

Let `P` be an essential composition-prime five-input Boolean gate and let

\[
u=(1/2,\ldots,1/2).
\]

The B-lead report proves from account01/B17's rigorous finite certificate that every central equality case is a cube-automorphic read-once comparator.  Hence no essential prime is an equality case and

\[
D_{\Gamma^\dagger}(P;u)\ge\delta_5
=0.004906502214.
\tag{4.1}
\]

For the explicit tube below I deliberately weaken this to the decimal floor

\[
\boxed{D_{\Gamma^\dagger}(P;u)\ge\delta_0:=0.0049065.}
\tag{4.2}
\]

This is the named completed other-account theorem actually applied in the new argument, not merely cited.

The previous account03/B15 tube used only a much smaller universal central reserve obtained from the scalar-lift/Poincare lattice and therefore certified radius `10^-7` for all five-bit gates.  Prime classification exposes a reserve about twenty times larger.  The remaining issue is to transport that reserve without paying a generic Fannes loss that needlessly treats the central spectrum as an arbitrary 32-atom distribution.

## 5. New KL-preserving stability lemma for a five-bit Boolean spectrum

Let

\[
w^0(S)=\widehat P_u(S)^2,
\qquad
w(S)=\widehat P_p(S)^2,
\]

and let `a^0,a` be the corresponding vectors of signed Fourier coefficients.
Assume

\[
\varepsilon:=\|p-u\|_\infty\le4.4\times10^{-6}.
\tag{5.1}
\]

The source-valid transform estimate (0.5) gives

\[
\eta:=\|a-a^0\|_2<12\varepsilon.
\tag{5.2}
\]

Let

\[
J=\{S:w^0(S)>0\},
\qquad
\zeta=\sum_{S\notin J}w(S).
\tag{5.3}
\]

Since every old-zero coordinate of `a^0` contributes its entire perturbed amplitude to `a-a^0`,

\[
\boxed{\zeta\le\eta^2<144\varepsilon^2.}
\tag{5.4}
\]

If `zeta<1`, let `r` be `w` conditioned on `J`; if `zeta=0`, use the same definition without renormalization.  Five-bit Booleanity now gives a discrete fact that generic Fannes continuity does not use:

\[
\widehat P_u(S)=2^{-5}\sum_xP(x)\chi_S(x).
\]

The sum of 32 signs is even.  Hence every nonzero uniform Fourier coefficient has magnitude at least `2/32=1/16`, so

\[
\boxed{w^0(S)\ge1/256\quad(S\in J).}
\tag{5.5}
\]

Put

\[
\ell_S=\log_2{1\over w^0(S)}\in[0,8].
\]

The entropy difference on the surviving support has the **exact** negative-KL decomposition

\[
H(r)-H(w^0)
=\sum_{S\in J}(r_S-w^0_S)\ell_S
-D_{\rm KL,2}(r\|w^0).
\tag{5.6}
\]

Because the two coefficient vectors have norm one,

\[
\|w-w^0\|_1
\le\|a-a^0\|_2\|a+a^0\|_2
\le2\eta.
\tag{5.7}
\]

Also

\[
(1-\zeta)\|r-w^0\|_1
\le2\eta+\zeta.
\tag{5.8}
\]

Since the range of `ell` is at most eight and the signed mass difference sums to zero,

\[
\sum(r-w^0)\ell
\le8\,\operatorname{TV}(r,w^0)
=4\|r-w^0\|_1.
\tag{5.9}
\]

Finally split entropy according to `J` versus `J^c`.  The leakage conditional law has at most 32 atoms, so its entropy is at most five.  Combining (5.4)--(5.9) yields

\[
\boxed{
H(w)-H(w^0)
\le
8\eta+h_2(\zeta)+9\zeta
-(1-\zeta)D_{\rm KL,2}(r\|w^0).
}
\tag{5.10}
\]

This is the promised exact information-credit payment.  The term

\[
-(1-\zeta)D_{\rm KL,2}(r\|w^0)
\]

is retained with its correct sign: redistributing mass among already-present dyadic Fourier atoms can only make the dangerous entropy increase smaller by exactly this relative entropy.  New spectral atoms are paid separately by their genuinely quadratic amplitude leakage `zeta<=eta^2`; they are not charged a spurious linear Fannes cost.

Equation (5.10) is analytic and source-valid for every five-bit Boolean gate.  It is not a finite-grid observation.

## 6. Explicit prime-tube theorem

Set once and for all

\[
\boxed{\varepsilon_0=4.4\times10^{-6}.}
\tag{6.1}
\]

For a five-bit nonconstant truth table its uniform output mass is `m/32`, `1<=m<=31`.  Product total variation gives

\[
|p_{\rm out}(p)-p_{\rm out}(u)|\le5\varepsilon_0.
\]

Therefore the smaller output representative stays above

\[
{1\over32}-5\varepsilon_0
=0.031228>{1\over64},
\tag{6.2}
\]

so the inherited derivative bound (0.4) applies to every output encountered in the tube.

Write

\[
\alpha_i(p)={\operatorname{It}_i(P;p)\over V_{p_i}}.
\]

This is exactly the pivotal probability of coordinate `i` under the other four product-biased inputs.  Hence

\[
0\le\alpha_i\le1,
\qquad
|\alpha_i(p)-\alpha_i(u)|\le4\varepsilon_0.
\tag{6.3}
\]

Put

\[
A(t)=\Gamma^\dagger(t)+h_2(V_t).
\]

Inside this tiny central tube, `A(t)<8`.  Symmetry of `V_t` gives

\[
V_t=1-4(t-1/2)^2,
\qquad
h_2(V_t)=h_2(4(t-1/2)^2).
\]

Thus

\[
|A(t)-A(1/2)|
\le85\varepsilon_0+h_2(4\varepsilon_0^2).
\tag{6.4}
\]

Equations (6.3)--(6.4) give the input-price loss

\[
\left|
\sum_i\alpha_i(p)A(p_i)-
\sum_i\alpha_i(u)A(1/2)
\right|
\le585\varepsilon_0+5h_2(4\varepsilon_0^2).
\tag{6.5}
\]

The output-potential loss is at most

\[
425\varepsilon_0.
\tag{6.6}
\]

For the entropy term use (5.10) with `eta<12 epsilon_0`.  Let

\[
q_0=144\varepsilon_0^2,
\qquad
z_0=4\varepsilon_0^2.
\]

Both are below `1/2`, so binary entropy is increasing on the needed interval.  The elementary inequality

\[
h_2(t)\le t\log_2(e/t)
\tag{6.7}
\]

and `e<3` give rigorous convenient bounds.  The adjacent arithmetic check verifies

\[
2^{31}q_0>3,
\qquad
2^{36}z_0>3,
\]

hence

\[
h_2(\zeta)\le h_2(q_0)<31q_0,
\qquad
h_2(z_0)<36z_0.
\tag{6.8}
\]

Combining (5.10), (6.5), (6.6), and (6.8), while **retaining** the relative-entropy credit, gives

\[
\boxed{
D_{\Gamma^\dagger}(P;p)
\ge
D_{\Gamma^\dagger}(P;u)
-1106\varepsilon_0-6480\varepsilon_0^2
+(1-\zeta)D_{\rm KL,2}(r\|w^0).
}
\tag{6.9}
\]

The deterministic arithmetic is

\[
1106\varepsilon_0+6480\varepsilon_0^2
=0.00486652545280.
\tag{6.10}
\]

Using the deliberately weakened central floor (4.2),

\[
\delta_0-
(1106\varepsilon_0+6480\varepsilon_0^2)
=0.00003997454720>0.
\tag{6.11}
\]

Therefore:

### Theorem B15-GIBBS-KL-PRIME-TUBE

For every essential composition-prime five-input Boolean gate `P` and every interior product-bias vector satisfying

\[
\boxed{
\max_i|p_i-1/2|\le4.4\times10^{-6},
}
\tag{6.12}
\]

the current common candidate satisfies

\[
\boxed{
D_{\Gamma^\dagger}(P;p)
\ge
3.99745472\times10^{-5}
+(1-\zeta)D_{\rm KL,2}(r\|w^0)
>0.
}
\tag{6.13}
\]

The displayed decimal floor uses `delta_0=0.0049065`, not the slightly stronger certified `delta_5`.

This turns the B-lead's qualitative `epsilon_5>0` into a source-certified explicit radius.  It also enlarges the previous explicit all-gates center radius `10^-7` by a factor of 44 on the mathematically relevant **composition-prime** five-input frontier.  It does not assert that decomposable five-input gates are safe throughout this larger tube merely from their top-level biases: their prime factors can inherit off-center output biases, and the exact composition cocycle must be applied at those induced biases.

## 7. Exact remaining obligation

The full problem is still open.  The common universal implication remains (0.2).  What changes is the five-input adversarial region:

\[
\boxed{
\text{any five-input composition-prime falsifier must satisfy}
\quad
\max_i|p_i-1/2|>4.4\times10^{-6}.
}
\tag{7.1}
\]

The information-theoretic form of the remaining gate inequality is exactly

\[
\boxed{
D_{\rm KL,2}(w^+\|\nu_p^+)
\ge
\log_2{Z-1\over x_q},
}
\tag{7.2}
\]

with the entire left side recoverable from the actual packet/original-coordinate-price statistic `(M,L_x)`.  Thus the next B15 attack should not return to a high-posterior pivot sector.  It should lower-bound this **global packet/price Gibbs KL excess** outside the certified prime tube, or produce a genuine prime gate/bias source for which (7.2) fails.

Higher-arity composition-prime gates remain completely outside Theorem B15-GIBBS-KL-PRIME-TUBE.  No finite-dimensional tube theorem is promoted to unrestricted FEI.

## 8. Verification scope and privacy

`check_gibbs_kl_prime_tube.py` verifies only the deterministic decimal/rational inequalities used in (6.8)--(6.11):

- `epsilon_0=4.4e-6`;
- the conservative central floor `delta_0=0.0049065`;
- `q_0=2.78784e-9`, `z_0=7.744e-11`;
- `2^31 q_0>3`, `2^36 z_0>3`;
- the potential-output interval remains above `1/64`;
- total deterministic loss `0.00486652545280`;
- final reserve `0.00003997454720`.

Its output is `PASS`.  Those checks do not prove the analytic KL identities; Sections 2, 3, and 5 do.

This report contains only FEI mathematics, source-bound repository identifiers, and sanitized verification metadata.  It contains no credentials, scheduler identifiers, machine paths, unrelated private material, benchmark gold, raw transcripts, email/Drive action, public posting, paid/remote model calls, workflows, or permission changes.
