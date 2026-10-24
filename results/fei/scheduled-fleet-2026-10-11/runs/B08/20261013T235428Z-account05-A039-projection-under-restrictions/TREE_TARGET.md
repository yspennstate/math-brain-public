# A039 stage 2: optimizing coherent restriction debt

All information is in bits. At an actual Boolean restriction node g queried at i, debt minus the B08 posterior credit is h2(Inf_i(g))-I_P(S_i;S_-i)=B_i(g). The cumulative objective with a genuine terminal term is

    C(T;f)=sum_internal w_h B_i(g_h)+E_leaf H(g_leaf).

The exact physical entropy decrement B_i+JS_i proves C(T;f)=H(f)-sum_internal w_h JS_i. Thus optimizing this objective is maximizing the single-use mixture information released by one actual tree, not resetting the original TC account at every node. Without the terminal term, stopping immediately would trivially cost zero and would not solve the assigned payment.

Completing a leaf by one additional physical query decreases C by its nonnegative JS. Hence an optimum exists among complete trees. It obeys the finite Bellman equation

    V(g)=min_relevant_i [B_i(g)+(V(g|i=0)+V(g|i=1))/2], V(constants)=0.

Dropping irrelevant coordinates is harmless: they have zero B, JS and influence and identical children. Physical coordinate names stay owned by the unique first query on each path. Randomization of query choices cannot improve the minimum, since it averages feasible deterministic costs. The common root-spectral lift gives V(g)=min_T H(S_root|transcript(T)); its leaf Fourier entropy is zero but the root spectral posterior need not be determined.

The separate compatible-leaf-reference posterior KL kappa of A097 is not I_P(S_i;S_-i). A097's control-first B05 residual and all-even-k bound are already closed calibration results. This run does not call a new erasure optimum a new proof of that known FEI class or a universal reference-transfer payment.

## Symmetry-complete B05 restriction state space

Write k=2q and b(x)=(-1)^(x1x2+...+x(k-1)xk), b'=b-2*1_zero, and let selector y choose b,b'. Activate this core only when r independent controls are all zero. The original roots use r=2k; k=2 is a valid calibration and k=4 is a member of the archived local-refund obstruction. Binary coordinates correspond to signs (-1)^x.

Every descendant after only zero data restrictions is D(a,d,t,r): a intact quadratic pairs, d leftover singleton variables from pairs with one zero bit fixed, t=1 for the point-flipped core or t=2 for the still-unfixed selector. The core is the quadratic on 2a variables, with a point flip on all 2a+d variables (and a selector for t=2). If any fixed data bit is one, the point defect disappears. The resulting state is P(a,l,s,r): a intact quadratic pairs, l linear characters, global sign s in {+1,-1}, and r controls. Dummy variables are removed.

All coordinate choices fall into the following symmetric types, each querying one actual fresh physical coordinate. Inactive control children are constant +1.

    D control: active D(a,d,t,r-1), inactive constant.
    D pair: zero D(a-1,d+1,t,r), one P(a-1,1,+,r).
    D singleton: zero D(a,d-1,t,r), one P(a,0,+,r).
    D selector (t=2): zero P(a,0,+,r), one D(a,d,1,r).
    P control: active P(a,l,s,r-1), inactive constant.
    P pair: zero P(a-1,l,s,r), one P(a-1,l+1,s,r).
    P linear: zero P(a,l-1,s,r), one P(a,l-1,-s,r).

If a=d=0, D mode 1 is the negative constant core and D mode 2 is a linear character core. Plain positive constant cores are globally constant. This is an exhaustive classification of descendants and query orbits, not a heuristic reduction of the Boolean spectrum. Data pairs may be permuted and their two bits exchanged; controls and linear/singleton bits may be permuted within their types. Every descendant drops at least one actual dependent coordinate, so Bellman recursion terminates.

Core coefficients are computed by integer Walsh transforms. If the remaining core dimension is m, its coefficients are w_T/2^m, p=2^-r, and activated Fourier coefficients are 1+p(c_empty-1) at empty, p(c_empty-1) at nonempty control-only sets, and p c_T at each nonempty core index T, repeated over all 2^r control indices. This supplies exact spectra, B for each coordinate orbit, and the physical influence. The exceptional empty fiber is always retained. No control cube is materialized.

For a root of dimension N, all probabilities use denominator D=2^(2N). Entropies and B are exact integer linear combinations of log2(prime)/D. Cumulative Bellman costs use denominator D*2^N, so the half-child operation is an exact integer operation at every descendant. Every nonzero candidate-cost comparison is certified by a rational outward enclosure of its prime-log combination; identically zero coefficient maps are exact ties. No numerical sign determines the optimal action without an interval certificate.

## AND/point-defect trees

For the m-bit point defect, all relevant coordinates are symmetric; a query has one constant and one (m-1)-bit point-defect child. Hence EVERY complete adaptive tree has the same V_m and is optimal; no best-coordinate search is required. Put a_m=2^(1-m). At any active m-state, all nonempty residual fibers have equal parent coefficients of magnitude a_m; their total contribution to B_m is (2^(m-1)-1)*2 a_m^2. The empty fiber contributes phi((1-a_m)^2,a_m^2), with phi(x,y)=(x+y)h2(y/(x+y)). Thus

    V_m=B_m+V_(m-1)/2, V_1=0,
    V_m=sum_(j=2)^m 2^(-(m-j)) B_j.

This is an exact optimum formula in finite logarithms for all m, with terminal entropy retained by completing the tree. It does not repeat the retired point-defect H<=4I proof or the retired Gamma payment test.

First unsupported universal line: proving V(f)<=K I(f) for every Boolean f, or transferring a prescribed non-exact leaf reference through overlapping histories with a paid terminal cost. The finite B05 optimum and its state compression do not supply either universal estimate.
