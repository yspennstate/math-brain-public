# Sharp repair of local-hull admission

All Fourier entropies are in bits on a uniform physical cube. Write S=K I-H
and b=(-S)_+. Full FEI is OPEN. Nonnegative credit owners may redistribute
across the full positive-probability sibling support with their individual
conditional means conserved. Total booked debit is nonnegative; individual
booked debit labels may be signed. External donor expenditure stays fixed.

## Failed statements and actual witnesses

The failed generic inference is: an initial full stopping-hull bank, perhaps
enlarged by a fixed constant factor, automatically pays every changing-mask
local-hull allocator. This is FALSE (A072 stage19). Its Boolean witness is
F_d(s,x)=chi_123(x) with its sign flipped only at the all-zero vertex, with
d selectors and3 parity bits, at K=1. The full hull R_d tends to0 but the
prescribed local-hull robust capital T_d is at least1/2. Querying all selectors
first has identically zero local hull, so actual credit is unchanged along
the all-zero path ending at the3-bit state with full hull1/2.

A natural stronger claim tested here, T_d=1/2 for this family, is ALSO FALSE.
The fixed d=0..6 formula calculation first separates it at d=3. A separate
literal6-bit/4096-augmented-state audit proves
5078/10000 < T_3 < 5079/10000. This is an actual Boolean accounting witness,
not an FEI counterexample. out/CAPITAL preserves a lower-bound path receipt.

The older A089 failed extrapolation also remains false: saturation of a
positive parent with nonnegative immediate children does not force later
child positivity. With g negative{0,1,2}, h negative
{0,1,2,4,8,16,32,6,17,40}, J(x)=-h(x xor1), the stage7 full terminals
J(-1,g|x0=b,g,g,g,g) have S4 in(-56/1000,-55/1000) at b0 and
(-46/1000,-45/1000) at b1. Their previously paid incoming credit must remain.

## 1. Exact minimum sibling credit rerouting

Let w_i>=0 sum to1; discard zero-weight outcomes. Given existing credits
c_i>=0 and required lower bounds u_i>=0, put a=E c and
n_i=(u_i-c_i)_+, p_i=(c_i-u_i)_+, N=E n, P=E p.
Seek f with E f=0 and c_i+f_i>=u_i. This is feasible iff a>=E u.
Its exact minimum gross positive CREDIT movement E(f)_+ is N.

Necessity: average the constraint; also f_i>=u_i-c_i on deficit outcomes,
so E(f)_+>=N. For sufficiency a-E u=P-N>=0. If P>0 set
f_i=n_i-(N/P)p_i. Then E f=0, positive and negative supports are disjoint,
and c+f-u=(1-N/P)p>=0, with E(f)_+=N. If P=0 then N=0 and c=u on
support; f=0 works. This includes a=0,N=0,P=N and equality of total stock
and demand. Negative c or owner-specific forbidden sibling supports are
outside the hypotheses. This is original credit redistribution, not a new
outside donor flow. It is sharp for every finite real input, not just a grid.

## 2. Coherent collateral repairs admission without increasing initial capital

On a finite physical restriction DAG let u(v)>=b(v) be nonnegative and
superharmonic for EVERY eligible physical query, including unadmitted ones:
u(v)>=E u(children). Supply a>=u(v), debit D=S(v)+a. A restricted current-mask
hull rho_M is the least nonnegative superharmonic majorant of b for queries
in M. Hence rho_M<=u at every state, by finite backward induction.

Keep active collateral rho_M(v) and escrow a-rho_M(v), both nonnegative.
Admitting additional coordinates only increases rho_M to rho_M'; it does
not change the function, u, actual credit a, debit or owner totals. Move
rho_M'-rho_M from escrow to active collateral. This is possible because
rho_M'<=u<=a. No old past credit is retrospectively replaced.

At a query start with the prescribed local-hull baseline
c_i=a+rho_M(child_i)-E rho_M(children). It is nonnegative since
a>=rho_M(parent)>=E rho_M(children), and E c=a. Apply section1 with
required u_i=u(child_i). Feasibility follows from a>=u(parent)>=E u_i.
The new actual credits a_i=c_i+f_i dominate u_i and retain mean a. The
exact smallest necessary rerouting of that baseline is

    E( u(child)-a-rho_M(child)+E rho_M(children) )_+.

Continue the same rule online. It uses only the current full function,
eligible-query universe and retained account, never future query answers
or the future choice of admitted core. Finite induction pays EVERY allowed
admission/query/stopping policy. This replaces the allocation rule explicitly;
it does not vindicate the failed inference about the unmodified allocator.

For credit owner L>=0 with sum owners a>0, send L_i=L*a_i/a. The conditional
mean stays L. At each child split active and escrow proportionally to the
same owner totals; an admission only changes that split. If a=0, all owners
vanish, all outgoing credit vanishes, and the same assertions hold without
division. Donor expenditure outside this subtree is unchanged.

Let d_i=S(child_i)+a_i>=0. Physical influence telescoping gives
E d=D+e=T, where e=E S(child)-S(parent). Append signed query label e to
old signed debit labels summing to D. If T>0 send every label through the
common mean-one kernel d_i/T. If T=0, each d_i=0 on support, so kernel1
keeps all signed labels and their sum0. Thus no sign assumption on e or
individual labels, division by zero, omitted terminal, or donor renewal is
hidden. Iterated conditional means preserve true root-weighted ownership.

