SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-24T05:20:52Z.
attacking: strengthen the global spectral-window Fourier exit to a 1/18 window, use its failure to force a larger literal physical hub, and feed that stronger hub into the live rank-two carrier with the fleet02/B02 physical-E3 receiver.

# fleet01/B02 — 1/18 spectral-window Fourier exit and 1/222 physical-hub funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Regularity: continuous `C_0` density on the Fourier-L1 branches below; the scalar-pivot density payment is only essential boundedness.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The exact target remains: independent ORIGINAL real coordinates with one-dimensional probability densities at most one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moments, compact/connected support, iid assumption, post-rotation independence, conditional projection-density cap, arbitrary-joint coarea, law-uniform pointwise quadratic-phase decay, or deletion of a nonzero coefficient tail is used.

## 1. Fresh sources and correction boundary


The parametric spectral-window theorem used and re-specialized below is the completed fleet03/B02 r47 report:

`yspennstate/math-open-problems@fbbacb396165d3e3a41304a73ff2331601e6ee05` (master content read during this run),
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260924T045848Z-fleet03-B02-qform-r47/REPORT.md`.

Its source theorem is the free-regularizer ridge/MSS argument at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

The completed designated partner theorem actually applied at an equation in Section 4 is fleet02/B02's marginal-free physical-third-volume Fourier theorem:

`yspennstate/math-open-problems@3fccd9b82b456e198758e5839be364b4b0ec5024`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T170839Z-fleet02-B02-qform-auto11/REPORT.md`.

For every literal ORIGINAL-coordinate physical cross block `B`, with `Z=E3(B)>0`, it proves

`||p_Q||_infinity <= C3 Z^(-1/6)`,
`integral_R |phi_Q(t)| dt <= 2*pi*C3 Z^(-1/6)`,
`C3=10.345083232147514...`,                                      (1.1)

and the density is continuous and vanishes at infinity.

The target-level scalar-pivot bounded-density theorem used in Section 3 is fleet03/B01:

