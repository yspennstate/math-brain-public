# fleet02/B14 auto11 — two-neighbor determinant flow at the multiplicity-eight endpoint

Run: `20260924T150131Z-fleet02-B14-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Baseline source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

**Status:** proved structural strengthening of the unpaid `s_8` chamber; **not** a multiplicity-eight density theorem. The lowest complete threshold independently reconstructed in this run is still nine. The unrestricted three-eigenvalue conjecture remains open.

Keep the baseline constants

`eta=1/100,   kappa=1/80^2=1/6400.`

## Theorem — residual-good order-two seeds force two ~44x heavier neighbors

Assume

1. `A=A^T` has no `eta`-pivot;
2. `s_8(A)>=1`;
3. `V_3(A)<kappa^3`.

Then `s_5(A)>=1`, so the audited baseline order-two spectral-to-volume proposition gives

`V_2(A)>=kappa^2.`

Therefore

`V_3(A)/V_2(A)<kappa.`

Apply the audited volume-sampling lemma at order `r=2`. There are disjoint two-sets `S,T` with nonsingular seed

`B=A[S,T]`

such that, writing `L=[n]\(S union T)` and

`P=A[:,T] B^{-1} A[S,:]`,

`E[L,L]=offdiag(A[L,L]-P[L,L])`,

we have

`||E||_F^2 <=9 V_3/V_2 <9 kappa,`

hence

`epsilon:=||E||_F<3/80.`                                          (1)

Let `A=D+R+E` be the baseline completion. Then

`rank R<=6`, `D=0` on `S union T`, `E_ii=0`, and `R[L,L]=P[L,L]`.

There is a two-set `H subset L` such that, if

`b=|det A[S,T]|`,
`c=|det A[H,T]|`,
`e=|det A[S,H]|`,

then

`boxed: c>gamma b  and  e>gamma b,`                               (2)

where

`gamma = 5(3583-3 sqrt(101))/404
       = 43.97092045961185... .`                                  (3)

Thus one residual-good sampled seed necessarily creates **two** neighboring disjoint order-two crossing minors, one replacing the row set and one replacing the column set, each more than forty-three times heavier in determinant magnitude.

### Proof

From (1), singular-value perturbation gives

`s_8(D+R)=s_8(A-E)>1-3/80=77/80.`

Since `rank R<=6`, the baseline rank-shift inequality gives

`s_2(D) >= s_8(D+R) >77/80.`                                    (4)

Because `D` is diagonal and vanishes on `S union T`, choose two indices

`H={h_1,h_2} subset L`

with

`|D_hh|>77/80.`                                                   (5)

The no-pivot condition gives

`|A_hh|<1/100`

and, for distinct indices,

`|A_ij|^2 < eta+eta^2 =101/10000,`

so

`|A_ij|<sqrt(101)/100.`                                          (6)

On `H x H`, `R=P` and `E` has zero diagonal. Hence (5) gives

`|P_hh|=|R_hh|=|A_hh-D_hh|>77/80-1/100=381/400.`                 (7)

For `h_1!=h_2`, (1) and (6) give

`|P_h1,h2|=|R_h1,h2|
 <=|A_h1,h2|+|E_h1,h2|
 <sqrt(101)/100+3/80
 =(4 sqrt(101)+15)/400.`                                         (8)

Therefore

```
|det P[H,H]|
 >= |P_h1,h1 P_h2,h2|-|P_h1,h2 P_h2,h1|
 > (381/400)^2-((4 sqrt(101)+15)/400)^2
 = (3583-3 sqrt(101))/4000
 = 0.8882125932841594... .                                      (9)
```

The interpolation factorization restricted to `H x H` is exact:

`P[H,H]=A[H,T] B^{-1} A[S,H].`

Taking determinants in absolute value gives

`c e = b |det P[H,H]|.`                                         (10)

Every entry of either disjoint `2 x 2` matrix `A[H,T]` and `A[S,H]` is off-diagonal, so (6) and Hadamard imply

`c,e < 2(101/10000)=101/5000=:U.`                               (11)

Combining (9)–(11),

```
c > [(3583-3 sqrt(101))/4000]/U * b,
e > [(3583-3 sqrt(101))/4000]/U * b.
```

The common ratio is exactly (3). This proves (2).

## Consequences

### 1. A residual-good seed is never even a one-step determinant maximum

Under the unpaid `s_8` assumptions, any nonsingular order-two seed with residual norm `<3/80` admits **both** a row-exchange and a column-exchange neighbor whose determinant is `>43.97` times larger. In particular, a determinant-maximal order-two seed must have residual norm at least `3/80`.

This identifies a precise mismatch in the current proof architecture: volume sampling finds small residual in a determinant-squared average, while the spectral information forces the particular small-residual seed to lie far down an ascending determinant chain.

### 2. Explicit upper bound on the good seed determinant

From `c<=U` and `c>gamma b`,

`b < U/gamma = 0.00045939452230830816... .`                     (12)

This alone does not contradict `V_2>=kappa^2` because the number of order-two seeds is dimension-dependent; one cannot replace the missing argument by a fixed-fragment count.

### 3. What would close the exchange route

A dimension-free proof that **one** of the two amplified neighbors in (2) inherits a residual bound `<3/80` would immediately allow strict determinant ascent. Iterating cannot cycle. To turn that into a contradiction one still needs a dimension-free stopping/charging principle, because the initial determinant may be arbitrarily small and the number of possible seeds grows with dimension.

A more realistic target is a weighted exchange inequality showing that the determinant-squared mass of residual-good seeds cannot all flow into residual-bad neighbors with unbounded multiplicity. The baseline sampling identity controls the weighted mean residual, so such a charging lemma would convert the present local amplification into a global contradiction.

## Counterexample to the wrong analytic shortcut

The determinant-flow theorem should not be replaced by a theorem asserting that a robust two-anchor cross determinant by itself implies a bounded quadratic density. That statement is false even for cap-one product uniforms.

Let `0<eps<1`, let `U_1,U_2,V_1,V_2` be independent `Unif[-1/2,1/2]`, and put

`K=eps [[0,1],[1,0]],  C=I_2,  R=K^{-1}.`

For

`Q=U^T K U+2 U.V+V^T R V`

we have `det(CC^T)=1`, but

`Q=(U+K^{-1}V)^T K(U+K^{-1}V)
  =2 eps Z_1 Z_2,`

where

`Z_1=U_1+V_2/eps`, `Z_2=U_2+V_1/eps`

are independent. Their common density equals `eps` on

`|z| <= (1-eps)/(2eps)`.

Hence the product formula gives, for all sufficiently small nonzero `t`,

`p_Q(t) >= (eps/2) log(c_eps/|t|) -> infinity.`                  (13)

The full four-dimensional quadratic matrix here has Schur complement zero and rank two, so (13) is **not** a counterexample to the fixed-multiplicity theorem or to unrestricted QFORM. It is a source-valid obstruction to a determinant-free two-anchor `L^infinity` receiver. The `s_8` proof must spend additional shared-anchor/Schur curvature, or exploit the determinant exchange structure above.

## Current threshold status

- baseline `s_17`: PASS in this run's full audit;
- complete rough-law theorem at `s_9`: independently reconstructed in this run, with conservative constant `<5338 K^2/s`;
- `s_8`: OPEN;
- unrestricted `s_3`: OPEN.

The new unpaid implication is therefore:

> **Either prove a dimension-free weighted exchange/charging principle for the two amplified order-two neighbors, or construct a shared-anchor overlap receiver that uses the extra Schur curvature before one-sided decoupling loses it.**
