Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed scheduler/runtime still has no model selector, reasoning-effort selector, authenticated runtime-model telemetry, or guaranteed hour-long execution setting, so this report does not claim otherwise. **NO MOVEMENT in the fixed metric: 1021 -> 1021. Methods used: #4 PROVE SOMETHING WEAKER COMPLETELY, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #29 ADD THE POINTS AT INFINITY.**

# R20 / I0100 — one-localized Paley theta, dyadic-zonotope reduction and a Paley one-point Kashin bound

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status after this run: **PARTIAL / source OPEN. NO CLOSURE CLAIM.**

## 1. Source, ownership, scope, and current status

Outside source: Afonso S. Bandeira, Randomstrasse 101 (2025), Conjecture 26, live source

`https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/`

and stable 2026 Randomstrasse compilation arXiv:2603.29571.

The live source was rechecked on 2026-09-17. It still defines `G_{p,1}` as the induced subgraph on the neighbors of 0 in the Paley graph, notes that the one-localization is circulant so its Lovasz-theta SDP reduces to an LP, and still states

\[
T_p:=\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}
\qquad(p\equiv1\pmod4,\ p\text{ prime}).
\]

The same page separately states Conjecture 27 (two-localization), Conjecture 28 (degree-four SoS), and Conjecture 29 (Paley ETF/RIP). Those remain excluded from R20.

Canonical ownership was reread from `operations/claims/I0100.md`: owner R20, lane CLOSABLE OUTSIDE, frozen metric = largest admissible prime with matching exact primal/dual certificates for the source-normalized theta quantity, preserving the full covered-prime set. The old R20 Kalikow assignment remains retired with its preserved handoff.

A bounded current literature/status search on 2026-09-17 checked the live Randomstrasse page, Magsino--Mixon--Parshall's 2019 localized-Paley LP work, the 2025 random-circulant Lovasz-theta paper, current arXiv/title queries for localized Paley theta, volume-sampling/DPP literature, and Kashin/Euclidean-section literature. No source-matching proof or refutation of Conjecture 26 surfaced. This is a dated bounded search, not a worldwide novelty certificate.

## 2. Repository continuation and fixed metric

I continued from the newest immutable R20 report

`runs/R20/2026-09-17T04-31-00Z_i0100_p1021_pivot_homotopy_6f2d91.md`

rather than restarting.

Before research I recovered/reread the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current new-methods owner directive / deployment state, the canonical I0100 claim, the newest own report, and current neighboring Paley reports. The intake corpus is too large for a literal byte-by-byte connector rendering; exact-ID/source/ownership retrieval plus the canonical claim/current queue was used for the relevant rows. I do not claim a visual reread of every one of the roughly 780 intake lines.

Neighbor separation remains intact:

- P04/I0101 = Randomstrasse Conjecture 27, two-localization;
- R12/I0102 = Conjecture 28, degree-four SoS;
- C28/I0103 = Conjecture 29, Paley ETF/RIP.

No result from those distinct scopes is counted for I0100.

The previous exact-certified set remains

\[
\boxed{\{5,13,17,29,41,181,241,421,541,601,661,1009,1021\}},
\qquad
\boxed{p_{\max}=1021}.
\]

A repository search found no later R20 `PASS_p` artifact with `p>1021`. The corrected p=1021 interval certificate remains the current finite frontier. Therefore the metric is honestly

\[
\boxed{1021\to1021}.
\]

Finite exact certificates remain PARTIAL for the asymptotic statement.

The previous run used methods #3/#6/#13, so this run deliberately moved to the recorded next triple #4/#23/#29.

## 3. Method #4 — prove something weaker completely: an exact dyadic pair / zonotope formula

The previous determinant/oriented-matroid formulation is exact but still global. This run uses the special fact that the one-localized Paley LP lives on an even cyclic group and splits it across the index-two subgroup.

The following statement is elementary and exact for any even cyclic moment problem of this form, not only Paley.

### Theorem R20-DYADIC1 — exact two-scale variational formula

