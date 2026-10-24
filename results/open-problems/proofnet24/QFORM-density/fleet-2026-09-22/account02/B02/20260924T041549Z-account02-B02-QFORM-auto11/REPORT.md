SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-24T04:15:49Z.

# account02/B02 — two-pair L2xL2 Fourier receiver and exact cross-volume obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate; complementary constructions/source-valid counterexamples  
Status: **NEW SUPPORTING FOURIER-L1 THEOREM + EXACT-TARGET OBSTRUCTION TO D'/D5-ONLY CLOSURE; FULL QFORM OPEN; FULL CONTINUITY OPEN; TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution context: `VERIFIED_BRAIN` in the programme-local sense (authenticated repository retrieval plus actual use of the preceding B02 receiver-memory snapshot); `full_brain_connected=false`.

The full target remains unchanged: independent original real coordinates with probability densities at most one; arbitrary real symmetric A with at least three eigenvalues of modulus at least one; no moment, support, log-concavity, iid, diagonal-basis-independence or post-rotation-independence assumptions. Continuity is separate from essential boundedness.

## 1. Fresh source state and mathematical inputs actually used

Initial fresh brain control was `yspennstate/math-research-brain@e78a429fff805dae3712a4ede4d9372a8d723503`; prepublication refresh advanced only operational/concurrent state to `81c0f4f33f79e90672a7c1cb5c2a518b90943d15`, with the same owner continuation and revision `2026-09-22.15`. The current correction ledger was reread before publication.

The required Claude-source package was read at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. I use two completed tools from that package at an actual obstruction below:

- D': third-volume decoupling with row-volume marginal gate `max alpha_i < 3/4` (or its sharper q-dependent form under the gate);
- D5: fifth-volume Fourier bound with no marginal gate, but requiring positive fifth exterior volume.

The reviewed sharp-Hausdorff--Young third-volume refinement used in prior B02 state is source-pinned through account03/B02 r35, `yspennstate/math-open-problems@c8536549aca3308f1773992e46a6abe4a1dc9922`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T170106Z-account03-B02-qform-r35/REPORT.md`. It records the sharp row-gated coefficient `3e` and a marginal-free physical-E3 compiler obtained by a physical hub cascade. The subsequent B02 rational-threshold refinement used in the receiver memory has coefficient `10.345084` multiplying `E3^{-1/6}`.

The newest completed designated partner used here is account03/B02 r45, `yspennstate/math-open-problems@969923934518c728e4611e670ab6244ceea30215`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T030004Z-account03-B02-qform-r45/REPORT.md`. Its mixed `2+1` theorem lower-bounds a sum of squared minors by `x1*x2 ||Q2 D||_F^2` and then forks that mass into a literal physical E3 cut or an overlap-one third-compound packet.

The preceding B02 receiver-memory snapshot actually used is the `20260924T031112Z-account02-B02-QFORM-auto11` snapshot. Its first unpaid implication was `QFORM-FIXEDSCALE-DIAGONAL-OR-CARRIERALIGNED-HUB-L1-v1` and, critically, it instructed this run not to repeat the exhausted strategy of forcing yet another transverse E3 cut.

## 2. New theorem — `QFORM-TWOPAIRS-ONESIDED-TWIST-L1-v1`

Let `U1,U2,V1,V2` be independent real random variables with densities at most one. Let `W` denote any further collection of independent original coordinates. Suppose that after conditioning `W=w`, the quadratic polynomial in these four active variables has the form

`Q_w = F_w(U1,U2) + (2a U1+c1(w)) V1 + (2b U2+c2(w)) V2 + d(w)`,  (2.1)

where `a,b` are fixed nonzero reals and `F_w` is arbitrary (for the quadratic-form application it may contain arbitrary same-side quadratic and affine terms in `U1,U2`). No independence is asserted after any rotation: the four variables in (2.1) are literal original coordinates. The theorem requires no `V1^2`, `V1 V2`, `V2^2`, `U1 V2` or `U2 V1` term in this chosen four-coordinate carrier after the outside coordinates are conditioned.

Then the full unconditional law satisfies

`boxed: integral_R |phi_Q(t)| dt <= 8*pi / sqrt(|a b|),`          (2.2)

and has a continuous density vanishing at infinity. Moreover the direct density estimate is sharper:

`boxed: ||p_Q||_infinity <= 2 / sqrt(|a b|).`                     (2.3)

Because the Fourier-L1 argument supplies a continuous representative and (2.3) holds essentially, that continuous representative also obeys the same height bound.

### 2.1 Proof of the Fourier-L1 estimate

Fix `w`. Write `h_j=c_j(w)/(2a_j)`, with `a_1=a`, `a_2=b`, and let `psi_j` be the characteristic function of `V_j`. Then

`phi_w(t)=E_U [ exp(i t(F_w(U)+d(w)))
                psi_1(2 a t (U1+h1))
                psi_2(2 b t (U2+h2)) ].`                         (2.4)

