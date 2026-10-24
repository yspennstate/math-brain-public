# PROB20-21 executed n=6 probe variants — exact reconstruction

Base source: `2026-09-16_14-43-07_UTC__n6_probe.cpp`.

The two additional diagnostic checkers executed in this run were mechanically generated from that base by replacing the final `return 0;` after the invariant printout with the exact blocks below. Their executed outputs are archived in `2026-09-16_14-43-07_UTC__n6_diagnostics_and_timeout.txt`. Local source SHA-256 values are recorded there and in the coverage manifest.

## Variant A — high-noise diagnostic

Local source SHA-256:
`bcadfc810a1d17f5fa0dc6295a59a45d81f332983feb348cf6c10ce175ab215e`

Exact inserted block:

```cpp
for(auto rr: {Q(1,64),Q(1,96),Q(1,128),Q(1,80)}){
    bool ok=true; mpq_class minmargin; bool hm=false; uint64_t mm=0;
    for(uint64_t m:nontriv){
        auto c=walsh_pm(m); mpq_class mu=abs(c[0]),var=1-mu*mu,W1=0;
        for(int i=0;i<NV;i++) W1+=c[1ull<<i]*c[1ull<<i];
        mpq_class d=var-W1;
        mpq_class L=(1-rr*rr)*d-63*rr*rr*var;
        mpq_class sq=L*L-4*mu*mu*rr*rr*63*var;
        if(L<=0 || sq<=0) ok=false;
        if(!hm || sq<minmargin){hm=true;minmargin=sq;mm=m;}
    }
    std::cout<<"rho="<<rr<<" high_exact_condition="<<(ok?"PASS":"FAIL")
             <<" min_sq_margin="<<minmargin<<" mask="<<mm<<"\n";
}
return 0;
```

## Variant B — reciprocal-threshold probe

Local source SHA-256:
`c4f59709427cdcf213e15e3574c422d2bae5f7e9736615a0fde4e46c2c902887`

Exact inserted block:

```cpp
for(int q=65;q<=96;q++){
    mpq_class rr=Q(1,q);
    bool ok=true; mpq_class minmargin; bool hm=false; uint64_t mm=0;
    for(uint64_t m:nontriv){
        auto c=walsh_pm(m); mpq_class mu=abs(c[0]),var=1-mu*mu,W1=0;
        for(int i=0;i<NV;i++) W1+=c[1ull<<i]*c[1ull<<i];
        mpq_class d=var-W1;
        mpq_class L=(1-rr*rr)*d-63*rr*rr*var;
        mpq_class sq=L*L-4*mu*mu*rr*rr*63*var;
        if(L<=0 || sq<=0) ok=false;
        if(!hm||sq<minmargin){hm=true;minmargin=sq;mm=m;}
    }
    if(ok){
        std::cout<<"first_pass_q="<<q<<" margin="<<minmargin<<" mask="<<mm<<"\n";
        break;
    }
}
return 0;
```

These variants are exploratory diagnostics only; neither receives finite-coverage credit. The full n=6 interval attempt timed out and additionally contains a later-detected low-noise substitution defect documented in the diagnostics file.
