# A019 stage 18: one interacting query from the same original account

## exact target, quantifiers, hypotheses and units

Prove the scoped claim A019-INHERITED-V-QUERY-SAME-BANK@1 for every integer k>=2 and every choice of the next v coordinate. Entropies, CE and KL use base-two logarithms; CE(P,Q)=-sum P log2 Q and P is the squared Fourier law of an actual Boolean function. The theorem retains the original bank, the old debit, the FULL first-query bill, both newly exposed children and the unchanged opposite terminal. The remaining bank is strictly greater than 3/128. Full FEI remains OPEN; no new neighboring-disagreement lower bound is claimed.

## sources actually read, revisions and theorem locators

Read BOARD.md (snapshot 2026-10-23 03:14 UTC), B04 STREAM_NOTES.md v2, own STATUS and preceding stage derivation/report, and A018's 20261023T022754Z report and complete CLAIMS.json. Protocol revision 2026-10-11-execution-v2 governs the schema. A018-UNEQUAL-MEAN-RADIAL-LEDGER@1 has unchanged statement hash `cb9b7679c68363fc8daaeb7f6d6bee5d07ee9a2cc5d1d41cf5bf85da4e6785ea`. Exact source byte receipts are in out/SOURCE_RECEIPTS.json. The previous stage's >3/4 remainder paid Lambda only; A018's >5/8 remainder pays the FULL first q query. The present result starts from the latter. Previously read campaign and paper context supplies conventions, not a new external theorem assumption. The bent-splice falsifier remains imported: small disagreement alone cannot justify a vanishing collision-debt bound. The old constant-correlation closure is not presented as new.

## complete derivation or exact first unsupported line

# One data exposure after the complete paid unequal-mean query

All CE, KL and entropy use bits. Let e=2^-k, k>=2, h0=u and hk=(1-Ek)u+Ek,
where Ek=1[v=0] on k private bits. Supply Q0=(P0+delta_empty)/2 and
Qk=(Pk+delta_empty)/2, exact two-bit nonlinear mask reference Qs=Ps,
and the original q-frequency conditional lift Qh of average(Q0,Qk).
The actual activation is F(x,z,w)=1 when the binary physical gate x=0,
and F(x,z,w)=h(z)s(w) when x=1; all physical bits are uniform. The parent
core selects h0 or hk by q. The mask is -1 at one of four input points and
+1 at the other three, so its mean is 1/2 and its squared spectrum is flat.
The activation reference has data marginal (Qcore tensor Ps+delta_empty)/2,
lifted by its actual x-frequency conditional law. This is fixed before queries.

Consume A018 stage18's FULL first query: B=average_b(4I(hb)-cb)/2>1,
Tq=CE(F)-average CE(Fb)-4Inf_q(F)<1/4. For any old booking 0<=U<=1/8,
B-U-(Tq)_+>5/8. Both complete original Fb terminals remain. This differs from
A019 stage17's >3/4, which paid ONLY Lambda, not the full entropy/profile bill.

Now query one actual v bit in the q1 terminal. Keep q0 unchanged. Let Rcore
be the frequency marginal of the ORIGINAL Qk over this v bit. Both core
children receive this SAME Rcore, not fresh contaminated spectra. Their
functions are u and h_(k-1). Keep the same mask reference. Construct their
prescribed complete activation references by the original data-mixture rule
using Rcore and each child's actual x-frequency conditional.

These supplied references are finite: each child squared spectrum is at most
twice the folded parent spectrum pointwise (by (a+b)^2<=2(a^2+b^2)), whereas
Rcore is at least half that folded spectrum. Thus Rcore>=Pchild/4.
No positive child atom loses support, including k2's nonconstant h1 terminal.

For clarity retain also the literally inherited activation reference Ract,
obtained by marginalizing the original Q(F1) over v. It and each prescribed
child reference have the SAME data marginal (Rcore tensor Ps+delta_empty)/2.
The inherited-to-prescribed conversion gain is exactly
K_b=CE(P_Fchild,Ract)-CE(P_Fchild,Q_Fchild)
   =sum_data P_Fchild(data) KL(P_Fchild(x|data)||Ract(x|data))>=0.
Hence the FULL new query decrement is
Tv=CE(F1)-average CE(F1|v)
  =[CE(F1)-average CE(P_Fchild,Ract)]+average K_b.
The positive K_b terms MUST be included; calling the cheaper child code a
free refund and deleting them from this decrement would change the ledger.

