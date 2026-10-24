Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **Movement: `T_corr=1 -> 2`. Methods tried: B14/B15/B4. New theorem-sized PARTIAL result: every balanced-phase amplitude-band family below has exact radial power exponent `alpha`; in particular a new continuum-amplitude, non-i.i.d., non-Hermitian C2 family is classified. Campbell--O'Rourke Question 1.9 remains OPEN.**

# HARD7-02 — Question 1.9: balanced-phase amplitude bands have the input power exponent

Status: **PARTIAL / source Question 1.9 remains OPEN by bounded current-status search / theorem candidate has an on-page proof and exact finite-algebra self-check but no independent audit.**

Frozen source metric:

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class of mu_{alpha,theta} is rigorously determined`.

Before: `T_corr=1` (the fixed-amplitude two-orbit family `vartheta_x` from the preceding run).

After: **`T_corr=2`**, counting only the explicit new uniform amplitude-band family defined in Section 3 below. The broader theorem is not used to inflate the count.

## 1. Continuity, ownership, repository state, and capability honesty

I resumed the active exclusive canonical claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

and the latest completed checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T18-14-04Z__q19-mahler-peeling-tail-exponent.md`.

At run start I re-read the controlling HARD7 file, both new-method directives, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the active claim, newest own Q1.9 reports, repository-wide Campbell--O'Rourke/claim aliases, and the neighboring C0032 terminal handoff. The claim remains exclusive to HARD7-02. C0032 is the distinct i.i.d. heavy-tailed circular-law density problem and remains in terminal handoff. No canonical claim was overwritten and no shared root ledger was edited.

The scheduler/runtime capability situation is still the one recorded by the controlling files. The exposed interface has task title, prompt, schedule/timing mode, enabled state and ordinary run controls, but **no binding model selector, no reasoning-effort selector, no authenticated effort telemetry and no guaranteed duration field**. Thus `GPT-6 / maximum` is a prompt request only; this run cannot honestly claim it. A real change requires a product/backend surface that exposes binding model/effort controls or an authorized account/workspace context in which those controls exist. Historical `You cannot modify this task` responses for P26/P01/P03 were permission-context failures. The compliant workaround is the owning/authorized context or platform support/ownership transfer; never a duplicate task or permission bypass. Repository evidence says P26 later became editable in a different authorized context, which does not imply every denied task is now editable. No scheduler mutation was attempted here.

No Gmail, Drive, public posting, paid compute, workflow execution, force push, neighboring-track edit, or permission bypass was performed.

## 2. Exact source statement and current-literature refresh

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Section 1.3 asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The source's Definition 1.3 gives C1, Definition 1.4 gives C2, and Theorem 1.6 says that under C2 the empirical spectral law of `A_n=X_n/a_n` converges in probability to deterministic `mu_{alpha,theta_d}`, depending only on `(alpha,theta_d)`. The source explicitly contrasts the i.i.d. axis-supported case, whose limiting ESD has a much lighter tail and all finite moments, with the Hermitian case, whose limiting law inherits the entry power tail.

Primary-source URL checked this run: `https://arxiv.org/html/2010.01261v3`, especially Definition 1.3/1.4, Theorem 1.6, and lines surrounding Question 1.9.

Fresh bounded 19 September 2026 searches used the exact title/authors, exact `Question 1.9` wording, `theta_d`, `mu_{alpha,theta_d}`, `tail behavior`, `heavy-tailed elliptic`, `PWIT`, and 2023--2026 follow-up terms. They recovered the 2022 source; Campbell--O'Rourke, *Spectrum of Levy--Khintchine Random Laplacian Matrices*, J. Theor. Probab. 37 (2024), DOI `10.1007/s10959-023-01275-4`; and Carpenter--O'Rourke, *The Limiting Spectral Distribution for Sparse Elliptic Random Matrices*, arXiv:2508.04891 (2025). I did **not** locate a paper claiming a general resolution of Question 1.9 or the balanced-phase amplitude-band theorem below. This is bounded negative evidence, not a worldwide novelty certificate.

## 3. New source-valid family and the fixed second metric unit

Fix `0<alpha<2` and put

`beta=alpha/2 in (0,1)`.

Let `H` be independent of `Phi`, where `Phi` is uniform on `[0,2pi)`. Assume

1. `H` and `1-H` have the same law;
2. for some `0<delta<1/2`, `P(delta <= H <= 1-delta)=1`.

Define the unit-sphere random vector

`W_H=(sqrt(H)e^{i Phi}, sqrt(1-H)e^{-i Phi})`,

and set

`theta_H=Law(W_H)`.

The explicit new family used for the metric is

