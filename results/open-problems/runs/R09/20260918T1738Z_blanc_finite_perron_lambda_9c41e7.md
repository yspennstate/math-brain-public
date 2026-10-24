Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO MOVEMENT on `BLANC-RENAUDIE-2026-MEANFIELD-7-10`: `M_A=0 -> 0`; stagnation count remains UNKNOWN because no supported count was frozen at admission. Methods used: #8, #16, #20.**

# R09 — Blanc-Renaudie mean-field `d=7,8,9,10`: finite Perron certificate for the killed-cluster eigenvalue

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Lane: **CLOSABLE OUTSIDE**

## 1. Runtime/control truth

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The runtime exposes no authenticated reasoning-effort receipt, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, maximum reasoning, or an hour-long execution guarantee.

The exposed task-management surface still has no bindable model-family or reasoning-effort field and no authenticated completed-run model telemetry. The repository policy still records the lawful remedies for a task-level authorization denial such as the historical `You cannot modify this task`: operate from the owning/otherwise-authorized context, obtain an authorized ownership/admin transfer, or use platform support. I made no scheduler or permission change.

## 2. Continuity, source status, and ownership

I recovered before research: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the exclusive claim `operations/claims/BLANC-RENAUDIE-2026-MEANFIELD-7-10.md`, the newest complete R09 report `runs/R09/20260918T1633Z_blanc_renaudie_admission_finite_certificate_b4a7c2.md`, current claim-namespace delta screens, and the neighboring older C0064 infrared-bound intake evidence. The exact Blanc-Renaudie claim remains exclusively R09-owned and `CLAIMED / READY / CLOSABLE OUTSIDE / OPEN`; coordinator screens after admission also recognize that ownership. I did not reopen Tang, G0013, the retired Chen-Wang successor, or C0064.

Fresh dated source/status search on 2026-09-18 recovered Arthur Blanc-Renaudie's arXiv:2609.20764, submitted 2026-09-17 and updated 2026-09-18, and did not recover a later source-matching proof of the nearest-neighbor cases `d=7,8,9,10`. This remains bounded negative evidence, not a worldwide novelty certificate. The source itself states that nearest-neighbor `d>=11` is known and identifies `7<=d<=10` as the remaining numerical-proof regime.

The frozen metric stays

\[
M_A:=\#\{d\in\{7,8,9,10\}:\text{a complete rigorous Theorem 1.1(a) certificate has been obtained}\}.
\]

No dimension is certified this run:

\[
\boxed{M_A:0\longrightarrow0.}
\]

The result below is a new certifier for a difficult constant inside the source proof, not a certificate of Theorem 1.1(a) in any dimension.

## 3. Method #8 — discretize: a completely finite Perron certificate for `lambda_p`

### 3.1 The two finite inputs

Fix nearest-neighbor bond percolation on `Z^d`, so the degree is

\[
\Omega=2d.
\]

For a finite set `S` containing the origin write

\[
\tau_{S,p}(0,x)=\mathbb P_p(0\leftrightarrow x\text{ by an open path contained in }S),
\qquad
\chi_S(p)=\sum_{x\in S}\tau_{S,p}(0,x),
\]

and

\[
\varphi_p(S)
:=p\sum_{\substack{u\in S,\ v\notin S\\u\sim v}}
\tau_{S,p}(0,u).
\]

The previous R09 report used `a=varphi_p(Lambda_m)<1` only to obtain a pointwise exponential tail. Summing the same Simon--Lieb first-exit inequality gives a much sharper finite susceptibility upper bound.

### Lemma 3.1 — finite susceptibility upper completion

If

\[
a:=\varphi_p(S)<1,
\]

then

\[
\boxed{\chi(p)\le \frac{\chi_S(p)}{1-a}.}
\tag{3.1}
\]

#### Proof

For every `x in Z^d`, Simon--Lieb gives

\[
\tau_p(0,x)
\le
\tau_{S,p}(0,x)
+p\sum_{\substack{u\in S,\ v\notin S\\u\sim v}}
\tau_{S,p}(0,u)\tau_p(v,x),
\]

where the restricted term is interpreted as zero when `x notin S`. Summing over `x` and using translation invariance,