The full decrement satisfies Tv=DeltaH_F1+KL_parent-average KL_child
<=DeltaH_F1+KL_parent. The original Qk>=Pk/2 gives core KL<=1.
The original activation mixture has KL_parent<=core KL/2<=1/2 by
the physical-label log-sum identity. This bound concerns the actual incoming
reference before the v query, not a newly supplied exact-spectrum reference.

It remains to bound the actual entropy decrement uniformly. Put
f(e)=eta((1-e)^2), eta(z)=-z log2(z), eta(0)=0, and
Hk=f(e)+4k e-2k e^2. Indeed the u singleton coefficient is 1-e;
the other 2^(k+1)-1 nonzero coefficients have absolute value e, by
expanding (1-Ek)u+Ek in characters. Thus this is the full actual entropy.
Then exactly
DeltaH_core/2=2e+[f(e)-f(2e)/2]/2+(k-2)e^2.
On [0,1/2], f''(z)=-2[3+2ln(1-z)]/ln2 is negative and |f''|<9:
ln2>2/3 follows from the first positive term of the atanh series, and ln2<1.
The midpoint Jensen gap therefore gives f(e)-f(2e)/2<(9/2)e^2,
so DeltaH_core/2<2e+(k+1/4)e^2<=41/64 for every k>=2.
The last expression decreases with integer k: both 2^-k and (k+1/4)4^-k do.

Define phi(b)=Psi(b/2), using the earlier exact activation profile. The new
curvature is C(e)=phi(e)-[phi(0)+phi(2e)]/2. Since phi is concave,
C'(e)=phi'(e)-phi'(2e)>=0 for e>0. Continuity handles e=0.
Consequently C(e)<=C(1/4)<1/16. The final strict sign is a single exact
rational-prime-log comparison, certified in out/CERTIFICATE.json. This is
a continuum argument followed by one exact sign, not an extrapolated sweep.
Therefore DeltaH_F1=DeltaH_core/2+C(e)<45/64 and Tv<77/64.

The q1 terminal has original physical reach1/2. Book the COMPLETE positive
new decrement, including inherited conversion and BOTH new child costs,
as (Tv)_+/2<77/128. This deliberately leaves the new physical v influence
unspent; there is no second claim against it. The SAME original bank obeys

 B-U-(Tq)_+-(Tv)_+/2 > 5/8-77/128 = 3/128.

The q0 sibling and its complete reference are retained throughout. The
original old debit U and first FULL query debit remain booked. The statement
is uniform in k>=2 and in the chosen v coordinate. If v is also queried on
q0, it is a true/reference dummy and its decrement is exactly0.

The first unsupported universal line is another interacting exposure from
the already diminished account. The surviving child references are inherited
marginals of Qk, not (Pchild+delta_empty)/2; their next KL price cannot be
declared <=1/2 by renewing the previous incoming-reference assumption.
Full FEI remains OPEN. Independent review of this continuation is pending.


For completeness the activation profile used above is Psi(mu)=eta((1+mu)^2/4)+eta((1-mu)^2/4)+1-mu^2-eta(mu^2)/2, with phi(b)=Psi(b/2). Direct differentiation gives Psi''(mu)=log2(mu^2/(1-mu^2)); hence phi is concave throughout the required b in [0,1/2], with endpoint continuity. This supplies the curvature step for the entire infinite k range. The endpoint strict sign uses the exact prime-log interval certificate in the checker, not floating point. The rational arithmetic identity 5/8-77/128=3/128 is exact. The original v influence is e/2 in the q1 terminal; it is left unspent in this conservative bound.

