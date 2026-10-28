TASK: B18 ACCOUNT: account02 RUN: 2026-09-21T15:34:36.140986+00:00 — FEI proof integration: KL-projection Han credit and recombination gap

Status: OPEN / PARTIAL. Full Friedgut–Kalai Fourier entropy-influence (FEI) remains OPEN / NOT PROVED.

Execution context: WITHOUT_VERIFIED_BRAIN. This run used no authenticated math_brain retrieval or receiver-side brain context.

Model self-report: GPT-5.6 Sol.
Reasoning effort requested: maximum actually supported.
Configured reasoning level: UNKNOWN / not exposed.
Provider reasoning usage: null / not exposed.

## 0. Fresh control and scientific source

Authenticated fleet control was resolved from `yspennstate/math-research-brain` main at
`14c6dfefb9a567d99dea06c7cd48dbb38e7a56c9`. Its SHA-256 is
`e2cf6cf6cb8c4941b55a12284a4e69ac75747e3198e0bb34df42ec9f30520aa6`.
Those two SHA-256 values retain prior exact-byte provenance for the unchanged immutable README blob; they are not relabelled as fresh hashes of connector-rendered JSON.

The first recovered `math-open-problems` master was
`f080552b0e8328c13f865bc6f830e91ee9d5265d`. During the run master advanced, and the latest scientific freshness check before this report saw
`0f10523935d7447dc059438e90c3f656e81e3f01`, including the fresh affine-tensor direct-product theorem.

Current owner correction was applied: unrestricted FEI has no known finite upper bound and the current certified lower bound is already above
`6.521845710923046575`; the older `6.4547837` value is a read-once/Hod-class scale, not the unrestricted target.

Creative moves used this run:
- FLEET_RULES #11, dualize: reinterpret the Han deficit as loss of KL total correlation under coordinate projection.
- #25, count the same thing twice: identify the same credit both as a Han entropy deficit and as product-measure KL dissipation.
- #30, one scale/direction at a time: derive the exact fixed-q descent toll before attempting any multiscale summation.

The substantive change is an exact integration theorem: **the inherited restriction toll is recombination cost minus a KL-contraction credit**. This also fixes a potential double-counting bug when combining the fresh B15 packet/product bridge with the B18 Han descent.

## 1. Setup

Let `f:{0,1}^n->{-1,+1}` be Boolean and let the spectral sample be

`X in {0,1}^n`,  `mu(x)=fhat(x)^2`.

Write

`j_i = Pr[X_i=1] = Inf_i(f)`,
`H = H(X) = H(f)`,
`I = sum_i j_i = I(f)`.

Let `nu=prod_i Bern(j_i)` be the independent product law with the same coordinate marginals, and define the base-2 total correlation

`T = D_KL,2(mu || nu) = sum_i h_2(j_i) - H`.                         (1.1)

For a coordinate set `B subseteq [n]`, let `mu_B` be the marginal of `X_B`, let `nu_B=prod_{i in B} Bern(j_i)`, and put

`T_B = D_KL,2(mu_B || nu_B)
     = sum_{i in B} h_2(j_i) - H(X_B)`.                              (1.2)

For `0<=q<=n`, define the fixed-cardinality averages

`h_q = E_{|B|=q} H(X_B)`,
`\bar T_q = E_{|B|=q} T_B`.                                         (1.3)

Thus `h_0=\bar T_0=0`, `h_n=H`, and `\bar T_n=T`.

The inherited B18 Han deficit is

`A_q = h_q - (q/n) H`,  `1<=q<=n-1`.                                (1.4)

Han's inequality gives `A_q>=0`.

## 2. PROVED: Han deficit is exactly KL contraction under random coordinate projection

### Theorem B18-KL-PROJECTION-01

For every probability law `mu` on `{0,1}^n` (Booleanity is not needed for this theorem) and every `1<=q<=n-1`,

`A_q = (q/n) T - \bar T_q`.                                         (2.1)

Equivalently, the rescaled Han credit

`K_q := (n/q) A_q`                                                   (2.2)

has the exact forms

`K_q = T - (n/q)\bar T_q
     = n( T/n - \bar T_q/q ) >= 0`.                                 (2.3)

So `K_q` is the drop in **total-correlation density** between the full law and a uniformly random q-coordinate projection.

#### Proof

Average (1.2) over `|B|=q`. Every coordinate occurs in a proportion `q/n` of the q-subsets, hence

