Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model or reasoning-effort receipt, so I do not claim GPT-6 / maximum. **NO MOVEMENT in the frozen exact-prime metric: `1213 -> 1213`; retained exact set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`; unchanged count `1 -> 2`; status PARTIAL / SOURCE OPEN. Section-B moves: second-pass #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #7 TAKE THE LIMIT, #10 DERANDOMIZE.**

# R20 / I0100 — exact log-stretch parameter, statistical dimension of the regular cone, and a fixed-margin derandomization target

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim: `operations/claims/I0100.md`.
Outside source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.

For `p = 1 mod 4`, put
\[
n=(p-1)/2.
\]
Let `Q` be the nonzero quadratic residues, choose a generator `alpha` of `Q`, and let
\[
S=\{d\in\mathbb Z_n\setminus\{0\}:\alpha^d-1\in Q\}.
\]
Then
\[
G_{p,1}=\operatorname{Cay}(\mathbb Z_n,S),
\qquad
T_p:=\vartheta(\overline{G_{p,1}}).
\]
The source target is
\[
T_p\sim\sqrt{p/2}=\sqrt{n+1/2},
\]
which is equivalent to `T_p ~ sqrt(n)`.

## 1. Recovery, ownership, and source gate

I continued from

`runs/R20/2026-09-17T16-04-11Z_i0100_selfdual_random_hierarchy_b7e2c4.md`

rather than restarting. I reread the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE state, the canonical I0100 claim, the new-methods deployment manifest, the newest R20 report, the newest neighboring Paley state I could recover, and targeted intake/claim material for I0100. The large root/intake files are connector-truncated, so this is a current-state plus exact-targeted dependency read, not a false claim that every unrelated byte of roughly 780 intake rows rendered in one response.

Ownership remains non-overlapping:

- I0100 / Conjecture 26 / one-localization belongs to R20;
- P04 / I0101 remains the distinct two-localization Conjecture 27; its newest report has frozen exact prime `4049` and source status OPEN / PARTIAL;
- R12 exhausted and handed off the distinct degree-four SoS I0102 target before rotating away;
- C28 / I0103 remains the distinct Paley-ETF / Conjecture 29 scope.

Fresh dated source check, 2026-09-17: the current public Jig #7 still labels the Conjecture-26 root **Open** and still asks whether the clique-bounding Lovasz theta of the Paley one-localization is asymptotic to `sqrt(p/2)`. The stable Randomstrasse compilation remains arXiv:2603.29571. A bounded current search found no source-matching resolution. This is dated negative search evidence, not a worldwide novelty certificate.

The exact finite frontier entering and leaving this run is
\[
\boxed{p_{\max}=1213}
\]
with the full exact-certified set
\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213\}}.
\]
I did **not** spend the run extending the prime table.

---

## 2. Starting point from the preceding run

Let
\[
H=\mathbf 1^\perp\subset\mathbb R^n,
\qquad m=\dim H=n-1.
\]
For a real subspace `E subset H`, the preceding R20 work uses the one-sided radial constant
\[
a_E=\min_{\substack{r\in E\\r_0=1}}
\left(-\min_{i>0}r_i\right).
\tag{2.1}
\]
If `F=E^perp` inside `H`, then for every `a>1/(n-1)`,
\[
a_E\ge a
\iff
F\cap\operatorname{pos}\{g_1(a),\ldots,g_m(a)\}\ne\{0\},
\tag{2.2}
\]
where
\[
g_i(a)=e_i+a e_0-\frac{1+a}{n}\mathbf1.
\tag{2.3}
\]
The Gram matrix is
\[
\langle g_i(a),g_j(a)\rangle
=\delta_{ij}+\tau(a),
\qquad
\tau(a)=\frac{(n-1)a^2-2a-1}{n}.
\tag{2.4}
\]
At
\[
a_*=\frac1{\sqrt n-1},
\]
we have `tau(a_*)=0`, so these generators form an orthonormal basis of `H`.

For the Paley complementary Fourier halves `N,S`, earlier exact identities give
\[
T_p=\frac{n a_N}{1+a_N}=1+\frac1{a_S}.
\tag{2.5}
\]
The preceding report also proved the exact complementary radial involution
\[
a_F=\frac{1+a_E}{(n-1)a_E-1}.
\tag{2.6}
\]

The previous run identified the self-dual orthant but still parameterized the neighborhood by `tau`. This run changes parameter before doing any further arithmetic.

---

## 3. #5 ADD A PARAMETER — an exact logarithmic stretch coordinate

Define, for every real `s`,
\[
\boxed{
a(s)=\frac{1+\sqrt n\,e^s}{n-1}.}
\tag{3.1}
\]
A direct substitution into (2.4) gives
\[
\boxed{
\tau(a(s))=\frac{e^{2s}-1}{n-1}=\frac{e^{2s}-1}{m}.
}
\tag{3.2}
\]
Thus `s=0` is exactly the self-dual orthant, not merely asymptotically.

### Theorem R20-STRETCH1 — exact rank-one stretch form

Under the orthonormal coordinate system on `H` given by the self-dual generators `g_i(a_*)`, the cone in (2.2) at `a=a(s)` is isometric to
\[
\boxed{
C_m(s)=A_s\mathbb R_+^m,
\qquad
A_s=I+(e^s-1)P,
\qquad
P=\frac1m\mathbf1\mathbf1^\top.
}
\tag{3.3}
\]
Equivalently, `A_s=e^{sP}`: it stretches exactly one direction, the diagonal direction, by `e^s` and leaves its orthogonal complement fixed.

#### Proof

The generator Gram matrix at (3.1) is
\[
I_m+\tau(a(s))J_m
=I_m+(e^{2s}-1)P.
\]
Since `P^2=P`,
\[
A_s^2
=I_m+(e^{2s}-1)P.
\]
Hence the columns of `A_s` have exactly the same Gram matrix as the regular-cone generators, proving the isometry. QED.

The diagonal stretch has an exact geometric meaning. At `s=0`,
\[
\frac1{\sqrt m}\sum_{i=1}^m g_i(a_*)
=\sqrt{\frac n{n-1}}
\left(e_0-\frac1n\mathbf1\right),
\]
so the stretched coordinate direction is precisely the normalized centered distinguished vertex.

### Exact theta coordinate

For the Paley `N`-half, solve (2.5) for
\[
a_N=\frac{T_p}{n-T_p}.
\]
Define its exact stretch coordinate `s_p` by `a_N=a(s_p)`. Then
\[
\boxed{
e^{s_p}=\frac{\sqrt n\,(T_p-1)}{n-T_p}.}
\tag{3.4}
\]
Equivalently,
\[
\boxed{
T_p=\sqrt n\,\frac{e^{s_p}\sqrt n+1}{e^{s_p}+\sqrt n}.
}
\tag{3.5}
\]
Therefore
\[
\boxed{
T_p/\sqrt n\to1
\iff
s_p\to0.
}
\tag{3.6}
\]
For bounded `s`, the ratio in (3.5) tends to `e^s`.

The complementary half has parameter exactly `-s_p`: (2.6) and (3.1) give
\[
\boxed{\mathfrak f(a(s))=a(-s).}
\tag{3.7}
\]
This is the clean form of complementarity that the previous `tau` parameter obscured.

If
\[
c=e^{2s}-1,
\]
then the earlier regular-cone correlation parameter is `tau=c/m`. Polarity is now exact:
\[
C_m(s)^\circ=-C_m(-s),
\tag{3.8}
\]
because `A_s^{-1}=A_{-s}` and the polar of the positive orthant is the negative orthant.

---

## 4. #7 TAKE THE LIMIT — statistical dimension of the rank-one-stretched orthant

Kabluchko--Zaporozhets call the same regular cone `C_m(r)` with generator Gram matrix `I_m+rJ_m`; their formulas apply here with
\[
r=\frac{e^{2s}-1}{m}.
\]
They compute all conic intrinsic volumes exactly. Instead of expanding their full alternating Crofton sum, the rank-one realization (3.3) makes the large-`m` statistical dimension almost one-dimensional.

Let
\[
\delta_m(s):=\delta(C_m(s))
=\mathbb E\|\Pi_{C_m(s)}G\|_2^2,
\qquad G\sim N(0,I_m).
\]
Put
\[
c=e^{2s}-1>-1,
\qquad
\phi(t)=\frac{e^{-t^2/2}}{\sqrt{2\pi}},
\qquad
Q(t)=\Phi(-t).
\]
Define
\[
\mu_1(t)=\mathbb E(Z-t)_+=\phi(t)-tQ(t),
\qquad Z\sim N(0,1).
\]

### Theorem R20-STATDIM1 — scalar limit for the regular cone

For every fixed real `s`, there is a unique real `t_s` satisfying
\[
\boxed{
t_s=c\,\mu_1(t_s)
=(e^{2s}-1)\bigl(\phi(t_s)-t_sQ(t_s)\bigr).
}
\tag{4.1}
\]
Moreover
\[
\boxed{
\frac{\delta_m(s)}m\longrightarrow Q(t_s)=\Phi(-t_s).
}
\tag{4.2}
\]
The limit obeys the exact dual symmetry
\[
\boxed{
Q(t_{-s})=1-Q(t_s),
\qquad t_{-s}=-t_s.
}
\tag{4.3}
\]
Near the self-dual point,
\[
\boxed{
\frac{\delta_m(s)}m
\longrightarrow
\frac12-\frac{s}{\pi}+O(s^2)
\quad(s\to0).
}
\tag{4.4}
\]

#### Proof

Write `A_s=I+alpha P`, `alpha=e^s-1`, and let `G` be standard Gaussian. Projection onto `A_s R_+^m` is equivalent to minimizing
\[
\frac12\|G-A_sx\|_2^2
\quad\text{over }x\ge0.
\]
Since
\[
A_s^2=I+cP=I+\frac cmJ,
\]
the KKT equations give
\[
\boxed{
x_i=(B_i-t_m)_+,}
\tag{4.5}
\]
where
\[
B=A_sG,
\qquad
B_i=G_i+\alpha\bar G,
\qquad
\bar G=\frac1m\sum_iG_i,
\]
and
\[
\boxed{
t_m=c\,\frac1m\sum_i(B_i-t_m)_+.}
\tag{4.6}
\]
For `c>-1`, the scalar function
\[
h_m(t)=t-c\,m^{-1}\sum_i(B_i-t)_+
\]
is strictly increasing: wherever differentiable,
\[
h_m'(t)=1+c\,m^{-1}\#\{i:B_i>t\}\ge\min(1,1+c)>0.
\]
Hence (4.6) has a unique root.

Almost surely `bar G -> 0`, and the empirical law of the `B_i` converges to `N(0,1)`. The roots therefore converge to the unique root of (4.1); uniqueness follows similarly because
\[
\frac d{dt}\{t-c\mu_1(t)\}=1+cQ(t)>0.
\]

Now
\[
\|A_sx\|_2^2
=x^\top(I+cP)x
=\sum_i x_i^2+\frac c m\left(\sum_i x_i\right)^2.
\]
Dividing by `m` and taking the empirical limit yields
\[
\frac1m\|\Pi_{C_m(s)}G\|_2^2
\to
\mu_2(t_s)+c\mu_1(t_s)^2,
\tag{4.7}
\]
where
\[
\mu_2(t)=\mathbb E(Z-t)_+^2
=(1+t^2)Q(t)-t\phi(t).
\]
Because `t_s=c\mu_1(t_s)`,
\[
\mu_2(t_s)+c\mu_1(t_s)^2
=\mu_2(t_s)+t_s\mu_1(t_s)
=Q(t_s).
\]
The projection norm is bounded by `||G||`, giving uniform integrability after normalization, so expectations converge and (4.2) follows.

For (4.3), polarity (3.8) gives the finite identity
\[
\delta_m(s)+\delta_m(-s)=m.
\]
Equivalently, if `c'=e^{-2s}-1=-c/(1+c)`, then `mu_1(-t)=mu_1(t)+t`; substituting `t=c mu_1(t)` shows that `-t` solves the equation for `c'`.

Finally, `t_s=2\phi(0)s+O(s^2)` and `Q(t)=1/2-\phi(0)t+O(t^3)`, yielding (4.4). QED.

### An exact finite-dimensional slope check from Kabluchko--Zaporozhets

This limit has a proof-independent exact check. Kabluchko--Zaporozhets give the intrinsic volumes
\[
v_k(C_m(r))
=\binom mk
 g_k\!\left(-\frac r{1+kr}\right)
 g_{m-k}\!\left(\frac r{1+kr}\right),
\tag{4.8}
\]
and their differential identity gives
\[
\frac{g_j'(0)}{g_j(0)}=\frac{j(j-1)}\pi.
\]
At `r=0`, `v_k=2^{-m} binom(m,k)`. Differentiating (4.8), summing `k v_k`, and using binomial moments gives
\[
\left.\frac{d}{dr}\delta(C_m(r))\right|_{r=0}
=-\frac{m(m-1)}{2\pi}.
\]
Since `r(s)=(e^{2s}-1)/m`,
\[
\boxed{
\delta_m'(0)=-\frac{m-1}{\pi}.
}
\tag{4.9}
\]
This exactly matches the limiting slope in (4.4).

### Random half-dimensional consequence

Let `L_m` be a Haar-random subspace of `R^m` with `dim(L_m)/m -> 1/2`. The approximate conic kinematic theorem of Amelunxen--Lotz--McCoy--Tropp says that random cone/subspace intersection has transition width of order `sqrt(m)` in statistical dimension. From (4.2), for every fixed `s>0`,
\[
\delta_m(s)=m\{Q(t_s)+o(1)\}<m/2-\Omega_s(m),
\]
whereas for fixed `s<0` it is above `m/2` by `Omega_s(m)`. Therefore
\[
\boxed{
\Pr[L_m\cap C_m(s)\ne\{0\}]\to
\begin{cases}
0,&s>0,\\
1,&s<0.
\end{cases}
}
\tag{4.10}
\]
At `s=0`, the preceding report's Wendel computation gives the critical probability asymptotic to `1/2` (with the known parity correction).

Equation (4.9) also shows the **natural random transition scale**: changing `s` by `Theta(m^{-1/2})` moves statistical dimension by `Theta(sqrt(m))`. Since
\[
\tau(s)=\frac{e^{2s}-1}{m},
\]
this corresponds to `tau=Theta(m^{-3/2})`, much narrower than the `Theta(1/m)` fixed-ratio scale.

I do **not** claim an exact limiting crossover law at `s=lambda/sqrt(m)` here; obtaining that would require a uniform second-order analysis of the Kabluchko--Zaporozhets formula or a sharper conic CLT. What is proved above is the fixed-`s` zero-one law and the exact slope.

---

## 5. What this changes about the strategy

The preceding report said the right comparison was a critical-window universality statement. The rank-one/statistical-dimension calculation shows that this was stronger than necessary for the source.

For bounded theta ratio `x=T_p/sqrt(n)`, (3.5) gives asymptotically
\[
s_p=\log x+o(1),
\]
while
\[
(n-1)\tau(a_N)=e^{2s_p}-1=x^2-1+o(1).
\]
Thus any fixed failure of the source, `x -> x_0 != 1`, corresponds to a **fixed nonzero log-stretch `s=log x_0`**, not to the narrow random critical window.

The random model then has a linear-in-`m` statistical-dimension gap by (4.2). So a deterministic proof does not need to reproduce the random `m^{-1/2}` crossover or decide the critical sign. It only has to rule out every fixed nonzero stretch.

That is a materially weaker transfer target.

---

## 6. #10 DERANDOMIZE — exact fixed-margin Paley criterion

For each Paley half `Z in {N,S}`, let `E_Z subset H` be the corresponding Fourier subspace and `F_Z=E_Z^perp`. Use the self-dual orthonormal coordinates from Theorem R20-STRETCH1.

Because `a(s)` is strictly increasing,
\[
a_Z\ge a(s)
\iff
F_Z\cap C_m(s)\ne\{0\}.
\tag{6.1}
\]
The two Paley thresholds are `s_p` and `-s_p` by (3.7).

### Theorem R20-FIXEDMARGIN1 — source conjecture as two fixed-margin nonintersection statements

The following are equivalent:

1. `T_p/sqrt(n) -> 1` along primes `p=1 mod 4`;
2. `s_p -> 0`;
3. for every fixed `epsilon>0`, for all sufficiently large admissible primes,
   \[
   \boxed{
   F_N\cap C_m(\epsilon)=\{0\},
   \qquad
   F_S\cap C_m(\epsilon)=\{0\}.
   }
   \tag{6.2}
   \]

#### Proof

(1) iff (2) is (3.6). For `Z=N`, the radial threshold is `s_p`; for `Z=S`, it is `-s_p`. Since (6.1) holds exactly and `a(s)` increases strictly, (6.2) says
\[
s_p<\epsilon,
\qquad
-s_p<\epsilon.
\]
For every fixed positive epsilon this is equivalent to `|s_p|->0`. QED.

This has a useful strict-separation form. By Gordan--Stiemke, since `C_m(epsilon)=A_epsilon R_+^m`,
\[
F_Z\cap C_m(\epsilon)=\{0\}
\]
is equivalent to the existence of a vector `h_Z in E_Z` with
\[
\boxed{A_\epsilon h_Z>0\quad\text{coordinatewise}.}
\tag{6.3}
\]
Because
\[
A_\epsilon h=h+(e^\epsilon-1)\bar h\,\mathbf1,
\]
where `bar h=m^{-1}sum h_i`, any such separator has positive mean. Normalizing `bar h=1`, (6.3) becomes the fixed-floor problem
\[
\boxed{
\min_i h_Z(i)>-(e^\epsilon-1).
}
\tag{6.4}
\]

Therefore Conjecture 26 can be proved without a critical-window universality theorem by constructing, for **each fixed epsilon>0**, one mean-one vector in each of the two transformed Paley Fourier halves whose floor beats the fixed negative constant `-(e^epsilon-1)`.

This is still nontrivial, but it is strictly more forgiving than reproducing Haar behavior at scale `s=O(m^{-1/2})`. It asks for two fixed-margin separators, not RIP, not all sparse vectors, and not an exact sign at the random critical point.

The old all-prime `sqrt(p)`-scale certificate corresponds asymptotically to `s=log(sqrt(2))`; viewed through (6.4), the previous factor-`sqrt(2)` barrier says precisely that the known explicit separator machinery has not yet pushed this fixed floor all the way from `epsilon > log(sqrt(2))` to arbitrary `epsilon>0`.

The earlier Jacobi-arcsine obstruction also fits this interpretation: a scalar/affine one-point profile cannot perform that continuation. The separator must use the genuinely dense nonlinear/transverse information isolated in the later R20 reports.

---

## 7. What was tried and what failed this run

### #5 ADD A PARAMETER

**Worked.** The logarithmic stretch `s` diagonalizes complementarity exactly, gives the exact rank-one cone `A_s R_+`, and turns the source into `s_p -> 0`.

### #7 TAKE THE LIMIT

**Worked.** The statistical dimension has the scalar limit (4.2), with exact polarity and exact slope `-(m-1)/pi` at the orthant. This proves the random half-dimensional model is robustly on the correct side for every fixed nonzero `s`.

### #10 DERANDOMIZE

**Partial but useful.** The random result does not itself transfer to the deterministic Paley orientation. What it does do is remove an unnecessarily strong obligation: we do **not** need critical-window universality. R20-FIXEDMARGIN1 reduces the source to two fixed-margin positive-separator constructions for every fixed epsilon.

I also tested the most obvious attempted derandomization conceptually: take the random projection KKT solution `(B_i-t)_+` and replace the Gaussian coordinates by a scalar function of the Paley one-point Jacobi coordinate. That collapses back to the scalar balanced-profile family already shown numerically and analytically to be insufficient (the affine/ReLU endpoint reproduces the old barrier, while fixed low polynomial degree stays well below the full radial optimum). I therefore did not spend validation budget on another scalar-profile numerical script.

The remaining obligation is genuinely vectorial: construct the two separators in (6.3)/(6.4), presumably by using joint Paley Fourier/Jacobi information rather than any one-coordinate profile.

---

## 8. Prior-art boundary and dated searches

Dated searches on 2026-09-17 included variants of

- `Randomstrasse Conjecture 26 Paley one localization theta sqrt p/2`;
- `Kabluchko Zaporozhets absorption probabilities Gaussian polytope regular spherical simplex p_n_d sigma`;
- `statistical dimension regular simplicial cone equicorrelated Gram matrix`;
- `contracted orthant statistical dimension` / `extended orthant statistical dimension`;
- `Amelunxen Lotz McCoy Tropp approximate kinematic formula statistical dimension`;
- `perceptron capacity half dimension positive orthant margin`.

Relevant established results recovered:

1. Kabluchko--Zaporozhets, *Absorption probabilities for Gaussian polytopes and regular spherical simplices*, Adv. Appl. Probab. 52 (2020), 588--616. They explicitly define the regular cone with Gram matrix `I+rJ`, call `r<0` / `r>0` contracted / extended orthants, compute all intrinsic volumes, and express the Gaussian-polytope non-absorption probability by Crofton sums.
2. Amelunxen--Lotz--McCoy--Tropp, *Living on the edge: phase transitions in convex programs with random data*, Information and Inference 3 (2014), 224--294. Statistical dimension controls the location and `sqrt(m)`-scale width of random conic intersection transitions.
3. Baryshnikov--Vitale / Wendel / Kabluchko--Zaporozhets already underlie the preceding R20 random-projection comparison.

Thus I make **no novelty claim** for regular simplicial cones, contracted/extended orthants, statistical dimension, conic kinematic phase transitions, or the Gaussian-polytope formula. The R20 contribution recorded here is a candidate synthesis/application: the exact Paley theta log-stretch (3.4), its rank-one regular-cone form, the scalar statistical-dimension limit derived above, and especially the fixed-margin derandomization reduction (6.2)--(6.4). A bounded search did not locate this exact chain; that absence is not a novelty certificate.

---

## 9. Validation / audits / metric bookkeeping

No new code was written. This was intentional: the work is theorem-sized analytic reduction, and the owner directive says to write the idea before code and avoid manufacturing checker output when the frozen metric does not move.

The new claims

- `R20-STRETCH1`,
- `R20-STATDIM1`,
- `R20-FIXEDMARGIN1`

have complete arguments on this page but are **SELF_CHECK_ONLY** pending OTHER-track audits.

Finite exact evidence is preserved. In addition to the earlier 2/2 outside-audited `p=181` and `p=241` packages, P26 has now independently reconstructed the exact `p=41` theorem and records

`P26-AUDIT-R20-I0100-P41-FOURIER-DUAL-ENDTOEND-24 = PASS_FULL_FINITE_PROOF / CLAIM_SCOPED / SOURCE_PARTIAL_OPEN`

with distinct R19 audit

`R19-AUDIT-R20-I0100-P41-01 = PASS`

and reconciliation

`P26-RECONCILE-R20-I0100-P41-2OF2-24 = PASS`.

That strengthens finite audit coverage but does not audit or close the asymptotic source.

---

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R20
  source: "Afonso S. Bandeira et al., Randomstrasse101 (2025), Conjecture 26 / I0100"
  source_target: "theta(complement G_{p,1}) ~ sqrt(p/2)"
  graph_normalization: "G_{p,1}=Cay(Z_n,S), n=(p-1)/2, S={d != 0: alpha^d-1 is a nonzero square}"
  metric: "largest admissible prime with matching exact primal/dual source-normalized theta certificates"
  metric_before: 1213
  metric_after: 1213
  covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
  status: PARTIAL
  source_status: OPEN
  unchanged_count_before: 1
  unchanged_count_after: 2
  tried_moves: [5,7,10]
  move_results:
    5: "R20-STRETCH1: exact log-stretch s with a(s)=(1+sqrt(n)e^s)/(n-1); regular cone is rank-one stretch A_s R_+ and complementarity is s -> -s"
    7: "R20-STATDIM1: for fixed s, delta(C_m(s))/m -> Phi(-t_s), t_s=(e^{2s}-1)E(Z-t_s)_+; exact slope delta_m'(0)=-(m-1)/pi and random fixed-s intersection has a zero-one law"
    10: "R20-FIXEDMARGIN1: source is equivalent to fixed positive-s nonintersection for BOTH complementary Paley halves for every epsilon>0; by Gordan this is two mean-one fixed-floor separator constructions"
  remaining_obligation: "for every fixed epsilon>0, construct strict positive separators A_epsilon h_N>0 and A_epsilon h_S>0 in the two transformed Paley Fourier halves; equivalently force |s_p|<epsilon and hence s_p->0"
  evidence:
    - "full written proofs R20-STRETCH1, R20-STATDIM1, R20-FIXEDMARGIN1 on this report page"
    - "Kabluchko-Zaporozhets exact regular-cone/intrinsic-volume formulas used for independent finite-dimensional slope check"
    - "Amelunxen-Lotz-McCoy-Tropp approximate kinematic theorem for the random fixed-s phase conclusion"
  audit_ids:
    - "R19-AUDIT-R20-I0100-P181-01=PASS_EXACT_FINITE_CASE"
    - "P26-AUDIT-R20-I0100-P181-FOURIER-DUAL-ENDTOEND-18=PASS_FULL_FINITE_PROOF"
    - "P26-RECONCILE-R20-I0100-P181-2OF2-18=PASS"
    - "R19-AUDIT-R20-I0100-P241-02=PASS_EXACT_FINITE_CASE"
    - "P26-AUDIT-R20-I0100-P241-FOURIER-DUAL-ENDTOEND-22=PASS_FULL_FINITE_PROOF"
    - "R19-AUDIT-R20-I0100-P41-01=PASS"
    - "P26-AUDIT-R20-I0100-P41-FOURIER-DUAL-ENDTOEND-24=PASS_FULL_FINITE_PROOF"
    - "P26-RECONCILE-R20-I0100-P41-2OF2-24=PASS"
  new_claim_audit_state: SELF_CHECK_ONLY
```

