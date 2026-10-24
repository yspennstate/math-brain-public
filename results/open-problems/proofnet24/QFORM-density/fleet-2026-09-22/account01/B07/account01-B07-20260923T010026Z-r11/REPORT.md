SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T01:00:26Z.
attacking: the q=0 bi-anchor determinant packet — an exact anchored exterior decomposition and a paired 3x3/2x2 Brascamp-Lieb receiver that avoids selecting one tiny minor.

# account01/B07 — anchored third-wedge decomposition and paired-volume receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** coordinate minor selection  
**Run:** `account01-B07-20260923T010026Z-r11`  
**Outcome:** **ESSENTIAL_STEP_APPLIED / SUPPORTING_LEMMAS_PROVED; FULL QFORM OPEN**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source boundary

The target remains: for every dimension, independent real original-coordinate inputs whose one-dimensional densities are at most one, and every real symmetric matrix A with at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of X^T A X, or give a valid counterexample. No moments, support bounds, log-concavity, iid assumption, or independence after spectral rotation is used below. Continuity is recorded separately and is not inferred from essential boundedness.

Fresh owner control at publication remains revision `2026-09-22.15`, QFORM-only. The live correction ledger was reread. In particular, nothing below uses the refuted arbitrary-joint rank-three coarea bound, the false positive conditional-density-moment gate, pointwise law-uniform stationary phase, fiber suprema, or a claim that one physical minor is uniformly large.

Completed sources actually consumed:

