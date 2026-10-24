"""Exact abstract-boundary obstructions, not forest counterexamples."""
from fractions import Fraction as F
from pathlib import Path
import json
from forest_four_port_adjacent_exploration import coeff_vectors, rayleigh


def main():
    rows=[F(1,1000),F(10),F(1,1000)];s=sum(rows);report={'status':'formal boundary rows only','cases':[]}
    for n in (4,5):
        states,coeffs=coeff_vectors(rows,[F(1)]*n)
        i=states.index((0,)*n);j=states.index(tuple(range(n)));A,E,G,C=coeffs
        cross=E[i]*G[j]+E[j]*G[i]-A[i]*C[j]-A[j]*C[i]
        assert cross<0
        boundary=[F(0)]*len(states);boundary[i]=F(3158);boundary[j]=F(1)
        R,values=rayleigh(coeffs,boundary)
        D=3158*(1+n*s)+(1+s)**n
        Dp=3158*n+n*(1+s)**(n-1)
        Dpp=n*(n-1)*(1+s)**(n-2)
        p=3158*(1+n*s)/D
        Us=n/(1+s);Uc=n*n/(1+n*s)
        Gs=n/(1+s)**2;Gc=n**3/(1+n*s)**2
        U=p*Uc+(1-p)*Us
        Gamma=p*Gc+(1-p)*Gs+s*p*(1-p)*(Uc-Us)**2
        logsecond=Dpp/D-(Dp/D)**2
        assert U/s-Gamma==-logsecond/s
        a,b,c=rows
        assert R==D*D*a*c*(U+a*c*U*U-b*Gamma)
        if n==5:assert R<0 and logsecond>0
        if n==4:assert R>0
        report['cases'].append({'ports':n,'outer_rows':'1/1000','middle_row':'10','column_profile':'all ones',
            'negative_bilinear_boundary_coefficient':str(cross),
            'formal_all_connected_weight':'3158','formal_all_separate_weight':'1',
            'all_other_boundary_weights':'0','exact_four_coefficients':list(map(str,values)),
            'exact_Rayleigh':str(R),'exact_logZ_second':str(logsecond),
            'ordinary_forest_backbone_realizability':'ruled out by matroid log-concavity' if n==5 else 'not asserted'})
    Path(__file__).with_name('forest_four_plus_port_boundary_obstructions_results.json').write_text(json.dumps(report,indent=2)+'\n')
    print('Exact four-port negative cross coefficient and five-port unrealizable boundary counterexample PASS.')


if __name__=='__main__':main()