\[
\chi(p)
\le
\chi_S(p)
+p\sum_{u,v}\tau_{S,p}(0,u)\chi(p)
=
\chi_S(p)+a\chi(p).
\]

Rearranging proves (3.1). In particular `a<1` again certifies `p<p_c`. `□`

This is elementary classical finite-size machinery; I do **not** claim novelty for (3.1).

Now use Blanc-Renaudie's pointed-cluster notation. For a live pointed cluster `A_vec=(A,a_vec)` let

\[
\mu_p(A_{\rm vec})=\mathbb P_p(C(0)=A),
\]

and recall that the killed operator is

\[
T_pg(A_{\rm vec})
=
\sum_{B_{\rm vec}}
\frac{\mu_p(B_{\rm vec})}{\Omega\chi(p)}
\mathbf 1\{(A_{\rm vec},B_{\rm vec})\notin\mathcal C_{\rm cut}\}
\,g(B_{\rm vec}).
\tag{3.2}
\]

Its maximal eigenvalue is the source quantity `lambda_p`.

Choose **any finite set `F` of live pointed finite clusters**, and any vector `z=(z_A)_{A in F}` with every `z_A>0`. Define the finite raw matrix

\[
K_F(A,B)
:=
\mathbf 1\{(A,B)\notin\mathcal C_{\rm cut}\}\mu_p(B)
\tag{3.3}
\]

and the rational Collatz lower quotient

\[
L_F(z)
:=
\min_{A\in F}
\frac{\sum_{B\in F}K_F(A,B)z_B}{z_A}.
\tag{3.4}
\]

### Proposition 3.2 — finite Perron/Susceptibility certificate

If `a=varphi_p(S)<1`, then

\[
\boxed{
\lambda_p
\ge
\frac{(1-a)L_F(z)}{\Omega\chi_S(p)}.
}
\tag{3.5}
\]

For rational `p`, finite `S`, finite pointed-cluster set `F`, and rational positive `z`, every quantity on the right can be certified by finite exact arithmetic.

#### Proof

The restriction of the raw killed matrix to `F` is `K_F`. By Collatz--Wielandt,

\[
\rho(K_F)\ge L_F(z).
\]

The normalized restriction of (3.2) is `K_F/(Omega chi(p))`. The same finite-submatrix Perron comparison used in the proof of Blanc-Renaudrie Lemma 3.13 / Theorem 3.5 gives

\[
\lambda_p\ge \frac{\rho(K_F)}{\Omega\chi(p)}
\ge \frac{L_F(z)}{\Omega\chi(p)}.
\]

Applying (3.1) yields (3.5). `□`

### Why this changes the numerical strategy

Section 1.3 of the source says the constants in Theorem 1.1 are computable but not written explicitly because the local modifications in Section 3 are extremely costly; Remark 3.6 says sufficiently good numerical control can bypass those modifications. Proposition 3.2 turns at least the **Theorem 3.5 eigenvalue lower-bound subproblem** into a direct finite exact calculation: no local modification radius `r`, finite-energy comparison factor, or infinite cluster-state normalization is needed once `a<1` is certified.

This does **not** by itself replace the later mixing and Fourier arguments; Section 6 below records that remaining obstruction precisely.

## 4. Method #16 — compute the smallest cases: the complete cluster-size <=2 matrix collapses exactly

I next computed every live pointed cluster whose underlying vertex cluster has size one or two. The exact checker is

`artifacts/R09/20260918T1738Z_blanc_finite_spectral_cert_9c41e7.py`

with executed output

`artifacts/R09/20260918T1738Z_blanc_finite_spectral_cert_9c41e7.out`.

The archived run ends `ALL_EXACT_CHECKS_PASS`. This is a **self-check**, not an independent audit.

Let `Omega=2d`. There are two cluster probabilities:

\[
\mu_1=(1-p)^\Omega
\tag{4.1}
\]

for the singleton cluster `{0}`, and

\[
\mu_2=p(1-p)^{2\Omega-2}
\tag{4.2}
\]

for any fixed two-vertex cluster `{0,e}` with `e~0`.

Let `F_2` consist of all **live** pointed states based on these clusters. Then

- there are `Omega` singleton pointed states;
- there are `2 Omega (Omega-1)` live pointed states based on two-vertex clusters.

The exhaustive exact enumeration exposed a stronger pattern: **every row of `K_{F_2}` has the same row sum**. More precisely, from every live source state in `F_2`,

