"use strict";
/* Reproduce agent 094's purposeful exact checks. No dependencies except the sibling module. */
function runChecks94(api) {
  const R=api.rat, z=R(0), one=R(1), pairs=[];
  for(let i=0;i<4;i++) for(let j=i;j<4;j++) pairs.push([i,j]);
  const equal=(a,b,message)=>{if(R(a).cmp(R(b))!==0) throw Error(message);};
  const assert=(v,message)=>{if(!v) throw Error(message);};
  const checks=[];
  // Independent ordered-parent polynomial expansion; does not call api.B,
  // api.V, api.bernsteinResidual, or api.cellData.
  function orderedResidualPolynomial(p,q,x,y) {
    const pc=[p,p.map((row,r)=>row.map((v,k)=>q[r][k].sub(v)))];
    const xc=[x,x.map((v,k)=>y[k].sub(v))];
    const out=Array.from({length:4},()=>[z,z,z,z]);
    for(let i=0;i<4;i++) for(let j=0;j<4;j++) {
      const r=pairs.findIndex(([a,b])=>a===Math.min(i,j)&&b===Math.max(i,j));
      for(let k=0;k<4;k++) for(let a=0;a<2;a++) for(let b=0;b<2;b++) for(let c=0;c<2;c++)
        out[a+b+c][k]=out[a+b+c][k].add(pc[a][r][k].mul(xc[b][i]).mul(xc[c][j]));
    }
    for(let k=0;k<4;k++) {out[0][k]=out[0][k].sub(x[k]); out[1][k]=out[1][k].sub(y[k].sub(x[k]));}
    return out;
  }
  function independentCheck(cert) {
    const path=api.readPath(cert.path), N=BigInt(cert.algorithm.grid_denominator);
    for(const a of cert.anchors) {
      const p=api.opAt(path,R(a.t)), x=a.x.map(R), f=orderedResidualPolynomial(p,p,x,x);
      const residual=f[0].reduce((v,w)=>v.add(w.abs()),z);
      equal(a.residual,residual,"Independent anchor residual");
      equal(a.error,residual.mul(5),"Independent anchor error");
      assert(BigInt(a.steps)<=BigInt(a.proved_step_limit),"Anchor horizon");
      for(let k=0;k<4;k++) equal(x[k],new api.R(BigInt(a.grid_counts[k]),N),"Grid count binding");
    }
    for(const c of cert.cells) {
      const a=cert.anchors[c.left], b=cert.anchors[c.right], p=api.opAt(path,R(a.t)), q=api.opAt(path,R(b.t));
      const f=orderedResidualPolynomial(p,q,a.x.map(R),b.x.map(R)), bs=c.bernstein_coefficients.map(row=>row.map(R));
      for(let k=0;k<4;k++) {
        const back=[bs[0][k],bs[1][k].sub(bs[0][k]).mul(3),
          bs[0][k].sub(bs[1][k].mul(2)).add(bs[2][k]).mul(3),
          bs[0][k].neg().add(bs[1][k].mul(3)).sub(bs[2][k].mul(3)).add(bs[3][k])];
        for(let d=0;d<4;d++) equal(f[d][k],back[d],"Independent cubic/Bernstein coefficient identity");
      }
    }
  }
  const activation=api.generate(api.demoInput()), invariant=api.generate(api.invariantInput());
  const demo=api.demoInput(), permutation=[0,3,2,1], permRows=pairs.map(()=>["0","0","0","0"]);
  for(let r=0;r<10;r++) {
    const [i,j]=pairs[r], a=Math.min(permutation[i],permutation[j]), b=Math.max(permutation[i],permutation[j]);
    const s=pairs.findIndex(([u,v])=>u===a&&v===b);
    for(let k=0;k<4;k++) permRows[s][permutation[k]]=demo.operators[0].rows[r][k];
  }
  const piecewise=api.generate({knots:["-2","1/3","7/4"],
    operators:[demo.operators[0],demo.operators[1],{rows:permRows}],epsilon:"1/100"});
  const cases={activation,invariant,piecewise}, results={};
  for(const [name,cert] of Object.entries(cases)) {
    results[name]=api.verify(cert); independentCheck(cert);
    checks.push(name+": exact verification, grid binding, ordered-parent residual, coefficientwise Bernstein identity");
  }
  assert(invariant.cells.length===1&&invariant.cells[0].radius==="0","Invariant segment exact tube");
  for(const a of invariant.anchors) {
    ["1/3","1/3","1/3","0"].forEach((v,k)=>equal(a.x[k],v,"Exact invariant-face fixedpoint"));
  }
  checks.push("Invariant face: one cell, zero radius, exact missing coordinate");
  let lower=R("2/5"),upper=z;
  for(const c of activation.cells) {
    if(R(c.coordinate_bounds[0][0]).cmp(lower)<0) lower=R(c.coordinate_bounds[0][0]);
    if(R(c.coordinate_bounds[0][1]).cmp(upper)>0) upper=R(c.coordinate_bounds[0][1]);
  }
  assert(lower.cmp(R("8/25"))>0&&upper.cmp(R("17/50"))<0,"Global activation interval");
  const p0=api.readOperator(demo.operators[0]),p1=api.readOperator(demo.operators[1]);
  for(let r=0;r<10;r++) {
    equal(p0[r][3],0,"Missing output initially zero");
    equal(p1[r][3],r===0?1:0,"Only incoming row is 00");
  }
  results.activation.missing_mass_slope_interval=["64/625","289/2500"];
  checks.push("Entire activation segment: (64/625)t <= p_3(t) <= (289/2500)t");
  assert(piecewise.anchors.some(a=>a.t==="1/3"),"Original knot must be an anchor");
  assert(JSON.stringify(piecewise.anchors[0].zero_coordinates)==="[3]","First boundary support");
  assert(JSON.stringify(piecewise.anchors[piecewise.anchors.length-1].zero_coordinates)==="[1]","Last boundary support");
  assert(piecewise.cells.every(c=>c.interior_support.length===4),"Both open segments are interior");
  checks.push("Piecewise path: nonuniform rational knots, two different endpoint boundary faces");
  const tamper=[
    ["residual",c=>{c.anchors[1].residual="0";}],
    ["radius",c=>{c.cells[0].radius="0";}],
    ["Bernstein coefficient",c=>{c.cells[1].bernstein_coefficients[1][0]="0";}],
    ["boundary support",c=>{c.cells[0].interior_support=[0,1,2];}],
    ["coverage endpoint",c=>{c.anchors[c.anchors.length-1].t="9/10";}],
    ["adjacency",c=>{c.cells[1].left=0;}],
    ["parent exclusion",c=>{c.path.operators[0].rows[0]=["1","0","0","0"];}]
  ];
  for(const [name,mutate] of tamper) {
    const cert=JSON.parse(JSON.stringify(activation)); mutate(cert); let rejected=false;
    try {api.verify(cert);} catch(e) {rejected=true;}
    assert(rejected,"Tampered certificate accepted: "+name); checks.push("Rejected tamper: "+name);
  }
  for(const bad of [0,-1,0.01,true,"1e-5"]) {
    const raw=api.demoInput();raw.epsilon=bad;let rejected=false;
    try{api.generate(raw);}catch(e){rejected=true;}
    assert(rejected,"Invalid tolerance accepted");checks.push("Rejected invalid tolerance: "+String(bad));
  }
  return {record:{all_checks_passed:true,checks,results,
    execution_environment:"JavaScript V8 with BigInt; no filesystem or external packages used in the recorded run"},
    certificates:cases};
}
if(typeof module!=="undefined") module.exports=runChecks94;
if(typeof require!=="undefined" && require.main===module) {
  const api=require("./094_qso_continuation.cjs");
  process.stdout.write(JSON.stringify(runChecks94(api).record,null,2)+"\n");
}
