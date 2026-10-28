SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T20:41:58Z.
attacking: the diffuse selected-three spectral-window survivor — turn complementary high-window leverage into a near-zero physical star plus two robust child directions, then recolor those three directions into a literal rank-three crossing.

# account01/B08 r35 — deletion rigidity and the dual two-child-plus-star half-cut

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: diffuse eigenvector case / exact structural identities  
Status: `PROVED SUPPORTING STRUCTURAL/ANALYTIC ROUTER + DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted QFORM conjecture remains OPEN. Full-target continuity remains OPEN. Continuity below is asserted only on the volume-stability paid branch.

No moments, bounded support, connected support, log-concavity, iid hypothesis, post-rotation independence, arbitrary-joint coarea bound, law-uniform pointwise quadratic-phase decay, or probabilistic deletion of a small coefficient matrix is used.

## 1. Exact deletion rigidity from three selected eigenvectors

Let `R` be an `n x 3` orthonormal frame of genuine eigenvectors,

    A R = R Lambda,       R^T R=I_3,       min_j |lambda_j| >= L.

Fix an ORIGINAL coordinate `i`, move it first, and write

    A = [ a    b^T ]
        [ b     C  ].

Let `p_i=||R_{i,*}||_2^2` be the selected-three leverage of that coordinate.

### Theorem 1 — `QFORM-DELETE1-TWOCHILD-RIGIDITY-v1`

If `p_i<1`, then

    boxed:  s_2(C) >= sqrt(1-p_i) L.                              (1.1)

More precisely,

    boxed:  s_3(C)^2 + ||b||_2^2 >= (1-p_i)L^2.                  (1.2)

#### Proof

Spectral calculus gives

    A^2 >= L^2 R R^T

in Loewner order, because every omitted spectral component of `A^2` is positive semidefinite. Taking the principal block after deleting coordinate `i` gives

    C^2 + b b^T = (A^2)_{-i,-i} >= L^2 R_{-i}R_{-i}^T.           (1.3)

The three nonzero eigenvalues of `R_{-i}R_{-i}^T` are those of

    R_{-i}^T R_{-i}=I_3-R_{i,*}^T R_{i,*},

namely `1,1,1-p_i`. Thus

    lambda_3(C^2+bb^T) >= (1-p_i)L^2.                            (1.4)

Since `bb^T` has rank one, Weyl with indices `(2,2)` gives

    lambda_3(C^2+bb^T) <= lambda_2(C^2)+lambda_2(bb^T)=s_2(C)^2,

which proves (1.1). Weyl with `(3,1)` gives

    lambda_3(C^2+bb^T) <= s_3(C)^2+||b||^2,

proving (1.2). QED.

This identity retains the entire complementary spectrum of `A`; no selected-rank-three truncation is substituted for the physical child block.

## 2. Complementary high-window leverage gives pivot-or-star currency

Let `P_3=RR^T` and let `P_H` be the full spectral projection onto `|lambda(A)|>=L/64`, so `P_3<=P_H`. Assume the selected three-frame is diffuse,

    max_i (P_3)_{ii} <= 1/48.                                    (2.1)

If the completed ridge-window gate fails,

    max_i (P_H)_{ii} > 1/32,                                    (2.2)

then for some coordinate `i`

    q_i := (P_H-P_3)_{ii} > 1/96.                               (2.3)

Because `P_H-P_3` is a spectral projection commuting with `A`,

    ||A e_i|| >= ||A(P_H-P_3)e_i||
               >= (L/64) sqrt(q_i)
               > kappa_0 L,                                    (2.4)

where

    kappa_0 = 1/(64 sqrt(96))
            = 0.0015947198846244651... .                        (2.5)

For `delta_0=kappa_0/2`, either

    |a| >= delta_0 L,                                           (2.6)

or, since `||Ae_i||^2=a^2+||b||^2`,

    ||b|| > beta_0 L,                                           (2.7)

with

    beta_0 = sqrt(kappa_0^2-delta_0^2)
           = sqrt(3)/(128 sqrt(96))
           = 0.0013810679320049757... .                         (2.8)

On (2.6), the completed all-sign scalar-pivot theorem applies directly because `s_3(A)>=L`:

    ||p_Q||_infinity <= C_*/sqrt(delta_0) * L^(-1)
                      < 4.928e10/L,                             (2.9)

where `C_*=1+44*10^(15/2)`. No continuity conclusion is imported from that theorem.

On the star branch (2.7), Theorem 1 and (2.1) give simultaneously

    s_2(C) >= sigma_0 L,
    sigma_0=sqrt(47/48)=0.9895285072531598... .                 (2.10)

Thus every unpaid failure of the full-window diffuse gate contains one literal physical star together with two robust child spectral directions.

## 3. Dual two-child-plus-star half-cut theorem

The next theorem turns exactly that geometry into a genuine literal rank-three crossing whenever the three directions are physically diffuse and transverse.

Let the top two singular/eigen directions of the symmetric child `C` be the orthonormal two-frame `U=[u_1,u_2]`, with signed eigenvalues `mu_1,mu_2` satisfying

    min(|mu_1|,|mu_2|) >= sigma L.                               (3.1)

Let

    v=b/||b||,
    d=dist(v,range U)>0,
    q=(I-UU^T)v/d,
    W=[q,U].                                                      (3.2)

Then `W^TW=I_3`. Put

    nu=max_j ||W_{j,*}||^2.                                      (3.3)

### Theorem 2 — `QFORM-DUAL-K2-STAR-HALFCUT-v1`

Assume

    ||b|| >= beta L,       nu<=1/48.                              (3.4)

Define

    kappa(beta,sigma,d)
      = beta sigma d / [2 sqrt(4 beta^2+sigma^2)].                (3.5)

If

    s_3(C) <= kappa(beta,sigma,d)L/16,                            (3.6)

then the full ambient quadratic form has a continuous `C_0` density and

    boxed: ||p_Q||_infinity < 23/[kappa(beta,sigma,d)L].         (3.7)

#### Proof

Apply the completed designated-partner account02/B08 r28 balanced-half-cut lemma to the actual three-frame `W`. It produces an ORIGINAL-coordinate split of the child bank,

    I=S disjoint_union T,

such that

    (1/4)I_3 <= W_S^T W_S, W_T^T W_T <= (3/4)I_3.               (3.8)

Let

    C_2=U diag(mu_1,mu_2)U^T

be the best signed rank-two spectral truncation of `C`, and form the literal crossing from `S` to the opposite bank `{i} union T`:

    M=[b_S, C[S,T]],
    M_0=[b_S, C_2[S,T]].                                        (3.9)

Write `z=W^T v=(d,a_1,a_2)^T`, `||z||=1`. Then

    M_0M_0^T=W_S K W_S^T,                                      (3.10)

where

    K=||b||^2 zz^T
      + diag(0,mu_1,mu_2) (U_T^T U_T)
        diag(0,mu_1,mu_2).                                      (3.11)

Here the diagonal matrices are understood in the `[q,U]` frame. By (3.8), for `x=(x_0,y)`,

    x^T K x
      >= beta^2 L^2 <z,x>^2 + (sigma^2 L^2/4)||y||^2.           (3.12)

The direction in the `U`-plane orthogonal to the `U`-component of `z` has eigenvalue at least `sigma^2L^2/4`. On the remaining two-dimensional plane, determinant-over-trace gives

    lambda_min(K)
      >= [beta^2 sigma^2 d^2/(4 beta^2+sigma^2)] L^2.            (3.13)

Since `W_S^TW_S>=I/4`, the three nonzero eigenvalues of `M_0M_0^T` are those of `K^(1/2)(W_S^TW_S)K^(1/2)`, hence

    s_3(M_0) >= (1/2)sqrt(lambda_min(K))
              >= kappa(beta,sigma,d)L.                           (3.14)

Because `d>0`, `K` is positive definite and `range(M_0)=range(W_S)`. Therefore every physical row leverage of `range(M_0)` is at most

    ||W_{j,*}||^2/lambda_min(W_S^TW_S)
      <=4nu<=1/12<1/2.                                          (3.15)

Finally

    M-M_0=[0,(C-C_2)[S,T]],
    ||M-M_0||op <= s_3(C).                                      (3.16)

Under (3.6), the completed literal-cross volume-stability theorem applies to the actual block `M`. It permits arbitrary internal terms on both physical banks, hence keeps `a`, `b_T`, `C[S,S]`, `C[T,T]`, every diagonal and every affine term. It gives (3.7) and continuity. QED.

The partner result is used at the decisive equation (3.8): its macroscopic original-coordinate half-cut is what allows the star plus two child directions to become a physical rank-three crossing without selecting a small scalar pivot.

## 4. Numerical specialization to the selected-three spectral-window survivor

In the branch from Section 2 take

    beta=beta_0=0.0013810679320049757...,
    sigma=sigma_0=sqrt(47/48),
    d>=1/2.

Then

    kappa_dual
      =0.00034526563789691794...,
    kappa_dual/16
      =2.157910236855737e-5.                                    (4.1)

Therefore, if the combined star-plus-top-two-child frame has leverage `nu<=1/48` and

    s_3(C) <= 2.157910236855737e-5 L,                            (4.2)

then

    boxed: ||p_Q||_infinity < 66615.376/L,                       (4.3)

with a continuous `C_0` representative.

Combining Sections 1--4 with the existing ridge-window receiver gives the following source-valid router for a selected diffuse three-frame:

- if the full `|lambda|>=L/64` spectral projection has leverage at most `1/32`, the existing ridge-window theorem pays continuously by `<64/L`;
- otherwise some high-window-heavy coordinate exists;
- if its diagonal is at least `delta_0 L`, the all-sign scalar-pivot theorem pays essentially bounded density by (2.9);
- otherwise it supplies `||b||>beta_0L` and `s_2(C)>=sigma_0L`;
- if additionally `d>=1/2`, `nu<=1/48`, and (4.2) holds, Theorem 2 pays continuously by (4.3).

Thus every survivor of this diffuse selected-three route now has at least one explicit obstruction:

    d<1/2,   or   nu>1/48,   or   s_3(C)>2.15791e-5 L,           (4.4)

in addition to the already separated non-diffuse selected-three case. These are literal coefficient/spectral objects; no random perturbation has been thrown away.

## 5. Remaining implication

The first B08 obligation after this run is

`QFORM-DUAL-K2-STAR-SURVIVOR-COMPILER-v1`:

> Pay the near-aligned star (`d<1/2`), heavy combined three-frame row (`nu>1/48`), or genuine third-child direction (`s_3(C)>2.15791e-5 L`) while retaining the full complementary spectrum and original-coordinate product provenance.

The full universal theorem is not claimed.

## 6. Source pins consumed

- designated partner half-cut/receiver: `math-open-problems@66582bd87d50634f3525a57c87acffdbde97aea1`, `account02/B08/20260923T153836Z-account02-B08-qform-r28/REPORT.md`;
- literal-cross volume stability: `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `interactive/20260923T002323Z-volume-stability/REPORT.md`;
- all-sign scalar pivot: current `interactive/20260923T192150Z-all-sign-scalar-pivot/REPORT.md`;
- previous B08 spectral-window/row router: `account01/B08/20260923T194115Z-account01-B08-qform-r34/REPORT.md`.

The live correction inbox was refreshed before this write. None of the refuted arbitrary-joint coarea, conditional-cap, post-rotation-independence, pointwise-decay, or small-random-tail shortcuts is used.