1. **Designated partner account02/B07**, `QFORM-Q0-DIFFUSE-OR-BIANCHOR-v1`, source `yspennstate/math-open-problems@edccaf86c8d51e96d800658b8efafe12fd443508`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T003127Z-account02-B07-r11/REPORT.md`. For a q=0 determinant packet of mass P>=1/5184, either the full density is already bounded by 106.921 via the volume-weighted Fourier theorem, or there are fixed disjoint physical row/column anchors whose determinant-weighted subpacket has mass >P/3>=1/15552. The same report proves the bounded-coordinate-core receiver and gives a target-valid diffuse block family showing that bounded-cardinality core extraction is not universally available.
2. `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Theorem D/D': product-preserving decoupling plus Brascamp-Lieb, with the exact determinant expansion and L^p characteristic-function lemma used below.
3. `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, path `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`: the full conjecture reduces, for any fixed tau in (0,1], to its no-tau-pivot class N3(tau), where |A_ii|<tau and every physical 2x2 principal determinant has magnitude <tau. In that class |A_ij|<sqrt(2 tau)<=sqrt2.

## 2. Compact conditional end-to-end argument and first missing implication

On the q=0 overlap branch, the designated partner gives the following exact alternative:

- either the full form is already paid by `||p_Q||_infinity<=106.921`;
- or there are fixed disjoint physical anchors i_0,j_0 for which the anchored third-minor packet has mass >1/15552.

The first missing implication is therefore not to choose one of those third minors. It is to spend their **aggregate anchored mass** while preserving the original product law.

This report gives two exact receivers.

1. The entire anchored third-minor array is one exterior operator

   `T = b wedge^2 C - L_c C i_r`,

   so constant anchored mass forces either an edge-times-second-compound resource or a two-star-times-transverse-core resource, both dimension-free.

2. When the anchored array correlates with the edge-times-second-compound term, a new paired 3x3/2x2 Brascamp-Lieb argument pays the branch whenever one residual side has paired-volume marginals <=9/16. In the N3 class this gives a continuous density bound `<223`. If both residual sides are heavy, a second row anchor and a second column anchor carry a constant paired-volume packet. Thus the unresolved branch is reduced to a sharply specified four-anchor packet or the star-star-transverse resource.

This is aggregate-before-inversion throughout; no reciprocal individual minor appears.

## 3. Exact anchored exterior decomposition

Let B be any real physical cross block with fixed row anchor i_0 and fixed column anchor j_0. After ordering those anchors first, write

    B = [ b   r^T ]
        [ c    C  ],                                             (3.1)

where r is indexed by the remaining columns, c by the remaining rows, and C by the remaining rows and columns.

For two-element residual row and column sets K,L define

    t_{K,L} = det B[{i_0} union K, {j_0} union L].                (3.2)

Let `i_r : wedge^2 R^n -> R^n` denote contraction by r,

    i_r(x wedge y)=<r,x>y-<r,y>x,                                (3.3)

and let `L_c(v)=c wedge v`. Regard C as a linear map from residual column space to residual row space.

### Theorem 3.1 — `QFORM-ANCHORED-THIRD-WEDGE-DECOMPOSITION-v1`

The coefficient array `(t_{K,L})` is exactly the exterior operator

    T = b wedge^2 C - L_c C i_r.                                 (3.4)

Consequently the full anchored third-minor mass is

    M_00(B):=sum_{|K|=|L|=2} t_{K,L}^2
            = ||b wedge^2 C-L_c C i_r||_HS^2.                   (3.5)

Moreover

    ||b wedge^2 C||_HS^2 = b^2 E_2(C),                           (3.6)

where `E_2(C)=e_2(CC^T)=sum_{|K|=|L|=2}det(C[K,L])^2`, and

    ||L_c C i_r||_HS^2
      = ||r||_2^2 ||c||_2^2 ||P_{c^perp} C P_{r^perp}||_F^2.     (3.7)

Here the last term is interpreted as zero when r=0 or c=0.

If b is nonzero, (3.4) is equivalently the exact Schur exterior identity

    M_00(B)=b^2 E_2(C-c r^T/b).                                  (3.8)

### Proof

For K={k_1,k_2}, L={l_1,l_2}, expansion of the anchored 3x3 determinant along its first row gives

`t_{K,L}=b det C[K,L]
 -c_{k_1}(r_{l_1}C_{k_2l_2}-r_{l_2}C_{k_2l_1})
 +c_{k_2}(r_{l_1}C_{k_1l_2}-r_{l_2}C_{k_1l_1}).`

This is exactly the `(K,L)` coefficient of `b wedge^2 C-L_c C i_r`, proving (3.4)-(3.5). Equation (3.6) is Cauchy-Binet for the second compound.

For (3.7), use orthogonal coordinates only inside this deterministic Hilbert-Schmidt calculation, not on the random inputs. Take `r=||r||e_1`. Contraction kills `wedge^2(r^perp)` and sends `e_1 wedge e_j` to `||r||e_j`. Also

    ||c wedge v||^2=||c||^2 ||P_{c^perp}v||^2.

Summing over an orthonormal basis `e_1 wedge e_j`, j>=2, gives exactly (3.7). Finally `wedge^2(C-c r^T/b)` expands to `wedge^2 C-b^{-1}L_c C i_r`; the rank-one term has zero second exterior power, proving (3.8). QED.

### Corollary 3.2 — a stable dimension-free dichotomy, including b=0

Put

    U=b wedge^2 C,   V=L_c C i_r,   T=U-V.

Since `||T||^2<=2||U||^2+2||V||^2`, whenever `M_00(B)>=delta` one has

    b^2 E_2(C) >= delta/4                                       (3.9)

or

    ||r||^2||c||^2||P_{c^perp}CP_{r^perp}||_F^2 >= delta/4.     (3.10)

At the singular mutual-edge endpoint b=0 there is no loss at all:

    M_00(B)
      =||r||^2||c||^2||P_{c^perp}CP_{r^perp}||_F^2.             (3.11)

Thus zero mutual edge does not destroy the anchored packet; it converts it exactly into a two-star-times-transverse-core bank.

## 4. A sharper correlation dichotomy

The identity `T=U-V` gives

    M_00=<T,U>-<T,V>.                                           (4.1)

Hence at least one of

    |<T,U>|>=M_00/2,    |<T,V>|>=M_00/2                         (4.2)

holds.

The second case immediately implies (by Cauchy-Schwarz)

    ||r||^2||c||^2||P_{c^perp}CP_{r^perp}||_F^2
       =||V||^2 >= M_00/4.                                      (4.3)

The first case is stronger than (3.9). Writing

    d_{K,L}=det C[K,L],
    Z_pair:=sum_{K,L}|t_{K,L}d_{K,L}|,                           (4.4)

we have, whenever b!=0,

    Z_pair >= |sum t_{K,L}d_{K,L}|
           = |<T,U>|/|b|
           >= M_00/(2|b|).                                      (4.5)

The quantity `Z_pair` is exactly the one paid by the next theorem.

## 5. Paired 3x3/2x2 Brascamp-Lieb receiver

The key analytic observation is that pairing an anchored 3x3 determinant with the residual 2x2 determinant on the same K,L moves **half an exponent** from the fixed heavy row to the fixed heavy column. The effective row order becomes `5/2`, which is still enough for an integrable `|t|^{-5/4}` characteristic-function envelope.

For `Z_pair>0`, normalize

    w_{K,L}=|t_{K,L}d_{K,L}|/Z_pair.                             (5.1)

Let the residual inclusion marginals be

    alpha_k=sum_{K contains k,L} w_{K,L},
    beta_l =sum_{K,L contains l} w_{K,L}.                        (5.2)

Then `sum alpha_k=sum beta_l=2`.

### Theorem 5.1 — `QFORM-BIANCHOR-PAIRED-23-BL-v1`

Assume for one orientation that

    max_k alpha_k <= h,        1/2 <= h < 5/8.                  (5.3)

Then the full ambient quadratic-affine form, retaining arbitrary same-side blocks, outside couplings, additional eigenvalues and signs, has a **continuous** density satisfying

    ||p_Q||_infinity
      <= [10 e^(2/5) 2^(-1/10) (2h)^(-1/2)/(5-8h)]
          Z_pair^(-1/5).                                        (5.4)

The same conclusion holds if (5.3) holds for the column marginals beta, by transposing the physical cross block.

At the convenient threshold h=9/16,

    ||p_Q||_infinity
       <= (40/3)(2e)^(2/5) Z_pair^(-1/5).                       (5.5)

### Proof

Condition on every original coordinate outside the two physical banks I,J. Decoupling the J bank exactly as in Theorem D gives

    |phi(t)|^2
      <= int prod_{i in I}|psi_i(2t <B_i,w>)|
             prod_{j in J}g_j(w_j) dw,                           (5.6)

where the `g_j` are independent difference densities, each bounded by one and of mass one. Same-side quadratic terms and arbitrary affine terms disappear from this decoupled inequality exactly as in the source theorem.

Use Brascamp-Lieb exponents

    c_{i_0}=1/2,       c_k=alpha_k,
    d_{j_0}=1/2,       d_l=1-beta_l.                             (5.7)

They satisfy the scaling identity because the row exponents sum to `1/2+2=5/2`, while the column exponents sum to `|J|-5/2`.

For positive Gaussian parameters write the determinant in the standard diagonal-plus-PSD form. Its Cauchy-Binet expansion contains, for every K,L, both

`t_{K,L}^2 d_{i_0} prod_{k in K}d_k prod_{j notin {j_0} union L}e_j`

and

`d_{K,L}^2 prod_{k in K}d_k e_{j_0} prod_{j notin {j_0} union L}e_j`.

Their sum is at least twice their geometric mean. Summing and applying weighted AM-GM with (5.1) yields the exact Gaussian determinant lower bound

    det(E+B^TDB)
      >=2 Z_pair d_{i_0}^{1/2}e_{j_0}^{1/2}
         prod_k d_k^{alpha_k}
         prod_{l!=j_0} e_l^{1-beta_l}.                           (5.8)

Therefore the Brascamp-Lieb constant is at most `(2Z_pair)^(-1/2)` times the usual exponent factors.

Let `F` denote the product of characteristic-function factors in (5.6). For `q>=1`, `0<=F<=1` gives `E F <=(E F^q)^(1/q)`. Take `q=2h`. Because every row exponent in (5.7) is at most h, the Fourier exponent `q/c_i` is at least two. The source L^p lemma gives

    int |psi_i(2ts)|^(q/c_i) ds
       <= (2pi/|t|) sqrt(c_i/q).                                (5.9)

The row exponent factors in the BL constant cancel. Their total is 5/2, hence a factor `q^(-5/4)|t|^(-5/2)`. On the column side `g_j<=1`, `int g_j=1`; the fixed `d_{j_0}=1/2` contributes `2^(1/4)`, and

    prod_{l!=j_0}(1-beta_l)^(-(1-beta_l)/2) <=e

because `sum beta_l=2`. Thus

    E F^q
      <= e 2^(-1/4)(2pi)^(5/2) Z_pair^(-1/2)
         q^(-5/4)|t|^(-5/2).                                   (5.10)

Consequently

    |phi(t)| <= min(1,
      A^(1/(2q)) q^(-5/(8q)) |t|^(-5/(4q))),                   (5.11)

with `A=e 2^(-1/4)(2pi)^(5/2)Z_pair^(-1/2)`. Since `q=2h<5/4`, the power `5/(4q)` is greater than one. Integrating (5.11) over the real line and dividing by `2pi` gives exactly (5.4). Fourier inversion also gives a continuous density vanishing at infinity. QED.

## 6. Actual application of the designated partner result

Apply account02/B07's completed `QFORM-Q0-DIFFUSE-OR-BIANCHOR-v1` to the q=0 packet.

If its light-marginal alternative holds, the full form is already paid by `106.921` and there is nothing further to select.

Otherwise it produces fixed physical anchors with determinant-weighted q=0 subpacket mass

    >1/15552.                                                    (6.1)

The full anchored mass (3.5) dominates that subpacket, so set

    delta_0=1/15552,       M_00>delta_0.                         (6.2)

The new correlation dichotomy (4.2) now gives the following **actual inequality**.

### Edge-correlated branch

If `|<T,U>|>=M_00/2`, then b is nonzero and

    Z_pair >= M_00/(2|b|).                                      (6.3)

Inside the current no-pivot reduction N3(tau), tau<=1, the exact 2x2 principal-determinant condition implies

    b^2 < tau^2+tau <=2,                                        (6.4)

so

    Z_pair >1/(31104 sqrt2).                                    (6.5)

If either residual paired-volume marginal family is at most `9/16`, Theorem 5.1 gives the explicit continuous density bound

    ||p_Q||_infinity
       < (40/3)(2e)^(2/5)(31104 sqrt2)^(1/5)
       =222.7074656782... <223.                                  (6.6)

This is a genuinely new paid subbranch: it begins from the partner's fixed bi-anchor aggregate packet and never chooses one residual minor.

If neither orientation is `9/16`-light, choose residual row/column coordinates k_*,l_* with

    alpha_{k_*}>9/16,       beta_{l_*}>9/16.

Under the **same paired determinant law** (5.1), union bound gives

    P_w(k_* in K and l_* in L)>1/8.                              (6.7)

Hence a second row anchor and a second column anchor carry the constant paired-volume packet

    sum_{K contains k_*,L contains l_*}
      |t_{K,L} det C[K,L]|
       > Z_pair/8
       >1/(248832 sqrt2).                                       (6.8)

This is a four-anchor packet with only one residual row and one residual column left in each term. Again, no single minor is inverted.

### Transverse-correlated branch

If instead `|<T,V>|>=M_00/2`, then (4.3) yields

    ||r||^2||c||^2||P_{c^perp}CP_{r^perp}||_F^2
       >1/62208.                                                 (6.9)

In particular the singular mutual-edge endpoint b=0 lands here automatically, with the stronger exact identity (3.11).

Thus the partner's previously unpaid bi-anchor alternative is now reduced to two explicit dimension-free currencies: the four-anchor paired `3x3/2x2` packet (6.8), or the two-star-times-transverse-core bank (6.9). The paired-light part is already paid with continuous density `<223` in N3.

## 7. Why this does not silently solve more than proved

The full QFORM conjecture is still OPEN.

- The q=0 packet is only one of the overlap branches in the global third-compound coloring; q=1,2,3 have their own shared-coordinate/Schur obligations.
- In the edge-correlated q=0 branch, (6.6) pays only the paired-marginal-light state. The four-anchor packet (6.8) still needs a product-preserving receiver.
- The transverse branch (6.9) is a strong aggregate geometric resource, but it is not by itself a density theorem. It shares physical banks and cannot be replaced by a fictitious independent rank-three projection.
- Account02/B07's zero-self random-shift theorem remains useful at exact zero diagonal, but nonzero self-curvature can square-collapse; I do not extend that theorem here.
- Continuity is proved on the paired-BL branch (Theorem 5.1/eq. 6.6), not globally.

## 8. First surviving implication

The next precise target is

**`QFORM-BIANCHOR-FOURANCHOR-OR-TRANSVERSE-PAYMENT-v1`.** In the N3 no-pivot class, prove a universal full-form density/half-Riesz estimate from either

1. the four-anchor paired volume (6.8), or
2. the transverse resource (6.9),

while retaining arbitrary same-side curvature, outside couplings, signs and additional eigenvalues.

A promising mechanism is to continue the same determinant-order interpolation: the four-anchor packet has one residual row/column left, whereas the transverse branch has the exact contraction factorization `L_c C i_r`. Any valid continuation must aggregate before reciprocal selection and must survive the partner's diffuse block and checkerboard stress families.

## 9. Exact finite verification

I checked (3.4)-(4.2) on exact rational matrices by direct determinant expansion and separately on random integer/real blocks of several rectangular sizes. For one exact sample

    b=2, r=(1,-2,3), c=(2,1,-1),
    C=[[1,0,2],[-1,3,1],[2,1,-2]],

one obtains

    M_00=642,  ||U||^2=772,  ||V||^2=994,
    <T,U>=210, <T,V>=-432,

and indeed `<T,U>-<T,V>=642=M_00`, with the transverse correlation branch active. These finite checks corroborate the algebra; the universal statements above are proved symbolically and do not rely on numerical sampling.

## 10. Honest status

**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_LEMMAS_PROVED`.  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** PROVED only on Theorem 5.1's paired-volume branch; OPEN for the unrestricted target.  
**Native brain:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write is not claimed as native learned-memory ingestion.
