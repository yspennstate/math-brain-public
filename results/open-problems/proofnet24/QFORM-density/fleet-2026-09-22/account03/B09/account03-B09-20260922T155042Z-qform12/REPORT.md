# QFORM-PIVOT-RIDGE-BILINEAR-v1

Run: `account03-B09-20260922T155042Z-qform12`  
Worker: `account03/B09` — Bilinear block mechanism  
Programme: `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
Status: **proved supporting theorem; full conjecture remains OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and scope

The fleet target is: for independent real coordinates with probability densities at most one and a real symmetric matrix having at least three eigenvalues of absolute value at least one, prove a universal essential-supremum bound for the density of `Q=X^T A X`, or give a counterexample. No moment, support, log-concavity, sign, or post-rotation independence assumption is used here.

This report proves a new pivot-plus-bilinear-block criterion. It retains arbitrary extra spectral directions and arbitrary self blocks. It does **not** prove the bare three-eigenvalue hypothesis forces the criterion, so it is not a full solution. The conclusion below is essential boundedness and hence an `O(|L|)` interval estimate. Continuity of the full output density is **not** proved by this argument.

## 2. Source-pinned inputs

1. Fresh control source read at start: `yspennstate/math-research-brain@78662a360fecd178e0c343e1107cecde5ea3cc70`, including `AGENTS.md`, `scheduled_tasks/README.md`, `fleet.json`, `roles.json`, `PROTOCOL.md`, programme manifest/current research/claims/corrections/memory protocol, and `assignments/account03/B09.json`.
2. Ridge characteristic-function envelope: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`, especially (5.4). For a residual cross block `N`, scale `gamma>0`, `1<=q<=2`,

   `K=N N^T (gamma^2 I+N N^T)^(-1)`, `theta=tr K`, `D=det(I+N N^T/gamma^2)`,

   if `max_i K_ii<=q/2`, then

   `|phi_R(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q))`,

   with `L_q=pi e sqrt(2/q)`. The source proof allows arbitrary self blocks, outside couplings, signs, and bounded-density product laws.
3. Overlap-one Schur aggregation used for comparison/application: `yspennstate/math-open-problems@290f3246bf7eaf376522bd67cb58afa841ad86c4`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/B09-20260922T144636Z-r12/REPORT.md`; brain handoff commit `c531f3c1b56c9a434013af4c71fa0696bb7c3469`. It proves `E_P E2(S_i[P,P^c])=M1_i/(16 a^2)` for a physical pivot `a=A_ii!=0`.

The designated partner is `account04/B09`. At the fresh-source checks there was no completed current-QFORM `account04/B09` artifact in either the shared handoff root or the canonical QFORM archive. I therefore did not fabricate partner consumption; this run proceeds asynchronously using the completed ridge proof and the completed account01/B09 aggregation result. A later completed `account04/B09` result should be applied on the next run.

## 3. New theorem: a square pivot lowers the ridge threshold by one effective Fourier dimension

Let `k` be an original physical coordinate with

`a=A_kk != 0`.

Write `Z=X_{-k}` and form the scalar Schur complement

`S=A_{-k,-k} - A_{-k,k} A_{k,-k}/a`.

Choose disjoint sets `I,J` of the residual **original** coordinates and put

`N=S[I,J]`.

Fix `gamma>0`, `1<=q<=2`, and define

`K=N N^T (gamma^2 I+N N^T)^(-1)`,

`theta=tr K`,

`D=det(I+N N^T/gamma^2)`.

Assume

`max_i K_ii <= q/2` and `theta>q`.

Then `Q=X^T A X` has an essentially bounded density. More quantitatively, for every

`r in (max(1,2q/theta), 2)`, `p=r/(r-1)`, `beta=theta/(2q)`,

one has

`||p_Q||_infinity <= |a|^(-1/2) P_r (2pi)^(-1/2) C_r^(r/2)
                     * [2 t0 beta r/(beta r-1)]^(1/2)`,

where

`P_r = 1 + (1-r/2)^(-1/r)`,

`C_r = r^(1/(2r)) / p^(1/(2p))`,

`t0 = [L_q/(2 gamma)] D^(-1/(2 theta))`.

Therefore every interval `L` satisfies

`P(Q in L) <= ||p_Q||_infinity |L|`.

The threshold is `theta>q`, not the direct-ridge threshold `theta>2q`. The extra physical square pivot supplies the missing half-order singular integration.

### Proof

Complete the square in the original coordinate `X_k`. With

`ell(Z)=A_{k,-k} Z/a`,

we have the exact identity

`Q = a (X_k + ell(Z))^2 + R(Z)`,

where `R(Z)=Z^T S Z`. Importantly, `Z` still consists of the original mutually independent coordinates.

Apply the source ridge envelope to `R`, using the cross block `N=S[I,J]`. It gives

`|phi_R(t)| <= min(1,(t0/|t|)^beta)`,

with `beta=theta/(2q)`. If `r>2q/theta`, then `beta r>1`, and therefore

`||phi_R||_r^r <= 2 t0 [1 + 1/(beta r-1)]
                = 2 t0 beta r/(beta r-1)`.

By inverse Hausdorff-Young in the convention `hat f(t)=int exp(itx)f(x)dx`, the law of `R` has an `L^p` density with `p=r/(r-1)>2` and

`||p_R||_p <= (2pi)^(-1/r) C_r ||phi_R||_r`.

Now condition on `Z`. Since the density of `X_k` is at most one, the pushforward of `a(X_k+ell(Z))^2` has conditional density bounded by

`|a|^(-1/2) s^(-1/2)`

on the appropriate half-line `s>0`; the shift `ell(Z)` does not change this bound. Consequently, for almost every `y`,

`p_Q(y) <= |a|^(-1/2) int_0^infinity s^(-1/2) p_R(y - sign(a)s) ds`.

Let `M=||p_R||_p` and let `r=p/(p-1)` be its conjugate exponent. Split the integral at `T=M^(-r)`. On `(0,T)`, Holder gives

`int_0^T s^(-1/2) p_R(y-sign(a)s) ds
 <= M [int_0^T s^(-r/2) ds]^(1/r)
 = (1-r/2)^(-1/r) M^(r/2)`.

On `(T,infinity)`, use only total mass one:

`int_T^infinity s^(-1/2) p_R(y-sign(a)s) ds <= T^(-1/2)=M^(r/2)`.

Hence

`||p_Q||_infinity <= |a|^(-1/2) P_r M^(r/2)`.

Substituting the Hausdorff-Young estimate and the preceding `L^r` estimate for `phi_R` gives exactly the displayed bound. This proves existence of an essentially bounded density and the linear interval estimate. No square-root small-ball decoupling is used.

## 4. Clean q=1 endpoint: two effective cross directions with diffuse ridge leverage

Take `q=1`, assume

`max_i K_ii <= 1/2`, `theta>=3/2`,

and choose `r=5/3`, `p=5/2`. Then `beta r>=5/4`, so

`||phi_R||_(5/3)^(5/3) <= 10 t0`.

With

`C_(5/3)=(5/3)^(3/10)/(5/2)^(1/5)`,

the theorem becomes

`||p_Q||_infinity <= C_* |a|^(-1/2) gamma^(-1/2) D^(-1/(4theta))`,

where

`C_*=(1+6^(3/5)) C_(5/3)^(5/6) sqrt(5 e sqrt(2)/2)
    = 11.8829259763...`.

Because `log D >= theta`,

`D^(-1/(4theta)) <= e^(-1/4)`,

and hence the simpler estimate

`||p_Q||_infinity <= 9.2544320556... / sqrt(|a| gamma)`.

This branch allows `rank(N)>2`; all extra singular directions and self blocks remain in the form.

## 5. No-leverage endpoint: three effective cross directions

Set `q=2`. Then `max_i K_ii<=1=q/2` is automatic, so no leverage hypothesis remains. The general theorem needs only `theta>2`.

In particular, if `N` has three singular values at least `sigma>0`, choose `gamma=sigma/3`. Then each of those three directions contributes at least `9/10` to `theta`, so

`theta>=27/10>2`.

Using `r=5/3`, one gets a completely dimension-free bound

`||p_Q||_infinity <= 18.1 / sqrt(|a| sigma)`

(the exact safe numerical constant from the displayed formula is below 18.084 after `log D>=theta`).

Thus a genuine physical square pivot plus three substantial Schur cross singular values gives an `O(|L|)` small-ball estimate with arbitrary rank, arbitrary extra eigenvalues, and no cross-range leverage assumption.

## 6. Application to the source-valid singleton-plus-two-banks obstruction

Consider the exact-rank-three family used in the correction archive,

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`.

