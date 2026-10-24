# account02/B02 — square-assisted elementary-symmetric half-Riesz bridge

Run: `20260922T170646Z-account02-B02-QFORM-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`; final owner-control family observed before publication: revision `2026-09-22.8`.  
Assignment: Integrated Fourier estimate.  
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is authenticated transport, not verified native learned-memory receiver ingestion.

## 1. Full target and first unpaid implication

The full target remains: for arbitrary independent real coordinates with probability densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `Q=X^T A X`, or give a valid counterexample. No moments, compactness, diagonal-basis independence, log-concavity, or sign restriction is imposed.

The live proof-first synthesis now has two complementary facts that matter here.

1. account03/B19 proves the full-target branch `s_2(A-diag A)<=499/1000` with density `<84`, and names the surviving task `QFORM-HALF-OFFDIAGONAL-OVERLAP-PAYMENT-v1`: pay the third-compound O0/O1/O2/O3 aggregate structure when the off-diagonal second singular value is larger.
2. My immediately preceding B02 run proved the exact third-compound ledger `sum_{j=0}^3 M_j=e_3(lambda(A)^2)>=1`, where `M_j` is the squared mass of `3x3` minors whose row/column triples overlap in `j` coordinates. In particular some overlap class has mass at least `1/4`.

This run attacks the overlap payment through a physical square plus an *integrated fractional Fourier resource*. It does not attempt the refuted pointwise Fresnel estimate, a conditional projection cap, or a single reciprocal minor.

## 2. Source inputs actually used

### 2.1 Reviewed regularized-determinant theorem

From my independently reviewed report

`yspennstate/math-open-problems@e3fe4ce35f6aa4a90cca913051886c96c7febfc3:proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T140817Z-account02-B02-qform-r11/REPORT.md`,

for an original-coordinate cross block `B` of a quadratic form `R`, for `1<=q<2`, if

`max_i (P_range(B))_ii <= q/2`,

then, with

`c_q=2q/(pi^2 e^2)`,                                                (2.1)

one has

`|phi_R(t)| <= det(I+c_q t^2 B B^T)^(-1/(4q)).`                      (2.2)

For `q=2`, (2.2) is unconditional. Arbitrary self blocks and outside couplings are retained by the source proof; the estimate is produced in original coordinates and does not assume independence after rotation.

The determinant expansion gives for every integer `k>=1`

`det(I+c_q t^2 BB^T) >= 1+c_q^k E_k(B)t^(2k)`,                       (2.3)

where

`E_k(B)=e_k(s_1(B)^2,...)=sum_{|S|=|T|=k} det B[S,T]^2`.             (2.4)

### 2.2 Named partner actually consumed

I consumed account03/B02's completed canonical result

`yspennstate/math-open-problems@16c7d95068defd13bad9f9fe86be6037d046a1ef:proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T160323Z-account03-B02-qform-r11/REPORT.md`.

Its `QFORM-RANK2-BALANCED-CUT-v1` says: if `S=VMV^T` has rank two, `V^T V=I_2`, and `mu=max_i ||v_i||^2`, then whenever

`sqrt(2mu)<tau<1`, `1<=q<2`, `2mu/(1-tau)<=q/2`,                    (2.5)

there is a deterministic physical cut `I,J` for which the cross block `B=S[I,J]` obeys the leverage hypothesis in (2.2) and

`E_2(B) > ((1-tau^2)^2/16) det(M)^2`.                               (2.6)

This partner inequality is applied quantitatively in Section 5 below.

## 3. New theorem: square-assisted `E_k` half-Riesz estimate

### Theorem `QFORM-SQUARE-ASSISTED-EK-HALF-RIESZ-v1`

Let the original variables be split as one physical coordinate `Z` and all remaining independent coordinates `W`. Suppose

`Q = d (Z+h(W))^2 + R(W)`, `d!=0`,                                  (3.1)

where `Z` has density at most one and is independent of `W`; no independence between `h(W)` and `R(W)` is assumed.

Let `B` be any original-coordinate cross block of the quadratic part of `R`. Fix `1<=q<=2`; for `q<2` assume

`max_i(P_range(B))_ii <= q/2`,                                       (3.2)

while for `q=2` there is no leverage condition. Let `k` be an integer satisfying

