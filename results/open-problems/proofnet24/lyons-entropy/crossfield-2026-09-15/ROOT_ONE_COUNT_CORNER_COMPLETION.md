# Root continuation — a far-corner bound and a compact remaining region

This root derivation is not an additional sub-agent. It concerns the same exact one-count Schur matrix as X069, X074, X083 and X084. The analytic corner argument below and the outward integer interval certificate now prove the comparison on the ENTIRE two-parameter square. The unrestricted Lyons conjecture and the additional nonorthogonal-column parameter remain open.

Write r=tanh R, s=tanh S and, by symmetry, R≥S≥0. In X069's orthogonal sum/difference coordinates put t=R+S, d=R−S, z=cosh t, w=cosh d, l=log z, m=log w. Its exact formulas are

    Uhat11=zw+2+z/w+w/z−1/(zw)−l−m,
    Uhat22=zw−1/(zw)+l+m,
    Uhat12=sinh t sinh d (1−1/(zw)),
    B=[[t−alpha m, beta m],[d−beta l, alpha l]],
    alpha=sinh t/(z+w), beta=sinh d/(z+w).

The required sufficient inequality is Uhat≥B^T B. Both alpha and beta lie in [0,1], and 0≤m≤d≤t, 0≤l≤t. Consequently the four entries of B have absolute values at most t,d,t,t, respectively, so

    ||B||_op²≤||B||_F²≤3t²+d²
             =4(R²+RS+S²)≤12R².

Each diagonal of Uhat is at least zw−1−l−m; its off-diagonal is nonnegative and at most sinh t sinh d. Therefore

    Uhat≥[cosh(2S)−1−2R]I,
    Uhat−B^T B≥[cosh(2S)−1−2R−12R²]I.        (1)

Set a=sech²R and b=sech²S. If a≤b²/256, X084 already proves the comparison. Otherwise cosh R<16cosh²S. Since e^R≤2cosh R and cosh S≤e^S,

    R<2S+log32<2S+4.

Combining this with (1) gives

    Uhat−B^T B≥F(S)I,
    F(S)=cosh(2S)−4S−9−12(2S+4)².             (2)

For S≥5 this is strictly positive. Indeed e²>7 follows from the exponential series, so cosh10>7^5/2=16807/2, while 4·5+9+12·14²=2381. Also F'(5)=2sinh10−676>0, and F''(S)=4cosh(2S)−96>0 for S≥5. These are elementary exact bounds. Thus (2) stays positive on the entire half-line.

**Conclusion.** U≥TT^T whenever min(R,S)≥5, in addition to the previously proved domains. X074's established sector and measured-touching arguments promote this to the same full sixteen-direction measured family with orthogonal balanced columns.

Outside this corner and X084's curved boundary domain, the remaining ordered parameters satisfy

    0≤S≤5,  S≤R≤2S+4≤14.

X083 removes S≤atanh(1/5), and X074 removes R≤atanh(3/5). The only remaining sufficient-matrix problem is therefore contained in the compact region

    atanh(1/5)≤S≤5,
    max(S,atanh(3/5))≤R≤2S+4.

This compact reduction is not itself a positivity proof. A useful numerical conditioning is the congruence diag(sech R,sech S) applied to U−TT^T; the exact target remains the original integrated logarithmic matrix. A rigorous interval or positive-basis certificate on the compact region could combine with the analytic domains to prove the complete sufficient inequality. No finite grid without certified cell bounds is adequate.

## Certified compact completion

The proposed certificate has now succeeded. The executable proof is in
`computations/root_one_count_compact/certify.py`, with its exact positive boxes
in `certificate.json`. `replay.py` independently reconstructs the covering
partition and recomputes all box inequalities; its output is in `replay.json`.

The starting rectangle is R in [2/3,14], S in [1/5,5]. It contains the remaining
region because atanh(3/5)>2/3 and atanh(1/5)>1/5. Closed bisections retain every
point with S≤R≤2S+4. Only boxes strictly outside that region are discarded.
The certificate uses 206 positive boxes and 36 outside boxes. Replaying the
exact partition establishes both positivity and coverage, including boundaries.

For clarity, here is the exact matrix evaluated on each box. Put

    a=sech²R, b=sech²S, r=tanh R, s=tanh S, c=a+b−ab,
    k=(1/2)log(c/(ab)), P=atanh(rs),
    T11=R+sP, T12=S−sk, T22=S+rP,
    T21=(1−r)R+r[log(1+r)−(1/2)log(1+a s²/b)].

The last expression equals R−rk exactly, keeping its cancellation inside a
logarithm. For D=diag(sqrt(a),sqrt(b)), the congruent remainder M=D(U−TT^T)D is

    M11=2+2a s²/c−a(T11²+T12²),
    M22=2+2b r²/c−b(T21²+T22²),
    M12=sqrt(ab)[2/c−2k−T11T21−T12T22].

Every certified box has a strictly positive outward lower bound for M11 and
det M. Sylvester's criterion proves M>0 throughout that entire box, hence
U−TT^T>0 there.

Every arithmetic endpoint is an integer divided by 10^24. Addition is exact;
multiplication and division round the extrema of the four endpoint products
or quotients outward. Squaring includes zero when necessary. Square roots use
integer square roots with outward rounding. No floating point sign is used.

For exp(x), x≥0, halve its argument until at most 1/2, enclose the Taylor sum
through degree 32, and bound the remaining tail by its first term divided by
1−x/34; repeated interval squaring restores the argument. For log(x), scale
by exact powers of two into [1,2], put z=(x−1)/(x+1), and use the first 40 terms
of 2 sum z^(2j+1)/(2j+1). Its positive tail is bounded by
2 z^81/[81(1−z²)]. The same series encloses log 2. Monotonicity encloses an
interval argument from its two endpoints. These series follow respectively
from the exponential series and integration of the geometric series, and
their explicit tails justify every transcendental enclosure.

The initial draft computation did not certify any boxes because premature
reciprocal rounding lost a tiny positive quantity; it also lacked reverse
division. Direct outward quotient arithmetic fixed both issues. Only the
successful final code and its replayed certificate support the theorem.

## Result and exact scope

Combining the compact certificate with X074's central square, X083's strip,
X084's curved boundary and the analytic far corner proves

    U(r,s)−T(r,s)T(r,s)^T ≥ 0 for every 0≤r,s<1.

X069's global lower-block estimate and square completion therefore give Q≥0
on the entire square. X074's other-sector identity, X037's cross-block theorem,
and the physical parity decomposition prove the complete sixteen-direction
measured entropy Hessian at every balanced four-site base

    K=I_4/2+[[0,Z],[Z*,0]],
    2Z=2^(−1/2)[[sqrt(r),sqrt(s)],[sqrt(r),−sqrt(s)]],
    0≤r,s<1,

including fixed measured diagonal gauge phases and coordinate permutations.
Both columns have equal coordinate moduli and are orthogonal. General
nonorthogonal balanced columns have an extra determinant parameter and are
NOT covered by this theorem. Arbitrary unitary rotation of the retained
measured pair is not permitted. Boundary or distant-endpoint Jensen claims
require a separately justified path remaining in a certified region.

Reproduce with `python computations/root_one_count_compact/certify.py` and
`python computations/root_one_count_compact/replay.py`. This is a finite
rigorous interval proof of a restricted scalar matrix inequality, combined
with analytic boundary domains, not a numerical grid claim and not a proof
of the general entropy conjecture.
