Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model/reasoning telemetry and the scheduler interface exposes no native model or reasoning selector, so I do not claim otherwise. **NO MOVEMENT in the fixed metric: `1061 -> 1061`; exact covered set remains `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061}`; status PARTIAL / source OPEN. Methods used: second-pass #3 PROVE SOMETHING STRONGER, #7 TAKE THE LIMIT, #24 FIND THE EXTREMAL OBJECT.**

# R20 / I0100 — exact fractional tiling and a one-sided Chebyshev formulation

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim: `operations/claims/I0100.md`.
Outside source: Afonso S. Bandeira, *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.
Tracked quantity: largest admissible prime with matching exact primal/dual certificates for the source-normalized one-localization theta quantity, preserving the complete exact-certified prime set.

## 1. State recovery, source gate, ownership, and audit changes

I continued from

`runs/R20/2026-09-17T09-29-00Z_i0100_p1061_saturated_defect_a91f6c.md`

rather than restarting. I reread/recovered the required campaign and root state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical I0100 claim, the newest own report, and current neighboring Paley ownership/history. The large intake corpus cannot be rendered byte-for-byte through the bounded connector, so I used the canonical exact-ID claim plus targeted repository searches; I do not pretend that a truncated connector response was a literal reread of every intake row.

The live Randomstrasse Paley page was reopened on 2026-09-17. It still defines `G_{p,1}` as the induced graph on the neighbors of zero, notes that the graph is circulant so the theta SDP reduces to an LP, and states Conjecture 26

\[
T_p:=\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}
\qquad(p\equiv1\pmod4).
\]

The same source still separately lists Conjecture 27 (two-localization), Conjecture 28 (degree-four SoS), and Conjecture 29 (Paley ETF/RIP). None is imported here. The current public Jig for this exact one-localization target is also still marked OPEN. A bounded 2026-09-17 literature search found no later primary source-matching proof or refutation. This is negative search evidence, not a novelty certificate.

Neighbor state remains separated. P04/I0101 is the distinct two-localization target and its newest visible state is a stuck-recovery report at exact finite frontier `p=4021`; R12 has already handed off former I0102/Conjecture 28 and is now on another canonical claim; the legacy C28 ETF scope is Conjecture 29, not I0100.

There is one useful audit update. P26 has now independently reconstructed the source-normalized `p=181` Fourier primal/dual proof and records

`P26-AUDIT-R20-I0100-P181-FOURIER-DUAL-ENDTOEND-18 = PASS_FULL_FINITE_PROOF / CLAIM_SCOPED / SOURCE_PARTIAL_OPEN`.

Together with the earlier distinct R19 verdict

`R19-AUDIT-R20-I0100-P181-01 = PASS_EXACT_FINITE_CASE`,

the **finite `p=181` theorem** now has two genuinely independent OTHER-track proof audits. P26 records `P26-RECONCILE-R20-I0100-P181-2OF2-18 = PASS`. This does not audit any later prime, any theorem below, or the asymptotic source conjecture.

The exact finite frontier therefore stays

\[
\boxed{p_{\max}=1061},
\]

with covered set

\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061\}}.
\]

I did not spend this run manufacturing a new finite certificate. The new work is structural.

All thirty Section-B moves have already been used at least once in earlier I0100 runs, so a literal never-before-used triple no longer exists. The preceding run used second-pass `#12/#18/#20`; this run follows its recorded next triple `#3/#7/#24`.

---

## 2. Exact starting point: the two complementary theta probability cones

Put

\[
n=\frac{p-1}{2},\qquad H=G_{p,1}=\operatorname{Cay}(\mathbb Z_n,S),
\]

where `S` is the nonzero localized-edge difference set and

\[
N=\mathbb Z_n\setminus(\{0\}\cup S).
\]

For admissible primes, `|S|=n/2-1` and `|N|=n/2`.

The preceding R20 reductions give the exact complementary moment programs

\[
\mathcal M_N=\left\{\mu\ge0:\sum_x\mu_x=1,\ \widehat\mu(t)=0\ (t\in N)\right\},
\]

