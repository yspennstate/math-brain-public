"use strict";

/*
Agent 094. Certified continuation for four-type strictly non-Volterra QSOs.
No external packages. All mathematical comparisons use BigInt rational arithmetic.
Run:
  node 094_qso_continuation.cjs --demo > certificate.json
  node 094_qso_continuation.cjs --verify < certificate.json
  node 094_qso_continuation.cjs < input.json > certificate.json
Input: {knots:[rational,...], operators:[{rows:[four-entry row,...]},...],
        epsilon:positive_rational}.
Rows are ordered by i=0..3, j=i..3; distinct parent pairs have multiplicity 2.
This certifies a fixedpoint path, not convergence of raw QSO iterates.
*/
function qsoContinuation94() {
  function fail(s) { throw new Error(s); }
  function abs(n) { return n < 0n ? -n : n; }
  function gcd(a,b) { a=abs(a); b=abs(b); while(b) { const r=a%b; a=b; b=r; } return a; }
  class R {
    constructor(n,d=1n) {
      if(typeof n!=="bigint" || typeof d!=="bigint" || d===0n) fail("Invalid rational");
      if(d<0n) { n=-n; d=-d; } const g=gcd(n,d); this.n=n/g; this.d=d/g;
    }
    static from(x) {
      if(x instanceof R) return x;
      if(typeof x==="bigint") return new R(x);
      if(typeof x==="number" && Number.isSafeInteger(x)) return new R(BigInt(x));
      if(typeof x!=="string" || !/^[+-]?[0-9]+(?:\/[1-9][0-9]*)?$/.test(x)) fail("Use explicit integer or numerator/denominator rationals");
      const a=x.split("/"); return new R(BigInt(a[0]),a.length===2?BigInt(a[1]):1n);
    }
    add(x) { x=R.from(x); return new R(this.n*x.d+x.n*this.d,this.d*x.d); }
    sub(x) { x=R.from(x); return new R(this.n*x.d-x.n*this.d,this.d*x.d); }
    mul(x) { x=R.from(x); return new R(this.n*x.n,this.d*x.d); }
    div(x) { x=R.from(x); if(x.n===0n) fail("Division by zero"); return new R(this.n*x.d,this.d*x.n); }
    neg() { return new R(-this.n,this.d); }
    abs() { return new R(abs(this.n),this.d); }
    cmp(x) { x=R.from(x); const z=this.n*x.d-x.n*this.d; return z<0n?-1:z>0n?1:0; }
    toString() { return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d); }
  }
  const rat=x=>R.from(x), Z=rat(0), ONE=rat(1), TWO=rat(2), CAP=rat("2/5");
  const K=rat("7/2"), H=rat(162);
  const pairs=[]; for(let i=0;i<4;i++) for(let j=i;j<4;j++) pairs.push([i,j]);
  const sum=v=>v.reduce((a,b)=>a.add(b),Z);
  const norm=v=>sum(v.map(x=>x.abs()));
  const add=(u,v)=>u.map((x,i)=>x.add(v[i]));
  const sub=(u,v)=>u.map((x,i)=>x.sub(v[i]));
  const scale=(u,a)=>u.map(x=>x.mul(a));
  const rmin=(a,b)=>a.cmp(b)<=0?a:b, rmax=(a,b)=>a.cmp(b)>=0?a:b;
  const eq=(a,b)=>a.cmp(b)===0;
  const strings=v=>v.map(x=>x.toString());
  const ceil=x=>{ x=rat(x); if(x.n<0n) fail("ceil requires nonnegative"); return (x.n+x.d-1n)/x.d; };
  function readOperator(raw) {
    if(!raw || !Array.isArray(raw.rows) || raw.rows.length!==10) fail("Operator needs ten unordered rows");
    return raw.rows.map((row,r)=>{
      if(!Array.isArray(row)||row.length!==4) fail("A coefficient row needs four entries");
      const a=row.map(rat), [i,j]=pairs[r];
      if(a.some(x=>x.cmp(Z)<0)||!eq(sum(a),ONE)||!eq(a[i],Z)||!eq(a[j],Z)) fail("Invalid stochastic parent-excluding row");
      return a;
    });
  }
  function readPath(raw) {
    if(!raw || !Array.isArray(raw.knots)||!Array.isArray(raw.operators)||raw.knots.length<2||raw.knots.length!==raw.operators.length) fail("Invalid path");
    const knots=raw.knots.map(rat), ops=raw.operators.map(readOperator);
    for(let i=1;i<knots.length;i++) if(knots[i-1].cmp(knots[i])>=0) fail("Knots must increase");
    return {knots,ops};
  }
  function writePath(path) { return {knots:strings(path.knots),operators:path.ops.map(p=>({rows:p.map(strings)}))}; }
  function blendOp(p,q,s) { return p.map((row,i)=>row.map((x,k)=>x.add(q[i][k].sub(x).mul(s)))); }
  const diffOp=(p,q)=>p.map((row,i)=>row.map((x,k)=>x.sub(q[i][k])));
  function rowDistance(p,q) { return p.reduce((a,row,i)=>rmax(a,norm(sub(row,q[i]))),Z); }
  function opAt(path,t) {
    if(t.cmp(path.knots[0])<0||t.cmp(path.knots[path.knots.length-1])>0) fail("Parameter outside path");
    let lo=0, hi=path.knots.length-1;
    while(hi-lo>1) { const m=Math.floor((lo+hi)/2); if(t.cmp(path.knots[m])<0) hi=m; else lo=m; }
    if(lo===path.knots.length-1) return path.ops[lo];
    const s=t.sub(path.knots[lo]).div(path.knots[lo+1].sub(path.knots[lo]));
    return blendOp(path.ops[lo],path.ops[lo+1],s);
  }
  function B(p,u,v) {
    const out=[Z,Z,Z,Z];
    for(let r=0;r<10;r++) {
      const [i,j]=pairs[r];
      const w=i===j?u[i].mul(v[i]):u[i].mul(v[j]).add(u[j].mul(v[i]));
      for(let k=0;k<4;k++) out[k]=out[k].add(p[r][k].mul(w));
    } return out;
  }
  const V=(p,x)=>B(p,x,x);
  function zeroOutputs(p) { return [0,1,2,3].filter(k=>p.every(row=>eq(row[k],Z))); }
  function checkState(x) {
    if(!Array.isArray(x)||x.length!==4) fail("Candidate needs four entries");
    const y=x.map(rat);
    if(!eq(sum(y),ONE)||y.some(z=>z.cmp(Z)<0||z.cmp(CAP)>0)) fail("Candidate outside capped simplex");
    return y;
  }
  function integerize(p) {
    let D=1n;
    for(const row of p) for(const x of row) D=D/gcd(D,x.d)*x.d;
    return {D,C:p.map(row=>row.map(x=>x.n*(D/x.d)))};
  }
  function startCounts(N,p) {
    const missing=zeroOutputs(p), allowed=[0,1,2,3].filter(k=>!missing.includes(k));
    const m=BigInt(allowed.length), counts=[0n,0n,0n,0n], q=N/m, r=N%m;
    for(let j=0;j<allowed.length;j++) counts[allowed[j]]=q+(BigInt(j)<r?1n:0n);
    return counts;
  }
  function evalGrid(C,counts) {
    const S=[0n,0n,0n,0n];
    for(let r=0;r<10;r++) {
      const [i,j]=pairs[r], w=counts[i]*counts[j]*(i===j?1n:2n);
      for(let k=0;k<4;k++) S[k]+=C[r][k]*w;
    } return S;
  }
  function roundStep(D,N,counts,S) {
    const den=5n*D*N, out=[], rem=[];
    for(let k=0;k<4;k++) {
      const num=3n*D*N*counts[k]+2n*S[k];
      out.push(num/den); rem.push(num%den);
    }
    let remaining=N-out.reduce((a,b)=>a+b,0n);
    const order=[0,1,2,3].sort((i,j)=>rem[i]>rem[j]?-1:rem[i]<rem[j]?1:i-j);
    for(let j=0;BigInt(j)<remaining;j++) out[order[j]]+=1n;
    if(out.some(x=>x<0n||5n*x>2n*N)||out.reduce((a,b)=>a+b,0n)!==N) fail("Rounding invariant failed");
    return out;
  }
  function solveAnchor(p,t,tau,N,warm) {
    let counts, initialBound=TWO;
    const missing=zeroOutputs(p);
    if(warm && !missing.some(k=>warm.counts[k]!==0n)) {
      counts=warm.counts.slice();
      initialBound=rmin(TWO,warm.error.add(K.mul(rowDistance(p,warm.p))));
    } else counts=startCounts(N,p);
    const {D,C}=integerize(p), den=D*N*N;
    let k=0n, pow=1n, target=initialBound.mul(30).div(tau);
    while(rat(pow).cmp(target)<0) { pow*=2n; k++; }
    const limit=9n*k;
    for(let step=0n;step<=limit;step++) {
      const S=evalGrid(C,counts);
      const rnum=S.reduce((a,v,j)=>a+abs(v-D*N*counts[j]),0n);
      if(5n*rnum*tau.d<=tau.n*den) {
        const residual=new R(rnum,den), error=residual.mul(5), x=counts.map(n=>new R(n,N));
        return {p,t,x,residual,error,counts,N,steps:step,limit,initialBound,missing};
      }
      if(step===limit) fail("Proved exact anchor horizon exhausted");
      counts=roundStep(D,N,counts,S);
    }
    fail("Unreachable");
  }
  function bernsteinResidual(p,q,x,y) {
    const dp=diffOp(q,p), d=sub(y,x);
    const f0=sub(V(p,x),x);
    const f1=sub(add(scale(B(p,x,d),2),B(dp,x,x)),d);
    const f2=add(B(p,d,d),scale(B(dp,x,d),2));
    const f3=B(dp,d,d);
    return [
      f0,
      add(f0,scale(f1,rat("1/3"))),
      add(add(f0,scale(f1,rat("2/3"))),scale(f2,rat("1/3"))),
      add(add(add(f0,f1),f2),f3)
    ];
  }
  function cellData(left,right) {
    const delta=rowDistance(left.p,right.p), anchor=rmax(left.error,right.error);
    const lipschitz=anchor.add(K.mul(delta).div(2));
    const curvature=anchor.add(H.mul(delta).mul(delta).div(8));
    const bernstein=bernsteinResidual(left.p,right.p,left.x,right.x);
    const bernsteinNorms=bernstein.map(norm);
    const residual=bernsteinNorms.reduce(rmax,Z).mul(5);
    const terms={diameter:TWO,lipschitz,curvature,bernstein:residual};
    let method="diameter", radius=TWO;
    for(const name of ["lipschitz","curvature","bernstein"]) if(terms[name].cmp(radius)<0) { radius=terms[name]; method=name; }
    const missing=zeroOutputs(blendOp(left.p,right.p,rat("1/2")));
    const bounds=[0,1,2,3].map(i=>missing.includes(i)?[Z,Z]:[
      rmax(Z,rmin(left.x[i],right.x[i]).sub(radius.div(2))),
      rmin(CAP,rmax(left.x[i],right.x[i]).add(radius.div(2)))
    ]);
    return {delta,terms,radius,method,bernstein,bernsteinNorms,missing,bounds};
  }
  function depthPlan(eta,epsilon) {
    let depth=0n, scale=1n;
    while(true) {
      const delta=eta.div(scale);
      if(K.mul(delta).cmp(epsilon)<=0 || H.mul(delta).mul(delta).cmp(epsilon.mul(4))<=0) return depth;
      depth++; scale*=2n;
    }
  }
  function anchorRecord(a) {
    return {t:a.t.toString(),x:strings(a.x),residual:a.residual.toString(),error:a.error.toString(),
      zero_coordinates:a.missing,grid_counts:a.counts.map(String),steps:String(a.steps),proved_step_limit:String(a.limit),
      initial_error_bound:a.initialBound.toString()};
  }
  function cellRecord(data,segment,index,depth) {
    const terms={}; for(const [k,v] of Object.entries(data.terms)) terms[k]=v.toString();
    return {left:index,right:index+1,segment,depth:String(depth),delta:data.delta.toString(),
      radius:data.radius.toString(),method:data.method,terms,
      bernstein_coefficients:data.bernstein.map(strings),
      zero_coordinates:data.missing,
      interior_support:[0,1,2,3].filter(i=>!data.missing.includes(i)),
      coordinate_bounds:data.bounds.map(strings)};
  }
  function generate(raw) {
    const path=readPath(raw), epsilon=rat(raw.epsilon);
    if(epsilon.cmp(Z)<=0) fail("Tolerance must be positive");
    const tau=epsilon.div(2), N=20n*(ceil(rat(75).div(tau))>1n?ceil(rat(75).div(tau)):1n);
    const knotAnchors=[], plans=[], leaves=[];
    let warm=null, solverSteps=0n, solved=0n;
    const solve=(p,t,seed)=>{
      const a=solveAnchor(p,t,tau,N,seed); solverSteps+=a.steps; solved++; return a;
    };
    for(let j=0;j<path.knots.length;j++) {
      warm=solve(path.ops[j],path.knots[j],warm); knotAnchors.push(warm);
    }
    for(let j=0;j<path.knots.length-1;j++) {
      const eta=rowDistance(path.ops[j],path.ops[j+1]), limit=depthPlan(eta,epsilon);
      plans.push({segment:j,coefficient_variation:eta.toString(),maximum_depth:String(limit),maximum_cells:String(2n**limit)});
      const stack=[{left:knotAnchors[j],right:knotAnchors[j+1],depth:0n}];
      while(stack.length) {
        const task=stack.pop(), data=cellData(task.left,task.right);
        if(data.radius.cmp(epsilon)<=0) leaves.push({...task,data,segment:j});
        else {
          if(task.depth>=limit) fail("Proved partition depth exhausted");
          const t=task.left.t.add(task.right.t).div(2), p=blendOp(task.left.p,task.right.p,rat("1/2"));
          const middle=solve(p,t,task.left), next=task.depth+1n;
          stack.push({left:middle,right:task.right,depth:next});
          stack.push({left:task.left,right:middle,depth:next});
        }
      }
    }
    const anchors=[leaves[0].left,...leaves.map(x=>x.right)], cells=leaves.map((x,i)=>cellRecord(x.data,x.segment,i,x.depth));
    return {schema:"qso4-certified-continuation-v1",indexing:"types 0,1,2,3; unordered rows lexicographic",
      path:writePath(path),epsilon:epsilon.toString(),anchors:anchors.map(anchorRecord),cells,
      algorithm:{anchor_tolerance:tau.toString(),grid_denominator:String(N),plans,anchors_solved:String(solved),total_rounded_steps:String(solverSteps)}};
  }
  function sameRational(got,want,label) { if(!eq(rat(got),want)) fail("Incorrect "+label); }
  function sameArray(got,want,label) {
    if(!Array.isArray(got)||got.length!==want.length||got.some((x,i)=>x!==want[i])) fail("Incorrect "+label);
  }
  function verify(cert) {
    if(!cert||cert.schema!=="qso4-certified-continuation-v1") fail("Wrong certificate schema");
    const path=readPath(cert.path), epsilon=rat(cert.epsilon);
    if(epsilon.cmp(Z)<=0) fail("Tolerance must be positive");
    if(!Array.isArray(cert.anchors)||cert.anchors.length<2||!Array.isArray(cert.cells)||cert.cells.length!==cert.anchors.length-1) fail("Invalid partition cardinality");
    const anchors=cert.anchors.map(raw=>{
      const t=rat(raw.t), p=opAt(path,t), x=checkState(raw.x), residual=norm(sub(V(p,x),x)), error=residual.mul(5), missing=zeroOutputs(p);
      sameRational(raw.residual,residual,"anchor residual"); sameRational(raw.error,error,"anchor error");
      if(error.cmp(epsilon.div(2))>0) fail("Anchor tolerance unmet");
      sameArray(raw.zero_coordinates,missing,"anchor zero coordinates");
      return {t,p,x,residual,error,missing};
    });
    if(!eq(anchors[0].t,path.knots[0])||!eq(anchors[anchors.length-1].t,path.knots[path.knots.length-1])) fail("Endpoints not covered");
    let segment=0, maxRadius=Z, minBounds=[CAP,CAP,CAP,CAP];
    for(let i=0;i<cert.cells.length;i++) {
      const raw=cert.cells[i], a=anchors[i], b=anchors[i+1];
      if(a.t.cmp(b.t)>=0||raw.left!==i||raw.right!==i+1) fail("Gap, repetition or invalid adjacency");
      while(segment+1<path.knots.length-1 && a.t.cmp(path.knots[segment+1])>=0) segment++;
      if(raw.segment!==segment || a.t.cmp(path.knots[segment])<0 || b.t.cmp(path.knots[segment+1])>0) fail("Cell crosses an original knot");
      const data=cellData(a,b);
      sameRational(raw.delta,data.delta,"cell coefficient distance");
      sameRational(raw.radius,data.radius,"cell radius");
      if(raw.method!==data.method) fail("Incorrect chosen bound");
      for(const [name,v] of Object.entries(data.terms)) sameRational(raw.terms[name],v,"bound "+name);
      if(data.radius.cmp(epsilon)>0) fail("Cell tolerance unmet");
      if(!Array.isArray(raw.bernstein_coefficients)||raw.bernstein_coefficients.length!==4) fail("Invalid Bernstein certificate");
      for(let r=0;r<4;r++) {
        if(!Array.isArray(raw.bernstein_coefficients[r])||raw.bernstein_coefficients[r].length!==4) fail("Invalid Bernstein vector");
        for(let k=0;k<4;k++) sameRational(raw.bernstein_coefficients[r][k],data.bernstein[r][k],"Bernstein coefficient");
      }
      sameArray(raw.zero_coordinates,data.missing,"cell zero coordinates");
      sameArray(raw.interior_support,[0,1,2,3].filter(k=>!data.missing.includes(k)),"cell interior support");
      if(!Array.isArray(raw.coordinate_bounds)||raw.coordinate_bounds.length!==4) fail("Invalid coordinate bounds");
      for(let k=0;k<4;k++) {
        if(!Array.isArray(raw.coordinate_bounds[k])||raw.coordinate_bounds[k].length!==2) fail("Invalid coordinate interval");
        for(let l=0;l<2;l++) sameRational(raw.coordinate_bounds[k][l],data.bounds[k][l],"coordinate bound");
        minBounds[k]=rmin(minBounds[k],data.bounds[k][0]);
      }
      maxRadius=rmax(maxRadius,data.radius);
    }
    return {verified:true,anchors:anchors.length,cells:cert.cells.length,maximum_radius:maxRadius.toString(),global_coordinate_lower_bounds:strings(minBounds)};
  }
  function demoInput(epsilon="1/100") {
    const outputs=[1,2,1,1,2,0,2,0,0,0];
    const rows=outputs.map(k=>[0,1,2,3].map(j=>j===k?"1":"0"));
    const final=rows.map(row=>row.slice()); final[0]=["0","0","0","1"];
    return {knots:["0","1"],operators:[{rows},{rows:final}],epsilon};
  }
  function invariantInput(epsilon="1/100") {
    const raw=demoInput(epsilon), rows=raw.operators[0].rows.map(x=>x.slice());
    rows[9]=["0","1","0","0"]; raw.operators[1]={rows}; return raw;
  }
  return {R,rat,readPath,writePath,readOperator,checkState,opAt,B,V,rowDistance,zeroOutputs,
    bernsteinResidual,cellData,generate,verify,demoInput,invariantInput};
}
const qso94=qsoContinuation94();
if(typeof module!=="undefined") module.exports=qso94;
if(typeof require!=="undefined" && require.main===module) {
  try {
    const fs=require("fs"), arg=process.argv[2], input=arg==="--demo"?qso94.demoInput():JSON.parse(fs.readFileSync(0,"utf8"));
    const out=arg==="--verify"?qso94.verify(input):qso94.generate(input);
    process.stdout.write(JSON.stringify(out,null,2)+"\n");
  } catch(e) { process.stderr.write(String(e.message||e)+"\n"); process.exitCode=1; }
}
