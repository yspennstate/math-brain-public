SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T09:06:05Z.
attacking: dense nonseparable Schur-bank localization—keep whole active product banks intact through curvature/volume payment, then condition only outside original coordinates; test whether high-leverage cancellation can be absorbed without support or moment assumptions.

# QFORM B14 r32 — critical Fourier-to-log localization and diffuse rank-two Schur banks

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** 20260923T090605Z-fleet02-B14-QFORM-r32  
**Status:** NEW SUPPORTING THEOREM + TARGET-VALID PROOF-INTERFACE OBSTRUCTION; FULL QFORM OPEN.  
**Continuity:** separate; not claimed for the full rough-law conclusion.  
**Execution:** WITHOUT_VERIFIED_BRAIN.

## 1. Exact target and first unpaid implication

The target remains: for arbitrary independent real coordinates with marginal densities at most one and every real symmetric A with at least three eigenvalues of modulus at least one, prove one universal essential density bound for X^T A X, or produce a valid counterexample. No moment, bounded-support, connected-support, finite-fragment, log-concavity, post-rotation independence, or continuity hypothesis is available.

This run attacks the first unpaid localization interface after a Schur reduction. A rank-two residual phase naturally gives only critical |t|^{-1} Fourier decay. That is not L1, so direct Fourier inversion fails. The question is whether the same critical decay can nevertheless be passed through the logarithmic physical-pair kernel, uniformly under arbitrary conditioning-generated affine terms and arbitrary fragmented/unbounded laws.

The answer is yes. The resulting compiler also closes a diffuse part of the kernel-affine gap left explicitly open by the designated partner fleet03/B14 r31.

## 2. Sources actually applied

### 2.1 Newest Claude result

The required source family is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed result used at the decisive inequality is the general-rank form of **Theorem F (Fresnel–Brascamp–Lieb)** from `FOURIER_ROUTE_REPORT.md`:

if

A_active = Delta + R Lambda R^T,

where Delta is any original-coordinate diagonal matrix, R has orthonormal columns, the rank-r frame has coordinate leverage at most 1/2, and arbitrary linear terms are present, then

|phi(t)| <= (4 pi)^(r/2) |t|^(-r/2) prod_k |lambda_k|^(-1/2).

For r=2 this is the critical bound

|phi(t)| <= 4 pi |t|^(-1) |lambda_1 lambda_2|^(-1/2).        (2.1)

The source explicitly allows arbitrary diagonal and linear twists; no rotated input variables are asserted independent.

### 2.2 Designated partner fleet03/B14 r31

The compatible completed partner result is

`QFORM-RANK2-SEMIDEFINITE-SCHUR-BANK-v1`,
canonical report
`yspennstate/math-open-problems@1d80c85a03f6d442c7771e0df3313ec80aab8446`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T083627Z-fleet03-B14-QFORM-r31/REPORT.md`.

It proves that after an invertible indefinite physical pair B, a rank-two semidefinite Schur bank is paid with zero support/fragment/moment tax when the conditioning-generated bank affine term lies in the range of that bank curvature. It also uses the completed physical-pair logarithmic envelope

p_Q(t) <= 2 sqrt(2)/r
          + D^(-1/2) E log_+(2r^2/(kappa |t-R|)),             (2.2)

where D=|det B| and kappa=sigma_min(B). Partner r31 explicitly records the kernel-affine component as unpaid.

The physical-pair envelope itself is source-pinned in the pair-log line of work, including the arbitrary-rank extension at
`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

## 3. New lemma: critical Fourier decay gives uniform logarithmic potential

### Lemma — `QFORM-CRITICAL-FOURIER-LOG-POTENTIAL-v1`

Let Y be a real random variable. Suppose that for some K>0,

|phi_Y(t)| <= min{1,K/|t|},       t != 0.                         (3.1)

Set

m0 := (sin(1/2)/(1/2))^2 = 4 sin^2(1/2),

c_E := 2/m0 = 1/[2 sin^2(1/2)] = 2.175342649670021... .          (3.2)

Then for every x in R and every rho>0 with K rho<=1,

P{|Y-x|<=rho}
 <= c_E K rho [1+log(1/(K rho))].                                (3.3)

Consequently, for every A>0,

sup_x E log_+(A/|Y-x|) <= Omega(KA),                              (3.4)

where

Omega(y) = c_E y [2+log(1/y)],    0<y<=1,
           log y + 2 c_E,         y>=1.                            (3.5)

The two formulas agree at y=1.

### Proof

For rho>0 define

k_rho(u) := [ sin(u/(2rho)) / (u/(2rho)) ]^2.                      (3.6)

On |u|<=rho, |u/(2rho)|<=1/2, hence k_rho(u)>=m0. Under the convention

hat f(t)=int exp(i t u) f(u) du,

the exact Fourier transform is the triangular function

