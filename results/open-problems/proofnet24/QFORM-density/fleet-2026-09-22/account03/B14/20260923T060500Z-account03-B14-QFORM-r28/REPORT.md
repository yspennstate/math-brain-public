SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T06:05:00Z.
attacking: zero-loss reduction from arbitrary rough inputs and threshold-spectrum matrices to compact finite-fragment inputs and generic strict-spectrum matrices, preserving the universal density constant.

# QFORM-GENERIC-EXTREME-LOCALIZATION-v1

Programme: QFORM-DENSITY-3EIG-20260922  
Worker: account03/B14  
Run: 20260923T060500Z-account03-B14-QFORM-r28  
Status: PROVED SUPPORTING LOCALIZATION THEOREM; FULL QFORM OPEN; full-target continuity OPEN.  
Execution: WITHOUT_VERIFIED_BRAIN.

## 1. Target and purpose

The target remains: for every n, every independent real X_i with densities 0<=f_i<=1, and every real symmetric A with at least three eigenvalues of absolute value >=1, prove that Q=X^TAX has a density bounded by one universal constant, or give a valid counterexample.

This note proves that, for the essential-boundedness target, there is exactly no loss in simultaneously imposing two auxiliary hypotheses that are often convenient in later analytic arguments:

1. every input marginal is the indicator of a compact finite union of intervals of total measure one; and
2. the matrix is invertible, has simple spectrum, and has three eigenvalues of modulus strictly greater than one.

The reduction preserves the optimal universal constant exactly. It also holds for the affine family x^TAx+l^Tx+c, which is the form produced by conditioning on outside original coordinates. Therefore arbitrary translations, threshold eigenvalues |lambda|=1, repeated/zero eigenvalues, distant fragments and unbounded original supports are not separate losses in the essential-density problem.

Continuity is explicitly separate: this reduction transfers interval concentration / L-infinity bounds, but not continuity of a density.

## 2. Classes and concentration constant

For a probability measure eta on R define

    Conc(eta) = sup_{I interval, 0<|I|<infinity} eta(I)/|I|.

If Conc(eta)<=C, then eta<=C Lebesgue measure on intervals, hence on Borel sets by outer regularity; therefore eta has a density p with ||p||_infinity<=C. Conversely a density cap C gives Conc(eta)<=C. Thus Conc is exactly the essential density norm, allowing us to state the reduction before absolute continuity has been proved.

Let D_n be the class of product probability laws mu=otimes_i mu_i on R^n such that each mu_i has a density f_i with 0<=f_i<=1.

Let F_n be the subclass for which each marginal density is 1_{E_i}, with E_i a compact finite union of bounded intervals and |E_i|=1. The components may be arbitrarily far apart and their number is not uniformly bounded.

Let A_3(n) be the symmetric n x n matrices having at least three eigenvalues of modulus >=1.

Let G_3(n) be the subclass of real symmetric matrices B such that:

- B is invertible;
- every eigenvalue of B is simple;
- at least three eigenvalues have modulus strictly >1.

For an affine quadratic polynomial

    P_{A,l,c}(x)=x^TAx+l^Tx+c,

