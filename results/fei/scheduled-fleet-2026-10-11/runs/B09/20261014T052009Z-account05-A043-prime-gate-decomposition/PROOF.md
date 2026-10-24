# Full four-bias coherent payment for prime56067

Use reflected coordinates (a,x,y,z)=(a,1-b,1-c,z), with probabilities (alpha,e,d,q). Write u=4alpha(1-alpha), vx=4e(1-e), vy=4d(1-d), w=4q(1-q). All four probabilities are interior unless discussing limits. Natural corrected entropy E=(ln2)Hplus uses h(t)=t^2ln(1/t^2), h(0)=0. Delta=I-Var is spectral deficit. The gate is

    f=-1+2z+2xy-2z[ax+(1-a)y].

It is the reflected form of the actual essential prime mask56067. No separately squared conjunction spectrum is used.

## Source review and recovered exact spectrum

Read A042-COHERENT-PRIME-LITERAL-FACE-ENDPOINT@1, hash bdb413e7929b8d926016b04a1ebc20b737b4adde4b91f37cf3537f011d91f6f9. From the Boolean polynomial, the singleton coefficients are c_a=q(d-e), c_x=d-q alpha, c_y=e-q(1-alpha), c_z=1-alpha e-(1-alpha)d. The pair coefficients are

    c_ax=-q/2, c_ay=q/2, c_az=(d-e)/2,
    c_xy=1/2, c_xz=-alpha/2, c_yz=-(1-alpha)/2.

The only triples are c_axz=-1/4,c_ayz=1/4; there is no quartic coefficient. Let B be total pair mass, Tx=u*vx*w/16, Ty=u*vy*w/16, T=Tx+Ty. Then Delta=B+2T, and R=sum_{|S|>=3}(|S|-2)P(S)=T. Direct degree counting also gives the source's exact identity

    Delta=Le e(1-e)+Ld d(1-d)+(uw/4)(d-e)^2+4ed(1-e)(1-d),
    Le=4alpha q(2-alpha-q), Ld=4(1-alpha)q(1+alpha-q).

This reconstruction and the independent tensor-moment checker recover the source spectrum, entropy and deficit at actual input laws.

For the source's tangent calculation, expanding its Ke expression in the formal symbols1,ln2,ln q,ln alpha and dividing by Le gives coefficients

    2(1-q)/(2-alpha-q), 2, -2q/(2-alpha-q), -2alpha/(2-alpha-q).

Thus Ke/Le=ln4+2[(1-q)+q ln(1/q)+alpha ln(1/alpha)]/(2-alpha-q). The corresponding Kd replaces alpha by1-alpha. The zero-baseline h(q(d-e)) and h((d-e)/2) terms are O(delta^2ln(1/delta)), without dividing by d-e; all nonzero-baseline terms have ordinary Taylor remainders on compact interior alpha,q domains. Hence the source's independent-rate cluster interval and collar follow, and the strict tangent inequality uses t ln(1/t)<=1-t exactly as stated. No uniform collar is inferred at alpha or q endpoints.

Independently reconstruct the source joint path alpha=1-t^2,e=t^6,d=t^8,q=1-t from the exact coefficients. Delta=4t^7+O(t^8). The x singleton contributes8t^7, the z singleton8t^7, and xz pair4ln4*t^7; all other terms are O(t^8ln(1/t)) or smaller. Therefore E=(16+8ln2)t^7+O(t^8ln(1/t)) and Hplus/Delta tends to Cstar=2+4/ln2. This does not substitute moving alpha,q into a fixed-parameter remainder. Verdict HOLDS for A042's complete stated narrow claim; no repair was supplied. The new global upper bound below is separate work.

## Exact pair-normalization ledger

Define A(t)=t ln(1/t)/(1-t), so0<=A(t)<=1 on[0,1], with continuous endpoint values. All six pairs have an ln4*P baseline. Their excess costs are exactly

    G_ax=2Tx*A(q), G_ay=2Ty*A(q),
    G_xz=2Tx*A(alpha), G_yz=2Ty*A(1-alpha),
    G_xy=0,
    G_az=(uw/4)h(d-e).

The expressions are from the combined coefficients of this single Boolean gate. All occurrences of Tx and Ty refer to the same physical triple packets, not newly created credits.

The remaining difference coefficient is paid by the two data variances. Put t=|d-e|. If d>=e, then d=e+t and

    e(1-e)+d(1-d)=t(1-t)+2e(1-t-e)>=t(1-t).

The other order is identical after exchanging d,e. The scalar logarithm inequality gives h(t)<=2t(1-t). Therefore

    G_az <= (uw/8)(vx+vy)=2(Tx+Ty).