`H_delta ~ Uniform[delta,1-delta]`,

`theta_delta = Law(W_{H_delta})`, `0<delta<1/2`.                 (3.1)

It has continuum amplitude support. It is therefore not a relabeling of the preceding two-point-amplitude family `vartheta_x`. Both coordinates are nonzero almost surely, so it is not the i.i.d. axis-supported endpoint; its support is not contained in the Hermitian circle `w=conj(z)`, so it is non-Hermitian.

Choose the exact representative

`P(R>r)=r^{-alpha}`, `r>=1`,

with `R` independent of `(H,Phi)`, and set

`(xi_1,xi_2)=R W_H`, `zeta=0`, `a_n=n^(1/alpha)`.                (3.2)

Then C1 holds exactly: `||(xi_1,xi_2)||=R`, so for every continuity set `D` of `theta_H` and `r>0`, for all sufficiently large `n`,

`n P(W_H in D, R>=r a_n)=theta_H(D) r^{-alpha}`.                 (3.3)

C1(ii) is trivial because `zeta=0`, and C2(ii) has constant `c=1`.

For C2(i), suppose `a z+b w=0` on `supp(theta_H)`. Fix any `h` in `supp(H)` and vary the phase. Then

`a sqrt(h)e^{i phi}+b sqrt(1-h)e^{-i phi}=0` for every `phi`.

Multiplying by `e^{i phi}` gives

`a sqrt(h)e^{2i phi}+b sqrt(1-h)=0` for every `phi`,

which forces `a=b=0`. Hence C2(i) holds. Theorem 1.6 therefore supplies the deterministic law `mu_{alpha,theta_H}` for this representative.

## 4. B14 — the acting group identifies the correct invariant

The circle group acts on the unit sphere by

`T_u(z,w)=(u z,u^{-1}w)`, `|u|=1`.                              (4.1)

For every fixed `h`, the conditional law of `W_H` given `H=h` is Haar measure on one orbit of this action. The product

`z w = sqrt(h(1-h))`                                               (4.2)

is invariant on that orbit.

This is exactly the symmetry needed by the determinant argument: after conditioning on all variables except one selected edge phase, the characteristic determinant has Laurent degree one in `u`. Randomizing `H` does not change the phase degree; it only randomizes the orbit invariant (4.2).

**B14 outcome: success.** The mechanism is not “constant reciprocal product”; it is Haar averaging on the balanced `S^1` action plus integrability of the invariant logarithm.

## 5. B15 — break the old constant-product rigidity

The preceding `vartheta_x` family had deterministic

`|W_1W_2|=sqrt(x(1-x))`.

The uniform-band family (3.1) deliberately breaks that rigidity: `|W_1W_2|=sqrt(H(1-H))` has a genuine continuum distribution. The counterexample-oriented question was whether amplitude randomness can destroy the power-law exponent even though each phase orbit has the reciprocal-edge mechanism.

The theorem below shows it does not, as long as the amplitude stays away from the axes. The random amplitude changes only constants through

`m_beta := E H^beta`,                                             (5.1)

and

`ell_H := E log sqrt(H(1-H))`,                                    (5.2)

not the power exponent. Thus the fixed-product structure from the preceding run was not essential.

**B15 outcome: success.** A genuinely larger dependence geometry retains the exact exponent.

## 6. B4 — complete class theorem

### Theorem 6.1 — balanced-phase amplitude-band exponent

Under the assumptions in Section 3, for every `0<alpha<2`,

`lim_{r->infinity} [-log mu_{alpha,theta_H}({|z|>r})]/log r = alpha`.  (6.1)

In particular this holds for the continuum-amplitude family `theta_delta` in (3.1).

### Proof, Step 1: all radial moments below `alpha`

Let `Z=|xi_1|^2=R^2 H`. By the symmetry `H =_d 1-H`, both coordinate marginals are the same. For every `y>=1`,

`P(Z>y)=E P(R>sqrt(y/H) | H)=m_beta y^{-beta}`.                   (6.2)

A row of `A_n=X_n/n^(1/alpha)` has independent off-diagonal squared magnitudes with this marginal. Dominate its squared Euclidean norm by

`S_n := n^(-1/beta) sum_{j=1}^n Z_j`,                             (6.3)

where the `Z_j` are independent copies of `Z`.

For `n>=2`, `t>=1`, set

`T=(t/2)n^(1/beta)>=1`.

Split according to a single large summand. The union bound and (6.2) give

`P(max_j Z_j/n^(1/beta)>t/2) <= 2^beta m_beta t^(-beta)`.         (6.4)

Also