Take absolute values only after retaining the original product variables, then apply Minkowski/Tonelli in `U` and Cauchy--Schwarz in `t`:

`||phi_w||_1
 <= E_U ||psi_1(2a(U1+h1)t) psi_2(2b(U2+h2)t)||_1
 <= E_U prod_(j=1)^2 ||psi_j(2 a_j (U_j+h_j)t)||_2.`              (2.5)

Plancherel and `f_{V_j}<=1`, `int f_{V_j}=1` give

`||psi_j||_2^2 = 2*pi ||f_{V_j}||_2^2 <= 2*pi`,                  (2.6)

hence

`||psi_j(2a_j(U_j+h_j)t)||_2
 <= sqrt(pi) |a_j|^(-1/2) |U_j+h_j|^(-1/2).`                     (2.7)

For every cap-one probability density `f` and every shift `h`, the one-dimensional bathtub inequality gives

`int f(u)|u+h|^(-1/2) du
 <= int_(-1/2)^(1/2) |u|^(-1/2) du
 = 2 sqrt(2).`                                                    (2.8)

Independence of `U1,U2` therefore yields

`||phi_w||_1 <= pi |ab|^(-1/2) (2sqrt(2))^2
               = 8*pi |ab|^(-1/2).`                              (2.9)

The bound is uniform in `w`, `F_w`, `c_j(w)` and `d(w)`. Since

`phi_Q(t)=E_W phi_w(t)`,

Tonelli gives `||phi_Q||_1 <= E_W ||phi_w||_1`, proving (2.2). Fourier inversion gives a continuous `C_0` density.

### 2.2 Direct height bound

Condition on `W=w` and `U=(u1,u2)`. The remaining random part is a sum of two independent scaled variables

`2a(u1+h1)V1 + 2b(u2+h2)V2`

plus a deterministic shift. Convolution with a probability law cannot increase a density supremum, so the conditional density height is at most

`1 / [2 max(|a(u1+h1)|, |b(u2+h2)|)].`                           (2.10)

Under the physical change of coefficient variables

`x1=a(u1+h1), x2=b(u2+h2)`,

the joint density `g` has total mass one and satisfies `g<=K:=1/|ab|`. The two-dimensional bathtub inequality for the decreasing kernel `1/||x||_infinity` gives

`int g(x)/||x||_infinity dx <= 4 sqrt(K)=4/sqrt(|ab|)`.          (2.11)

Indeed the extremal cap-K set is the centered square of area `1/K`; if its radius is `r=1/(2sqrt(K))`, then

`K int_(||x||_infinity<=r) ||x||_infinity^(-1) dx
 =K int_0^r s^(-1) d(4s^2)
 =8Kr
 =4sqrt(K).`                                                      (2.12)

Averaging (2.10) proves (2.3), uniformly in the conditioned outside coordinates.

### 2.3 Exact boundary of this proof

The one-sided twist hypothesis is real. A naive claim that each hyperbolic pair retains a uniform `L^2_t` bound after arbitrary quadratic twists on both endpoints is false. For independent standard Gaussians `U,V` (whose densities are below one),

`U^2+V^2+2UV=(U+V)^2`,

and

`|E exp(i t (U+V)^2)|=(1+16t^2)^(-1/4)`,                         (2.13)

whose square has a logarithmically divergent integral. Thus the next receiver cannot simply apply the present per-pair L2 step after absorbing arbitrary curvature on both banks; it must use two-pair/third-resource structure jointly.

This is an obstruction to a proposed extension, not to QFORM and not to target-wide Fourier-L1.

## 3. Exact-target stress family for D', D5 and the new receiver

On seven original coordinates `(x0,y1,y2,y3,z1,z2,z3)`, define

`A_eps = [1] direct_sum [[0,D_eps],[D_eps,0]],`

`D_eps=diag(1,1,eps)`, `0<=|eps|<=1`.                             (3.1)

Then

`spec(A_eps)={1,+/-1,+/-1,+/-|eps|}`.                            (3.2)

Hence every member, including `eps=0`, satisfies the exact target hypothesis with at least five eigenvalues of modulus at least one. The quadratic form is

`Q_eps=X0^2+2Y1Z1+2Y2Z2+2eps Y3Z3`.                              (3.3)

### 3.1 D' and D5 on every physical cross cut

A disjoint physical cut never sees the diagonal loop `A_{x0,x0}=1`. The remaining coefficient graph is just three disjoint matching edges of weights `1,1,eps`. Therefore every physical cross block has rank at most three. More precisely,

`boxed: sup_(I disjoint J) E3(A_eps[I,J])=eps^2,`                 (3.4)

`boxed: sup_(I disjoint J) E5(A_eps[I,J])=0.`                     (3.5)

For the full matching block `M_eps=D_eps`, when `eps!=0` there is exactly one nonzero third minor, so every third-volume row marginal is `alpha_i=1`. Thus the source D' gate `alpha_i<h<3/4` fails maximally. D5 is unavailable because every fifth volume vanishes. The reviewed marginal-free E3/sharp-HY compiler does pay `eps!=0`, but only as

