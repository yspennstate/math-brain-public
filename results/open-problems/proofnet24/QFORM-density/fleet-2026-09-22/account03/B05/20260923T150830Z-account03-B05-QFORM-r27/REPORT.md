SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T15:08:30Z.
attacking: QFORM-UNCONDITIONAL-NEAR-PARALLEL-PRODUCT-TRACE-v1 — keep the residual product projection inside one unconditional coarea receiver and close every quantitative nonzero raw-diagonal scalar-pair branch.

# account03/B05 r27 — a sigma-free, kappa-free raw-diagonal exit by Schur-to-fresh-square coarea

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea bound.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval was used, but repository transport is not native learned-memory ingestion.  
**Status:** `NEW SUPPORTING THEOREM / PARTNER APPLIED / FULL QFORM OPEN`.  
**Regularity:** the theorem below proves absolute continuity and an essential `L^infinity` bound in its stated branch. It does not prove continuity.

## 1. The first missing implication from r26

The preceding B05 run proved that conditioning the residual coordinate `R` of a genuine two-dimensional product projection `(S,R)` is too lossy: every positive moment of the fiber cap `||p_(S|R)||_infinity` can diverge even while the actual target-valid quadratic output remains uniformly bounded. Hence the next valid receiver has to keep `R` inside the same unconditional original-product integral.

The live ratio-variance packet from account01/B05 r26 has exactly that form. One original-coordinate bank gives an orthonormal product projection `(S,R)`, and two disjoint rank-one banks give normalized scalar projections `Y,Z`. The homogeneous packet matrix, in the order `(S,R,Y,Z)`, can be written

```
H = [[C,P],
     [P^T,B]],
B = [[a,c],[c,d]],
```

where `B` is invertible and indefinite and

```
C-P B^(-1) P^T = lambda [[m,0],[0,0]],
mu = |det B| |lambda|.                                             (1.1)
```

Here `m>0` is the packet Schur-direction mass; the ratio-packet lemma supplies a packet with `m>=3/20` at its fixed `h=1` choice. The residual size `sigma` is encoded in how `(S,R)` was formed, but (1.1) is exact for every `sigma>0`. No independence between `S` and `R` is asserted.

The main point of this run is that if either raw scalar-bank diagonal `a` or `d` is nonzero, the residual `R` can be retained completely unconditioned and the branch is paid without either the physical-pair condition number `kappa` or the ratio residual `sigma`.

## 2. Source theorems actually consumed

### 2.1 Ratio-variance packet normal form

Canonical source:

`yspennstate/math-open-problems@b0299facc04ea0c03276dddb1a12c027aed5a946`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T033640Z-account01-B05-QFORM-r26/REPORT.md`.

It supplies (1.1), the genuine original-coordinate product provenance of `(S,R,Y,Z)`, and a packet with `m>=3/20`.

### 2.2 Fresh-bank translated-square receiver

Consumed source:

`yspennstate/math-open-problems@552cc02b9161cc94ce42b04200799d1ebd3635f2`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T113953Z-account01-B16-QFORM-r12/REPORT.md`.

Its equation (1.1), ultimately based on the orientation-free rank-two affine half-Riesz theorem, says the following. For disjoint original-coordinate banks `I,J`, let

```
P0 = M X_I in R^2,     Z0=n^T X_J,
```

with `rank M=2`, let `L` be invertible symmetric `2x2`, let `gamma!=0`, allow an arbitrary affine term on the whole `I` bank, and allow an arbitrary same-`I`-bank measurable shift `h(X_I)` inside the fresh square. Then

```
||p_[P0^T L P0 + d0^T X_I+c0 + gamma(Z0+h(X_I))^2]||infinity
 <= 128 sqrt(2)/(||n|| sqrt(|gamma|))
    [det(MM^T)|det L|]^(-1/4).                                  (2.1)
```

This theorem is exactly suited to the present obstruction because the whole dependent residual coordinate may remain in the receiver bank `I`; it is never conditioned.

### 2.3 Designated partner account04/B05

Canonical source:

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`.

If `m_*` is the largest positive exact-slope mass, its theorem gives

```
||p_Q||infinity < 51.6 (mu m_*)^(-1/3).                         (2.2)
```

Section 6 applies this to the exact double-zero complement of the new theorem.

## 3. Algebraic lemma: a nonzero scalar pivot exposes the entire rank-two Schur resource

The packet matrix `H` in (1.1) has rank exactly three. Indeed `B` is invertible and its Schur complement has rank one, hence

```
rank H = rank B + 1 = 3.                                          (3.1)
```

Assume first that

```
d=H_ZZ !=0.                                                       (3.2)
```

Write `W=(S,R,Y)`. Partition

```
H = [[A,v],
     [v^T,d]],