`E[Z 1_{Z<=T}] <= int_0^T P(Z>s) ds`
`<= 1 + m_beta T^(1-beta)/(1-beta)`.                              (6.5)

Markov's inequality therefore yields

`P(n^(-1/beta) sum_j Z_j 1_{Z_j<=T}>t/2)`
`<= 2 n^(1-1/beta)t^(-1)`
`   + [2^beta m_beta/(1-beta)] t^(-beta)`
`<= [2 + 2^beta m_beta/(1-beta)] t^(-beta)`.                      (6.6)

Combining (6.4)--(6.6),

`P(S_n>t) <= C_beta t^(-beta)`,                                   (6.7)

where

`C_beta := 2 + 2^beta m_beta (2-beta)/(1-beta)`.                  (6.8)

Now fix `0<p<alpha` and put `q=p/2<beta`. Tail integration gives

`E S_n^q <= 1 + q C_beta/(beta-q) =: M_p`.                        (6.9)

For `0<p<2`, Weyl log-majorization followed by the Schur--Horn/Schatten row inequality gives for every finite matrix

`sum_k |lambda_k(A_n)|^p <= sum_k s_k(A_n)^p`
`<= sum_i ||Row_i(A_n)||_2^p`.                                    (6.10)

Taking expectations, dividing by `n`, and using (6.9),

`E int |z|^p mu_{A_n}(dz) <= M_p`.                                (6.11)

Theorem 1.6 gives weak convergence in probability of `mu_{A_n}` to deterministic `mu:=mu_{alpha,theta_H}`. Apply that convergence to `min(|z|^p,K)` and then let `K->infinity` by monotone convergence. Thus

`int |z|^p mu(dz) <= M_p`, `0<p<alpha`.                           (6.12)

Writing

`F(r):=mu({|z|>r})`,

Markov gives

`F(r) <= M_p r^(-p)`.                                             (6.13)

Hence

`liminf_{r->infinity} [-log F(r)]/log r >= alpha`.                (6.14)

### Step 2: one selected edge, exact phase peeling

Fix `s>=1`. Call an unordered edge `e={i,j}` an `s`-exceedance when

`R_e > s n^(1/alpha)`.                                            (6.15)

Conditional on exceedance, write

`R_e=s n^(1/alpha)Y`,

where

`P(Y>y)=y^(-alpha)`, `y>=1`.                                      (6.16)

Let `X=Y^2`. Its density is

`beta x^(-beta-1) 1_{x>=1}`.                                     (6.17)

Condition on all variables except the selected edge's `(H,Phi,Y)`. Put `u=e^{i Phi}` and `h=H`. The two normalized directed entries on the edge are

`sY sqrt(h) u`, `sY sqrt(1-h) u^(-1)`,

so their product is

`q=s^2 sqrt(h(1-h)) X`.                                           (6.18)

For fixed spectral parameter `z`, let

`D(u)=det(zI-A_n)`.

In the Leibniz expansion a permutation uses neither selected directed entry, exactly one, or both. Therefore

`D(u)=c_{-1}u^(-1)+c_0+c_1u`,                                    (6.19)

and the phase-zero coefficient is

`c_0=A_0-qB`,                                                     (6.20)

where `A_0` is the determinant with both selected entries set to zero and

`B=det(zI-A_n^{\setminus{i,j}})`                                 (6.21)

is the principal minor deleting the two endpoints. Indeed, terms using both entries force the transposition `i<->j`; the permutation sign contributes the minus sign in (6.20).

Multiply (6.19) by `u`. For every polynomial `a_0+a_1u+a_2u^2`, Jensen's formula and the factorization into roots give

`(1/(2pi)) int_0^{2pi} log|a_0+a_1e^{it}+a_2e^{2it}| dt`
`>= log|a_1|-log 2`.                                              (6.22)

(The inequality is just `|a_1|<=2 M(P)` for the Mahler measure `M(P)`.) Hence

`E_Phi log|D(e^{i Phi})| >= log|A_0-qB|-log 2`.                  (6.23)

### Step 3: Pareto logarithmic anti-concentration for every `alpha`

For every `c in C`,

`E log|X-c| >= -alpha`.                                           (6.24)

To prove this, first `|X-c|>=|X-Re(c)|`. The logarithm can be negative only on the interval `|x-Re(c)|<1`. The density in (6.17) is at most `beta`; because `log|t|<0` on `|t|<1`,

`int beta x^(-beta-1) log|x-Re(c)| 1_{|x-Re(c)|<1} dx`
`>= beta int_{-1}^1 log|t| dt = -2 beta = -alpha`.                (6.25)

Outside that interval the logarithm is nonnegative, proving (6.24).