hat k_rho(t)=2 pi rho (1-rho|t|)_+.                                (3.7)

Therefore

P{|Y-x|<=rho}
 <= m0^(-1) E k_rho(Y-x)
 <= m0^(-1) rho int_{-1/rho}^{1/rho} |phi_Y(t)| dt.                (3.8)

If K rho<=1, then 1/rho>=K, so (3.1) gives

int_{-1/rho}^{1/rho}|phi_Y(t)|dt
 <= 2K [1+log(1/(K rho))].                                        (3.9)

Equations (3.2), (3.8), (3.9) prove (3.3). The trivial probability bound one is retained outside this range.

For the logarithmic potential use layer cake:

E log_+(A/|Y-x|)
 = int_0^infinity P{|Y-x|<A e^(-s)} ds.                            (3.10)

Write y=KA. If y<=1, substitute (3.3) for every s>=0:

(3.10)
 <= c_E y int_0^infinity e^(-s)
       [1+log(1/y)+s] ds
 = c_E y [2+log(1/y)].                                             (3.11)

If y>=1, use the trivial bound one on 0<=s<=log y. On writing s=log y+u in the tail, K A e^(-s)=e^(-u), and (3.3) gives

(3.10)
 <= log y + c_E int_0^infinity e^(-u)(1+u)du
 = log y+2c_E.                                                      (3.12)

This proves the lemma. No density, moment, support, or continuity assumption on Y is used.

## 4. Localization compiler through an indefinite physical pair

### Theorem — `QFORM-CRITICAL-FOURIER-LOG-LOCALIZATION-v1`

Split the original independent coordinates as X=(U,V,Z), with U in R^2. Let the physical pair block B=A_UU be invertible and indefinite, and put

D=|det B|,
kappa=sigma_min(B).                                                 (4.1)

Complete the pair exactly. Condition only on the outside ORIGINAL coordinates Z=z, leaving the active bank V as a genuine cap-one product law. Suppose the conditional remainder R_z(V) satisfies, uniformly in z and in all induced affine terms,

|phi_{R_z}(t)| <= min{1,K/|t|}.                                    (4.2)

Then the full form has an essentially bounded density and

||p_Q||_infinity
 <= inf_{y>0}
    { 4 sqrt[K/(kappa y)] + D^(-1/2) Omega(y) },                   (4.3)

with Omega from (3.5). In particular the choice y=1 gives

||p_Q||_infinity
 <= 4 sqrt(K/kappa) + [sin(1/2)]^(-2) D^(-1/2).                   (4.4)

### Proof

Lemma (3.4) applies to each conditional remainder with the same K. Hence for every center t and A>0,

E[log_+(A/|t-R|) | Z=z] <= Omega(KA)                               (4.5)

uniformly in z. Averaging preserves (4.5). Insert A=2r^2/kappa into the partner physical-pair envelope (2.2):

||p_Q||_infinity
 <= 2sqrt(2)/r + D^(-1/2) Omega(2K r^2/kappa).                     (4.6)

Set y=2K r^2/kappa. Then

2sqrt(2)/r = 4 sqrt[K/(kappa y)],                                  (4.7)

which proves (4.3). At y=1, 2c_E=[sin(1/2)]^(-2), proving (4.4).

This is a localization principle in the required sense: arbitrary outside coordinates may be conditioned, their induced affine terms may be arbitrarily large, and their laws may have arbitrary distant fragments or unbounded supports. Only a uniform whole-active conditional Fourier envelope is required; no active-coordinate normalization or support truncation occurs before reciprocal payment.

## 5. Apply Claude Theorem F: diffuse rank-two Schur curvature of either sign

### Theorem — `QFORM-DIFFUSE-RANK2-SCHUR-AFFINE-v1`

In the setting of Section 4, suppose the V-Schur block has the whole-bank decomposition

S_VV = Delta + lambda_1 a a^T + lambda_2 b b^T,                    (5.1)

where

- Delta is an arbitrary ORIGINAL-coordinate diagonal matrix;
- a,b are orthonormal vectors in the V-coordinate space;
- lambda_1 lambda_2 != 0, with arbitrary signs;
- the rank-two frame has leverage

  max_i (a_i^2+b_i^2) <= 1/2.                                     (5.2)

All outside couplings S_VZ and every affine perturbation are arbitrary. Put

P=|lambda_1 lambda_2|.                                              (5.3)

Then

||p_Q||_infinity
 <= inf_{y>0}
    { 8 sqrt(pi) kappa^(-1/2) P^(-1/4) y^(-1/2)
      + D^(-1/2) Omega(y) },                                       (5.4)

and therefore

boxed{
||p_Q||_infinity
 <= 8 sqrt(pi) kappa^(-1/2) P^(-1/4)
    + [sin(1/2)]^(-2) D^(-1/2).
}                                                                  (5.5)

