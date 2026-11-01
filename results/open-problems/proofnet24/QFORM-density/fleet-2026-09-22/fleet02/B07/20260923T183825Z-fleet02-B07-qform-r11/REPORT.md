SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T18:38:25Z.
attacking: partner r35 rank-two interface tube — retain its determinant weights, close the physically support-concentrated rank-two carrier branch by an actual principal core, and identify exact target-class diffuse/coloop endpoints without selecting one coordinate minor.

# fleet02/B07 r11 — rank-two carrier Pluecker mass gives a 262-coordinate actual spectral core

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Method: complementary constructions and source-valid counterexamples  
Run: `20260923T183825Z-fleet02-B07-qform-r11`  
Initial control head: `yspennstate/math-research-brain@0c15c14199790afed64185ab32189722b0c41bc5`  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW R35 RANK-TWO-CARRIER PLUECKER CORE RECEIVER / EXACT DIFFUSE AND ONE-COLOOP TARGET REGRESSIONS / PINNED-e5 FOURIER PAYMENTS / FULL QFORM OPEN**.

The unrestricted conjecture is not proved or disproved here. Inputs are independent ORIGINAL-coordinate real variables with densities at most one. No moments, bounded support, connected support, log-concavity, iid assumption, diagonal-basis assumption, or post-rotation independence is used. Singular frames below are deterministic matrix geometry only. Essential boundedness is the target; continuity remains separate unless a quoted theorem explicitly provides it.

## 1. First unpaid implication

After the result below, the first B07 debt is

`QFORM-R35-R2-PLUECKER-DIFFUSE-OR-R1-ROUGH-TAIL-RECEIVER-v1`:

> In the partner r35 low-E3 branch, after removing all rank-two carriers whose left and right rank-two Pluecker laws each put at least half their mass on at most 131 physical coordinates, pay either (i) a rank-at-most-one compound-interface carrier or (ii) a rank-two carrier for which at least one physical Pluecker law is genuinely support-diffuse. The payment must retain the true nonzero interface tail, arbitrary same-bank quadratic curvature, all outside couplings, and all extra spectrum. It may not condition on a rotated complement and assert independence, may not treat the small Frobenius tail as a small random error, and may not replace the aggregate Pluecker law by one selected minor.

Two exact tail-zero endpoints of (ii) are paid below by the pinned e5 Fourier theorems. What remains is the uniform rough-tail bridge; this is precisely where conditional adaptation rather than finite-dimensional spectral extraction is needed.

## 2. Fresh source boundary and incoming r35 packet

The latest completed designated partner consumed in this run is fleet03/B07 r35,