\[
N_1=\Omega
\]

singleton target states are non-cut, and

\[
N_2=(\Omega-1)(2\Omega-1)
\]

two-vertex target states are non-cut. Hence the all-ones vector is an exact Perron eigenvector and

\[
\boxed{
\rho(K_{F_2})
=
\Omega(1-p)^\Omega
+(\Omega-1)(2\Omega-1)p(1-p)^{2\Omega-2}.
}
\tag{4.3}
\]

### Direct proof of the row count

For a live source state `(A,a_vec)`, `a^+ notin A`, so `0 notin A-a^+`. Therefore a singleton target `{0}` is never cut, giving all `Omega` singleton targets.

For every live source with `|A|<=2`, the translated deletion set

\[
A-a^+
\]

contains **exactly one nearest neighbor** `e_*` of the origin. This is immediate for `A={0}`. For `A={0,f}`, either the pointed edge leaves from `0`, in which case `-a^+` is the unique unit vector in the two-point deletion set, or it leaves from `f`, in which case `f-a^+` is the unique unit vector. The other translated vertex has `l1` distance two.

A two-vertex target `B={0,e}` is cut only when `e=e_*`, the target tail is `b^-=e_*`, and removing `e_*` disconnects that tail from `0`. For that unique target cluster there are exactly `Omega-1` live choices of `b^+` (all neighbors of `e_*` except `0`). Thus exactly `Omega-1` of the `2Omega(Omega-1)` two-vertex pointed targets are cut, leaving

\[
2\Omega(\Omega-1)-(\Omega-1)
=(\Omega-1)(2\Omega-1)
\]

non-cut targets. This proves (4.3) without relying on the checker.

Combining (3.5) and (4.3) gives the explicit finite lower bound

\[
\boxed{
\lambda_p\ge
\frac{1-a}{\Omega\chi_S(p)}
\left[
\Omega(1-p)^\Omega
+(\Omega-1)(2\Omega-1)p(1-p)^{2\Omega-2}
\right].
}
\tag{4.4}
\]

This formula is valid for any finite Simon--Lieb block `S` with `a=varphi_p(S)<1`.

### Exact calibration in dimensions 7--10

For the smallest possible block `S=Lambda_0={0}`, one has

\[
\chi_S=1,
\qquad
 a=\Omega p.
\]

At the exact rational calibration point

\[
p=\frac1{2\Omega}=\frac1{4d},
\]

so `a=1/2`, the exact checker yields

\[
\begin{array}{c|c|c}
d & \text{certified lower bound from (4.4)} & \text{gain over singleton-only }F\\
\hline
7 & 0.47442023227126007\ldots & 1.57874845\ldots\\
8 & 0.47604319490457640\ldots & 1.58230029\ldots\\
9 & 0.47730050799365986\ldots & 1.58504686\ldots\\
10& 0.47830323390108180\ldots & 1.58723415\ldots
\end{array}
\]

The output archives the exact rational values, not just decimals.

This calibration is **not** close enough to criticality to advance `M_A`: (3.1) gives `chi(p)<=2` at these `m=0` points, whereas the source explicitly warns that the useful numerical regime may require susceptibility on the order of `10^2`--`10^3`. The point of the calculation is different: the finite Perron certificate itself is numerically non-degenerate, and adding only the complete size-two cluster layer already improves the most primitive spectral certificate by about 58%.

## 5. Method #20 — find why the algorithm still fails: `lambda_p` is no longer the main constant bottleneck

The preceding result materially sharpens the dependency audit.

The source's Section 3 has at least three quantitatively distinct obligations:

1. **Theorem 3.5:** lower-bound the killed-cluster Perron eigenvalue `lambda_p` under condition `(C)` and large susceptibility.
2. **Theorem 3.14:** obtain exponential total-variation mixing for the Doob `h`-transformed pointed-cluster chain.
3. **Theorem 3.24 / Proposition 3.25:** obtain the high-frequency Fourier contraction used later in Section 6.

