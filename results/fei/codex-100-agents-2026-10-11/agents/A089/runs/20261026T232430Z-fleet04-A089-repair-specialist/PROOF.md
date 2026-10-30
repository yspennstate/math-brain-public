# The debit sign and the exact conditional funding criterion

The debit in A089 stage10 section 5 has its sign reversed. The correction is
S=KI-H and d=S+a. A080 supplies the objection and its repair. The coherence
and initial-price sandwich statements survive; that written owner proof does
not. A075's later whole-row cancellation gives the stronger reserve 3 in
place of 9/2. Initial influence funding, and full FEI, remain OPEN.

## 1. Failed statement and a Boolean counterexample

The original immutable source is runs/20261023T130925Z-fleet03-A089-repair-specialist/PROOF.md,
section 5. Its exact failed sentence is:

> With S_b=H(F_b)-K I(F_b), booked debits d_b=S_b+a_b are nonnegative.

The hypothesis is supplied credit a at least the coherent bank; both complete
physical children and all signed historical debit labels must be retained.
The failure is not repaired by requiring the parent debit to be nonnegative.

Let f(x0,x1,x2)=1 on x0=0 and (-1)^(x1+x2) on x0=1, using bits 0,1.
Its four nonzero Walsh coefficients have magnitude 1/2, so H(f)=2 and
I(f)=3/2. All its restrictions have H<=2I (the 27 partial assignments are
checked separately). Thus its full stopping hull rho_10 is zero. Use the
one-core identity decomposition, which has C=0, and kappa=9/2. Its bank is
27/4. Supply a=13, and query x0. The child banks are 0 and 9, so the stated
mean-conserving allocation gives credits 17/2 and 35/2. The written parent
debit is 2-10(3/2)+13=0. The written child debits are 17/2 and -5/2.
All bank, initial-credit and nonnegative-parent hypotheses hold.

With S=KI-H the same child credits give debits 17/2 and 75/2. The corrected
parent debit is 26, and the signed query charge is -3; their sum is the
mean child debit 23. With A075's kappa=3 the credits are 10 and 16; the false
child debits are 10 and -4, and the correct ones are 10 and 36. Both full
children, including the constant child, remain in the calculation.

## 2. Strongest one-step replacement with prescribed child requirements

Let two actual children have arbitrary nonnegative required credits u0,u1.
Let a>=0 be the ACTUAL arriving credit, the sum of finitely many old
nonnegative owner labels c_l. Credit can be redistributed between children
but each original owner's conditional mean must be conserved. There is a
feasible child allocation a_b>=u_b if and only if a>=(u0+u1)/2.

Necessity follows by taking means. For sufficiency put

    r=a-(u0+u1)/2,     a_b=u_b+r.

If a>0, send owner l to c_l a_b/a. Each child owner is nonnegative, its
mean is c_l, and the sum is a_b. If a=0, feasibility and u_b>=0 force
u0=u1=a0=a1=0 and every c_l=0; send all zero owners to zero.
There is no division by a zero owner or by a child capacity.

For an FEI ledger at rate K>=0 define

    S_v=K I(f_v)-H(f_v),     d_v=S_v+a_v.

Assume u_b >= max(0,-S_b). Then each d_b>=0. If the old signed debit
labels l_m sum to d_parent, the new signed query label is exactly

    e=mean S_b-S_parent
     =H(parent)-mean H(child)-K Inf_i(parent).

Consequently T=d_parent+e=mean d_b>=0. If T>0 send EACH old signed label
and the new label through the same kernel k_b=d_b/T. Its mean is one,
and the child labels sum to d_b. Labels need not be individually positive;
the total is nonnegative. If T=0, nonnegativity forces d0=d1=0. Use k_b=1:
the signed labels retain their means and still sum to zero at both children.
An old cancelling pair is retained rather than discarded or renewed.
Historical reaches, already stopped siblings and spent external donors are
unchanged. No current influence component is declared to be new credit.

Both nonnegativity assumptions are necessary: negative u permits a negative
child credit, and a floor below -S_b permits a negative total debit. Individual
signed labels cannot be required positive, since the exact e may be negative
(as it is in section 1). The criterion a>=mean u is exact; no smaller bound
can work under mean conservation with these same child requirements.

## 3. All-policy version and the precise remaining gap

For each actual restriction define, by finite backward induction,

    rho_K(f)=max((H(f)-K I(f))_+, max_i mean rho_K(f|i=b)).

Constants have rho=0; the maximum over no coordinates is omitted. The least
initial nonnegative credit allowing arbitrary adaptive physical queries and
stops with nonnegative credits/debit totals and the owner conservation above
is EXACTLY rho_K. Stop-now necessity gives a>=(H-KI)_+. Allowing any first
query gives a>=mean rho(child) by induction. These together give a>=rho.
Conversely, a>=rho supplies the floors u_b=rho(child) in section 2 for every
selected query and satisfies the stop-now floor. Induction handles every
finite adaptive policy without a distributional-independence assumption.
This characterization is a corrected account of the already defined hull,
not a new universal entropy bound.

More generally any nonnegative superharmonic U>=(H-KI)_+ is a sufficient
supplied bank; it need not be the minimal one. The exact e telescopes on
every finite stopping tree with actual reaches:

    E sum_(visited internal v) e_v
      =H(root)-E H(leaf)-K[I(root)-E I(leaf)].