Its nonzero spectrum is `{1,1,-1}`. For even `m>=4`, use the singleton as the physical pivot, so `a=1`, and split each of the two size-`m` banks into two halves. The residual Schur cross block has exactly two nonzero singular values

`s_1=s_2=1/2`.

Choose `gamma=1/(2 sqrt(3))`. Then the two ridge eigenvalues are both `3/4`, hence

`theta=3/2`, `D=16`.

On either row bank the ridge diagonal is `(3/4)/(m/2)=3/(2m)<=1/2`, so the q=1 theorem applies and yields

`||p_Q||_infinity <= 13.933`.

This is uniform in `m` and uses the high-cardinality physical bank rather than any fixed local minor. It is consistent with, and independently recovers a uniform payment for, the family that refutes the naive local-cross-rank dichotomy.

## 7. Relation to overlap-one aggregation and the remaining first implication

The account01/B09 identity aggregates all overlap-one 3x3 minors through a common physical pivot before paying a local inverse minor. The theorem above removes the former **exact-rank-two** restriction on the resulting Schur cross cut whenever that cut has a ridge certificate with `theta>q`. In particular:

* diffuse two-direction ridge mass is enough via `q=1`;
* any three sufficiently effective ridge directions are enough via `q=2`, with no leverage condition.

The remaining structural debt is therefore sharper:

`QFORM-PIVOT-RIDGE-EXTRACTION-v1` — starting only from three eigenvalues `|lambda|>=1`, prove that one can find either (i) a directly controlled diagonal/three-bank branch already in the archive, or (ii) a physical pivot `a` and residual original-coordinate cross block `N` for which the pivot-ridge bound has a universal scale, e.g. `|a| gamma >= c` together with `theta>q` and the needed ridge-diagonal condition when `q<2`.

The known corrections show that one fixed local minor or one exact rank-two Schur extraction is not enough. The new theorem instead permits arbitrary rank and frequency-scale regularization.

## 8. Integrity / correction checks

Consumed corrections include: phase-aligned densities refute law-uniform pointwise quadratic Fourier decay; post-rotation coordinates are not independent; naive fiber-sup integration can lose dimension; a single rank-two Schur extraction is not forced; a local rank-three cross-cut dichotomy is false; and bounded conditional caps do not substitute for original product provenance. None of those refuted premises is used here.

No Gaussian, moment, compact-support, connected-support, log-concavity, or diagonal-basis assumption is introduced. No Monte Carlo evidence is used as proof. Full QFORM remains OPEN and the continuity request remains OPEN for this branch.
