Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED**; GPT-6 / maximum was requested, but this runtime exposes no authenticated model/reasoning telemetry, so I do not claim otherwise. **NO MOVEMENT in the fixed metric: `1033 -> 1033`; exact covered set remains `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033}`; status PARTIAL / source OPEN. Methods used: #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #18 SAY IT IN ANOTHER LANGUAGE, #19 MAKE IT AN ALGORITHM.**

# R20 / I0100 — Legendre Mellin identities and a linear obstruction to the common-neighbor completion route

Run timestamp: 2026-09-17T06:49:52Z.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Canonical claim: `operations/claims/I0100.md`.  
Source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26, stable compilation arXiv:2603.29571.  
Tracked quantity: largest admissible prime with matching exact primal and dual certificates for the source-normalized one-localization theta quantity, retaining the complete exact-certified prime set.

## 1. State recovery, ownership, and current source check

I continued from the newest immutable R20 report

`runs/R20/2026-09-17T06-17-46Z_i0100_p1033_cocircuit_typical_c8f2d4.md`

rather than restarting. I reread `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, and the canonical claim `operations/claims/I0100.md`. The claim still gives R20 exclusive ownership of I0100 in the CLOSABLE OUTSIDE lane and explicitly excludes Conjecture 27 / two-localization, Conjecture 28 / degree-four SoS, and Conjecture 29 / Paley ETF-RIP.

The newest neighboring P04 report remains on I0101 / Conjecture 27, with exact-certified domain `{149,257,1009,4001,4013,4021}` and status PARTIAL / source OPEN. R12 has already handed off its former I0102 / Conjecture 28 assignment and subsequently moved through I0060 to another source target. No P04, R12, or C28 claim is imported here.

The primary Randomstrasse compilation and the current public Jig root were rechecked on 2026-09-17. Conjecture 26 is still posed as

\[
\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2},\qquad p\equiv1\pmod4,
\tag{1.1}
\]

and the public root is still OPEN. Magsino--Mixon--Parshall remains the published source for the circulant local-theta LP/dual. A bounded current search found no source-matching proof or refutation. This is a dated search result, not a worldwide novelty certificate.

The same public Jig currently records a separate sufficient route: complete the edge common-neighbor deviation matrix by arbitrary off-edge entries, and try to make its top eigenvalue `o(p)`. Its Statement 6 proves that such an `o(p)` completion would imply the desired upper half of (1.1), and Statement 18 names this as Hypothesis A. The work below shows that **Hypothesis A itself cannot hold**. This invalidates that sufficient route only; it does not refute Conjecture 26.

The preceding report proposed next methods #17/#20/#25. A history check showed #20 and #25 had already been used in earlier I0100 runs, so the current contract requires replacing them. The only section-B moves not previously used on I0100 were #17, #18, and #19; those are the three used here. After this run all thirty numbered moves have been exercised at least once.

---

## 2. Exact local arithmetic

Let `p = 1 mod 4` be prime, let `chi` be the quadratic character of `F_p`, and write

\[
Q=(\mathbb F_p^\times)^2,
\qquad n=|Q|=\frac{p-1}{2}.
\]

The one-localization `H=G_{p,1}` has vertex set `Q`; two vertices `u,v` are adjacent iff `chi(u-v)=1`. Fix a generator `alpha` of `Q` and identify `Q` with `Z_n` by `s -> alpha^s`. Its connection set is

\[
S=\{s\ne0:\chi(\alpha^s-1)=1\},
\qquad |S|=d=\frac{p-5}{4}.
\tag{2.1}
\]

For `x in F_p`, define the Legendre trace sum

\[
T(x):=\sum_{z\in\mathbb F_p}
\chi\bigl(z(z-1)(z-x)\bigr).
\tag{2.2}
\]

For `x in Q`, `x != 1`, and `chi(x-1)=1`, let `C(x)` be the number of common neighbors of `1` and `x` inside `H`. Expanding the three quadratic-character indicators, with the three half-weight corrections at `z=0,1,x`, gives the exact identity

\[
\boxed{
C(x)=\frac{p-15+T(x)}8.
}
\tag{2.3}
\]

Indeed

\[
\frac18\sum_z(1+\chi z)(1+\chi(z-1))(1+\chi(z-x))
=\frac{p-3+T(x)}8,
\]

because each of the three quadratic pair sums is `-1`; the left side counts each true common neighbor with weight one and the points `0,1,x` with weight `1/2`, hence subtraction of `3/2` gives (2.3).

Since

\[
\frac{d^2}{n}
=\frac{(p-5)^2}{8(p-1)}
=\frac{p-9}{8}+\frac{2}{p-1},
\]

the edge deviation used by the public common-neighbor completion route is

\[
\boxed{
e(x):=C(x)-\frac{d^2}{n}
=\frac{T(x)}8-c_p^{(0)},
\qquad
c_p^{(0)}:=\frac34+\frac{2}{p-1}.
}
\tag{2.4}
\]

Thus the edge data are literally a shifted Legendre-family Frobenius trace.

---

# 3. Method #17 — look for the numbers somewhere else: the Mellin transform is a Jacobi-sum square

The values `T(x)` are the negative Frobenius traces of the Legendre elliptic curves

\[
E_x:y^2=z(z-1)(z-x).
\]

The relevant transform is unexpectedly rigid.

## Theorem R20-MELLIN1 — exact multiplicative Mellin transform

For every multiplicative character `A` of `F_p^*`, extended by zero at zero in the standard way,

\[
\boxed{
\sum_{x\in\mathbb F_p^\times}A(x)T(x)
=J(A,\chi)^2,
}
\tag{3.1}
\]

where

\[
J(A,\chi)=\sum_{u\in\mathbb F_p^\times}A(u)\chi(1-u).
\]

### Proof

Swap the two sums in the left side. The `z=0` term vanishes, and for `z != 0`, after `x=zu`,

\[
\sum_{x\ne0}A(x)\chi(z-x)
=A(z)\chi(z)J(A,\chi).
\]

Multiplying by `chi(z(z-1))` removes `chi(z)^2`, so the outer sum is

\[
J(A,\chi)\sum_{z\ne0}A(z)\chi(z-1).
\]

Because `chi(-1)=1`, the remaining sum is again `J(A,chi)`. This proves (3.1). QED.

For `A=1` and `A=chi`, the Jacobi sum equals `-1`; for all other characters its modulus is `sqrt(p)`. Multiplicative Parseval therefore gives an exact global second moment:

\[
\sum_{x\ne0}T(x)^2
=\frac{2+(p-3)p^2}{p-1}
=p^2-2p-2.
\]

Since `T(0)=-1`,

\[
\boxed{
\sum_{x\in\mathbb F_p}T(x)^2=p^2-2p-1.
}
\tag{3.2}
\]

This is the first useful bridge to classical Jacobi-sum / Sidelnikov-sequence arithmetic. It also identifies exactly why the previous first-order sequence calculations kept returning Jacobi sums: the entire Legendre trace has a Jacobi-square Mellin spectrum.

### Prior-art boundary

Jacobi-sum formulae for correlations of Sidelnikov and generalized Legendre-Sidelnikov sequences are established literature; this run does not claim that general mechanism as new. More directly relevant is Katz's treatment of the Legendre sheaf in *Convolution and Equidistribution*: the Legendre sheaf is rank two, pure of weight one, with geometric monodromy `SL_2`; its symmetric square is pure of weight two with geometric monodromy `SO_3`; Kummer twists retain bounded conductor. Those facts give the uniform complete-sum estimates used below. The exact identity (3.1) is written out here because it is elementary and makes the route transparent.

---

# 4. Method #18 — say it in another language: an edge second moment from a single twisted Legendre moment

Let

\[
\mathcal E_p=
\{x\in\mathbb F_p:\chi(x)=\chi(x-1)=1\},
\]

which is exactly the set of multiplicative ratios representing local edges from `1`. Define

\[
U_p:=\sum_{x\in\mathbb F_p}\chi(x)T(x)^2.
\tag{4.1}
\]

The `S_3` symmetry of the Legendre parameter collapses all the edge-restriction bookkeeping to this one twisted moment.

First,

\[
T(1-x)=T(x),
\qquad
T(1/x)=\chi(x)T(x)\quad(x\ne0).
\tag{4.2}
\]

The first follows from `z -> 1-z`; the second from `z -> z/x`. Therefore `T(x)^2` is invariant under the six Möbius transformations of the Legendre parameter.

Let

\[
V_p:=\sum_x\chi(x)\chi(x-1)T(x)^2.
\]

The transformation `x -> x/(x-1)` is a bijection of `F_p\{1}` to itself, preserves `T^2`, and sends `chi(x)` to `chi(x)chi(x-1)`. The omitted point `x=1` contributes `T(1)^2=1`, so

\[
\boxed{V_p=U_p-1.}
\tag{4.3}
\]

Similarly `x -> 1-x` shows

\[
\sum_x\chi(x-1)T(x)^2=U_p.
\]

Expanding the exact edge indicator

\[
\frac14(1+\chi x)(1+\chi(x-1))
\]

and removing the spurious half-weights at `x=0,1` gives

\[
\boxed{
\sum_{x\in\mathcal E_p}T(x)^2
=\frac{p^2-2p-6+3U_p}{4}.
}
\tag{4.4}
\]

This is an exact count-the-same-quantity-two-ways identity, now expressed in the language of a single twisted Frobenius second moment.

Katz's Legendre-sheaf description gives

\[
\boxed{U_p=O(p^{3/2})}
\tag{4.5}
\]

with an absolute implied constant. Here is the precise weight argument. On `A^1\{0,1}`, if `Leg` denotes the rank-two Legendre sheaf, then `T(x)^2` is the trace of `Sym^2(Leg)` plus the determinant term `p`. The sheaf `Sym^2(Leg)` is geometrically irreducible, pure of weight two, with geometric monodromy `SO_3`. Tensoring it with the quadratic Kummer sheaf `L_chi(x)` remains geometrically nontrivial and of uniformly bounded conductor. Grothendieck--Lefschetz plus Deligne's weight bound therefore bounds the complete twisted trace sum by a constant times `p^(3/2)`; the determinant and singular-point corrections are only `O(p)`.

Combining (4.4) and (4.5),

\[
\boxed{
\sum_{x\in\mathcal E_p}T(x)^2
=\frac{p^2}{4}+O(p^{3/2}).
}
\tag{4.6}
\]

The same rank-two Legendre/Kummer argument gives

\[
\sum_{x\in\mathcal E_p}T(x)=O(p).
\tag{4.7}
\]

Using (2.4), the squared `l2` energy of the prescribed common-neighbor edge deviations is therefore

\[
E_p:=\sum_{x\in\mathcal E_p}e(x)^2
=\frac1{64}\sum_{x\in\mathcal E_p}T(x)^2+O(p)
\]

and hence

\[
\boxed{
E_p=\frac{p^2}{256}+O(p^{3/2}).
}
\tag{4.8}
\]

This is the first point where the constant `1/256` appears naturally: it is `1/4` from the density of the edge character class times `1/64` from the one-eighth Frobenius-trace normalization.

---

# 5. Method #19 — make it an algorithm: solve the best completion as a Fourier LP

The public Jig completion route permits arbitrary off-edge entries. Rather than guessing a completion, optimize over all of them.

Let `c_p^CN` denote the minimum possible largest eigenvalue among all real symmetric matrices `R` indexed by the vertices of `H` such that

1. `R_uu=0` for every vertex;
2. on every edge `uv`,
   \[
   R_{uv}=|N(u)\cap N(v)|-d^2/n;
   \]
3. off the edges, `R_{uv}` is unrestricted.

This is exactly the smallest `c` that can appear in the public common-neighbor completion implication.

## 5.1 Translation averaging loses nothing

Because `H` is Cayley, translating a feasible `R` by any element of `Z_n` produces another feasible matrix with the same spectrum. Averaging all translates preserves every forced edge value and the zero diagonal. Since `lambda_max` is convex,

\[
\lambda_{\max}(\overline R)
\le \lambda_{\max}(R).
\]

Therefore the optimum is attained by a **circulant** completion. Thus the apparently matrix-valued completion problem is exactly a finite Fourier linear program.

Let `b:Z_n -> R` be the fixed edge-data sequence

\[
b_0=0,
\qquad b_s=e(\alpha^s)\ (s\in S),
\qquad b_t=0\ (t\notin\{0\}\cup S),
\]

and let

\[
\beta_k=\sum_{s\in\mathbb Z_n}b_s e^{2\pi i ks/n}
\]

be its real Fourier transform. A circulant completion adds an arbitrary real-even sequence supported on the nonedge lags.

The primal LP is

\[
\min c
\quad\text{such that}\quad
\beta_k+\widehat x(k)\le c\quad\forall k,
\tag{5.1}
\]

with `x` supported on the free nonedge lags.

Its dual is the probability-moment problem

\[
\boxed{
 c_p^{CN}
 =\max\left\{
 \sum_k y_k\beta_k:
 y_k\ge0,\ \sum_k y_k=1,\
 \check y(t)=0\ \forall t\in N
 \right\},
}
\tag{5.2}
\]

where `N` is the nonedge-lag set. Real-even symmetrization may be imposed without changing the value. Finite-dimensional LP strong duality applies because the primal is feasible and bounded below by zero (every feasible completion has zero trace).

## 5.2 A universal dual witness

Because `b_0=0`,

\[
\sum_k\beta_k=0.
\]

Because the edge data are nonzero for large `p`, Parseval gives a nonzero Fourier vector, hence

\[
\beta_{\min}:=\min_k\beta_k<0.
\]

Set

\[
t_p=-\frac1{\beta_{\min}},
\qquad
 y_k=\frac{1+t_p\beta_k}{n}.
\tag{5.3}
\]

Then `y_k>=0` and `sum y_k=1`. Moreover inverse Fourier transformation gives

\[
\check y(t)=\mathbf1_{t=0}+t_p b_t,
\]

so it vanishes on every free nonedge lag. Thus (5.3) is dual feasible. Its objective is, by Parseval,

\[
\sum_k y_k\beta_k
=\frac{t_p}{n}\sum_k\beta_k^2
=t_p\sum_s b_s^2
=\frac{E_p}{-\beta_{\min}}.
\]

Therefore

\[
\boxed{
 c_p^{CN}\ge \frac{E_p}{-\beta_{\min}}.
}
\tag{5.4}
\]

This converts the whole completion question into two scalar estimates: the edge-data energy and one Fourier coefficient bound.

## 5.3 Uniform Fourier bound from the Legendre sheaf

Every character of the cyclic square subgroup `Q` extends to a multiplicative character `A` of `F_p^*`; the two extensions differ by `chi` and agree on `Q`. Expanding the exact edge indicator shows that every `beta_k` is a fixed linear combination of complete sums of the forms

\[
\sum_x A(x)T(x),
\quad
\sum_x A(x)\chi(x)T(x),
\quad
\sum_x A(x)\chi(x-1)T(x),
\quad
\sum_x A(x)\chi(x)\chi(x-1)T(x),
\tag{5.5}
\]

plus character sums without `T` and `O(1)` singular-point corrections.

The first two sums are explicitly `J(A,chi)^2`-type sums by (3.1), hence `O(p)`. The last two are complete trace sums of the rank-two Legendre sheaf or its quadratic twist, further tensored with a Kummer sheaf `L_A`. Katz's Legendre-family results give geometric `SL_2` monodromy and bounded conductor uniformly in the multiplicative character `A`; Deligne's theorem therefore gives an absolute constant `C` such that

\[
\boxed{
\max_k|\beta_k|\le Cp
}
\tag{5.6}
\]

for every admissible prime `p`. The character-only terms are also `O(p)` uniformly (and in nontrivial cases are only Jacobi-size `O(sqrt p)`).

Combining (4.8), (5.4), and (5.6) proves the main result of this run.

## Theorem R20-CNFAIL1 — the `o(p)` common-neighbor completion does not exist

There are absolute constants `kappa>0` and `p_0` such that for every prime `p = 1 mod 4`, `p>=p_0`,

\[
\boxed{
 c_p^{CN}\ge \kappa p.
}
\tag{5.7}
\]

### Proof

From (4.8), for all sufficiently large `p`, `E_p >= p^2/512`. From (5.6), `-beta_min <= Cp`. Substitute in (5.4):

\[
 c_p^{CN}\ge\frac{p^2/512}{Cp}
=\frac{p}{512C}.
\]

Take `kappa=(512C)^{-1}`. QED.

### Consequence for the current public route

The public Jig's Hypothesis A asks for completions with top eigenvalue at most `delta p` for every `delta>0` and all sufficiently large admissible primes; equivalently it requires

\[
 c_p^{CN}=o(p).
\]

Theorem R20-CNFAIL1 proves the negation:

\[
\boxed{
\liminf_{p\to\infty,\ p=1\bmod4}
\frac{c_p^{CN}}p\ge\kappa>0.
}
\tag{5.8}
\]

So the common-neighbor completion sufficient condition cannot prove the source asymptotic. Statements 3/5/6 on the public page remain correct implications; their hoped-for small-`c` premise fails.

This is **not** a refutation of Randomstrasse Conjecture 26. Hypothesis A was explicitly only sufficient, not necessary. The source remains OPEN.

---

## 6. What this teaches about the actual conjecture

The completion route fails for a structural reason, not for lack of a clever off-edge fill. The forced edge data already carry quadratic Frobenius-trace energy

\[
E_p\asymp p^2,
\]

while every multiplicative Fourier coefficient of that data is only `O(p)`. The positive dual witness (5.3) converts those two facts into a linear-in-`p` obstruction for **every** completion.

This also explains the numerically observed scale from earlier experimentation without using those floating computations as evidence: the correct completion scale is linear in `p`, so seeking `o(p)` was asking the free entries to cancel an amount of positive Fourier-cone mass that the edge data themselves prohibit.

The useful part for I0100 is the language transfer. The same positive-Fourier probability cone that appeared in R20's theta/Haar-factor duality reappears as the exact dual of the common-neighbor completion LP. The difference is that here an explicit first-order perturbation of uniform measure, (5.3), already witnesses a linear obstruction. For theta itself, the corresponding cone optimizer is much subtler and has mass of order `p^{-1/2}` at the distinguished frequency. Thus the completion route is now cleanly separated from the true source bottleneck.

A next source-valid attack should therefore return to the theta cone itself rather than trying to improve this second-moment completion.

---

## 7. Prior-art search and novelty boundary

Dated queries on 2026-09-17 covered:

- the stable Randomstrasse compilation / Conjecture 26 and current public Jig root;
- Magsino--Mixon--Parshall, *Linear programming bounds for cliques in Paley graphs*;
- Katz, *Convolution and Equidistribution*, Chapter 15 on the Legendre family and its Kummer twists;
- current hypergeometric / Legendre-family Frobenius moment literature;
- Jacobi-sum and Sidelnikov-sequence correlation literature;
- current work attached to the public common-neighbor completion route.

The general ingredients are classical: Jacobi sums, Legendre-family Frobenius traces, Kummer twists, Grothendieck--Lefschetz, Deligne weights, and finite LP duality. Katz explicitly records the rank-two pure-weight-one Legendre sheaf with geometric `SL_2` monodromy and the pure-weight-two symmetric square with `SO_3` monodromy. Sidelnikov correlation literature already uses Jacobi sums extensively. I therefore make **no novelty claim** for those mechanisms.

The bounded search did not locate the specific combination (5.2)--(5.8) ruling out the present public `c=o(p)` completion hypothesis, but a negative search is not a novelty certificate. Publication novelty remains UNVERIFIED.

---

## 8. Validation / exact-certification status

No new finite prime was promoted this run. The fixed metric remains `1033`, with the exact-certified set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033}`.

