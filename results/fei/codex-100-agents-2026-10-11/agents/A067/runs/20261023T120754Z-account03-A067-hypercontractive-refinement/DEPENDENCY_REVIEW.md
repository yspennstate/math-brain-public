# Independent reconstruction of the supplied A088 account

Source: A088 run20261023T105519Z PROOF.md sections1--5 and its preceding
run20261023T070855Z PROOF.md. This review supplies no repair. Full finite
frontiers are rebuilt by this run from original Boolean truth tables and
physical restrictions; no A088 code or output is imported.

Write q=4^-m, u=1+q, v=1+2q, B=2^j 2^-m and alpha=2^-m/2^j.
Then alpha B=q, alpha<=B, alpha<=1/4, B<=1/2 at any pair query.
The canonical pair Walsh coefficients are (1,1,1,-1)/2. Summing the
removed Fourier labels gives the exact original reference displayed in
A088 equations(1),(4),(5). Physical restrictions give their actual laws.
The marked incident edges give the pre-w influences1/2+B^2,2B^2 and
post-w influences1/2+2B^2,4B^2. The changed latter values are not assumed
equal to the former. All signs and dimensions are preserved.

For any query write L=sum P log2(Q_marg/Q), including both complete child
bills. The elementary bound ln x<=x-1 gives L<=1+M/ln2, where
M=sum P[Q_marg/(2Q)-1]. Exact sign multiplicities give the moments in
the source proof. The pre-w first-query moment is nonpositive. At j=0
the partner moment is2q/u and gives the already independently checked
first-block credit<-9q/4. For j>=1, alpha<=1/8 gives denominator
u^2-4alpha^2>=15/16. The numerator bracket
1-3B^2+4B^3alpha/u<=1, since4Balpha/u=4q/u<3.
Hence the partner moment is at most(32/15)alpha^2. Using ln2>2/3 and
alpha^2<=B^2/16 yields the local block debit at most
-6B^2+(8/5)alpha^2<=-(59/10)B^2. Its original reach1/(2*4^j)
gives credit at most-59q/20. All pre-w cumulative CE debits are nonpositive.

At w after H pairs, the W=0 log increment is at most
(3/2)q/(u-2alpha sigma), whose denominator is at least9/16. Its
root-weighted contribution is at most(4/3)q/4^H. The W=1 part is
strictly less than(2m+1)B^2, because v+2alpha<2. Subtracting the actual
rate3 influence and applying original reach gives a total w charge less
than q(m+1/3)<=7/48 for every m>=2. Monotonicity of(m+1/3)4^-m
reduces the last scalar bound to m=2; no finite-to-infinite extrapolation.

Post-w, the first moment is negative. The partner moment's sign bracket
is bounded above by
B[-2q-4B^2(1-4B^2/v)]<0, since4B^2<=1<v. Thus both query CE drops
are less than1 and every post-w block contributes less than-3q at its
original reach. Combining pre-w credits, one w charge and all post-w
credits gives the FULL cumulative E_old,Q<7/48.

For the full terminal KL, retain every earlier clean exit. Pre-w first-one
and second-one bounds are1 and1/2, with geometric weighted total
<(5/12)(1-4^-H). The w clean exit has KL<1 at reach1/(4*4^H).
Post-w first-one and second-one bounds are1 and1/2, with total
<(5/24)(4^-H-4^-T). The active post-w law satisfies P/Q<=2*4^T:
the cross terms cancel, leaving1<=2*4^T. Its contribution is at most
(1+2T)/(4*4^T). Summing gives
K_old<5/12+4^-H/24+(1+12T)/(24*4^T)<=19/32.
The final scalar inequality follows because(1+12T)4^-T is maximal at
integer T=1, and4^-H<=1. This retains the active terminal and every
signed bank; no term is clipped. Hence E_old,H=E_old,Q+K_old<71/96.

The original r and I_X are unchanged; so the remaining account is
r+I_X-E_old,H>m-71/96. The source's J(H,T) is independently checked
against the sum of actual root-weighted physical influences. All old
rate2 invoices are retained by the exact relation E_H,2=E_H,3+J.

Verdict: the specified all-dimensional source allowance and early-w/post-w
frontier are sound, without a repair. This is scoped independent acceptance
of the supplied account, not a full FEI result. The new clean continuation
lemma in PROOF.md is this agent's contribution and awaits a different reviewer.
