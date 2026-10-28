SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T07:45:55Z.
attacking: optimize the physical-row marginal threshold by splicing the D' determinant-entropy receiver with the marginal-free one-hub E2 promotion theorem, then test the sharpened constant on a dense rotated indefinite carrier.

# account01/B04 r30 — optimized row-cap splice for the physical E3 crossing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING CONSTANT IMPROVEMENT / FULL QFORM OPEN / INDEPENDENT REVIEW PENDING**  
Continuity: the paid branch below has a continuous `C_0(R)` density; full-target continuity remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target remains unchanged: independent ORIGINAL real coordinates with scalar densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, Gaussian, compact-support, connected-support, log-concavity, diagonal-basis, post-rotation independence, generic joint coarea, fiber-supremum, or law-uniform scalar pointwise quadratic-phase decay assumption is used.

## 1. Source-pinned inputs


The first analytic input is my earlier global row-cap theorem at

- `yspennstate/math-open-problems@d68771753f4b44672e307bb817409483a503eba0`
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260924T034618Z-account01-B04-QFORM-auto11-r28/REPORT.md`.

For a literal original-coordinate cross block `M=A[I,J]`, any supported row-triple law with all row marginals at most `h`, `1/2<=h<3/4`, gives through the owner-pinned D' theorem

`||p_Q||_infinity <= A(h) G^(-1/6)`,

where

`A(h)=6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1)`,                         (1.1)

and the proof supplies Fourier `L1`, hence `p_Q in C_0(R)`.

The second analytic input is the completed marginal-free one-hub projected-E2 theorem

- `QFORM-ONEHUB-E2-MARGINAL-GATE-REMOVAL-v1`
- `yspennstate/math-open-problems@585b5a3ca7e887e5cd16f45ea49056d548361dfb`
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T173320Z-auto11-heavyrowpromotion/REPORT.md`.

In its notation, with one original hub row `m` and projected residual two-volume `Z2>0`, the full ambient quadratic law has a continuous density and

`||p_Q||_infinity <= C_E2 (||m||^2 Z2)^(-1/6)`,                  (1.2)

`C_E2=3*2^(7/6)*exp(1/3)=9.39913188784886... .`                  (1.3)

Arbitrary same-bank curvature and affine terms are retained.

The designated partner result actually applied below is account02/B04 r20:

- handoff commit `math-research-brain@9c5dd9f36f322a2b4e040d25a97e7d07eb61dad3`;
- primary report `math-open-problems@db9f71028e300f49dd92b7273472dae6d824e992:proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/account02-B04-20260924T051847Z/REPORT.md`.

Its proved pair-anchored E3 theorem is

`||p_Q||_infinity <= 3*2^(5/6) W_ab^(-1/6)`                      (1.4)

whenever the pair-anchored third-volume `W_ab>0`; its proof is product-preserving and gives Fourier `L1`.

## 2. Canonical row-volume law and the exact heavy-row identity

Let the physical rows of `M` be `m_i`. Put

`z_S=det(M[S,:]M[S,:]^T)` for `|S|=3`,
`Z=sum_S z_S=e_3(MM^T)>0`,                                      (2.1)

and define the canonical row-volume law

`p_S=z_S/Z`,
`alpha_i=sum_(S contains i) p_S`.                                (2.2)

For this canonical law the determinant-entropy row currency is exactly

`G_row(p)=exp(H(p)+sum_S p_S log z_S)=Z`.                         (2.3)

Fix a physical row `a` with `alpha_a>0`. Then `m_a!=0`. Let `P_a` be orthogonal projection onto `span(m_a)` in the right-coordinate space, and let `C_a` have rows

`c_i=m_i(I-P_a)`, `i!=a`.                                        (2.4)

Define

`Z2(a)=e_2(C_a C_a^T)`.                                          (2.5)

### Exact identity

`boxed: ||m_a||^2 Z2(a)=alpha_a Z.`                              (2.6)

Indeed, for every distinct `i,j!=a`, Gram-Schmidt along `m_a` gives

`det Gram(m_a,m_i,m_j)
 =||m_a||^2 det Gram(c_i,c_j)`.                                  (2.7)

Summing (2.7) over all unordered pairs `{i,j}` gives the left side of (2.6), while the same sum is exactly the canonical mass of all row triples containing `a`, namely `alpha_a Z`.

