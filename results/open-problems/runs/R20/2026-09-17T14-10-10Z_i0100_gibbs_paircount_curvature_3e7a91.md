Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime still provides no authenticated applied-model receipt or reasoning-effort telemetry, so I do not claim GPT-6 / maximum. **NO MOVEMENT in the fixed metric: `1201 -> 1201`; exact covered set remains `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201}`; post-movement unchanged count `1 -> 2`; status PARTIAL / SOURCE OPEN. Section-B moves used: second-pass #6 DEFORM TO A SOLVABLE POINT, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE.**

# R20 / I0100 — zero-temperature Gibbs deformation and exact pair-count curvature

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim: `operations/claims/I0100.md`.
Outside source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.
Target:
\[
T_p:=\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2},\qquad p\equiv1\pmod4,
\]
where the theta normalization is the clique-bounding theta of the complement used by the current public problem page.
Tracked quantity: largest admissible prime with matching exact primal/dual certificates for this source-normalized quantity, retaining the complete exact-certified prime set.

## 1. Continuity, source gate, ownership, and status

I continued from the newest immutable R20 report

`runs/R20/2026-09-17T13-17-45Z_i0100_projected_simplex_balance_7a4c2e.md`

rather than restarting. I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the canonical I0100 claim, and the newest located neighboring Paley ownership records. The canonical claim still gives R20 exclusive ownership of I0100 in the CLOSABLE OUTSIDE lane. P04/I0101 remains the distinct two-localization Conjecture 27 assignment. R12 has already handed off its former I0102 / Conjecture 28 degree-four-SoS assignment after its permitted stuck recoveries; that former scope is not imported here. C28's Paley ETF/RIP work is the distinct Conjecture 29 scope.

The primary Randomstrasse stable compilation and current public Jig problem were rechecked on 2026-09-17. The public root is still marked **Open** and still asks whether the Lovasz theta of the Paley one-localization is asymptotic to `sqrt(p/2)`. The stable source still states Conjecture 26 and still records the crucial fact that the one-localization is circulant, so its theta SDP reduces to an LP. A bounded current search found no source-matching proof or refutation. This is a dated search outcome, not a novelty certificate.

Dated search strings used this run included:

- `Randomstrasse 101 Conjecture 26 Paley one-localization theta sqrt p/2`, restricted to the current Jig;
- `2603.29571 Randomstrasse101` for the stable compilation;
- `projected simplex radial depth convex hull entropy central path Fourier`;
- `Caratheodory-Fejer finite cyclic groups positive definite extremal`;
- `Jacobi sums Legendre trace Mellin transform Sidelnikov correlation`.

The literature search recovered the established Krenedits--Revesz Caratheodory--Fejer / positive-definite extremal literature and Alaca--Millar's Jacobi-sum formulation for Sidelnikov correlations, but no theorem that gives the Paley radial constant required here. The connector search is bounded and does not certify worldwide novelty.

The fixed exact frontier remains
\[
\boxed{p_{\max}=1201},
\]
with exact-certified set
\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201\}}.
\]
The existing proof-grade `p=1201` checker/output remains the finite evidence. I did not spend this run manufacturing another certificate.

The previous report established the projected-simplex formulation `R20-HULL1`, the exact balancing projection `R20-BAL1`, and the complementary radial identities
\[
a_N=\frac{T_p}{n-T_p},\qquad a_S=\frac1{T_p-1}.
\]
This run attacks the next question: can one deform from a completely solved balanced point to the radial optimizer in a way that exposes exactly which Paley arithmetic obstructs a scalar proof?

---

## 2. Idea before code

For a symmetric nonzero frequency set `Z subset Z_n`, the preceding report defined the unit tight-frame vertices
\[
u_x=q^{-1/2}P_Ze_x,\qquad q=|Z|/n,
\]
and, with `u_0` distinguished,
\[
c_x=\langle u_0,u_x\rangle,\qquad z_x=u_x-c_xu_0\quad(x\ne0).
\]
The radial constant is
\[
a_Z=\max\left\{-\sum_{x\ne0}y_xc_x:
 y_x\ge0,\ \sum y_x=1,\ \sum y_xz_x=0\right\}.
\tag{2.1}
\]