`k>q`, `E_k(B)>0`.                                                     (3.3)

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= H_{k,q} |d|^(-1/2) E_k(B)^(-1/(4k))`,            (3.4)

where

`H_{k,q} = [sqrt(e)/(k 2^(3/4) q^(1/4))]
            BETA(1/(4k), 1/(4q)-1/(4k)).`                            (3.5)

This theorem is dependence-safe with respect to the square shift: `h(W)` and `R(W)` may be arbitrarily dependent because they are functions of the same remaining product coordinates.

### Proof

For a fixed `W=w`, the pushforward of the cap-one density of `Z` under `d(Z+h(w))^2` has density at output displacement `u` bounded by

`|d|^(-1/2)|u|^(-1/2)`.                                              (3.6)

Therefore the unconditional density exists as a conditional mixture and satisfies, for a.e. `a`,

`p_Q(a) <= |d|^(-1/2) E |R-a|^(-1/2).`                               (3.7)

It remains to bound the half-Riesz potential of `R` uniformly in translation.

With Fourier convention `hat f(t)=int exp(itx)f(x)dx`,

`hat{|x|^(-1/2)}(t)=sqrt(2pi)|t|^(-1/2)`.                            (3.8)

The identity can be justified here without assuming an a priori density for `R` by convolving `|x|^(-1/2)` with a Gaussian approximate identity, applying Fourier inversion, and then using Fatou. Since the right-hand side below is finite, (2.2)--(2.3) give

`sup_a E|R-a|^(-1/2)
 <= (1/sqrt(2pi)) int_R |phi_R(t)| |t|^(-1/2) dt
 <= (1/sqrt(2pi)) int_R |t|^(-1/2)
       [1+c_q^k E_k(B)t^(2k)]^(-1/(4q)) dt`.                         (3.9)

For `gamma>0` and `a0>1/(4k)`, direct substitution `x=gamma t^(2k)` gives

`int_R |t|^(-1/2)(1+gamma t^(2k))^(-a0) dt
 = gamma^(-1/(4k))/k
   BETA(1/(4k),a0-1/(4k)).`                                          (3.10)

Here `a0=1/(4q)`, so finiteness is **exactly** `k>q`. Taking

`gamma=c_q^k E_k(B)`

and using

`c_q^(-1/4)=sqrt(pi e)(2q)^(-1/4)`                                  (3.11)

reduces (3.9) to (3.5). Combining with (3.7) proves (3.4). QED.

### Structural meaning

Direct `L^1_t` inversion of the same determinant envelope requires `k>2q`. A genuine physical square contributes the half-Riesz weight `|t|^(-1/2)` and **halves that threshold to `k>q`**. This is a new integrated-Fourier bridge, not a pointwise-decay statement.

Two useful exact instances are:

- `q=1,k=2`, leverage at most `1/2`:

  `||p_Q||_infinity <= 7.673760 |d|^(-1/2) E_2(B)^(-1/8)`;           (3.12)

- `q=2,k=3`, **no leverage condition**:

  `||p_Q||_infinity <= 9.840656 |d|^(-1/2) E_3(B)^(-1/12)`.          (3.13)

Thus an arbitrary higher-rank Schur remainder is already paid whenever it exposes a dimension-free `E_3` cross aggregate; no projection-leverage gate is needed in that branch.

The theorem does not imply continuity. It proves essential boundedness by a conditional density representation. It also does not prove a target-wide `||phi_Q||_1` bound; the full stronger Fourier criterion remains neither proved nor refuted.

## 4. Exact O1 overlap interface

Let `i` be a physical coordinate with `d=A_ii!=0`, write

`A = [[d,a^T],[a,C]]`,
`S_i = C-aa^T/d`.                                                     (4.1)

For disjoint two-subsets `R,T` of the remaining coordinates, the Schur determinant identity is

`det A[{i} union R,{i} union T] = d det S_i[R,T]`.                    (4.2)

Define the O1 mass attached to the common pivot `i` by

`H_i = sum_{|R|=|T|=2, R cap T=empty}
       det A[{i} union R,{i} union T]^2`.                             (4.3)

Randomly color every remaining coordinate left/right. Each ordered disjoint pair `(R,T)` lands with `R` left and `T` right with probability `1/16`. Hence some cut `L,J` satisfies

`E_2(S_i[L,J]) >= H_i/(16 d^2)`.                                     (4.4)

If a cut satisfying (4.4) also obeys the leverage gate for some `q<2`, Theorem 3 gives the explicit O1 payment

`||p_Q||_infinity
 <= sqrt(2) H_{2,q} |d|^(-1/4) H_i^(-1/8)`.                         (4.5)

Equation (4.5) identifies the exact remaining O1 difficulty: not the minor algebra, not the shared square shift, and not the Fourier integration, but arranging aggregate mass and a non-endpoint leverage certificate simultaneously. In rank-two Schur geometry the named partner does exactly that, as shown next. In higher rank, `q=2,k=3` provides a separate leverage-free escape when a third Schur cross direction is available.

## 5. Named-partner theorem applied to actual inequalities

Substitute the partner lower bound (2.6) into Theorem 3 with `k=2`. The result is

`||p_Q||_infinity
 < sqrt(2) H_{2,q}(1-tau^2)^(-1/4)
   |d|^(-1/2)|det M|^(-1/4).`                                       (5.1)

This is a shorter dependence-safe integrated proof than the partner's `L^r`-density/near-far route, and its constants improve the same localized branches.

For exact rank three, the partner's Schur determinant identity is

`|det M|=|det Lambda| ell/|d|`,                                      (5.2)

where `ell` is the spectral-row leverage of the physical pivot. Thus (5.1) becomes

`||p_Q||_infinity
 < sqrt(2) H_{2,q}(1-tau^2)^(-1/4)
   (|d| |det Lambda| ell)^(-1/4).`                                  (5.3)

Under the localized hypotheses `ell>1/2`, `|d|>=1/2`, `|det Lambda|>=1`, the last factor is `<sqrt(2)`. Exact rational parameter choices give:

1. If `mu<1/8`, take `tau=1/2,q=1`. Then
   `||p_Q||_infinity <16.492` on the localized exact-rank-three branch. The partner's earlier number for this branch was `<25.101`.
2. If `mu<=1/6`, take `tau=0.58,q=1.6`. The hypotheses in (2.5) hold because `sqrt(1/3)<0.58` and `2mu/(1-tau)<=0.793651<0.8=q/2`. Then
   `||p_Q||_infinity <38.408`, improving the partner's displayed `<74.376`.
3. If `mu<=0.18`, take `tau=0.6001,q=1.801`. Then
   `sqrt(2mu)<=0.6<0.6001` and `2mu/(1-tau)<=0.900226<0.9005=q/2`, giving
   `||p_Q||_infinity <75.879`.
   This covers the widened `mu<=0.18` branch from my preceding run with a stronger constant than the previous `<103` calculation.

These are actual applications of the named account03/B02 theorem, not restatements.

## 6. Relation to the freshest synthesis and what remains unpaid

A fresh account03/B19 synthesis published during this run proves the complete branch

`s_2(A-diag A)<=499/1000 => ||p_Q||_infinity<84`

and identifies the remaining full-target task as payment of the O0/O1/O2/O3 overlap structure when this off-diagonal spectral quantity is larger.

The present theorem supplies two new pieces for that exact task:

- **O1 converter:** one nonzero physical pivot plus leverage-compatible O1/Schur `E_2` mass is paid by (4.5), with no independence between square shift and residual;
- **higher-rank leverage-free converter:** one nonzero physical pivot plus Schur `E_3` mass is paid unconditionally by (3.13).

The first unpaid implication is now narrower: handle the residual cases where O1 mass is concentrated behind a near-zero physical pivot or every mass-carrying rank-two Schur cut is at the leverage endpoint, and simultaneously pay O2/O3 configurations without selecting a tiny fixed minor. The archived flat/Hadamard and singleton-plus-two-banks corrections show that reciprocal one-minor or universal rank-three-cut replacements are invalid. The zero/near-isotropic physical-pivot branch therefore remains genuinely structural.

No target-level counterexample and no counterexample to a universal full `||phi_Q||_1` estimate was found in this run. The stronger full-Fourier criterion remains open; the proved weighted integrated resource (3.9) is sufficient for the density branches above.

## 7. Exact computation and integrity notes

`check_constants.py` and `CHECK_OUTPUT.txt` in this run directory evaluate only the beta-function constants and the exact partner parameter inequalities. The output ends `STATUS=PASS`. These numerical checks are regression only; Sections 3--5 are analytic.

Source corrections consumed include: pointwise oscillatory decay false; no independence after rotation; conditional projection caps false; one fixed cross minor/rank-three cut is not universal; phase-Wiener absolute-value route false. No challenged premise is used.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data, email, paid calls, public release, permission changes, or remote workflows are present in this report.