\[
\mathcal M_S=\left\{\nu\ge0:\sum_x\nu_x=1,\ \widehat\nu(s)=0\ (s\in S)\right\},
\]

with

\[
\boxed{\max_{\mu\in\mathcal M_N}\mu_0=\frac{T_p}{n}},
\qquad
\boxed{\max_{\nu\in\mathcal M_S}\nu_0=\frac1{T_p}}.
\tag{2.1}
\]

Choose optimal `mu,nu` and reflection-average them. Complementary Fourier zero sets give

\[
\boxed{\mu*\nu=U_n},
\tag{2.2}
\]

where `U_n(x)=1/n`. At zero, the term `x=0` alone contributes

\[
\mu_0\nu_0=\frac{T_p}{n}\frac1{T_p}=\frac1n=(\mu*\nu)(0).
\]

All summands are nonnegative, so reflection symmetry gives

\[
\boxed{\mu(x)\nu(x)=0\qquad(x\ne0).}
\tag{2.3}
\]

This was the Haar-factor input behind the previous saturated-majorant theorem.

---

## 3. Method #3 — prove something stronger: the theta optimizer is an exact fractional factorization of the cyclic group

The new point is that optimality and translation invariance force a much stronger normalization than was used previously.

### Lemma R20-TILE0 — the distinguished atom is the largest atom

For every optimal `mu` in `M_N`,

\[
\mu(x)\le\mu(0)\qquad\forall x\in\mathbb Z_n.
\tag{3.1}
\]

The same holds for an optimal `nu` in `M_S`.

#### Proof

Translation preserves nonnegativity, total mass, and every prescribed Fourier zero: translation only multiplies each Fourier coefficient by a phase. If some `mu(x)>mu(0)`, translating `x` to zero would produce another feasible probability whose zero atom is larger than the optimum in (2.1), contradiction. The argument for `nu` is identical. QED.

Now scale the two optimal factors by their maximal atoms:

\[
f=\frac{\mu}{\mu_0}=\frac n{T_p}\mu,
\qquad
h=\frac{\nu}{\nu_0}=T_p\nu.
\tag{3.2}
\]

### Theorem R20-TILE1 — exact complementary fractional tiling

The canonical pair `(f,h)` obeys all of the following identities:

\[
\boxed{0\le f,h\le1,\qquad f(0)=h(0)=1,}
\tag{3.3}
\]

\[
\boxed{f(x)h(x)=\delta_0(x),}
\tag{3.4}
\]

\[
\boxed{(f*h)(x)=1\qquad\forall x\in\mathbb Z_n,}
\tag{3.5}
\]

\[
\boxed{\widehat f|_N=0,\qquad \widehat h|_S=0,}
\tag{3.6}
\]

and

\[
\boxed{\sum_x f(x)=\frac n{T_p},\qquad \sum_xh(x)=T_p.}
\tag{3.7}
\]

Conversely, suppose nonnegative `f,h` satisfy `f(0)=h(0)=1`, the Fourier constraints (3.6), and the exact convolution identity (3.5). Then, after normalizing each to total mass one, the two resulting probability measures are optimal in (2.1), and necessarily

\[
\boxed{\left(\sum f\right)\left(\sum h\right)=n,
\qquad T_p=\sum h=\frac n{\sum f}.}
\tag{3.8}
\]

If in addition (3.4) holds, they are exactly a complementary-support optimal pair of the kind constructed above.

#### Proof

Equation (3.3) is Lemma R20-TILE0 after scaling. Equation (3.4) follows from (2.3), including the value one at zero. Equation (3.5) follows from (2.2) and

\[
\frac1{\mu_0\nu_0}=n:
\qquad f*h=n(\mu*\nu)=1.
\]

The Fourier constraints and masses are immediate from the definitions.

Conversely put

\[
A=\sum f,\qquad B=\sum h.
\]

Summing (3.5) over the group gives `AB=n`. The probability measures `mu=f/A` and `nu=h/B` are feasible in `M_N` and `M_S`, respectively, with

\[
\mu_0=1/A=B/n,
\qquad
\nu_0=1/B.
\]

