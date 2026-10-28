# Full-affine child credit under rare activation

Uniform finite F_2 cubes, Boolean signs, normalized Walsh coefficients;
entropy in bits. For a sign h put w_h(u)=Pr[h(x)!=h(x+u)], mu=E h,
delta=1-mu, I=sum_i w_h(e_i). Two different finite minima are needed:

    ell(h)=min_{linear input changes} I(h),
    a(h)=min_{linear input changes and character modulation} I(h).

Equivalently, ell is the cheapest independent parity basis with weights
w_h(u), and a has weights min(w_h(u),1-w_h(u)). Both include zero weights
and dimension zero; always 0<=a(h)<=ell(h)<=I(h). Entropy is unchanged
by either type of transform. No unbounded-dimensional optimizer is used.

## 1. Exact root optimization identity

For k>=2, p=2^-k, set F(x,z)=1+1[z=0^k](h(x)-1). Then

    a(F)=ell(F)=p[ell(h)+k(1-mu)].                         (1)

The root influence before optimization is p[I(h)+k(1-mu)].
Consequently its full affine reduction saves exactly p[I(h)-ell(h)].
The smaller quantity a(h) cannot replace ell(h) in (1).

Proof. The activation directional ledger gives

    w_F(u,0)=p w_h(u),
    w_F(u,v)=p delta for every v!=0.

For EVERY Boolean direction u, w_h(u)<=delta: a disagreement forces at
least one of h(x),h(x+u) to equal -1, and their negative probabilities
sum to delta. Also 0<=delta<=2. Thus all F parity costs are <=1/2 at
k>=2. Taking their minorities changes nothing, proving a(F)=ell(F).

On the data-only subspace the weights are p w_h(u)<=p delta. All
directions outside it have identical weight p delta. A minimum-weight
data basis followed by k control basis vectors is therefore optimal.
For completeness, this follows without assuming that an arbitrary
optimal basis splits into blocks: at every threshold t<p delta, the
rank of vectors of weight <=t is exactly the rank of the corresponding
data vectors; at threshold p delta the full rank is n+k. These ranks
determine the sum of the cheapest basis weights by the finite greedy
rank-count argument. They equal those of the displayed data-plus-control
basis. This also handles ties, zero weights and delta=0. Parseval or
direct physical translation proves the directional ledger, so no
independence of spectral coordinates is assumed.

Checks that could fail: complement costs at k1; confusion of linear and
affine input maps versus Fourier translations; a basis mixing data and
controls; zero rank; and Booleanity in w_h<=delta. Each is used above at
the specified line. For k1,h=-1, a(F)=0 but the right side of (1) is1;
the k>=2 condition is essential without additional hypotheses.

## 2. All physical data blocks and the complete reset bank

Let A be ANY block of original data coordinates, including empty and full,
and let h_b be every actual physical child. Controls remain unqueried.
Write averages over all 2^|A| branches. Define the source full-affine
release and the source linear-only release by

    rho_A(h)=I(h)-I_A(h)-E a(h_b),
    r_A(h)=I(h)-I_A(h)-E ell(h_b).

Physical influence telescopes, so both are nonnegative and

    r_A(h)=rho_A(h)-E[ell(h_b)-a(h_b)] <=rho_A(h).           (2)

Each activated physical child is precisely activation of h_b, with the
SAME controls. Since E mu_b=mu, applying (1) on each branch gives

    rho_A(F)=p r_A(h)
            =p rho_A(h)-p E[ell(h_b)-a(h_b)].              (3)

No child entropy or branch is deleted. Equation(3) applies in the
original coordinates even when F is not already affine-minimal. If
h is linear-minimal, then F is already fully affine-minimal by (1),
so this identity also applies to that proposed restricted endpoint.

To make the entropy/deficit payment explicit, put

    R_k(mu)=H(F)-p H(h).

This is a scalar profile, independent of the rest of h. The exact
coefficient multiplicity calculation is

 R_k(mu)= -(1-p delta)^2 log2((1-p delta)^2)
          +p mu^2 log2(mu^2)+2k p(1-mu^2)
          +(p-p^2)delta^2(2k-log2(delta^2)).                (4)

Terms with zero mass have value zero. Let L_A=H-EH(child), D_K=H-KI,
S_A^*=E[K a(child)-H(child)]. Direct algebra, retaining all terminals,
gives the exact same-bank transform

 D_K(F)+S_A^*(F)
   =p[D_K(h)+S_A^*(h)]
      +R_k(mu)-E R_k(mu_b)
      +Kp E[ell(h_b)-a(h_b)].                            (5)

Equivalently the left side is
L_A(F)-Kp[I_A(h)+r_A(h)]. K can be any fixed real number in this
algebraic identity; payment interpretations below require K>=0.
The final term in (5) is a real lost translation credit, not unused new
influence. Rarity scales it, rather than removing it relative to the
queried influence. The scalar profile term has no asserted sign.

The credit is unavailable at this DATA frontier, not permanently destroyed.
There is an exact admissible continuation. After querying A, choose in
each h_b a minimum linear data basis and leave all controls unchanged;
this is a full affine minimum of the activated child by (1). Next query
ALL k controls. The active branch is that linearly optimized h_b, which
can now be affinely minimized; every inactive branch is constant. The
expected extra reset release at that second frontier is exactly

    p E[ell(h_b)-a(h_b)].                                (7)