`yspennstate/math-open-problems@3a3334245375f0d72687f3cb482b4478d51f3188`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T173750Z-fleet03-B07-qform-r35/REPORT.md`.

Its incoming literal original-coordinate cross block is

`K=A[L,R]`,                                                      (2.1)

with second compound mass

`Z=e_2(KK^T)>Z0 h^4`,
`Z0=854675.100194511`,                                          (2.2)

at the strict-N3 scale

`h=(2sqrt(2)-1)/1572864
  =1.1624826588606455e-6`.                                      (2.3)

The same strict-N3 state carries the physical coefficient bounds

`|A_ij|<=h/8` for relevant distinct original coordinates,
`|A_ii|<h^2/128`.                                               (2.4)

Let the nonzero singular values of K be `s_r`, set `x_r=s_r^2`, `S=sum_r x_r`, and normalize its spectral pair-volume law by

`q_{rs}=x_r x_s/Z`, `r<s`.                                      (2.5)

Its inclusion marginals are

`alpha_r=x_r(S-x_r)/Z`,
`sum_r alpha_r=2`.                                              (2.6)

Partner r35 defines the spectral projection P onto directions with

`alpha_r>2/3`.                                                  (2.7)

Hence `rank(P)<=2`. On the low-E3 branch for the full one-sided physical interface

`T_L=A[L,L^c]`,                                                  (2.8)

r35 proves

`||(I-P_L)T_L||_F < eps0 h`,
`eps0=3/sqrt(Z0)=0.0032450450393877377`.                        (2.9)

The transpose-side projection uses the same selected singular indices. The sibling E3 branch is already analytically paid in r35; this report studies the low-E3 branch and, within it, the case `rank(P)=2`.

The required pinned source was read at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The source's unrestricted conjecture remains open. Its completed rank-r Fresnel--Brascamp--Lieb theorem and mixed-hub theorem are applied below to exact target-class obstructions; they are not used nominally.

## 3. Two heavy compound directions carry one-third of all E2 volume

Assume `rank(P)=2`, and call the selected singular indices `a,b`. In the probability law (2.5), the events

`E_a={pair contains a}`, `E_b={pair contains b}`

have probabilities `alpha_a,alpha_b>2/3`. Since a pair contains both a and b exactly on the single event `{a,b}`,

`q_ab=P(E_a intersect E_b)
    >=P(E_a)+P(E_b)-1
    >1/3`.                                                       (3.1)

Therefore

`boxed:
(s_a s_b)^2 > Z/3 > (Z0/3)h^4.`                                (3.2)

This is the first useful aggregate consequence. It selects two SINGULAR directions because r35's spectral compound projection already did so; it does not select any physical coordinate minor.

Let

`U=[u_a,u_b]`, `V=[v_a,v_b]`,                                  (3.3)

where U and V are orthonormal two-frames in the physical L and R coordinate spaces, and put

`C=s_a u_a v_a^T+s_b u_b v_b^T`.                               (3.4)

Because P is the singular-direction projection, the restriction of (2.9) to the K block is exactly the unselected singular tail:

`boxed: ||K-C||_F<eps0 h.`                                      (3.5)

No random-variable perturbation argument is made from (3.5); it will only certify the actual finite physical matrix after restriction.

## 4. The rank-two physical Pluecker laws

For a physical row support `R0 subset L`, define

`rho_L(R0)=det(U_R0^T U_R0)`.                                  (4.1)

Cauchy--Binet gives

`rho_L(R0)
 =sum_{S subset R0, |S|=2} det(U_S)^2`.                         (4.2)

Since `U^T U=I_2`, the same sum over all row pairs equals one. Thus (4.2) is exactly the probability that the rank-two carrier's normalized squared-Pluecker row pair lies entirely inside R0. Define analogously

`rho_R(C0)=det(V_C0^T V_C0)
 =sum_{T subset C0, |T|=2} det(V_T)^2`.                         (4.3)

These are the determinant/volume weights carried through the selection. The theorem below requires aggregate capture `rho_L,rho_R`; no individual row pair or column pair is ever inverted.

A useful sufficient condition is physical leverage-tail control. If

`delta_L=sum_{i outside R0} ||U_i||_2^2`,                       (4.4)

then, writing `N=U_{R0^c}^T U_{R0^c}` with eigenvalues `n1,n2>=0`,

`rho_L=det(I_2-N)
      =(1-n1)(1-n2)
      =1-delta_L+n1 n2
      >=1-delta_L`.                                             (4.5)

So a leverage tail at most 1/2 implies `rho_L>=1/2`, but (4.1) is the more intrinsic rank-two area quantity.

## 5. Exact factorization of retained carrier determinant mass

Take physical supports `R0 subset L`, `C0 subset R`; write

`p=|R0|`, `q=|C0|`, `m=max(p,q)`,                               (5.1)

and let

`C00=C[R0,C0]`.                                                 (5.2)

Because C has exact rank at most two, applying Cauchy--Binet on both sides gives the exact identity

`e_2(C00 C00^T)
 =(s_a s_b)^2 rho_L(R0) rho_R(C0)`.                             (5.3)

One way to see (5.3) is to expand each physical `2x2` determinant:

`det C[S,T]
 =(s_a s_b) det U[S,:] det V[T,:]`,                             (5.4)

then sum its square over `S subset R0`, `T subset C0` and use (4.2)-(4.3).

Combining (3.2) and (5.3),

`boxed:
e_2(C00 C00^T)
 >(Z/3) rho_L rho_R.`                                           (5.5)

Let `t1>=t2>=0` be the two nonzero singular values of C00. Since C00 has rank at most two,

`t1 t2=sqrt(e_2(C00 C00^T))
 >sqrt(Z/3) sqrt(rho_L rho_R).`                                 (5.6)

This is the key improvement over applying a crude pigeonhole bound to all physical minors: the entire selected singular pair-volume remains aggregated inside the two Pluecker support probabilities.

## 6. Convert carrier area into an actual second singular value

Let

`K00=K[R0,C0]`, `E00=K00-C00`.                                 (6.1)

Equation (3.5) gives

`||E00||_op<=||E00||_F<eps0 h`.                                (6.2)

By the physical coefficient cap (2.4),

`||K00||_op<=||K00||_F<=sqrt(pq)h/8<=m h/8`.                   (6.3)

Hence

`t1=||C00||_op
 <=||K00||_op+||E00||_op
 <(m/8+eps0)h`.                                                 (6.4)

Divide (5.6) by (6.4), use (2.2), and then restore the true tail with Weyl:

`boxed:
s_2(K00)
 >h[ sqrt(Z0/3)*sqrt(rho_L rho_R)/(m/8+eps0)-eps0 ].`          (6.5)

This is an ACTUAL singular-value bound for the physical K block. The small tail has not been discarded from the random quadratic form; it has only been used in the deterministic matrix inequality (6.2).

## 7. Actual bounded physical principal core

Let

`H=R0 union C0`.                                                (7.1)

The two sides are disjoint original-coordinate banks. Decompose the actual physical principal block as

`A_HH = O00+B00`,                                               (7.2)

with

`O00=[[0,K00],[K00^T,0]]`,                                     (7.3)

and B00 block-diagonal, containing the two TRUE same-side principal blocks. The singular values of O00 duplicate those of K00, so

`s_4(O00)=s_2(K00)`.                                            (7.4)

From (2.4), each same-side block of size at most m has maximum absolute row sum below

`mu_m=(m-1)h/8+h^2/128`,                                       (7.5)

hence

`||B00||_op<=mu_m`.                                             (7.6)

Weyl's singular-value inequality and (6.5) give the new physical-core theorem.

### Theorem 7.1 — `QFORM-R35-R2-CARRIER-PLUECKER-CORE-v1`

On the partner r35 low-E3 branch, suppose the heavy compound projection has rank two. For any physical supports R0,C0 of size at most m, with carrier Pluecker capture probabilities rho_L,rho_R,

`boxed:
s_4(A_HH)
 > h Gamma_m(rho_L,rho_R),`                                    (7.7)

where

`Gamma_m(rho_L,rho_R)
 = sqrt(Z0/3)*sqrt(rho_L rho_R)/(m/8+eps0)
   -eps0 -(m-1)/8-h/128.`                                      (7.8)

Whenever `Gamma_m>0`, the ACTUAL physical principal block A_HH has four eigenvalues of modulus at least `h Gamma_m`.

No individual physical minor is selected, and no post-rotation independence is asserted.

## 8. Concrete half-volume threshold: 131+131 coordinates

Assume each carrier Pluecker law places at least half its mass on the retained support:

`rho_L>=1/2`, `rho_R>=1/2`.                                    (8.1)

Then `sqrt(rho_L rho_R)>=1/2`, so

`Gamma_m >= [sqrt(Z0/3)/2]/(m/8+eps0)
             -eps0-(m-1)/8-h/128`.                             (8.2)

The right side decreases for positive integer m in the relevant range. At `m=131`,

`boxed: Gamma_131>0.04131120978916627`,                         (8.3)

and therefore

`boxed:
s_4(A_HH)>sigma_core,
 sigma_core=4.802356499645993e-8.`                              (8.4)

The same crude estimate is negative at `m=132`, so this report claims 131, not 132.

Thus the entire half-Pluecker-support branch produces an actual principal core on at most

`|H|<=262`                                                      (8.5)

ORIGINAL coordinates with four substantial eigenvalues.

Condition on all original coordinates outside H. Independence and the cap-one laws on H are unchanged, and every outside interaction becomes an arbitrary deterministic affine term. Apply the completed finite-dimensional projected-gradient theorem at

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,
`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1:

on d original coordinates, three actual eigenvalues of modulus at least sigma imply

`||p_q||_infinity <=2 sqrt(6 pi d)/sigma`.                      (8.6)

With `d<=262` and (8.4),

`boxed:
||p_Q||_infinity <2.927e9`                                     (8.7)

on the branch (8.1). The constant is deliberately unoptimized. The conclusion is an essential density bound; this report does not add a continuity claim.

This closes a substantially larger bounded-support carrier branch than the earlier direct aggregate-E2 support estimate, because it spends the one-third two-heavy singular-pair mass before distributing over physical coordinate minors.

## 9. Exact diffuse two-frame regression: bounded-core extraction still cannot be universal

The complement of Theorem 7.1 is real. The newest correction ledger already warns that diffuse two-frame families defeat stronger hub/star forcing; the following exact calculation is used only as a regression for the present Pluecker support statement, not claimed as a new full-QFORM counterexample.

Take even N. Let

`u_+(i)=1/sqrt(N)`,
`u_-(i)=eps_i/sqrt(N)`,                                        (9.1)

where exactly N/2 signs eps_i are +1 and N/2 are -1. Let U=[u_+,u_-] and take V to be another such flat orthonormal two-frame on a disjoint N-coordinate bank. Define

`K_N=U V^T`,
`A_N=[[0,K_N],[K_N^T,0]]`.                                     (9.2)

