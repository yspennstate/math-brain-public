# r62 derivation B — full s3 epsilon-log small-ball theorem

We prove the normalized statement first: independent coordinate densities <=1 and s_3(A)>=1. Let J be an interval of length ell. For ell>1 the final bound is trivial, so take 0<ell<=1.

## A. Diagonal pivot

Suppose |a_ii|>=eta=1/12. Complete the square in the ORIGINAL coordinate X_i:
[
 Q=a(X_i-mu(X_{-i}))^2+R(X_{-i}).
]
The quadratic matrix S of R is the Schur complement. The audited Schur count gives
[
 N_S(1)>=N_A(1)-1>=2,
]
so ||S||>=1.

For fixed residual value r, Lemma 5.1 bounds the conditional density by
[
 p_{Q|X_{-i}}(z)<=|a|^{-1/2}|z-r|^{-1/2}.
]
Let d(r,J) be the distance from r to J. Then
[
 int_J|z-r|^{-1/2}dz
 <=2sqrt(2),{ellover sqrt(d(r,J)+ell)}.
]
If r is outside J this follows by subtracting square roots; if r lies in J, write the two distances to the endpoints as u,v with u+v=ell and use sqrt(u)+sqrt(v)<=sqrt(2ell).

Let c be the midpoint of J. For y>=0,
[
 (y+ell)^{-1/2}
 <=1+{1over2}int_ell^1
 u^{-3/2} 1_{{y+ell<u}}du.
]
If d(R,J)+ell<u, then |R-c|<u. Since ||S||>=1, Lemma 5.4 gives
[
 P(d(R,J)+ell<u)<=19sqrt(u).
]
Hence
[
 E(d(R,J)+ell)^{-1/2}
 <=1+{19over2}log(1/ell).
]
Using |a|^{-1/2}<=sqrt(12),
[
 P(Q in J)
 <=4sqrt(6),ell
 left(1+{19over2}log(1/ell)ight).
]
Both coefficients, 4sqrt(6)<10 and 38sqrt(6)<94, are below 269.

The conditional square law is absolutely continuous for almost every X_{-i}; Tonelli/mixing therefore proves absolute continuity of Q.

## B. No diagonal pivot, but a pair pivot

Suppose every |a_ii|<1/12 and for some pair
[
 |a_ii a_jj-a_ij^2|>=1/256.
]
Condition on all coordinates except X_i,X_j.

If the binary quadratic matrix is definite, Lemma 5.2 gives conditional density at most
[
 pi(1/256)^{-1/2}=16pi<51.
]

If it is indefinite, write D=|det B|>=1/256. The conditional critical value v is a quadratic polynomial in the remaining ORIGINAL coordinates whose matrix is the Schur complement S. The Schur count now gives
[
 N_S(1)>=N_A(1)-2>=1,
]
hence ||S||>=1. This is all Lemma 5.4 requires, so
[
 sup_z Elog_+(1/|z-v|)<=2+2log19.
]
The corrected hyperbola lemma then gives, exactly as in the five-eigenvalue paper,
[
 ||p_Q||_infty
 <=D^{-1/2}
 left(6+log_+(16sqrt(D))
       +2+2log19ight).
]
Using D>=1/256 and
[
 sup_{D>0}D^{-1/2}log_+D=2/e
]
gives
[
 ||p_Q||_infty
 <16(8+4log2+2log19)+e^{-1}<269.
]
The important observation is that this pair argument needs only ONE residual unit-scale direction, so s_3(A)>=1 is sufficient.

Again conditional mixing gives absolute continuity.

## C. No pivot

Use DERIVATION_TIME_LP.md. Put
[
 C_*=19.25994030087079...
]
If C_* ell<=e^-2,
[
 P(Q in J)
 <=e C_* elllog(1/(C_*ell))
 <53 elllog(1/ell).
]
If C_*ell>e^-2, use P<=1. At the switching length
[
 ell_0=e^{-2}/C_*=0.007026775842627811...
]
one has
[
269 ell_0(1+log(1/ell_0))
=11.2618793118...>1.
]
Thus the claimed 269 endpoint dominates the trivial bound for every larger ell.

## D. Assemble and scale

The three cases are exhaustive. For normalized units,
[
 P(Q in J)
 <=min{1,269 ell(1+log_+(1/ell))}.
]

For general input density cap K and spectral scale s, set Y=KX and
[
 widetilde Q
 =Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
]
Then
[
 Q=(s/K^2)widetilde Q.
]
An interval J for Q corresponds to an interval of length
[
 delta=K^2|J|/s
]
for widetilde Q. Therefore
[
 oxed{
 P(Q in J)
 <=min{1,269 delta(1+log_+(1/delta))}.
 }
]

This proves absolute continuity and an almost-linear small-ball theorem under the exact full three-eigenvalue hypotheses. It does NOT prove a uniformly bounded density or continuity.