For `B!=0`, factor (6.20) using (6.18), apply (6.24), and then average over `H`:

`E_{Phi,Y,H} log|det(zI-A_n)|`
`>= 2 log s + ell_H - (alpha+log 2)`
`   + log|det(zI-A_n^{\setminus{i,j}})|`.                         (6.26)

If `B=0`, the right side is `-infinity` and the inequality is trivial in the extended sense. Since `H in [delta,1-delta]`, `ell_H` is finite.

### Step 4: positive density of disjoint exceedance edges

Let `G_s` be the graph of `s`-exceedance edges. By the exact Pareto representative,

`G_s = G(n,1/(s^alpha n))`.                                       (6.27)

Let `M_s` be its set of isolated edges and `m_s=|M_s|`. These edges are pairwise vertex-disjoint, and conditional on `G_s` their phases, amplitudes and overshoots remain independent. Iterating (6.26) across all isolated edges gives

`E_selected log|det(zI-A_n)|`
`>= m_s K_s + log|det(zI-A_n^{\setminus V(M_s)})|`,               (6.28)

where

`K_s=2log s+ell_H-(alpha+log2)`.                                  (6.29)

The exact isolated-edge expectation is

`E[m_s/n]`
`= [(n-1)/(2s^alpha n)] (1-1/(s^alpha n))^(2(n-2))`
`-> e^(-2/s^alpha)/(2s^alpha)`.                                  (6.30)

Logarithmic singularities at finitely many circle points are handled by truncating the logarithm below and passing monotonically; no eigenvalue perturbation estimate is used.

### Step 5: circular logarithmic potential

For every finite matrix `M`, Jensen's formula gives

`(1/(2pi)) int_0^{2pi} log|det(re^{it}I-M)|dt`
`= sum_j log max(r,|lambda_j(M)|)`.                               (6.31)

Define

`V_n(r)=(1/n) sum_j log^+(|lambda_j(A_n)|/r)`.                    (6.32)

Circle-average (6.28), use (6.31), and bound the `(n-2m_s)`-dimensional minor's circular average below by `(n-2m_s)log r`. After subtracting `n log r`,

`E V_n(r) >= E[m_s/n] [K_s-2log r]`.                             (6.33)

Choose

`c_H := exp(ell_H/2)/(2 exp((alpha+1)/2))`                         (6.34)

and set `r=c_H s`. Then exactly

`K_s-2log r = 1+log 2`.                                          (6.35)

For every fixed `r>0`, (6.11) makes `log^+(|z|/r)` uniformly integrable with respect to the finite ESDs: for any fixed `p in (0,alpha)`,

`sup_n E int_{|z|>L} log^+(|z|/r) mu_{A_n}(dz)`
`<= [sup_{u>L} log^+(u/r)/u^p] M_p ->0`.                         (6.36)

Using Theorem 1.6 first on bounded truncations and then (6.36),

`E V_n(r) -> V(r):=int log^+(|z|/r) mu(dz)`.                      (6.37)

Combine (6.30), (6.33)--(6.37). For every `s>=1`,

`V(c_Hs) >= (1+log2)e^(-2/s^alpha)/(2s^alpha)`.                   (6.38)

Equivalently, for `r>=c_H`,

`V(r) >= A_H r^(-alpha) exp[-2(c_H/r)^alpha]`,                    (6.39)

where

`A_H=(1+log2)c_H^alpha/2 >0`.                                    (6.40)

In particular,

`V(r) >= A_H e^(-2) r^(-alpha)` for all `r>=c_H`.                 (6.41)

### Step 6: from integrated potential to the pointwise tail

Layer cake gives the exact identity

`V(r)=int_r^infinity F(t) dt/t`.                                  (6.42)

Fix any `p in (0,alpha)` and choose `gamma>alpha/p`. Using monotonicity of `F` and (6.13), for `r>1`,

`V(r)`
`<= int_r^{r^gamma} F(t)dt/t + int_{r^gamma}^infinity M_p t^(-p)dt/t`
`<= (gamma-1)log r F(r) + (M_p/p) r^(-p gamma)`.                  (6.43)

Because `p gamma>alpha`, the last term is at most `(A_H e^(-2)/2)r^(-alpha)` for all sufficiently large `r`. Comparing (6.41) and (6.43) gives

`F(r) >= [A_H e^(-2)/(2(gamma-1))] r^(-alpha)/(log r)`            (6.44)

for all sufficiently large `r`. Therefore

`limsup_{r->infinity} [-log F(r)]/log r <= alpha`.                (6.45)

Together with (6.14), this proves (6.1). `QED`

