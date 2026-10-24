import pathlib
p=pathlib.Path('ATTEMPT.md');t=p.read_text(encoding='utf8');start=t.index('## 4. Reciprocal-weight coupling');end=t.index('## 5. Combine the bounds');old=t[start:end]
new='''## 4. A direct reciprocal certificate for every spectral sector

Assume n>=8 and 4/n^2<=beta<=1/16. Put a=n*sqrt(beta), so 2<=a<=n/4. We prove gamma_B>=sqrt(beta)/5 by the complete sector decomposition, avoiding any probabilistic tail approximation.

For degree 0, its positive spectrum is that of A_0 from Section 2. Use h(k)=1/(k+a). Direct substitution gives

    -A_0 h(k)/h(k)
      =beta(n-k-1)/(k+a+1)-k(k-1)/[n(k+a-1)]+beta+2k/n
      >=beta(n-k-1)/(k+a+1)+beta+k/n.

The inequality uses a>=1 to bound k(k-1)/(k+a-1)<=k. If k<=a then n-k-1>=n/2 (n>=8,a<=n/4) and k+a+1<=5a/2. Thus the birth term is at least beta*n/(5a)=sqrt(beta)/5. If k>=a the last term k/n is at least sqrt(beta). It follows from positive-function comparison that every positive eigenvalue in degree 0 is at least sqrt(beta)/5.

For each degree l>=1, use the same h(k)=1/(k+a) on l<=k<=n-l in (H). Its exact certificate is

    -A_l h(k)/h(k)
      =beta(n-k-l)/(k+a+1) + l beta
       +(k-1)[(l-1)k+l a]/[n(k+a-1)].                      (S)

To verify the cancellation, combine the death contribution

    -(k-1)(k-l)/[n(k+a-1)]

with the killing contribution l(k-1)/n; their numerator is (k-1)[l(k+a-1)-(k-l)]=(k-1)[(l-1)k+l a]. All terms displayed in (S) are nonnegative on the sector domain.

If k<=a, then l<=k implies n-k-l>=n-2a>=n/2, while k+a+1<=5a/2. Its birth term is again at least sqrt(beta)/5. If k>=a, then [(l-1)k+l a]>=a and

    (k-1)/(k+a-1)>=1/3,

because 3(k-1)-(k+a-1)=2k-a-2>=a-2>=0. The last term in (S) is therefore at least a/(3n)=sqrt(beta)/3. Positive-function comparison proves the principal eigenvalue of every -A_l is at least sqrt(beta)/5, hence so are all their eigenvalues.

Completeness of the orthogonal sector decomposition now gives

    gamma_B>=sqrt(beta)/5,    gamma_M>=sqrt(beta)/5.         (L1)

This proof works at the boundary n=8,beta=1/16,a=2 and has no unknown concentration estimate. A fully written independent coupling proof is retained in Appendix A below; it obtains the same bound and was useful for independently checking factors in the generator.

'''
t=t[:start]+new+t[end:];t+='\n## Appendix A. Independent coupling proof of (L1)\n\n'+old[old.index('Assume n>=8'):]
t=t.replace('There is no remaining mathematical gap in this order statement.','There is no remaining mathematical gap in this order statement. The two independent proofs of (L1) are the direct sector certificate in Section 4 and the coupling argument in Appendix A.')
p.write_text(t,encoding='utf8')
print('Direct all-sector certificate saved; independent coupling retained.')
