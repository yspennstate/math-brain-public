# Independent reconstruction: A023 overlap v2 separator slice

Source: A023-OVERLAP-EXPOSURE-GOOD-CONTROL-LEDGER@2, statement digest
ceb0a37e4a74494589bdfd8efddf7cdad84f842cfba3ba3f1bc6932b12d9fc9c.
Reviewer A040. This audit concerns the added one-separator theorem. Earlier
version-1 scope was reviewed in A040 stage 2 and is not counted twice.
No modification or substantive repair to the source theorem is required.
Verdict: HOLDS for the separator extension. The all-width reconstruction
below and all 51 frozen roots passed; see out/RESULTS.json (20,734 exact
assertions). This is not acceptance of an arbitrary-depth generalization.

All entropies are in bits, c=1/ln(2). For an indicator E, J(E)=I(1-2E)/2.
Core g is balanced and independent of all control coordinates.

## Boundary reconstruction from physical edges

Let p=2^-L, q=2^-R, r=2^-T; beta=q+r-qr, eta=pqr,
pi=(beta+eta)/2 and e=beta-eta. Children at X are A0=WUV and
A1=U OR V. They are nested and their difference D is an indicator.
The expected core survival is pi, counting each actual history once.

At a U-coordinate, the A1 boundary occurs when V=0 and all other U
literals hold. The A0 boundary occurs when W=V=1 and all other U
literals hold. These events are disjoint. The analogous V events are
disjoint; only A0 has W boundary. Therefore

    J(A0)=(L+R+T)eta,
    J(A1)=R q(1-r)+T r(1-q),
    J(D)=J(A0)+J(A1)=2 Jrem.

Balance makes a control pivot change F on exactly half the core cube.
Hence d_X=e/2, I_ctrl=d_X+Jrem, I_terminal=pi I(g), and

    c_X=I(F0 F1)/2=J(D)/2+e I(g)/2=Jrem+e I(g)/2.

This reconstructs the factors of two without interpreting a sum of event
boundaries as physical influence. Since pi-e/2=eta, the terminal unit
reserve has exactly eta I(g) slack. Every remaining control coordinate
uses exactly its entire one-unit reserve for the root face. Thus
c_X<=I(F)-d_X. Odd faces containing X are removed at first revelation;
partitioning actual two-dimensional faces gives the exact Q telescope.

## Descendant goodness in every width

For a constant child, with signed disagreement d, group the empty Fourier
row separately. Its parent masses are (1-d)^2 and d^2, and all other rows
contribute 2d(1-d). Thus

    B=2d(1-d)+E((1-d)^2,d^2),
    E(a,b)=(a+b)h2(b/(a+b)).

Write A=d-d^2+d^2 log2(((1-d)^2+d^2)/d^2). Then B-A<=cd:
their difference is d(1-d)+(1-d)^2 log2(1+(d/(1-d))^2),
bounded by d(1-d)+cd^2<=cd. Endpoints follow by continuity.
Since ((1-d)^2+d^2)<=1,

    B/d<=1+c+2/(euler ln2)<4.

Here max_{0<=d<=1} d ln(1/d)=1/euler. The exact estimates
c<81/56 and euler>8/3 already give a strict rational bound below 4.

For U OR V, at a live U query let rho=2^-j be the probability of all
remaining U literals, and let r be the residual V probability. Signed
disagreement is d=rho(1-r)/2. Nonempty remaining-U Fourier labels
contribute 2(1-rho)d to B exactly: the child with U failed depends only
on V and g, so these nonempty-U child labels have one zero child
amplitude; their equal parent masses give the stated contribution.
The aggregate empty-U mismatch is rho d and its packet mass is at most
one. Concavity of binary erasure entropy gives its contribution at most
h2(rho d). Therefore

    B/d<=2(1-rho)+rho log2(euler/(rho d))
        <2+2(j+1)2^-j<=4.

The strict step uses 1-r>=1/2>euler/8; the last dyadic inequality follows
from j+1<=2^j for integer j>=0. After an event succeeds stop at g; after
it fails use the constant-child rule. The X=0 branch is a single point
event and needs only that rule. This proves all-width descendant
goodness independently of core dimension or spectrum. Root goodness
is not used.

## Root payment, true KL account, and the retained terminal

The mismatch set between any two children has density d. Its product
sign has half-influence at least d log2(1/d), by cube edge isoperimetry.
Also B<=h2(d)<=d log2(1/d)+cd. Consequently B<=c_X+cd;
at good nodes use the stronger defining B<=4d. At the root this gives
B_X<=4d_X+1_bad c_X.