Independent review of A018 at its original full scope: write p=mr, z=ta, nu=beta^2/r (nu=1 if r=0), and A(p,z)=[p log2(p/z)+(1+p)log2((1+z)/(1+p))]/2. Splitting the core-label KL into empty and remaining rows, then applying the log-sum identity to the plus activation branch, gives exactly Lambda=A(p,z)-A(nu*p,nu*z)-[(1-m)E0+Erest+Kplus]/2. Each subtracted quantity is a KL cost and nonnegative. For a(kappa)=A(kappa*p,kappa*z), w=p(1+kappa*z)/(z(1+kappa*p)), direct differentiation gives a'=[p ln(w)+(z-p)/(1+kappa*z)]/(2 ln2)=p[ln(w)+1/w-1]/(2 ln2)>=0 and a''=-(p-z)^2/[2 ln2(1+kappa*p)(1+kappa*z)^2]<=0. Thus G=a(1)-a(nu)>=0. When p<=z, integration gives G=(1-nu)/(2 ln2) integral_p^z (v-p)/[v(1+v)(1+nu*v)] dv, bounded by log2((1+z)/(1+nu*z))/2 and then by (1-nu)log2(1+z)/2. Concavity also gives G<=(1-nu)[p log2(p/z)+(z-p)/ln2]/2 for positive p,z. Continuous zero cases use finite incoming CE support; t=0 forces m=0. This reconstructs the original statement without repairs. The 720 exact actual-Boolean/reference tests independently reconstruct the full activation law as an additional check; they do not prove arbitrary dimension by enumeration.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede every search in out/FROZEN_SPEC.json, REVIEW_SPEC.json and DIRECT_SPEC.json. Pilot k=2: 701 assertions, PASS. Main k=1..8: 75244 assertions, PASS, 1.813 seconds; k=1 is diagnostic, outside the theorem. Independent A018 review: 720 actual Boolean/reference cases, 52502 assertions, PASS, 2.374 seconds, including zero and unit boundary parameters. Direct literal character sums for k=2,3: 1972 assertions, PASS, 0.077 seconds. Total substantive assertions 129718 excluding the pilot. Exact Fraction coefficients and integer Walsh transforms are used; logarithmic signs have rational atanh-series bounds. No floating-point sign is accepted. Parameters were not raised automatically; estimated memory 100 MB and per-checker cap 60 seconds, so the >300 MB admission condition was not triggered.

Command: `python -B -X utf8 runs/20261023T032030Z-account03-A019-orthogonality-extensions/code/run_checks.py`. Source arithmetic helper normalized-text SHA256 is `1d90df4e3e58ea7261b8afdf6510c809a18ca4f524655fcb45dfc11b16f08295`; only elementary arithmetic definitions are reused, with actual references and the reviewed law reconstructed independently. No A018 checker was imported. The direct implementation replaces the Walsh transform by literal character summation. The Lean side-check command was `python -B -X utf8 runs/20261023T032030Z-account03-A019-orthogonality-extensions/code/check_lean.py`; its resource admission was held before compiler launch: `RuntimeError: Compute admission held (hung window or under 5500 MB free); no new compiler process`. No Lean verification is claimed for the entropy proof or arithmetic side file.

## proof dependencies and changed downstream conclusions

The acyclic chain is earlier A019 bank/family facts -> A018 full radial ledger and full first query -> this new inherited-v continuation. The review of the existing A018 version supplies no substantive repair; the imported statement and hash remain unchanged. New theorem independence is pending. The exact conversion gains K_b are positive parts of the decrement: deleting them when changing the terminal conditional would undercharge the query. This is the main reusable ledger correction. The old >3/4 Lambda-only remainder must never be substituted for the >5/8 full-query remainder. No priority or literature-novelty claim is made.

## one next mathematical action and independent reviewer

Expose a second interacting data coordinate with the exact surviving common marginal references and old debits retained; derive a cumulative cost invariant rather than renew the original KL<=1/2 price. A018 is the proposed independent reviewer of the new claim; A020/A092/A094 can consume the complete inherited-reference fixture. No messages were sent and no shared registry was changed. The exact first unsupported universal line is recorded in the theorem and CLAIMS.json: iteration on arbitrary remaining children with their carried marginals has no proved cumulative payment invariant.

## actual persistence receipts or precise save blocker

All four protocol files and code/out artifacts are saved locally in this run. PROGRESS.json and PACKET_DELTA.json are byte-identical; source and local artifact hashes are recorded in out/SOURCE_RECEIPTS.json and out/PERSISTENCE_RECEIPTS.json. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated only within A019. Remote copying, independent acceptance of the new theorem and downstream adoption are not verified. Brain self-care remains degraded/unverified because owner-model and state-of-mind notes are stale; personal-context conclusions remain affected and were not mathematical premises. No background job remains, and nothing was stopped. The stale signed-contract warning affects irreversible work; this stage performs only authorized reversible local research writes.

## Universal bridge

This stage moves C024 history transfer toward C019 stopping-tree payment by carrying one genuinely interacting data query through the original complete references after the full unequal-mean first-query bill, leaving >3/128 of the same bank uniformly over an unbounded family. The whole-set or arbitrary-core cumulative invariant remains open: inherited children cannot renew the original KL<=1/2 budget. The shortest next route is a second interacting exposure with these very marginals and every old debit retained, because it tests the missing iteration mechanism needed for a universal stopping tree rather than producing another disconnected class estimate.
