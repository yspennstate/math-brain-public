# Rare activation already satisfies finite bounded-degree phase normal form

All cubes are finite and uniform over F2. Entropy H is normalized squared
Walsh entropy in bits, I is physical total influence, and D_K=H-KI.
This is an endpoint admission theorem, not a proof or disproof of FEI.

## 1. Two elementary estimates, with all Fourier rows retained

Let f be a Boolean sign with delta=P(f=-1). Let q=(-1)^P be another
Boolean sign, and let J be its set of essential PHYSICAL coordinates,
r=|J|. Multiplication by q acts orthogonally within each Fourier block
with fixed outside label T on J-complement. Indeed this block is the
Walsh transform on J of the partial outside coefficient
F_T(x_J)=E_outside[f(x) chi_T(x_outside)]. Multiplying it by the sign
q(x_J) preserves its squared norm. Therefore the probability marginal
of squared Fourier coefficients on outside labels is exactly unchanged.
Conditional entropy on the r inside labels lies in [0,r]. Hence

    H(qf)-H(f) <= r.                                      (1)

No support component, sign, or mixed label is removed. Zero-mass blocks
contribute zero. The argument also works when J is empty.

Write d_i h(x)=1[h(x)!=h(x+e_i)]. Since d_i(qf) is the XOR of d_iq and
d_if, for each i in J,

    Inf_i(qf)-Inf_i(f)
      = Inf_i(q)-2 P(d_iq=1 AND d_if=1)
      >= Inf_i(q)-2 Inf_i(f) >= Inf_i(q)-4 delta.           (2)

The last inequality uses {d_if=1} subset {f(x)=-1} union
{f(x+e_i)=-1}; no independence is assumed. Coordinates outside J have
EXACTLY unchanged influence. Thus

    I(qf)-I(f) >= I(q)-4 delta r.                          (3)

## 2. Degree and the quantitative phase gap

A nonzero multilinear F2 polynomial of degree at most s is nonzero on
at least fraction 2^-s of its cube. For completeness, induct on its
actual degree/number of variables. If independent of a variable, remove
it. Otherwise write P=x_i A+B with nonzero A of degree at most s-1.
For every assignment where A=1, precisely one of P(0),P(1) equals1.
Induction gives probability at least (1/2)*2^-(s-1)=2^-s.
A nonzero constant is the base case, including s=0.

If deg(P)<=d, d>=1, every essential derivative P(x)+P(x+e_i) is a
nonzero polynomial of degree at most d-1. Consequently

    I(q) >= 2^(1-d) r.                                    (4)

Together (1)--(4) prove the dimension-free bound

    D_K(qf)-D_K(f)
      <= -r gamma,   gamma=K(2^(1-d)-4 delta)-1.           (5)

For K>2^(d-1) and delta<(2^(1-d)-1/K)/4, gamma>0.
Every NONCONSTANT degree<=d phase strictly reduces the deficit.
The two constant phases preserve H,I and D. This proves global finite
phase-orbit optimality, not merely stationarity under a list of moves.

In particular for cubic phases it suffices that

    K>4 and delta<(K-4)/(16K).                             (6)

For quadratic phases replace4 by2 in the K threshold and use
delta<(1/2-1/K)/4. The proof covers physical degree, not Fourier degree.

## 3. Joint affine/phase orbit: no change of the original pair

Suppose additionally that f minimizes I under all invertible affine
INPUT maps. For each such A, f_A=f composed with A still has negative
mass delta and H(f_A)=H(f), with I(f_A)>=I(f). Apply (5) to f_A:

    D_K(q f_A) <= D_K(f)-r gamma.                          (7)

Affine substitution preserves degree<=d, so every member of the finite
joint affine/degree<=d phase orbit has exactly this form. Thus f itself
is a global maximum of D_K in that orbit, with a strict gap against
every nonconstant phase. No root replacement, changed partition, or
renewed bank is needed. Global sign is harmless. An input-affine minimum
exists in the finite affine group; this existence is not FEI.

## 4. Arbitrary seed admission, retaining the paid ORIGINAL pair

Consume the previously independently reviewed A005 paid-pair embedding
as restated and extended in A055 stage19 PROOF Sections1--3. Given any
positive-entropy Boolean seed, take its full-span affine-minimal
compression g with H0=H(seed), q0=I(g)<=I(seed), and mu=E g, |mu|<1.
For t positive, put k=max(3,ceil(sqrt(t))), p=2^-k,

    Q=(-1)^(ab+ac+bc+za),
    F_t=1+1[k controls all0]*(Q g^tensor(t)-1).

The consumed construction is already full-span and affine-minimal;
its original displayed pair is (a,b), not a newly chosen affine pair.
It has delta_t<=p, I(F_t)->0, and

    H(F_t)/I(F_t) -> H0/q0 >= H(seed)/I(seed).              (8)

