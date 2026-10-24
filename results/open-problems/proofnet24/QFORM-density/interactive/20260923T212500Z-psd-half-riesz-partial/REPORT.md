# Arbitrary-rank PSD half-Riesz theorem and two sharper special cases

Status: the all-target positive-semidefinite half-Riesz theorem is proved in the archived assembled manuscript. The signed indefinite QFORM/RMT density conjecture remains open.

Let X have independent real coordinates with densities bounded by one. Let B be positive semidefinite with its second largest eigenvalue lambda_2(B) at least sigma>0. Let Q=X^TBX+d·X+c, with arbitrary affine coefficients.

## The full all-target PSD statement

For every dimension, rank, product input law, affine term, and target s,

sup_s E|Q-s|^(-1/2)
 ≤ C_PSD/sqrt(sigma),

where the explicit source constant is

K_1=4sqrt(128),
K_2=4sqrt(600)K_1,
C_PSD=3sqrt(K_2(3+log K_2))<675.

This follows from Proposition sd:psd-levels(2) and the layer-cake calculation in Lemma sd:composition(3) of the archived assembled manuscript:

https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/semidefinite.tex

For lambda_2(B)≥1, the proposition proves the uniform near-linear logarithmic concentration estimate

P(|Q-s|≤u)≤K_2 u(1+log(1/u)), 0<u≤1.

For V≥1, layer cake then gives

E|Q-s|^(-1/2)
 ≤V+K_2∫_V^infinity t^(-2)(1+2log t)dt
 =V+K_2(3+2log V)/V.

Choosing V=sqrt(K_2(3+log K_2)) yields at most 3V. Dividing Q by sigma and scaling the half-power kernel gives the displayed sigma^(-1/2) bound.

The manuscript proves the concentration proposition by a physical-positive-pivot or diffuse-Gram-partition dichotomy. In the pivot case, the PSD Schur complement keeps one eigenvalue at least one and the first-level square-root concentration bound composes with the conditional square density. In the diffuse case, a volume-weighted random Gram partition gives an integrable-in-frequency k=2 bound; a Fejér kernel converts that into the logarithmic concentration estimate. The manuscript supplies the partition, ridge-leverage, and Fourier details and allows arbitrary original-coordinate affine terms.

The same manuscript proves the stronger three-eigenvalue density theorem
||p_Q||_infinity≤17100/lambda_3(B)
when lambda_3(B)>0, again with arbitrary rank and affine term. These PSD results do not settle the indefinite signed-spectrum theorem.

## 1. Sharper bound below the quadratic minimum

Assume d∈range(B). Put x_0=(1/2)B^+d and m=c-(1/4)d^TB^+d. Then

Q=m+(X+x_0)^TB(X+x_0).

For every s≤m,

E|Q-s|^(-1/2) ≤ 2sqrt(2pi)/sqrt(sigma).

Proof. Choose an orthonormal two-frame U for the top two eigendirections of B. Positive semidefiniteness gives
Q-m≥sigma |U^T(X+x_0)|².
The two-dimensional orthogonal projection Y=U^T(X+x_0) has a density bounded by two, by the dimension-two projection-density theorem for independent cap-one coordinates. Consequently, for s≤m,
|Q-s|^(-1/2)≤sigma^(-1/2)|Y|^(-1).
Among probability densities on R² bounded by two, the integral of |y|^(-1) is maximized by density two on the centered disk of area 1/2. This gives E|Y|^(-1)≤2sqrt(2pi).

This special-case constant is much smaller than C_PSD. If d has a component in ker(B), a finite quadratic minimum need not exist, but the full all-target theorem above still applies.

## 2. Sharper bound from a physical definite pair

Suppose there are physical original indices i,j such that the principal 2 by 2 block B_{I,I}, I={i,j}, has determinant at least delta²>0. Then, for arbitrary d and all s,

E|Q-s|^(-1/2) ≤ 2sqrt(2pi/delta).

Proof. Condition all other original coordinates. The remaining quadratic in (X_i,X_j) has the same positive-definite Hessian B_{I,I}, with arbitrary induced affine coefficients and a target shift. Completing the square and polar coarea show that its conditional scalar density is at most pi/sqrt(det B_{I,I})≤pi/delta. A scalar probability density capped by M has half-Riesz potential at most 2sqrt(2M), by placing density M on the interval of length 1/M centered at the target. Take M=pi/delta and average the conditional estimate.

This also handles arbitrary rank and cross couplings. Diffuse rank-two PSD matrices need not have a physical pair with determinant bounded below, so the Gram-partition part of the full theorem is substantive.

## 3. Schur structure and a shortcut obstruction

For a physical positive pivot a=B_ii>0, write
B=[[a,w^T],[w,D]]
and S=D-ww^T/a≥0. After completing the square in X_i, the conditional density at target s is bounded by

a^(-1/2) E[1_{R<s}(s-R)^(-1/2)],

where R is the Schur quadratic with arbitrary induced affine terms. The side indicator is useful: for a rank-one square R=Y², the two-sided potential E|R|^(-1/2)=E|Y|^(-1) can diverge, while
sup_s E[1_{Y²<s}(s-Y²)^(-1/2)]
is at most pi times the density cap of Y.

The exact rank-one Loewner decomposition
B=diag(0,S)+a[1;w/a][1;w/a]^T
implies lambda_2(B)≤lambda_1(S). The archived manuscript controls the Schur center through its first concentration level and the square-root profile; it does not replace R by an independent spectral truncation.

A top-two planar density cap by itself cannot justify a higher-rank extension. For an arbitrary joint law of (Y,R), one could take Y uniform on a disk and R=s-|Y|²≥0 there, making |Y|²+R constant. This is only a method obstruction: it is not a counterexample with independent originals and a PSD quadratic tail. The archived Gram-partition proof retains exactly that missing product and quadratic structure.

The earlier version of this report incorrectly called the all-target arbitrary-rank PSD half-Riesz statement open. The theorem above corrects that status. Only the unrestricted indefinite QFORM/RMT target remains open.