By (2.1),

\[
B/n\le T_p/n,
\qquad
1/B\le1/T_p.
\]

The two upper bounds multiply to `1/n`, while the two left sides also multiply to `1/n`; hence both inequalities are equalities. Thus `B=T_p` and `A=n/T_p`. QED.

This is stronger than the scalar defect formula: the theta optimum is an exact **nonnegative fractional factorization of Haar measure**, normalized so that both factors have peak one and have disjoint physical supports away from the identity. General decompositions of uniform laws on finite groups are classical (Sherstnev and earlier work), so I do not claim the uniform-convolution mechanism as new. The Paley-specific content is the simultaneous complementary prescribed Fourier supports, peak-one normalization, and theta extremality.

It is convenient to set

\[
u=f+h,\qquad v=f-h.
\tag{3.9}
\]

Then

\[
u(0)=2,\qquad v(0)=0,
\]

and (3.3)--(3.4) imply the exact pointwise free-boundary identity

\[
\boxed{u=|v|+2\delta_0,\qquad 0\le u(x)\le1\ (x\ne0).}
\tag{3.10}
\]

Let `L` be the previous self-adjoint multiplier: `+1` on `S`, `-1` on `N`, zero on the constant frequency. Since

\[
Lf=f-\frac{1}{n}\left(\sum f\right)\mathbf1,
\qquad
Lh=\frac{1}{n}\left(\sum h\right)\mathbf1-h,
\]

we get

\[
\boxed{Lu=v+2\lambda\mathbf1,}
\qquad
\lambda=\frac{T_p-n/T_p}{2n}.
\tag{3.11}
\]

Eliminating `v` yields an exact nonlinear fixed-point equation for the canonical optimizer:

\[
\boxed{
|Lu-2\lambda\mathbf1|=u-2\delta_0,
\quad
u(0)=2,
\quad
0\le u(x)\le1\ (x\ne0).
}
\tag{3.12}
\]

Thus a putative asymptotic obstruction is not an arbitrary bad vector: it must be an exact bounded free-boundary solution of (3.12) with the Paley multiplier.

---

## 4. Method #7 — take the limit: every persistent imbalance has one scalar shape parameter

Write

\[
x_p=\frac{T_p}{\sqrt n}.
\]

The exact scalar from the preceding run becomes

\[
\boxed{
\sqrt n\,\lambda_p
=\frac12\left(x_p-\frac1{x_p}\right).
}
\tag{4.1}
\]

Therefore, along any subsequence on which `x_p -> x in (0,infinity)`, the only possible nonzero limiting scalar defect is

\[
c=\lim\sqrt n\lambda_p=\frac12(x-x^{-1}),
\tag{4.2}
\]

or equivalently

\[
\boxed{x=c+\sqrt{1+c^2}.}
\tag{4.3}
\]

The exact tiling masses satisfy

\[
\frac1{\sqrt n}\sum f=\frac1{x_p},
\qquad
\frac1{\sqrt n}\sum h=x_p,
\tag{4.4}
\]

and

\[
\frac1{\sqrt n}\sum v
=\frac1{x_p}-x_p
=-2\sqrt n\lambda_p.
\tag{4.5}
\]

Consequently Conjecture 26 is exactly the assertion that the two peak-one complementary fractional Haar factors asymptotically carry equal mass:

\[
\boxed{
T_p\sim\sqrt n
\iff
\sum h-\sum f=o(\sqrt n)
\iff
\sqrt n\lambda_p\to0.
}
\tag{4.6}
\]

A counterexample subsequence with a finite nonzero defect `c` would therefore have to produce exact Paley fractional tilings solving (3.3)--(3.6), (3.12), with asymptotic masses

\[
\sum h\sim\bigl(c+\sqrt{1+c^2}\bigr)\sqrt n,
\qquad
\sum f\sim\bigl(-c+\sqrt{1+c^2}\bigr)\sqrt n.
\tag{4.7}
\]

This is the limiting obstruction I was looking for in the preceding report. It is much more rigid than a generic limit of LP bases.