Proposition 3.2 gives a direct finite route to item 1 at a proposed numerical initialization point. But items 2 and 3 still contain the expensive local-modification mechanism. The source's proof of Theorem 3.14 passes through the good-state/minorization construction and Proposition 3.21; its final contraction exponent depends on a finite `N` assembled from those constants. The proof of Proposition 3.25 explicitly reuses the local modifications to force a displacement change and hence Fourier contraction. Theorem 3.24 then chooses small parameters as powers of the lower bound on `lambda_p`.

Therefore the current obstacle is **not merely “extract `f_d(C)`” and not merely “lower-bound `lambda_p`.”** A practical certificate for `d=7,...,10` needs one of the following genuinely new ingredients:

- a finite-state/tail certificate for **mixing and three-step Fourier contraction**, analogous to Proposition 3.2 for the Perron eigenvalue; or
- an explicit numerical triangle/cut estimate strong enough to make the source's “skip local modifications” remark quantitative simultaneously for the mixing and high-frequency steps; or
- a different renormalization/local-CLT implementation, as the source itself suggests in Section 1.3.

This is a useful negative result for the algorithm design: spending the next run extracting the enormous original local-modification constants in Theorem 3.5 would be the wrong bottleneck. The spectral subproblem now has a finite exact substitute.

## 6. What moved mathematically, and what did not

The source-level metric did not move:

\[
\boxed{M_A=0.}
\]

No dimension is claimed proved, and there is no source closure.

What did improve is the route:

- the same Simon--Lieb block used for the previous global-tail certificate also gives the much sharper exact susceptibility upper bound `chi<=chi_S/(1-a)`;
- together with any finite pointed-cluster matrix it gives a finite exact lower certificate for Blanc-Renaudrie's `lambda_p`;
- the entire underlying-cluster-size `<=2` matrix is solved in closed form, checked exactly in `d=7,8,9,10`, and already gives a nontrivial spectral bound;
- the constant-DAG audit now isolates mixing/Fourier contraction, rather than the Perron eigenvalue, as the next Section-3 numerical bottleneck.

Novelty of the finite Perron packaging is **unverified**. Collatz--Wielandt, Simon--Lieb, and the source's finite-submatrix Perron comparison are standard ingredients; the value here is the source-specific exact combination and the closed size-two row count. Do not present it externally as new without a dedicated prior-art audit.

## 7. Next fresh methods

Do not repeat `#8/#16/#20`. The next proposed triple on this problem is:

- **#11 DUALIZE:** derive a finite minorization / Dobrushin certificate for the `h`-transformed kernel using computable left/right Perron vectors plus a rigorous tail remainder, targeting Theorem 3.14 directly;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** search the rigorous lace/NoBLE and numerical high-dimensional percolation literature for explicit triangle/cut constants in `d=7,8,9,10`, with special attention to whether the source's Remark 3.6 can be made numerical without reconstructing the costly local modifications;
- **#19 MAKE IT AN ALGORITHM:** turn the three-step Fourier contraction in Proposition 3.25 into a finite state-space optimization with certified tail error, so the local-CLT/high-frequency step can be checked by a machine once finite cluster data are supplied.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  track: R09
  source: BLANC-RENAUDIE-2026-MEANFIELD-7-10
  status_before: OPEN
  status_after: OPEN
  metric: M_A
  value_before: 0
  value_after: 0
  movement: false
  stagnation_count: UNKNOWN
  methods: [8, 16, 20]
  new_rigorous_results:
    - "Finite susceptibility upper completion: chi(p) <= chi_S(p)/(1-varphi_p(S))."
    - "Finite Perron certificate: lambda_p >= (1-a)L_F(z)/(Omega chi_S(p))."
    - "Closed-form size<=2 pointed-cluster Perron row mass, with exact d=7..10 self-check."
  source_scope_closed: false
  finite_artifacts:
    - artifacts/R09/20260918T1738Z_blanc_finite_spectral_cert_9c41e7.py
    - artifacts/R09/20260918T1738Z_blanc_finite_spectral_cert_9c41e7.out
  prior_art_status: "Fresh 2026-09-18 bounded source/current-status search found no later source-matching resolution; novelty of the source-specific finite Perron packaging remains unverified."
  next_methods: [11, 17, 19]
  remaining_obligation: "Certify a full Theorem 1.1(a) initialization in at least one of d=7,8,9,10; immediate route bottleneck is a practical finite certificate for mixing and high-frequency Fourier contraction, plus near-critical finite-volume data."
```
