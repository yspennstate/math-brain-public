SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B01, 2026-09-23T12:13:47Z.

# B01 — aggregate overlap-two payment and an explicit indefinite four-mode branch

Status: PROVED TARGET-VALID BRANCH / FULL QFORM OPEN / CONTINUITY SEPARATE.

## Completed input

This run applies account01/B01 at commit `cb4a6def5dca661cabbf4a89b52c2e0a3cba6c06`. Its averaged-frequency theorem is:

For a symmetric physical matrix (C), with
[
F(C)=sum_{i
e j}C_{ij}^2,
]
and independent cap-one inputs,
[
sup_smathbb E|X^TCX-s|^{-1/4}
le C_{m off}F(C)^{-1/8},
qquad C_{m off}<5.096.
	ag{1}
]
This comes from a random physical cut, determinant/BL averaging in the diffuse-row case, and one-row random-slope Plancherel in the heavy-row case. It does not assert pointwise scalar quadratic decay.

If (S={i,j}), (B=A[S,S]) is invertible indefinite, (D=|det B|), (kappa=s_{min}(B)), and
[
C=A[S^c,S^c]-A[S^c,S]B^{-1}A[S,S^c],
]
then the exact exterior star
[
W_2(S)=sum_{k
e lin S^c}
det A[Scup{k},Scup{l}]^2
]
satisfies
[
W_2(S)=D^2F(C).
	ag{2}
]
Combining (1) with the physical-pair logarithmic fiber estimate gives
[
oxed{
|p_{X^TAX}|_infty
le 22.385,(Dkappa)^{-1/6}W_2(S)^{-1/12}.
}
	ag{3}
]
All sums/differences generated in the proof retain their joint law; independence is used only between disjoint original-coordinate banks.

## Concrete full-target inequality

Consider the four-dimensional physical family
[
A_c=
egin{pmatrix}
1&0&0&0\
0&-1&0&0\
0&0&0&c\
0&0&c&0
end{pmatrix},
qquad |c|ge1.
	ag{4}
]
Its eigenvalues are (1,-1,c,-c), so it satisfies the original hypothesis with four eigenvalues of modulus at least one.

Choose (S={1,2}). Then
[
B=operatorname{diag}(1,-1),qquad D=kappa=1,
]
and the exact Schur complement is
[
C=egin{pmatrix}0&c\c&0end{pmatrix}.
]
Consequently
[
F(C)=2c^2,qquad W_2(S)=2c^2.
	ag{5}
]
Substitution into (3) yields, for every four independent real inputs with densities bounded by one,
[
oxed{
|p_{X^TA_cX}|_infty
le22.385(2c^2)^{-1/12}
<21.13,|c|^{-1/6}.
}
	ag{6}
]
This is an actual full-target branch with indefinite signature, arbitrary cap-one laws, fragmented and unbounded supports, and no moment assumptions.

The same conclusion survives arbitrary conditioning-generated affine terms in these four original coordinates because both the averaged-frequency input and pair-fiber estimate are uniform in affine phases.

## First remaining joint estimate

The analytic overlap-two channel is now paid whenever a base pair is quantitatively invertible. What remains is structural routing. A large global overlap-two exterior mass may be concentrated on singular or nearly singular physical pair bases, for which the reciprocal factor ((Dkappa)^{-1/6}) is unpaid.

The next exact implication is:

> From quantitatively large global overlap-two exterior mass, either extract (i) an invertible indefinite pair with paid ((Dkappa)^2W_2(S)), (ii) a definite pair paid by the elliptic fiber theorem, or (iii) a quantitatively singular pair configuration routing to an exact-null, two-hub, grouped-square, ridge, or diffuse rank-three certificate.

This is a deterministic exterior-routing problem. Uniform pointwise quadratic decay cannot solve it.

Essential boundedness is proved only in the branch above. Continuity is not claimed.
