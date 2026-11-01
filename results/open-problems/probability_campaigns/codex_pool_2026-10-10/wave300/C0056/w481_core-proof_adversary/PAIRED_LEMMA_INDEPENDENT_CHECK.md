# Independent check of w480's proposed entropy identity

2026-10-10. Checked the statement in w480/STATEMENT_FOR_ADVERSARY.md after saving INDEPENDENT_OBSTRUCTION.md and CAVITY_REDUCTION.md. No w480 proof text has yet been read. This is an independent verification of the proposed formula, with a separate proof of the entropy-to-AC implication. Review by w482 is still required for this derivation.

## Exact integral: the proposed constant and quantifiers are correct

For a in R, b>0, lambda>0, write f(v)=b/[pi*((lambda v-a)^2+b^2)]. Substitute t=(lambda v-a)/b and c=1/(pi b). The integral over all real v is F(c)/lambda, where

F(c)=(1/pi) integral_R log(1+c/(1+t^2))/(1+t^2) dt.

For c>=0, differentiating under the integral is justified by domination by (1+t^2)^(-2). A partial-fraction integral gives

F'(c)=(1/pi) integral_R 1/((1+t^2)(1+c+t^2)) dt
     =1/(sqrt(1+c)*(1+sqrt(1+c))).

At c=0 this expression is 1/2, agreeing with the direct integral. F(0)=0. Integrating the derivative proves

integral_R f(v) log(1+f(v)) dv
 = (2/lambda) log((1+sqrt(1+1/(pi b)))/2).

Translation of a disappears because the integral is over the whole real line. This is not the equality for a uniform[-1,1] random variable; truncation to [-1,1] and its density 1/2 give an upper bound:

E[f(V_0) log(1+f(V_0)) | H^(0)]
 <= (1/lambda) log((1+sqrt(1+1/(pi b)))/2)
 <= (1/(2 lambda)) log(1+1/b).

The second inequality uses (1+sqrt(1+c))/2 <= sqrt(1+c), then c=1/(pi b)<=1/b. This controls constants without replacing the actual site law by an unbounded law.

## A complete entropy criterion without a hidden independence assumption

Let mu_omega be a probability measure and let f_eta=P_eta*mu_omega, with normalized Poisson kernel P_eta(t)=eta/[pi*(t^2+eta^2)]. Fix a bounded open interval J and a deterministic sequence eta_n decreasing to zero. Suppose

sup_n E integral_J Phi(f_eta_n(E)) dE <= C < infinity,
where Phi(t)=t log(1+t), t>=0.

Fatou gives T(omega)=liminf_n integral_J Phi(f_eta_n) finite almost surely. For each such omega choose a subsequence with all its entropy integrals <=T+1. For K>0 and every measurable B contained in J,

integral_B f_eta_n <= K|B| + (T+1)/log(1+K)

along that subsequence: split into f<=K and f>K, and use Phi(f)>=f log(1+K) on the latter set. Absolute continuity follows directly. For a compact Lebesgue-null N contained in J, take open U with N contained in U, closure(U) contained in J, and arbitrarily small |U|. Choose phi in C_c(U), 0<=phi<=1, phi=1 on N. Poisson approximation gives mu_omega(N) <= lim_n integral phi f_eta_n <= K|U|+(T+1)/log(1+K). Let |U| decrease to zero with K fixed, then K increase to infinity. Thus mu_omega(N)=0. Inner regularity of the finite measure on J extends this to every Lebesgue-null Borel subset of J. No pointwise-to-measure inference, exchange of probability and boundary limits, or inter-site independence is required.

Applying the verified conditional bound above shows that w480's (LG) assumption implies this criterion with C <= (1/(2 lambda)) sup_n E integral_J log(1+1/b(E,eta_n)) dE. Countably many sites then give the operator-level pure AC conclusion as in CAVITY_REDUCTION.md. Nonzero spectral projection and GOE statistics remain separate.

## Verdict and concrete missing premise

Scoped verdict: the proposed exact identity is KEEP; the entropy-to-AC implication is KEEP under the explicitly infinite-volume, fixed-lambda (LG) premise. These are independent checks of the statement, not a referee approval of an unseen proof or a served-model gate receipt.

The logarithmic moment (LG) is the unproved input. First-moment spectral averaging cannot supply it. In the diagonal iid model S=0 and b=eta, so integral_J log(1+1/b)=|J| log(1+1/eta) diverges, even though E Im G_00<=pi/(2 lambda). This gives the minimal counterexample to deriving (LG) from spectral averaging alone. The logarithmic premise is weaker than the inverse-b premise independently saved in CAVITY_REDUCTION.md.

NEXT: Read w480's finished proof only at the entropy compactness and finite/infinite-volume steps; test any proposed proof of (LG) at fixed lambda against this counterexample and the order of limits.
