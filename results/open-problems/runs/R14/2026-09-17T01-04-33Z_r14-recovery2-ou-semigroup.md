Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime and the exposed scheduler schema provide no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **NO METRIC MOVEMENT: `6.48139658710 -> 6.48139658710`; unchanged count `4 -> 5`; STUCK-RECOVERY-2. Section-B moves actually tried: #10 DERANDOMIZE, #14 FIND THE GROUP ACTING, #16 COMPUTE THE SMALL CASE / FINITE CORE.**

Problem/source: Elizabeth Gardner (1988), *The space of interactions in neural network models*, J. Phys. A 21, 257--270, DOI `10.1088/0305-4470/21/1/030`; modern source navigation through Stojnic arXiv:1306.3980, El Alaoui--Sellke arXiv:2010.15811, Montanari--Zhong--Zhou arXiv:2110.15824 / PTRF 188 (2024), and Stojnic arXiv:2312.16531. Frozen target: rigorous high-probability SAT/UNSAT threshold bracket at `kappa=-1` in the iid standard-Gaussian spherical model.

Status: **PARTIAL / source problem OPEN / SECOND AND FINAL STUCK RECOVERY USED.** The rigorous bracket remains

`alpha_L = 630297437506/10^11 = 6.30297437506`,

`alpha_U = 1278437096216/10^11 = 12.78437096216`,

with width

`64813965871/10^10 = 6.48139658710`.

This recovery does not manufacture a new endpoint. Its useful result is a new reduction of the complete `r=2` sfl stationary equations: the Gaussian derivative burden collapses from first/second derivatives with respect to all three parameters to **three scalar one-dimensional Gaussian expectations**. The exact tails of all three scalar expectations outside `|z|<=9` are now certified. The only remaining blocker for `alpha=12.5` is compact-interval validated quadrature / root certification.

## 1. Continuity, repository, ownership, and current source status

Before research I reread/rechecked current `master` rather than restarting:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own report `runs/R14/2026-09-16T23-52-29Z_r14-recovery1-preconditioned-2sfl.md`;
- newest neighboring reports `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md` and `runs/R07/20260917T0024Z_i0077_nonsyndetic_density_pulses_08.md`;
- targeted intake/repository searches for the negative spherical perceptron and R14 ownership.

The approximately-780-row intake family remains too large for a literal connector rendering without truncation. Whole-intake reread is therefore **ACCESS-LIMITED / TARGETED**, not falsely claimed complete. The exact R14 target, source family, prior R14 history, exclusions, and neighboring work were directly recovered. `POSTED.md` excludes the owner's Ising-perceptron manuscript; it does not exclude this spherical Gaussian source target.

Fresh bounded source/literature checks dated 2026-09-17 included:

- `arXiv:2312.16531` and its current HTML, especially Corollary 1 / equations (33)--(35) and Theorem 2: the complete sfl identity is evaluated at a solution of the stationarity system; its concrete capacity values are obtained by numerical evaluation;
- `arXiv:2608.29416` (Huang--Sellke--Sun, submitted 2026-08-29): exact thresholds for a dimension-free-Lipschitz **algorithmic** class in projection pursuit; its abstract explicitly says characterization of all non-algorithmic feasible projections remains a major outstanding challenge;
- bounded queries for later negative-spherical-perceptron capacity / full-RSB / rigorous satisfiability results and later author papers.

I found no later primary theorem in this bounded search that rigorously identifies the unrestricted full-radius negative-margin SAT threshold. This is dated bounded negative evidence, not a worldwide novelty certificate.

## 2. Exact blocker entering recovery 2

C188 uses