Let `n=2m`, let `S=-S` be a set of nonzero frequencies in `Z_n`, and define

\[
H_S:=\max\left\{\mu_0:
\mu_j\ge0,\quad \sum_{j\in\mathbb Z_n}\mu_j=1,\quad
\widehat\mu(s)=0\ \forall s\in S
\right\}.
\tag{3.1}
\]

For R20, `H_S=1/T_p` with `S` the localized Paley edge-difference set.

For `j in Z_m`, put

\[
a_j=\mu_j+\mu_{j+m},\qquad
b_j=\mu_j-\mu_{j+m}.
\tag{3.2}
\]

Define the even-frequency set

\[
E=\{k\in\mathbb Z_m:2k\in S\}
\tag{3.3}
\]

and

\[
\mathcal A_E=\left\{a\in\mathbb R_{\ge0}^m:
\sum_j a_j=1,\quad
\sum_j a_j e^{2\pi i k j/m}=0\ \forall k\in E
\right\}.
\tag{3.4}
\]

Realify the odd Fourier constraints in `S`: choose real feature vectors `v_j in R^r`, `j in Z_m`, so that

\[
\sum_j b_jv_j=0
\tag{3.5}
\]

is exactly equivalent to all odd-frequency moment equalities. For fixed `a in A_E`, define the symmetric zonotope

\[
Z_O(a)=\sum_{j\ne0}[-a_jv_j,a_jv_j]
\tag{3.6}
\]

and its radial depth in the distinguished direction

\[
\rho_O(a)=\sup\{t\ge0:t v_0\in Z_O(a)\}.
\tag{3.7}
\]

Then, with the convention that the odd-free case has `rho_O(a)=+infinity`,

\[
\boxed{
H_S
=
\frac12\max_{a\in\mathcal A_E}
\left[a_0+\min\{a_0,\rho_O(a)\}\right].
}
\tag{3.8}
\]

Moreover the radial depth has the exact polar formula

\[
\boxed{
\rho_O(a)
=
\inf_{y:\langle y,v_0\rangle=1}
\sum_{j\ne0}a_j\,|\langle y,v_j\rangle|,
}
\tag{3.9}
\]

where the formula is interpreted after quotienting by the common nullspace of the `v_j` if necessary.

### Proof

Pairing `j` with `j+m` is a bijection between nonnegative `mu` and pairs `(a,b)` satisfying

\[
a_j\ge0,\qquad |b_j|\le a_j,\qquad \sum_j a_j=1,
\tag{3.10}
\]

because

\[
\mu_j=\frac{a_j+b_j}{2},\qquad
\mu_{j+m}=\frac{a_j-b_j}{2}.
\tag{3.11}
\]

Also

\[
\mu_0=\frac{a_0+b_0}{2}.
\tag{3.12}
\]

For an even frequency `s=2k`,

\[
\widehat\mu(2k)
=
\sum_{j=0}^{m-1}a_j e^{2\pi i k j/m},
\tag{3.13}
\]

so the even constraints are exactly `a in A_E`.

For odd `s`, the factor gained by translating a point by `m` is `-1`, hence the odd constraints depend only on `b`; after taking one representative from each conjugate pair and splitting into real and imaginary parts they are exactly (3.5).

Fix `a in A_E`. Equation (3.5) is

\[
b_0v_0=-\sum_{j\ne0}b_jv_j.
\tag{3.14}
\]

The box restrictions `|b_j|<=a_j` for `j ne 0` say that the right-hand side runs through the symmetric zonotope `Z_O(a)`. Thus the largest admissible nonnegative value of `b_0` is exactly

\[
\max b_0=\min\{a_0,\rho_O(a)\}.
\tag{3.15}
\]

Substituting (3.15) into (3.12) and then maximizing over `a in A_E` proves (3.8).

For (3.9), the support function of (3.6) is

\[
h_{Z_O(a)}(y)
=
\sum_{j\ne0}a_j|\langle y,v_j\rangle|.
\tag{3.16}
\]

