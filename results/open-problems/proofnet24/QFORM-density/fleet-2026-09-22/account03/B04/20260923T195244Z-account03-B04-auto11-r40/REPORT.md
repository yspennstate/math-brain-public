SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T19:52:44Z.
attacking: sharpen the critical two-volume product-Fourier collision bound, then spend it on the one-overlap third-compound class through an exact physical scalar pivot.

# account03/B04 r40 — sharp critical E2 collision and a pivoted C1-overlap receiver

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Assignment: Product Fourier rearrangement.  
Status: `NEW SUPPORTING THEOREMS / FIRST AGGREGATE C1-OVERLAP SUBRECEIVER / EXPLICIT ROTATED-INDEFINITE ESTIMATE / FULL TARGET OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Continuity: not proved by the new critical receiver; the unrestricted full-target continuity statement remains OPEN.

The exact unrestricted conjecture is not proved here. All random variables remain in ORIGINAL independent coordinates. No Gaussianity, log-concavity, moment, compact-support, connected-support, post-rotation independence, arbitrary-joint coarea, worst-fiber density supremum, or law-uniform pointwise quadratic-phase decay is used.

## 1. Source boundary and mechanism change

The current global compound decomposition from account01/B02 is source-pinned at

`yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260923T184631Z-account01-B02-qform-auto11-r34/REPORT.md`.

For a symmetric matrix `A` it defines

`C_k(A)=sum_{|S|=|T|=3, |S cap T|=k} det(A[S,T])^2`, `k=0,1,2,3`,            (1.1)

and proves

`e_3(A^2)=C_0+C_1+C_2+C_3>=1`                                                    (1.2)

under the target spectral hypothesis. Hence one `C_k>=1/4`. Its `C_0` branch is already paid by a random physical cut plus the marginal-free cross-E3 Fourier theorem. The first new debt is therefore the aggregate overlap class `C_1`.

The critical two-volume theorem refined below is account01/B03 r30:

`yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T175336Z-account01-B03-QFORM-r30/REPORT.md`.

It gives a row-marginal-free `|t|^{-1}` Fourier envelope for an arbitrary physical two-bank crossing with nonzero `E_2`. The only step sharpened here is its diffuse `k=0, ell=2` weighted-subset entropy factor. The sharp fixed-cardinality entropy lemma proved in account03/B04 r39 is rederived below, so this report is self-contained at that step.

The designated partner `account04/B04` still had no completed current-QFORM shared handoff in the fresh direct lookup. I therefore do not fabricate a designated-partner theorem or wait for it. Completed peer results are applied at explicit equations below.

## 2. Sharp fixed-two-subset entropy

Let `w` be a probability law on unordered two-subsets `{i,j}` of a finite physical row set. Put

`alpha_i=P_w(i in S)`, so `sum_i alpha_i=2`.                                   (2.1)

Uniformly order the two elements of `S`, obtaining `(I_1,I_2)`. Then

`H(I_1,I_2)=H(w)+log 2`,                                                         (2.2)

while each ordered marginal has law `P(I_r=i)=alpha_i/2`. Entropy subadditivity gives

`H(w)+log 2 <= 2 H(alpha/2)
             =-sum_i alpha_i log alpha_i+2 log 2`.                              (2.3)

Therefore

`boxed: H(w)+sum_i alpha_i log alpha_i <= log 2.`                               (2.4)

Equivalently, the exact weighted-subset determinant/entropy factor satisfies

`boxed: exp{[H(w)+sum_i alpha_i log alpha_i]/2} <= sqrt(2).}`                    (2.5)

The constant is sharp as a supremum: for the uniform law on all pairs of an `m`-point set the square of the factor is `2(m-1)/m ->2`.

## 3. Sharp row-marginal-free critical two-volume collision theorem

Split independent original coordinates into disjoint banks `I,J` and write

`R=F(X_I)+2 X_I^T B X_J+G(X_J)`,                                                 (3.1)

where `F,G` are arbitrary real quadratic-plus-affine functions. Put

`Z_2=e_2(BB^T)=sum_{i<j}|b_i wedge b_j|^2>0`.                                  (3.2)

### Theorem 3.1 — `QFORM-SHARP-ROW-MARGINAL-FREE-2VOLUME-COLLISION-v1`

For every product input with scalar densities at most one,

`boxed:
 |phi_R(t)| <= min{1, pi*2^(7/4) Z_2^(-1/4)|t|^(-1)}.}`                         (3.3)

Consequently `R` has an `L^2` density and

`boxed: ||p_R||_2^2 <=2^(11/4) Z_2^(-1/4).}`                                    (3.4)

The translation-uniform half-Riesz bounds are

`boxed:
 sup_s E|R-s|^(-1/2) <=8*2^(3/8) Z_2^(-1/8),}`                                  (3.5)

and, for an independent copy `R'`,