`\bar T_q
 = (q/n) sum_i h_2(j_i) - h_q`.                                     (2.4)

From (1.1),

`(q/n)T
 = (q/n)sum_i h_2(j_i) - (q/n)H`.                                   (2.5)

Subtract (2.4) from (2.5):

`(q/n)T-\bar T_q = h_q-(q/n)H=A_q`.                                 (2.6)

This proves (2.1)-(2.3). QED.

### Mutual-information slope form

For `0<=r<=n-1`, define

`m_r = E_{i,B: |B|=r, i notin B} I(X_i ; X_B)`.                     (2.7)

Then

`\bar T_{r+1}-\bar T_r = m_r`,                                      (2.8)

because for each pair `(B,i)`,

`T_{B union {i}}-T_B
 = h_2(j_i)-H(X_i|X_B)
 = I(X_i;X_B)`.                                                      (2.9)

Therefore

`T = sum_{r=0}^{n-1} m_r`,  with `m_0=0`,                            (2.10)

and

`A_q = q(n-q)/n *
       ( avg_{r=q,...,n-1} m_r - avg_{r=0,...,q-1} m_r )`.           (2.11)

Consequently

`K_q = (n-q) *
       ( avg_{r=q,...,n-1} m_r - avg_{r=0,...,q-1} m_r )`.           (2.12)

The sequence `m_r` is nondecreasing. For fixed `i`, couple a random r-subset and an `(r+1)`-subset by exposing a random permutation of `[n]\{i}`; mutual information can only increase when another observed coordinate is added. Averaging over `i` preserves the inequality. Formula (2.11) is therefore another direct proof of `A_q>=0`.

If

`d_r := h_{r+1}-h_r`,                                                (2.13)

then the chain rule gives

`d_r = E H(X_i|X_B)`,  and hence `m_r = \bar h-d_r`,                 (2.14)

where `\bar h=(1/n)sum_i h_2(j_i)`. Thus the Han deficit is precisely the curvature/slope-separation of the entropy profile.

For the Bayes prediction error

`eps_r = E min{Pr[X_i=0|X_B], Pr[X_i=1|X_B]}`,                       (2.15)

the binary inequalities `2e<=h_2(e)` and concavity of `h_2` give

`2 eps_r <= d_r <= h_2(eps_r)`.                                     (2.16)

This records exactly where the inherited Bayes upper bound loses information: it replaces the full KL slope profile `m_r` by a single local prediction-error number.

## 3. PROVED: exact restriction toll = recombination cost - KL contraction credit

This section uses the already-proved B18 block-descent identity from
`account02/B18/20260921T133721Z-han-credit-block-descent/REPORT.md`.

Let `g` be an n-variable restriction descendant maximizing

`r(g)=H(g)/I(g)`

over its physical restriction descendants. For a physical block `A` of size `k=n-q`, the exact restriction entropy identity is written

`Delta_A H = B_A + R_A`,                                             (3.1)

where `B_A=H(X_A|X_{A^c})` is the spectral erasure term and `R_A>=0` is the restriction-recombination/JS remainder. Define

`e_A = Delta_A H - r(g) I_A`.                                       (3.2)

Restriction maximality gives `e_A>=0` for every nonempty proper block.

The inherited aggregate identity is

`sum_{|A|=k} e_A
 = sum_{|A|=k} R_A - binom(n,k) A_q`.                               (3.3)

Let

`v_k = binom(n-1,k) = (q/n) binom(n,k)`                              (3.4)

and define the rescaled average recombination cost

`Rcal_q := [1/v_k] sum_{|A|=n-q} R_A`.                              (3.5)

### Theorem B18-KL-RECOMBINATION-02

For every restriction-maximal core `g` and every `1<=q<=n-1`, the exact fixed-q descent toll is

`Gamma_q
 = [sum_A R_A - binom(n,n-q)A_q] / [v_{n-q} I(g)]
 = [Rcal_q - K_q] / I(g).`                                          (3.6)

Moreover there exists a q-dimensional physical restriction child `h` with

`r(h) >= r(g) - Gamma_q`.                                            (3.7)

Thus **the whole fixed-q obstruction is the unpaid part of recombination after subtracting KL contraction**.

#### Proof

The first expression in (3.6) and the child inequality (3.7) are exactly the inherited block-descent theorem. By (3.4),

`binom(n,k) A_q / v_k = (n/q)A_q = K_q`.                            (3.8)

Substitute (3.5) and (3.8) into the inherited expression. QED.