For a closed centrally symmetric convex body, `t v_0 in Z` iff

\[
t|\langle y,v_0\rangle|\le h_Z(y)
\quad\text{for every }y.
\]

Normalizing `\langle y,v_0\rangle=1` gives exactly (3.9). QED.

This is a complete weaker theorem: it does not prove Bandeira's asymptotic, but it replaces the full `2m`-variable positive LP by a nested problem consisting of (i) an `m`-point positive Fourier-zero problem for `a`, and (ii) a weighted one-direction zonotope radius for the odd constraints.

## 4. Exact small-case check: the odd scale is a real obstruction already at p=17

Only after deriving R20-DYADIC1, I built one exact arithmetic self-check at the already-certified prime `p=17`.

For `p=17`, `n=8`, `m=4`, the localized edge-frequency set is

\[
S=\{1,4,7\}.
\]

The known exact theta-optimal probability measure has pair variables

\[
\boxed{
a=(1/2,1/4,0,1/4),
\qquad
b=(\sqrt2/4,-1/4,0,1/4).
}
\tag{4.1}
\]

The only even constraint is frequency 4, which becomes the `Z_4` frequency 2 equality

\[
a_0+a_2=a_1+a_3=1/2.
\]

Hence the **even-only relaxation** has the exact optimum

\[
\boxed{\max a_0=1/2}.
\tag{4.2}
\]

But the odd frequencies `1,7` give feature vectors

\[
v_j=(\cos(\pi j/4),\sin(\pi j/4)).
\]

For the `a` in (4.1), the zonotope generated by `a_1v_1` and `a_3v_3` has exact radial depth

\[
\boxed{\rho_O(a)=\sqrt2/4<1/2=a_0}.
\tag{4.3}
\]

Therefore (3.8) gives

\[
H_S=\frac12\left(\frac12+\frac{\sqrt2}{4}\right)
=\frac14+\frac{\sqrt2}{8},
\]

and

\[
\boxed{T_{17}=8-4\sqrt2}.
\tag{4.4}
\]

So even at the first nontrivial exact example, optimizing the index-two/even relaxation does **not** automatically lift through the odd constraints. This is a concrete exact failure-to-glue phenomenon, not a numerical impression.

Artifact created after the idea:

- `artifacts/R20/i0100_p17_dyadic_zonotope_selfcheck.py`
  - creation commit `d5493bad8c2f413a064e93c5cbeea0b474ecd375`;
  - read back at that exact commit.
- `artifacts/R20/i0100_p17_dyadic_zonotope_selfcheck.out`
  - creation commit `566d45654d1a02795afe96890bafb309b08cd21d`;
  - read back at that exact commit;
  - execution stdout SHA-256 `4602fea3a05cc41133078172d28a611db6f37df5c3871ac41360379aea6dd1aa`;
  - ends `PASS`.

This checker is a **self-check** of the p=17 finite specialization only. It does not certify the asymptotic theorem.

## 5. Method #23 — do what the proposer did not expect: turn the odd gluing problem into a directional Kashin problem

The source is phrased as graph theta/pseudorandomness. R20-DYADIC1 says the missing half of the LP is instead a weighted `l1` geometry problem for a very specific half-Fourier subspace.

Specialize now to the localized Paley graph. Write

\[
p=4m+1,
\qquad n=(p-1)/2=2m,
\]

choose a primitive root `g mod p`, put

\[
\alpha=g^2,\qquad \beta=g^4,\qquad c=g^2,
\]

so `beta` generates the fourth powers, a subgroup of order `m`. The localized connection set is

\[
S_p=\{d\ne0:\chi(\alpha^d-1)=1\},
\tag{5.1}
\]

where `chi` is the quadratic character.

For the **odd** localized frequencies write `d=2k+1`. Then

\[
\alpha^{2k+1}=c\beta^k,
\]

and define

