SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T18:51:49Z.
attacking: a two-large-eigenvalue L3 ridge bridge and scalar-pivot Schur closure for the full matrix.

# account03/B16 QFORM r15 — fractional ridge-to-pivot bridge

Status: SUPPORTING THEOREMS PROVED; FULL QFORM OPEN / NOT PROVED. Continuity is proved only in the pre-existing L-infinity ridge branch, not by the new L3-to-square bridge below. Execution memory: WITHOUT_VERIFIED_BRAIN.


This run deliberately changes mechanism after the preceding B16 pivot/pair runs: it uses a fractional Fourier L3 bridge from the completed ridge theorem, then closes one physical square while retaining dependence.

## 1. Input theorem used exactly

Use the completed ridge theorem from

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7:proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an original-coordinate cross block B and gamma>0 define

K = BB^T (gamma^2 I+BB^T)^(-1),
theta = tr K,
D = det(I+BB^T/gamma^2).

For 1<=q<=2, if max_i K_ii<=q/2, the proof gives the characteristic-function envelope

|phi(t)| <= min(1,(t0/|t|)^beta),

where

beta = theta/(2q),
t0 = L_q/(2 gamma) D^(-1/(2 theta)),
L_q = pi e sqrt(2/q).

The proof is joint in the original product coordinates and permits arbitrary self blocks, outside couplings, and coordinate-separable measurable perturbations. No rotated independence is asserted.

## 2. New theorem: ridge L^r density from a sub-L1 Fourier exponent

### Theorem QFORM-RIDGE-LR-v1

Let 2<=r<=infinity and put s=r/(r-1) in [1,2]. Under the preceding ridge hypotheses, assume

theta s > 2q.

Then the output law has a density p in L^r and

||p||_r <= (2pi)^(-1/s) C_s
          [ (L_q/gamma) D^(-1/(2theta))
            * theta s/(theta s-2q) ]^(1/s),                 (2.1)

where

C_s = s^(1/(2s)) / (s')^(1/(2s')),

with s'=r, is the sharp Beckner Hausdorff-Young constant in the Fourier convention hat f(t)=int e^{itx}f(x)dx.

### Proof

The ridge theorem gives |phi(t)|<=min(1,(t0/|t|)^beta). Since beta s>1,

int_R |phi(t)|^s dt
 <= 2 t0 + 2 int_{t0}^infinity (t0/t)^(beta s) dt
 = 2 t0 * beta s/(beta s-1)
 = (L_q/gamma) D^(-1/(2theta)) * theta s/(theta s-2q).       (2.2)

Because phi is in L^s, inverse Hausdorff-Young gives an L^r density and

||p||_r <= (2pi)^(-1/s) C_s ||phi||_s,

which is (2.1). At r=infinity, s=1, this specializes exactly to the completed ridge L-infinity estimate, so the normalization is consistent. QED.

The point is that theta need not exceed 2q. For L3 it is enough that theta>4q/3. This avoids the universally false demand phi in L1.

## 3. New theorem: two large diffuse eigenvalues already give an L3 density

### Theorem QFORM-TWO-EIG-SPECTRAL-WINDOW-L3-v1

Let S be any real symmetric matrix. Suppose S has at least two eigenvalues of absolute value at least a>0. Let P be the spectral projection onto all eigenspaces of S with |lambda|>=a/64, and suppose

max_i P_ii <= 1/32.                                           (3.1)

For independent real input coordinates with probability densities bounded by one, and even after adding arbitrary real coordinate-separable measurable terms finite almost surely, the output R has an L3 density satisfying

||p_R||_3 <= C_3 a^(-2/3),                                  (3.2)

where

C_3 = C_(3/2) [144 sqrt(12e)/13]^(2/3)
    = 15.1338077639... < 15.14.                              (3.3)

### Proof

Scale first to a=1. Apply the same two-part MSS frame partition used in the completed spectral-window theorem to the high spectral frame. If I,J are the resulting original-coordinate blocks, the two restricted Gram matrices lie between 7I/32 and 25I/32. For the high spectral cross block B0 this implies

s_2(B0)>=7/32,

because only two high singular directions are needed here. The omitted low spectral tail has operator norm at most 1/64, hence for the full cross block B,

s_2(B)>=7/32-1/64=13/64.                                    (3.4)

Also range(B0)=range(U_I), and the projection diagonal onto this range is at most

(1/32)/(7/32)=1/7.                                          (3.5)

Set

gamma = 13/(64 sqrt 6).