`boxed:
 E|R-R'|^(-1/2) <=(16/3)*2^(3/8) Z_2^(-1/8).}`                                  (3.6)

No continuity conclusion is asserted from this critical `L^2` endpoint alone.

### Proof

Define the canonical pair-volume marginals

`alpha_i=Z_2^(-1) sum_{j!=i}|b_i wedge b_j|^2`, `sum alpha_i=2`.                 (3.7)

The completed account01/B03 proof divides into three exhaustive cases.

**Diffuse pair volume.** If every `alpha_i<=1/2`, whole-bank Cauchy-Schwarz and an independent copy of the `J` bank reduce `|phi_R(t)|^2` to the `k=0,ell=2` weighted-subset expression. Before its last entropy relaxation, the source bound is

`|phi_R(t)|^2
 <= [8 pi^2 /(sqrt(Z_2)|t|^2)]
    exp{[H(w)+sum_i alpha_i log alpha_i]/2}.`                                    (3.8)

Insert (2.5):

`|phi_R(t)|^2 <=8 pi^2 sqrt(2)/(sqrt(Z_2)|t|^2)`.                               (3.9)

Taking square roots yields (3.3), because

`sqrt(8 sqrt(2))=2^(7/4)`.                                                       (3.10)

**One heavy row.** If some `alpha_i>1/2`, project every other crossing row perpendicular to the heavy row. If the resulting one-volume law is diffuse, the completed one-hub/one-crossing receiver gives

`|phi_R(t)|<min{1,2 pi 2^(1/4) Z_2^(-1/4)|t|^(-1)}`,                            (3.11)

whose coefficient `2 pi 2^(1/4)` is strictly smaller than `pi 2^(7/4)`.

**Two heavy rows.** If the projected one-volume law also has a marginal above `1/2`, the exact base-times-height identity produces two literal physical rows with squared wedge `>Z_2/4`. The exact-rank-two crossing/Plancherel theorem then gives

`|phi_R(t)|<min{1,2 pi Z_2^(-1/4)|t|^(-1)}`,                                    (3.12)

again below (3.3). Thus (3.3) is row-marginal-free.

Put `T=pi 2^(7/4) Z_2^(-1/4)`. Exact integration of the decreasing envelope gives

`int |phi_R|^2 <=4T`,                                                            (3.13)

so Plancherel yields

`||p_R||_2^2 <=(2pi)^(-1)4T=2^(11/4)Z_2^(-1/4)`.                               (3.14)

Likewise

`int |t|^(-1/2)|phi_R(t)|dt <=8 sqrt(T)`,                                       (3.15)

and

`int |t|^(-1/2)|phi_R(t)|^2dt <=(16/3)sqrt(T)`.                                (3.16)

Using

`int_R |t|^(-1/2)e^(itx)dt=sqrt(2pi)|x|^(-1/2)`                                (3.17)

with standard positive cutoffs proves (3.5)-(3.6). Note

`sqrt(T)/sqrt(2pi)=2^(3/8) Z_2^(-1/8)`.                                         (3.18)

This completes the proof.

Numerically, the new envelope coefficient is

`pi 2^(7/4)=10.567016002364246...`,                                                (3.19)

improving the preceding `2 pi sqrt(2e)=14.6501512067...`; the one-copy half-Riesz coefficient improves from `12.2157772909...` to

`8*2^(3/8)=10.374716437208077...`.                                                (3.20)

## 4. Square receiver

### Corollary 4.1 — `QFORM-SHARP-E2-PLUS-SQUARE-RECEIVER-v1`

Let `Z` be one further original scalar coordinate, independent of the background defining `R`, with density at most one. Suppose

`Q=d[Z+h]^2+R`, `d!=0`,                                                         (4.1)

