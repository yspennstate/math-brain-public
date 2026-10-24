# account04/B16 — nested-heavy fixed-pair determinant mass and a universal zero-diagonal atom bound

**Run:** `20260922T161909Z-account04-B16-QFORM-r2`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The owner target remains the following universal statement: for independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove that the quadratic form has a density bounded by one universal constant, or give a valid counterexample. No moment, support, log-concavity, Gaussian, or diagonal-basis independence assumption is made. Continuity is tracked separately.

This report does not use a bounded projected density as a substitute for an indefinite level-set bound. It does not select an arbitrarily small physical minor and average its reciprocal cost. It keeps the original-coordinate determinant bank identified by the completed assigned-partner result.

The completed assigned-partner input is account01/B16, run `20260922T154258Z-account01-B16-QFORM-r12`, source-read at

`yspennstate/math-open-problems@47fe1ce92881fa4b6df0fa8a12b706d6a4eb14c5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260922T154258Z-account01-B16-QFORM-r12/REPORT.md`,

blob `66a96301a5033af3d0cc3c94ae66a9f8ada85194`.

It proves the fixed-pair identity
[
 sum_{k
e i,j}|det A_{{i,j,k}}|
 =|detLambda|,G_{ij},qquad
 G_{ij}=|r_i|^2|r_j|^2-langle r_i,r_jangle^2,
]
and identifies normalized weights (w_kge0), (sum w_k=1), such that
[
 |det A_{{i,j,k}}|=|detLambda|G_{ij}w_k.
]
The same (w_k=l_k^2) build a normalized original-coordinate bank (L=sum l_kX_k) whose density is at most two. Its partner theorem also gives, for an invertible zero-diagonal physical triple (C),
[
 |p_Q|_inftyle C_{m off}|det C|^{-1/3},
 qquad
 C_{m off}=2^{4/3}{log3+2log(3/2)}
 =4.8117455951457755ldots ,
]
with arbitrary outside quadratic terms and couplings.

## 2. Nested-heavy geometry

Let
[
 A=RLambda R^	op,qquad R^	op R=I_3,
]
be an exact-rank-three physical block; (r_k) denotes row (k) of (R). Fix a physical row (i) with
[
 c=|r_i|^2>1/2,qquad e=r_i/sqrt c.
]
For another row (j), define its residual leverage after the first row by
[
 h=|(I-ee^	op)r_j|^2.
]
Assume the genuinely nested-heavy condition (h>1/2).

### Lemma 2.1 — exact nested-heavy Gram identity

Under these definitions,
[
 oxed{G_{ij}=ch>1/4.}
]

Indeed,
[
egin{aligned}
G_{ij}
&=|r_i|^2|r_j|^2-langle r_i,r_jangle^2\
&=cleft(|r_j|^2-langle e,r_jangle^2ight)
=c|(I-ee^	op)r_j|^2=ch.
end{aligned}
]
This is exact and uses no probabilistic input.

Combining it with the partner fixed-pair identity yields the determinant-mass estimate
[
 oxed{sum_{k
e i,j}|det A_{{i,j,k}}|
 =|detLambda|ch>rac14|detLambda|.}
 	ag{2.1}
]
If all three nonzero eigenvalues of the block have modulus at least one, then (|detLambda|ge1), so the fixed-pair physical determinant bank has total mass (>1/4). This is a universal lower bound even when every individual physical triple is tiny.

## 3. Target-level heavy atom theorem

### Theorem 3.1 — `QFORM-NESTED-HEAVY-ZERODIAG-ATOM-v1`

In the setting above, suppose all three nonzero eigenvalues of the exact-rank-three block have modulus at least one. Let the partner weights be (w_k). If for some (k
e i,j)

[
 A_{ii}=A_{jj}=A_{kk}=0,qquad w_kge	au>0,
]
then, for arbitrary outside original coordinates, arbitrary outside quadratic terms and arbitrary couplings to the block,
[
 oxed{
 |p_Q|_infty
 le C_{m off}left(rac4	auight)^{1/3}.}
 	ag{3.1}
]

In particular, if (w_kge1/8),
[
 oxed{|p_Q|_infty
 le C_{m off},32^{1/3}
 =15.276340039075507ldots .}
 	ag{3.2}
]

### Proof

The atomwise partner identity and Lemma 2.1 give
[
 |det A_{{i,j,k}}|
 =|detLambda|ch,w_k
 >rac14 w_k
 gerac{	au}{4}.
]
The zero-diagonal hypothesis and the positive determinant show that this physical triple is invertible. Condition on every original coordinate outside ({i,j,k}). Independence and the original density caps of (X_i,X_j,X_k) are preserved; all outside interactions become arbitrary linear terms, which are allowed by the partner zero-diagonal triple theorem. Hence
[
 |p_{Qmid X_{{i,j,k}^c}}|_infty
 le C_{m off}|det A_{{i,j,k}}|^{-1/3}
 le C_{m off}(4/	au)^{1/3}.
]
The bound is independent of the conditioned values. Mixing proves (3.1), absolute continuity, and then (3.2). QED.

This is a substantive application of the assigned partner theorem to an actual target-level conditional density inequality. No independence of rotated spectral coordinates is asserted.

## 4. What the theorem removes

The nested-heavy state is precisely the branch in which a first physical leverage exceeds one half and a second row remains heavy after orthogonal removal of the first. Lemma 2.1 shows that this branch cannot have a small fixed-pair determinant **bank**: its total mass is universally bounded below. Theorem 3.1 shows that if even one zero-diagonal atom carries one eighth of that normalized bank, the complete quadratic form is paid by the explicit universal constant (15.277).

Consequently, an unpaid zero-diagonal nested-heavy configuration must satisfy
[
 w_k<1/8
]
for every eligible zero-diagonal third coordinate. If every positive bank atom is eligible, there must be at least nine positive atoms. Thus the remaining case is genuinely diffuse; it cannot be mislabeled as a missing large physical minor.

## 5. First unpaid implication

The exact remaining projection-product debt exposed here is:

**`QFORM-NESTED-HEAVY-DIFFUSE-CUBIC-BANK-v1`.** In the nested-heavy state (c,h>1/2), exploit the normalized original-coordinate bank
[
 L=sum l_kX_k,qquad |p_L|_inftyle2,qquad
 |det A_{{i,j,k}}|=|detLambda|ch,l_k^2,
]
to pay the diffuse case (max l_k^2<1/8) before taking reciprocal local-minor constants. The desired scale is the total invariant ((|detLambda|ch)^{-1/3}), not a linear average of (|det A_{{i,j,k}}|^{-1/3}). Arbitrary outside couplings must remain allowed.

The present theorem does not prove that cubic-bank aggregation inequality. It also does not extract an exact-rank-three physical block from an arbitrary full matrix with additional spectral components. Those are separate debts.

## 6. Status and regularity

Proved here:

1. the exact identity (G_{ij}=ch) in the nested-heavy state;
2. the universal fixed-pair determinant-mass lower bound (2.1);
3. the target-level heavy zero-diagonal atom estimate (3.1), including the explicit bound (3.2), by direct application of the completed account01/B16 theorem.

Not proved: the diffuse cubic-bank aggregation, arbitrary exact-rank-three closure, stability under arbitrary additional spectral components, or the full owner conjecture.

The theorem proves an essentially bounded density in its scope. Continuity is not proved.

**Full QFORM conjecture: OPEN / NOT PROVED.**