define

    C_aff_full = sup_{n,A in A_3(n),l,c,mu in D_n} Conc((P_{A,l,c})_#mu),

and

    C_aff_genff = sup_{n,B in G_3(n),l,c,nu in F_n} Conc((P_{B,l,c})_#nu).

The suprema are extended-real numbers. Likewise define C_hom_full and C_hom_genff by fixing l=0,c=0.

## 3. The theorem

### Theorem 3.1 (generic-extreme localization, exact constant)

    C_aff_full = C_aff_genff,
    C_hom_full = C_hom_genff.

In particular, if a universal interval bound

    P{U^TBU+l^TU+c in I} <= C |I|                         (3.1)

is proved for every n, every B in G_3(n), every affine l,c, and every finite-fragment product law in F_n, then the same numerical C holds for every A in A_3(n), every affine l,c, and every arbitrary cap-one product law in D_n. The homogeneous target follows by l=c=0.

No support radius, fragment count, fragment separation, translation magnitude, moment, eigenvalue gap at one, spectral multiplicity, or nullspace penalty appears in the constant.

### Proof

The inequalities

    C_aff_genff <= C_aff_full,
    C_hom_genff <= C_hom_full

are immediate because G_3(n) is a subclass of A_3(n) and F_n is a subclass of D_n.

It remains to prove the reverse inequality. We do the affine case; the homogeneous case is identical with l=c=0.

Fix n, A in A_3(n), l in R^n, c in R, and first fix one finite-fragment product law nu in F_n. Let K=supp(nu). Since every E_i is a compact finite union of bounded intervals, K is compact. Put

    R = sup_{x in K} ||x||_2 < infinity.                         (3.2)

We now construct symmetric B_m in G_3(n) with

    ||B_m-A||_op ->0.                                          (3.3)

Diagonalize A=O diag(lambda_1,...,lambda_n) O^T. Choose three indices J for which |lambda_j|>=1. For every m choose real perturbations eps_{j,m} with max_j |eps_{j,m}|<1/m such that:

- lambda_j+eps_{j,m} is nonzero for all j;
- the n numbers lambda_j+eps_{j,m} are pairwise distinct;
- for j in J with |lambda_j|=1, eps_{j,m} has the outward sign sign(lambda_j), so |lambda_j+eps_{j,m}|>1;
- for j in J with |lambda_j|>1, eps_{j,m} is chosen small enough to retain modulus >1.

Such a choice exists because at each stage there are only finitely many forbidden values (zero and previously chosen eigenvalues), while each allowed perturbation interval contains infinitely many points; for threshold eigenvalues we use the appropriate one-sided interval. Set

    B_m=O diag(lambda_1+eps_{1,m},...,lambda_n+eps_{n,m}) O^T.

Then B_m is invertible, has simple spectrum, has three eigenvalues of modulus >1, and ||B_m-A||_op<1/m.

For x in K,

    |P_{B_m,l,c}(x)-P_{A,l,c}(x)|
      = |x^T(B_m-A)x|
      <= R^2 ||B_m-A||_op =: eta_m,                         (3.4)

with eta_m->0. If I is any bounded interval and

    I^{eta}={t:dist(t,I)<eta},

then |I^{eta}|=|I|+2eta and (3.4) gives the event inclusion

    {P_{A,l,c}(X) in I} subset {P_{B_m,l,c}(X) in I^{eta_m}}. (3.5)

Therefore, by the definition of C_aff_genff,

    P_nu{P_{A,l,c} in I}
      <= P_nu{P_{B_m,l,c} in I^{eta_m}}
      <= C_aff_genff (|I|+2 eta_m).                           (3.6)

Letting m->infinity yields

    P_nu{P_{A,l,c} in I} <= C_aff_genff |I|                  (3.7)

for every finite-fragment product nu in F_n, uniformly in l and c. Note the important order: the radius R may be arbitrarily large and may depend on the particular distant-fragment law, but it appears only in eta_m, which is sent to zero before any universal constant is read off. There is therefore no bounded-support-radius or fragment-separation tax.

Now apply the completed account04/B14 affine-family finite-mixture localization theorem (canonical source: yspennstate/math-open-problems@19d9434e07142e6b9fe19b4a88bbd46ccec8eeee, proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T001323Z-account04-B14-affine-mixture-compiler-r5/REPORT.md, Theorem 2.1 and its finite-mixture paragraph). That theorem states that a bound uniform in l,c over finite-fragment indicator product laws transfers, with the identical constant, to every cap-one product law in D_n. Applying it to (3.7) gives

    P_mu{P_{A,l,c} in I} <= C_aff_genff |I|                  (3.8)

for every mu in D_n, including arbitrary unbounded supports and infinitely fragmented marginals. Taking the supremum over n,A,l,c,mu proves

    C_aff_full <= C_aff_genff.

Together with the trivial reverse inequality this proves the affine equality. Restricting throughout to l=c=0 proves the homogeneous equality. QED.

## 4. Translation invariance and why affine uniformity is the right conditional interface

For any h in R^n, write X=Y+h. Then

    P_{A,l,c}(Y+h)
      = Y^TAY + (l+2Ah)^T Y
        + c + l^T h + h^T A h.                              (4.1)

Physical-coordinate translation preserves independence and every marginal density cap. It also maps a compact finite-union indicator to another compact finite-union indicator of the same total measure. Hence the affine concentration class is exactly invariant under arbitrary coordinate shifts.

This is useful after conditioning on outside original coordinates. If X=(U,V) and

    A = [[B,C],[C^T,D]],

then for each fixed V=v,

    X^TAX = U^TBU + (2Cv)^T U + v^TDv.                      (4.2)

Thus an affine-uniform theorem for the active physical block B is precisely what is needed. Equations (3.7)-(3.8) show that, for essential boundedness, one may prove such a theorem only on generic B with strict spectral inequalities and compact finite-fragment active marginals; arbitrary outside-induced translations and arbitrary rough active laws then cost exactly zero.

This uses the account04/B14 result at an actual inequality: (3.7), which has a concrete constant C_aff_genff for every l,c, is fed into the partner's finite-mixture compiler to obtain (3.8) for the full cap-one class. No conditional density cap, no post-rotation independence, and no bounded-diameter hypothesis is introduced.

## 5. Consequences for future QFORM arguments

### 5.1 Threshold eigenvalues can be treated as strict

A proof may assume the three relevant eigenvalues satisfy |lambda|>1, provided the bound is uniform and the final passage uses Theorem 3.1. Eigenvalues exactly at |lambda|=1 are recovered with no multiplicative (1+epsilon) loss.

### 5.2 Repeated and zero eigenvalues can be removed during the proof

A proof may assume invertibility and simple spectrum without claiming repeated eigenvalues are a geometric degeneracy of the original quadratic Hessian. The assumptions are merely a dense regularization device. The original singular/repeated matrix is recovered by the compact-extreme support limit (3.4)-(3.7).

### 5.3 Distant fragments and unbounded original supports need not be controlled by a support radius

The finite-fragment approximants can have arbitrarily distant components. Their support radius only multiplies ||B_m-A||_op in the vanishing error eta_m. The partner finite-mixture theorem then lifts the result to genuinely unbounded and infinitely fragmented input laws. Thus no uniform moment or diameter estimate is needed.

### 5.4 The reduction does not justify rotating the input coordinates

The orthogonal O above is used only to construct nearby matrices B_m; the random vector X is never changed to O^TX. Independence therefore remains in the original physical coordinates throughout.

## 6. Continuity is not transferred

Theorem 3.1 is an interval-concentration / essential-density theorem. Even if each approximating generic finite-fragment instance happened to possess a continuous density bounded by C, total-variation or weak limits of such densities need not have a continuous representative without an additional uniform regularity mechanism.

Earlier B14 work gave an explicit target-valid obstruction to a universal output equicontinuity modulus using phase-aligned finite-fragment laws. Therefore no continuity claim is made here. The owner-requested continuous-density conclusion for the unrestricted target remains a separate open obligation.

## 7. Relation to the remaining full problem

This theorem removes a class of technical excuses but not the main structural difficulty. After this reduction one may, with no loss in the optimal essential-density constant, work on compact finite-fragment product inputs and generic matrices with strict three-large-eigenvalue inequalities. The remaining hard implication is still structural/analytic: convert the three-large-eigenvalue condition into a product-preserving smoothing estimate in the no-pivot / grouped-bank / non-coloop regimes. In particular, Theorem 3.1 does not create a good physical minor, does not validate a fiber-sup argument, and does not replace aggregate-before-inversion.

The immediate use for B14 is that future near-coloop or grouped-bank arguments may perturb away accidental spectral equalities and matrix singularities while retaining the exact universal constant, and may postpone all rough-support issues to the final account04/B14 finite-mixture lift.

## 8. Integrity and source corrections consumed

Consumed corrections include: no uniform pointwise quadratic-phase decay; no post-rotation independence; no naive fiber-sup dimension-free estimate; no arbitrary-joint rank-three coarea theorem; no bounded-diameter/fixed-fragment-count localization; and no inference of continuity from an essential density cap. None is used as a premise.

Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.  
New proved result: exact equality of the full and generic-finite-fragment optimal concentration constants, both homogeneous and affine.  
Partner actually applied: account04/B14 r5 affine-family finite-mixture localization theorem.  
Continuity: OPEN beyond previously proved structural branches.  
Native brain ingestion: NOT VERIFIED.
