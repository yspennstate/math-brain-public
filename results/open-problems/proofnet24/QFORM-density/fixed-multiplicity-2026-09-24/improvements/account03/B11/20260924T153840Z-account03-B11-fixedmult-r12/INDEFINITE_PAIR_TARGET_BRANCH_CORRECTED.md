# Target-level indefinite-pair pivot branch and sign-resolved Schur survival — corrected text

Run: 20260924T153840Z-account03-B11-fixedmult-r12
Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924
Pinned source: yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f
Source path: proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex
Source blob: 19fb119877426b640b2c0dae19ec2f78a399fe11

This file supersedes the sibling INDEFINITE_PAIR_TARGET_BRANCH.md only as a text-encoding repair. The earlier file contains escaped-character corruption from transport. The mathematics below is the intended theorem.

STATUS: PROVED SUPPORTING TARGET-LEVEL BRANCH. The full three-eigenvalue conjecture and general eight-eigenvalue theorem remain open.

## 1. Sign-resolved Schur count

Let A be symmetric and block-decomposed as

A = [[B, C], [C^T, D]],  det(B) != 0,
S = D - C^T B^{-1} C,

where B has order k. For t>0 define

N_+(H,t) = number of eigenvalues of H >= t,
N_-(H,t) = number of eigenvalues of H <= -t,

and let nu_+(B), nu_-(B) be the positive and negative inertia of B.

Then

N_+(S,t) >= N_+(A,t) - nu_+(B),
N_-(S,t) >= N_-(A,t) - nu_-(B).                                  (1)

Proof for invertible A.
Block elimination gives inertia additivity:

nu_+(S)=nu_+(A)-nu_+(B),
nu_-(S)=nu_-(A)-nu_-(B).                                          (2)

The complementary principal block of A^{-1} is S^{-1}. For an invertible symmetric H,

N_+(H,t) = nu_+(H) - #{ eigenvalues of H^{-1} > 1/t }.           (3)

Since S^{-1} is a principal compression of A^{-1}, Cauchy interlacing gives

#{ eigenvalues of S^{-1} > 1/t }
 <= #{ eigenvalues of A^{-1} > 1/t }.                             (4)

Combining (2)-(4) proves the positive inequality in (1). Apply the same argument to -A for the negative inequality.

Singular ambient A.
Fix 0<delta<t. Choose epsilon_m -> 0 avoiding the finitely many values making A+epsilon_m I singular, with |epsilon_m|<delta/2. Since B is invertible, B+epsilon_m I has the same inertia as B for large m. Let S_m be the corresponding Schur complement; S_m -> S in operator norm. Every eigenvalue of A at least t remains at least t-delta after perturbation, so

N_+(A+epsilon_m I,t-delta) >= N_+(A,t).

Apply the invertible result at t-delta:

N_+(S_m,t-delta) >= N_+(A,t)-nu_+(B).

Pass m->infinity and then delta->0. This proves the positive inequality in (1). The negative inequality follows by sign reversal.

Thus the usual unsigned loss k splits exactly by pivot inertia.

## 2. Consequence for signatures (+,+,-) and (+,-,-)

Suppose s_3(A)>=s>0 and B is a principal indefinite 2-by-2 pivot. Then nu_+(B)=nu_-(B)=1.

For a (+,+,-) threshold signature,

N_+(A,s)>=2 and N_-(A,s)>=1,

so (1) gives

N_+(S,s)>=1.                                                       (5)

For (+,-,-),

N_-(S,s)>=1.                                                       (6)

Therefore the majority-sign third spectral direction survives the indefinite pair at the full scale s.

## 3. Density theorem at the full three-eigenvalue target in the physical indefinite-pair branch

Let X have independent real coordinates with densities <=K, let

Q = X^T A X + b^T X + c,

and assume s_3(A)>=s>0. Suppose a principal 2-by-2 block B is indefinite and

|det B| >= s^2/400.                                                (7)

