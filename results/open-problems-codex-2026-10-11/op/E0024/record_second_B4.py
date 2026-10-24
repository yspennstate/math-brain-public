from pathlib import Path
s=r'''

## B4. Exact optimal symmetric-reference test for arbitrary Levy measures (proved)

This extends B3 beyond densities and stable processes. It is a characterization of the reference-law hypothesis, NOT a characterization of (H).

Let nu be any Levy measure on R^d, let nu^- be its reflection, and put Lambda=nu+nu^-. Lambda is symmetric and sigma-finite off zero. Write g=dnu/dLambda. Then 0<=g<=1 and dnu^-/dLambda=1-g; choose versions such that g(-x)=1-g(x) almost everywhere, as follows from uniqueness of Radon-Nikodym derivatives. Define

J(nu) = (1/4) int (sqrt(g)-sqrt(1-g))^2 dLambda,
h(x) = (1/4)(sqrt(g(x))+sqrt(1-g(x)))^2,
rho_* = h Lambda.

Then rho_* is symmetric, is a Levy measure, and dominates nu: h(-x)=h(x), 1/4<=h<=1/2, so nu<<rho_*. The bounds on h prove the Levy integrability condition.

For two sigma-finite Levy measures, write their unnormalized Hellinger integral as

I(nu,rho)=int (sqrt(dnu/dM)-sqrt(drho/dM))^2 dM,

where M=nu+rho; this is independent of the dominating measure. If nu<<rho, it equals int(1-sqrt(dnu/drho))^2 drho, including regions where the target density is zero.

### Optimality

For EVERY symmetric Levy measure rho, even one not dominating nu,

I(nu,rho)>=J(nu),

and equality holds for rho=rho_*. Thus J is exactly the minimum Hellinger cost of replacing the jump measure by a symmetric one.

Proof. Use the symmetric dominating measure M=Lambda+rho. Set f=dnu/dM, f^-=dnu^-/dM, s=drho/dM. Reflection gives f^-(x)=f(-x) and s(x)=s(-x) almost everywhere. Hence

2 I(nu,rho)=int [(sqrt(f)-sqrt(s))^2+(sqrt(f^-)-sqrt(s))^2] dM
 >= (1/2) int (sqrt(f)-sqrt(f^-))^2 dM
 = 2 J(nu).

The inequality is exactly B3.1. For the last equality, on {dLambda/dM>0} write f=g*dLambda/dM and f^-=(1-g)*dLambda/dM; outside it both are zero. This change of dominating measure proves the equality also for infinite integrals. For rho_*, sqrt(h)=(sqrt(g)+sqrt(1-g))/2, so

I(nu,rho_*)=int [sqrt(g)-(sqrt(g)+sqrt(1-g))/2]^2 dLambda
           =(1/4) int (sqrt(g)-sqrt(1-g))^2 dLambda=J(nu).

This proves optimality. QED.

### Exact path-law symmetrization criterion

For a Levy process with triplet (a,Q,nu), a symmetric Levy reference to which its finite-horizon laws are absolutely continuous exists IF AND ONLY IF

J(nu)<infinity
and v:=a+int_{|x|<1} x(nu-rho_*)(dx) belongs to Range(Q).       (B4.1)

When these hold, (0,Q,rho_*) is such a reference.

Proof. If J is finite, the small-jump vector integral defining v is absolutely convergent by the Cauchy-Schwarz argument in B2, applied to nu<<rho_* and I=J. If v belongs to Range(Q), source Theorem 4.5 with reference (0,Q,rho_*) gives the asserted local absolute continuity.

Conversely suppose a symmetric reference (0,Q_0,rho) exists. Source Theorem 4.5 forces Q_0=Q, I(nu,rho)<infinity and a+int_{|x|<1}x(nu-rho)(dx) in Range(Q). Optimality implies J<infinity. Using a common dominating measure and (u+w)^2<=2u^2+2w^2 gives

I(rho,rho_*)<=2 I(rho,nu)+2 I(nu,rho_*)<infinity.

For ANY two Levy measures A,B with finite Hellinger integral, Cauchy-Schwarz proves

int_{|x|<1}|x| |A-B|(dx)
 <= sqrt(I(A,B)) * sqrt(2 int_{|x|<1}|x|^2(A+B)(dx))<infinity.

Apply it to rho and rho_*. Their signed difference is symmetric; its absolutely convergent small-jump vector integral is zero by the substitution x -> -x. Therefore

int_{|x|<1}x(nu-rho)(dx)=int_{|x|<1}x(nu-rho_*)(dx),

so v belongs to Range(Q). QED.

Notice also that Lambda/2-rho_* is a finite symmetric measure when J<infinity: its density relative to Lambda is (sqrt(g)-sqrt(1-g))^2/4, so its total mass is J. This is another check on the drift correction.

B3's skew stable process has J=infinity, even though it satisfies (H). Thus (B4.1) cannot be inferred from the original (H) hypotheses. B4 nonetheless gives an exact criterion, valid for atomic and singular jump measures as well, for how far the selected path-law reduction can go. It does not infer full (H) for a singular symmetric reference from (H_m), and does not establish an unproved symmetric-product theorem.
'''
p=Path('SECOND_ATTEMPT.md');p.write_text(p.read_text(encoding='utf8')+s,encoding='utf8')
