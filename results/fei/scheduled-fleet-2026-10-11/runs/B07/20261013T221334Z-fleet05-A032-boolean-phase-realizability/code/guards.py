import json,math
from fractions import Fraction as F
from pilot import ROOT,walsh
truth=[-1]+[1]*7;W=walsh(truth);ks=[];marg=[];Q=F(0)
for J in range(4):
    a=[W[J]**2,W[J+4]**2];z=sum(a);w=F(z,64);p=F(a[1],z)
    n=int(p not in (0,F(1,2),1));Q+=w*n;ks.append(w);marg.append(p)
I=sum(ks[J]*J.bit_count() for J in range(4))
assert ks==[F(5,8),F(1,8),F(1,8),F(1,8)] and Q==F(5,8) and I==F(1,2)
out={'three_bit_defect':{'truth':truth,'walsh_integers':W,'masses':list(map(str,ks)),'conditional_marginals':list(map(str,marg)),'Q':str(Q),'I_address':str(I),'H_address':'3-(5/8)log2(5)','guard':'retained; not excluded by product hypothesis'},'non_boolean_control':{'function':'psi(x)=product_i (sqrt(15)+x_i)/4, independent of both address variables','norm_squared':'1','spectral_marginals':'1/16','masses':['1','0','0','0'],'Q':'m','H_address_plus_I_address':'0','phase_admission_failure':'psi at all-plus is ((sqrt(15)+1)/4)^m>1 for m>=1'},'tensor_scope':'Tensor with an actual Boolean function having product squared spectrum adds only fair or deterministic coordinates (Boolean product rigidity), leaving Q, address masses and address influence unchanged. An arbitrary Boolean tensor seed need not preserve the conditional-product hypothesis; this refinement does not resolve that universal embedding.'}
(ROOT/'out/guards.json').write_text(json.dumps(out,indent=2));print('PASS: direct defect guard; exact symbolic non-Boolean control recorded')