Numerically,

8 sqrt(pi)=14.1796308072441...,
[sin(1/2)]^(-2)=4.35068529934004... .                              (5.6)

The theorem is uniform in dimension, the entire diagonal twist Delta, all outside couplings, all conditioning-generated affine terms, translations, support locations/diameters, fragment count/separation, tails, and moments.

### Proof

After conditioning on Z=z, the remainder is

R_z(V)=V^T S_VV V+q(z)^T V+d(z),                                  (5.7)

where q(z)=2S_VZ z+g_V may point in ANY direction, including the kernel of the rank-two component in (5.1).

Apply the required newest-Claude Theorem F at rank r=2 to the whole product bank V. The diagonal Delta and the arbitrary q(z) are exactly the allowed diagonal and linear twists. Because a,b are orthonormal and (5.2) is the Theorem-F leverage gate,

|phi_{R_z}(t)|
 <= min{1, 4 pi P^(-1/2) |t|^(-1)}                                (5.8)

uniformly in z. Thus Section 4 applies with

K=4 pi/sqrt(P).                                                     (5.9)

Substitution into (4.3)--(4.4) gives (5.4)--(5.5).

No spectral rotation of V is performed on the probability law: a,b occur only as deterministic phase coefficients inside Theorem F, whose proof keeps the original-coordinate product factorization.

## 6. Exact relation to the designated partner result

Partner fleet03/B14 r31 and Theorem (5.5) are complementary rather than duplicates.

Partner r31 covers a rank-two semidefinite Schur bank **without any leverage restriction**, but it requires every conditioning-generated bank affine vector to lie in Range(S0). It then gets the sharper two-dimensional projection-density route and an optimized piecewise pair-log constant.

The present theorem covers a diffuse rank-two component of **either sign**, permits an arbitrary diagonal twist, and permits completely arbitrary affine vectors q(z), including kernel leakage, but requires leverage <=1/2. Thus it pays a genuine portion of the exact gap identified by r31.

For a semidefinite diffuse bank satisfying both hypotheses, r31 is preferable when q(z) is range-compatible. When q(z) has a kernel component, (5.5) remains available whereas the r31 range-translation step is unavailable.

## 7. Target-valid kernel-leakage stress outside the partner range condition

Fix m>=2. Let a_m,b_m,c_m be three mutually orthonormal block-constant vectors on three disjoint m-coordinate banks:

a_m=m^(-1/2)(1,...,1,0,...,0,0,...,0),

b_m=m^(-1/2)(0,...,0,1,...,1,0,...,0),

c_m=m^(-1/2)(0,...,0,0,...,0,1,...,1).

Take an original physical pair U=(U_1,U_2), an outside scalar Z, and the homogeneous form

Q_m,gamma
 = 2 U_1 U_2
   +(a_m^T V)^2 +(b_m^T V)^2
   +2 gamma (c_m^T V) Z.                                          (7.1)

The physical pair has B=[[0,1],[1,0]], hence D=kappa=1. The V-Schur curvature is

S0=a_m a_m^T+b_m b_m^T,                                            (7.2)

so P=1 and its leverage is 1/m<=1/2. Conditioning on Z=z produces the bank affine vector

q(z)=2 gamma z c_m,                                                 (7.3)

which lies in Ker(S0), not Range(S0), whenever gamma z!=0. Thus the partner r31 range hypothesis fails on the generic fiber.

Nevertheless Theorem (5.5) gives for arbitrary cap-one product laws

||p_Q||_infinity
 <= 8 sqrt(pi)+[sin(1/2)]^(-2)
 = 18.5303161065842...                                              (7.4)

uniformly in m and gamma.

This is an exact-target family. The homogeneous coefficient matrix decomposes orthogonally into the physical hyperbolic pair, +1 on a_m, +1 on b_m, and the c_m--Z cross pair [[0,gamma],[gamma,0]]. Hence its nonzero spectrum is

{1,-1,1,1,|gamma|,-|gamma|}                                        (7.5)

(up to omission of the last pair when gamma=0). In particular at least four eigenvalues have modulus at least one regardless of gamma. Every individual coefficient in the two diffuse square banks tends to zero as m grows, while the bound (7.4) stays fixed.

## 8. Source-valid obstruction: L1 Fourier integrability of a rank-two remainder is too strong

### `QFORM-REMAINDER-L1-FOURIER-TOO-STRONG-v1`

Let X_1,...,X_4 be iid Uniform[-1/2,1/2] and

Q=2X_1X_2+2X_3X_4.                                                  (8.1)

The coefficient matrix is diag([[0,1],[1,0]],[[0,1],[1,0]]), with spectrum {1,-1,1,-1}; it is fully inside the exact target.

For one pair R=2X_1X_2, direct integration gives

