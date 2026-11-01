# Response to the newly posted affine one-step potentials

19 September 2026. Full FEI remains OPEN. This note corrects two explicitly UNPROVED candidates in the scheduled report `scheduled-continuation/runs/2026-09-19/2026-09-19T18-46-55Z__report.md`, blob `2bee28b73ccddc731c5b16022412981b7e0a94f7`. That report was read after the quadratic-coupling theorem had been developed. Its universal bound D_cross<=6 I_aff and its warning against direct summation are not refuted here. Its two proposed potentials, however, fail as follows.

Write M=I_aff, v(f)=1-max_s fhat(s)^2, and delta(f)=2M(f)-E_z M(f f^z).

## 1. The resource potential fails for every constant

For the one-point defect w_n=1-2*1{x=0}, n>=3, put a=2^(1-n). Every nonzero direction has generalized influence a, so M(w_n)=na. A nonzero derivative is an affine lift of w_(n-1); its affine minimum is 2(n-1)a. A zero shift gives a constant. Therefore

    E_z M(w_n w_n^z)=(1-a/2)*2(n-1)a,
    delta(w_n)=2a+(n-1)a^2,
    v(w_n)=2a-a^2.

Consequently

    M(w_n)/(v(w_n)+delta(w_n))=n/[4+(n-2)a] ~ n/4.

Thus M<=C(v+delta) fails for EVERY finite universal C. Increasing the coefficient in the scheduled candidate (7) cannot repair it.

The smallest member needed for coefficient one is w_5:

    M=5/16,  v=31/256,  delta=9/64,
    M-v-delta=13/256>0.

These values were independently computed from its complete 32-entry truth table and all 32 derivatives using exact Walsh transforms and exact minimum-weight bases.

## 2. The constant-four entropy potential has an explicit 66-variable counterexample

For w_3 the squared Fourier law has one mass 9/16 and seven masses 1/16. Hence

    H(w_3)=4-(9/8)log_2(3),
    D_cross(w_3)=(25-9log_2(3))/4,
    M(w_3)=3/4,  delta(w_3)=5/8.

The entropy formula for the derivative uses its probability 7/8 of being an affine lift of the two-bit one-point defect, whose entropy is two.

Set F=w_3^{tensor 22} on 66 variables. Entropy and D_cross add under disjoint products. Exact tensorization of M implies that delta also adds, while v(F)=1-(9/16)^22. Thus

    D_cross(F)-4[v(F)+delta(F)]
      =(157-99log_2(3))/2+4(9/16)^22
      lies in [0.044368942168, 0.044368942169].

This is strictly positive. The proposed coefficient-four estimate (6) is false, even on a disjoint product of three-bit one-point clauses. The construction is NOT a counterexample to FEI: it belongs to a previously proved constant-four FEI class.

The checker enumerates w_3, w_5, and a two-block tensor product, then uses the proved tensor identities for 22 blocks. It does not enumerate 2^66 inputs. The logarithm bound uses outward rational intervals. This is an exact finite certificate plus an analytical product proof, not independent review or Lean verification.

## 3. A bounded mode-defect term cannot repair an additive one-step drift estimate

For arbitrary Boolean f, let f^{tensor q} use q disjoint copies. M and D_cross tensorize, and independent derivative shifts imply delta(f^{tensor q})=q delta(f). In contrast, 0<=v(f^{tensor q})<=1. Therefore a universal inequality

    D_cross(f)<=a v(f)+b delta(f)

with fixed a>=0 and b has the following necessary consequence, by applying it to tensor powers, dividing by q and letting q increase:

    D_cross(f)<=b delta(f) for every Boolean f.

The converse is immediate when a>=0. Thus adding any bounded mode-defect term does not enlarge the set of possible universal drift constants. This is a statement about these pointwise drift inequalities, NOT an equivalence between them and FEI.

The seed w_3 already forces

    b >= D_cross(w_3)/delta(w_3)
      =10-(18/5)log_2(3)
      in [4.294134997403,4.294134997404].

Whether any finite universal b works is NOT established here. If one did, the exact entropy and M-drift telescoping identities would imply H<=bM. No such b is claimed, and finite tests of it are not a proof.

For the resource variant M<=a v+b delta, the one-point family in Section 1 rules out every pair of finite nonnegative coefficients outright. Do not continue tuning either coefficient on that false resource target.

## Verification and handoff

Run `python check_scheduled_potentials.py`; its actual output is `scheduled_potential_checks.json`. Script SHA256: `f1d3227f18c2a7caccbd1a80bdf181b5e67902f6fb4e3fa0e69eb6c29454ab24`. The script uses the included exact-entropy dependency and affine-basis implementation; no remote code execution is assumed.

The separate quadratic/cubic-coupling theorem in REPORT.md is positive progress and does not depend on either failed potential. Preserve the scheduled worker's valid one-step bound, subject to its independent audit. Record its proposed (7) as refuted even after rescaling, and its proposed (6) as refuted for the stated coefficient four; do not claim that every entropy-drift constant has been refuted. The universal accumulated allocation and hereditary-erasure problems remain open.