`yspennstate/math-open-problems@28cbe14c4381d5f1b58145b29bbcc160b4d2ea5c`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T233049Z-auto11/REPORT.md`.

Under `s3(A)>=1`, any literal `a=A_ii!=0` gives

`||p_Q||_infinity <137 |a|^(-1/2)`.                              (1.2)

Continuity is not asserted by (1.2).

## 2. New theorem: `QFORM-1OVER18-SPECTRAL-WINDOW-L1-v1`

For `eta in (0,1)`, let

`P_eta = 1_{|A|>=eta}`                                           (2.1)

be the coefficient spectral projection. The parametric ridge/MSS theorem says that if

`max_i (P_eta)_ii <= eps`,                                       (2.2)

put

`delta = 1/2-eps-sqrt(2 eps)`,
`sigma = delta-eta`.                                             (2.3)

If `sigma>0` and

`( sqrt(eps/delta) + sqrt(6)*eta/sigma )^2 <1/2`,                (2.4)

then the full ambient law, retaining every smaller spectral direction, has

`||p_Q||_infinity <= 9 sqrt(3e)/(2 sigma)`,
`integral_R |phi_Q(t)|dt <=9 pi sqrt(3e)/sigma`,                 (2.5)

with a continuous `C_0` density.

I now take the stronger window

`boxed: eta=1/18, eps=1/76.`                                     (2.6)

Then

`delta=37/76-1/sqrt(38)=0.324620684132395...`,
`sigma=295/684-1/sqrt(38)=0.269065128576839...`.                 (2.7)

The leverage inequality (2.4) is very close to its endpoint, so here is an exact rational certificate rather than a floating-point assertion.

First,

`1/sqrt(38) < 162222/10^6`,                                     (2.8)

because

`162222^2*38 -10^12 = 7,136,792 >0`.

Hence

`delta > 37/76-162222/10^6`.                                    (2.9)

Direct rational comparison then gives

`sqrt((1/76)/delta) <201329/10^6`;                              (2.10)

the squared-margin certificate is

`(201329/10^6)^2 -(1/76)/(37/76-162222/10^6)
 =483350323731 / 3083891000000000000 >0`.

Also

`sqrt(6)<244949/100000`,                                        (2.11)

because `244949^2-6*100000^2=12601>0`. Using the same lower bound for `sigma=delta-1/18` gives

`sqrt(6)*(1/18)/sigma <505763/10^6`;                            (2.12)

the rational margin is

`505763/10^6 -(244949/100000)*(1/18)/(37/76-162222/10^6-1/18)
 =9924497/23005019000000 >0`.

Therefore the left side before squaring in (2.4) is less than

`(201329+505763)/10^6 =707092/10^6`,                             (2.13)

and

`1/2 -(707092/10^6)^2
 =1306471/62500000000 >0`.                                      (2.14)

Thus (2.4) holds rigorously.

### Consequence

If

`boxed: max_i (P_(1/18))_ii <=1/76,`                             (2.15)

then

`boxed: ||p_Q||_infinity <47.760,`                               (2.16)

`boxed: integral_R |phi_Q(t)|dt <300.084,`                       (2.17)

and the density has a continuous `C_0` representative.

This raises the completed `1/19` window from the preceding r47 source to `1/18`. The proof still keeps every eigenvalue below the cutoff in the exact quadratic phase; it does not truncate the random output.

## 3. Failure of the window gives a cleaner global `1/222` physical hub

Assume (2.15) fails. Choose an ORIGINAL coordinate `i` with

`(P_(1/18))_ii>1/76`.                                            (3.1)

Then exactly

`||A e_i||_2^2=(A^2)_ii
 >=(1/18)^2 (P_(1/18))_ii
 >1/(18^2*76)=1/24624.`                                         (3.2)

But

`||Ae_i||_2^2=A_ii^2+||A[i,i^c]||_2^2`.                         (3.3)

If both terms on the right had size at most `1/222`, then

`||Ae_i||_2^2 <=2/222^2=1/24642 <1/24624`,                      (3.4)

a contradiction. Therefore every target matrix obeys the exhaustive dimension-free dichotomy

`boxed:
 either max_i(P_(1/18))_ii<=1/76 and (2.16)-(2.17) hold,
 or some original coordinate i satisfies
 |A_ii|>1/222 OR ||A[i,i^c]||_2>1/222.
}`                                                               (3.5)

The exact nonsimplified hub scale from (3.2) is `1/(18 sqrt(152))=0.00450615...`; the clean `1/222` scale in (3.5) is slightly weaker and completely rational.

### Pay the diagonal alternative at the owner-theorem level

If

`|A_ii|>1/222`,                                                  (3.6)

then the scalar-pivot theorem (1.2) gives

`boxed: ||p_Q||_infinity <137 sqrt(222)<2041.255.`               (3.7)

This is essential boundedness; no continuity claim is imported from (1.2).

The scalar-chirp `L^3` theorem from the preceding fleet01/B02 run also gives the independent integrated-frequency fact

`||phi_Q||_3^3 <=32*pi/|A_ii|`,

hence on (3.6)

`boxed: ||phi_Q||_3 <(32*pi*222)^(1/3)<28.155.`                  (3.8)

Thus after the complete spectral-window and scalar-pivot exits, a still-unpaid target instance can be studied under the concrete source-coordinate conditions

`max_j |A_jj|<1/222`,
`||A[i,i^c]||_2>1/222` for some physical i.                      (3.9)

This is a global reduction, not a claim that one heavy row alone is already enough; the live correction against one-heavy-row square absorption remains binding.

## 4. Equation-level application of the designated fleet02/B02 receiver

Now feed the stronger global hub into the currently propagated robust near-rank-two full-cut packet. Let

`N=A[L,R]`, `L disjoint R`, `L union R=[n]`,                     (4.1)

be the live literal full cut whose two leading squared singular values obey

`x1*x2 > kappa :=247/576`.                                      (4.2)

Suppose the hub coordinate from (3.9) lies in `L` (the right-bank argument is the transpose). Let `u1,u2` and `v1,v2` be the top-two coefficient singular vectors of `N`; no random variable is rotated. Define

`ell_i=u1(i)^2+u2(i)^2`,
`q_i=||N[i,:](I-P_span(v1,v2))||_2`,                             (4.3)

`b_i=A[L\{i},i]`,
`d_i=dist(b_i,span(u1^(-i),u2^(-i))).`                           (4.4)

Take

`delta0=1/444`.                                                   (4.5)

The fleet02/B02 physical-hub exterior calculation has four exhaustive alternatives.

### 4.1 Cross-tail exit

If `q_i>=delta0`, then

`E3(N)
 >=x1*x2 sum_(j>=3)x_j
 >=x1*x2 q_i^2
 > kappa/444^2
 =247/113550336
 =2.17524675576e-6.`                                             (4.6)

Apply the completed fleet02/B02 theorem (1.1) to this actual literal physical block. It gives

`boxed: ||p_Q||_infinity <91.156,`                               (4.7)
`boxed: integral_R |phi_Q(t)|dt <572.745.`                       (4.8)

This branch has a continuous `C_0` density.

### 4.2 Punctured same-bank transverse exit

The exact punctured exterior identity is

`W_i>=x1*x2(1-ell_i)d_i^2`,                                     (4.9)

and a fair physical Bernoulli split converts it to a literal cross block `B_i` with

`E3(B_i)>=W_i/16`.                                               (4.10)

If `ell_i<=3/4` and `d_i>=delta0`, then

`E3(B_i)
 >kappa delta0^2/64
 =247/7267221504
 =3.39882305588e-8.`                                             (4.11)

Applying (1.1) at this actual inequality yields

`boxed: ||p_Q||_infinity <181.766,`                              (4.12)
`boxed: integral_R |phi_Q(t)|dt <1142.070.`                      (4.13)

Again the density is continuous `C_0`.

### 4.3 Near-coloop or stronger carrier alignment

If `ell_i>3/4`, retain a top-two near-coloop. Because `sum_i ell_i=2`, there are at most two on each side of the full cut, hence at most four total.

Otherwise `ell_i<=3/4`, while failure of Sections 4.1-4.2 gives

`q_i,d_i<1/444`.                                                 (4.14)

Let `g_i` be the Euclidean norm of the two carrier-aligned pieces: the top-two right-plane component of `N[i,:]` and the projection of `b_i` onto the punctured top-two left plane. These coefficient pieces are orthogonal and lie on disjoint physical banks, so exactly

`||A[i,i^c]||_2^2=g_i^2+d_i^2+q_i^2`.                           (4.15)

Using the live strict hub inequality `||A[i,i^c]||_2>1/222` and (4.14),

`g_i^2 >1/222^2-2/444^2 =1/(2*222^2)`,                          (4.16)

hence

`boxed: g_i>1/(222 sqrt(2))=0.00318516568... .}`                 (4.17)

This strictly strengthens the preceding `1/(228 sqrt(2))` carrier scale.

For every non-near-coloop coordinate, the exact row-deletion identity from the previous B02 run remains available:

`E2(N_(-i))>=x1*x2(1-ell_i)>247/2304`.                           (4.18)

Thus the live unpaid carrier packet now simultaneously has

`max_j |A_jj|<1/222`,
`g_i>1/(222 sqrt(2))`,
`E2(N_(-i))>247/2304`,                                           (4.19)

with the full nonzero quadratic tail retained.

This is the required equation-level use of the completed fleet02/B02 result: the new deterministic lower bounds (4.6) and (4.11) are fed directly into its marginal-free physical-`E3` Fourier theorem, producing (4.7)-(4.8) and (4.12)-(4.13).

## 5. What is and is not closed

The full universal QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. No exact-target counterexample to a universal unweighted

`integral_R |phi_Q(t)|dt <= C`

was found, so that stronger criterion remains **OPEN_NOT_REFUTED**.

This run establishes two concrete advances:

1. a stronger full-matrix Fourier exit: the high spectral window may be raised from `1/19` to `1/18` at leverage threshold `1/76`, giving the explicit `47.760` density / `300.084` Fourier-L1 bounds;
2. failure of that exit forces a larger literal physical hub at clean scale `1/222`; after paying the diagonal alternative, the live robust rank-two survivor is reduced to genuine E3 Fourier exits, at most four near-coloops, or the stronger carrier-aligned-plus-disjoint-E2 packet (4.19).

The first unpaid B02 implication is therefore

`QFORM-SMALLDIAG-1OVER222-CARRIER-HUB-DISJOINT-E2-L1-v1`:

starting from (4.19), couple the single fixed carrier-aligned physical hub to the robust hub-disjoint two-volume before taking absolute values, or route it to the fixed overlap-one grouped-pivot/two-pair receiver. The completed fleet02/B02 one-sided two-pair theorem cannot simply be invoked unless two literal source-separated channels are first produced; its Gaussian twist counterexample forbids pretending arbitrary two-sided curvature is harmless.

The separately tracked fixed overlap-one `V1` grouped-pivot packet and the at-most-four near-coloop packet remain live. Repeating transverse-E3 extraction is not the next mechanism once (4.19) has been reached.

## 6. Integrity and scope ledger

- original-coordinate independence preserved: yes;
- arbitrary cap-one laws: yes;
- arbitrary dimension and signs: yes in each stated branch;
- small spectral/coefficient tails retained exactly: yes;
- pointwise scalar van der Corput used: no;
- rotated random variables treated as independent: no;
- Monte Carlo or histogram used as proof: no;
- general full-target density theorem: not claimed;
- target-wide Fourier L1 theorem: not claimed;
- privacy review: changed files contain only source-pinned pure mathematics and nonsecret run metadata; no credentials, personal archives, financial material, or public-release action.