For clarity, isoperimetry here requires no FEI premise. A subset with m
vertices spans at most m log2(m)/2 internal edges: split the cube with
child sizes a<=b, bound cross edges by a, and use h2(a/(a+b))>=2a/(a+b)
in the induction. Subtract internal edges from the degree sum to obtain
the required boundary bound, including densities above one half.

For child Fourier amplitudes a,b, let Q=(a^2+b^2)/2 and
m=(|a|-|b|)^2/4. These are the parent packet mass and its smaller atom.
The exact erasure packet B equals E(parent masses). Hence

    Jminor=sum m log2(Q/m),
    0<=B-Jminor<=c mu,    mu=sum m<=d.

This follows from -(1-t)ln(1-t)<=t. The scalar Jensen-Shannon bound is
JS<=2c mu: set t=(a^2-b^2)/(a^2+b^2) and use
[(1+t)ln(1+t)+(1-t)ln(1-t)]/2<=1-sqrt(1-t^2).
The difference's derivative on [0,1) is t/sqrt(1-t^2)-artanh(t)>=0;
its derivative in turn is nonnegative and it starts at zero. Thus the
actual entropy decrement is exactly B+JS<=Jminor+3c mu.
The complete normalized reference is Q over all Fourier labels, with

    Jminor=mu[log2(1/mu)-D2(m/mu || Q)].

No derivative-support conditioning or omitted KL normalizer is used.
Summing the fair stopping tree, including every surviving core terminal,
gives the sharper source ledger

    H(F)<=(4+2c)(d_X+Jrem)+Q_bad+pi H(g)
        <=(4+2c)d_X+(5+2c)Jrem+pi H(g)+(e/2)I(g).

Also J_tree+pi H(g)<=5(d_X+Jrem)+pi H(g)+(e/2)I(g).
Adding 3c sum mu costs at most 3c(d_X+Jrem).
With H(g)<=C0 I(g), all displayed claims follow with rate
max(5+2c,C0+1) for entropy. The terminal hypothesis is explicit.

For the source balanced bent-surgery family, a vertex flip changes any
data influence by at most 2delta, delta=2^-k. A fair selector adds delta
influence; balancing adds one. Thus
I(g)>=1+k/2-(k-1)delta and H(g)<=k+1 (balancing shifts every Fourier
index by the z coordinate without changing entropy), proving H(g)/I(g)<3 for all
even k>=4. This proves H(F)<8I, retained J+terminal<=5I and full
sufficient KL bill<10I, without an arbitrary-core estimate.

## Ownership limit and quantitative posterior insufficiency

This is one reserve, consumed before descent. The control part of the
root face uses every nonseparator controller coordinate's reserved unit.
The core part uses fraction e/(2pi), leaving fraction eta/pi. Nothing
here supplies the consumed control capacity to a later separator.
The first unsupported universal line remains a uniform bound for total
ancestral reservations per actual coordinate with arbitrary terminal
entropy paid. Neither the finite root-goodness grid nor a positive KL
term proves that line.

For a quantitative test, fix L=R=T=1 and let g_k=z*b_k for an even-k
quadratic bent function. Then pi=7/16 and eta=1/8. The active terminal
has exactly H(g_k)=k and I(g_k)=1+k/2. Every control Fourier erasure B,
posterior J, and minority KL credit is independent of k: pure-control
rows are unchanged and each nonempty bent row is replicated 2^k times
with squared amplitude scaled by 2^-k. The same holds at every reached
control history. In particular any fixed positive root credit C has

    C/(pi H(g_k))=(16 C/7)/k.

The root posterior credit C=I(S_X;S_-X), the complete minority KL
divergence D2(nu||Q), and its weighted credit mu D2(nu||Q) are all
strictly positive. Exact vectors and positive rational intervals are in
out/CREDIT_FIXTURE.json; here mu=1/4, so the divergence is four times
the weighted credit. Each satisfies the displayed Theta(1/k) ratio to
the terminal entropy, with its explicit constant (16/7)C. Direct k=2,4
checks verify the replication identity, whose all-k proof is above.
Also H(F_k)=H(F_dictator)+(7/16)k and
I(F_k)=3/4+(7/16)(1+k/2), so H(F_k)/I(F_k)->2. This is a credit
insufficiency example, not a FEI counterexample. It does not assert that
total correlation or every function-dependent divergence is small.
