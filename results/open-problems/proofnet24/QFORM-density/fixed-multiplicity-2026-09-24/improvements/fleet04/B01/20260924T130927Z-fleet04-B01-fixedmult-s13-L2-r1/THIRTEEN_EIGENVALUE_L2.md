# Thirteen-eigenvalue dimension-free L2 density theorem

Run: `20260924T130927Z-fleet04-B01-fixedmult-s13-L2-r1`  
Pinned baseline: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Theorem

Let (X=(X_1,ldots,X_n)) have independent real coordinates with probability densities bounded by (K), where (K>0). Let (A=A^T), (binmathbb R^n), (cinmathbb R). If

[
s_{13}(A)ge s>0,
]

then (Q=X^TAX+b^TX+c) has a density in (L^2(mathbb R)) and

[
oxed{ |p_Q|_2le sqrt{6010},rac{K}{sqrt s} }.
]

No sign, moment, support, smoothness, identical-law, or remaining-spectrum assumption is imposed. Continuity is not asserted.

## Proof in the normalized case

Assume (K=s=1), and use the manuscript parameters

[
eta=1/100,qquad kappa=1/80^2.
]

### No-pivot branch

Apply Proposition `prop:volume` with (k=4). Since (4k-3=13),

[
V_4(A)gekappa^4.
]

The random-cut lemma gives a disjoint original-coordinate partition (Isqcup J) such that the crossing matrix (M=A_{I,J}) satisfies

[
Z_4(M)ge4^{-4}kappa^4.
]

The crossing-volume envelope therefore gives

[
|phi_Q(t)|
le min{1,u/|t|},
qquad
u=pi e,Z_4(M)^{-1/8}
le160pi e.
]

Consequently

[
|phi_Q|_2^2
le
2int_0^u1,dt+
2u^2int_u^infty t^{-2},dt
=4u
le640pi e.
]

An (L^2) characteristic function yields an (L^2) density. For completeness, convolve the law with the manuscript Gaussian (g_arepsilon). Its density has Fourier transform (e^{-arepsilon t^2}phi_Q(t)), which converges to (phi_Q) in (L^2). Plancherel gives convergence of the Gaussian-smoothed densities in (L^2) to an inverse transform (p). The smoothed laws also converge weakly to the law of (Q), so testing against compactly supported continuous functions identifies the law with (p(x),dx). Plancherel then yields

[
|p_Q|_2^2
=rac1{2pi}|phi_Q|_2^2
le320e
<6010.
]

### Pivot branches

If (|a_{ii}|geeta), the Schur spectral-count lemma leaves at least twelve eigenvalues of modulus at least one. In particular Proposition `prop:nine` applies to the residual quadratic polynomial, and the manuscript scalar profile gives

[
|p_Q|_inftyle eta^{-1/2},601=6010.
]

For a definite principal pair pivot,

[
|p_Q|_inftylepieta^{-1/2}=10pi<6010.
]

For an indefinite principal pair pivot, the Schur complement retains at least eleven unit spectral directions, hence at least one. The manuscript's hyperbolic envelope and logarithmic-potential estimate give the same displayed main-proof bound (<251<6010).

Thus in every pivot branch,

[
|p_Q|_2^2
le|p_Q|_infty|p_Q|_1
le6010.
]

Combining the no-pivot and pivot cases proves

[
|p_Q|_2lesqrt{6010}
]

in the normalized setting.

## Scaling

Set (Y=KX) and

[
widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q.
]

The normalized theorem applies to (widetilde Q). With (a=K^2/s),

[
p_Q(x)=a,p_{widetilde Q}(ax),
qquad
|p_Q|_2=a^{1/2}|p_{widetilde Q}|_2.
]

Therefore

[
|p_Q|_2lesqrt{6010},K/sqrt s.
]

## Scope and obstruction

This is a genuine fixed-multiplicity improvement for finite-norm regularity, not an (L^infty) theorem. At order four the envelope is only (1/|t|), which belongs to (L^2) but not (L^1). A bare (1/|t|) envelope cannot imply bounded density: the product of two independent uniform variables has a logarithmically unbounded density while its characteristic function has this decay. Any 13-eigenvalue (L^infty) theorem must use additional quadratic/product structure beyond absolute Fourier inversion.