---

## 5. Method #24 — find the extremal object: a one-sided Chebyshev vector in the Paley half-Fourier space

The second exact reformulation removes the nonnegativity cone from the foreground and isolates one extremal vector.

Let

\[
E_N=\{r:\mathbb Z_n\to\mathbb R:\ \widehat r(0)=0,
\ \operatorname{supp}\widehat r\subseteq N\}.
\tag{5.1}
\]

Define the one-sided Chebyshev constant

\[
\boxed{
a_p=
\min_{\substack{r\in E_N\\r(0)=1}}
\left(-\min_{x\in\mathbb Z_n}r(x)\right).
}
\tag{5.2}
\]

### Theorem R20-CHEB1 — exact theta/Chebyshev identity

\[
\boxed{
T_p=\frac{n a_p}{1+a_p},
\qquad
a_p=\frac{T_p}{n-T_p}.
}
\tag{5.3}
\]

Hence

\[
\boxed{
T_p\sim\sqrt n
\iff
a_p=\frac{1+o(1)}{\sqrt n}.
}
\tag{5.4}
\]

#### Proof

Use the standard circulant theta dual in the equivalent form

\[
T_p=\min\left\{\sum_xq(x):
q\ge0,\ q(0)=1,\ \widehat q|_S=0\right\}.
\tag{5.5}
\]

For a feasible `q`, put

\[
c=\frac1n\sum_xq(x).
\]

At any nontrivial optimum `c<1`. Define

\[
r=\frac{q-c\mathbf1}{1-c}.
\tag{5.6}
\]

Then `r in E_N`, `r(0)=1`, and nonnegativity of `q` says

\[
r(x)\ge-\frac{c}{1-c}\qquad\forall x.
\]

Thus

\[
a_p\le\frac{c}{1-c}.
\tag{5.7}
\]

Conversely, if `r in E_N`, `r(0)=1` and `r>=-a`, then

\[
q=\frac{a}{1+a}\mathbf1+rac1{1+a}r
\tag{5.8}
\]

is feasible for (5.5), has `q(0)=1`, and has total mass

\[
n\frac{a}{1+a}.
\]

Taking the two optima proves (5.3). QED.

This is a finite-dimensional Caratheodory--Fejer/Turan-type extremal problem. Krenedits--Revesz and related literature establish broad positive-definite extremal frameworks on finite/LCA groups; I do not claim that generic framework as new. The point here is that I0100 reduces **exactly** to the one-sided floor of the particular Paley half-Fourier subspace `E_N`.

The canonical factor `h` from Theorem R20-TILE1 is exactly the optimal `q` in (5.5). Therefore

\[
r_*(x)=\frac{h(x)-T_p/n}{1-T_p/n}
\tag{5.9}
\]

is a Chebyshev minimizer. For every `x != 0` with `f(x)>0`, (3.4) forces `h(x)=0`, so

\[
\boxed{r_*(x)=-a_p.}
\tag{5.10}
\]

Thus the positive support of the complementary theta factor is contained in the **contact set of the extremal one-sided Chebyshev vector**. This is the exact extremal object behind the basic-support/cocircuit phenomena observed in the finite certificates.

---

## 6. The old factor-sqrt(2) certificate is exactly the uncorrected orthogonal projection

The Chebyshev formulation cleanly identifies why the earlier SLCE/Jacobi route stopped at the wrong constant.

Let `P_N` be the orthogonal Fourier projection onto `E_N`. Since `|N|=n/2`,

\[
r^{(0)}=2P_N\delta_0
\tag{6.1}
\]

satisfies `r^(0)(0)=1`. With `K=L delta_0`, the projection identity is

\[
\boxed{r^{(0)}=\delta_0-\frac1n\mathbf1-K.}
\tag{6.2}
\]

Hence, for `x != 0`,

\[
r^{(0)}(x)=-\frac1n-K(x),
\]

and

\[
-\min r^{(0)}=\max_{x\ne0}\left(\frac1n+K(x)\right).
\tag{6.3}
\]

The classical Jacobi/SLCE estimate used in the earlier R20 all-prime construction gives

