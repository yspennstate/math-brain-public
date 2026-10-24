"use strict";
// Original open-domain diagnostics; not evaluation-bank material. Node 18+.
function entropy(p) { let h=0; for(const x of p) if(x>0) h-=x*Math.log2(x); return h; }
function spectrum(f,n,p) {
  const size=1<<n, q=Array(size).fill(0);
  for(let s=0;s<size;s++) {
    let a=0;
    for(let x=0;x<size;x++) {
      let w=1,chi=1;
      for(let i=0;i<n;i++) {
        const z=(x>>i)&1;
        w*=z?p[i]:1-p[i];
        if((s>>i)&1) chi*=(z-p[i])/Math.sqrt(p[i]*(1-p[i]));
      }
      a+=w*f[x]*chi;
    }
    q[s]=a*a;
  }
  return q;
}
function restricted(f,n,i,z) {
  const g=[];
  for(let y=0;y<(1<<(n-1));y++) {
    const x=(y&((1<<i)-1))|(z<<i)|((y>>i)<<(i+1));
    g.push(f[x]);
  }
  return g;
}
function main() {
  const L=37/32-45/(128*Math.LN2);
  const threshold=2-7/8*Math.log2(3);
  const epsilon=L-threshold;
  let minimum_scalar=Infinity, min_scalar_vs_L=Infinity;
  for(let j=0;j<=20000;j++) {
    const theta=Math.PI*j/20000;
    const c=Math.cos(2*theta),d=Math.cos(2*theta-Math.PI/3);
    const h=entropy([(1+c)/2,(1-c)/2])+entropy([(1+d)/2,(1-d)/2]);
    minimum_scalar=Math.min(minimum_scalar,h);
    min_scalar_vs_L=Math.min(min_scalar_vs_L,h-L);
  }
  let cases=0,min_slack=Infinity,max_parseval_error=0,violations=0;
  const grid=[1/8,1/4,1/2,3/4,7/8];
  for(let code=0;code<256;code++) {
    const f=Array.from({length:8},(_,x)=>((code>>x)&1)?1:-1);
    for(let i=0;i<3;i++) for(const pi of [1/4,3/4])
    for(const pj of grid) for(const pk of grid) {
      const p=[0,0,0],other=[0,1,2].filter(j=>j!==i);
      p[i]=pi;p[other[0]]=pj;p[other[1]]=pk;
      const parent=spectrum(f,3,p),residual=Array(4).fill(0);
      for(let s=0;s<8;s++) {
        const t=(s&((1<<i)-1))|((s>>(i+1))<<i);
        residual[t]+=parent[s];
      }
      const cp=[p[other[0]],p[other[1]]];
      const c0=spectrum(restricted(f,3,i,0),2,cp);
      const c1=spectrum(restricted(f,3,i,1),2,cp);
      max_parseval_error=Math.max(max_parseval_error,
          Math.abs(parent.reduce((a,b)=>a+b,0)-1),
          Math.abs(c0.reduce((a,b)=>a+b,0)-1),
          Math.abs(c1.reduce((a,b)=>a+b,0)-1));
      const M=entropy(parent)-entropy(residual);
      const J=entropy(residual)-(1-pi)*entropy(c0)-pi*entropy(c1);
      const tax=0.5*(entropy([pi,1-pi])+Math.log2(Math.max(pi,1-pi)));
      const slack=tax-(J-M);
      min_slack=Math.min(min_slack,slack);
      if(slack<epsilon-1e-10)violations++;
      cases++;
    }
  }
  const log_certificate={lower_ln3:1+1/12+1/80,upper_ln2:7/10,
    rational_margin:112*(1+1/12+1/80)-108*(7/10)-45};
  const results={status:violations===0 && log_certificate.rational_margin>0 &&
    min_scalar_vs_L>-1e-10 && max_parseval_error<1e-12?"PASS":"FAIL",
    precision:"IEEE754 double; diagnostics only, analytic proof separate",
    scalar_angle_cases:20001,scalar_min_entropy_bits:minimum_scalar,
    scalar_min_minus_analytic_lower: min_scalar_vs_L,
    analytic_scalar_bound_L_bits:L,half_tax_threshold_T_bits:threshold,
    analytic_slack_epsilon_bits:epsilon,
    n3_boolean_truth_tables:256,n3_full_parameter_cases:cases,
    n3_min_half_tax_slack_bits:min_slack,n3_violations:violations,
    max_parseval_normalization_error:max_parseval_error,
    rigorous_log_bound_certificate:log_certificate,
    note:"n=3 enumeration and scalar grid are floating diagnostics, not universal proofs or outward-certified arithmetic."};
  if(results.status!=="PASS")throw Error(JSON.stringify(results));
  return results;
}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(main(),null,2));