The other four excesses sum to at most4T. Thus total pair excess G<=6T. Triples contribute ln16*T. Consequently the full higher-degree entropy has the exact decomposition and rigorous bound

    E_ge2=ln4*B+G+ln16*T=ln4*Delta+G
            <=ln4*Delta+6T.

This is a complete bias-independent payment of the signed quadratic profile, after amplitude cancellation. It does not charge the raw constituent shared-guard loss L.

## Singleton reserve and all-bias theorem

For every Boolean sign, Di=(f|Yi=1-f|Yi=0)/2 lies in{-1,0,1}; |E Di|<=E Di^2 and h(E Di)<=2|E Di|(1-|E Di|). Parseval supplies E_single<=4Delta-2R. Here R=T, so

    E <= (4+ln4)Delta+4T
      <= (6+ln4)Delta,

because2T<=Delta. In bits,

    Hplus(f) <= (2+6/ln2)(I-Var)

for every four independent interior biases. The constant is approximately10.656170245334. It is a proved nonsharp global upper bound; the sharp all-bias supremum is between Cstar=2+4/ln2 and2+6/ln2. The lower endpoint is the actual source joint path, not a contracted zero-deficit quotient. Constants and deterministic inputs follow by contraction/continuity. At uniform physical inputs, H=Hplus-t log2 t, t=(E f)^2, and -t ln t<=1-t=Var gives ordinary H<=(2+6/ln2)I. Exact nonnegative-weight disjoint corrected entropy/deficit composition transfers this bound to read-once formulas of these prime gates and any gates already bounded by that constant at their actual induced laws.

The exact retained slack S=4Delta-2T-E_single is nonnegative. Since E_ge2=ln4*Delta+G, the sharp-Cstar residual is

    (4+ln4)Delta-E = S+2T-G.

Thus sharp Cstar would follow from G<=S+2T. The sufficient condition S>=4T, or a polynomial lower bound on S, is only an exploratory candidate unless proved. The theorem above does not assume either. The checker records finite signs separately from continuum conclusions.

## Exact failure of the polynomial slack shortcut

Set ti=|ci|, di=E Di^2, and let vi be the input variance factors. The exact reserve is S=sum_i vi[2(di-ti)+phi(ti)], where phi(t)=2t(1-t)-h(t). The inequality ln r<=(r-r^(-1))/2 for r>=1 gives 2t ln(1/t)<=1-t^2, hence phi(t)>=t(1-t)^2. Thus the rational polynomial surrogate

    S_poly=sum_i vi[2(di-ti)+ti(1-ti)^2]

is a valid lower bound on S. However S_poly>=4T is FALSE. At (alpha,e,d,q)=(1/2,1/1024,1/1048576,1/16), exact arithmetic gives

    S_poly-4T=-16029490109593689663/302231454903657293676544<0.

The eight sign-polynomial Bernstein pilot had negative coefficients in six sign regions; that pilot alone was inconclusive. The displayed actual rational witness refutes the sufficient polynomial assertion. Outward rational logarithm intervals at this same witness certify S>=4T and the sharp-Cstar inequality. Consequently neither actual assertion is refuted. All661 frozen fixtures also certify both signs, but those are finite evidence only. The first unsupported sharp step remains G<=S+2T for every interior input law. The global nonsharp theorem uses none of these proposed slack strengthenings.

For completeness, the read-once transfer uses the exact identities Hplus(F)=Hplus(g)+sum_i wi Hplus(fi) and Delta(F)=Delta(g)+sum_i wi Delta(fi), where wi=I_i(g)/Var(fi)>=0 and g is evaluated at the actual induced independent child laws. Constants are contracted. Applying one common bound to the root and children proves the asserted transfer by induction; it does not replace a prime's induced law by the uniform law.

## Scope and universal frontier

A044-SHARED-GUARD-CANCELLATION-OBSTRUCTION@1 (hash7d78ab7cf325ab80263b94a66f6ac63f38d885de9a60e8fce6bebee46403a120) already proves L/Delta diverges on alpha=q=1/2,e=d tending to0, even though actual entropy stays paid. Its A042 independent acceptance is consumed; it is not reopened as a positive raw-loss debit. The earlier A044 acceptance of A043 two-term overlap/classification/census remains scoped and excludes reacceptance of the reviewer's own mux dependency.

This stage closes the arbitrary-four-bias inequality for the first coherent shared-guard prime, while retaining a nonsharp gap in the optimal constant. For arbitrary primes the pair amplitudes can depend on more than two remaining coordinates, and their actual difference costs lack the proved variance relation above. The first unsupported universal step is a cofactor-compatible assignment of those costs to actual higher-degree packets and inherited terminal entropy with bounded congestion. Applying this gate-specific affine ledger to every prime is not justified.