```

and define the scalar-pivot Schur complement

```
N=A-vv^T/d.                                                        (3.3)
```

By (3.1)-(3.2),

```
rank N=2.                                                          (3.4)
```

For a real symmetric rank-two `3x3` matrix `N`, let `pdet(N)` be the product of its two nonzero eigenvalues. Then

```
boxed:
 |pdet(N)| = sum_(i<j) |det N_[i,j]|.                              (3.5)
```

To prove (3.5), write

```
N=V diag(alpha,beta) V^T,     V^T V=I_2.
```

Cauchy--Binet gives

```
det N_[i,j] = alpha beta det(V_[i,j])^2.
```

All nonzero physical `2x2` principal minors therefore have the same sign, and another Cauchy--Binet identity gives

```
sum_(i<j) det(V_[i,j])^2=det(V^TV)=1.
```

This proves (3.5).

Now use the scalar Schur determinant identity. For every pair `i<j` among `(S,R,Y)`,

```
det H_[i,j,Z] = d det N_[i,j].                                    (3.6)
```

Define the full principal-minor packet through the physical `Z` pivot by

```
Pi_Z = sum_(i<j in {S,R,Y}) |det H_[i,j,Z]|.                       (3.7)
```

Equations (3.5)-(3.6) give the exact aggregate identity

```
boxed:
 Pi_Z = |d| |pdet(N)|.                                             (3.8)
```

The crucial point is that this spends the whole rank-two Schur resource before selecting any one physical two-coordinate receiver.

There is also a protected lower bound already built into the ratio packet. The principal `3x3` block on `(S,Y,Z)` has Schur complement `lambda m` over `B`, so

```
det H_[S,Y,Z] = det(B) lambda m.
```

Hence

```
boxed:
 Pi_Z >= mu m.                                                     (3.9)
```

No condition number of `B`, no residual scale `sigma`, and no conditional density of `S|R` enters (3.8)-(3.9).

## 4. Main theorem: raw-diagonal fresh-square exit

### Theorem `QFORM-RATIOPACKET-RAWDIAG-FRESH-SQUARE-v1`

Under the ratio-packet hypotheses (1.1), put

```
delta_B=max(|a|,|d|).
```

If `delta_B>0`, then the full conditional packet form, with arbitrary affine terms generated by all conditioned outside original coordinates, has an essentially bounded density satisfying

```
boxed:
 ||p_Q||infinity
 <= 128 sqrt(2) (delta_B mu m)^(-1/4).                             (4.1)
```

The estimate is completely independent of both the ratio residual `sigma` and the scalar-pair minimum singular value `kappa`.

### Proof

Suppose first `|d|=delta_B>0`. Complete the physical scalar `Z` exactly, including its affine term. With `W=(S,R,Y)`, the conditional polynomial becomes

```
Q = W^T N W + ell^T W+c
    + d [Z+h(W)]^2,                                                (4.2)
```

where `N` is (3.3) and `h` is affine in `W`. In original coordinates, `W` consists of three orthonormal linear forms supported on the union `I` of the first packet bank and the `Y` bank. The `Z` scalar is a unit-norm projection of a disjoint original-coordinate bank `J`.

Because `N` has rank two, choose an orthonormal eigenframe `V in R^(3x2)` for its nonzero range and write

```
N=V Lambda V^T,     Lambda=diag(alpha,beta), alpha beta!=0.
```

If `C_I` denotes the three-column orthonormal coefficient frame of `W` in the original `I` coordinates, then

```
P0=V^T W=(C_I V)^T X_I
```

is a two-dimensional orthonormal product projection. Thus in (2.1) one may take

```
det(MM^T)=1,     |det Lambda|=|pdet(N)|,     ||n||=1,
 gamma=d.
```

The affine term in (4.2) is arbitrary on the entire `I` bank, and the shift `h(W)` is an allowed same-bank shift. Therefore (2.1) gives

```
||p_Q||infinity
 <=128 sqrt(2) |d|^(-1/2)|pdet(N)|^(-1/4).
```

Using (3.8),

```
|d|^(-1/2)|pdet(N)|^(-1/4)
 = (|d| Pi_Z)^(-1/4).
```

Then (3.9) yields

```
||p_Q||infinity
 <=128 sqrt(2)(|d| mu m)^(-1/4),                                  (4.3)
```

which is (4.1) in this case.

If instead `|a|=delta_B>0`, interchange the two independent scalar banks `Y,Z`, repeat the same scalar-pivot Schur argument, and obtain

```
||p_Q||infinity
 <=128 sqrt(2)(|a| mu m)^(-1/4).                                  (4.4)
```

This proves (4.1). QED.

### What the theorem pays

This is an unconditional product-preserving receiver. The dependent pair `(S,R)` is never split into conditional fibers. In particular the fragmented construction from r26, where every positive moment of `||p_(S|R)||infinity` diverges, causes no loss in (4.1).

The new theorem is also complementary to r22's pair-log theorem

```
||p_Q||infinity
 <=8*2^(3/4)*sqrt(5) (mu kappa m)^(-1/4),                          (4.5)