\[
K=\{k\in\mathbb Z_m:\chi(c\beta^k-1)=1\}.
\tag{5.2}
\]

The odd feature space in (3.5), after multiplying coordinate `j` by the harmless unit phase `e^{-\pi i j/m}`, is exactly the `m`-point Fourier subspace with frequency support `K`. Thus its `l1` geometry can be attacked directly by multiplicative character sums.

### Proposition R20-ODD1 — a deterministic one-point Kashin bound

Let `V_K` be the `m`-point Fourier subspace whose Fourier support is contained in `K`. Then every `f in V_K` satisfies

\[
\boxed{
\sum_{j\ne0}|f_j|
\ge
\frac{2(m-|K|)}{\sqrt p}|f_0|
\ge
\left(\frac{m}{\sqrt p}-1\right)|f_0|.
}
\tag{5.3}
\]

In particular, since `p=4m+1`,

\[
\sum_{j\ne0}|f_j|
\ge
\left(\frac12+o(1)\right)\sqrt m\,|f_0|.
\tag{5.4}
\]

This is a one-distinguished-coordinate statement, much weaker than a full restricted-isometry theorem and therefore distinct from C28's Paley-ETF/RIP problem.

### Proof

For `t in Z_m` set

\[
Z_t=\sum_{k=0}^{m-1}\chi(c\beta^k-1)e^{-2\pi i tk/m}.
\tag{5.5}
\]

Let `rho_t` be any multiplicative character on `F_p^*` extending the character of the fourth-power subgroup with

\[
\rho_t(\beta)=e^{-2\pi i t/m}.
\]

Let `nu` be a quartic character with `nu(g)=i`. Since `nu(c)=-1`, the indicator of the coset `c<beta>` is

\[
1_{c\langle\beta\rangle}(x)
=
\frac14\sum_{r=0}^3(-1)^r\nu(x)^r.
\tag{5.6}
\]

Up to the unit factor `rho_t(c)^{-1}`, (5.5) is therefore

\[
\frac14\sum_{r=0}^3(-1)^r
J(\rho_t\nu^r,\chi),
\tag{5.7}
\]

because `chi(-1)=1` for `p=1 mod 4`. Standard Jacobi-sum identities give magnitude `sqrt(p)` in the nonexceptional cases and magnitude at most 1 in the trivial/inverse exceptional cases. Hence, by the triangle inequality,

\[
\boxed{|Z_t|\le\sqrt p\quad\forall t.}
\tag{5.8}
\]

Since

\[
1_K(k)=\frac12\left[1+\chi(c\beta^k-1)\right],
\]

we obtain

\[
\left||K|-\frac m2\right|\le\frac{\sqrt p}{2}
\tag{5.9}
\]

and, for every nonzero `t`,

\[
\left|\widehat{1_K}(t)\right|\le\frac{\sqrt p}{2}.
\tag{5.10}
\]

Let `P_K` be the orthogonal projection onto `V_K`. Its circulant kernel is

\[
(P_K)_{ij}=\frac1m\sum_{k\in K}e^{2\pi i k(i-j)/m}.
\]

Thus

\[
(P_K)_{00}=\frac{|K|}{m},
\qquad
|(P_K)_{0j}|\le\frac{\sqrt p}{2m}\quad(j\ne0).
\tag{5.11}
\]

For `f in V_K`, `f=P_Kf`, so at coordinate zero

\[
\left(1-\frac{|K|}{m}\right)|f_0|
\le
\frac{\sqrt p}{2m}\sum_{j\ne0}|f_j|.
\]

Rearranging gives the first inequality in (5.3). From (5.9),

\[
m-|K|\ge\frac m2-\frac{\sqrt p}{2},
\]

which gives the second inequality. QED.

The Jacobi-sum estimate itself is classical; no novelty is claimed for it. The useful point here is that the exact R20-DYADIC1 reduction asks for precisely a **one-point weighted `l1` inequality**, and the Paley odd-frequency subspace already satisfies the correct `sqrt(m)` order deterministically by a short character-sum argument.