Then K_N has singular values exactly 1,1 and no others, so

`spec_nonzero(A_N)={1,1,-1,-1}`.                               (9.3)

This is a genuine target-class family.

Its second compound is

`e_2(K_N K_N^T)=1`,                                             (9.4)

its singular-index pair law is concentrated on the unique pair and therefore both spectral marginals equal one, and its r35 low-E3 tail is exactly zero.

For a physical row pair `{i,j}`,

`det U[{i,j},:]=(eps_j-eps_i)/N`.                               (9.5)

Thus the squared Pluecker weight is `4/N^2` for opposite-sign pairs and zero otherwise. There are `N^2/4` opposite-sign pairs, so the weights sum to one. If a support R has m coordinates, writing a,b for its two sign counts,

`rho_L(R)=4ab/N^2<=m^2/N^2`.                                  (9.6)

The same holds on the V side. In particular no fixed-cardinality support carries half the Pluecker area as `N->infinity`.

Every entry of K_N has magnitude at most `2/N`. Hence for every physical principal block with at most M coordinates,

`||A_N[H,H]||_op<=M/N ->0`                                     (9.7)

(up to the harmless sharper factor obtained from the row/column split). Thus no bounded physical principal core has three eigenvalues bounded away from zero.

For sufficiently large N the physical off-diagonal and principal-pair bounds also lie inside the same strict-N3 chamber. Therefore a zero-tail rank-two interface with the entire E2 volume in two singular directions may still be maximally physical-support-diffuse. This refutes only the stronger bounded-core shortcut, not QFORM.

## 10. Required pinned e5 theorem pays the exact fully diffuse regression

For A_N in Section 9, the four-dimensional range projection has physical coordinate leverage exactly `2/N` on each side. For `N>=4` this is at most `1/2`.

Apply the completed rank-r Fresnel--Brascamp--Lieb theorem from the required pinned e5 `FOURIER_ROUTE_REPORT.md` to the rank-four form A_N. Its four nonzero eigenvalues have absolute value one, so

`boxed:
|phi_Q(t)| <= min(1,16 pi^2 |t|^-2).`                           (10.1)

Integrating the envelope,

`int_R min(1,16 pi^2 t^-2) dt=16 pi`,                          (10.2)

and Fourier inversion gives

`boxed: ||p_Q||_infinity<=8.`                                  (10.3)

This is a real application of a completed theorem from the mandated e5 source to the exact obstruction identified in Section 9. It uses product structure in the original coordinates and does not rotate the random variables into independence.

## 11. A second exact survivor: one physical Pluecker coloop plus one diffuse direction

Support-diffuse Pluecker mass is not synonymous with uniformly low coordinate leverage. There is a second exact endpoint which matters for the next receiver.

Let the left bank consist of one hub coordinate h and N leaves. Define the left two-frame

`u_1=e_h`,
`u_2=N^(-1/2) 1_(leaves)`.                                     (11.1)

Let V=[v_1,v_2] be the flat constant/alternating orthonormal frame on a disjoint N-coordinate right bank, and again set

`K_N=U V^T`, `A_N=[[0,K_N],[K_N^T,0]]`.                         (11.2)

The spectrum is again exactly (9.3), and the interface tail is zero. But the left Pluecker law is now

`w({h,i})=1/N` for each leaf i,
`w(S)=0` otherwise.                                             (11.3)

Thus h is a literal physical coloop: its Pluecker inclusion marginal is one. Nevertheless any support consisting of h and at most m-1 leaves captures only

`rho_L=(m-1)/N`,                                                (11.4)

so bounded carrier support still fails.

The largest physical coefficient is `N^-1/2` (on the hub row); all bounded principal blocks nevertheless have operator norm tending to zero, because a block with p leaf/hub rows and q right columns has carrier norm bounded by