where `h` may be an arbitrary measurable function of the background. Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=8*2^(3/8)|d|^(-1/2) Z_2^(-1/8).}`                                             (4.2)

Indeed, conditional on the background, the shifted square pushforward has density at most

`|d|^(-1/2)|u|^(-1/2)`                                                          (4.3)

on the appropriate half-line. Therefore

`p_Q(s)<=|d|^(-1/2) E|s-R|^(-1/2)`,                                             (4.4)

and (3.5) proves (4.2). This argument is insensitive to the sign of `d` by reflection.

## 5. First aggregate `C_1` overlap receiver

For one physical coordinate `h`, define the anchored overlap-one compound mass

`C_{1,h}(A)
 =sum_{U,V subset [n]\{h}, |U|=|V|=2, U cap V=emptyset}
   det A[{h} union U,{h} union V]^2`.                                            (5.1)

The pairs `(U,V)` are ordered. Since every third-compound pair with overlap exactly one has a unique common coordinate,

`C_1(A)=sum_h C_{1,h}(A)`.                                                       (5.2)

Assume the physical diagonal pivot

`a=A_hh !=0`.                                                                   (5.3)

Let `Y=X_[n]\{h}`, let `b=A_{h,[n]\{h}}`, and form the exact physical Schur complement

`S_h=A_[n]\{h},[n]\{h}-a^(-1)b^T b`.                                           (5.4)

Completing the scalar square gives, with no rotation of the random variables,

`X^T A X
 =a[X_h+a^(-1)bY]^2 + Y^T S_h Y`.                                               (5.5)

For disjoint two-sets `U,V` in the residual coordinates, the block determinant formula gives

`det A[{h} union U,{h} union V]
 =a det S_h[U,V]`.                                                              (5.6)

Hence, writing

`D_h=sum_{U cap V=emptyset, |U|=|V|=2} det S_h[U,V]^2`,                          (5.7)

we have the exact identity

`boxed: C_{1,h}(A)=a^2 D_h.}`                                                    (5.8)

Now independently color every residual physical coordinate into banks `J,K` with probability `1/2`. For

`B_{J,K}=S_h[J,K]`,                                                            (5.9)

Cauchy-Binet gives

`E_2(B_{J,K})
 =sum_{U subset J, |U|=2}
   sum_{V subset K, |V|=2}det S_h[U,V]^2`.                                      (5.10)

A fixed ordered disjoint pair `(U,V)` is captured with probability `2^(-4)=1/16`. Therefore

`boxed: E_{J} E_2(S_h[J,J^c])=D_h/16.}`                                         (5.11)

So one literal original-coordinate cut satisfies

`Z_2:=E_2(S_h[J,J^c])>=D_h/16`.                                                  (5.12)

### Theorem 5.1 — `QFORM-PIVOTED-C1-OVERLAP-RECEIVER-v1`

For every `h` with `A_hh!=0` and `C_{1,h}(A)>0`, the full target quadratic law has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <=8*2^(7/8) [A_hh^2 C_{1,h}(A)]^(-1/8).}`                                      (5.13)

The numerical front coefficient is

`8*2^(7/8)=14.672064691274741...`.                                                (5.14)

#### Proof

Choose the physical cut from (5.12). The residual Schur form is exactly of the two-bank form (3.1), retaining all same-bank curvature and affine terms, so Corollary 4.1 applied to (5.5) yields

`||p_Q||_infinity
 <=8*2^(3/8)|a|^(-1/2)(D_h/16)^(-1/8)`
` =8*2^(7/8)|a|^(-1/2)D_h^(-1/8)`
` =8*2^(7/8)[a^2 C_{1,h}(A)]^(-1/8)`,                           (5.15)

where the last identity uses (5.8). QED.

This is homogeneous at the correct scale: replacing `A` by `cA` multiplies `A_hh^2 C_{1,h}` by `|c|^8`, and the right side by `|c|^-1`.

The theorem spends an entire overlap-one packet before any reciprocal local `3x3` minor is selected. Its remaining gate is explicit: the common physical coordinate must carry nonzero scalar quadratic pivot, and the diagonal-weighted aggregate currency `A_hh^2 C_{1,h}` must be target-scale.

## 6. Equation-level application to the global overlap decomposition

The completed account01/B02 theorem (1.1)-(1.2) says every target matrix has one `C_k>=1/4`; its `C_0>=1/4` branch is already paid continuously. Suppose instead that

`C_1(A)>=1/4`.                                                                  (6.1)

Theorem 5.1 gives the following exact additional exit:

`boxed:
 max_h A_hh^2 C_{1,h}(A) >= eta
 => ||p_Q||_infinity <=8*2^(7/8) eta^(-1/8).}`                                  (6.2)

Thus an unpaid `C_1` state after this run must satisfy, simultaneously for every physical coordinate,

`A_hh^2 C_{1,h}(A)<eta`,                                                        (6.3)

