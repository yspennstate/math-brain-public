"use strict";
/*
Independent exact certificate for agent 102's audit of agents/060.md.
Only built-in JavaScript BigInt arithmetic is used. There is no filesystem,
network, numerical optimization, or external-library dependency.
Run with: node 102_parental_leakage_exact.js
In code mode this source was evaluated directly; its last expression returns
the same JSON-serializable object that Node prints.
*/
const audit102Result = (() => {
  function check(ok, label) { if (!ok) throw new Error(label); }
  function gcd(a, b) {
    a = a < 0n ? -a : a; b = b < 0n ? -b : b;
    while (b !== 0n) { const r = a % b; a = b; b = r; }
    return a;
  }
  class Rat {
    constructor(n = 0n, d = 1n) {
      if (n instanceof Rat) { this.n = n.n; this.d = n.d; return; }
      n = BigInt(n); d = BigInt(d);
      check(d !== 0n, "zero denominator");
      if (d < 0n) { n = -n; d = -d; }
      const g = gcd(n, d); this.n = n / g; this.d = d / g;
    }
    add(b) { b = new Rat(b); return new Rat(this.n*b.d+b.n*this.d, this.d*b.d); }
    neg() { return new Rat(-this.n, this.d); }
    sub(b) { return this.add(new Rat(b).neg()); }
    mul(b) { b = new Rat(b); return new Rat(this.n*b.n, this.d*b.d); }
    div(b) { b = new Rat(b); return new Rat(this.n*b.d, this.d*b.n); }
    cmp(b) {
      b = new Rat(b); const t = this.n*b.d - b.n*this.d;
      return t < 0n ? -1 : t > 0n ? 1 : 0;
    }
    eq(b) { return this.cmp(b) === 0; }
    pow(k) {
      check(Number.isSafeInteger(k), "nonintegral exponent");
      if (k < 0) return new Rat(this.d, this.n).pow(-k);
      return new Rat(this.n ** BigInt(k), this.d ** BigInt(k));
    }
    toString() { return this.d === 1n ? String(this.n) : String(this.n)+"/"+String(this.d); }
  }
  const r = (n, d = 1) => new Rat(n, d);
  const sum = a => a.reduce((s, x) => s.add(x), r(0));
  const min = (a, b) => a.cmp(b) <= 0 ? a : b;

  class Laurent {
    constructor(entries = []) {
      this.c = new Map();
      for (const [k, v0] of entries) {
        check(Number.isSafeInteger(k), "bad Laurent exponent");
        const v = new Rat(v0).add(this.c.get(k) || r(0));
        if (v.eq(0)) this.c.delete(k); else this.c.set(k, v);
      }
    }
    static constant(v) { return new Laurent([[0, new Rat(v)]]); }
    static mono(k, v = 1) { return new Laurent([[k, new Rat(v)]]); }
    static of(v) { return v instanceof Laurent ? v : Laurent.constant(v); }
    add(other) { other = Laurent.of(other); return new Laurent([...this.c, ...other.c]); }
    neg() { return new Laurent([...this.c].map(([k,v]) => [k,v.neg()])); }
    sub(other) { return this.add(Laurent.of(other).neg()); }
    mul(other) {
      other = Laurent.of(other); const entries = [];
      for (const [i,a] of this.c) for (const [j,b] of other.c) entries.push([i+j,a.mul(b)]);
      return new Laurent(entries);
    }
    divScalar(other) { return this.mul(r(1).div(other)); }
    eq(other) { return this.sub(other).c.size === 0; }
    at(x) { return sum([...this.c].map(([k,v]) => v.mul(x.pow(k)))); }
    serialize() {
      return Object.fromEntries([...this.c].sort((a,b)=>a[0]-b[0]).map(([k,v])=>[String(k),String(v)]));
    }
  }
  const lsum = a => a.reduce((s,x)=>s.add(x), Laurent.constant(0));

  const d=r(7,50), cap=r(17,40), eps=r(1).sub(d.mul(2)).div(r(3).sub(d.mul(2)));
  const rem=r(1).sub(cap.mul(2));
  const capSlack=cap.sub(d.add(r(1).sub(d).mul(r(1).sub(cap).pow(2))));
  check(eps.eq(r(9,34)), "sign weight");
  check(rem.eq(r(3,20)), "cap residual");
  check(capSlack.eq(r(53,80000)), "strict coordinate cap");
  check(cap.mul(2).cmp(1)<0 && cap.mul(3).cmp(1)>0, "vertex regime");
  check(rem.cmp(0)>0 && rem.cmp(cap)<0, "residual range");

  // Enumerate by active box constraints, independently of a permutation list.
  const vertexMap = new Map();
  for (let free=0; free<4; free++) {
    const fixed=[0,1,2,3].filter(i=>i!==free);
    for (let mask=0; mask<8; mask++) {
      const v=[r(0),r(0),r(0),r(0)];
      fixed.forEach((i,k)=>{v[i]=(mask & (1<<k)) ? cap : r(0);});
      v[free]=r(1).sub(sum(v));
      if (v[free].cmp(0)>=0 && v[free].cmp(cap)<=0) vertexMap.set(v.map(String).join(","),v);
    }
  }
  const vertices=[...vertexMap.values()];
  check(vertices.length===12,"number of cap vertices");
  for (const v of vertices) {
    const sorted=[...v].sort((a,b)=>a.cmp(b));
    check(sorted.every((x,i)=>x.eq([r(0),rem,cap,cap][i])),"cap vertex shape");
  }
  const records=[];
  for (const v of vertices) for (const a of [eps,r(1).sub(eps)]) for (const b of [eps,r(1).sub(eps)]) {
    const aw=[a,r(1).sub(a)], bw=[b,r(1).sub(b)];
    let value=r(0);
    for(let i=0;i<2;i++) for(let j=0;j<2;j++) value=value.add(aw[i].mul(bw[j]).mul(min(v[i],v[j+2])));
    check(value.cmp(eps.mul(rem))>=0,"weighted minimum at a reduced corner");
    records.push({m:v.map(String),a:String(a),b:String(b),value:String(value)});
  }
  let weightedMin=r(1);
  for (const t of records) {
    const [n,den="1"]=t.value.split("/");
    weightedMin=min(weightedMin,r(n,den));
  }
  check(records.length===48,"number of reduced corners");
  check(weightedMin.eq(r(27,680)), "sharp minimum on closed capped simplex");
  const equalityCorners=records.filter(t=>t.value===String(weightedMin)).length;
  check(equalityCorners===8,"weighted-minimum equality corner count");
  const oldTransfer=d.add(r(1).sub(d).mul(cap));
  const correction=d.mul(weightedMin);
  const transfer=oldTransfer.sub(correction);
  check(oldTransfer.eq(r(1011,2000)),"unweighted transfer");
  check(transfer.eq(r(8499,17000)),"weighted transfer");
  check(r(1,2).sub(transfer).eq(r(1,17000)),"strict transfer gap");
  check(transfer.mul(2).eq(r(8499,8500)),"fixed-point difference factor");
  check(r(3,4).sub(r(43,50).pow(2)).eq(r(13,1250)),"strict enlargement over old threshold");

  const eta=Laurent.mono(1), inverse=Laurent.mono(-1), one=Laurent.constant(1);
  const rows=[];
  for(let i=0;i<4;i++) for(let j=i;j<4;j++) {
    const out=Array.from({length:4},()=>Laurent.constant(0));
    if(j<3 && i===j) {
      for(let k=0;k<3;k++) if(k!==i) out[k]=Laurent.constant(r(1,2));
    } else if(j<3) {
      for(let k=0;k<3;k++) if(k!==i && k!==j) out[k]=one;
    } else if(i<3) {
      out[3]=eta;
      for(let k=0;k<3;k++) if(k!==i) out[k]=one.sub(eta).divScalar(2);
    } else {
      out[3]=eta;
      for(let k=0;k<3;k++) out[k]=one.sub(eta).divScalar(3);
    }
    check(lsum(out).eq(1),"row stochasticity");
    for(const coefficient of out) {
      check([...coefficient.c.keys()].every(k=>k===0 || k===1),"affine coefficient");
      check(coefficient.at(r(0)).cmp(0)>=0 && coefficient.at(r(1)).cmp(0)>=0,"coefficient nonnegativity on [0,1]");
    }
    // Set removes the repeated parent: row 44 contributes eta, not 2 eta.
    const leakage=lsum([...new Set([i,j])].map(k=>out[k]));
    check(leakage.eq(j===3 ? eta : 0),"total parental leakage");
    check(out[3].eq(j===3 ? eta : 0),"fourth-coordinate polynomial coefficient");
    rows.push({i,j,out,leakage});
  }
  check(rows.length===10,"all unordered parent rows");

  function apply(point) {
    const result=Array.from({length:4},()=>Laurent.constant(0));
    for(const row of rows) {
      const factor=point[row.i].mul(point[row.j]).mul(row.i===row.j ? 1 : 2);
      for(let k=0;k<4;k++) result[k]=result[k].add(row.out[k].mul(factor));
    }
    return result;
  }
  const boundary=[Laurent.constant(r(1,3)),Laurent.constant(r(1,3)),Laurent.constant(r(1,3)),Laurent.constant(0)];
  const interior=Array.from({length:3},()=>inverse.sub(1).divScalar(3));
  interior.push(Laurent.constant(2).sub(inverse));
  const residuals={};
  for(const [label,point] of [["boundary",boundary],["interior",interior]]) {
    check(lsum(point).eq(1),"symbolic simplex normalization");
    const output=apply(point);
    const residual=output.map((p,k)=>p.sub(point[k]));
    check(residual.every(p=>p.eq(0)),"symbolic full fixed point "+label);
    const t=point[3];
    check(eta.mul(t).mul(Laurent.constant(2).sub(t)).sub(t).eq(0),"fourth-coordinate scalar fixed point "+label);
    residuals[label]=residual.map(p=>p.serialize());
  }
  const exampleEta=r(3,5), example=interior.map(p=>p.at(exampleEta));
  check(example.every((x,i)=>x.eq(i===3 ? r(1,3) : r(2,9))),"rational counterexample");
  check(interior.every(p=>p.at(exampleEta).cmp(0)>0),"example interior positivity");
  // The report proves positivity for the entire open parameter interval.
  check(interior.every((p,i)=>p.at(r(1,2)).eq(i===3 ? 0 : r(1,3))),"lower endpoint collapse");
  check(interior.every((p,i)=>p.at(r(1)).eq(i===3 ? 1 : 0)),"upper endpoint limit");

  return {
    all_exact_checks_passed:true,
    arithmetic:"JavaScript built-in BigInt rational and Laurent arithmetic; no floating-point certification",
    provenance:"Independent certificate by agent 102 for agents/060.md at commit 4c708781adf206a4d28b7e3027365ba2b735c12d",
    constants:{
      d:String(d),Q:String(cap),epsilon:String(eps),R:String(rem),cap_slack:String(capSlack),
      weighted_minimum:String(weightedMin),cap_vertices:vertices.length,reduced_corner_checks:records.length,
      weighted_minimum_equality_corners:equalityCorners,unweighted_transfer:String(oldTransfer),
      retained_correction:String(correction),weighted_transfer:String(transfer),
      strict_gap_below_one_half:String(r(1,2).sub(transfer)),difference_factor:String(transfer.mul(2)),
      old_threshold_square_gap:String(r(3,4).sub(r(43,50).pow(2)))
    },
    sharpness:{
      parameter_domain:"1/2 < eta < 1",exact_total_parental_leakage:"eta",unordered_rows:rows.length,
      coefficient_nonnegativity:"All coefficients are affine and nonnegative at eta=0 and eta=1.",
      fourth_coordinate_on_simplex:"eta*x4*(2-x4)",
      boundary:boundary.map(p=>p.serialize()),interior:interior.map(p=>p.serialize()),
      full_fixed_point_residuals:residuals,example_eta:String(exampleEta),example_point:example.map(String),
      tensor_is_strictly_positive:false,interior_fixed_point_is_strictly_positive:true,
      row_data:rows.map(({i,j,out,leakage})=>({parents:[i+1,j+1],coefficients:out.map(p=>p.serialize()),leakage:leakage.serialize()}))
    },
    reduced_corner_records:records,
    scope:"Algebraic checks support the independent analytic proof; no Python execution, arbitrary-difference contraction, convergence extension, or optimal threshold is asserted."
  };
})();
if (typeof console !== "undefined") console.log(JSON.stringify(audit102Result,null,2));
audit102Result;