`sqrt(q/N)+sqrt((p-1)q)/N ->0`                                  (11.5)

for fixed p,q. For sufficiently large N this family also lies in strict N3.

This exact endpoint shows why the remaining rank-two Pluecker-diffuse branch must itself allow an anchored/coloop geometry; a proof that replaces support diffusion by the condition `max_i ||U_i||^2<=1/2` would miss a genuine target-class configuration.

## 12. The pinned e5 mixed-hub theorem pays the exact coloop regression

The one-coloop family is also not a QFORM counterexample. Take the physical hub set `H={h}`. On the remaining original coordinates, the light quadratic block has exact rank two with orthonormal eigenvectors

`w_+=(u_2+v_2)/sqrt(2)`,
`w_-=(u_2-v_2)/sqrt(2)`,                                       (12.1)

and eigenvalues +1 and -1. The hub coupling vector is v_1. The three columns

`w_+, w_-, v_1`                                                 (12.2)

are orthonormal on the nonhub coordinate space. Their physical row leverages are `1/N` on each leaf and `2/N` on each right coordinate, hence at most 1/2 for `N>=4`.

Apply the completed mixed-hub theorem H from the pinned e5 source with `|H|=1`, `r=2`, determinant Gram equal to one, and `|lambda_1 lambda_2|=1`. Its stated characteristic-function constant specializes to

`boxed:
|phi_Q(t)|<=min(1,8 pi^2 |t|^-2).`                              (12.3)

Therefore

`boxed:
||p_Q||_infinity<=4 sqrt(2)<5.657.`                             (12.4)

Again the tail-zero endpoint is paid for the correct product-structure reason. The open issue is uniformity when the r35 nonzero rough interface tail is restored; one may not treat its tiny Frobenius norm as a tiny random perturbation because no moments or support bounds exist.

## 13. What this changes in the proof map

Partner r35 reduced its aggregate-E2 state to an E3-paid branch or a rank-at-most-two interface tube. The present theorem resolves a concrete, substantially larger part of that tube:

1. If r35's heavy compound projection has rank two and the left and right rank-two carrier Pluecker laws each put at least half their area on at most 131 physical coordinates, then an ACTUAL principal block on at most 262 original coordinates has four eigenvalues of modulus at least `4.8023565e-8`, and the full ambient form has the universal essential density bound (8.7).

2. If that branch fails, no assertion about a single good minor is made. Either the compound carrier has rank at most one, or at least one rank-two carrier Pluecker law is support-diffuse at the explicit half-area/131-coordinate scale.

3. The flat two-frame and one-coloop families prove that both completely diffuse and anchored-diffuse zero-tail geometries are genuine target-class endpoints with no bounded physical spectral core.

4. The mandated pinned e5 Fourier theorems pay both exact endpoints, with bounds 8 and `4sqrt(2)` respectively. Hence the remaining obstruction is not the exact rank-two carrier itself; it is the dependence-safe reattachment of the true nonzero rough tail while arbitrary same-bank curvature remains.

This is consistent with the current owner continuation's warning that the conditional-adaptation step `(SP)` is still open. The result here does not smuggle in `(SP)` by conditioning on a rotated complement.

## 14. Verification and boundary of the claim

The algebraic identities used above are exact:

- singular pair inclusion-exclusion gives (3.1);
- rank-two physical minor factorization gives (5.3);
- the r35 Frobenius tail is used only as a deterministic operator perturbation on the finite physical core;
- same-side curvature is retained in A_HH and bounded there by the actual strict-N3 coefficient cap;
- conditioning occurs only outside a set of ORIGINAL coordinates after the actual spectral core has already been certified.

A numerical regression independently checked the identity

`e_2(U_R diag(s)^2? restricted carrier)= (s1 s2)^2 det(U_R^T U_R)det(V_C^T V_C)`

on 100 random orthonormal two-frames to machine precision (`2.3e-15` maximum absolute error). This is a regression check only; the proof is Cauchy--Binet above.

The numerical constants are

`h=1.1624826588606455e-6`,
`eps0=0.0032450450393877377`,
`sqrt(Z0/3)=533.7524707810138`,
`Gamma_131=0.04131120978916627`,
`sigma_core=4.802356499645993e-8`,
`2sqrt(6pi*262)/sigma_core=2.926690557543719e9`.

The same crude formula gives `Gamma_132<0`, so the report does not claim 132.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.**