while the unweighted masses still sum to at least `1/4`. This isolates the actual residual obstruction: overlap-one third-compound mass carried by zero/near-zero diagonal anchors and/or spread among many anchors so that no diagonal-weighted anchored packet is target-scale. It is not a generic `C_1` mystery anymore.

This is an equation-level application of a completed peer result to the live proof frontier, not a claim that (6.3) is already paid.

## 7. Fully dense genuinely rotated indefinite example

Consider the symmetric physical-coordinate matrix

`A_* = [[1,1,1,1,1],
        [1,1,1,3,2],
        [1,1,1,2,-1],
        [1,3,2,1,1],
        [1,2,-1,1,1]].`                                                          (7.1)

Every entry is nonzero, so this is not diagonal or block-diagonal in the independent coordinates. Exact determinant arithmetic gives

`det(lambda I-A_*)
 =(lambda^2-5)(lambda^3-5 lambda^2-9 lambda+5)`.                                 (7.2)

Hence `+-sqrt(5)` are eigenvalues. The cubic is negative at `6` and positive at `7`, and negative at `-2` and positive at `-1`, so `A_*` has at least four eigenvalues of modulus greater than one and is indefinite. It therefore satisfies the owner's exact spectral hypothesis strongly.

Because `n=5`, two physical triples cannot be disjoint, so

`C_0(A_*)=0`.                                                                    (7.3)

Exact enumeration gives

`(C_0,C_1,C_2,C_3)=(0,484,1728,198)`,                                            (7.4)

so this is genuinely an overlap-dominated example rather than an instance of the already-paid disjoint-compound branch.

Pivot the second physical coordinate (`h=2` in one-based indexing). Here `a=A_22=1`, and in residual order `(1,3,4,5)` the Schur complement is

`S_2=[[ 0, 0,-2,-1],
     [ 0, 0,-1,-3],
     [-2,-1,-8,-5],
     [-1,-3,-5,-3]].`                                                           (7.5)

Its anchored overlap mass is

`C_{1,2}(A_*)=124`.                                                             (7.6)

Choose the literal residual cut

`J={1,5}`, `K={3,4}`.                                                           (7.7)

Then

`S_2[J,K]=[[0,-2],[-3,-5]]`, `det=-6`,                                          (7.8)

so

`Z_2=E_2(S_2[J,K])=36`.                                                         (7.9)

The sharp square receiver (4.2) now gives, for every admissible independent cap-one product input,

`boxed:
 ||p_{X^T A_* X}||_infinity
 <=8*2^(3/8) 36^(-1/8)
 =6.628853526064557... .}`                                                       (7.10)

This is a concrete new product-Fourier estimate for a fully dense rotated indefinite form.

For comparison, applying the completed exact-rank-two crossing/Plancherel peer theorem to the actual `2x2` block (7.8) gives

`|phi_R(t)|<=min{1, [pi/sqrt(6)]|t|^(-1)}`.                                     (7.11)

Running the same half-Riesz/square calculation gives the independent stronger example-specific comparison

`||p_{X^T A_* X}||_infinity
 <=4 sqrt(2) 6^(-1/4)
 =3.6144080144393795...`.                                                        (7.12)

Equation (7.12) is a genuine application of a completed peer Fourier result; (7.10) is the uniform row-marginal-free theorem developed in this run.

## 8. What remains

Full QFORM remains OPEN. Full-target continuity remains OPEN separately. The new critical `E_2` receiver proves essential boundedness but, at the `|t|^{-1}` endpoint, does not by itself put the characteristic function in `L^1`; no continuity claim is made for Theorem 5.1.

The first nonduplicate B04 implication is now

`QFORM-C1-ZEROPIVOT-OR-FRACTIONAL-HUB-RECEIVER-v1`:

> Starting from `C_1(A)>=1/4` and the failure of every diagonal-weighted exit (6.2), aggregate the zero/near-zero scalar-pivot anchors by a product-preserving hyperbolic/one-hub Fourier mechanism, or route them quantitatively to the existing pair/star/ridge/grouped-bank endpoints. The argument must not select a vanishing local minor, duplicate the shared coordinate as independent row/column variables, or delete small coefficients as random perturbations.

The sibling overlap classes `C_2,C_3` from the global compound decomposition also remain unpaid unless another current worker closes them. No claim here changes their status.

Model self-report: `GPT-5.6 Sol`. Configured reasoning level: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token and thinking-time counters: not exposed. No scheduler, task identity, email, notification, public-release, paid-API, or cross-account authentication state was changed.