All finite-prime membership in that set continues to rely only on the previously archived exact primal/dual interval certificates. The new contribution is theorem-sized and its full argument is on this page; no floating SDP/LP output is used as a certificate or as part of Theorem R20-CNFAIL1.

Existing independent R20 audits remain:

- `R19-AUDIT-R20-I0100-P181-01 = PASS_EXACT_FINITE_CASE`;
- `R19-AUDIT-R20-I0100-P241-02 = PASS_EXACT_FINITE_CASE`;
- `R19-AUDIT-R20-I0100-TUR1-05 = PASS_ALGEBRAIC_CORE`.

None audits R20-CNFAIL1, the primes `317,601,661,1009,1021,1033`, or the source asymptotic. No closure audit is claimed.

---

## 9. Scheduler/model control boundary

The currently exposed task controls still provide title/prompt, schedule/timing, enabled state, and timing mode, but no native model-family field, no reasoning-effort field, no authenticated completed-run model telemetry, and no guaranteed full-hour execution setting. Consequently GPT-6/maximum remains a prompt request, not a verified native setting.

Actually forcing and verifying it would require a product/workspace scheduler or API surface exposing model + reasoning fields and completed-run telemetry, or an authorized platform-side intervention. The repository implementation record says the historical P26 `You cannot modify this task` error was ownership/context dependent and that a later authorized context succeeded. The legitimate workaround is the authorized owning context or platform support, not a duplicate schedule or a permission bypass. No scheduler change was attempted in this run.