### Weighted corollary for the zonotope radius

Suppose an even-feasible outer probability `a in A_E` satisfies a tail floor

\[
a_j\ge\gamma/m\qquad(j\ne0).
\tag{5.12}
\]

The polar formula (3.9), after the unit-modulus modulation just described, and R20-ODD1 imply

\[
\boxed{
\rho_O(a)
\ge
\frac{\gamma}{m}\,
\frac{2(m-|K|)}{\sqrt p}
\ge
\frac{\gamma}{m}\left(\frac{m}{\sqrt p}-1\right)
=
\left(\frac\gamma2+o(1)\right)m^{-1/2}.
}
\tag{5.13}
\]

Thus the odd gluing radius is automatically on the **correct square-root scale** for any sufficiently flat even-feasible outer measure. The remaining source-level difficulty is now a sharp-constant problem coupling the even outer measure and this weighted radius, not merely proving square-root order.

## 6. Why determinant/volume averaging alone does not solve the sign problem

I also recovered a post-report exact p=17 artifact already present under R20:

`artifacts/R20/i0100_p17_projection_dpp_selfcheck.*`.

It checks exact projection-DPP/volume-sampling identities for the p=17 Fourier row system:

- total determinant mass = 1;
- each column inclusion probability = 1/2;
- each unconditional signed-basic coefficient mean = 1/8;
- each unconditional second moment = 35/512;
- positive bases = 20 of 70;
- total DPP mass on positive bases = 7/16;
- the largest positive zero atom is `1/4+sqrt(2)/8`, giving `T_17=8-4sqrt(2)`.

This fits established volume-sampling prior art: determinant-proportional sampling gives unbiased pseudoinverse/regression estimators and exact or one-sided second-moment formulas under appropriate support/rank hypotheses. Therefore the generic determinant averaging itself is not claimed new.

The failure is exactly the one R20 needs to understand: **theta requires positivity, while volume sampling naturally averages signed basic solutions.** At p=17 positive bases carry substantial but not full volume mass (`7/16`). An average signed basis can therefore have beautiful exact moments while saying too little about the best orientation-positive basis. This is consistent with the 2025 random-circulant theta paper: its Fourier/RIP upper route loses a `log log` factor and, in its LP analysis, positivity is a central obstruction rather than a disposable detail.

The closest broad geometric analogue is Kashin/Euclidean-section theory, where random half-dimensional subspaces have strong `l1/l2` equivalence. That shows the desired geometry is plausible in random subspaces, but the bounded search found no theorem transferring the sharp weighted **Paley arithmetic** directional constant required by (3.8). Importing a full RIP theorem would also trespass into the distinct C28 scope; R20-ODD1 avoids that by proving only the one distinguished-direction inequality actually needed here.

## 7. Method #29 — add the points at infinity: compactify the failure to glue

Equation (3.9) turns an abstract failed lift into a concrete boundary witness.

If, for an even-feasible `a`,

\[
\rho_O(a)<a_0,
\tag{7.1}
\]

then after quotienting by the common nullspace there is a supporting functional `y_*` with

\[
\langle y_*,v_0\rangle=1,
\qquad
\sum_{j\ne0}a_j|\langle y_*,v_j\rangle|=\rho_O(a)<a_0.
\tag{7.2}
\]

Equivalently, after demodulation in the Paley case, there is a vector `f` in the odd partial-Fourier subspace with

\[
f_0=1,
\qquad
\sum_{j\ne0}a_j|f_j|<a_0.
\tag{7.3}
\]

So a failure of the odd lift has a precise **weighted trigonometric separator**. When `a` approaches the boundary of its positive cell and some generators disappear, projectivizing the supporting functional is the natural compactification: the limiting obstruction is a signed fundamental-cocircuit / supporting-hyperplane pattern rather than an unstructured diverging LP vector.

At `p=17` this boundary obstruction is completely explicit: the even optimum has `a_0=1/2`, while the odd supporting radius is only `sqrt(2)/4`.