This follows by cancellation of each child S against its parent occurrence;
there is no product estimate over histories. Thus negative charges are
signed releases in the same ledger, not fresh independent income.

Because H is nonnegative and superharmonic under physical restriction,
0<=rho_K<=H and 0<=H-rho_K<=KI. For every disjoint partition, the coherent
bank below therefore lies between H+(kappa-K)I and H+kappa I. Fixing K and
requiring an initial dimension-independent O(I) price remains FEI-equivalent,
even if the partition is chosen separately for each Boolean function.
The first unsupported universal line is precisely that initial payment from
the SAME unused original influence account on an arbitrary indecomposable
core. Correcting the debit sign supplies no such starting capital.

## 4. Independent reconstruction of A075's whole-row cancellation

This section accepts A075-WHOLE-ROW-SIGNED-COMPOSITION-DRIFT@1 unchanged.
It is credited to A075; A089 supplies an independent reconstruction.
All entropy units are bits. Define eta(t)=-t log2(t), with eta(0)=0, and

    L(x,y)=eta(x^2)+eta(y^2)
           -[eta((x+y)^2)+eta((x-y)^2)]/2.

Writing s=x^2+y^2 gives L=Phi(x^2,y^2)+Jrow, both nonnegative, with
Phi(A,B)=(A+B)log2(A+B)-Alog2(A)-Blog2(B). Cancellation of the total mass
terms proves L(lambda x,lambda y)=lambda^2 L(x,y), also at zero.

The two elementary bounds are Phi(x^2,y^2)<=2|xy|/ln2 and
Jrow<=2min(x^2,y^2)/ln2. For the first use ln(1+t^2)<=t for t>=0;
its difference has derivative (t-1)^2/(1+t^2)>=0 and value zero at zero.
For the second, Jrow=s G(2xy/s)/ln2 and
G(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2. Evenness and
atanh(z)<=z/sqrt(1-z^2), by derivative comparison on [0,1), give
G(z)<=1-sqrt(1-z^2). Continuity treats the endpoints, and s=0 is separate.
Therefore L(x,y)<=2min(|x|,|y|)(|x|+|y|)/ln2.

For a Boolean core g, let mu=Eg, t=ghat({i}), d=Inf_i(g). Its conditional
means mu+t,mu-t lie in [-1,1], so |mu|+|t|<=1; also |t|<=d from its
signed Boolean derivative. Hence L(mu,t)<=2d/ln2. Booleanity is used here;
this is not a statement for arbitrary normalized real functions.

For F=h(g1,...,gr), write h=A+z_j D. Fourier coefficients on the other
physical blocks satisfy sum_W Dhat(W)^2=q_j, by D in {0,+1,-1} and Parseval.
Every paired row with nonempty remaining frequency in block j is Dhat(W)
times the corresponding core row. They cancel completely, using homogeneity,
when subtracting the full and q_j-weighted core entropy decrements. Only
the empty remaining core frequency differs, with full pair
(Ahat(W)+mu Dhat(W), t Dhat(W)). The unchanged core weights have mean
q_k because pivotality is affine in the queried core's output law. Thus

    mean C_child-C_parent
      =q_j L(mu,t)-sum_W L(Ahat(W)+mu Dhat(W),t Dhat(W))
      <=(2/ln2) q_j d=(2/ln2) Inf_i(F).

No variance, influence or pivotal probability is cancelled in a denominator.
The proof covers constant cores, dummy queries, zero means and endpoint
biases. Since ln2>2/3, kappa=3 suffices. Influence decreases in mean by the
queried influence, so C+kappa I is superharmonic; its value at complete
revelation is zero, proving its nonnegativity. Adding sum_j q_j rho_K(g_j)
preserves both properties and majorizes (H(F)-KI(F))_+. Section 2 with the
corrected S convention propagates its ACTUALLY supplied credit under every
physical query, admission revealing no bits, and stop. A changed partition
is a separate transaction. A075's original owner argument already uses the
correct sign and needs no amendment. Initial funding is still unpaid.

## 5. Validation and proof rung

The exact check covers 278 Boolean tables of dimensions 0 through 3 at five
rates, 4020 query/rate rows, and 1024 complete disjoint compositions with
3072 physical query rows. The saved frozen specification precedes execution.
Each spectrum is independently computed by direct characters and FWHT;
edge influences are compared with spectral ones. Prime-log vectors prove
equalities exactly; directed 192-bit logarithm enclosures with the stated
positive-series tail decide signs. There are 38022 successful main checks
(including 3072 runtime guards); the separate pilot has 2502 checks.
Zero credit, zero debit total, signed cancelling labels, constants, dummy
coordinates and all five rates including K=0 are present.

The all-dimensional statements in sections 2-4 have complete analytic
proofs, with independent review pending for the repaired owner proof.
Finite checks validate the formulas and implementation; they do not prove
FEI. A core Lean check, if admitted, certifies only its named integer
conservation statement, not entropy, real-valued division, or this proof.

Formal receipt: the guarded core attempt returned SETUP_UNVERIFIED (exit2), with no compiler process launched because compute admission held. No Lean-checked mathematical result is claimed. The analytic proof and exact finite certificates are the achieved rung.