This identity is the splice point: a row that is too heavy for D' automatically generates the exact one-hub projected-E2 currency needed by (1.2), with no local minor inversion.

## 3. Main theorem — optimized row-cap splice

### Theorem `QFORM-Z3-OPTIMIZED-ROWCAP-SPLICE-v1`

For every literal original-coordinate cross block `M=A[I,J]` with

`Z=e_3(MM^T)>0`,                                                  (3.1)

the full ambient quadratic law has a continuous `C_0(R)` density and

`boxed: ||p_Q||_infinity <= C_30 Z^(-1/6),}`                     (3.2)

where the completely explicit rational-threshold certificate

`h0=324/625=0.5184`                                               (3.3)

gives

`C_30 = 15625 sqrt(e)/(1737 sqrt(2))
      =10.487028558565074... .`                                  (3.4)

This improves the previously recorded marginal-free E3 constant

`C_old=3*2^(4/3)*exp(1/3)=10.550168831164775...`                  (3.5)

by `0.06314027259970...`, i.e. about `0.5985%`.

### Proof

There are two cases.

#### Case A: every canonical row marginal satisfies `alpha_i<=h0`

Use the canonical law (2.2) in the D' row-cap receiver. By (2.3), `G=Z`. Hence

`||p_Q||_infinity <= A(h0) Z^(-1/6)`.                            (3.6)

Now

`2h0=648/625`,
`3-4h0=579/625`,                                                  (3.7)

so

`A(h0)
 =6sqrt(e)*(625/648)^(1/2)*(625/579)
 =15625 sqrt(e)/(1737 sqrt(2))
 =10.487028558565074... .`                                       (3.8)

The D' proof gives Fourier `L1`, hence a `C_0` density.

#### Case B: some canonical row marginal satisfies `alpha_a>h0`

Use row `a` as a literal original hub, condition any original coordinates outside the chosen crossing partition, and retain all induced affine and same-bank quadratic terms. By (2.6),

`||m_a||^2 Z2(a)=alpha_a Z>h0 Z`.                                (3.9)

Apply the completed one-hub E2 theorem (1.2):

`||p_Q||_infinity
 <=C_E2 (alpha_a Z)^(-1/6)
 <C_E2 h0^(-1/6) Z^(-1/6)`.                                     (3.10)

Numerically,

`C_E2 h0^(-1/6)=10.486814313156756... < C_30`.                   (3.11)

The conditional densities are uniformly bounded `C_0` functions. Averaging over the conditioned original coordinates preserves continuity and vanishing at infinity by dominated convergence. Thus (3.2) follows in both cases. QED.

### Near-optimal threshold within this two-receiver splice

Because `A(h)` is increasing on `[1/2,3/4)` while `C_E2 h^(-1/6)` is decreasing, the best threshold for this exact two-receiver splice is the unique `h_*` satisfying

`A(h_*)=C_E2 h_*^(-1/6)`,                                       (3.12)

or equivalently

`(3-4h_*) h_*^(1/3)=2^(-2/3) e^(1/6)`.                           (3.13)

Numerically,

`h_*=0.518394440469914...`,
`C_*=10.486833057409717...`.                                     (3.14)

The rational value `h0=324/625` is used in the theorem statement so that the published constant (3.4) is a simple explicit certificate requiring no root-finding premise.

## 4. Disjoint third-compound corollary

Suppose a physical symmetric carrier `S` has disjoint third-compound mass

`Delta_3^disj(S)
 =sum_(|R|=|T|=3, R cap T=empty) det S[R,T]^2 >0`.                (4.1)

Randomly color physical coordinates into two labelled banks. A fixed ordered disjoint pair of triples lands across the cut with probability `2^-6`. Hence some literal original-coordinate cut `I|J` satisfies

`e_3(S[I,J]S[I,J]^T)>=Delta_3^disj(S)/64`.                       (4.2)

Applying Theorem (3.2) gives the continuous-density estimate

`boxed:
 ||p_Q||_infinity
 <=2 C_30 [Delta_3^disj(S)]^(-1/6)
 <20.9740571172 [Delta_3^disj(S)]^(-1/6).}`                      (4.3)

This is only a supporting branch: the bare three-large-eigenvalue hypothesis does not automatically force target-scale disjoint third-compound mass.

## 5. Dense genuinely rotated indefinite stress family

Reuse the fully dense family from r28, now tuned exactly to the new rational threshold. Let `H_8` be the Sylvester Hadamard matrix and

