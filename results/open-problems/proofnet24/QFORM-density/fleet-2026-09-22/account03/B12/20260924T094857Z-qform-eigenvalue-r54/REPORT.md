SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T09:48:57.429592Z.
attacking: two-sided relative-resonance stability: large negative spectral overshoot is protective once the quadratic square term is retained; arbitrary noncommutativity costs at most a half-mode factor, while a small normalized commutator preserves all nonresonant modes.

# account03/B12 — two-sided resonance-window stability for arbitrary signed additions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T094857Z-qform-eigenvalue-r54`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING STABILITY THEOREMS / FULL QFORM OPEN**  
Continuity: **not proved by this run; the six-mode receiver used below gives absolute continuity plus an essential L-infinity bound, but its theorem as a whole does not claim a continuous representative.**  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source boundary

The owner target remains the unrestricted statement: for every `n`, independent real ORIGINAL-coordinate inputs `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density with a universal essential `L^infinity` bound, or give a valid counterexample.

No Gaussianity, log-concavity, moments, compact support, connected support, iid hypothesis, diagonal-basis independence, or post-rotation independence is used below. The new results are deterministic matrix inequalities on ORIGINAL-coordinate carriers. Added quadratic pieces are never peeled off as independent convolutions.


Two completed dependencies are used at equations:

1. **Designated partner account04/B12 r8**, `yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T002154Z-account04-B12-multihub-shear-r8/REPORT.md`.
   Its theorem `QFORM-MULTIHUB-ALIGNED-SPECTRAL-PACKET-STABILITY-v1` proves
   ```
   s_(p+ell)(P_H A_*)
   >= gamma(||Lambda^{-1}W^T||) min{s_p(Lambda),s_ell(R)},
   gamma(t)=(sqrt(t^2+4)-t)/2,
   ```
   for the final pre-tail physical carrier with `C_*=U Lambda U^T`,
   `B_*=UW^T+R`, `U^T R=0`.

2. **Completed six-square-mode receiver**, account02/B12 at
   `yspennstate/math-open-problems@c635fcdce6aa206c68f1f14e061cf617d72376fb`,
   theorem `QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2`. If `H` is an ORIGINAL-coordinate set of size `m>=6` and
   `lambda_6((A^2)[H,H])>=h^2>0`, then
   ```
   ||p_(X^TAX)||_(infinity,ess) <= C_m/h,
   C_m=max{
      8 N_2 sqrt(6 pi m),
      4 pi N_2,
      3*400^(1/3)*(4N_2)^(5/6),
      10 sqrt(2e/3)
   },
   N_2=binom(m,2).
   ```
   That source explicitly does **not** claim continuity for the theorem as a whole.

The previous account03/B12 r53 theorem is preserved at
`yspennstate/math-open-problems@ee98b8445086ec2ab29bdd8aa62dbcc4f433def4`.
It retained only a one-sided lower bound from the normalized anticommutator. The present run changes mechanism by retaining the full square term and treating the resonance point `-1` two-sidedly.

## 2. Exact whitened carrier identity

Let `M in R^(n x m)` have full column rank. Put

```
G=M^T M,          g=s_m(M)>0,
U=M G^(-1/2).
```

Then `U^T U=I_m`. For an arbitrary added carrier action
`N in R^(n x m)`, define

```
B = G^(-1/2) M^T N G^(-1/2),
C = N G^(-1/2),
Z = (I-UU^T) C.
```

Since `U^T C=B`, one has the orthogonal decomposition

```
C=UB+Z,           U^T Z=0,
(M+N)G^(-1/2)=U(I+B)+Z.                       (2.1)
```

Therefore

```
[(M+N)G^(-1/2)]^T[(M+N)G^(-1/2)]
=(I+B)^T(I+B)+Z^T Z.                           (2.2)
```

Consequently, for every singular index `j=1,...,m`,

```
s_j((M+N)G^(-1/2)) >= s_j(I+B).                (2.3)
```

Also
`M+N=[(M+N)G^(-1/2)]G^(1/2)`. The standard singular-value product inequality
`s_j(XY)>=s_j(X)s_m(Y)` for invertible square `Y` gives

```
boxed: s_j(M+N) >= g s_j(I+B).                 (2.4)
```

A short min-max proof of the product inequality is included for completeness. Let `V` be a `j`-dimensional right subspace on which `X` expands by at least `s_j(X)`. Then `Y^{-1}V` has dimension `j`; for unit `x` in it, `y=Yx in V` satisfies `||y||>=s_m(Y)`, so
`||XYx||>=s_j(X)||y||>=s_j(X)s_m(Y)`.

Equation (2.2) is the key correction to a one-sided first-order analysis: very negative relative interaction can be repaired by the positive quadratic term `B^T B` and by transverse square energy `Z^TZ`.

Write

```
H=(B+B^T)/2,       K=(B-B^T)/2,                (2.5)
```

so `H` is symmetric and `K` is skew-symmetric.

## 3. Arbitrary noncommutativity: a bipolar spectral-gap shield

Fix `rho>0`. Let the eigenvalues of `H` be `mu_1,...,mu_m`, with multiplicity, and define

```
V_+ = spectral subspace of H for [ -1+rho, +infinity ),
V_- = spectral subspace of H for ( -infinity, -1-rho ],
d_+ = dim V_+,   d_- = dim V_-,
d=max{d_+,d_-}.                               (3.1)
```

### Theorem 3.1 — `QFORM-BIPOLAR-ANTICOMMUTATOR-GAP-SHIELD-v1`

For arbitrary `N`, with **no bound whatsoever on `K`**, one has

```
boxed: s_d(M+N) >= g rho.                       (3.2)
```

If

```
q = #{i: -1-rho < mu_i < -1+rho},             (3.3)
```

then `d_+ + d_- = m-q`, hence

```
boxed:
s_(ceil((m-q)/2))(M+N) >= g rho.                (3.4)
```

(The statement is interpreted only when the displayed index is positive.)

### Proof

For `x in V_+`,

```
x^T(I+B)x
=||x||^2+x^T Hx
>=rho ||x||^2,                                  (3.5)
```

because `x^T Kx=0`. Cauchy-Schwarz gives

```
||(I+B)x|| ||x|| >= |x^T(I+B)x|
                  >= rho ||x||^2,
