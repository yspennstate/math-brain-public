# A089: exact existential repair of the every-coordinate obstruction

## exact target, quantifiers, hypotheses and units

All entropies are in bits. For a Boolean sign f, let p_S=fhat(S)^2,
I_i=sum_{S contains i}p_S, and B_i=H(S_i|S_without_i). Define
Phi(u,v)=(u+v)h2(v/(u+v)), with its continuous boundary values.
We compute min_{i:I_i>0} B_i/I_i on the two families specified by the
B18 lead. The proofs cover all their parameters, not an extrapolation
from the finite checks.

**Result, author proved; independent review pending:** On B05 sparse bent
point surgery the minimizing type is a data coordinate for k=4 and a
control coordinate for even k>=6. An exact sharp uniform constant is
K_B05=psi(57/262144), where

    psi(t)=2-2t+Phi((1-t)^2,t^2)/t.

In particular K_B05 < 2+7/1024. This also covers any number r>=2k of
controls. On the A062 activation family, the minimizing coordinate is
the balancing sign, and the exact sharp uniform constant is

    K_A062=Phi(1,1/4)=(5/4)log2(5)-2 < 1.

Its best-coordinate ratio tends to zero. Neither family obstructs the
existential good-coordinate form of C018. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the complete EXECUTION_PROTOCOL.json, revision
2026-10-11-execution-v2; report README and CURRENT_STATUS; claim,
obstruction, packet and next-action indices; campaign plan and recovered
run navigation. Read BOARD.md and B18 STREAM_NOTES.md v1, 22:45 UTC,
whose A089 target specifies these two families. Read supplement
CAMPAIGN.md, CLAIMS.md (C005/C013/C018/C019), COUNTEREXAMPLES.md,
SEED_LEMMAS.md, NATIVE_MAPPING.md and source inventory. Mathematical
source actually consumed: sources/ERASURE_REDUCTION.md sections 1-4,
including its exact B_i formula and physical influence identity.

Original failed statement: B05 REPORT.md,
20261011T193057Z-account01-B05-rare-restrictions, sections 2-6;
registry pins its original commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b
and the independent B19 acceptance at
7955d427222392911dc6af2e4ee3aa8aab67ac8c. Read A021 rare-core report
and A062 REPORT.md, 20261011T220423Z-account05-A062-influence-compensator,
including the exact construction in its dimension-limit witness.

The supplied four paper text versions were inspected for context and
scope; the relevant mathematical passages read are threshold 38pp,
section 8.4, Proposition 8.9 and Corollary 8.10 (activation), and
percolation 30pp, section 2, Lemma 2.1 (terminal refinement cost).
Earlier versions were inspected as historical context. This is not an
independent audit of either whole manuscript. No percolation estimate
is imported. Local file hashes are in out/SOURCE_INVENTORY.json and
out/PAPERS.json. The new formulas below are independently derived.

## complete derivation or exact first unsupported line

### 1. Preserve the failed statement and witness

The original false universal statement is: fixed finite K,A,B>=0 exist
such that, at **every** actual Boolean coordinate split,

    L <= K d + A V_post + B M_inf.

Here L=B_i, d=I_i, V_post=sum_W q_W(theta_W-d)^2, and
M_inf=sum_j (I_j(child+)-I_j(child-))^2. B05's actual family has, at its
selector y, d=2^(-3k), B_y/d=k+log2(e)+o(1),
V_post/d<=4*2^(-k), and M_inf/d=12k*2^(-3k). It refutes every fixed
choice of these prices. The first invalid line in any proof using that
helper is its assertion at every coordinate. Replacing "every" by
"some" is a different quantifier and needs a new proof.

A062's separate failed inference is that a uniformly bounded root
influence permits dropping the terminal reserve in a dimension limit.
Its activation witness has root I<=3/2 but expected terminal influence
tending to 1/2 and expected terminal entropy equal to 1, although the
coupled terminal random variables tend almost surely to zero. The
coordinate result here does not repair that limit exchange.

### 2. Elementary entropy tools

For u,v>=0, Phi(u,v)<=u+v and Phi(u,v)>=2min(u,v), by the upper bound
and chord lower bound for h2. If u>=v>0, then

    Phi(u,v) >= v[log2(u/v)+1].                         (E1)

Indeed u log2(1+v/u)>=v, since log2(1+x)>=x for 0<=x<=1.
For any u,v with u+v<=1,

    Phi(u,v) <= v log2(e/v).                           (E2)

This follows from h2(theta)<=theta log2(e/theta).
Writing c=log2(e)=1/ln2, we use 7/5<c<3/2. For completeness,
the positive series ln2=2 sum_{j>=0}(1/3)^(2j+1)/(2j+1)
gives ln2>2/3 and ln2<=2/3+1/36=25/36<5/7.