The completed ridge perturbation lemma therefore gives

max_i K_ii <= (1/sqrt7 + sqrt6/13)^2 < 1/2.                 (3.6)

The two singular values in (3.4) each contribute at least 6/7 to theta, so

theta >= 12/7.                                               (3.7)

Take q=1 and r=3, hence s=3/2. The new threshold is

theta s >= 18/7 > 2,

so Theorem 2 applies. The elementary inequality log D>=theta gives D^(-1/(2theta))<=e^(-1/2), and theta s/(theta s-2) is decreasing in theta; at theta=12/7 it equals 9/2. Thus

||p_R||_3
 <= (2pi)^(-2/3) C_(3/2)
    [ (pi e sqrt2/gamma) e^(-1/2) * 9/2 ]^(2/3)
 = C_(3/2) [144 sqrt(12e)/13]^(2/3)
 < 15.14.                                                    (3.8)

For general a, apply this to S/a and rescale the scalar output; the L3 norm scales by a^(-2/3). QED.

This theorem is not a bounded-density theorem by itself. Its purpose is to provide exactly the fractional regularity needed by a dependent physical square.

## 4. Dependence-safe square smoothing from an L3 base

### Lemma QFORM-DEPENDENT-SQUARE-L3-v1

Let R have density h in L3 with ||h||_3=M. Let V be any real random variable such that, for almost every r, the conditional law V|R=r has a density bounded by one. Then for every alpha!=0,

Y=R+alpha V^2

has an essentially bounded density and

||p_Y||_infinity <= (8/3^(3/4)) |alpha|^(-1/2) M^(3/4).      (4.1)

### Proof

Conditioning on R=r, the density of alpha V^2 is bounded on the appropriate half-line by

|alpha|^(-1/2) u^(-1/2), u>0,

because the two preimages contribute at most one each after the square-root Jacobian. Hence at any target y, split u at H>0. The near part is bounded by Holder,

|alpha|^(-1/2) M (int_0^H u^(-3/4) du)^(2/3)
 = |alpha|^(-1/2) 2^(4/3) M H^(1/6).                         (4.2)

For the far part, u^(-1/2)<=H^(-1/2) and the remaining mixture has total probability at most one, hence

far <= |alpha|^(-1/2) H^(-1/2).                             (4.3)

Optimizing H gives (4.1). No independence of R and V is used. QED.

## 5. New full-matrix branch: scalar pivot plus diffuse two-eigenvalue Schur remainder

### Theorem QFORM-SCALAR-PIVOT-DIFFUSE-SCHUR-BRIDGE-v1

Write A in one original physical coordinate i as

A = [[alpha, b^T],[b,C]],  alpha!=0,

and let

S=C-bb^T/alpha

be the Schur complement. Suppose that for some mu>0:

1. S has at least two eigenvalues of absolute value at least mu;
2. the spectral projection of S onto |lambda|>=mu/64 has every original-coordinate diagonal at most 1/32.

Then for arbitrary independent cap-one input laws,

||p_(X^T A X)||_infinity
 <= C_* (|alpha| mu)^(-1/2),                                 (5.1)

where

C_*=(8/3^(3/4)) C_3^(3/4)
   =26.9283786689... <27.                                    (5.2)

### Proof

Let Z denote all coordinates except X_i. Completing the square in the actual independent coordinate X_i,

X^T A X = alpha (X_i+b^TZ/alpha)^2 + Z^T S Z.               (5.3)

Set R=Z^T S Z and V=X_i+b^TZ/alpha. By Theorem 3,

||p_R||_3 <= C_3 mu^(-2/3).                                 (5.4)

Although V and R are dependent, conditioning on R preserves the cap needed by Lemma 4. Indeed, conditional on Z=z, V is just a translate of X_i and has density at most one. Mixing those translated densities over the conditional law Z|R=r still gives a conditional density of V|R=r bounded by one. Therefore Lemma 4 applied to (5.3) gives

||p_Q||_infinity
 <= (8/3^(3/4)) |alpha|^(-1/2)
      (C_3 mu^(-2/3))^(3/4)
 = C_* (|alpha|mu)^(-1/2).                                  (5.5)

QED.

This is a full-matrix statement: every additional Schur eigenvalue and coupling is retained. It uses product structure before the nonlinear square and never assumes independence after an eigenbasis rotation.

## 6. Stable-pivot structural lemma

The previous theorem becomes target-relevant without assuming the Schur complement itself has two unit eigenvalues.

