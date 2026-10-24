# C0143: Exponential infinite-cluster contact tail on every regular tree above criticality

Label: proof; author checked only. Independent audit: PENDING w347.

On the (b+1)-regular tree with b>=2, independent Bernoulli bond percolation at fixed p in (1/b,1), there are constants C,c>0 such that P_p(|C_o|<infinity and J_o>n)<=C*exp(-c*n), where J_o counts all graph edges from C_o to vertices in any infinite open cluster. The assertion also holds trivially at p=1.

Assumptions: A regular tree of degree b+1, integer b>=2; Independent Bernoulli bond percolation; Fixed p>1/b; Contacts count graph edges, which must be closed at a finite open-cluster boundary

Let t in (0,1) be the smaller solution of t=1-p+p*t^b. The root cluster is finite with probability t^(b+1). Conditional on finiteness, each outward edge opens into a finite branch with probability r=p*t^(b-1); this gives root offspring Binomial(b+1,r) and later offspring Binomial(b,r), independently. Strict convexity of f(x)=1-p+p*x^b-x, with roots t and 1, gives f'(t)<0, hence b*r<1. The forward progeny equation is F=z*(1-r+r*F)^b. The analytic implicit function theorem at (z,F)=(1,1), whose derivative in F is 1-b*r>0, gives a positive fixed point F_*(z)>1 for some z>1 sufficiently close to one. In fact F_*(z)>=z. The generating functions of generation-truncated progeny start at F_0(z)=z and satisfy F_(m+1)(z)=z*(1-r+r*F_m(z))^b. They increase and are bounded above by F_*(z), by induction. Monotone convergence then proves that the full progeny has a finite exponential moment at this z. The root-size generating function is z*(1-r+r*F(z))^(b+1), also finite. Markov's inequality gives an exponential tail for the finite cluster size. A finite connected tree with N vertices has exactly (b-1)*N+2 boundary edges by the degree sum, so J_o<=(b-1)*N+2. This transfers the size bound to J_o, with constants depending on b,p. At p=1 the finite-cluster event is empty.

Limits: This does not give the requested estimate on arbitrary transitive graphs. The constants deteriorate toward criticality; no uniform rate in p is asserted.

Existing card: None
Source snapshot: ~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/problems.jsonl:143