The least full-universe envelope is R_all, the maximum expected terminal b
over finite stopping policies. Necessity follows by taking expectations of
nonnegative credit at every stopping leaf. Consequently initial a=R_all is
SHARP for this repaired model. A supplied old net debit D>=0 simply gives
a=D-S at a root with R_all=-S and is retained, not reset. This theorem also
works with a tractable upper envelope u instead of an exact full hull.

## 3. All-d Boolean application, rather than another finite extrapolation

For r parity bits and t selector bits write m=r+t,N=2^m and
F_(r,t)(z)=chi_P(z)-2*1_(z=0). It is sign valued. For m>=1 its INTEGER
Walsh numerators are W(A)=N*1_(A=P)-2. Their squares sum toN^2; integer
character inversion gives exactly the prescribed signs. Direct edges give
I_(r,t)=r+2(m-2r)/N: flipping the vertex removes r parity edges and adds
m-r others. For m=0 the function is constant. For m>=1 the spectral
entropy H_m depends only on m: main mass(1-2/N)^2 and N-1 masses4/N^2.

Every query answer1 yields pure parity, with entropy0 and nonnegative K=1
slack; only the unique all-zero path may have a deficit. Hence for EVERY
r,t the full hull has the finite formula

    R(r,t)=max_(0<=r'<=r,0<=t'<=t)
       2^(-(r+t-r'-t')) * (H_(r'+t')-I_(r',t'))_+.

Every term is attained by querying exactly the removed coordinates with
answers0 and then stopping; all other leaves contribute0. This proves both
directions and constructs a known full-universe envelope for every d.
The local hull has the same formula with removals restricted to admitted
counts. No all-d conclusion is inferred from the seven formula test cases.

For F_d=F_(3,d), the failed source bank has R_d=R(3,d). It is positive by
retaining r'=2,t'=0, whose need is1 at reach2^(-(d+1)). It tends to0:
with v=1-(1-2/N)^2, H_m=h2(v)+v log2(N-1), 1/N<=v<=4/N for m>=2,
and -(1-v)ln(1-v)<=v imply H_m<=8(m+1)/2^m, using ln2>1/2.
Therefore R_d<=8(d+4)/2^(d+3). The m0,1 terms vanish.

To reconstruct the obstruction completely, H_m decreases for m>=3: in
natural units the derivative with respect to z=2/2^m is
4(1-z)ln((1-z)/z)-2>0 for0<z<=1/4, because ln3>1. Meanwhile
I_(3,t)>=9/4, and H_3=4-(9/8)log2 3<9/4 because3^9>2^14. Thus all
F_(3,t) have positive rate1 slack; admitting/querying only selectors has
rho=0. Ending on F_(3,0) requires full hull1/2: its active query gives
one two-bit need1 and one pure-parity need0. Hence fixed-allocator
T_d>=1/2 while R_d->0, and no universal factorT<=L R exists.

By section2, however, the SAME original R_d pays ALL online admissions,
queries and stops for EVERY d under the minimally rerouted allocator, with
separately conserved owners and all full terminal outcomes. No initial
constant-factor enlargement is needed. This is the useful repaired application.
It resolves the admission inference once an envelope is supplied; it does
not create a universally influence-paid initial envelope.

The smallest source witness makes the repair concrete: for d=1 initial
credit1/4, a selector-only query has baseline credits(1/4,1/4), while the
two full-envelope requirements are(1/2,0). The sharp conditional gross
rerouting is1/8, sending credits to(1/2,0). Their mean remains1/4. The
parity admission is then solvent with no additional initial bank. Original
owner labels move by the same conserved kernels; this is not fresh income.

## 4. Exact remaining universal gap

A dimension-independent all-function u with u>=(-S_K)_+, superharmonic
under every query, and u<=L I would prove FEI(K+L). Conversely FEI(K+L)
supplies u=L I, since physical I(parent)=Inf_query+E I(child). Thus a
universal influence-paid envelope is still exactly the unpaid bridge.
The new sharp rerouting lemma removes the unnecessary demand that a
particular changing-mask local allocator must preserve that envelope for
free. It does not prove a bound on universal R_all or on H/I.

## 5. Independent reconstruction of the remaining source theorem scope

A072's no-damage claim through3 bits holds for EVERY real K>=0. On a
one-bit Boolean function H=0 and S=K I>=0. Therefore on at most2 free
bits every proper child has need0, so rho_M=b for every admitted mask.
On3 bits, every first physical query has full-child hulls exactly b(child),
regardless of mask. A full-root bank a>=R_all covers their mean. The local
allocator therefore sends a_i=b(child_i)+a-E b(child)>=b(child_i), and
at smaller states no new requirement appears. All admissions leave credit
unchanged. This proves robust capital T=R_all, not just agreement at K=1.

The source max-path characterization follows without a spectrum assumption:
given any prescribed zero-mean query increments delta_i, the exact required
credit is max over all actual paths of b(last)-sum delta. Backward induction
takes the unweighted maximum over query outcomes, unchanged admissions,
and immediate stop. It is necessary by following a violating path and
sufficient because every arrival satisfies the next requirement. The
source's T>=rho_M follows by averaging the child inequalities and using
E delta=0; with all coordinates admitted, the affine hull allocator makes
T=rho_all. The same owner/debit kernels as section2 preserve every label.

Together with section3's independent all-d Walsh/edge/entropy construction
and the literal-state audit, this reconstructs the source claimed obstruction,
including its universal recurrence and all-K small-dimension boundary.
Source statement/version are retained unchanged in the local review record.