```

so `||(I+B)x||>=rho||x||` on the entire `d_+`-dimensional subspace. The singular-value min-max principle gives
`s_(d_+)(I+B)>=rho`.

Likewise, for `x in V_-`,

```
x^T(I+B)x <= -rho ||x||^2,
```

so again `||(I+B)x||>=rho||x||` and
`s_(d_-)(I+B)>=rho`.

Taking the larger of the two subspaces yields
`s_d(I+B)>=rho`, and (2.4) proves (3.2). Since the three disjoint spectral regions in (3.1)-(3.3) exhaust the spectrum of `H`,
`d_++d_-=m-q`, so `d>=ceil((m-q)/2)`, proving (3.4). QED.

### Interpretation

This is a genuinely two-sided resonance statement. A mode with normalized signed interaction far below `-1` is **not** automatically destructive: it has overshot the cancellation point and becomes large again after squaring. The only dangerous scalar location is a window around the relative cancellation value `-1`. With arbitrary noncommutativity, the proof can safely combine only one side of that window at a time, which is why the worst-case count loses a factor of two.

This theorem has no norm, rank, sign, eigenvalue-magnitude, or commutator restriction on the added matrix action.

## 4. Small normalized commutator: preserve every nonresonant mode

The half-mode loss disappears when the normalized commutator is controlled.

Let

```
kappa=||K||_op.                                 (4.1)
```

### Theorem 4.1 — `QFORM-RESONANCE-WINDOW-COMMUTATOR-SHIELD-v1`

With `q` as in (3.3),

```
boxed:
s_(m-q)(M+N) >= g (rho-kappa)_+.                (4.2)
```

### Proof

Set `D=I+H`. Since `D` is symmetric, its singular values are precisely
`|1+mu_i|`. By definition of `q`, at least `m-q` of these are at least `rho`; hence

```
s_(m-q)(D)>=rho.                                (4.3)
```

Since `I+B=D+K`, rectangular/square singular-value Weyl gives

```
s_(m-q)(I+B)
>=s_(m-q)(D)-||K||
>=rho-kappa.                                    (4.4)
```

Taking the positive part and using (2.4) proves (4.2). QED.

This theorem is strictly stronger than the r53 one-sided anticommutator bound on large negative overshoot. The r53 estimate discards a mode once its first-order interaction passes below `-1`; Theorem 4.1 keeps it unless it lies near the actual cancellation window, with nonnormality paid separately through `kappa`.

## 5. QFORM form: normalized anticommutator and commutator

Let `H0` be `m` literal ORIGINAL coordinates and let `P:R^m->R^n` be their coordinate embedding. Let `A_*` and `E` be arbitrary real symmetric matrices, put

```
M=A_*P,          N=EP,
G=P^T A_*^2 P=M^TM,
```

and assume `M` has full column rank.

Then the matrices in (2.5) become

```
H_E =
  (1/2) G^(-1/2)
  P^T(A_*E+EA_*)P
  G^(-1/2),                                      (5.1)

