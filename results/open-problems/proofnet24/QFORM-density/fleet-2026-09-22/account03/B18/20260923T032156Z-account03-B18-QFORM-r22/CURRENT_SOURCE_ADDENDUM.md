# r22 addendum — apply the 20260923T002323Z volume-stability continuation

After the initial report was committed, fresh `AGENTS.md` required every worker to consume the owner continuation `QFORM-CLAUDE-LATEST-20260922T225732Z` and its current handoff `20260923T002323Z-volume-stability`. I therefore read the complete current theorem package at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/`,

including `REPORT.md` and `PEER_TAIL_EXTENSION.md`, and apply it here rather than merely citing it.

## A. Direct proof-map application

Let `A` be in the exact-rank-three Schur-isotropic large-shear class of the main report (`r=||u||>=1`). The new volume-stability theorem gives an independent continuous-density exit whenever some ORIGINAL-coordinate cut `I,J` has cross block

`M=A[I,J]=M0+E`

with

`s3(M0)>=a>0`,
`max_i (P_range(M0))_ii<=1/2`,
`||E||op<=a/16`.

At that exact scope, all same-side self blocks, outside couplings and induced affine terms are allowed, and the theorem gives

`boxed: ||p_Q||_infinity <23/a.`                                 (A.1)

Consequently, after the source-separated branch of the main report is removed, the **remaining non-separated large-shear debt can be restricted further** to matrices for which every prospective cross cut fails at least one of the three gates above. This is an actual logical elimination of the near-diffuse rank-at-least-three cross regime from the local large-shear problem.

The peer-tail extension yields a second elimination. For any cut whose cross block `M` has row projection `P` satisfying

`max_i P_ii<=1/2`,
`||(I-P)M||op<=sqrt(T2)/15`,
`T2=sum_(j>=3) s_j(M)^2>0`,

we have

`boxed:
 ||p_Q||_infinity
 <=(9sqrt(3)e/2)[s1(M)^2 s2(M)^2 T2]^(-1/6).`                    (A.2)

Thus a non-separated large-shear survivor must also avoid every quantitatively payable two-large-directions-plus-collective-tail cut. This narrows the local unresolved branch to low-total-tail/high-leverage cross geometry, exactly where grouped/hub mechanisms are needed.

No small operator-norm perturbation of the random quadratic form is used; the theorem retains the actual cross matrix in the Fourier argument.

## B. Exact incompatibility on the r22 stress family

The explicit family from the main report is

`A_r=[[0,0,r/s,0],
      [0,0,1/s,0],
      [r/s,1/s,0,0],
      [0,0,0,1]],  s=sqrt(1+r^2), r>=1,`

with spectrum `{-1,0,1,1}`.

For **every** disjoint coordinate cut `I,J` of this four-coordinate matrix,

`rank A_r[I,J] <= min(|I|,|J|) <=2`.                            (B.1)

Therefore every such cross block has

`s3(M)=0`, `E3(M)=0`, and `T2=0` once the two nonzero singular directions are removed. Hence neither the baseline three-volume theorem nor its collective-tail extension can be invoked on this family. In particular, it is impossible to manufacture the required positive `a` in (A.1), and (A.2) has no positive tail resource.

This exact incompatibility proves that the source-separated zero-pivot theorem in the main report is not a repackaging of the newest volume-stability exit: it pays a target family that the current three-volume/collective-tail mechanism cannot touch.

On this same family the completed account04/B18 zero-pivot 1+2 theorem gives the continuous bound

`||p_Q||_infinity <= 6*2^(1/3)=7.559526299369...`,

so the combination is genuinely complementary.

## C. Updated remaining implication

For the exact-rank-three Schur-isotropic large-shear core, after this current-source application, the unpaid class can be stated cleanly as:

1. the residual product frame is **not** source-separated along `n=u/r`;
2. no original-coordinate cross cut satisfies the near-diffuse rank-at-least-three volume-stability certificate (A.1);
3. no original-coordinate cross cut satisfies the two-directions-plus-collective-tail certificate (A.2).

The next mechanism must therefore handle a non-separated **low-total-tail or high-leverage/hub** configuration while preserving original-coordinate product provenance. The full QFORM conjecture remains OPEN / NOT PROVED; full-target continuity remains open.

This addendum makes no independent-review claim for the newest volume-stability package; its own source labels that package as supporting arguments pending the designated independent reviews. The application above is conditional on the exact proved package as supplied by the current owner-directed source.
