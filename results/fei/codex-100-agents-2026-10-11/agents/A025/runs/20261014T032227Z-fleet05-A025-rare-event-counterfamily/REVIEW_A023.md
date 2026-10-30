# Independent reconstruction: A023 v3 additional whole-block theorem

Verdict: HOLDS at the additional whole-block scope, including its stated
entropy, minority/KL, coordinate reserve, bent/edit and fresh-activation
consequences. The earlier bundled v1/v2 claims are excluded from this
acceptance. Source: A023 run 20261014T022245Z, PROOF.md and CLAIMS.json,
claim A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER v3. No repair is supplied;
A025 is an independent reviewer for this source addition, not a contributor
to its statement. The nested counterfamily in this run is a separate
extension that the source explicitly leaves unproved.

Put alpha=2^-s, gamma=P(G!=H), Delta=(Hhat-Ghat)/2. Parseval gives
sum Delta^2=gamma. At a live query, rho=2^-(j-1), d=rho gamma. For each
nonempty residual selector label, both parent sector coefficients have
magnitude rho |Delta_T|; there are rho^-1-1 such labels. Their total
conditional entropy is exactly 2(1-rho)d. The empty selector rows have
derivative mass rho^2 gamma and combined row mass at most one. The binary
entropy remainder and log-sum bound their cost by
rho^2 gamma log2(e/(rho^2 gamma)). These are the actual Boolean Fourier
rows, with no disjointness or balance assumption.

Physical reach times d is 2alpha gamma. Independently expanding the sums
sum rho=2(1-alpha) and sum l rho=2[1-(s+1)alpha] gives

    E_B<=2(1-2alpha)I_S
         +4alpha gamma(1-alpha)[log2(1/gamma)+c],
    I_S=2s alpha gamma, c=1/ln2.

For the disagreement set, internal edge induction gives
edges(E)<=|E| log2(|E|)/2: split child sizes a<=b, use at most a joining
edges, and apply h2(a/(a+b))>=2a/(a+b). Subtract from n|E| to obtain
gamma log2(1/gamma)<=I(GH)/2. Therefore R=2alpha(1-alpha)I(GH) is a
valid single whole-block logarithmic reserve. The product edge flips iff
exactly one source edge flips, so each coordinate has
Inf_i(GH)<=Inf_i(G)+Inf_i(H), and

    R_i<=2alpha[(1-alpha)Inf_i(G)]
         +2(1-alpha)[alpha Inf_i(H)].

The bracketed values are final physical terminal contributions, not
new capacities at each failure history. Summing them proves R<=2I_T.
Influence telescoping retains exactly I_T=(1-alpha)I(G)+alpha I(H), and
entropy stopping retains exactly H_T=(1-alpha)H(G)+alpha H(H).

The scalar JS inequality is reconstructed as follows. For row masses p,q,
its natural-log Jensen gap is <=(sqrt(p)-sqrt(q))^2/2. Put
x=(p-q)/(p+q); the reduced scalar statement follows from
artanh(x)<=x/sqrt(1-x^2), by differentiating on [0,1) and symmetry.
For signed Fourier amplitudes a,b, (|a|-|b|)^2<=(a-b)^2. Summing squared
child-amplitude differences gives 4d; hence JS<=2c d. Thus the full
physical entropy decrement is bounded by A_s I_S+R, with

    b_s=2(1-2alpha)+2c(1-alpha)/s,
    A_s=b_s+2c.

The series for ln2 gives ln2>2(1/3+1/81)=56/81, so c<81/56.
Substitution checks A_s<11/2 at s=1..4 and b_s<5/2 at s=1..5;
for s>=5 use A_s<2+(12/5)c<11/2, and for s>=6 use
b_s<2+c/3<5/2. The independent script checks the finite cases and the
rational tail bounds. There is no precision-based limit inference.

For each parent spectral pair, magnitude-minority mass equals the
smaller of the two parent sector masses (absolute values permit swapping
them). Its charge m log2(Q/m) is one nonnegative summand of the sector
binary entropy, so Jminor<=B. Also mu<=d. This proves the source's
retained (5/2)I_S+R minority debt and the separate allowance
(5/2+3c)I_S+R<7I_S+R, with H_T restored throughout.

For even m>=4 bent/edit branches with a shared balancing literal z,
both Fourier supports have at most 2^m labels, so H<=m. Tensor-flat
Walsh coefficients give I(G)=1+m/2. A one-vertex edit changes at most
m undirected edges, so I(H)>=1+m/2-2m2^-m. Since
2-4m2^-m>=1 for m>=4, both terminal H/I ratios are <2. The whole-block
bound then has rate <11/2, retained J+terminal rate <=4 and full sufficient
KL rate <7. Multiplying by one shared literal makes both branches and
the switch balanced. A fresh constant-child activation has B/d<3 and
JS/d<3, preserving the complete terminal bill and giving rate <6 and
I=2^-t[I(F)+t]. These are explicit terminal certificates, not arbitrary-
core FEI assertions.

Validation independently generates actual truth tables/FWHT and integer
edges; no A023 helper or saved result is imported. All 256 ordered labeled
two-bit branch pairs at s=1,2,3, plus four bent/edit fixtures (m=4,6,
s=1,2), total 772 cases, passed 10,109 checks in 0.9077 seconds. Prime-log
normalization recognizes exact equality; 30-term atanh intervals with
explicit remainder and 100-bit outward rounding certify 73 distinct
expressions. A separate 36-term/104-bit implementation reproduced all 73.
The all-dimensional reconstruction above supplies the proof; finite
validation alone would not establish the unbounded-width claim.

No claim is accepted that these exact reserve fractions can be renewed
at nested ancestors, that the actual entropy bound upper-bounds localized
odd-face cost, or that arbitrary terminal cores satisfy FEI.