`||p_Q||_infinity <= 10.345084 |eps|^(-1/3)`,                    (3.6)

with the corresponding Fourier-L1 certificate; this deteriorates without bound as `eps->0` and disappears at `eps=0`.

This is a real obstruction to a proof architecture that tries to close the exact target by forcing a uniformly positive physical D'/D5 exterior currency.

### 3.2 Uniform integrated-Fourier payment

Apply Theorem 2 with `a=b=1`, active variables `(Y1,Y2,Z1,Z2)`, `F=0`, and independent remainder

`R=X0^2+2eps Y3Z3`.                                                (3.7)

For every `eps`, every allowed product law,

`boxed: integral_R |phi_{Q_eps}(t)|dt <= 8*pi,`                  (3.8)

`boxed: ||p_{Q_eps}||_infinity <=2.`                              (3.9)

Thus this exact-target family has a continuous `C_0` density with a uniform height bound even though all physical E3 currencies collapse like `eps^2` and every E5 currency is exactly zero.

This is not a counterexample to QFORM and not a counterexample to the stronger target-wide Fourier-L1 criterion. It is a source-valid counterexample to D'/D5-only structural closure.

## 4. Equation-level application of the newest designated partner r45

Use the literal full partition

`L={x0,y1,y2,y3}`, `R={z1,z2,z3}`.                               (4.1)

The cross block `N=A[L,R]` has squared singular values `1,1,eps^2,0`, so `x1*x2=1`. Its top-two left carrier is `span{y1,y2}`. The same-side block `D=A[L,L]` is the single diagonal square at `x0`, hence

`||(I-P2)D||_F^2=1`.                                              (4.2)

The r45 mixed `2+1` lower bound therefore gives `T>=1`. In this family the aggregate can be evaluated exactly:

`boxed: T=1+2 eps^2,  T_off=0,  T_overlap=T.`                     (4.3)

The three nonzero terms are

`det A[{x0,y1,y2},{x0,z1,z2}]=1`,

`det A[{x0,y1,y3},{x0,z1,z3}]=eps`,

`det A[{x0,y2,y3},{x0,z2,z3}]=eps`.                              (4.4)

Thus the newest partner's fork lands **entirely** in its overlap-one third-compound branch. In fact direct enumeration gives

`V1=4+8 eps^2`,                                                    (4.5)

so a fixed overlap-one packet survives even at `eps=0` while every disjoint physical E3/E5 currency vanishes.

This is the requested equation-level partner application: it shows that the r45 physical-diagonal endpoint is not an artefact of loose inequalities. It is a genuine geometry in which overlap-one curvature must be paid by a mechanism different from forcing another disjoint cross volume. Theorem 2 supplies exactly such a mechanism on the source-separated two-pair subfamily.

## 5. Deterministic checks

A finite enumeration over all `3^7=2187` assignments of each coordinate to the row side, column side or neither was run for `eps=1,0.1,0.01,0`. It returned maximum physical cross ranks `3,3,3,2`, maximum `E3` values `1,10^-2,10^-4,0`, and `E5=0` in every case, exactly matching (3.4)-(3.5). The spectrum was also reproduced exactly to numerical precision. The mixed-volume enumeration returned `T=1+2eps^2`, `T_off=0`, and total overlap-one mass `V1=4+8eps^2`. Saved check status: `PASS`.

These computations corroborate only finite algebraic identities already proved above; they are not evidence for the unrestricted conjecture.

## 6. What this changes in the B02 proof graph

The previous unpaid implication was `QFORM-FIXEDSCALE-DIAGONAL-OR-CARRIERALIGNED-HUB-L1-v1`. This run resolves a nontrivial source-coordinate subclass of that endpoint: when a robust physical rank-two crossing contains two literal matching channels and all active self-curvature can be placed on one source bank after outside conditioning, the full law has a uniform unweighted Fourier-L1 estimate with no third/fifth cross-volume requirement.

The exact family (3.1) proves that a fixed diagonal third spectral direction can feed only an overlap-one packet while every disjoint D'/D5 currency degenerates. Therefore repeating transverse-E3 extraction is the wrong next mechanism.

The first unpaid implication is now

`QFORM-OVERLAP1-TWOPAIRS-TWOSIDED-CURVATURE-L1-v1`:

starting from the r45 fixed overlap-one/grouped-pivot packet or the carrier-aligned physical hub, extend the two-pair source-preserving receiver to the case where the opposite bank carries genuine quadratic curvature/coupling, without post-rotation independence and without splitting into per-pair L2 estimates that are refuted by (2.13). A successful receiver may use a joint two-pair oscillatory integral, fractional potential, or the third physical square/hub as an additional smoothing resource. The unrestricted target remains open.

No exact-target QFORM counterexample was found. No exact-target counterexample to universal unweighted Fourier-L1 was proved in this run.