\[
\max_{x\ne0}K(x)\le\frac{\sqrt p}{n}.
\tag{6.4}
\]

Therefore

\[
a_p\le\frac{\sqrt p+1}{n}.
\]

Substitution into (5.3) gives exactly

\[
\boxed{T_p\le\sqrt p-1,}
\tag{6.5}
\]

the same all-prime certificate previously obtained by the explicit SLCE spectral factor. Since `p=2n+1`, this has asymptotic Chebyshev floor `sqrt(2/n)`, whereas Conjecture 26 requires `1/sqrt(n)`.

So the missing constant can now be stated with no SDP language at all:

> Starting from `r^(0)=2P_N delta_0`, find a correction `w in E_N` with `w(0)=0` such that
> \[
> \min_x\bigl(r^{(0)}(x)+w(x)\bigr)
> \ge-\frac{1+o(1)}{\sqrt n}.
> \]

This is a **factor-sqrt(2) one-sided Chebyshev flattening problem** in a single Paley Fourier eigenspace. It is strictly narrower than the separate Paley-ETF/RIP conjecture: no uniform control over all sparse vectors or all submatrices is requested.

---

## 7. What the three methods say

### #3 PROVE SOMETHING STRONGER

Succeeded structurally: R20-TILE1 characterizes the actual theta optimum by peak-one nonnegative factors `f,h` satisfying both `f*h=1` and `fh=delta_0`, with complementary Paley Fourier supports. This contains the scalar balance problem rather than merely bounding it.

### #7 TAKE THE LIMIT

Succeeded as a reduction: any finite nonzero limiting defect is parameterized by the single scalar `c` in (4.2), and forces the exact unequal fractional-tiling masses (4.7). The source conjecture is exactly asymptotic mass balance of these two factors.

It did **not** by itself exclude `c != 0`; compactness without a Paley-specific amplitude theorem would merely produce a bad limiting free-boundary object.

### #24 FIND THE EXTREMAL OBJECT

Succeeded sharply: the extremal object is the one-sided Chebyshev minimizer `r_*` in `E_N`, and theta is exactly `n a_p/(1+a_p)`. The old `sqrt(p)-1` certificate is the raw orthogonal projection `2P_N delta_0`; the conjecture asks for a correction that flattens its worst negative lobe by asymptotic factor `sqrt(2)`.

This is the clearest next target found so far.

---

## 8. Prior-art boundary and current literature

Search date: 2026-09-17.

- The live Randomstrasse source still states Conjecture 26 and separately states Conjectures 27--29.
- Magsino--Mixon--Parshall is prior art for the localized circulant LP and its dual.
- Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky (SampTA 2025 / arXiv:2502.16227) proves square-root scaling for dense random circulant theta only up to a `log log` factor; exact behavior remains open there.
- Krenedits--Revesz treat Caratheodory--Fejer/point-value extremal problems for positive-definite functions on finite/LCA groups. This is relevant background to (5.2), not a source-matching solution found here.
- Sherstnev gives necessary/sufficient conditions and later classifications for decompositions of uniform distributions on finite groups. Hence uniform convolution factorization itself is established literature.

The bounded current search did not locate the target-specific simultaneous package `peak-one + physical disjointness + complementary Paley Fourier supports + theta-optimal masses`, nor a theorem forcing its two masses to balance. This is not a publication-novelty certificate.

---

## 9. Audit / closure status

No source closure is claimed.

- `p=181` finite theorem: now 2/2 independent OTHER-track proof audits (`P26...18=PASS` and `R19...01=PASS`).
- later exact primes through `1061`: not promoted by that audit; each remains author-track evidence unless separately audited.
- R20-TILE0/TILE1, the free-boundary formulation, and R20-CHEB1: written proofs on this page, currently **self-check only**, no OTHER-track audit.
- asymptotic Conjecture 26: OPEN / PARTIAL here.

No new finite claim was made this run, so there is no new checker artifact solely for these algebraic reductions. Theorems above are proved on the page rather than supported only by numerics.

---

## 10. Scheduler/model reality