Then Q has a density satisfying

||p_Q||_infinity < 392.5 K^2/s.                                  (8)

Only essential boundedness is claimed here; continuity is not proved.

Proof.
Normalize K=s=1. Put Delta=|det B|>=1/400. Condition on all coordinates outside the pivot. The hyperbolic-pair lemma in the pinned manuscript gives, uniformly in the conditional affine terms,

p_{Q | outside}(z)
 <= Delta^{-1/2} [ 6 + log_+(16 sqrt(Delta)/|z-v(outside)|) ],     (9)

where the quadratic part of the conditional critical value v is the Schur complement S.

The ordinary Schur count gives N_S(1)>=N_A(1)-2>=1, hence ||S||>=1. The manuscript's quarter-power concentration lemma gives

sup_z E log_+(1/|z-v|) <= L0 := 4 + 4 log 5.                      (10)

Average (9) and use

log_+(16 sqrt(Delta)/u)
 <= log 16 + (1/2) log_+ Delta + log_+(1/u).

Because Delta^{-1/2}<=20 and

sup_{Delta>0} Delta^{-1/2} log_+ Delta = 2/e,

we get

||p_Q||_infinity
 <= 20(6 + log16 + L0) + 1/e
 = 200 + 80 log10 + 1/e
 < 392.5.                                                           (11)

Undo the standard Y=KX and A/s normalization to obtain (8).

The sign-resolved count is stronger than needed for the numerical bound, but identifies the sign of the surviving third direction.

## 4. Rank-two logarithmic control and how the third direction removes it

For independent centered unit uniforms U,V,

p_{2UV}(x) = log(1/(2|x|)),  0<|x|<1/2.                           (12)

Thus the opposite-sign rank-two saddle is genuinely unbounded.

In the branch above, the indefinite pair contributes a logarithmic conditional envelope. The third large Schur direction moves the pair's critical value with enough concentration control to make the expected logarithm finite. Averaging (9) using (10) is exactly the logarithm-removal step. No post-rotation independence is used.

## 5. Designated account04/B11 result applied to an actual target inequality

Use the completed account04/B11 sharpness family at

yspennstate/math-open-problems@4a818c0cd169a3a52aac71de48e45ef338cd94fb

path:

proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account04/B11/20260924T151545Z-account04-B11-fixedmult-schur-r1/SCHUR_SHARPNESS_FAMILY.md

Take p=q=1, epsilon=1/10, and direct-sum an independent +1 scalar coordinate. The ambient spectrum is

{1.1, -1.1, 1, 0, 0},

so s_3(A)=1 and the threshold signature is (+,+,-). The physical pivot is

B = diag(0.1,-0.1),  |det B|=0.01>1/400.

The partner algebra makes the four-dimensional Schur block exactly zero; the full Schur remainder is the direct-summed +1. Therefore

N_+(S,1)=1=N_+(A,1)-nu_+(B),
N_-(S,1)=0=N_-(A,1)-nu_-(B).                                     (13)

Applying (8) gives the actual target inequality

||p_Q||_infinity < 392.5

for every independent cap-one input law and arbitrary affine perturbation. Direct-summing -1 instead gives the (+,-,-) analogue.

The same partner family with epsilon->0 proves that no universal Schur-count improvement can charge fewer than one positive and one negative direction merely because an indefinite pivot is small. Hence the remaining 9->8 obstruction cannot be repaired by sharper Schur bookkeeping.

## 6. Scope

Proved:
- sign-resolved Schur spectral counts, including singular ambient matrices;
- a full three-eigenvalue density theorem in the physical indefinite-pair-pivot branch (7);
- explicit identification of the majority-sign third direction;
- an actual target-family application of the completed account04/B11 sharpness result.

Still open:
- no-pair-pivot part of the unrestricted three-eigenvalue conjecture;
- general s_8 no-pivot logarithmic endpoint;
- global continuity in this branch.