Let rho=||b||/|alpha|. Define

L = [[1,(b/alpha)^T],[0,I]],
D = diag(alpha,S).

Then

A=L^T D L.                                                   (6.1)

Since ||L||<=1+rho,

s_3(D) >= s_3(A)/||L||^2.                                   (6.2)

Under the target hypothesis s_3(A)>=1, D therefore has at least three singular values at least

mu=(1+rho)^(-2).                                             (6.3)

Only one of those can come from the scalar block alpha, so S has at least two singular values at least mu. Consequently, if the mu/64 Schur spectral window is diffuse in the precise sense of Theorem 5, then

||p_Q||_infinity <27 (1+rho)/sqrt(|alpha|).                  (6.4)

For example, if |alpha|>=1/4 and ||b||<=|alpha|, the branch has

||p_Q||_infinity <108.                                      (6.5)

The remaining structural debt is explicit: the bare three-large-eigenvalue hypothesis has not yet been shown to force either such a diffuse Schur window or another already-paid heavy-coordinate branch. The known singleton-plus-two-banks family forbids replacing this debt by a single uniformly good minor or cross-rank-three dichotomy.

## 7. Designated partner account04/B16 applied to an actual inequality

Two completed account04/B16 results were read and used:

- `account04/B16 r1`, scientific source `yspennstate/math-open-problems@226e8a59044520bf290acfa4ef2d80cdab1b8669`, proves that in exact rank three, if a row i has spectral leverage c_i>0, physical diagonal d_i=A_ii!=0, and every transverse row leverage is <=1/2, then

  ||p_Q||_infinity <=4 sqrt(2e) (c_i |d_i| |det Lambda|)^(-1/4).    (7.1)

- `account04/B16 r2`, scientific source `yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`, proves that if c_i>1/2 and some transverse residual leverage h_j>1/2, then the pair Gram area is G_ij=c_i h_j>1/4 and the exact determinant bank has mass |det Lambda|G_ij>|det Lambda|/4. (7.2)

Therefore, in exact rank three with |lambda_k|>=1, if there is a physical row i with

c_i>1/2,   |A_ii|>=1/4,                                     (7.3)

then either all transverse leverages are <=1/2, in which case (7.1) gives

||p_Q||_infinity
 <4 sqrt(2e) [(1/2)(1/4)]^(-1/4)
 =15.6853685261...;                                          (7.4)

or some transverse leverage exceeds 1/2, in which case (7.2) triggers the previously proved B16 nested-heavy pair-pivot closure `QFORM-NESTED-HEAVY-PAIR-PIVOT-CLOSURE-v1` at

`yspennstate/math-open-problems@79f522e69a2d8ea0ce1c294445e6e361acef5c1d`

and gives

||p_Q||_infinity <310.                                       (7.5)

Thus the whole exact-rank-three branch (7.3) is paid by <310. This is a genuine use of the designated partner mathematics, not a citation-only mention.

## 8. What is and is not proved

New:

- A general ridge L^r theorem whose threshold theta*r/(r-1)>2q is weaker than the L1/Fourier-inversion threshold.
- A two-large-eigenvalue spectral-window L3 theorem with explicit norm <15.14 a^(-2/3), allowing arbitrary smaller nonseparable spectrum.
- A dependence-safe L3-to-Linfinity physical-square theorem.
- A full-matrix scalar-pivot + diffuse-Schur bridge with constant <27(|alpha|mu)^(-1/2).
- A stable-pivot lemma that supplies two Schur eigenvalues at scale (1+||b||/|alpha|)^(-2).
- A designated-partner closure of the exact-rank-three heavy-diagonal branch by <310.

Not proved:

- an exhaustive structural reduction from only s_3(A)>=1 to the hypotheses of Theorem 5 or another paid branch;
- the full universal QFORM constant;
- a continuous representative for the new L3-to-square branch.

The next target-relevant implication is an exhaustive product-preserving dichotomy: either find a physical pivot whose Schur two-eigenvalue spectral window is diffuse at its natural stable-pivot scale, or prove that failure of every such window forces a heavy coordinate/group configuration paid by the pair-log, nested-heavy, weighted-affine-fiber, or grouped-bank theorems. This is a structural statement about original coordinates, not a rotated-independence claim.

## 9. Numerical constant check

The companion `check_results.json` records direct evaluation of the constants in (3.3), (5.2), (6.5), and (7.4). Those calculations are checks only; the preceding derivations are the proof.