## 7. Exact worked uniform-band slice and finite self-check

Take `alpha=1`, `delta=1/4`, and `H~Uniform[1/4,3/4]`. Then exact integration gives

`m_{1/2}=E sqrt(H) = -1/6 + sqrt(3)/2`
`=0.699358737117771980...`,                                       (7.1)

and symmetry gives

`ell_H=E log sqrt(H(1-H))`
`=-1+log(3sqrt(3)/4)`
`=-0.738375928117726082...`.                                      (7.2)

The scale in (6.34) is

`c_H=3^(3/4)e^(-3/2)/4`
`=0.127156693669448873...`,                                       (7.3)

and the bracket in (6.35) is exactly `1+log2`.

The elementary constants were checked exactly, after the idea checkpoint was committed, by

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T19-14-06Z__q19-balanced-phase-band-check.py`

commit `da76f9a80cd08c152ab61455f78dc357837f90c9`, with archived output

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T19-14-06Z__q19-balanced-phase-band-check.out`

commit `fb9c7aabc30ff1ff92ec2e491719062a555392de`, ending

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit. The generic Laurent determinant identity used in Step 2 was also exact-symbolically checked in the preceding Q1.9 run; the proof is reproduced above so the present theorem does not rely on code as a substitute for mathematics.

## 8. What moved, what did not, and why this is source-relevant

The metric moves **`T_corr=1 -> 2`** because the uniform amplitude-band family (3.1) is a second explicit non-i.i.d., non-Hermitian C2 dependence family whose full asymptotic radial exponent is now determined. It is structurally different from the earlier fixed-amplitude two-point family: its angular spectral measure contains a continuum of balanced-phase orbits with nonconstant `|zw|`.

More strongly, the argument proves a class theorem for every symmetric amplitude law supported in `[delta,1-delta]` and every `0<alpha<2`. I count this as one new family for the frozen metric, not infinitely many units.

The source Question 1.9 is **not closed**. Arbitrary `theta_d` need not admit the balanced `S^1` action; it can approach or charge the coordinate axes, need not have an integrable logarithmic reciprocal-product invariant, and can have directional tail behavior not captured by this radial theorem. The source's i.i.d. axis case remains qualitatively lighter-tailed, while Hermitian laws retain the entry tail. A general classification still requires understanding which geometric properties of `theta_d` select these regimes.

## 9. Section-B accounting

- **B14 FIND THE GROUP ACTING — success.** The balanced `S^1` action isolates the invariant `zw` and makes phase-Mahler peeling exact after conditioning on amplitude.
- **B15 BREAK THE SYMMETRY ON PURPOSE — success.** Replacing a constant reciprocal product by a continuum random amplitude shows the prior exponent theorem is not an artefact of fixed `|W_1W_2|`.
- **B4 PROVE SOMETHING WEAKER, COMPLETELY — success.** Instead of arbitrary `theta_d`, the full balanced-phase amplitude-band class is proved, for all `0<alpha<2`, with a pointwise tail lower bound up to `log r` and exact exponent.

These are different from the immediately preceding B6/B11/B29 triple.

Suggested next triple, if Q1.9 remains the active claim: **B1/B20/B27**. Change category from angular measures to orbit quotients; identify exactly why the phase-peeling algorithm fails for a two-phase/non-Haar support; and test whether a stronger orbitwise condition can swap the quantifiers from “this balanced class” to “every `theta_d` with a positive reciprocal-product sector.”

## 10. Persistence and ledger delta

The mathematical idea was written before code in

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T19-14-06Z__idea-before-code-q19-balanced-phase-band.md`

at commit `6fe10e42f88295cf85e1f0c9c82aa019bef8226f`, and that commit was read back successfully.

Checker commit `da76f9a80cd08c152ab61455f78dc357837f90c9` and output commit `fb9c7aabc30ff1ff92ec2e491719062a555392de` were both read back successfully. No receipt-only commit was created.

Structured `ledger_delta` for the authorized shared-ledger maintainer:

- `track`: `HARD7-02`
- `source_target`: Campbell--O'Rourke (2022), Question 1.9
- `canonical_claim`: `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`
- `metric`: `T_corr`
- `before`: `1`
- `after`: `2`
- `status`: `PARTIAL`
- `movement`: `YES`
- `new_result`: exact radial exponent `alpha` for balanced-phase amplitude-band laws; explicit uniform-band family added to metric
- `source_status`: `OPEN` under bounded 2026-09-19 current-literature search
- `audits`: `0/2` for this theorem candidate
- `next_methods`: `B1/B20/B27`

The unchanged streak is reset to zero because the frozen quantity moved. Section I is not triggered this run.