The uniform weights `y_x=1/(n-1)` are always feasible because `sum z_x=0`. They are the easy point. The exact optimizer is the hard point. The natural deformation is therefore not another ad hoc polynomial certificate but the entropy-regularized path from the uniform distribution to the extremal radial distribution.

The second idea is to exploit the actual cyclic/dihedral harmonic-frame action before estimating anything. At the uniform point it forces exact isotropy in the transverse directions. Hence the first transverse derivative vanishes. The first genuinely nonlinear term is second order, and it can be counted exactly two ways: geometrically as a frame imbalance and arithmetically as variance of additive representation counts of the Paley frequency set. That variance is in turn the same Legendre elliptic trace family already isolated in earlier R20 work.

No new finite code is needed for the claims below; the proofs are on the page.

---

## 3. #6 DEFORM TO A SOLVABLE POINT — an exact zero-temperature Gibbs path

Let
\[
\mathcal Y_Z:=\left\{y\ge0:\sum_{x\ne0}y_x=1,
\ \sum_{x\ne0}y_xz_x=0\right\}
\]
and let
\[
a(y):=-\sum_{x\ne0}y_xc_x.
\]
Thus `a_Z=max_{y in Y_Z} a(y)`.

For `tau>=0`, define the entropy-regularized value
\[
\boxed{
\Psi_Z(\tau)
:=\max_{y\in\mathcal Y_Z}
\left\{\tau a(y)+H(y)\right\},
\qquad
H(y):=-\sum y_x\log y_x.
}
\tag{3.1}
\]
The uniform off-zero distribution lies in the relative interior of `Y_Z`, so for every finite `tau` the strict concavity of entropy gives a unique maximizer `y_tau` on the relevant affine span.

### Theorem R20-GIBBS1 — exact deformation from uniform Haar weights to the Chebyshev optimizer

