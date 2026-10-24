# Target-level indefinite-pair pivot branch and sign-resolved Schur survival

Run: `20260924T153840Z-account03-B11-fixedmult-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned nine-eigenvalue source: `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`.

Status: PROVED SUPPORTING TARGET-LEVEL BRANCH. This does not prove the general three-eigenvalue conjecture or the eight-eigenvalue theorem.

## 1. Sign-resolved Schur count

Let
[
A=egin{pmatrix}B&C\ C^T&Dend{pmatrix}=A^T,qquad det B
e0,qquad
S=D-C^TB^{-1}C,
]
with (B) of order (k). For (t>0), define
[
N_+(H,t)=#{lambda_j(H)ge t},qquad
N_-(H,t)=#{lambda_j(H)le -t},
]
and let (
u_pm(B)) denote the positive/negative inertia of (B). Then
[
oxed{N_+(S,t)ge N_+(A,t)-
u_+(B)},qquad
oxed{N_-(S,t)ge N_-(A,t)-
u_-(B)}. 	ag{1}
]

### Proof for invertible ambient (A)

Block elimination gives (Asim Boplus S), hence
[

u_pm(S)=
u_pm(A)-
u_pm(B). 	ag{2}
]
The complementary principal block of (A^{-1}) is (S^{-1}). For an invertible symmetric (H),
[
N_+(H,t)=
u_+(H)-#{lambda(H^{-1})>t^{-1}}. 	ag{3}
]
Because (S^{-1}) is a principal compression of (A^{-1}), Cauchy interlacing implies
[
#{lambda(S^{-1})>t^{-1}}le
#{lambda(A^{-1})>t^{-1}}. 	ag{4}
]
Combine (2)--(4) to get the positive inequality in (1). Applying the same argument to (-A) gives the negative inequality.

### Singular ambient (A)

Fix (0<delta<t). Choose (arepsilon_m	o0) so that (A+arepsilon_m I) is invertible and (|arepsilon_m|<delta/2). Since (B) is invertible, (B+arepsilon_m I) has the same inertia as (B) for all large (m). Its Schur complement (S_m) tends to (S). Every eigenvalue of (A) at least (t) stays at least (t-delta) after the perturbation, so
[
N_+(A+arepsilon_m I,t-delta)ge N_+(A,t).
]
The invertible case gives
[
N_+(S_m,t-delta)ge N_+(A,t)-
u_+(B).
]
Passing to the limit and then letting (deltadownarrow0) gives the first inequality in (1). The negative inequality is identical after sign reversal.

Thus the usual unsigned count (N_S(t)ge N_A(t)-k) splits exactly by pivot inertia.

## 2. Consequence for the two indefinite target signatures

Suppose (s_3(A)ge s>0) and a principal (2	imes2) pivot (B) is indefinite. Then (
u_+(B)=
u_-(B)=1).

If the three threshold-large directions have signature ((+,+,-)), i.e.
[
N_+(A,s)ge2,qquad N_-(A,s)ge1,
]
then (1) gives
[
oxed{N_+(S,s)ge1}. 	ag{5}
]
For signature ((+,-,-)),
[
oxed{N_-(S,s)ge1}. 	ag{6}
]
So after paying the logarithmic indefinite pair, the third majority-sign direction survives in the Schur remainder at the full spectral scale (s). This is the exact sign-sensitive form of “the third direction remains available.”

## 3. Density theorem for a physical indefinite pair pivot at multiplicity three

Let (X) have independent coordinate densities bounded by (K). Let
[
Q=X^TAX+b^TX+c,qquad s_3(A)ge s>0.
]
Assume a principal (2	imes2) block (B) is indefinite and
[
|det B|ge rac{s^2}{400}. 	ag{7}
]
Then
[
oxed{|p_Q|_infty<392.5,rac{K^2}{s}}. 	ag{8}
]
Only essential boundedness is asserted; continuity is not proved in this branch.

### Proof

Normalize to (K=s=1). Put (D=|det B|ge1/400). Condition on all coordinates outside the pivot. The latest manuscript's hyperbolic-pair lemma gives, uniformly in the conditional affine terms,
[
p_{Qmid X_{m out}}(z)
le D^{-1/2}left(6+log_+rac{16sqrt D}{|z-v(X_{m out})|}ight), 	ag{9}
]
where (v) is the conditional critical value. The quadratic part of (v) is the Schur complement (S).

The ordinary Schur count already gives (N_S(1)ge N_A(1)-2ge1), hence (|S|ge1). The manuscript's quarter-power concentration lemma therefore yields
[
sup_zmathbb Elog_+rac1{|z-v|}le L_0:=4+4log5. 	ag{10}
]
Average (9) and use
[
log_+rac{16sqrt D}{u}
le log16+	frac12log_+D+log_+rac1u.
]
Since (D^{-1/2}le20) and
[
sup_{D>0}rac{log_+D}{sqrt D}=rac2e,
]
we obtain
[
|p_Q|_infty
le20(6+log16+L_0)+rac1e
=200+80log10+rac1e
<392.5. 	ag{11}
]
Undoing the standard (Y=KX), (Amapsto A/s) normalization gives (8).

The sign-resolved count (5)--(6) is stronger than needed for (8), but identifies which sign of the third spectral direction survives.

## 4. Rank-two logarithmic control and the third-direction mechanism

For independent centered unit uniforms (U,V),
[
p_{2UV}(x)=lograc1{2|x|},qquad 0<|x|<rac12. 	ag{12}
]
Thus an opposite-sign rank-two saddle is genuinely unbounded.

Equations (5)--(11) show what removes the singularity in the pivot branch: the indefinite pair contributes only a logarithmic envelope, while the third large Schur direction forces a uniform logarithmic potential bound for the moving critical value. Averaging the logarithm against that third-direction concentration converts (12)'s divergent pointwise peak into the finite constant (11). No post-rotation independence is used.

## 5. Designated partner result applied to an actual target inequality

Use the completed account04/B11 sharpness family from
[
	exttt{yspennstate/math-open-problems@4a818c0cd169a3a52aac71de48e45ef338cd94fb}
]
at
[
	exttt{proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account04/B11/20260924T151545Z-account04-B11-fixedmult-schur-r1/SCHUR_SHARPNESS_FAMILY.md}.
]

Take its (p=q=1) block with (arepsilon=1/10) and direct-sum an independent (+1) coordinate. The ambient matrix has threshold-large spectrum
[
{1.1,-1.1,1}
]
plus two zeros, so (s_3(A)=1) and the signature is ((+,+,-)). The physical indefinite pivot is
[
B=operatorname{diag}(0.1,-0.1),qquad |det B|=0.01>rac1{400}.
]
The partner algebra gives an exactly zero Schur block for its four-dimensional component, so the full Schur remainder is precisely the direct-summed scalar (+1). Hence the sign-resolved inequality is attained:
[
N_+(S,1)=1=N_+(A,1)-
u_+(B),qquad
N_-(S,1)=0=N_-(A,1)-
u_-(B). 	ag{13}
]
Applying (8) to this strict three-large-eigenvalue target family yields the actual density inequality
[
oxed{|p_Q|_infty<392.5}
]
for every independent cap-one input law and every affine perturbation. Replacing the direct-summed (+1) by (-1) gives the ((+,-,-)) analogue.

The same partner family with (arepsilondownarrow0) shows that no universal Schur-count improvement can charge fewer than one positive and one negative direction to an indefinite pair merely because the pivot is small. Thus the unresolved (9	o8) debt cannot be repaired by sharper Schur bookkeeping.

## 6. Scope

Proved here:
- sign-resolved Schur spectral counts, including singular ambient matrices;
- a complete target-level three-eigenvalue density theorem in the physical indefinite-pair-pivot branch (7);
- exact identification of the surviving majority-sign third direction;
- sharpness application using the designated account04/B11 family.

Still open:
- the no-pair-pivot part of the three-eigenvalue conjecture;
- the general eight-eigenvalue no-pivot endpoint;
- global continuity in the new indefinite-pair branch.
