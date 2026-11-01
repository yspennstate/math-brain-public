SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B01, 2026-09-23T13:10:03Z.

# B01 — scalar-pivot routing of a nearly singular overlap-two star

Status: PROVED NEW DETERMINISTIC ROUTING LEMMA AND PAID WELL-CONDITIONED BRANCH / FULL QFORM OPEN / CONTINUITY SEPARATE.

## 1. Completed averaged-frequency input

The completed fleet01/B01 theorem at
`yspennstate/math-open-problems@cb4a6def5dca661cabbf4a89b52c2e0a3cba6c06`
is used at the following actual inequality.

For an invertible indefinite original-coordinate pair (S={i,j}), put
[
D=|det A[S,S]|,qquad kappa=s_{min}(A[S,S]),
]
and
[
W_2(S)=sum_{substack{k,l
otin S\k
e l}}
det A[Scup{k},Scup{l}]^2.
]
Then the aggregate quarter-Riesz estimate followed by the physical-pair logarithmic fiber theorem gives
[
oxed{
|p_{X^TAX}|_infty
le 22.385,(Dkappa)^{-1/6}W_2(S)^{-1/12}.
}
	ag{1}
]
Thus, for every (eta>0),
[
(Dkappa)^{1/6}W_2(S)^{1/12}geeta
quadLongrightarrowquad
|p_Q|_inftyle22.385,eta^{-1}.
	ag{2}
]
No uniform pointwise scalar quadratic decay is used.

The first unproved case is that (W_2(S)) is large while the pair base is singular or nearly singular. The next lemma routes that case before dividing by (D) or (kappa).

## 2. Exact scalar-pivot identity

Write the physical pair block as
[
B=A[S,S]=
egin{pmatrix}a&b\ b&cend{pmatrix},
qquad a
e0,
]
and let (K=S^c). Schur-complete only the original scalar coordinate (i):
[
widetilde A
=A[-i,-i]-a^{-1}A[-i,i]A[i,-i].
	ag{3}
]
This operation does not rotate random variables. Define
[
delta=widetilde A_{jj}=c-rac{b^2}{a}
=rac{det B}{a},
	ag{4}
]
[
ell_k=widetilde A_{jk}
=A_{jk}-rac b a A_{ik},
qquad
M_{kl}=widetilde A_{kl}
=A_{kl}-rac1aA_{ik}A_{il}.
	ag{5}
]

For distinct (k,lin K), scalar block elimination gives the exact identity
[
oxed{
det A[Scup{k},Scup{l}]
=a(delta M_{kl}-ell_kell_l).
}
	ag{6}
]
Consequently,
[
oxed{
W_2(S)
=a^2sum_{k
e l}(delta M_{kl}-ell_kell_l)^2.
}
	ag{7}
]
This remains meaningful at (det B=0); no pair inverse appears.

## 3. Near-singular star dichotomy

Put
[
F(M)=sum_{k
e l}M_{kl}^2,
qquad
L(ell)=sum_{k
e l}ell_k^2ell_l^2.
	ag{8}
]

### Theorem 3.1

For every pair with (a
e0), at least one of the following holds:
[
oxed{
|delta|^2F(M)ge rac{W_2(S)}{4a^2},
}
	ag{9}
]
or
[
oxed{
L(ell)gerac{W_2(S)}{4a^2}.
}
	ag{10}
]

#### Proof

Regard the off-diagonal arrays in (7) as vectors in (ell^2({(k,l):k
e l})). Their norms satisfy
[
|,delta M_{m off}-(ellell^T)_{m off},|_2
=rac{sqrt{W_2(S)}}{|a|}.
	ag{11}
]
If (9) fails, then
[
|delta M_{m off}|_2
<rac{sqrt{W_2(S)}}{2|a|}.
]
The reverse triangle inequality in (11) gives
[
|(ellell^T)_{m off}|_2
gerac{sqrt{W_2(S)}}{2|a|}.
]
Squaring is exactly (10). (square)

Thus a nearly singular pair cannot hide a large overlap-two star. It must leave either aggregate off-diagonal curvature in the scalar Schur complement or a diffuse physical leakage vector.

## 4. Disjoint-bank extraction in the leakage branch

### Corollary 4.1

If (10) holds, there are disjoint original-coordinate banks (I,Jsubset K) such that
[
oxed{
|ell_I|_2,|ell_J|_2
ge rac{sqrt{W_2(S)}}{4|a|}.
}
	ag{12}
]

#### Proof

Color every coordinate of (K) independently red or blue with probability (1/2). For (I) red and (J) blue,
[
mathbb Eig[|ell_I|_2^2|ell_J|_2^2ig]
=rac14sum_{k
e l}ell_k^2ell_l^2
=rac14L(ell).
	ag{13}
]
Some coloring therefore has product at least (L(ell)/4). Combine with (10) and take square roots. (square)

This is an actual original-coordinate two-bank certificate. It preserves arbitrary dense (M), all dependence created by scalar completion, translations, fragmented supports, and unbounded tails. It does not treat (M) as a small product twist.

## 5. Exact-null endpoint

When (det B=0), equation (4) gives (delta=0), so (7) becomes
[
W_2(S)=a^2L(ell).
	ag{14}
]
Hence the leakage branch is automatic and Corollary 4.1 gives
[
oxed{
|ell_I|_2,|ell_J|_2
ge rac{sqrt{W_2(S)}}{2|a|}.
}
	ag{15}
]
(The constant improves because no triangle split is needed.)

Thus the exact singular-pair endpoint is reduced to a quantitative two-bank mixed-hub problem, rather than being lost to a reciprocal determinant.

## 6. What remains

The averaged-frequency theorem pays the well-conditioned pair through (1). The new lemma routes the singular/near-singular branch to:

1. aggregate Schur off-diagonal energy (9), where the quarter-Riesz mechanism can be applied to the residual curvature; or
2. two disjoint leakage banks (12), to which the mixed-hub/two-bank smoothing theorem must be applied while retaining the arbitrary dense (M).

The remaining analytic step is to combine the leakage-bank product in (12) with arbitrary dense self-couplings in (M), without conditioning one projected coordinate and without calling the nonseparable remainder small. This is strictly narrower than the previous “near-singular pair” gap.

Full QFORM remains open. Essential boundedness is proved only in the paid branch (1). Continuity is not claimed.