---

## 10. `ledger_delta`

```yaml
ledger_delta:
  track: R20
  intake: I0100
  source: "Afonso S. Bandeira et al., Randomstrasse101 2025, Conjecture 26 — Paley one-localization"
  target: "vartheta(complement G_{p,1}) ~ sqrt(p/2), p = 1 mod 4 prime"
  metric: "largest admissible prime with matching exact primal/dual source-normalized theta certificates; preserve full exact-covered set"
  before: 1033
  after: 1033
  covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033]
  movement: "no movement"
  unchanged_count_before: 0
  unchanged_count_after: 1
  status: "PARTIAL / SOURCE OPEN"
  tried_moves: [17,18,19]
  new_claims:
    - "R20-MELLIN1: exact multiplicative Mellin transform sum A(x)T(x)=J(A,chi)^2"
    - "exact global second moment sum_x T(x)^2 = p^2-2p-1"
    - "exact edge second-moment reduction sum_edge T^2=(p^2-2p-6+3U_p)/4"
    - "R20-CNFAIL1: optimal common-neighbor completion has c_p^CN >= kappa p for all large admissible p, so public Hypothesis A c=o(p) is false"
  remaining_obligation: "prove the actual theta asymptotic; CNFAIL1 eliminates only a sufficient second-moment completion route and does not decide Conjecture 26"
  evidence:
    - "full proofs in this immutable report"
    - "Katz Legendre/Kummer monodromy + Deligne weight bounds for the uniform O(p) and O(p^(3/2)) trace estimates"
    - "prior exact primal/dual certificate artifacts through p=1033 retained unchanged"
  audits:
    - "R19-AUDIT-R20-I0100-P181-01=PASS_EXACT_FINITE_CASE"
    - "R19-AUDIT-R20-I0100-P241-02=PASS_EXACT_FINITE_CASE"
    - "R19-AUDIT-R20-I0100-TUR1-05=PASS_ALGEBRAIC_CORE"
    - "R20-CNFAIL1: no OTHER-track audit yet"
  closure: false
```

## 11. Next route

All thirty numbered section-B moves have now been used at least once on I0100. The next run should not manufacture another finite certificate merely to move the prime frontier. The strongest new obligation is to return to the exact theta/Haar-factor cone and exploit the Mellin identity (3.1) there: the completion LP failed because its forced data have macroscopic `l2` energy, while theta needs a positive measure with a distinguished atom on the `p^{-1/2}` scale. A useful fresh direction outside the now-exhausted numbered menu is to construct a **nonlinear Jacobi-square theta dual** whose positivity is automatic from a modulus square and whose edge Fourier coefficients cancel beyond first order.

**NO CLOSURE CLAIM.**