`q=p D^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

and reduces complete `r=2` stationarity to the three variables `(p,D,gamma)`.

At `kappa=-1`, write

`B=c/(4 gamma)`,

`h_B(x)=exp(-B (x-1)_+^2)`,

`f_{p,B}(z)=E_H h_B(sqrt(p) z+sqrt(1-p)H)`,

and

`I(p,B)=E_Z log f_{p,B}(Z)`.

The complete reduced objective has the form

`Ftilde_alpha(p,D,gamma) = T(p,D,gamma) - (alpha/c(p,D)) I(p,B)`,

where

`T=(1/2)(1-pq)c-gamma_p+(1/(2c))log(D/(2gamma_p))-q/(2D)+gamma`.

Recovery 1 planned to validate `grad Ftilde=0` by enclosing three first derivatives and nine second derivatives of the Gaussian integral. The new observation below makes that overkill.

## 3. Move #14 — FIND THE GROUP ACTING: the hidden Ornstein--Uhlenbeck semigroup

Set

`t=-(1/2)log p`, so `p=e^{-2t}`.

Then

`f_{p,B}(z) = P_t h_B(z)`

for the stationary Ornstein--Uhlenbeck semigroup

`P_t h(z)=E h(e^{-t}z+sqrt(1-e^{-2t})H)`

with generator

`L=d^2/dz^2-z d/dz`.

For `0<p<1`, Gaussian smoothing makes `f` smooth and positive. Put `u=log f`. Since `partial_t f=L f` and `dt/dp=-1/(2p)`, stationary Gaussian integration by parts gives

`partial_p I`
`= -(1/(2p)) E[(Lf)/f]`
`= -(1/(2p)) E[Lu+(u_z)^2]`
`= -(1/(2p)) E[(u_z)^2]`.

Thus, defining

`K(p,B)=E[(partial_z log f_{p,B}(Z))^2]`,

we have the exact identity

`boxed: I_p = -K/(2p)`.

This is the main conceptual reduction of the run. It is an entropy/Fisher-information identity for the OU semigroup, not a numerical approximation.

## 4. Move #10 — DERANDOMIZE: replace parameter-derivative quadrature by three scalar expectations

Let

`I_B = partial_B I = E[partial_B log f]`.

Because `B=c/(4gamma)`, direct chain rule gives

`B_p=B c_p/c`, `B_D=B c_D/c`, `B_gamma=-B/gamma`.

Using `I_p=-K/(2p)`, the three gradient equations are algebraically equivalent, on the inherited box where `c_D != 0`, to

`R_1 := I_B + 4 gamma^2/alpha = 0`,

`R_2 := I - B I_B + c^2 T_D/(alpha c_D) = 0`,

`R_3 := K/(2p) + (c/alpha)(T_p-(c_p/c_D)T_D) = 0`.

Proof: `F_gamma=0` first gives `I_B=-4gamma^2/alpha`. Next

`F_D=T_D+(alpha c_D/c^2)(I-BI_B)=0`,

which is `R_2=0`. Substituting that into

`F_p=T_p+(alpha c_p/c^2)(I-BI_B)-(alpha/c)I_p=0`

and using the OU identity yields `R_3=0`. Conversely these substitutions reconstruct all three gradient equations.

The exact symbolic checker also verifies `c_D<0` throughout the inherited C189 rational box. A coarse exact proof is enough: there `p<2/3`, `D^2<1/2`, and the numerator of

`c_D = [1+D^2(1-3p)+pD^4]/[D^2(p-1)(1-pD^2)^2]`

is `>1-D^2>1/2`, while the denominator is negative.

**Consequence for certification:** the Gaussian part of stationarity now requires only values of

`I`, `I_B`, and `K`,

not twelve separate parameter-derivative integrals. Deterministic rational/logarithmic terms remain explicit.

The exact checker output records `EXACT_OU_ALGEBRA_PASS`.

## 5. Move #16 — finite-core computation: all three scalar tails are now certified

Work on the same recovery-1 box

`p in [0.6562,0.6564]`,

`D in [0.6525,0.6528]`,

`gamma in [0.1587,0.1591]`.

Recovery 1 already proved the objective tail

`|E[log f(Z); |Z|>9]| < 5.26e-17`.

This run adds exact rational envelopes for the other two scalar quantities.

### Tail of `I_B`

Let `Y=sqrt(p)z+sqrt(1-p)H-1`, with conditional mean `mu=sqrt(p)z-1` and variance `sigma^2=1-p`.

For `z<=-9`, `f>=P(Y<=0)>1/2`, while

`Y_+^2 e^{-B Y_+^2} <= 1/B <1`,

so `|partial_B log f|<2`.

For `z>=9`, put

`G0=E exp(-B Y^2)`.

The positive-half contribution in `f` is at least `G0/2`, because the shifted Gaussian CDF is at least `1/2`. Also

`E[Y^2 e^{-B Y^2}]=G0(sigma^2/A+mu^2/A^2)`,

where `A=1+2B sigma^2`. Hence

`|partial_B log f| <= 2(1+z^2)`.

Using `Qbar(9)<phi(9)/9`, `int_9^infty z^2 phi(z)dz=9phi(9)+Qbar(9)`, and the exact rational majorant

`phi(9)<(10/27)^40`,

the checker certifies

`E[|partial_B log f(Z)|; |Z|>9] < 19(10/27)^40 < 1.1e-16 < 1e-15`.

### Tail of `K`

For `z<=-9`, `f>1/2`. Since

`|h_B'(x)|=2B r e^{-Br^2} <=2sqrt(B)<6`

on the box (`B<8`), we get `|u_z|<12`, hence `u_z^2<144`.

For `z>=9`, Cauchy--Schwarz applied to the full tilted Gaussian gives

`|u_z| <= 4 sqrt(p) B sqrt(sigma^2/A+mu^2/A^2)`

`<32(1+z)`.

Therefore

`K`'s integrand is `<2048(1+z^2)` on the right tail. The same Gaussian tail identities then give the exact rational certificate

`E[K-integrand; |Z|>9] < 19000(10/27)^40 < 1.1e-13 < 1e-12`.

The executed output records

- `EXACT_SCALAR_TAILS_PASS`,
- objective tail `<1e-16`,
- `I_B` tail `<1e-15`,
- `K` tail `<1e-12`,
- `ALL_EXACT_CHECKS_PASS`.

Artifact source: `artifacts/R14/2026-09-17T01-04-33Z_r14-recovery2-ou-semigroup.py`, creation commit `4b537ac7cdf8cd4a8c10b884e00c35c365b25583`.

