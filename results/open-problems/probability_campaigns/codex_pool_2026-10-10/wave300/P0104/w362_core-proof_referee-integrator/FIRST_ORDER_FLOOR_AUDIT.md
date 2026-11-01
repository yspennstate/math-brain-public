# First-order floor and corrected route

The previous conditional implication was algebraically valid, but its proposed full-kernel decay input was impossible whenever the first-order energy is positive. w361 corrected the input; this audit independently verifies the correction.

Keep the two conventions distinct. In PRODUCT_RESAMPLING.md, E(t)=-C'(t) is the weighted energy. In w361's ATTEMPT.md, H(t)=exp(t)E(t) is the unweighted threshold-kernel sum. If v_S=||f_S||_2^2 for the finite independent-product expansion, then

    E(t)=sum_{S nonempty}|S|exp(-|S|t)v_S,
    H(t)=L+sum_{|S|>=2}|S|exp(-(|S|-1)t)v_S,
    L=sum_{|S|=1}v_S,
    R(t)=H(t)-L>=0,
    Var(f)=L+integral_0^infinity exp(-t)R(t)dt.

The finite sum proves each identity directly and gives H(t)->L. If L>0, a proposed bound H(t)<=C n F(n^(1/3)t) for every t>=0 forces F(s)>=L/(Cn) for every s>=0. It therefore contradicts the integrability of nonnegative F. There is no cancellation available because every spectral summand is nonnegative.

Our independent binary-square receipt has spectral masses v_1=1/4, v_2=3/32, v_3=0 and v_4=1/64. Therefore

    H(t)=1/4+(3/16)exp(-t)+(1/16)exp(-3t),
    L=1/4,
    Var(f)=1/4+3/32+1/64=23/64.

The corrected sufficient input is L_n<=C n^(2/3), R_n(t)<=C n F(n^(1/3)t) for every t>=0 with nonnegative integrable F, and H_n(t)>=c n for 0<=t<=c' n^(-1/3), with constants independent of n. The upper identity and substitution s=n^(1/3)t give C n^(2/3)(1+integral F). On the persistence interval exp(-t)>=exp(-c') for n>=1, giving c c' exp(-c') n^(2/3). All three quantitative inputs remain unproved.

The covariance-tail calibration in PRODUCT_RESAMPLING.md needs no correction: it uses the weighted energy and a finite-time covariance bound. That bound already includes the first-order contribution exp(-t)L_n. It does not assume the unweighted full kernel decays to zero.

The old R004 route verdict is changed from KEEP to FIX for the infeasible input. w361-C004 and w361-C005 receive separate KEEP verdicts for the floor identity and the corrected conditional implication. The parent target remains unresolved.

NEXT: Prove bounds on the first-order energy and on the coupled higher-order remainder, or prove the finite-time covariance bound directly; none is supplied by the spectral identity alone.