```

because (4.1) replaces `kappa` by the raw physical diagonal scale `delta_B`. Near an off-diagonal double-zero pair, `kappa` may remain comparable to `|c|` while `delta_B` vanishes; away from that endpoint, (4.1) closes the packet without paying the pair condition number.

## 5. Quantitative packet corollary

The ratio-packet selection lemma at `h=1` gives

```
m>=3/20.                                                           (5.1)
```

Therefore every branch with

```
mu>=mu_0>0,     delta_B>=delta_0>0
```

obeys

```
boxed:
 ||p_Q||infinity
 <=128 sqrt(2) [(3/20)mu_0 delta_0]^(-1/4).                        (5.2)
```

For the concrete threshold `mu_0=1`, `delta_0=1/16`,

```
||p_Q||infinity <581.745.                                          (5.3)
```

The numerical value is not intended to be sharp. Its significance is that the estimate is dimension-free and survives `sigma/sqrt(m)->0` and arbitrary fragmentation of the input supports.

A finite algebraic diagnostic was also run on 1000 random invertible symmetric `B`, random cross blocks `P`, nonzero `lambda`, and `m in[0.1,1]`. For every usable nonzero `Z` pivot, the computed rank-two Schur complement satisfied the same-sign principal-minor identity (3.5); the maximum floating discrepancy between `pdet(N)` and `e_2(N)` was `2.91e-8`. This is only a regression check; the proof is (3.5)-(3.8).

## 6. Designated partner account04/B05 applied to the complementary endpoint

The new theorem requires a nonzero raw scalar diagonal. At the exact double-zero endpoint

```
a=d=0,     B=[[0,c],[c,0]],     c!=0,                              (6.1)
```

it intentionally gives no bound. The designated account04/B05 theorem (2.2) supplies a genuinely different exit when the slope measure has an atom.

For an actual quantitative branch, take

```
mu>=1,     m_*>=1/4.
```

Then (2.2) gives

```
boxed:
 ||p_Q||infinity
 <51.6*4^(1/3)
 <81.91,                                                            (6.2)
```

uniformly in the off-diagonal scale `c`. In particular one may take the exact double-zero family with `lambda=c^(-2)`, so `mu=c^2|lambda|=1`; (6.2) remains fixed as `c->0`. This explicitly shows that the exact-slope aggregate mechanism covers a portion of the branch where the raw-diagonal theorem is silent.

Together with r22's exact-double-zero residual-coupling theorem

```
||p_Q||infinity
 <14.7240 [mu m (eta_R/|c|)^2]^(-1/3),                             (6.3)
```

the remaining endpoint has to evade three distinct aggregate receivers simultaneously.

## 7. The remaining B05 obstruction is now narrower

The present run eliminates the general phrase “near-parallel residual packet” as the obstruction. The residual itself is not the issue. A true survivor of the current coarea package must approach the following simultaneous regime:

1. `delta_B=max(|a|,|d|)->0`, so the new raw-diagonal fresh-square receiver (4.1) is unavailable quantitatively;
2. no positive exact-slope mass `m_*` bounded below, so account04/B05 cannot pay the packet by (2.2);
3. in the exact-double-zero limit, the normalized residual raw coupling `eta_R/|c|->0`, so r22's null-scalar determinant receiver (6.3) also degenerates;
4. the aggregate determinant parameter `mu` and packet mass `m` remain the resources that must be preserved before inversion;
5. all arbitrary affine leakage, unbounded/fragmented input supports, and original-coordinate product provenance must remain intact.

The next precise B05 implication is therefore

### `QFORM-NEAR-DOUBLEZERO-ESCAPED-CURVATURE-COAREA-v1`

Retain the small scalar diagonals exactly, and prove that when both raw diagonals and the residual-to-offdiagonal coupling vanish relative to the packet determinant resource, the forced third curvature must appear in a different original-coordinate aggregate that can be coupled to the same unconditional coarea integral before any reciprocal minor is paid.

Small `a,d` cannot be dropped as small random errors because the original variables have no moment or support assumptions. The next mechanism should therefore be a determinant/Pluecker aggregation or a fresh-bank transducer, not a perturbative truncation and not conditioning on `R`.

## 8. Scope

This report proves a new source-valid supporting theorem for the live ratio packet and applies the designated partner result to a complementary exact endpoint. It does **not** prove the unrestricted three-large-eigenvalue conjecture and does not produce a counterexample. No Gaussianity, moment bound, log-concavity, compact support, connected support, diagonal-basis independence, or conditional projection-density cap was used.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Full-target continuity remains open.