The explicit non-character shear releases p/4 at original reach1/4;
its queried influence is p. Its complete local bill divided by p tends
to4, so it is strictly paid for every fixed K>16/5, eventually.
All complete original terminals and the one existing bank are retained.
For every original proper block A, A055 proves simultaneously

    N_A*=E[(H(child)-K a(child))_+] ->0,
    |S_A*|=|E[K a(child)-H(child)]| ->0.                   (9)

Fix an integer d>=1 and K>max(2^(d-1),16/5). Since p->0,
gamma_t>=K(2^(1-d)-4p)-1>0 eventually. Equations(5)--(7) now apply
to THIS SAME F_t, preserving its original paid pair and every reserve.
In particular the construction is globally cubic-phase/affine optimal
at every fixed K>4, eventually. No difficult bounded-degree phase FEI
assumption is needed; (4) is elementary and (1) keeps all mixed rows.

Therefore, for each fixed K>max(2^(d-1),16/5) and each epsilon>0,
FEI(K) on roots satisfying ALL of the following implies full FEI(K):
full-span affine minima; global joint degree<=d phase/affine deficit
optimality at that SAME K; I<epsilon; an explicitly paid original pair;
and N_A*<epsilon, |S_A*|<epsilon for EVERY proper original block.
The converse is immediate. For each seed choose arbitrarily large t,
apply the endpoint inequality, and use the finite-function ratio limit
(8). Zero-entropy seeds are trivial. This equivalence uses no universal
optimizer, no claimed positive witness at high K, and no tail continuity.

If the canonical seed has H0/q0>K, these same roots also maximize their
OWN ratio R_t=H(F_t)/I(F_t) in the finite joint orbit, eventually: R_t>K,
the threshold (2^(1-d)-1/R_t)/4 is at least its K counterpart, and (7)
at rate R_t makes every competitor's D_(R_t)<=0. This is an initial
normalization statement, never permission to change a spent bank's rate.

## 5. Exact obstruction and scope

If H0-Kq0>0, eventually F_t has D_K(F_t)>0 while its displayed paid
pair has S_pair*<-D_K(F_t)<0 and N_pair*>D_K(F_t)>0. Its normalized
failure is bounded below in the limit by H0/q0-K. Thus adding global
cubic-phase optimality DOES NOT repair the exact child eligibility
failure in rare-core examples. Approximate absolute eligibility of ALL
blocks, even together with this new normal form, is still insufficient.

This does not embed a violating seed into a genuinely least-essential-
dimension witness: its nonnegative complete smaller-child reserves are
precisely what fails. Nor does it imply the phase condition is useless
when combined with those exact reserves. It identifies which additional
condition must do essential work.

FIRST UNSUPPORTED UNIVERSAL LINE: combine exact nonnegative complete
smaller-child reserves with A052's original-pair signed cubic alignment
to force adequate UNUSED independent quotient-rank funding, on one
original proper pair of a sufficiently high-K genuine critical source,
from the SAME bank with all mixed Fourier rows. The global cubic-phase
normal form alone supplies no admission obstruction to an arbitrary seed.
Full FEI remains OPEN; no universal constant is improved.

## 6. Where bounded degree is essential

For a conditional violating seed write G_t=Q g^tensor(t)=(-1)^P_G,
and let A be the k-control activation polynomial. In F2 notation
F_t=(-1)^(A P_G). Multiplication by the actual phase

    q_erase=(-1)^((1+A)P_G)

maps F_t EXACTLY to G_t. Since the controls are disjoint from G_t,
deg(q_erase)=k+deg(P_G), with deg(P_G)=max(2,deg(g)) fixed in t.
There is no top-term cancellation: choose any highest-degree data
monomial and multiply it by the unique full control monomial of A.
Its coefficient is1. This degree diverges along the activation sequence.

The consumed exact Q identities give
D_K(G_t)=t(H0-Kq0)+4-2K, whereas D_K(F_t)/t->0.
If H0-Kq0>0, then D_K(G_t)>D_K(F_t) eventually. Thus the SAME rare
roots fail global optimality under unrestricted-degree output phases.
The exact eraser and its degree identify why the fixed-degree result
does not silently extend to all phase functions. No assertion that this
degree is minimal for every profitable phase is made.

For the actual point8 example from the previously checked paid-pair
certificate, K=15/4,k=10000,t=100000000, the NEW quadratic-phase gap is
gamma>=7/8-15*2^-10000>3/4. Therefore this same explicit positive-deficit
root, original paid pair and absolute-all-block reserve obstruction also
have global joint QUADRATIC/affine optimality, with strict gap>3r/4.
This finite example is below the cubic thresholdK>4; it is not presented
as an actual high-K violation or a disproof of FEI.