It is the same credit omitted from (3), redeemed only after resolving the
controls. The second queried influence is pk delta. With first data
query-plus-reset spend p[I_A+r_A] and final expected leaf influence
p E a(h_b), the complete original-owner telescope is

 p[I_A+r_A] +pk delta+p E[ell(h_b)-a(h_b)]+p E a(h_b)
      =p[I(h)+k delta]=I(F).                             (8)

The complete final expected leaf entropy is p E H(h_b); inactive branches
are constants. There is no new reserve at the second frontier. Resolving
the controls still has its full entropy bill, so (7)--(8) are a transport
identity, not a proof of uniformly paid query/reset selection.

## 3. A canonical parent loses all its source singleton reset credit

Take h(x1,x2)=(-1)^(x1*x2), with table (1,1,1,-1), k>=2. Its spectrum
is flat on four atoms, so H(h)=2, I(h)=ell(h)=a(h)=1 and mu=1/2.
Query x1. Its two children are a constant and a literal, respectively:

    rho_1(h)=1/2, r_1(h)=0,
    E[ell(child)-a(child)]=1/2.

The activated root is the point defect on k+2 coordinates. It has full
affine spectral span, is affine-minimal, mean 1-p/2, I=p(1+k/2), and
every coordinate influence p/2. The two complete activated data children
are a constant and the point defect on k+1 coordinates; their affine
influences are 0 and p(k+1). Thus rho_1(F)=0, despite
p rho_1(h)=p/2>0. The false credit-transfer equality is refuted even at
a full-span affine-minimal parent with all influences <=1/8 at k2.
Letting k grow makes total influence and every coordinate influence tend
to zero while the entire scaled source reset credit remains lost.

At k2, exact values are mu_F=7/8, I_F=1/2, d_1=1/8, child affine
influences 0 and3/4. This root has FEI ratio<4 and is not a high-K
critical witness. No universal FEI counterexample follows from it.

There is also an exact signed payment failure at K2. The source query
plus reset has L_1-K(d_1+rho_1)=2-2(1)=0, whereas activation has

    L_1(F)-2(d_1(F)+rho_1(F))
      =(120+18log2(3)-49log2(7))/32 >0.

The strict sign is exactly 2^120*3^18>7^49. All literal child entropies
are retained: H(F)=6-(49/32)log2(7), and its two children have entropies
0 and4-(9/8)log2(3). This refutes transporting an already paid source
query by rarity scaling alone, even allowing optimal affine child resets.
It is not a selected-pair or genuine-critical-witness counterexample.

## 4. Tensor bent cores: explicit nonzero surviving credit

For h equal to t independent copies of the two-bit h above, t>=2,
the root law is flat on F_2^(2t), so ell(h)=a(h)=I(h)=t and mu=2^-t.
Each original data query has source rho_i=1/2. The two children have
flat spectral laws on affine subspaces of dimension d=2t-2: one
linear subspace and one coset not containing zero. Their affine
minima are both d/2=t-1. Their linear minima are t-1 and t-1/2.
Consequently r_i=1/4, and activation has exactly

    rho_i(F)=p/4, versus the naive scaled source credit p/2. (6)

Here is the finite-dimensional fact used: a law uniform on an affine
subspace of dimension d has affine-minimum influence d/2. Its linear
minimum is d/2 when the coset contains zero; it is (d+1)/2 when d>=1
and the coset avoids zero; for a nonzero singleton it is1. To prove the
nonzero-coset case, remove annihilator zero directions. The residual
linear span has dimension d+1; the one nonzero constant functional has
cost1, every nonconstant nonzero functional cost1/2. Choose a nonconstant
dual basis v1,...,vd and the extra vector c+v1, where c is the constant
functional. These d+1 vectors are independent and all cost1/2. No basis
can cost less, since each nonzero independent functional has cost>=1/2.
This proves the statement, including d1; d0 is the separately stated
character endpoint. No asymptotic approximation is used in (6).

## 5. Scoped reconstruction and the universal unpaid line

A051 RESET_BUDGET Sections2--3 supply the live interface. Reconstructing
its one-node account directly gives S_A=S_A^*+K rho_A and
D_K+S_A^*=L_A-K(I_A+rho_A). On a least-essential-dimension positive
K witness, K>=0, every affinely optimized proper child is a smaller
Boolean sign and has nonnegative K a(child)-H(child). Summing finite
query/reset identities along actual reaches spends queried influence
and reset release exactly once. This is a scoped analytic acceptance
of those identities, not acceptance of the source's channel bound or
critical all-block budget. Equations(3)--(5) use exactly this unchanged
physical bank; they do not identify transformed physical charts.

FIRST UNSUPPORTED LINE: at a genuine critical witness, select an original
proper pair with L_A<=K(I_A+rho_A) using the SAME unused S_A^*, mixed
refund and complete terminals. A source proof supplying only rho_A(h)
cannot be lifted through activation without paying BOTH explicit
corrections in (5). Neither the canonical point-defect example nor the
tensor-bent example has the required high-K criticality. The new ledger
closes this reset-credit transport question in every dimension; it
does not supply the missing lower funding/selection theorem.