`U=H_8[:,0:4]/sqrt(8)`,                                          (5.1)

and let

`V=(1/15)
 [[14,-2,-3,-4],
  [-2,11,-6,-8],
  [-3,-6,6,-12],
  [-4,-8,-12,-1]]`,                                               (5.2)

so `V^T V=I_4`. For `y>0`, put `L=sqrt(y)` and

`R_y=[L e_1; L e_2; L e_3; U]`,
`M_y=R_y V^T`.                                                     (5.3)

Every physical entry of `M_y` is nonzero. Also

`M_y^T M_y=diag(y+1,y+1,y+1,1)`,                                 (5.4)

so its singular values are `sqrt(y+1)` three times and `1` once.

Define the fully dense symmetric matrix

`A_y=[[0,M_y],[M_y^T,0]] +10^(-3)(J_11 direct_sum J_4)`.          (5.5)

The same-bank perturbation has operator norm at most `0.011`. Thus for every `y>=1` the six eigenvalues inherited from the first three crossing singular values have modulus at least

`sqrt(y+1)-0.011 >=sqrt(2)-0.011>1`.                              (5.6)

Hence `A_y` is genuinely rotated, indefinite, fully dense, and satisfies the exact owner spectral target.

The exact row-triple volume face masses relative to the three heavy rows are

`W_empty=4`,
`W_a=3y` for each one-heavy face,
`W_ab=2y^2` for each two-heavy face,
`W_123=y^3`.                                                       (5.7)

Therefore

`Z(y)=e_3(M_yM_y^T)=4+9y+6y^2+y^3=(y+1)^2(y+4)`,                (5.8)

and each heavy canonical row marginal is

`alpha_H(y)=y(y+3)/[(y+1)(y+4)]`.                                (5.9)

Choose `y=y0` to make this marginal exactly `h0=324/625`. The equation is

`301 y0^2+255 y0-1296=0`,                                        (5.10)

so

`y0=(-255+sqrt(1625409))/602
   =1.69421144734834...`,
`L0=1.30161877957732... .`                                       (5.11)

Then the three heavy marginals equal `0.5184`, while by symmetry each of the eight light marginals equals

`[3-3(0.5184)]/8=0.1806`,                                       (5.12)

so the canonical row law lies exactly on the D' gate.

At this point

`Z(y0)=41.333001538086286...`,                                   (5.13)

and the new theorem gives

`boxed:
 ||p_(X^T A_y0 X)||_infinity
 <=5.639876923233456...,
 p_(X^T A_y0 X) in C_0(R).}`                                    (5.14)

The older generic E3 constant would give

`5.673833478645989...`.                                          (5.15)

Thus the new splice yields a strict quantitative improvement on an actual dense rotated indefinite target-valid matrix.

## 6. Designated account02/B04 partner applied to an actual inequality

Use the first two heavy rows of the same `M_y0`. Their pair-anchored third-volume is exactly

`W_12=2y0^2+y0^3=y0^2(y0+2)
     =10.603688798646596... .`                                   (6.1)

The completed account02/B04 r20 theorem (1.4) therefore applies to this same full ambient quadratic law and yields

`boxed:
 ||p_(X^T A_y0 X)||_infinity
 <=3*2^(5/6) W_12^(-1/6)
 =3.606368399164259... .}`                                       (6.2)

This is sharper on this deliberately pair-concentrated matrix. The point of Theorem 3.1 is different: it improves the **uniform marginal-free E3 compiler** without assuming a distinguished heavy pair. Equation (6.2) is an actual same-matrix application of the designated partner theorem, not merely a citation.

## 7. What remains open

The full conjecture is still open. This run improves the paid physical-crossing branch; it does not prove that every symmetric matrix with three eigenvalues of modulus at least one has a literal physical cut with target-scale `e_3`.

The first unpaid implication remains structural:

`QFORM-LOW-E3-TO-RANK2-HUBSTAR-OR-OTHER-PAID-ENDPOINT-v1`.

Starting only from the bare spectral hypothesis, if every useful literal cross block has small `e_3`, force a target-scale original-coordinate rank-at-most-two/hub-star/square-bank/fixed-pair endpoint, or another already-paid receiver, without deleting a small rough quadratic tail and without rotating the independent coordinates.

This report makes no full-solution claim and has not received the two independent end-to-end reviews required for a full candidate.