p_R(r)=log(1/(2|r|)) 1_{|r|<1/2},                                  (8.2)

so p_R is logarithmically unbounded. Its characteristic function is

phi_R(t)=2 Si(t/2)/t,                                               (8.3)

and therefore

phi_R(t) ~ pi/t                                                     (8.4)

as |t|->infinity. Consequently

int_R |phi_R(t)|dt = infinity.                                     (8.5)

Thus any proof interface requiring the rank-two Schur remainder itself to have an L1 characteristic function, or a bounded density obtained from absolute Fourier inversion, already fails on a legal target input.

But the full Q is harmless. Equation (8.2) gives

||p_R||_2^2
 =2 int_0^(1/2) log^2(1/(2r))dr
 =int_0^1 log^2(1/u)du
 =2.                                                               (8.6)

Hence Young/Cauchy--Schwarz gives

||p_Q||_infinity=||p_R*p_R||_infinity <=||p_R||_2^2=2.             (8.7)

This is not a counterexample to QFORM. It is a counterexample to the proof demand that every critical rank-two remainder first become L1-Fourier/bounded-density before the extra smoothing direction is used. The correct interface can remain at critical |t|^{-1}, convert it to rho log(1/rho) concentration, and only then pay the logarithmic or square kernel.

## 9. Localization / mixture interpretation

The proof order is now explicit:

1. keep the active original-coordinate product bank intact;
2. prove a whole-bank critical Fourier envelope uniformly in every affine term;
3. convert that envelope to a translation-uniform rho log(1/rho) small-ball estimate by the squared-sinc lemma;
4. integrate the logarithmic physical-pair kernel;
5. only then average over outside original-coordinate conditioning and arbitrary mixtures/fragments.

No active marginal is normalized after conditioning, no bounded-diameter replacement is made, and no reciprocal fragment scale is introduced. Since every estimate is already uniform over all cap-one product laws, finite-fragment approximation is optional rather than a hidden hypothesis; the same constant survives any valid total-variation finite-mixture compiler.

This ordering is compatible with the existing B14 fragmentation barriers: active fragmentation before reciprocal/volume payment can create N^2 losses, whereas outside conditioning after the whole-active certificate costs zero.

## 10. Relation to the already-completed arbitrary-rank pair theorem

The arbitrary-rank physical-pair theorem at commit 742ac943... already proves a density bound whenever the full target s_3(A)>=s and an indefinite physical pair has quantitative D,kappa, using a generic quarter-power small-ball estimate for the entire Schur complement. The present result is not claimed to replace that theorem.

Its additional information is a **scale-sensitive critical interface**: it exposes the rank-two whole-bank volume P and allows one to optimize (5.4) jointly against D and kappa, while preserving arbitrary affine leakage and diagonal twists. It also proves that critical |t|^{-1} decay, although insufficient for direct inversion, is analytically sufficient for the pair-log layer. This is the useful interface for near-pivot structural arguments in which D,kappa may be small but aggregate Schur curvature becomes large.

## 11. First unpaid implication after this run

`QFORM-HIGH-LEVERAGE-RANK2-OR-WHOLE-VOLUME-EXIT-v1`:

In every surviving N3/no-pivot configuration, after any useful scalar/pair Schur reduction, prove one of the following *before active-law fragmentation*:

1. a rank-two low-rank-plus-diagonal Schur component with leverage <=1/2, so Theorem (5.4) applies;
2. a partner-r31 semidefinite range-compatible bank;
3. a whole-law D'/D5/mixed-hub/ridge/bank certificate from the completed source results; or
4. a bounded high-leverage original-coordinate core whose critical remainder admits a uniform |t|^{-1} or rho log(1/rho) estimate with all conditioning-generated affine terms retained.

For a rank-two orthonormal frame the leverage scores sum to two, so there are at most three coordinates with leverage strictly larger than 1/2. The unresolved issue is not their cardinality but preserving enough aggregate curvature after isolating them without replacing the remaining product bank by a rotated conditional law.

A successful structural bridge must not normalize thin fragments first, treat a small matrix coefficient as a small random perturbation on unbounded inputs, or infer independence after rotation.

## 12. Scope / correction ledger

Consumed corrections include: law-uniform scalar pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive moments of worst conditional projection-density caps can diverge; post-rotation independence is unavailable; bounded-diameter and fixed-fragment localization are false; a universally good physical minor/cross-rank-three cut is not forced; and active-fragment-first reciprocal volume estimates incur genuine losses.

The newest Claude `COUNTEREXAMPLE_SEARCH.md` reports no QFORM counterexample and identifies delocalized/high-dimensional structure as the remaining plausible hiding place; its numerical evidence is not used as proof here. The theorem above uses only the proved Theorem-F inequality.

Full QFORM remains OPEN. No continuity statement is inferred from the rough-law localization argument.