K_E =
  (1/2) G^(-1/2)
  P^T(A_*E-EA_*)P
  G^(-1/2).                                      (5.2)
```

`H_E` is symmetric and `K_E` is skew-symmetric. Since the final matrix is symmetric,

```
(M+N)^T(M+N)
=P^T(A_*+E)^2P
=((A_*+E)^2)[H0,H0].                             (5.3)
```

Thus Theorems 3.1 and 4.1 are direct statements about the actual final square-energy compression. No random-variable rotation occurs.

### Rank and dense-tail stability

After obtaining a bound
`s_d((A_*+E)P)>=h_0`, add any real symmetric `R_0,T` satisfying

```
rank(R_0P)<=r,       epsilon=||TP||_op.           (5.4)
```

Rank-r singular-value interlacing and Weyl give

```
boxed:
s_(d-r)((A_*+E+R_0+T)P)
>= [h_0-epsilon]_+,                              (5.5)
```

whenever `d-r>=1`.

Therefore, in the commutator-controlled branch, if

```
m-q-r>=6,
h=g(rho-kappa)-epsilon>0,                        (5.6)
```

then

```
lambda_6((A^2)[H0,H0])>=h^2,                    (5.7)
```

and the completed six-mode compiler gives

```
boxed:
||p_(X^TAX)||_(infinity,ess) <= C_m/h.           (5.8)
```

The same conclusion holds in the arbitrary-commutator branch whenever
`ceil((m-q)/2)-r>=6` and
`h=g rho-epsilon>0`.

This is dependence-safe: `R_0` and `T` remain inside the final quadratic form. The theorem uses only deterministic matrix rank and norm information.

## 6. Required partner application: eleven-row multihub carrier

Apply the completed **account04/B12 r8 theorem** at a literal equation, with

```
m=11, p=2, ell=9,
U=(e_1,e_2),
Lambda=4 I_2,
W=0,
R=2 [ 0_(2x9) ; I_9 ].                          (6.1)
```

Then

```
s_2(Lambda)=4,
s_9(R)=2,
||Lambda^(-1)W^T||=0,
gamma(0)=1.
```

The partner theorem gives

```
boxed:
s_11(P_H A_*) >= 2.                              (6.2)
```

Because `A_*` is symmetric, the transposed carrier `M=A_*P_H` has the same singular values, so `g=2`.

### 6.1 Completely noncommuting signed additions: no resonance at all

Let `E=E^T` be **arbitrary** except that its normalized anticommutator `H_E` from (5.1) has no eigenvalue in `(-2,0)`. This is the choice `rho=1`, `q=0`. No condition is imposed on `K_E`, and no rank, sign, norm, or eigenvalue-magnitude bound is imposed on `E`.

Theorem 3.1 gives, because `m=11`,

```
ceil(11/2)=6,
boxed:
s_6((A_*+E)P_H) >= 2.                            (6.3)
```

Now add any further symmetric `T` satisfying only the local condition

```
||TP_H||_op <= 1/4.                              (6.4)
```

The complement-only spectrum of `T` may be arbitrary. Weyl gives

```
boxed:
sqrt(lambda_6((A^2)[H,H])) >= 7/4.               (6.5)
```

For `m=11`, `N_2=55`, and the six-mode compiler constant is

```
C_11
=max{
  440 sqrt(66 pi),
  220 pi,
  3*400^(1/3)*220^(5/6),
  10 sqrt(2e/3)
}
=6335.772588288578... .                          (6.6)
```

Hence

```
boxed:
||p_Q||_(infinity,ess)
<= C_11/(7/4)
=3620.4414790220444... .                         (6.7)
```

Also `s_6(A)>=s_6(AP_H)>=7/4`, so this final family is genuinely in the owner target class (indeed it has at least six eigenvalues of modulus greater than one).

This is an actual end-to-end density branch for **arbitrary noncommuting added spectrum** under a two-sided normalized-antocommutator gap. Continuity is not claimed by the receiver.

### 6.2 Exact cancellation plus a huge negative overshoot

The sharper commutator-controlled theorem shows why the two-sided treatment is materially stronger than r53.

Use the explicit symmetric baseline realizing (6.1) on
`n=20` coordinates, with `H={1,...,11}` and nine complementary coordinates:
two physical diagonal columns of norm four, followed by nine disjoint physical/complement cross columns of norm two. Its carrier singular values are

```
4,4,2,2,2,2,2,2,2,2,2.
```

Fix `L>=3` and choose the relative multipliers

```
beta=(-1,-L,0,2,3,4,5,6,7,8,9).                (6.8)
```

There is a literal real symmetric added matrix `E_L` with

```
(E_L)_(1,1)=4 beta_1,
(E_L)_(2,2)=4 beta_2,
(E_L)_(i,j_i)=(E_L)_(j_i,i)=2 beta_i,
   i=3,...,11,                                   (6.9)
