# fleet03/B13 r8 — nine-eigenvalue bound below 338

Run id: 20260924T195800Z-fleet03-B13-fixedmult-audit-r8

Status: supporting replacement proof; independent end-to-end review pending. The unrestricted three-large-eigenvalue conjecture, the eight-eigenvalue theorem, and global continuity remain open.

## Sources and pair audit

Current objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924, owner control revision 2026-09-24.1.

I compared the pair arguments in:
- standalone paper: proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/paper.tex (blob 823201f05363fcc60c38cce0feb5abb636f081d7);
- independent interactive synthesis: yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f, proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex (blob 19fb119877426b640b2c0dae19ec2f78a399fe11).

Both give the same deterministic physical-pair statements. A definite pair with joint density cap M has output density <= pi M/sqrt(|det B|). For an indefinite pair, D=|det B|>0,
[
p(z)le D^{-1/2}left(6+log_+rac{16sqrt D}{|z-v|}ight)
]
a.e. I rechecked the hyperbolic parametrization, Jacobian 1/(2 sqrt D), original-coordinate tail monotonicity, cap-one half-line bathtub step, and AM-GM Lambda>=2/sqrt D. The positive and negative tails may use different original coordinates; neither proof assumes otherwise. The two write-ups agree on this mechanism. Existing Lean checks cover the elementary constants/derivative identities, not the full coarea/change-of-variables theorem.

Partner actually applied below:
fleet04/B13, yspennstate/math-open-problems@0d1dd8180db0e205cab284c51b178af425e5c7f1, INDEFINITE_PAIR_274.md.

## New parameter tuple

Normalize K=s=1 and keep
[
p=1/400
]
so the partner theorem applies verbatim. Replace the scalar/volume parameters by
[
d=rac7{121},qquad h=rac{8769}{100000},qquad kappa=h^2,
]
and use
[
q=rac{76467}{1000000}.
]

Without a scalar or pair pivot,
[
|A_{ii}|<d,qquad |A_{ij}|^2<p+d^2<q^2,
]
because
[
q^2-(p+d^2)=rac{6385785049}{14641000000000000}>0.
]
The exact interpolation/Gershgorin margins are
[
1-d-h=rac{10338951}{12100000}>0,
]
[
1-d-q-4h=rac{62305533}{121000000}>0,
]
[
1-d-2q-9h=rac9{1890625}>0.
]
Therefore the source no-pivot proof remains valid for k=1,2,3:
[
s_{4k-3}(A)ge1,quad A	ext{ no pivot}
Longrightarrow V_k(A)ge h^{2k}.
]
For r=1,2, the sampled error is <(r+1)h; the selected diagonal of R is >1-(r+1)h-d and each off-diagonal is <q+(r+1)h, so the displayed margins give strict row diagonal dominance. For r=0, ||A||<d+h<1.

## No-pivot branch: <338

A random physical cut gives Z_3>=h^6/64. The source crossing theorem gives
[
|p_Q|_inftyle C_3 Z_3^{-1/6}le 2C_3/h,qquad
C_3=3sqrt2,e,(9/2)^{1/6}.
]
Since C_3^6=26244e^6, it is enough to show C_3<169h. The elementary exponential series gives e<27183/10000=2.7183. Exact rational arithmetic gives
[
(169h)^6-26244(27183/10000)^6
=rac{5030948981012557610171017965235761}{10^{30}}>0.
]
Hence the no-pivot density is <338. This branch is continuous.

## Scalar pivot: every five-direction remainder branch is <338

An outer scalar pivot costs d^{-1/2}; its Schur complement has at least five unit-scale spectral directions.

**No-pivot remainder.** With C_2<14,
[
H_{m no}le C_2sqrt{2/h},
qquad
14d^{-1/2}sqrt{2/h}<300.
]
After squaring, the exact positive margin is
[
300^2-14^2(121/7)(2/h)=rac{111610000}{8769}.
]

**Pair remainder.** The full pair half-potential bound gives
[
16p^{-1/4}d^{-1/2}<300,
]
and the exact squared margin is
[
300^2-16^2(121/7)cdot20=rac{10480}{7}.
]

**Nested scalar remainder.** Complete the inner scalar square. Its Schur remainder T has operator norm at least one, hence
[
P(|T-a|<ho)lemin{1,5ho^{1/4}}.
]
For delta=d/16=7/1936>1/625,
[
Elog_+rac{delta}{|T-a|}le4+4log5+logdelta.
]
Using
[
J(u)le pi+4log2+2log_+(1/|u|)
]
in the scaled convolution gives
[
sup_aE|R-a|^{-1/2}
le d^{-1/2}left(12+pi+2lograc{625d}{4}ight).
]
After the outer scalar pivot,
[
B_{m ss}
=rac1dleft(12+pi+2lograc{4375}{484}ight).
]
The degree-nine positive Taylor partial sum proves
[
log(4375/484)<1101/500:
]
[
sum_{k=0}^9rac{(1101/500)^k}{k!}-rac{4375}{484}
=rac{3077110316097587625214643241}
{1058750000000000000000000000000}>0.
]
With pi<22/7,
[
B_{m ss}
<rac{121}{7}left(12+rac{22}{7}+rac{2202}{500}ight)
=rac{4139047}{12250}
<338,
]
with final margin 1453/12250.

## Pair pivots and partner application

The definite pair branch is unchanged:
[
|p_Q|_inftylepi p^{-1/2}=20pi<63.
]

For an indefinite pair, removing the two physical pivot coordinates leaves a Schur complement with at least seven unit-scale spectral directions, so its quadratic operator norm is at least one. Since p remains exactly 1/400, the completed fleet04/B13 theorem applies directly:
[
|p_Q|_infty
le20left(8+lograc{1444}{5}ight)<274.
]

## Candidate replacement theorem

All branches are therefore below 338. Rescaling Y=KX and A/s gives
[
oxed{
s_9(A)ge s>0
Longrightarrow
|p_{X^TAX+b^TX+c}|_{infty,mathrm{ess}}
<338,rac{K^2}{s}.
}
]
The proof retains arbitrary dimension, signature, remaining spectrum, affine terms, and arbitrary independent coordinate laws with density <=K. It uses no Gaussianity, support, moment, log-concavity, rotated independence, interval extremality, or centered-uniform assumption.

Continuity is proved only in the no-pivot Fourier branch, not globally.

The existing Lean package checks the old 400-paper parameters and elementary pair/kernel algebra. It does not yet certify this new tuple or the <338 arithmetic. A companion file in this run records proposed Lean statements and is explicitly UNCOMPILED.