The elementary inequalities

    1-h2((1+z)/2) >= c z^2/2,
    1-h2((1+z)/2) <= c(1-sqrt(1-z^2))

follow respectively by integrating atanh(z)>=z and
atanh(z)<=z/sqrt(1-z^2); the latter proof is reproduced in the
erasure source. These inequalities provide every all-parameter sign
used below; floating logs are unnecessary.

### 3. B05: Fourier expansion and all coordinate ratios

Use 0/1 physical bits with characters (-1)^(S dot x). Let k>=4 be even,
delta=2^(-k), s=sqrt(delta)=2^(-k/2), r>=2k, p=2^(-r),
m=s-delta, a=1-m, and t=pa. Let b be the quadratic bent sign on k
bits, D the indicator of x=0, A the indicator of z=0 on r controls,
and C the indicator y=1. The actual sign is

    f(x,z,y)=1+A(z)(h(x,y)-1),
    h(x,y)=b(x)-2D(x)C(y).

At y=0 this is G; at y=1 it is H from the original B05 construction.
The Fourier coefficients c_T of b are +-s, with c_empty=c_{singleton}=s.
The core coefficients are hhat(T,empty)=c_T-delta and
hhat(T,{y})=delta. Therefore fhat(empty)=1-pa; on every other index
with core index empty and nonempty control index the coefficient is
-pa; on every nonempty core index it is p times its core coefficient.

Let

    b_x = 1/2-delta/2 + Phi((s-delta)^2,(s+delta)^2)/(4delta).

All data coordinates have identical ratios, and direct spectral pairing
gives

    I_x = p(1/2+delta),
    B_x = p(b_x-2m^2)+(p-p^2)Phi(a^2,m^2)
          +Phi((1-pa)^2,p^2m^2).                      (B05-X)

To see the multiplicities in b_x, translation of the bent spectrum by
one data coordinate has 2^(k-2) same-sign pairs and 2^(k-2)
opposite-sign pairs. The sum of the coefficient over the same-sign
pairs is 1/2, since sum_T c_T=b(0)=1 and opposite pairs cancel.
Thus their mass after subtracting delta is 1/2-3delta/2;
the y-containing pairs add delta, and the opposite pairs contribute
Phi((s-delta)^2,(s+delta)^2)/(4delta). This is b_x.
Activation replaces the empty-core coefficient in **all** control
fibers, giving the two correction terms in (B05-X). The first finite
check caught my initial omission of the nonempty-control fibers;
out/FIRST_CHECK_FAILURE.md preserves that implementation correction.
Data edge counting gives I_x: b has I_x=1/2, and flipping its origin
increases each data influence by 2delta in the y=1 child only.

Every control coordinate has

    I_z=t,
    B_z=2t-2t^2+Phi((1-t)^2,t^2),
    B_z/I_z=psi(t).                                   (B05-Z)

For nonempty core indices both control-edge coefficients are equal;
their total B contribution is p(1-m^2). The nonempty residual control
indices contribute (p-2p^2)a^2, and the empty residual pair contributes
Phi((1-t)^2,t^2). The sum is (B05-Z).

For the selector put e=p^2delta^2 and
N_+=(2^k+2^(k/2))/2-1, N_-=(2^k-2^(k/2))/2. Its exact closed form is

    I_y=p delta,
    B_y=2^r[N_+ Phi(p^2(s-delta)^2,e)
              +N_- Phi(p^2(s+delta)^2,e)]
        +(2^r-1)Phi(p^2a^2,e)+Phi((1-pa)^2,e).         (B05-Y)

These formulas are finite closed expressions in k,r and logarithms.
They do not enumerate an exponentially large cube to state the answer.

### 4. B05: determine the minimizing coordinate and sharp constant

The selector's nonempty-data fibers have midpoint p(c_T-delta).
Their q/e >=1/(2delta), because (1-s)^2+s^2>=1/2. Their total
mismatch mass is (1-delta)I_y. Thus

    B_y/I_y >= (1-delta)(k-1) >=45/16.                (B05-Y-lower)

By Phi>=2min, psi(t)>=2. Also t<=p<=delta^2 and a>=13/16>1/2.
Using (E2) and -2t<=0,

    psi(t) <= 2+t[c+2log2(1/t)]
           <= 2+p(4+2r)
           <= 2+delta^2(4+4k).                       (B05-Z-upper)

The last step uses that 2^(-r)(4+2r) decreases in integer r.

The entropy deficit inequalities in section 2 applied with
z=2s/(1+delta) yield

    1-c delta <= b_x <= 1-c delta/(1+delta).          (B05-core)