For every finite `tau`, there is a transverse vector `h_tau` such that
\[
\boxed{
y_\tau(x)=
\frac{\exp(-\tau c_x+\langle h_\tau,z_x\rangle)}
{\sum_{w\ne0}\exp(-\tau c_w+\langle h_\tau,z_w\rangle)},
}
\tag{3.2}
\]
with
\[
\sum y_\tau z=0.
\]
Moreover
\[
\boxed{\Psi_Z'(\tau)=a(y_\tau),}
\tag{3.3}
\]
and `Psi_Z'` is nondecreasing. Finally,
\[
\boxed{\lim_{\tau\to\infty}\Psi_Z'(\tau)=a_Z.}
\tag{3.4}
\]
Thus the exact theta/Chebyshev optimizer is the zero-temperature endpoint of a canonical maximum-entropy path beginning at the uniform off-zero distribution.

#### Proof

The Lagrange multiplier for `sum y z=0` gives (3.2). Equivalently, strong finite-dimensional entropy duality gives
\[
\Psi_Z(\tau)=
\min_h\log\sum_{x\ne0}
\exp(-\tau c_x+\langle h,z_x\rangle).
\tag{3.5}
\]
The first-order equation in `h` is exactly `sum y_tau z=0`. The envelope theorem gives (3.3).

Write, under `y_tau`,
\[
V=\operatorname{Var}(c),\quad
v=\operatorname{Cov}(z,c),\quad
M=\operatorname{Cov}(z,z)
\]
on the transverse span. Differentiating the balance equation gives
\[
h_\tau'=M^{-1}v,
\]
and therefore
\[
\boxed{
\Psi_Z''(\tau)
=V-v^TM^{-1}v\ge0.
}
\tag{3.6}
\]
This is the Schur complement of the covariance matrix of `(c,z)`, proving monotonicity.

Finally, because `0<=H(y)<=log(n-1)`, the variational formula gives
\[
\tau a_Z\le\Psi_Z(\tau)\le\tau a_Z+\log(n-1).
\tag{3.7}
\]
Hence `Psi_Z(tau)/tau -> a_Z`. Since `Psi_Z'` is monotone and bounded above by `a_Z`, its limit must be `a_Z`, proving (3.4). QED.

This is a refinement of the earlier R20 maximum-entropy flat-spectrum formulation, not a claim that entropy regularization itself is new. What is new to this track is the exact identification of its zero-temperature endpoint with the projected-simplex radial optimizer and the curvature calculation below.

---

## 4. #14 FIND THE GROUP ACTING — exact isotropy at the solved endpoint

The cyclic regular representation is not decorative here. It gives the harmonic frame identities exactly. Put
\[
A:=\frac n{|Z|}.
\]
The previous report proved
\[
\sum_{x\ne0}z_x=0,
\qquad
\sum_{x\ne0}c_xz_x=0,
\qquad
\sum_{x\ne0}z_xz_x^T=A I,
\tag{4.1}
\]
and
\[
\sum_{x\ne0}c_x=-1,
\qquad
\sum_{x\ne0}c_x^2=A-1.
\tag{4.2}
\]
At `tau=0`, the Gibbs optimizer is therefore exactly uniform:
\[
y_0(x)=\frac1{n-1},\qquad h_0=0.
\]
The covariance blocks are
\[
M_0=\frac{A}{n-1}I,
\qquad
v_0=0,
\]
so
\[
\boxed{h_0'=0.}
\tag{4.3}
\]
In particular the transverse correction cannot appear linearly. The longitudinal radial slope begins with
\[
\boxed{
\Psi_Z'(0)=\frac1{n-1},
}
\tag{4.4}
\]
and
\[
\boxed{
\Psi_Z''(0)
=\frac{A-1}{n-1}-\frac1{(n-1)^2}.
}
\tag{4.5}
\]
For both Paley halves, `A=2+o(1)`, hence under the natural scaled inverse temperature `tau=s sqrt(n)`,
\[
\frac{d}{ds}\Bigl[\sqrt n\,\Psi_Z'(s\sqrt n)\Bigr]_{s=0}
=n\Psi_Z''(0)\longrightarrow1.
\tag{4.6}
\]
So the desired radial constant `1` is normalized correctly already at first order in the scaled temperature. The obstruction is not the initial slope. It is the transverse nonlinear response.

There is also an exact second derivative. Differentiate the balance equation twice at `tau=0`. Since `h_0'=0`, one gets
\[
0=\frac1{n-1}\sum_{x\ne0}z_x(c_x-\bar c)^2
+\frac{A}{n-1}h_0'',
\]
where `bar c=-1/(n-1)`. Using `sum z=sum cz=0`,
\[
\boxed{
h_0''=-\frac1A R_Z,
\qquad
R_Z:=\sum_{x\ne0}c_x^2z_x.
}
\tag{4.7}
\]
Thus `R_Z` is the first genuinely nonlinear transverse obstruction.

Because `Z=-Z`, reflection `x -> -x` is in the stabilizer of the distinguished vertex. The entropy maximizer is unique, so it is reflection invariant: `y_tau(x)=y_tau(-x)`. Hence `h_tau` lies in the reflection-fixed transverse subspace. I use only this genuine stabilizer; no larger automorphism group is assumed.

---

## 5. #25 COUNT THE SAME THING TWICE — quadratic imbalance = additive pair-count variance

Let
\[
r_Z(k):=|\{(a,b)\in Z^2:a+b=k\}|.
\tag{5.1}
\]
The same vector `R_Z` in (4.7) has an exact combinatorial norm formula.

### Theorem R20-COUNT1 — exact representation-variance identity

For every symmetric `Z` as above, with `d=|Z|` and `A=n/d`,
\[
\boxed{
\|R_Z\|_2^2
=\frac{A^5}{n^3}
\left[
\sum_{k\in Z}r_Z(k)^2
-\frac1d\left(\sum_{k\in Z}r_Z(k)\right)^2
\right].
}
\tag{5.2}
\]
Equivalently, the first nonlinear transverse curvature is exactly the variance, on `k in Z`, of the number of additive representations of `k` by two elements of `Z`.

#### Proof

The longitudinal row is
\[
c=q^{-1}P_Z\delta_0,
\qquad q=d/n,
\]
so under the unnormalised DFT convention
\[
\widehat c=A\,1_Z.
\]
Therefore
\[
\widehat{c^2}(k)=\frac{A^2}{n}r_Z(k).
\tag{5.3}
\]
The frame synthesis of the coefficients `c_x^2` is
\[
\sum_xc_x^2u_x=q^{-1/2}P_Z(c^2),
\]
while its `u_0` component is `sum_x c_x^3`. Since `z_0=0`, subtracting the longitudinal component gives `R_Z`. Parseval and (5.3) yield
\[
\|R_Z\|^2
=A\|P_Z(c^2)\|^2-\left(\sum_xc_x^3\right)^2
\]
\[
=\frac{A^5}{n^3}\sum_{k\in Z}r_Z(k)^2
-\frac{A^6}{n^4}\left(\sum_{k\in Z}r_Z(k)\right)^2.
\]
Since `A/n=1/d`, this is exactly (5.2). QED.

This is useful because `r_Z` can be counted a second way from the finite-field definition of the Paley localized frequency sets.

---

## 6. Exact Paley pair counts: the same Legendre elliptic trace reappears

Write
\[
Q=(\mathbb F_p^\times)^2,
\qquad n=|Q|=\frac{p-1}{2},
\]
fix a generator `alpha` of `Q`, and put
\[
T(t)=\sum_{z\in\mathbb F_p}\chi(z(z-1)(z-t)).
\tag{6.1}
\]
For exponent `k != 0`, write `t=alpha^k` and
\[
\sigma(t)=\chi(t-1)\in\{+1,-1\}.
\]
Let
\[
S=\{k\ne0:\sigma(\alpha^k)=+1\},
\qquad
N=\{k\ne0:\sigma(\alpha^k)=-1\}.
\]
Then `|N|=n/2` and `|S|=n/2-1`.

### Theorem R20-PAIR1 — exact two-sum counts

For every `k != 0`,
\[
\boxed{
r_N(k)
=\frac n4+\frac{T(t)-2}{8}+\frac{\sigma(t)}2,
}
\tag{6.2}
\]
and
\[
\boxed{
r_S(k)
=\frac n4-1+\frac{T(t)-2}{8}-\frac{\sigma(t)}2.
}
\tag{6.3}
\]
In particular,
\[
\boxed{
r_N(k)=\frac n4+\frac{T(t)-6}{8}\quad(k\in N),}
\tag{6.4}
\]
while
\[
\boxed{
r_S(k)=\frac n4+\frac{T(t)-14}{8}\quad(k\in S).}
\tag{6.5}
\]

#### Proof

For `x in Q`, the exact indicator that its exponent lies in `N` is
\[
I_N(x)=\frac{1-\chi(x-1)-1_{x=1}}2,
\]
and similarly
\[
I_S(x)=\frac{1+\chi(x-1)-1_{x=1}}2.
\]
Because `t,x in Q`,
\[
\chi(t/x-1)=\chi(t-x).
\]
Thus `r_N(k)=sum_{x in Q} I_N(x)I_N(t/x)` and likewise for `S`.

The needed restricted sums are
\[
\sum_{x\in Q}\chi(x-1)=-1,
\qquad
\sum_{x\in Q}\chi(t-x)=-1,
\tag{6.6}
\]
and
\[
\boxed{
\sum_{x\in Q}\chi(x-1)\chi(t-x)=\frac{T(t)-2}{2}.
}
\tag{6.7}
\]
For (6.7), insert `1_Q(x)=(1+chi(x))/2` on `x != 0`. The untwisted quadratic sum over all `x` is `-1`, but its `x=0` term is `1`, giving `-2` on `x !=0`; the quadratic-character-twisted term is exactly the cubic trace `T(t)`. Expanding the two exact indicators, including the corrections at `x=1,t`, gives (6.2) and (6.3). QED.

This is the main arithmetic bridge of the run: the quadratic transverse failure of the projected-simplex entropy path is controlled exactly by the same Legendre elliptic family that appeared earlier in R20's common-neighbor analysis.

---

## 7. The first nonlinear transverse curvature has a nonzero universal scale

Earlier R20 work established the exact global second moment
\[
\sum_{t\in\mathbb F_p}T(t)^2=p^2-2p-1
\tag{7.1}
\]
and, writing
\[
U_p=\sum_t\chi(t)T(t)^2,
\]
the standard Legendre-sheaf/Kummer-twist estimate
\[
U_p=O(p^{3/2}).
\tag{7.2}
\]
It also gave on the edge class `S`
\[
\sum_{k\in S}T(\alpha^k)^2
=\frac{p^2-2p-6+3U_p}{4}
=\frac{p^2}{4}+O(p^{3/2}),
\tag{7.3}
\]
and `sum_{k in S} T(alpha^k)=O(p)`.

The square subgroup satisfies
\[
\sum_{t\in Q}T(t)^2
=\frac{p^2-2p-2+U_p}{2}.
\]
Removing `t=1` and the `S` class therefore gives
\[
\boxed{
\sum_{k\in N}T(\alpha^k)^2
=\frac{p^2-2p-2-U_p}{4}
=\frac{p^2}{4}+O(p^{3/2}).
}
\tag{7.4}
\]
The corresponding first moment is `O(p)` by the same bounded-conductor Legendre/Kummer trace estimate (equivalently, combine the square-subgroup Mellin identity with the `S`-class estimate).

Now (6.4)--(6.5) say that, restricted to the relevant frequency half, `r_Z(k)` differs from an affine constant by exactly `T(alpha^k)/8`. Hence (5.2), (7.3), and (7.4) give for **both** Paley halves `Z=N,S`
\[
\boxed{
\|R_Z\|_2^2
=\frac1{2n}+O(n^{-3/2}).
}
\tag{7.5}
\]
Indeed `A_Z=2+O(1/n)`, `|Z|=n/2+O(1)`, and the centered trace second moment on either class is `n^2+O(n^{3/2})`; the factor `1/64` from (6.4)--(6.5) combines with `A^5 -> 32` in (5.2).

Combining with (4.7),
\[
\boxed{
\sqrt n\,\|h_{Z,0}''\|_2
\longrightarrow\frac1{2\sqrt2},
\qquad Z=N,S.
}
\tag{7.6}
\]

This is a useful negative diagnosis. The cyclic symmetry makes the first transverse derivative vanish exactly, but the second transverse derivative does **not** disappear asymptotically: after the natural `sqrt(n)` normalization it has a nonzero universal constant. Thus any proof that keeps the entropy deformation scalar in the one-point Jacobi coordinate beyond first order is structurally impossible. The first nonlinear response already sees additive pair-count fluctuations, i.e. a genuinely joint statistic.

This also explains why the previous run's exact balancing projection was the right object. The term `R_Z` is precisely the quantity that `B_Z` removes from a quadratic scalar profile.

No source asymptotic follows yet: (7.6) diagnoses the needed mechanism but does not bound the full zero-temperature path through to radial depth `1/sqrt(n)`.

---

## 8. What moved mathematically, and what did not

The fixed finite metric did **not** move. The research state did:

1. `R20-GIBBS1` gives an exact, monotone, zero-temperature deformation from the solved uniform point to the exact Chebyshev/theta radial optimizer.
2. The actual harmonic group action gives exact transverse isotropy at the solved point and forces `h_0'=0`.
3. `R20-COUNT1` identifies the first nonlinear transverse obstruction with an exact additive representation-count variance for the frequency set.
4. `R20-PAIR1` evaluates those pair counts in the Paley case by the Legendre elliptic trace `T(t)`.
5. The existing Legendre second-moment machinery then proves the universal curvature law (7.6) for both complementary halves.

This is a new way to state the missing step: one must control the **entire vector-valued entropy central path after the first nonzero transverse curvature**, not merely sharpen the one-point Jacobi endpoint or choose a scalar nonlinear profile.

A useful next target is now explicit. With
\[
m_Z(\tau):=\Psi_Z'(\tau),
\]
prove, for `Z=N,S`, that at some `tau=tau_p` before the entropy path reaches a singular face,
\[
\sqrt n\,m_Z(\tau_p)\ge1-o(1).
\tag{8.1}
\]
Because `m_Z` is monotone and tends to `a_Z`, (8.1) would prove the two radial lower bounds from `R20-TWORAD1` and therefore Conjecture 26. The missing input is a quantitative lower bound on the Schur-complement Fisher curvature
\[
\Psi_Z''(\tau)
=\operatorname{Var}_{y_\tau}(c)
-\operatorname{Cov}(c,z)^T
\operatorname{Cov}(z,z)^{-1}
\operatorname{Cov}(z,c)
\tag{8.2}
\]
along enough of the path. The exact pair-count computation says which arithmetic tensor enters first when this curvature starts to depart from its isotropic value.

Exploratory floating calculations were used only to decide whether low-degree scalar profiles deserved further effort; they are not archived as evidence and no theorem here depends on them.

---

## 9. Prior-art boundary

The entropy/Gibbs variational principle, finite-dimensional exponential families, and Caratheodory--Fejer positive-definite extremal theory are classical and are not claimed as new. Krenedits--Revesz (2015/2018) is the relevant positive-definite extremal background. Jacobi-sum correlation formulae for Sidelnikov-type sequences are also established; Alaca--Millar (2019) is a representative reference. Earlier R20 work already cited Katz's Legendre-sheaf monodromy/Deligne machinery for (7.2)--(7.4).

The candidate new synthesis here is the chain

`Paley theta -> projected-simplex radial depth -> entropy zero-temperature path -> first transverse curvature -> additive pair-count variance -> Legendre elliptic trace second moment`.

The bounded dated search did not locate that chain or `R20-COUNT1/R20-PAIR1` applied to Randomstrasse Conjecture 26. This is **not** a publication novelty certificate. The new theorem-sized claims remain self-check only until another track reconstructs them.

---

## 10. Audit state and closure status

Existing independent R20 finite audits remain scoped to earlier exact primes/algebraic cores. In particular, `p=181` and `p=241` have distinct OTHER-track finite proof passes. None of `R20-GIBBS1`, `R20-COUNT1`, `R20-PAIR1`, or the curvature law (7.6) has an OTHER-track audit yet.

Therefore:

- finite frontier: **PARTIAL evidence only** for the asymptotic;
- source Conjecture 26: **OPEN**;
- this run: **NO CLOSURE CLAIM**.

---

## 11. Scheduler/model-control status

The exposed scheduler surface still has task text/title, schedule/timing, enabled state, and timing mode, but no native model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no control that guarantees hour-long execution. Thus GPT-6/maximum remains a request in prompt text, not a verified scheduler setting.

The historical P26 `You cannot modify this task` error was an ownership/context restriction. The repository's current deployment record states that P26 was later updated successfully from another authorized context. The legitimate remedy for future model routing is an owning product/workspace surface or platform API/support that actually exposes model and reasoning controls; duplicating tasks or bypassing permissions is not an acceptable workaround. No scheduler change was attempted in this run.

---

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R20
  intake: I0100
  source: "Bandeira et al., Randomstrasse101 (2025), Conjecture 26"
  source_status: OPEN
  metric: "largest admissible prime with matching exact primal/dual certificates"
  before: 1201
  after: 1201
  movement: false
  unchanged_count_before: 1
  unchanged_count_after: 2
  covered_primes:
    - 5
    - 13
    - 17
    - 29
    - 41
    - 181
    - 241
    - 317
    - 421
    - 541
    - 601
    - 661
    - 1009
    - 1021
    - 1033
    - 1049
    - 1061
    - 1093
    - 1201
  status: PARTIAL
  tried_moves: [6, 14, 25]
  tried_moves_pass: 2
  new_claims:
    - R20-GIBBS1
    - R20-COUNT1
    - R20-PAIR1
    - R20-CURV1
  remaining_obligation: >-
    Prove enough lower control on the Schur-complement Fisher curvature along the vector-valued entropy path for both complementary Paley Fourier halves to force sqrt(n)*a_N >= 1-o(1) and sqrt(n)*a_S >= 1-o(1), equivalently T_p/sqrt(n) -> 1.
  evidence:
    - "existing p=1201 exact primal/dual interval checker and output"
    - "R20-HULL1/BAL1/TWORAD1 from preceding immutable report"
    - "on-page proofs of GIBBS1, COUNT1, PAIR1"
    - "earlier exact Legendre Mellin/second-moment identities and standard bounded-conductor trace estimates"
  audit_ids:
    - "R19 finite-prime/Turan audits retained"
    - "P26-AUDIT-R20-I0100-P181-FOURIER-DUAL-ENDTOEND-18=PASS_FULL_FINITE_PROOF"
    - "P26-AUDIT-R20-I0100-P241-FOURIER-DUAL-ENDTOEND-22=PASS_FULL_FINITE_PROOF"
  new_claim_audit_state: SELF_CHECK_ONLY
```

Next second-pass moves, if the metric has not moved before the next invocation: **#4 PROVE SOMETHING WEAKER COMPLETELY, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME.** These are aimed at the Fisher-curvature path, not at manufacturing a checker-only prime extension. If the unchanged streak reaches three, the subsequent invocation must follow the section-I stuck protocol rather than produce another routine lemma.

**NO CLOSURE CLAIM.**