# Independent reconstruction: B16-RETAINED-KL-SANDWICH@1

Verdict: HOLDS at the exact stated stopping-tree scope. This review independently reconstructs the analytic proof; the lead's float census is evidence, not a sign certificate. Author/reviewer independence: A080 did not contribute to the lead's version 1.

Let u=a_T and v=a_(T+i) be parent coefficients, q=u²+v² and m=min(u²,v²). The two actual Boolean children have coefficients u+v and u-v. Their average squared mass is q. Thus erasure is B_i=sum q h2(m/q), and the entropy chain rule gives Delta_i H=B_i+JS(children). All zero-q packets contribute zero.

1. Expand each binary entropy. Q_i=sum m log2(q/m) and B_i-Q_i=sum (q-m)log2(q/(q-m)). Since -(1-t)ln(1-t)<=t for t=m/q, 0<=B_i-Q_i<=M_i/ln2, M_i=sum m.
2. For a parent pair put z=2uv/q, using its absolute value in the even function d(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2. The JS packet equals q d(z)/ln2. Differentiation proves d(z)<=1-sqrt(1-z²): the derivative gap z/sqrt(1-z²)-atanh(z) starts at zero and has derivative (1-z²)^(-3/2)-(1-z²)^(-1)>=0. Since q[1-sqrt(1-z²)]=2m, JS_i<=2M_i/ln2. The endpoints follow by continuity. This is sharper than merely bounding JS by queried influence.
3. Parent spectra give M_i<=min(Inf_i,1-Inf_i)<=Inf_i. Equivalently, child coefficients a,b give m=(|a|-|b|)²/4, M_i=(1-sum|ab|)/2, and triangle inequality bounds the affinity below by |1-2Inf_i|. These definitions agree exactly; unoriented child-difference mass (a-b)²/4 is not M_i.
4. At M_i>0 define nu_T=m_T/M_i. Parseval makes q a probability law and m>0 implies q>0. Substitution yields Q_i=M_i[log2(1/M_i)-D2(nu||q)]. No singular KL term is introduced. At M_i=0 use Q_i=0.
5. In a physical binary restriction tree, conditional on reaching a node, the next unfixed uniform bit is fair even when its choice depends on earlier values. Hence child weights are w/2 and w=2^-depth. Telescoping gives H(root)-E H(leaf)=sum w Delta H and I(root)-E I(leaf)=sum w Inf. Re-querying a fixed coordinate is excluded or removed as a redundant step. The tree is finite; a branch uses at most n distinct physical coordinates.
6. Combining these identities proves Q_tree+E H(leaf)<=H(root)<=Q_tree+E H(leaf)+(3/ln2)M_tree and M_tree<=I(root)-E I(leaf). All arbitrary Boolean leaf terms remain present.

For complete trees the terminal functions are constant. A universal bound Q_tree<=K I for one admissibly chosen complete tree per f implies FEI(K+3/ln2); FEI(C) implies Q_tree<=C I for every complete tree. This establishes equivalence of finiteness, not equality of Q across orders or equivalence of prescribed numerical constants. Different trees can have different Q, within (3/ln2)I. At stopping trees neither Q alone nor the leaf-free endpoint is sufficient.

Every line in the lead's version 1 is supported; first unsupported universal line remains a uniform finite bound on Q_tree/I, equivalently FEI. This does not certify the lead's separate majority-Lambda conjecture.
