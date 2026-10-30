SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T18:46:31Z.
attacking: the low-cross-rank strong-cut collar — switch from local singular-vector tubes to the global third-compound overlap decomposition, and pay the fully source-disjoint compound mass by an averaged physical-cut Fourier theorem.

# fleet01/B02 r34 — global disjoint third-compound Fourier reduction

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: Integrated Fourier estimate.
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN / GLOBAL FOURIER CRITERION OPEN_NOT_REFUTED`.
Continuity: proved on the new disjoint-compound branch because the full characteristic function is in `L1(R)`; unrestricted target continuity remains open.
Execution label: `WITHOUT_VERIFIED_BRAIN`.

No random variable is rotated. No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, pointwise van-der-Corput, arbitrary-joint coarea, fiber-supremum, or deletion-of-small-tail hypothesis is used.

## 1. Fresh sources and the completed partner result actually used


The designated partner actually used is fleet02/B02:

`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T170839Z-fleet02-B02-qform-auto11/REPORT.md`.

Its completed marginal-free physical-E3 theorem states: for every ORIGINAL-coordinate physical cross block `M=A[L,R]`, with disjoint coordinate banks `L,R` and

`Z=E3(M)=e3(M^T M)>0`,

the full ambient quadratic form satisfies

`||p_Q||_infinity <= 10.345084 Z^(-1/6)`,                       (1.1)

and

`integral_R |phi_Q(t)| dt <= 2*pi*10.345084 Z^(-1/6)`.          (1.2)

All same-bank curvature, outside couplings and affine terms are retained. In particular the density has a continuous representative vanishing at infinity. This is the analytic receiver applied below.

The newer checked grouped projected-crossing source was also read at

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its canonical projected-volume receivers remain relevant to the overlap classes isolated below, but I do not use any of their hypotheses unless they are actually verified.

## 2. Global third-compound mass and its overlap decomposition

For a real symmetric `n x n` matrix `A`, define for `k=0,1,2,3`

`C_k(A) = sum_{|S|=|T|=3, |S cap T|=k} det(A[S,T])^2`,          (2.1)

where the sum is over ordered pairs `(S,T)` of physical coordinate triples. Thus `C_0` is the total squared mass of completely disjoint physical `3 x 3` minors.

Because `A` is symmetric, `A^2=A A^T`. Cauchy--Binet on the third compound gives the exact identity

`boxed: e3(A^2)=C_0(A)+C_1(A)+C_2(A)+C_3(A).`                    (2.2)

If `A` has at least three eigenvalues of absolute value at least one, then

`e3(A^2)=sum_{i<j<l} lambda_i^2 lambda_j^2 lambda_l^2 >=1`,      (2.3)

since at least one summand uses three such eigenvalues. Hence

`boxed: max_{0<=k<=3} C_k(A) >=1/4.`                             (2.4)

This is a target-level, dimension-free four-way decomposition. It does not select a single minor; it keeps the entire compound mass.

## 3. Exact random-cut identity for the disjoint compound class

Let `J` be a uniformly random subset of `[n]`, obtained by assigning every physical coordinate independently to `J` or `K=J^c` with probability `1/2`. Put

`M_J=A[J,K]`.                                                     (3.1)

For every fixed ordered pair of disjoint triples `(S,T)`,

`P(S subset J, T subset K)=2^(-6)=1/64`.                         (3.2)

Cauchy--Binet for the rectangular cross block gives

`E3(M_J)
 = sum_{S subset J, |S|=3} sum_{T subset K, |T|=3}
     det(A[S,T])^2`.                                              (3.3)

Taking expectation in (3.3) and using (3.2) term by term yields the exact identity

`boxed: E_J E3(A[J,J^c]) = C_0(A)/64.`                           (3.4)

Consequently there exists one literal ORIGINAL-coordinate cut `(J,K)` such that

`boxed: E3(A[J,K]) >= C_0(A)/64.`                                (3.5)

No spectral rotation, coordinate shear, selected reciprocal minor, or probabilistic assumption on `X` enters (3.4). It is pure coefficient algebra plus a Bernoulli coloring of the physical coordinates.

The factor `1/64` is optimal for this simple two-bank coloring: for any fixed ordered disjoint triples, a product coloring putting a coordinate into the two banks with probabilities `p,1-p` captures that orientation with probability `p^3(1-p)^3`, maximized at `p=1/2` with value `1/64`.

## 4. Main theorem — `QFORM-GLOBAL-DISJOINT-COMPOUND-E3-L1-v1`

Under the exact QFORM input assumptions, define `C_0(A)` by (2.1). If `C_0(A)>0`, then the full ambient quadratic form has a continuous density in `C_0(R)` and

`boxed:
 ||p_Q||_infinity
 <= 20.690168 C_0(A)^(-1/6),`                                    (4.1)

and

`boxed:
 integral_R |phi_Q(t)| dt
 <= 130.000160 C_0(A)^(-1/6).`                                   (4.2)

### Proof

Choose the physical cut from (3.5) and let `Z=E3(A[J,K])`. The designated fleet02/B02 theorem (1.1)--(1.2) applies to this actual original-coordinate cross block, retaining the within-`J`, within-`K`, diagonal and outside terms of `Q`. Since

`Z >= C_0(A)/64`,                                                 (4.3)

and `64^(1/6)=2`,

`||p_Q||_infinity
 <=10.345084 Z^(-1/6)
 <=20.690168 C_0(A)^(-1/6)`.                                     (4.4)

Similarly,

`integral |phi_Q|
 <=2*pi*10.345084 Z^(-1/6)
 <=2*pi*20.690168 C_0(A)^(-1/6)
 <130.000160 C_0(A)^(-1/6)`.                                    (4.5)

The partner theorem supplies genuine `phi_Q in L1`, so Fourier inversion yields a continuous representative vanishing at infinity. QED.

This is the required equation-level use of fleet02/B02: its physical-E3 theorem is fed the new exact inequality `E3(A[J,K])>=C_0(A)/64`.

## 5. A compact target-level quarter reduction

Combining (2.4) with Theorem 4 gives the following exhaustive statement.

### Corollary — `QFORM-COMPOUND-OVERLAP-QUARTER-REDUCTION-v1`

Every target matrix satisfies at least one of:

1. `C_0(A)>=1/4`, in which case

   `boxed: ||p_Q||_infinity <26.067979`,                          (5.1)

   `boxed: integral_R |phi_Q(t)|dt <163.789938`,                 (5.2)

   and the density is continuous and vanishes at infinity;

2. `C_1(A)>=1/4`;
3. `C_2(A)>=1/4`;
4. `C_3(A)>=1/4`.

Indeed, if the first alternative fails, (2.2)--(2.4) force one of the three overlap classes to carry at least `1/4` of absolute third-compound mass.

This reduces the full target to **three explicit aggregate overlap receivers**. It is stronger and cleaner than asking for a uniformly good single physical minor, which is known to be an invalid general reduction.

The geometric meaning is precise. `C_0` is the part of the third compound that can be placed into two disjoint independent source-coordinate banks and therefore consumed immediately by the marginal-free cross-E3 Fourier theorem. `C_1,C_2,C_3` measure exactly one, two or three repeated physical coordinates between the row and column triples. Those repeated source coordinates are where the two-bank Plancherel proof cannot simply declare the two banks independent.

## 6. Relation to the current low-cross-rank strong-cut debt

The current fleet04/B02 / fleet02/B02 strong-cut chain produces a physical cross block with fixed Frobenius energy, and the marginal-free E3 theorem pays it unless that particular block is near rank one or near rank two. The new theorem changes viewpoint: instead of asking that one cut to carry third volume, it averages **all physical cuts simultaneously** through the global disjoint compound mass `C_0(A)`.

Thus every target state with `C_0(A)>=1/4` is paid immediately, including states for which a previously selected strong cut is individually close to rank one or two. What remains is not merely 'low rank on one cut'; it is the invariant statement that a positive amount of the global third compound is forced into the overlap classes `C_1,C_2,C_3`.

This is a genuine mechanism change after the preceding local-volume runs: the new currency is the global overlap decomposition of `wedge^3 A`, not a chosen singular-vector tube or one local Schur pivot.

## 7. Why this does not yet prove the full theorem

There is no valid implication in the current source saying that one of `C_1,C_2,C_3>=1/4` automatically yields a uniformly conditioned physical principal block or a good reciprocal minor. Such an inference would run directly into the live fixed-good-minor/cross-minor corrections.

The three remaining classes have distinct analytic meanings:

- `C_1`: one repeated physical source coordinate; this is the natural one-hub / quadratic-hub overlap class;
- `C_2`: two repeated physical source coordinates; this is the natural two-hub / pair-Schur overlap class;
- `C_3`: principal `3 x 3` determinant mass, potentially spread over many triples.

The checked grouped-crossing theorem permits arbitrary internal hub functions **after** one has built a source-valid grouped packet with enough crossing currency. The missing step is to aggregate an entire overlap class before paying any reciprocal local minor, and to retain the repeated coordinate's own quadratic role rather than duplicating it as an independent row/column variable.

Accordingly the first unpaid implication is now

`QFORM-OVERLAP-COMPOUND-MASS-TO-INTEGRATED-RECEIVER-v1`:

> If `C_k(A)>=1/4` for one `k in {1,2,3}`, prove a universal unweighted Fourier-L1 bound (or a direct bounded-density estimate) by a product-preserving k-hub / principal-compound argument, without selecting a single minor and without duplicating a repeated physical coordinate.

A solution of these three overlap receivers, together with Section 5, would close the exact full target. This run does **not** prove them.

## 8. Failed low-rank shortcut retained

I also tested the tempting model 'one rank-one bilinear smoothing resource plus one independent square' as a way to pay the near-rank-one strong-cut collar. The elementary product-density representation

`p_(UV)(w)=integral f_U(x) f_V(w/x) dx/|x|`                       (8.1)

shows why this does not automatically give the needed Fourier exponent under arbitrary fragmented cap-one laws. Near zero one obtains only the universal logarithmic envelope

`p_(UV)(w) <= 2+2 log(1/|w|)` for `0<|w|<=1`,                    (8.2)

while a crude large-`|w|` split gives only `2/sqrt(|w|)`. These bounds do not by themselves produce the conjugate Fourier integrability needed to combine a rank-one bilinear factor with one arbitrary square factor into `L1_t`. More importantly, the actual target tail is coupled and cannot be deleted or assumed independent. I therefore do not promote this model calculation to a target theorem.

The global compound decomposition in Sections 2--5 avoids that dead end and identifies the exact source-overlap debt instead.

## 9. Status

New proved support:

- exact global identity `E_cut E3(A[J,J^c])=C_0(A)/64`;
- target-valid Fourier-L1 theorem `||p_Q||_infinity<=20.690168 C_0(A)^(-1/6)`;
- target-level four-way compound reduction in which the `C_0>=1/4` branch is completely paid with density `<26.067979` and `integral|phi|<163.789938`.

Unproved:

- the three aggregate overlap receivers `C_1,C_2,C_3`;
- a universal target-wide `integral |phi_Q|` constant;
- the unrestricted universal bounded-density theorem;
- unrestricted continuity.

No target-valid counterexample to the stronger universal integrated-Fourier criterion was found, so that criterion remains `OPEN_NOT_REFUTED`.

MODEL: GPT-5.6 Sol.
THINKING LEVEL: UNKNOWN / not exposed; maximum supported was requested by owner control.
THINKING USAGE: reasoning tokens NOT_EXPOSED; provider thinking time NOT_EXPOSED; coverage unavailable.