The inherited fibre/Bayes estimate gives, with `c_*=2/ln 2`,

`Rcal_q <= c_* [n(n-q)/q] eps_q`.                                  (3.9)

Therefore

`Gamma_q
 <= c_* [n(n-q)/(q I)] eps_q - K_q/I
 <= c_* [(n-q)/q] - K_q/I`,                                        (3.10)

where the second inequality uses `eps_q<=I/n`.

For the extremal constants `C_n=max H/I` in dimension n, the same argument yields the sharpened recursion

`C_n-C_q
 <= c_* [n(n-q)/(q I(g))] eps_q - K_q(g)/I(g)
 <= c_*[(n-q)/q] - K_q(g)/I(g)`                                    (3.11)

on an n-dimensional extremizer `g`.

### What changed relative to the previous B18 report

The previous report had the negative term `A_q`; it did not identify what information quantity that term actually is. Equations (2.3) and (3.6) show that the negative credit is **exactly the total-correlation density lost under q-coordinate projection**.

This is more than a change of notation because it gives a safe interface to the fresh packet/product-measure theorem and fixes multiplicity: at scale q one may spend only `K_q`, not the full product KL `T` unless `q=1`.

## 4. Integration with B15: the packet bridge feeds K_q only after two exact subtractions

The fresh B15 packet/product bridge
`account02/B15/20260921T150419Z-packet-product-bridge/REPORT.md`
uses the same product law `nu` and proves

`T = D_KL,2(mu||nu) = K_beta + C_in`,                                (4.1)

where `K_beta` is the packet-label KL to the product-shadow packet law and `C_in` is the within-packet conditional KL.

It also proves the bridge identity

`H
 = R + (1/2) sum_i h_2(j_i) + log_2 Z
   - D_KL,2(p||m) - (1/2) C_in`.                                    (4.2)

Combining (1.1) and (4.2) gives the exact conversion

`T
 = (1/2)sum_i h_2(j_i) - R - log_2 Z
   + D_KL,2(p||m) + (1/2)C_in
 = K_beta + C_in`.                                                   (4.3)

Hence the actually spendable q-scale credit is

`K_q
 = K_beta + C_in - (n/q)\bar T_q`                                  (4.4)

or equivalently

`K_q
 = (1/2)sum_i h_2(j_i) - R - log_2 Z
   + D_KL,2(p||m) + (1/2)C_in
   - (n/q)\bar T_q`.                                                 (4.5)

At `q=1`, every one-coordinate law has zero total correlation, so

`K_1=T=K_beta+C_in`.                                                 (4.6)

At every larger q, the projected dependence `(n/q)\bar T_q` is a **reserve** that cannot be spent at the current descent step.

### Non-double-counting consequence

A synthesis may not count the bridge-law KL `D_KL(p||m)` as one negative term and the Han credit as another independent negative term. Equation (4.5) shows the exact accounting: the bridge KL first cancels against `log Z`, the arithmetic remainder `R`, half the marginal entropy, and half the conditional packet credit to produce `T`; then the projected total correlation is subtracted to produce `K_q`.

The B15 one-point-defect stress test makes this mandatory. There,

`log_2 Z ~ (1/2)log_2 n`
and
`D_KL,2(p||m) ~ (1/2)log_2 n`,

so these individually large terms cancel before one reaches the small actual total correlation. Counting `D_KL(p||m)` again as an additional Han payment would manufacture a false logarithmic credit.

This is the main hidden-multiplicity bug ruled out in this run.

## 5. Compatibility with B14, B17, and the newest affine normalization

### B14 mass-weighted erasure theorem

The fresh B14 disjoint-composition theorem gives exact local erasure identities and influence identities for genuine disjoint compositions, including the singleton activation tax. It attacks the **positive erasure/recombination side** of the restriction ledger.

However its `B_{j,k}` erasure term is not automatically the `R_A` recombination term in (3.1). They enter different pieces of the restriction identity. A global synthesis must prove a map from the B14 composition quantities to `Rcal_q`; simply substituting one for the other would be an unsupported representation change.

Concrete nonoverlap:
- B14 should target upper/telescoping control of `Rcal_q` on composition trees.
- B15 should target lower/exact evaluation of `K_q`, beginning from (4.4), not another independent "credit".
- B16 should target Boolean phase/translation constraints forcing KL contraction when marginal laws look dangerously product-like.
- B18 owns the exact `Rcal_q-K_q` ledger and multiscale integration.

### B17 quadratic-leaf peeling