Executed output: `artifacts/R14/2026-09-17T01-04-33Z_r14-recovery2-ou-semigroup.out`, creation commit `456bdaf6f69f05cff1d2887e5409682c3eb1dd22`, SHA-256 `8b3a7f187ed3c055477ecb04ab1c33613423c0b03ecfc9db90bd9658bfb6846b`.

## 6. Numerical-only consistency check

This does not enter the bracket.

At the inherited `alpha=12.5` scout point

`x0=(p,D,gamma)`
`=(0.656313184757223, 0.652653689820474, 0.158861855012242)`,

96-node Gauss--Hermite gives

`c=3.5522352299234883`,

`B=5.590132429288564`,

`I=-0.12551087529553803`,

`I_B=-0.008075868472937753`,

`K=0.18521718293697967`.

The three new scalar residuals are numerically

`(3.99e-17, 1.11e-16, -1.83e-15)`.

Thus the OU reduction reproduces the previously recovered full stationary point to numerical precision. This is a self-check only; it is explicitly labeled `NUMERICAL_ONLY` in the artifact.

## 7. Exact remaining blocker after recovery 2

The blocker is now substantially narrower than in recovery 1:

> Validate the three compact one-dimensional Gaussian integrals `I`, `I_B`, and `K` on `[-9,9]` over a small rational parameter box strongly enough to certify a zero of `(R_1,R_2,R_3)` near the alpha=12.5 scout, and then certify the complete comparison value positive at that root.

All three tails outside `[-9,9]` are already negligible by exact rational bounds. The remaining transcendental operations on the compact interval are only `sqrt`, `exp`, `Phi`, and `log`, plus rational operations. A viable next implementation is an interval Taylor / composite quadrature with outward rational enclosures, combined with Poincare--Miranda or interval Newton on the three reduced residuals.

What failed this recovery: I did **not** obtain the final validated compact-interval quadrature/root box. Therefore `alpha=12.5` remains numerical and is not promoted to `alpha_U`.

The nearest solved analogue remains C180--C184, where the partial lift collapses to one scalar concave maximizer. The complete `r=2` lift lacks that final one-dimensional parameter reduction; the new OU identity removes most derivative quadrature but not the remaining three-dimensional root existence.

## 8. Stuck-policy disposition

This is the **second recovery on the same hard target**, the maximum permitted by the owner policy. The recovery choice was again the allowed action **reduce the obstruction to a finite computation and run it**, but with a genuinely new route (OU semigroup/Fisher identity) rather than another derivative checker.

Because the fixed metric still did not move, the next R14 invocation may not produce a third recovery lemma on the same blocker. It must do one of two things:

1. if the compact validated quadrature/root certificate actually succeeds, record the resulting bracket movement; or
2. otherwise write the mandatory handoff and rotate to the next eligible HARD outside target after current source/status/ownership admission.

No silent reset of the stagnation count is permitted.

## 9. R15 audit duty

The newest R15 report is `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`. It explicitly retires I0076 from active hourly attack after six unchanged runs and leaves an OPEN/PARTIAL handoff; it is not a source-closure package. Therefore the R14 closure-audit trigger did not fire and I did not invent a new audit PASS.

## 10. Model / scheduler boundary

The repository policy and exposed tool schema remain unchanged: native task editing exposes prompt/title/schedule/enablement/timing controls but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run telemetry**. GPT-6 / maximum is therefore prompt text only in this runtime. A task returning `You cannot modify this task` must be handled from an authorized owning account/workspace context that has the relevant permission, or escalated to platform support; duplicate-task creation or permission bypass is not a legitimate workaround. I made no scheduler changes.

```yaml
ledger_delta:
  track: "R14 HARD OUTSIDE"
  source: "Gardner 1988 negative-margin spherical perceptron; arXiv:1306.3980, 2010.15811, 2312.16531"
  target: "rigorous SAT/UNSAT threshold bracket at kappa=-1"
  metric: "alpha_upper-alpha_lower"
  before: "6.48139658710"
  after: "6.48139658710"
  alpha_lower: "6.30297437506"
  alpha_upper: "12.78437096216"
  status: "PARTIAL / OPEN"
  unchanged_count_before: 4
  unchanged_count_after: 5
  stuck_recovery: "2 of 2 used"
  methods: [10, 14, 16]
  exact_evidence:
    - "OU chain-rule stationarity algebra: EXACT_OU_ALGEBRA_PASS"
    - "tails: |I|<1e-16, |I_B|<1e-15, K-tail<1e-12"
    - "artifacts/R14/2026-09-17T01-04-33Z_r14-recovery2-ou-semigroup.py"
    - "artifacts/R14/2026-09-17T01-04-33Z_r14-recovery2-ou-semigroup.out"
  numerical_only:
    - "alpha=12.5 reduced residual scout; not a bracket endpoint"
  audit_ids: []
  next_obligation: "validated compact [-9,9] quadrature/root certificate or mandatory handoff/rotation"
```