For k=4, m=3/16 and a=13/16. In Phi(a^2,m^2), the ratio
(a^2+m^2)/m^2=178/9<20 has logarithm <9/2, since 20^2<2^9.
Hence Phi(a^2,m^2)<=6m^2. Moreover p^2m^2<=delta^5,
and monotonicity of v log2(e/v) for v<=1 gives

    Phi((1-pa)^2,p^2m^2)/p <= delta^3(c+5k).

Here (E2) bounds the left side by
p m^2 log2(e/(p^2m^2)), which increases in both p and m^2 on
0<p<=delta^2, 0<m^2<=delta. Its partial derivatives are positive
because p^2m^2<=delta^5<=2^(-20). Thus substitution of their upper
bounds is valid even when r>2k; dividing an upper bound for Phi
by a smaller p alone would not justify this step.

With (B05-core),

    B_x/p <= 1-(7/5)/17+4(9/256)+22/4096 < 9/8.

Since I_x/p=9/16, its ratio is strictly below 2. Both other types
are >=2, so every data coordinate is a minimizer at k=4.

For even k>=6, a/m>1/s, so log2(a^2/m^2)>k, and (E1) gives
Phi(a^2,m^2)>=(k+1)m^2. Dropping the nonnegative last term in
(B05-X), and using c<3/2, shows

    B_x/I_x >= 2 + delta/(1/2+delta)
       * [((k+1)(1-p)-2)(1-s)^2-7/2].

The bracket is >=(7(1-1/4096)-2)(49/64)-7/2>8/25;
the positive factors increase with k, while p decreases. Since
1/2+delta<=33/64<8/15, the data ratio is >2+(3/5)delta.
But (4+4k)delta<=28/64=7/16, so the control ratio is
<=2+(7/16)delta. The selector lower bound also exceeds this.
Therefore **controls are exactly the minimizing type for k>=6**.

For sharpness, psi is strictly increasing on 0<t<=1/256. Indeed,
with Q=(1-t)^2+t^2, direct differentiation gives

    psi'(t) = -2 + log2(Q/t^2)
                    -(1-t^2)/t^2 * log2(Q/(1-t)^2)
             >= -2+2log2((1-t)/t)-c(1+t)/(1-t) >0.

Here log2((1-t)/t)>=log2(255)>7 and
c(1+t)/(1-t)<(3/2)(257/255)<2. As k increases through even values,
t(k,2k)=delta^2(1-s+delta) strictly decreases: the delta^2 factor
shrinks by 1/16, while a grows by a factor <16/13.
At fixed k, t decreases with r. Thus the maximum control minimum
is attained at k=6,r=12, where a=57/64 and t=57/262144.
At k=4 the minimum is <2 whereas psi(t)>2 for small positive t
(also follows from strict increase and lim_{t->0}psi(t)=2).
Consequently the claimed K_B05 is the exact sharp constant over
all even k>=4,r>=2k, and K_B05<2+28/4096=2+7/1024.

The limiting minimum is 2. This confirms that B05's logarithm is
localized to its selector; it is not an existential-selection no-go.

### 5. A062: exact minimum, sharp constant, and vanishing limit

Let k>=1, M=2^(k-1), q=2^(-k), and

    g_k(y_0,x)=(-1)^(y_0) product_{j=1}^M (-1)^(x_{2j-1}x_{2j}),
    f_k=1+A_k(z)(g_k-1).

The core is balanced, H(g_k)=2M=2^k and I(g_k)=M+1. All its
nonzero coefficients contain y_0; their magnitudes are 2^(-M).
Let v=4^(-M). The squared coefficient at {y_0} is v.

Every control has I_z=q and ratio psi(q)>=2. Every bent data
coordinate has I_x=q/2 and B_x=q, ratio exactly 2: in each
y_0-containing control fiber the paired squared coefficients are equal,
and y_0-absent pairs contribute zero. The balancing sign has

    I_{y_0}=q,
    B_{y_0}=(q-q^2)Phi(1,v)+Phi((1-q)^2,q^2v),
    R_k=B_{y_0}/I_{y_0}
       =(1-q)Phi(1,v)+Phi((1-q)^2,q^2v)/q.             (A062-sign)

Only the zero bent-data index pairs with the y_0-absent activation
coefficients. There are 2^k-1 nonempty control fibers and one empty
fiber; all other sign pairs have a zero member. This proves the formula.

For k=1, q=1/2,v=1/4. Homogeneity of Phi gives
R_1=Phi(1,1/4)=(5/4)log2(5)-2. The exact integer comparisons
2^11<5^5<2^12 imply 3/4<R_1<1.

For k>=2, v<=1/16 and q<=1/4. Since log2(1+v)<1,

    Phi(1,v)<=v(3+2M),
    Phi((1-q)^2,q^2v)/q <=qv(2+2k+2M).