```

where the `j_i` are the nine paired complement coordinates. Then

```
E_L P_H = M diag(beta),                          (6.10)
```

and the normalized interaction is exactly

```
B=H_E=diag(beta),       K_E=0.                   (6.11)
```

For `rho=1`, exactly one eigenvalue (`-1`) lies in the resonance window `(-2,0)`, while the arbitrarily negative mode `-L` lies safely beyond the cancellation window. Thus `q=1`, `kappa=0`, and Theorem 4.1 gives

```
boxed:
s_10((A_*+E_L)P_H) >= 2.                         (6.12)
```

This is exact: the final carrier singular values, in decreasing order for large `L`, include

```
4(L-1), 20,18,16,14,12,10,8,6,2,0,
```

so `s_10=2`.

Now add an arbitrary real symmetric `R_0` satisfying only

```
rank(R_0P_H)<=4,                                 (6.13)
```

with no norm, sign, or eigenvalue-size bound. Rank interlacing preserves

```
s_6((A_*+E_L+R_0)P_H)>=2.                        (6.14)
```

After any further symmetric dense `T` satisfying (6.4),

```
boxed:
s_6(AP_H)>=7/4,                                  (6.15)
```

so the same target-class density bound (6.7) holds.

The added packet `E_L` has unbounded mixed-sign global spectrum as `L->infinity`: the cross-pair blocks contribute positive and negative eigenvalues of magnitudes `2|beta_i|`, while the diagonal part contains a negative eigenvalue of magnitude `4L`.

### Strict comparison with r53

On the same example, the r53 one-sided theorem orders

```
mu_1=-L, mu_2=-1, mu_3=0, ...
```

and after spending only one worst destructive direction (`q=1`) gives the lower bound

```
2(1+mu_2)_+ = 0.
```

It must spend **two** directions before obtaining a positive lower bound. The new resonance-window theorem spends only the genuinely cancelling mode `-1`; the much more negative `-L` direction is recognized as overshoot and is retained. Thus the new theorem protects ten modes rather than nine on this family.

## 7. Deterministic computation

`CHECK.py` and `CHECK_RESULTS.json` accompany this report. They are sanity checks only; every theorem above has an analytic proof.

With deterministic seed `202609240954`:

1. 10,000 random full-column carriers with symmetric interaction spectra entirely outside the `rho=1` resonance window and **arbitrary skew/noncommuting parts** were tested against Theorem 3.1. Violations: `0`. Minimum observed margin:
   `0.4497372627025509`.

2. 10,000 random carriers with up to five resonance-window modes, `rho=0.7`, and random normalized commutator norm at most `0.2` were tested against Theorem 4.1. Violations: `0`. Minimum observed margin:
   `0.21234809042275804`.

3. In the explicit partner-compatible family with `L=10^6`, the checker obtained
   ```
   kappa=0,
   q=1,
   s_10=2 exactly to floating-point precision,
   r53 one-sided q=1 bound=0,
   new q=1 resonance-window bound=2.
   ```
   The six-mode receiver constant after a local `1/4` tail is
   `3620.4414790220444...`.

No histogram, Monte Carlo density estimate, or interval extremality claim is used.

## 8. What is and is not solved

### Proved this run

- `QFORM-BIPOLAR-ANTICOMMUTATOR-GAP-SHIELD-v1`: arbitrary noncommuting additions, no magnitude/rank/sign bound, retain at least half of the modes outside a two-sided relative-cancellation window.
- `QFORM-RESONANCE-WINDOW-COMMUTATOR-SHIELD-v1`: with normalized commutator defect `kappa`, retain **all** nonresonant modes at scale `g(rho-kappa)`.
- Rank-`r` and dense local-tail stability after either shield.
- An actual account04/B12 r8 end-to-end application yielding an essentially bounded density for a target-class family with arbitrary signed additions.
- A literal symmetric hostile-spectrum family with one exact cancellation, one arbitrarily large negative overshoot, arbitrary mixed-sign large modes, four additional completely uncontrolled local-rank directions, and a dense local tail.

### Not proved

The FULL QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The missing structural implication is now sharper:

> Starting only from `s_3(A)>=1`, force an ORIGINAL-coordinate carrier whose normalized anticommutator has a two-sided gap around the true cancellation value `-1` on enough directions, or show that a high-dimensional concentration of relative interaction inside that resonance window forces one of the already-paid projected-crossing, grouped-bank, ridge, hub/common-plane, Schur, physical-core, or Pluecker-volume exits.

The present theorem does **not** prove that every target matrix admits such a baseline/carrier decomposition. Continuity for the full conjecture, and even for the six-mode branch used here, is not established by the cited receiver.

## 9. Source pins

- Fresh control repository: `yspennstate/math-research-brain`, branch `main`; publication-refresh commit recorded in the run receipt.
- Designated partner: `yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`,
  `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T002154Z-account04-B12-multihub-shear-r8/REPORT.md`.
- Six-mode receiver: `yspennstate/math-open-problems@c635fcdce6aa206c68f1f14e061cf617d72376fb`,
  theorem `QFORM-SIX-SQUARE-MODE-PAIR-COMPILER-v2`.
- Previous B12 one-sided theorem preserved for comparison:
  `yspennstate/math-open-problems@ee98b8445086ec2ab29bdd8aa62dbcc4f433def4`,
  `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T084208Z-qform-eigenvalue-r53/REPORT.md`.

Repository transport is not native brain ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.
