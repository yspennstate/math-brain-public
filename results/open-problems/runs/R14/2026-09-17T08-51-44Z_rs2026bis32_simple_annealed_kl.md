Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `D_bis: 2 -> 2`; unchanged count `0 -> 1`. Methods actually tried: #6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE, #25 COUNT THE SAME THING TWICE.**

# R14 — RS-2026-BIS32: simple-model annealed symmetry and a reverse-KL dual

Status: **OPEN / PARTIAL**. Current owned target: `RS-2026-BIS32`, Randomstrasse 101 / Afonso S. Bandeira, Conjecture 32 (Min and Max Bisections), tracing to Zdeborova--Boettcher. The original negative-margin spherical-perceptron target remains handed off and is not reopened; its last supported rigorous bracket remains

\[
6.30297437506\le \alpha_c(-1)\le12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

The intervening I0089 Riesz target also remains handed off after its permitted HARD recoveries. This report continues from `runs/R14/2026-09-17T08-00-47Z_i0089-handoff_rs2026bis32-first.md`, not from either retired predecessor.

## 1. Required recovery, source status, and prior attempt

I reread the current campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical claim `operations/claims/RS-2026-BIS32.md`, the newest R14 report, the newest visible neighboring R15 state, and repository/intake hits for the bisection problem. The historical intake alias is `E0053`, “Sum of maximum and minimum bisection of a random regular graph”; its recorded substantive attempt was unresolved and already identified the fixed-`d` asymmetry as the missing issue. I therefore do not restart from the large-`d` physics heuristic.

Fresh primary-source checks on 2026-09-17 again found the live Randomstrasse page stating

\[
\frac{\mathbf E\,\mathrm{MinBis}(G_d)+\mathbf E\,\mathrm{MaxBis}(G_d)}{n}
=\frac d2+o(1),\qquad n\to\infty,
\tag{BIS32}
\]

for every fixed integer `d>=3`, where `G_d` is uniform among simple `d`-regular graphs on even `n`. Zdeborova--Boettcher's original paper states the physics conjecture; the later rigorous results recovered in the bounded search remain either large-degree results or positive-temperature results. In particular:

- Dembo--Montanari--Sen and El Alaoui--Montanari--Sellke concern the large-degree regime;
- Gheissari--Perkins--Yap (arXiv:2511.16620) prove fixed-magnetization ferromagnetic annealed/quenched agreement only below reconstruction and obtain a positive-temperature ZB relation, not this zero-temperature balanced MinBis/MaxBis identity;
- Lichev--Mitsche give bounds for the cubic minimum bisection, not the exact source limit.

No fixed-`d` source-matching closure was found in the bounded fresh search. This is negative search evidence, not a novelty certificate.

The fixed metric remains

\[
D_{\rm bis}:=\sup\{D\ge2:\text{(BIS32) is rigorously proved for every }3\le d\le D\}.
\]

Before this run `D_bis=2`; after this run it is still `2`.

## 2. Preserved exact reductions from the preceding run

For balanced spins

\[
\Omega_n=\{\sigma\in\{-1,+1\}^n:\sum_i\sigma_i=0\},
\qquad
H_G(\sigma)=\sum_{\{i,j\}\in E(G)}\sigma_i\sigma_j,
\]

put

\[
M_+(G)=\max_{\Omega_n}H_G,\qquad M_-(G)=\min_{\Omega_n}H_G.
\]

Since `|E|=dn/2`,

\[
\mathrm{MinBis}(G)=\frac{dn/2-M_+(G)}2,
\qquad
\mathrm{MaxBis}(G)=\frac{dn/2-M_-(G)}2.
\]

Thus (BIS32) is equivalent to

\[
\frac1n\mathbf E[M_+(G_d)+M_-(G_d)]\to0.
\tag{2.1}
\]

For

\[
P_{n,d}(\beta)=\frac1n\mathbf E\log Z_G^0(\beta),
\qquad
Z_G^0(\beta)=\sum_{\sigma\in\Omega_n}e^{\beta H_G(\sigma)},
\]

the preceding run proved the exact soft-max bound

\[
\left|
\frac{P_{n,d}(\beta)-P_{n,d}(-\beta)}\beta
-\frac1n\mathbf E[M_++M_-]
\right|\le\frac{\log2}{\beta}.
\tag{2.2}
\]

Therefore the source conjecture at fixed `d` is equivalent to vanishing zero-temperature odd balanced pressure.

The preceding run also obtained the exact configuration-model pairing count for one fixed balanced spin. Let

\[
m=n/2,\qquad M=dm=dn/2,
\]

so each spin class owns `M` half-edges. If `K` cross-edges occur, then, for admissible parity,

\[
N_M(k)=\binom Mk^2 k!\,((M-k)-1)!!^2.
\tag{2.3}
\]

That finite identity was already exact-checked and archived; I did not create a redundant checker this run.

## 3. Method #6 — deform configuration model to the uniform simple model

The previous report's main caveat was that (2.3) lived in the configuration model. The first new result removes that caveat at the exponential scale needed for annealed pressure.

### C196 — uniform interior simplicity transfer

**Claim.** Fix `d>=3` and `epsilon in (0,1/2)`. For a fixed balanced partition and every admissible `k` satisfying

\[
\varepsilon M\le k\le(1-\varepsilon)M,
\]

there exists `c=c(d,epsilon)>0` such that, for all sufficiently large admissible `n`,

\[
c\le \mathbf P_{\rm CM}(\mathrm{Simple}\mid K=k)\le1.
\tag{3.1}
\]

Since the unconditional fixed-`d` configuration model has simplicity probability bounded away from zero, this implies

\[
\mathbf P_{\rm simple}(K=k)
=\Theta_{d,\varepsilon}(\mathbf P_{\rm CM}(K=k))
\tag{3.2}
\]

uniformly over the interior range.

**Proof.** Condition on the exact cross-stub subsets. For each vertex in the two spin classes let `a_i,b_j in {0,...,d}` be its selected cross-stub degree. The cross pairing is a bipartite configuration model with degree sequences `(a_i)` and `(b_j)`, total degree `k`. The remaining stubs form two independent ordinary configuration models with degrees `(d-a_i)` and `(d-b_j)`, each of total degree `M-k`.

On the stated interior range, all three total degrees are `Theta(n)`, while every individual degree is bounded by the fixed constant `d`. Hence for every one of the three degree sequences

\[
\sum_v r_v^2\le d\sum_v r_v=O\!\left(\sum_v r_v\right).
\]

Janson's simplicity theorem gives a probability bounded away from zero for each ordinary bounded-degree configuration model, and the bipartite counterpart in Janson's sequel gives the same for the cross component. The bound is uniform over the present family: otherwise one could choose a sequence of bounded-degree degree sequences, with linear total degree, whose simplicity probability tends to zero, contradicting those theorems. Conditional on the cross-stub subsets, the three pairings are independent. Because the three components occupy disjoint edge types (`S-S`, `T-T`, `S-T`), the full graph is simple iff all three components are simple. Their product gives (3.1). Averaging over the selected cross-stub subsets preserves the lower bound.

Finally, the configuration model conditioned on simplicity is uniform over labeled simple `d`-regular graphs, and the unconditional simplicity probability stays bounded away from zero for fixed `d`. Bayes' identity yields (3.2). QED.

This is exactly the configuration-model-to-simple deformation that was missing from the preceding run. It is **not** a quenched theorem and does not move `D_bis`.

## 4. Method #25 — count graph/bisection pairs twice: the exact simple-model annealed rate

Apply Stirling's formula to (2.3), divide by the total number `(2M-1)!!` of configuration-model pairings, and write `q=k/M`. Uniformly for `q` in compact subsets of `(0,1)`,

\[
\frac1n\log\mathbf P_{\rm CM}(K=k)
=
\frac d2\big(H(q)-\log2\big)+o(1),
\tag{4.1}
\]

where

\[
H(q)=-q\log q-(1-q)\log(1-q).
\]

C196 transfers the same exponential rate to the uniform simple model. Multiplying by the number

\[
|\Omega_n|=\binom n{n/2}=\exp(n\log2+o(n))
\]

of balanced spins gives the annealed complexity exponent

\[
\boxed{
\Psi_d(q)=\log2+\frac d2\big(H(q)-\log2\big).
}
\tag{C197.1}
\]

It is exactly reflection-symmetric:

\[
\Psi_d(q)=\Psi_d(1-q).
\tag{4.2}
\]

So a pure first-moment argument based only on the number of balanced cuts is intrinsically unable to distinguish the lower and upper extremal deviations from `dn/4`.

For orientation only, not as a rigorous source endpoint, the cubic annealed zero solves

\[
H(q)=\frac13\log2,
\]

numerically at

\[
q\approx0.0614904700787242,
\]

corresponding to lower/upper cut densities `k/n` approximately `0.0922357051` and `1.4077642949`. Lichev--Mitsche's rigorous cubic lower bound `0.103295 n` is already stronger than this raw first-moment barrier; that is concrete evidence that the missing fixed-`d` information is structural/quenched rather than elementary counting.

### C197 — closed form of the balanced annealed pressure on uniform simple regular graphs

Define

\[
A_{n,d}(\beta)
:=\frac1n\log\mathbf E_{G_d}Z_G^0(\beta).
\]

For every fixed real `beta`,

\[
\boxed{
\lim_{n\to\infty}A_{n,d}(\beta)
=
\log2+\frac d2\log\cosh\beta.
}
\tag{C197.2}
\]

In particular the limiting annealed pressure is even in `beta`.

**Proof.** For one fixed balanced spin, `H_G(\sigma)=M-2K=M(1-2q)`. By permutation symmetry,

\[
\mathbf E Z_G^0(\beta)
=|\Omega_n|\,\mathbf E e^{\beta(M-2K)}.
\]

The global upper bound `P_simple(K=k)<=C_d P_CM(K=k)` follows from Bayes and the fixed-`d` lower bound on unconditional simplicity. For the lower bound at the Laplace maximizer, C196 applies because for every fixed finite `beta` the maximizer stays a fixed positive distance from `0` and `1`. Hence the Laplace principle with (4.1) gives

\[
\lim A_{n,d}(\beta)
=\sup_{0\le q\le1}
\left\{
\Psi_d(q)+\frac d2\beta(1-2q)
\right\}.
\]

The maximizer is

\[
q_\beta=\frac1{1+e^{2\beta}},
\]

and the elementary entropy duality

\[
\sup_q\{H(q)+\beta(1-2q)\}=\log(2\cosh\beta)
\]

gives (C197.2). The parity restriction on admissible `k` changes the grid spacing by `O(1/M)` and does not affect the limit. QED.

This strictly strengthens the preceding configuration-model annealed observation: the desired `+beta/-beta` symmetry holds at leading order in the **actual uniform simple graph ensemble** for every fixed finite temperature.

But it still does not prove the source conjecture. As `beta->infinity`, (C197.2) behaves as

\[
\frac d2|\beta|+\left(1-\frac d2\right)\log2+o(1),
\]

and is dominated by exponentially rare graphs/spins near the extreme cut boundary. The annealed-to-quenched gap is therefore allowed to be linear in `|beta|n`.

## 5. Method #11 — dualize the annealing gap to a reverse relative entropy

The annealing gap has an exact information-theoretic representation that isolates the source obstruction more cleanly than pressure language alone.

Let `P=P_{n,d}` denote the uniform law on simple labeled `d`-regular graphs, and define the tilted graph law

\[
Q_{n,d,\beta}(G)
:=
P(G)\frac{Z_G^0(\beta)}{\mathbf E_P Z_G^0(\beta)}.
\tag{5.1}
\]

Then, exactly,

\[
\begin{aligned}
D(P\|Q_{n,d,\beta})
&=\mathbf E_P\log\frac{P(G)}{Q_{n,d,\beta}(G)}\\
&=\log\mathbf E_PZ_G^0(\beta)-\mathbf E_P\log Z_G^0(\beta)\\
&=n\big(A_{n,d}(\beta)-P_{n,d}(\beta)\big).
\end{aligned}
\tag{C198.1}
\]

Thus the quenched correction is exactly a **reverse KL divergence per vertex** from the null random-regular graph law to its balanced Ising planted mixture.

The joint version of (5.1), proportional to

\[
P(G)\,\mathbf 1_{\{\sigma\in\Omega_n\}}e^{\beta H_G(\sigma)},
\]

is a balanced planted regular block model: `beta>0` favors assortative/monochromatic edges and `beta<0` favors disassortative/bichromatic edges. This recasts the source conjecture as a comparison of the zero-temperature information costs of the assortative and disassortative planted models.

Since C197 gives

\[
A_{n,d}(\beta)-A_{n,d}(-\beta)\to0
\quad\text{for every fixed }\beta,
\]

combining C198.1 with the preserved soft-max equivalence (2.2) yields the exact fixed-`d` equivalence

\[
\boxed{
\text{(BIS32)}
\iff
\lim_{\beta\to\infty}\limsup_{n\to\infty}
\frac{
|D(P_{n,d}\|Q_{n,d,\beta})-D(P_{n,d}\|Q_{n,d,-\beta})|
}{\beta n}
=0.
}
\tag{C198.2}
\]

No existence of a finite-`beta` quenched pressure limit is needed for this formulation; the vanishing annealed odd term is already enough to pass to the displayed `limsup` equivalence.

This is the strongest route found this run. The elementary counting side is now completely symmetric even in the actual simple ensemble. What remains is a genuinely quenched statement: the two **reverse-KL slopes** must agree at zero temperature.

## 6. Why the three attacks do not yet move `D_bis`

### #6 outcome

**Succeeded at its intended intermediate task.** The configuration-model/simple-model gap is removed for all interior cut fractions at exponential scale. It does not control `E log Z`.

### #25 outcome

**Succeeded and produced C197.** The simple-model annealed complexity and pressure are explicitly reflection/even symmetric. This also certifies an obstruction: no proof using only first moments of balanced cut counts can distinguish the two zero-temperature quenched extrema.

### #11 outcome

**Succeeded as a reduction, not a closure.** C198 converts the entire fixed-`d` conjecture into equality of two reverse-KL slopes. Existing high-temperature theorems do not run to `beta=infinity`. Gheissari--Perkins--Yap show annealed/quenched agreement for the zero-magnetization ferromagnet below reconstruction, which makes the `+beta` KL cost sublinear there; that finite-temperature fact stops precisely before the regime needed for the zero-temperature source statement. The disassortative side is likewise not identified all the way to zero temperature by a source-matching theorem.

The exact remaining source-valid obligation for the first metric movement is therefore already sharp at `d=3`:

\[
\boxed{
\lim_{\beta\to\infty}\limsup_{n\to\infty}
\frac{
|D(P_{n,3}\|Q_{n,3,\beta})-D(P_{n,3}\|Q_{n,3,-\beta})|
}{\beta n}
=0.
}
\tag{BLOCK-3}
\]

Proving `(BLOCK-3)` moves `D_bis:2->3`. A numerical pressure estimate, a large-`d` theorem, or a restricted replica/overlap ansatz does not.

## 7. Literature comparison and what is now genuinely different

The bounded search recovered the following relevant primary results:

1. **Zdeborova--Boettcher**, arXiv:0912.4861: the original physics conjecture and numerical evidence.
2. **Janson**, arXiv:math/0609802 and arXiv:1307.6344: ordinary and bipartite configuration-model simplicity criteria used in C196.
3. **Gheissari--Perkins--Yap**, arXiv:2511.16620: fixed-magnetization ferromagnetic annealed/quenched equality below reconstruction and a positive-temperature ZB relation.
4. **Lichev--Mitsche**, EJC 2023: rigorous cubic minimum-bisection bounds `0.103295 n` and `0.139822 n`, showing that first-moment counting alone is quantitatively nonsharp even at `d=3`.

I did not locate a source giving C198.2 in the reverse-KL planted-mixture form, but this is only bounded negative evidence; no novelty claim is made.

## 8. Next new-method triple

This is only the first unchanged continuation on RS-2026-BIS32, so the Section-I stuck protocol is not triggered. The next run should not repeat either `#2,#18,#5` or `#6,#11,#25`. The next planned triple is:

- **#12 FIND WHAT IS CONSERVED:** identify a quantity shared by the `+beta` and `-beta` planted regular models after conditioning on the balanced labels, with the aim of comparing their reverse information costs rather than each pressure separately;
- **#20 FIND WHY THE ALGORITHM FAILS:** analyze the exact point at which second-moment/contiguity proofs break at reconstruction and ask whether the *difference* of the two KL costs can remain controlled after each individual annealing gap becomes extensive;
- **#30 ONE SCALE AT A TIME:** prove slope symmetry first on a finite `beta` interval beyond the current reconstruction threshold, then localize the first possible symmetry-breaking beta rather than attacking `beta=infinity` in one jump.

## 9. Honest status and closure gates

- Source target: **OPEN**.
- R14 result: **PARTIAL**.
- Metric: `D_bis: 2 -> 2`.
- Unchanged count: `0 -> 1`.
- New on-page claims: C196, C197, C198.
- Finite numerical values in this report: explanatory only; no rigorous endpoint movement.
- Exact finite checker: none newly needed; previous exact pairing/small-`n` checker remains archived and PASS.
- Independent OTHER-track audits of C196--C198: `0/2`.
- No source theorem is called closed.

## 10. Model/scheduler control limitation

The task interface available to this runtime still exposes prompt/title/schedule/enablement/timing controls but no authenticated model-family selector, no reasoning-effort selector, and no completed-run model telemetry. Therefore GPT-6/maximum remains a prompt request only in this environment. The previously observed `You cannot modify this task` error is an authorization/context restriction; the valid remedy is the authorized owning workspace/account surface or platform support, not duplication or permission bypass. No scheduler changes were attempted in this run.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R14
  target: RS-2026-BIS32
  source_status: OPEN
  worker_status: PARTIAL
  metric:
    name: D_bis
    before: 2
    after: 2
    moved: false
  unchanged_count:
    before: 0
    after: 1
  methods_tried: [6, 11, 25]
  claims_added:
    - C196: uniform interior configuration-model-to-simple simplicity transfer
    - C197: simple-model annealed balanced-cut rate and even pressure limit
    - C198: reverse-KL planted-mixture equivalence
  exact_remaining_obligation: BLOCK-3
  audit_count_new_claims: "0/2"
  next_methods: [12, 20, 30]
  predecessor_perceptron_reopened: false
  shared_roots_modified: false
```