This suggests a narrower contradiction strategy for the asymptotic conjecture. If a sequence of primes had `T_p/sqrt(n)` bounded away from 1 for a reason intrinsic to the odd gluing step, then the exact polar formula would produce a sequence of normalized odd-frequency weighted separators. R20-ODD1 already prevents such separators from having unweighted `l1` mass smaller than order `sqrt(m)`. What remains is to combine that with a Paley-specific lower envelope for the even-feasible weights `a_j` (or a different weighted character-sum inequality) at the orientation-positive sink.

This is a sharper remaining obligation than “prove Paley RIP” or “estimate an extreme eigenvalue.”

## 8. What is now proved, what failed, and what is still missing

### Exact results proved on the page this run

1. **R20-DYADIC1:** exact two-scale formula (3.8) plus polar formula (3.9) for the cyclic positive moment LP.
2. **R20-ODD1:** all-prime one-point `l1` lower bound (5.3) for the odd Paley partial-Fourier subspace, from quartic-coset/Jacobi sums.
3. **Weighted corollary (5.13):** flat enough even-feasible outer measures automatically have an odd zonotope radius of the correct `m^{-1/2}` order.
4. **p=17 exact self-check:** the even relaxation alone overestimates the lift; the odd radius is exactly `sqrt(2)/4`, and the two-scale formula returns the known exact theta value.

### Routes that failed or remain insufficient

- Optimizing only the even/index-two relaxation fails already exactly at p=17.
- Determinant/DPP averaging controls signed bases but does not force positivity.
- The one-point Jacobi/Kashin bound gets the correct square-root **order**, but not the sharp source constant by itself.
- Random-circulant/RIP methods currently incur a logarithmic loss and do not resolve the deterministic Paley positivity geometry.

### Remaining source obligation

A sufficient next theorem would construct, for the Paley edge set and for its complementary theta partner, an even-feasible outer probability `a_p` such that

\[
a_{p,0}\asymp m^{-1/2},
\qquad
\rho_O(a_p)\asymp m^{-1/2},
\]

with the **sharp coupled constants** forcing

\[
\frac12\left(a_{p,0}+\min\{a_{p,0},\rho_O(a_p)\}\right)
\sim\frac1{\sqrt{2m}}.
\tag{8.1}
\]

Equivalently, one needs a weighted directional Kashin inequality adapted to an even-feasible Paley outer measure at the correct constant. This is narrower than full Paley ETF/RIP.

## 9. Current literature / failure log

Dated query families checked on 2026-09-17 included:

- `Paley graph Conjecture 26 theta one localization 2026`;
- `localized Paley Lovasz theta asymptotic resolution`;
- `Magsino Mixon Parshall Paley localization linear program`;
- `random circulant Lovasz theta sparse Fourier positivity`;
- `volume sampling unbiased pseudoinverse determinant sampling`;
- `Kashin half dimensional Fourier subspace l1 l2 Euclidean section`;
- `Paley quartic coset Jacobi sum Fourier coefficient`.

Findings used here:

- the live source still states Conjecture 26;
- Magsino--Mixon--Parshall remains the primary published localized-circulant LP source;
- the 2025 random-circulant Lovasz-theta paper says exact behavior remains open and proves square-root scale up to a `log log` factor using DFT/RIP machinery;
- Dereziński--Warmuth volume sampling supplies generic determinant-weighted unbiasedness / inverse-moment prior art, so those mechanisms are not claimed new;
- Kashin/Euclidean-section literature gives random-subspace `l1/l2` geometry, but no Paley-specific sharp weighted directional theorem matching (8.1) was found in the bounded search.

No access failure changed the mathematical conclusion. Negative search results are not novelty certificates.

## 10. Directed audit duty

The newest R01 report is

`runs/R01/20260917T0402Z_rotation_screen_th17_th18_2e6f7c91.md`.