---

## 11. Next methods

The next run should not chase another prime or another scalar polynomial profile. The most direct continuation is a fixed-margin separator construction.

Use second-pass methods:

- **#19 MAKE IT AN ALGORITHM:** build an iterative correction that starts from the known `s > log(sqrt(2))` separator and decreases `s`, enforcing positivity after each dense Fourier correction.
- **#21 ASK WHO ELSE HAS THIS SHAPE:** compare (6.3) to deterministic/perceptron positive-dependence margins and discrepancy-style vector balancing, looking specifically for one-vector fixed-floor theorems rather than full RIP.
- **#29 ADD THE POINTS AT INFINITY:** compactify the normalized separator feasible set (`mean=1`) and characterize the first boundary face hit as `s downarrow 0`; the limiting support/sign pattern may expose the missing invariant.

If the frozen metric also fails to move on the next run, the unchanged streak will reach three and the following run must obey the section-I stuck protocol rather than produce another lemma on the same route.

---

## 12. Model / scheduler control limitation

The repository's current deployment manifest still records the same product limitation: the exposed scheduler surface has prompt/title, schedule/timing, enabled state, and timing mode, but **no native model-family selector, no reasoning-effort selector, no authenticated completed-run model-routing receipt, and no guaranteed full-hour execution field**. GPT-6 / maximum therefore remains prompt-only.

The historical P26 `You cannot modify this task` event was an ownership/context boundary. The deployment record says P26/P04 were not editable in that native census, while later repository receipts show successful modification from another authorized context. The legitimate fix is an authorized owning product/workspace context or a platform/API surface that actually exposes model/reasoning controls; no duplicate task, permission bypass, or scheduler change was attempted here.

**NO CLOSURE CLAIM.**