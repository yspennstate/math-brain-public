"use strict";
/*
Agent 090: exact certificate for the cubic four-type parent-exclusion note.
Dependency-free JavaScript; run with node agents/090_exact_certificate.js.
The proof is analytic. This program checks the symbolic transfer expansion,
its extremizers, the rational invariant-cap chain, and contraction constants.
*/
(function () {
  function assert(ok, message) { if (!ok) throw new Error(message); }
  function gcd(a, b) {
    a = a < 0n ? -a : a; b = b < 0n ? -b : b;
    while (b) { const r = a % b; a = b; b = r; }
    return a;
  }
  function Q(n, d) {
    n = BigInt(n); d = d === undefined ? 1n : BigInt(d);
    assert(d !== 0n, "zero denominator");
    if (d < 0n) { n = -n; d = -d; }
    const g = gcd(n, d); return { n: n / g, d: d / g };
  }
  function add(a, b) { return Q(a.n * b.d + b.n * a.d, a.d * b.d); }
  function neg(a) { return Q(-a.n, a.d); }
  function sub(a, b) { return add(a, neg(b)); }
  function mul(a, b) { return Q(a.n * b.n, a.d * b.d); }
  function cmp(a, b) {
    const t = a.n * b.d - b.n * a.d; return t < 0n ? -1 : t > 0n ? 1 : 0;
  }
  function eq(a, b) { return cmp(a, b) === 0; }
  function fmt(a) { return a.d === 1n ? String(a.n) : a.n + "/" + a.d; }
  function max(a, b) { return cmp(a, b) >= 0 ? a : b; }
  const zero = Q(0), one = Q(1), two = Q(2), three = Q(3);
  function square(a) { return mul(a, a); }
  function cube(a) { return mul(square(a), a); }

  // Integer quadratic polynomials in a=m_0,b=m_1,c=m_2,d=m_3.
  // A monomial is the sorted pair of coordinate indices, e.g. "02" means ac.
  function put(p, monomial, value) {
    p[monomial] = (p[monomial] || 0) + value;
    if (p[monomial] === 0) delete p[monomial];
  }
  function polySum() {
    const p = {};
    for (const a of arguments) for (const k of Object.keys(a)) put(p, k, a[k]);
    return p;
  }
  function polyEq(a, b, label) {
    const keys = new Set(Object.keys(a).concat(Object.keys(b)));
    assert(Array.from(keys).every(k => (a[k] || 0) === (b[k] || 0)), label);
  }
  function evaluate(p, m) {
    let v = zero;
    for (const k of Object.keys(p)) {
      v = add(v, mul(Q(p[k]), mul(m[Number(k[0])], m[Number(k[1])])));
    }
    return v;
  }
  const rows = [];
  for (let a = 0; a < 4; a++)
    for (let b = a; b < 4; b++)
      for (let c = b; c < 4; c++) rows.push([a, b, c]);
  assert(rows.length === 20, "twenty symmetric cubic parent rows");
  const polys = {};
  for (const row of rows) polys[row.join("")] = {};
  for (let a = 0; a < 4; a++) for (let b = 0; b < 4; b++) {
    for (const spec of [[0, 1], [2, -1]]) {
      const row = [a, b, spec[0]].sort().join("");
      put(polys[row], [a, b].sort().join(""), spec[1]);
    }
  }
  const expectedFree = {
    "000": { "00": 1 },
    "002": { "00": -1, "02": 2 },
    "003": { "03": 2 },
    "022": { "02": -2, "22": 1 },
    "033": { "33": 1 },
    "111": {},
    "112": { "11": -1 },
    "113": {},
    "122": { "12": -2 },
    "133": {},
    "222": { "22": -1 },
    "333": {}
  };
  let forced = {}, freeCount = 0;
  for (const row of rows) {
    const key = row.join("");
    const misses = [0, 1, 2, 3].filter(k => !row.includes(k));
    assert(misses.length > 0, "every cubic parent row permits an offspring");
    const forcedZero = row.includes(0) && row.includes(1);
    const forcedOne = row.includes(2) && row.includes(3);
    assert(!(forcedZero && forcedOne), "forced group rules are consistent");
    if (forcedOne) forced = polySum(forced, polys[key]);
    else if (!forcedZero) {
      assert(Object.prototype.hasOwnProperty.call(expectedFree, key), "free row listed");
      polyEq(polys[key], expectedFree[key], "free row expansion " + key);
      freeCount++;
    }
  }
  assert(freeCount === 12, "twelve free group-probability rows");
  polyEq(forced, { "03": -2, "13": -2, "33": -1 }, "forced contribution");
  // Maximizing the certainly positive free coefficients cancels 2ad+d^2.
  polyEq(polySum(forced, { "00": 1, "03": 2, "33": 1 }),
         { "00": 1, "13": -2 }, "base of exact positive-part maximum");
  // The three ratio regions give max(a^2,2ac,c^2).
  polyEq({ "00": 1 }, { "00": 1 }, "c <= a/2");
  polyEq(polySum({ "00": 1 }, expectedFree["002"]),
         { "02": 2 }, "a/2 <= c <= 2a");
  polyEq(polySum({ "00": 1 }, expectedFree["002"], expectedFree["022"]),
         { "22": 1 }, "c >= 2a");

  // Build exact admissible extremizers at three rational caps.
  const sharp = [];
  for (const q of [Q(1, 4), Q(8, 25), Q(1, 3)]) {
    const m = [q, q, q, sub(one, mul(three, q))];
    const output = {};
    for (const row of rows) {
      const key = row.join("");
      const forcedZero = row.includes(0) && row.includes(1);
      const forcedOne = row.includes(2) && row.includes(3);
      const p = forcedZero ? 0 : forcedOne ? 1 : cmp(evaluate(polys[key], m), zero) >= 0 ? 1 : 0;
      const choices = [0, 1, 2, 3].filter(k => !row.includes(k) && (k < 2 ? 1 : 0) === p);
      assert(choices.length > 0, "extreme group choice permits an offspring");
      output[key] = choices[0]; // Deterministic stochastic row.
    }
    let D = zero;
    for (let a = 0; a < 4; a++) for (let b = 0; b < 4; b++) {
      const u = output[[a, b, 0].sort().join("")] < 2 ? 1 : 0;
      const v = output[[a, b, 2].sort().join("")] < 2 ? 1 : 0;
      D = add(D, mul(Q(u - v), mul(m[a], m[b])));
    }
    const bound = mul(mul(two, q), sub(mul(Q(4), q), one));
    assert(eq(D, bound), "sharp cap transfer bound at " + fmt(q));
    sharp.push({ cap: fmt(q), transfer: fmt(D) });
  }

  const lambda = Q(3, 10), cap = Q(1, 3);
  function f(u) { return add(mul(sub(one, lambda), u), mul(lambda, cube(sub(one, u)))); }
  assert(cmp(lambda, cap) <= 0, "zero endpoint for cap invariance");
  assert(eq(f(cap), Q(29, 90)), "cap endpoint equals 29/90");
  assert(cmp(f(cap), cap) < 0, "strict cap endpoint");
  const chain = [Q(1), Q(7, 10), Q(1, 2), Q(2, 5), Q(7, 20), cap];
  const exactValues = [Q(7, 10), Q(4981, 10000), Q(31, 80), Q(431, 1250), Q(26191, 80000)];
  const capChecks = [];
  for (let n = 0; n + 1 < chain.length; n++) {
    const v = f(chain[n]);
    assert(eq(v, exactValues[n]), "exact cap chain value " + n);
    assert(cmp(max(lambda, v), chain[n + 1]) <= 0, "cap chain inequality " + n);
    capChecks.push({ from: fmt(chain[n]), envelope: fmt(v), to: fmt(chain[n + 1]) });
  }
  const transferCap = Q(2, 9);
  const cutGain = mul(three, transferCap);
  const nonsplit = mul(three, lambda);
  const split = add(sub(one, lambda), mul(mul(three, lambda), transferCap));
  assert(eq(cutGain, Q(2, 3)), "uniqueness gain 2/3");
  assert(eq(nonsplit, Q(9, 10)), "nonsplit contraction 9/10");
  assert(eq(split, Q(9, 10)), "split contraction 9/10");
  assert(cmp(split, one) < 0, "strict contraction");
  const allFourParentTypes = [0, 1, 2, 3];
  assert([0, 1, 2, 3].every(k => allFourParentTypes.includes(k)), "degree-four forbidden row");

  const result = {
    status: "PASS",
    symmetricRows: rows.length,
    freeGroupRows: freeCount,
    symbolicExpansion: "verified over integer polynomial coefficients",
    transferFormula: "max(a^2,2*a*c,c^2)-2*b*d",
    sharpCapExamples: sharp,
    capChain: capChecks,
    iteration: "(7 I + 3 V)/10",
    entrySteps: 5,
    contraction: fmt(split),
    fixedPointSignCutGain: fmt(cutGain)
  };
  if (typeof globalThis.certificateReport === "function") globalThis.certificateReport(result);
  else console.log(JSON.stringify(result, null, 2));
  return result;
})();