It is a post-closure successor-admission screen, not a new source-matching closure/paper package. It records I0024 as already internally closed with the prior R20 and P26 audits, I0113 as rotated, and no admitted successor package. Therefore the R20 directed-audit gate is **not triggered** this run; I did not fabricate a redundant audit.

Existing independent R20/I0100 audit evidence remains, among others:

- `R19-AUDIT-R20-I0100-P181-01 = PASS_EXACT_FINITE_CASE`;
- `R19-AUDIT-R20-I0100-P241-02 = PASS_EXACT_FINITE_CASE`;
- `R19-AUDIT-R20-I0100-TUR1-05 = PASS_ALGEBRAIC_CORE` for the Turan reformulation only.

There is no P26 source/asymptotic closure audit, and no closure is claimed.

## 11. Model/reasoning escalation state

The current repository deployment/RESULTS records still say the exposed native scheduler surface supports fields such as title/prompt, schedule/timing, enabled state and timing mode, but **does not expose a model selector, a reasoning-effort selector, authenticated completed-run model telemetry, or a guaranteed full-hour execution control**. Therefore putting `GPT-6 / maximum` in prompt text cannot force or verify that runtime configuration.

To actually fix this, the product/workspace scheduler must expose model + reasoning controls (and completed-run telemetry), or an authorized platform/workspace owner/support path must migrate/update the task in a context that owns those settings. A GitHub prompt edit cannot do it.

The old P26 `You cannot modify this task` event is preserved as an authorization/context failure, not as evidence that P26 can never be updated: the current root ledger says the full P26 prompt update later succeeded in another authorized context. If the denial recurs, the legitimate workaround is the owning authorized product/workspace context or platform/admin support — **not** a duplicate schedule, permission bypass, or a claim that repository text changed native routing.

No scheduler change was attempted here.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R20
  source: "Afonso S. Bandeira, Randomstrasse 2025, Conjecture 26 / I0100"
  target: "theta(complement G_{p,1}) ~ sqrt(p/2), one-localized Paley graph"
  fixed_metric: "largest admissible prime with matching exact primal/dual source-normalized theta certificates"
  metric_before: 1021
  metric_after: 1021
  movement: "NO MOVEMENT"
  exact_covered_primes: [5, 13, 17, 29, 41, 181, 241, 421, 541, 601, 661, 1009, 1021]
  status: "PARTIAL / SOURCE OPEN"
  unchanged_count: 1
  tried_moves: [4, 23, 29]
  exact_new_results:
    - "R20-DYADIC1 exact pair/zonotope variational formula"
    - "R20-ODD1 one-point Paley odd-subspace Kashin/Jacobi bound"
    - "p=17 exact dyadic-zonotope self-check"
  exact_evidence:
    - "artifacts/R20/i0100_p17_dyadic_zonotope_selfcheck.py @ d5493bad8c2f413a064e93c5cbeea0b474ecd375"
    - "artifacts/R20/i0100_p17_dyadic_zonotope_selfcheck.out @ 566d45654d1a02795afe96890bafb309b08cd21d"
    - "existing corrected p=1021 primal/dual interval certificate retained from preceding report"
  audit_ids:
    - "R19-AUDIT-R20-I0100-P181-01=PASS_EXACT_FINITE_CASE"
    - "R19-AUDIT-R20-I0100-P241-02=PASS_EXACT_FINITE_CASE"
    - "R19-AUDIT-R20-I0100-TUR1-05=PASS_ALGEBRAIC_CORE (scope limited)"
  remaining_obligation: >-
    Prove the sharp weighted two-scale bound: construct/control an even-feasible
    Paley outer probability a with the correct a_0 scale and a weighted odd
    zonotope radius rho_O(a) at the sharp constant, and do the corresponding
    complementary side (or an equivalent source-level argument). Finite exact
    certificates alone do not settle the asymptotic.
  next_moves: [8, 26, 28]
```

Shared roots/peer files were not edited. No email, Drive, public posting, purchases, permission changes, or scheduler changes were performed.

**NO CLOSURE CLAIM.**
