from pathlib import Path
R=Path(__file__).resolve().parents[1];p=R/'DERIVATION.md';s=p.read_text(encoding='utf-8')
s=s.replace('h2(d_j)+(2/ln2)d_j','h2(d_j)+(4/ln2)d_j').replace('log2(1/d_j)+3/ln2','log2(1/d_j)+5/ln2')
lo=s.index('For completeness,');hi=s.index('The hypercube',lo)
s=s[:lo]+'''For completeness, the child amplitudes u,v have m=(u²+v²)/2. The entropy decrement is membership conditional entropy plus JS of the child squared spectra. Membership entropy is at most h2(d_j) by concavity. The pair JS contribution in natural units is

    [u² ln(u²/m)+v² ln(v²/m)]/2
    <= (u²-v²)²/[2(u²+v²)] <= (u-v)².

The first inequality is log x<=x-1 (zero terms by continuity), and the second is (u+v)²<=2(u²+v²). Summing and dividing by ln2 gives JS<=4d_j/ln2, because sum(u-v)²=4d_j. Zero pairs contribute zero and require no division. Thus no sharp JS/Hellinger comparison or external analytic premise is required.

Since ln2>3/5, 5/ln2<9. Combining (1),(2) and summing log2(1/d_j)=s0-j-1 gives

    L_ell <= (1+2^-ell)c + 2pt T,
    T=15(s0-ell)+ell(s0+8)-ell(ell-1)/2.                (3)

This bounds the full leaf-plus-query bill, not selector entropy alone. The elementary inequality ln2>3/5 follows, for example, by integrating 1/x on [1,2] and using the lower midpoint-paired bound 2/3 (or the first atanh term at 1/3).

'''+s[hi:]
s=s.replace('-11ell','-7ell').replace('-11 = q²+15q+3','-7 = q²+15q+7').replace('(q²+15q+3)/2^q','(q²+15q+7)/2^q').replace('q²+13q-13','q²+13q-9').replace('37/4','41/4').replace('[(3/2)C0+2]','[(3/2)C0+1]').replace('3C0/2+2','3C0/2+1').replace('-11;','-7;')
p.write_text(s,encoding='utf-8')