The exposed scheduling interface still offers prompt/title, schedule/timing, enabled state and timing mode, but no native model field, no reasoning-effort field, no authenticated completed-run model telemetry, and no guaranteed hour-long execution setting. Thus `GPT-6 / maximum` remains a prompt request, not a verified routing setting.

The historical P26 task-ID modification refusal (`You cannot modify this task`) was an ownership/context boundary in one exposed context. Current repository records also say a later authorized context successfully applied the full P26 update. The legitimate remedy for future native model/reasoning control is a product/workspace scheduler surface or API that exposes those fields and run telemetry, or an authorized owning/admin context. GitHub text and duplicate schedules are not a valid workaround. No scheduler change was attempted in this R20 run.

---

## 11. Next route

All thirty first-pass moves are exhausted, so the next run should continue the second-pass rotation with a triple different from `#3/#7/#24`:

- **#5 ADD A PARAMETER AND DIFFERENTIATE:** build a low-dimensional Paley/Jacobi correction family `r^(0)+w_t` inside `E_N`, and derive the derivative of the worst-lobe Chebyshev objective at contact-set changes;
- **#10 DERANDOMIZE:** compare the one-sided Chebyshev floor for a random half-Fourier subspace, then isolate the exact finite collection of character-correlation estimates needed to transfer the construction to Paley `N`;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** search one-sided trigonometric approximation, discrepancy/vector-balancing and equiripple/Remez literature for a theorem that controls the minimum of a prescribed-spectrum vector with one fixed interpolation value.

The mathematical obligation is now very specific:

\[
\boxed{
a_p=
\min_{r\in E_N,\ r(0)=1}\left(-\min_xr(x)\right)
=\frac{1+o(1)}{\sqrt n}.
}
\]

Equivalently, prove asymptotic equality of the two masses in the exact fractional tiling R20-TILE1.

```yaml
ledger_delta:
  worker: R20
  source: "Afonso S. Bandeira / Randomstrasse101 2025, Conjecture 26; I0100"
  target: "theta(complement G_{p,1}) ~ sqrt(p/2)"
  metric_name: "largest admissible prime with matching exact primal/dual certificate"
  metric_before: 1061
  metric_after: 1061
  covered_prime_set: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061]
  status: "PARTIAL / SOURCE OPEN"
  unchanged_count_before: 0
  unchanged_count_after: 1
  tried_moves: [3,7,24]
  moves_are_second_pass: true
  new_claims:
    - "R20-TILE0: translation optimality makes the distinguished atom maximal"
    - "R20-TILE1: exact peak-one complementary fractional Haar tiling"
    - "R20-CHEB1: exact one-sided Chebyshev identity T_p = n a_p/(1+a_p)"
    - "projection diagnosis: raw 2 P_N delta_0 recovers the prior sqrt(p)-1 certificate"
  remaining_obligation: "prove a_p=(1+o(1))/sqrt(n), equivalently balance the two exact fractional-tiling masses or show sqrt(n)*lambda_p -> 0"
  evidence:
    previous_exact_frontier_checker: "artifacts/R20/i0100_p1061_exact_interval_certificate.py @ 6dd0642dae067f2a13dd2581070eda686cc3266a"
    previous_exact_frontier_output: "artifacts/R20/i0100_p1061_exact_interval_certificate.out @ 9e824a9e6b04432ce20d055627676cced287b898"
    this_run: "full written proofs in this immutable report; no new finite checker claim"
  audit_ids:
    - "P26-AUDIT-R20-I0100-P181-FOURIER-DUAL-ENDTOEND-18 = PASS_FULL_FINITE_PROOF / CLAIM_SCOPED / SOURCE_PARTIAL_OPEN"
    - "R19-AUDIT-R20-I0100-P181-01 = PASS_EXACT_FINITE_CASE"
    - "P26-RECONCILE-R20-I0100-P181-2OF2-18 = PASS"
  new_claim_audit_status: "SELF-CHECK ONLY; OTHER-track audit missing"
  next_moves: [5,10,21]
```

**NO CLOSURE CLAIM.**