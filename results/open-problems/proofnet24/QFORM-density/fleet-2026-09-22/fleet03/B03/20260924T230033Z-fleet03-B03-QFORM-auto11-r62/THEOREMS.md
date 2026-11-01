# r62 theorem statements

Pinned corrected paper: `5ba2a4d6b689721601cce7ec7e22ffea9fa98f90`,
`proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/paper.tex`,
blob `bbebd6f6c5a27e9f639186a305008ab43a481e70`.

The complete corrected source was independently read. The B03 copy/conditioning interface passes: the decoupling theorem copies a whole original-coordinate bank and never treats a coordinate difference as independent of its conjugate sum.

## Theorem 1: QFORM-3EIG-NOPIVOT-WEIGHTED-L2-v1

Normalize to independent coordinate densities at most one, (s_3(A)>=1), and no pivot at eta=1/12, zeta=1/256. Put
[
 gamma_2=(44-15 sqrt(2))/96,
 qquad
 a_*=2^(3/4) pi e/gamma_2.
]
Then
[
 |phi_Q(t)| <= min(1,a_*/|t|).
]
For every -1<sigma<1,
[
 oxed{
 int_R |t|^sigma |phi_Q(t)|^2 dt
 <=4 a_*^(1+sigma)/(1-sigma^2).
 }
]
In particular
[
 int |t|^(-1/2)|phi_Q(t)|^2dt
 <=(16/3)sqrt(a_*)
 =41.48595888463038...
]
and for an independent copy (Q') of the whole scalar output this integral equals
[
 sqrt(2 pi) E|Q-Q'|^(-1/2).
]

## Theorem 2: QFORM-3EIG-NOPIVOT-ALL-FINITE-LP-v1

Put
[
 C_*=a_*/pi=2^(3/4)e/gamma_2=19.25994030087079...
]
In the same no-pivot branch the law has a density and for every finite p>=2,
[
 oxed{ ||p_Q||_p <= (C_* p)^(1-1/p). }
]
For every interval J,
[
 P(Q in J)<=(C_* p |J|)^(1-1/p).
]
If (C_*|J|<=e^(-2)), choosing
(p=log(1/(C_*|J|))) gives
[
 oxed{
 P(Q in J)
 <=e C_* |J| log(1/(C_*|J|)).
 }
]

## Theorem 3: QFORM-3EIG-LOG-SMALLBALL-v1

Let X_i be independent real variables with densities at most K. Let A=A^T satisfy s_3(A)>=s>0 and let
[
 Q=X^T A X+b^T X+c
]
with arbitrary b,c. Then the law of Q is absolutely continuous. For every interval J, set
[
 delta=K^2 |J|/s.
]
Then
[
 oxed{
 P(Q in J)
 <=min(1,269 delta (1+log_+(1/delta))).
 }
]
This matches all quantifiers of the owner's three-large-eigenvalue problem but retains one logarithm instead of the desired universal linear bound.

Full three-eigenvalue L-infinity remains OPEN. Full-target continuity remains OPEN.
