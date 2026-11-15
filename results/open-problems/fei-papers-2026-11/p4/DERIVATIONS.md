# P4 derivations (re-derived by hand 10 Nov 23:1x, an agent; sources FLOW.md 12(z),(aa),(bb), STATE 2b)

Notation. mu(S) = fhat(S)^2, U ~ mu, I = E|U|, Var = 1 - mu(empty). D_S f = sum_{U >= S} fhat(U) chi_{U-S}.
up_t(T) = sum_{U >= T} mu(U) t^{|U-T|} = ||T_sqrt(t) D_S f||^2, up = up_1 (= KKLMS generalized influence I_T[f]).
A = E_mu log2(1/up(S)), B = E_mu log2(up(S)/mu(S)), H = A + B.

(a) Split. D_S f takes values in 2^(1-|S|) Z (2^|S| terms +-1, even sum, divided by 2^|S|). So
    (D_S f)^2 >= 2^(1-|S|) |D_S f| pointwise, up(S) >= 2^(1-|S|) E|D_S f| >= 2^(1-|S|) |fhat(S)|, mu(S) <= 4^(|S|-1) up(S)^2.
    For S nonempty log2(1/up(S)) <= (|S|-1) + (1/2) log2(1/mu(S)); S empty contributes 0 (up = 1).
    A <= H/2 + I - Var, hence H <= 2B + 2I - 2Var. Also A >= 0 so B <= H. FEI <=> B <= C I.

(b) Fixed t in (0,1). nu_t(T) = (1-t)^|T| up_t(T) = P[thinned U = T] (each element kept w.p. 1-t): a probability law.
    Gibbs: H <= E_mu log2(1/nu_t(S)) = E_mu log2(1/up_t(S)) + I log2(1/(1-t)). And up_t >= mu gives E log2(1/up_t) <= H.
    FEI <=> E_mu log2(1/up_t(S)) <= C_t I, for each fixed t < 1. (t = 1 is A: necessary only.)

(c) Tilted excess. d/d(ln t) ln up_t(T) = sum_{U>=T} |U-T| mu(U) t^|U-T| / up_t(T) =: m_t(T) (posterior mean of the
    deleted count); its ln t-derivative is a posterior variance, so m_t is nondecreasing in t. up_0(T) = mu(T), so
    B = (1/ln 2) int_0^1 E_mu m_t(S) dt / t (Tonelli, integrand >= 0).
    Combining (b) at lambda with (a): E log2(1/up_lam) = A + (1/ln2) int_lam^1 E m_t dt/t, so
    H/2 <= I (1 + log2(1/(1-lam))) - Var + (1/ln 2) int_lam^1 E_mu m_t dt/t.
    FEI <=> int_{1/2}^1 E_mu m_t dt <= C I  (=> : int_{1/2}^1 E m_t dt <= int_0^1 E m_t dt/t = B ln 2 <= H ln 2).

(d) Predictor. Q(T,i) = mu(T+i)/I on pairs i not in T (a law). L = E_Q log2((mu(T)+mu(T+i))/mu(T+i)).
    For p_i(T) >= 0, K = (1/I) sum (mu(T)+mu(T+i)) p_i(T), R = (mu(T)+mu(T+i)) p_i(T)/(K I). Gibbs E_Q log(Q/R) >= 0 gives
    L <= log2 K + E_Q log2(1/p_i(T)), equality at p_i(T) = mu(T+i)/(mu(T)+mu(T+i)) (then K = 1).
    sum_i E_i = I L + sum mu(T) log2(1 + mu(T+i)/mu(T)) in [I L, I L + I/ln 2]. With P1 (FEI <=> sum E_i <= C I):
    FEI <=> L <= C.

(e) Translation. (chi_R f)^(S) = fhat(S xor R); pairs {T, T+i} map to pairs, Phi symmetric, so every E_i is
    invariant; Inf_i(chi_R f) = 1 - Inf_i(f) for i in R. R = {i : Inf_i > 1/2} gives I(chi_R f) = sum min(p_i, 1-p_i).
    FEI <=> sum_i E_i <= C sum_i min(Inf_i, 1 - Inf_i). Since |fhat({i})| <= E|D_i f| = Inf_i,
    Inf_i - fhat({i})^2 >= p_i(1-p_i) >= min/2, so also FEI <=> sum E_i <= C (I - W_1). Comparison: the author 2610.16069
    Lemma 2.2 (cite).
