# Addendum — hand proof of the Hadamard face calculation in REPORT.md

This addendum removes any dependence of the displayed constant `3e/2^(4/3)` on a finite computer enumeration.

Let the eight physical rows be indexed by `(a,s)` with `a in {1,2,3,4}` and `s in {+1,-1}`. The first four selected Sylvester-Hadamard columns give four mutually orthogonal sign vectors `h_a in {+/-1}^4`, and the fifth selected column distinguishes the two copies by `s`. Thus a row of

`M_epsilon=(H8[:,0:5]/sqrt(8)) diag(2,2,2,2,epsilon)`

has the form

`x_(a,s)=(v_a, s c)`,

where `v_a=h_a/sqrt(2)`, `v_a.v_b=2 delta_ab`, and `c=epsilon/sqrt(8)`. Put `t=epsilon^2`, so `c^2=t/8`.

## Three-row volumes

There are only two possible triple types.

**Type A: three distinct base indices.** There are `C(4,3)*2^3=32` such triples. Their Gram matrix is

`2 I_3 + c^2 ss^T`

for a sign vector `s in {+/-1}^3`. The matrix determinant lemma gives

`a_A=2^3(1+(c^2/2)*3)=8+3t/2=(16+3t)/2`.

**Type B: one base index appears with both signs, and one other base index appears once.** There are `4*3*2=24` such triples. Subtracting the two repeated-base rows isolates `(0,2c)`; an elementary Gram determinant (or one Gram--Schmidt step followed by the orthogonality of the two base vectors) gives

`a_B=2t`.

These counts total `32+24=56=C(8,3)`.

## Four-row volumes

Again there are three support types.

**Four distinct base indices.** There are `2^4=16` sets. Their Gram matrix is `2I_4+c^2ss^T`, so

`d_4=2^4(1+(c^2/2)*4)=16+4t=4(t+4)`.

**Three distinct base indices, one repeated with both signs.** There are `4*C(3,2)*2^2=48` sets. At `t=0` the first four coordinates have rank three; the repeated-sign difference supplies exactly the fifth direction. Gram--Schmidt gives

`d_3=4t`.

**Two distinct base indices, both repeated with both signs.** There are `C(4,2)=6` sets. All four rows lie in the span of the two base directions and the fifth direction, so the rank is at most three and

`d_2=0`.

The counts total `16+48+6=70=C(8,4)`. Summing the four-volumes gives

`E4=16*4(t+4)+48*4t=256(1+t)`,

agreeing with the singular-value calculation `e4(4,4,4,4,t)`.

## Face sums b_S and the two tau values

For a Type-A triple (three distinct bases), there are five possible fourth rows. Two of them are the two signs of the missing fourth base and produce four-distinct-base packets of volume `4(t+4)`. The other three are the opposite-sign copies of the three bases already present and produce volume `4t`. Hence

`b_A=2*4(t+4)+3*4t=4(8+5t)`,

and

`tau_A=b_A/a_A=8(8+5t)/(16+3t)`.

For a Type-B triple (one repeated base and one single base), adding the opposite sign of the single base produces a two-pair rank-three packet with volume zero. The four rows coming from either sign of either of the two unused base indices produce the three-distinct-base volume `4t`. Therefore

`b_B=4*4t=16t`,

and

`tau_B=b_B/a_B=8`.

Since the deletion law is `mu(S)=b_S/[4E4]`, its total masses on the two types are

`m_A=32 b_A/[1024(1+t)]=(8+5t)/[8(1+t)]`,

`m_B=24 b_B/[1024(1+t)]=3t/[8(1+t)]`.

Thus

`tau_geo=tau_A^(m_A) 8^(m_B)`.

Weighted AM--GM gives

`tau_geo <= m_A tau_A+8m_B
 = 2(17t^2+64t+32)/[(1+t)(3t+16)]`.

Finally,

`4(1+t)-[m_A tau_A+8m_B]
 =6t(2t^2+9t+2)/[(1+t)(3t+16)] >=0`.

Therefore

`tau_geo<=4(1+t)`

for every `t>=0`, and consequently the exact entropy currency satisfies

`G=4E4/tau_geo=1024(1+t)/tau_geo>=256`.

With the row-transitivity argument in REPORT.md, `q=1`, so the entropy-weighted third-volume theorem gives rigorously, without a numerical enumeration,

`||p_(X^T A_epsilon X)||_infinity <=3e*256^(-1/6)=3e/2^(4/3)`.

The finite `CHECKS.json` remains only a consistency check of these identities.