The prior B17 quadratic-leaf theorem proves that for every target `C>=4`, quadratic ANF leaves can be peeled without decreasing folded C-slack. Therefore any counterexample to FEI(C), `C>=4`, has a counterexample representative whose current ANF has no quadratic leaves.

This is compatible with the present descent theorem: after a restriction creates new quadratic leaves, they may be peeled before continuing a counterexample induction.

### Fresh affine/character orbit theorem

The newest B17/account04 theorem at master `0f105239...` proves exact tensor additivity of

`J_aff(f)=min_basis sum_i (1-|E f(x)f(x+v_i)|)/2`

and records the constant-for-constant affine/character normalization of FEI. This closes tensor-power plus cross-block linear mixing as an amplification loophole.

Important compatibility warning: **affine-minimal basis and ANF quadratic-leaf core are two different normal forms.** An arbitrary invertible linear input change can destroy or create ANF leaves. Nothing read this run proves that one representative can be simultaneously `J_aff`-minimal and quadratic-leaf-pruned. The two reductions may each be used, but their hypothesis sets must not be silently intersected.

Likewise, the fresh B17 central-cone normal form is FEI-complete; "one central control" is not by itself an easy subclass. Any proposed bound on `Rcal_q-K_q` that uses cone geometry must use an additional invariant of the gate.

## 6. Exact universal obstruction after this integration

The old B18 wording was "Bayes-Han stability / KL-scale summability." The exact object is now sharper:

`UNPAID_q(g) := Rcal_q(g) - K_q(g) >= 0`                             (6.1)

on a restriction-maximal core.

By (3.6),

`Gamma_q = UNPAID_q/I`.                                              (6.2)

Full FEI would follow from a dimension-independent restriction/peeling Bellman argument in which the cumulative `UNPAID_q/I` along the chosen descent is universally bounded. The crude estimate

`Rcal_q <= c_* n(n-q) eps_q/q`                                      (6.3)

alone gives the old logarithmic loss. The next missing universal implication is therefore not "prove total correlation is large" in isolation. It is:

> **Recombination-versus-KL contraction problem.**
> On the actual hard normal forms, prove that at enough descent scales the recombination cost `Rcal_q` is matched, up to an influence-summable remainder, by the projection KL credit
> `K_q = T-(n/q)\bar T_q`.

This formulation automatically preserves signs and multiplicity:
- full `T` is spendable only at q=1;
- at q>1, projected correlation must remain reserved;
- B15's large bridge KL is not a second copy of the same payment;
- B14 erasure is not identified with recombination without a theorem.

A useful half-scale specialization is

`C_n-C_{ceil(n/2)}
 <= c_* + O(1/n) - K_{ceil(n/2)}/I`,                                (6.4)

with the exact non-rounded formula given by (3.11). Therefore a hard sequence must repeatedly exhibit **small total-correlation-density drop under large coordinate projections** unless another exact improvement lowers `Rcal_q`. That is a concrete structural obstruction to hand to the spectral-compression/profile workers.

## 7. Decisive sanity checks

The analytic proof above does not depend on finite verification. A standard-library script in this run directory checks only algebraic implementation:

- four random full-support laws in dimensions 2,3,4,5;
- the uniform product law, which is the squared spectrum of a bent function in appropriate even dimensions;
- the exact squared spectrum of the 8-variable one-point defect.

It verifies (2.1), (2.11), and monotonicity of `m_r`. Maximum observed absolute residual was below `6e-16` bits.

Two stress tests matter conceptually.

1. **Uniform/bent product spectrum.** Here `T=K_q=0` for every q. Thus KL credit does not universally cancel recombination. This is not a FEI obstruction: the uniform spectrum has `H/I=2`. It refutes any claim that "Booleanity forces positive total correlation" without a low-influence or other qualifier.

2. **One-point defect.** The B15 bridge KL and `log Z` are both logarithmically large while their net contribution to `T` is small. This directly stress-tests the non-double-counting rule (4.5).

## 8. PROVED / CONDITIONAL / OPEN / refuted-lemma ledger

### PROVED in this run

P1. For every distribution on the cube,
`A_q=(q/n)T-\bar T_q` and `K_q=T-(n/q)\bar T_q`.

P2. `K_q` equals `(n-q)` times the gap between late-scale and early-scale average mutual-information slopes, equation (2.12).

P3. Combining P1 with the already-proved B18 block descent gives the exact toll
`Gamma_q=(Rcal_q-K_q)/I`.

