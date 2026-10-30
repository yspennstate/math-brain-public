# A031 independent acceptance of A096-UNIVERSAL-LEVEL12-ERASURE@1

Verdict: ACCEPT_AT_STATED_SCOPE, pending supervisor index adoption. No repair
or new hypothesis is supplied. This accepts H2<=155600/50301 I and
T12<=16700/2187 I<8I for every actual uniform-cube Boolean sign. It does
not accept any bound on edges beginning at spectral level >=2.

Sources read in full for this claim: A096 run 20261011T234252Z
DERIVATION.md, REPORT.md equations (1)-(7) and scope controls, CLAIMS.json.
The original theorem has no pending external proof dependency.

Reconstruction: a physical derivative h is 0,+1,-1, so support density
epsilon equals E h^2 and |h| equals its support indicator. For its linear
projection L with variance D, orthogonality gives E hL=D. For the uniform
measure conditioned on the derivative support, relative entropy to the
uniform measure is ln(1/epsilon). The elementary entropy variational
inequality, or Jensen applied to the exponential likelihood, gives
E_support |L| <=[ln(1/epsilon)+ln E exp(t|L|)]/t.
The independent Rademacher product mgf bounds the last logarithm by
ln2+t^2 D/2. Optimize t to get D<=2 epsilon^2 ln(2/epsilon).
All zero cases are immediate. This is the source proof's substantive
Booleanity input; it cannot be replaced by norm-one spectral energy.

Normalize the occupied pair masses by W2. The influence pair reference
Q_ij=2 epsilon_i epsilon_j/I^2 has total at most one and covers every
occupied pair. Gibbs applied after reference normalization therefore gives
H2<=sum_i D_i log2(1/epsilon_i)+W2 log2(I^2/(2W2)).
The negative normalization correction can be dropped, not inverted.
For t=-ln epsilon, the first term per unit influence is at most
2exp(-t)(t^2+t ln2)/ln2. The maxima of t^2exp(-t) and texp(-t)
give 8/(e^2 ln2)+2/e. The inequality ln z<=2sqrt(z)/e and W2<=1
pay the second term by sqrt2/(e ln2) I, also when its logarithm is negative.
Finally phi(x,y)<=y log2(1/y)+y/ln2 when x+y<=1. Each pair appears
twice and 2W2<=I, establishing the claimed erasure constant.
The saved exact rational arithmetic reconstructs both published rational
constants from e>27/10, ln2>69/100, sqrt2<71/50.

Executed independent checks use direct physical flip indicators and direct
character sums, not the author's Walsh implementation: every Boolean sign
at n<=3 and every physical coordinate. Sparse derivative inequalities use
proved rational-log lower bounds. The normalized product spectral law at
theta=1/128 violates the sparse-derivative inequality by the exact integer
comparison 127*127^126>16*128^126, while 2ln256<16. The source's
normalized two-level real family at n=65537 has T12/I>=10, exceeding
16700/2187, without allocating a vector of that dimension. These are
non-Boolean controls, not candidate FEI counterexamples.

Command: python -X utf8 code/review_level12.py. Exact counts and runtime
are in out/LEVEL12_REVIEW.json; specification was saved before execution.
A031 supplies no substantive repair and is not a contributor to this
version. Original files and shared registries are untouched. Acceptance
does not imply supervisor adoption or downstream mathematical use.