Thus R_k<=v(4+k+3M)<=4(M+1)4^(-M)<=3/4, using M>=k.
The function (M+1)4^(-M) decreases at integer M>=2. Therefore
R_k<1 for every k, it is strictly smaller than both other coordinate
types, and sup_k R_k=R_1. Also R_k<=4(M+1)4^(-M)->0.
This is an exact closed-form best-coordinate computation and an
optimal uniform bound for this particular all-dimensional family.

### 6. Useful application and exact remaining gap

This repair restores the **root selection** application that the
every-coordinate helper could not justify. For B05 choose a data bit
at k=4 and a control bit at k>=6; for A062 choose the balancing sign.
Using C005, the root entropy decrement is bounded by
(K_B05+2/ln2)I_i or (K_A062+2/ln2)I_i, respectively.
This invokes no variance credit and does not reuse influence.

It does not prove an induction over these root families: arbitrary
restrictions can leave the quantified class. In particular an A062
sign restriction produces two unbalanced activated bent cores, so a
policy must still pay their entropy. The exact first unsupported
universal line is that every nonconstant restriction reached by the
chosen policy has a uniformly paid good coordinate or a certified
terminal reserve. A small root erasure ratio cannot remove arbitrary
leaf entropy. No universal B<=KI conclusion is asserted.

## executed validation with domain, arithmetic, commands and outputs

Frozen spec was saved in out/FROZEN_SPEC.json before execution.
code/check.py v1.1 builds five actual Boolean truth tables: B05
(k,r)=(4,8),(4,9), and A062 k=1,2,3. Every coordinate is checked.
Integer Walsh transforms are paired independently of direct edge
boundary influence. Entropy equalities use exact rational formal
prime-log vectors; no logarithmic sign is inferred from floating point
or presumed prime-log independence. Equality of vectors suffices.
All infinite-parameter inequalities are supplied by the proofs above.

Command from A089:
`python -X utf8 runs\20261011T224857Z-account05-A089-repair-specialist\code\check.py`.
The executed result is out/CHECK.json. The first implementation
failure and correction are preserved in out/FIRST_CHECK_FAILURE.md.
The initial omission was diagnosed from actual Walsh coefficient
multiplicities, then corrected before claiming a validated formula.
The uncached v1 passed 150 assertions but took 202.310 seconds,
exceeding the frozen 60-second pilot limit; this execution error is
recorded in out/CHECK_v1_overrun.json. The corrected implementation's
memoization changes no domain or arithmetic and has its own frozen
spec saved before rerunning. The final assertions and measured runtime
are recorded in CHECK.json and the final persistence receipt. No heavy job, GPU, dimension
escalation, external independent reviewer, or formal verification is
claimed.

## proof dependencies and changed downstream conclusions

The new bundled claim uses self-contained Walsh expansion, boundary
counting and scalar entropy inequalities. B05 and A062 establish which
families to audit; neither an unproved global FEI premise nor B09 is
used. C005 is used only for the stated root-decrement corollary.
The repair is contributed work, so A089 cannot independently accept
its own version. It adds one bundled unreviewed repair, not multiple
broad candidate routes.

Changed downstream conclusion for A023/A026/A064/A087/A094: B05 and
A062 do not challenge existential good-coordinate selection even
though their every-coordinate or limit-exchange helpers fail. B05's
optimal coordinate type changes at k=6; A062 has a much cheaper
balancing-sign coordinate than the control-first policy uses.

## one next mathematical action and independent reviewer

Apply the sign-first policy on A062 and compute the complete erasure
and influence ledger of the resulting two unbalanced activated bent
cores, with both terminal reserves. This tests whether the cheap root
coordinate extends to C019, rather than extrapolating a root bound.
Independent reconstruction requested in the saved handoff: A090
primary and A094 alternate, concentrating on activation fiber
corrections and the k=4 versus k>=6 ordering proof.

## actual persistence receipts or precise save blocker

Saved REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json,
code/check.py, code/finalize.py and out/ files in the assigned A089 run
directory. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated.
out/RECEIPTS.json records local hashes, sizes, validation output and
schema checks. No other agent or shared tree was modified. Supervisor
copy, mirror verification, independent acceptance and downstream use
remain unverified. There is no local save blocker.

**Universal bridge:** This stage moves C018 existential erasure selection
by completely resolving its good-coordinate test on both lead-selected
refuting families, with exact minima and sharp family constants; the
B05 all-coordinate obstruction does not survive existential selection.
It does not prove the universal aggregate bound B<=KI, and the
restriction closure/terminal payment remains unpaid. The NEXT action
is sign-first A062 continuation with labelled reserves: it directly
tests transport of the newly cheap coordinate into the C019 universal
ledger, the shortest unresolved implication here rather than another
isolated entropy estimate.