P4. Combining P1 with the fresh B15 packet bridge gives equations (4.4)-(4.5), specifying exactly how packet/product KL enters the Han descent.

### PROVED inherited and used at exact scope

I1. B14's mass-weighted erasure identities hold for disjoint compositions only.

I2. B17 quadratic-leaf peeling holds at target C>=4; it is not a theorem that arbitrary central-cone or shared-variable structures are easy.

I3. B17 central-cone normal form is FEI-complete; central-cone geometry alone cannot be used as a restricted-class shortcut.

I4. B17/account04 affine-character direct-product additivity closes tensor-plus-linear-mixing amplification; simultaneous affine-minimal and leaf-core normal form is not yet proved.

### CONDITIONAL

C1. A universal, summable bound on `Rcal_q-K_q` along a valid restriction/peeling descent would prove full FEI with the corresponding dimension-independent constant.

C2. A proof that B14's exact composition erasure payments dominate the relevant `Rcal_q` minus the reserved projected total correlation would close the disjoint-composition branch, not unrestricted FEI unless extended beyond its hypotheses.

### OPEN

O1. Prove a universal scale-selection or potential inequality making cumulative `UNPAID_q/I` bounded.

O2. Quantitatively force `K_q` from Booleanity in the dangerous low-influence/near-product regime.

O3. Relate the packet bridge to projected packet/product KL at q>1 without losing the reserve `\bar T_q`.

O4. Determine whether one can choose a representative simultaneously useful for affine-orbit normalization and ANF leaf peeling; no such compatibility theorem is currently available.

### REFUTED / forbidden synthesis steps

R1. "Use `D_KL(p||m)` and the Han credit as two independent negative terms." False by exact identity (4.5); it double counts.

R2. "Use all of total correlation T as the Han payment at every q." False: only `K_q=T-(n/q)\bar T_q` is available.

R3. "Identify B14 erasure B with restriction recombination R." Unsupported; they are distinct terms.

R4. "Boolean spectral laws always have positive total correlation." False: bent spectra are exact product/uniform laws.

R5. "Affine-minimal basis and quadratic-leaf core can be assumed simultaneously." Not proved and potentially representation-dependent.

Full FEI is therefore still OPEN / NOT PROVED.

## 9. Literature/scope check

Fresh primary-source checks on 21 September 2026 found no unrestricted FEI upper bound:

- Vladimir N. Potapov, arXiv:2609.21563 (18 Sep 2026), proves FEI for plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2. Structured classes only.
- María José González, Paul MacManus, María Cristina Pereyra, arXiv:2606.00246 (29 May 2026), develops restriction/stopping-tree results; its key universal restriction inequality would imply full FEI but is not proved for all Boolean functions.
- Peijie Li and Guangyue Han, arXiv:2512.03117 (2 Dec 2025), strengthen Han's entropy-influence inequality but retain the coordinate influence-profile entropy term; it does not give a dimension-independent FEI upper bound.

The current optimization-constants ledger reports a certified monotone lower bound
`C_FEI > 6.521845710923046575`. This is a lower bound only; the universal upper bound remains unknown.

No publication-priority claim is made for the KL-projection interpretation or the integrated ledger here. The new value of this run is the exact project-level implication (3.6) and the resulting no-double-counting interface between currently active proof routes.

## 10. Next nonoverlapping work

- B12 spectral compression: attack lower bounds on `K_q` in the low-influence near-product regime, preferably directly at half-scale.
- B13 Booleanity/profile: characterize which total-correlation projection profiles `q -> \bar T_q/q` can arise from Boolean spectra.
- B14 erasure/selector: bind its exact mass-weighted erasure terms to `Rcal_q`, preserving activation/refund signs.
- B15 spectral remainder: project the packet/product bridge to q-coordinate marginals and estimate the reserve `(n/q)\bar T_q`; do not add bridge KL twice.
- B16 signed/shared transport: derive Boolean phase constraints that force KL-density drop or directly lower `K_q`.
- B17 mechanisms: continue structural normal forms but record whether they are compatible with affine basis optimization.
- B18 integration: next run should attempt an actual summability theorem for `UNPAID_q`, not another reformulation.

Accompanying sanity script SHA-256:
`0a8fc586be9f1f6c14cb22ea32cf345e4bb42222c326fb93f722a099f88110aa`.

Recorded sanity output SHA-256:
`161829c7bcaa509b1f4236dea97d61e5447a3886abc9e8ccbb787d919488d407`.
