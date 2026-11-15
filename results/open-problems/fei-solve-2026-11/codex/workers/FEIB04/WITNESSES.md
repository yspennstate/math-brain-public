# Search witnesses

These are lower bounds on unrestricted suprema. They are not global maxima.
S = empty is included. All logarithmic quantities are in bits. Influence
is an expected number of sensitive coordinates. Exhaustive symmetric-class numerical
maxima, including a representative of every output-complement pair, are
in symmetric_search.jsonl. Complete records are in search_audit.json.

| n | best Gamma/I | witness | best balanced Gamma/(I-1) | witness |
|---|---:|---|---:|---|
| 6 | 0.523731127744 | truth:6:ordinary | 0.689548150491 | truth:6:balanced |
| 7 | 0.624076163553 | block:7:ordinary | 0.694742671847 | truth:7:balanced |
| 8 | 0.627219751450 | block:8:ordinary | 0.762762075485 | symmetric:8:balanced |
| 9 | 0.712432861119 | symmetric:9:ordinary | 0.801046772704 | block:9:balanced |
| 10 | 0.712432861119 | embedding:10:symmetric:9:ordinary | 0.801046772704 | embedding:10:block:9:balanced |
| 11 | 0.755555729626 | block:11:ordinary | 0.834333689746 | block:11:balanced |
| 12 | 0.755555729626 | embedding:12:block:11:ordinary | 0.896994903569 | block:12:balanced |
| 13 | 0.791524158167 | symmetric:13:ordinary | 0.896994903569 | embedding:13:block:12:balanced |
| 14 | 0.803067237009 | block:14:ordinary | 0.896994903569 | embedding:14:block:12:balanced |
| 15 | 0.818794138007 | block:15:ordinary | 0.914596376813 | block:15:balanced |
| 16 | 0.836833202802 | block:16:ordinary | 0.914596376813 | embedding:16:block:15:balanced |
| 17 | 0.848406920346 | block:17:ordinary | 0.983146568043 | block:17:balanced |
| 18 | 0.861912974053 | symmetric:18:ordinary | 1.027939128342 | block:18:balanced |
| 19 | 0.871821816326 | block:19:ordinary | 1.027939128342 | embedding:19:block:18:balanced |
| 20 | 0.890955034811 | symmetric:20:ordinary | 1.027939128342 | embedding:20:block:18:balanced |

A plus sign means f=+1; a minus sign means f=-1. In a one-block
symmetric witness the string runs from Hamming weight 0 to n.
Two-block strings run in row-major order, first-block weight outside
and second-block weight inside. Truth-table strings list f(x) for
integer x=0,1,...; the stored hexadecimal encoding sets bit x when
f(x)=-1. Composition witnesses name two gate ids and the zero-based
outer coordinate replaced by the balanced inner gate. Dummy extensions
use the named lower-dimensional function and ignore the added inputs;
this keeps the ambient-dimension lower bounds nondecreasing.

## truth:6:ordinary

truth table, input integer 0 first.

```text
-++---+++-++--+-+-++-+++++++++-+++++-+-+-+++++++-++-++-+++++++++
```

Gamma = 1.3093278193589115 bits; I = 2.5; bias = 0.46875.

## truth:6:balanced

truth table, input integer 0 first.

```text
+++-++--++-+-+--------+--+--+---++-+--+-+++++--++++---+-+++++-+-
```

Gamma = 1.1636125039537499 bits; I = 2.6875; bias = 0.

## block:7:ordinary

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 3, 4.

```text
--+++-+++-+++--++--+
```

Gamma = 1.5016832685494927 bits; I = 2.40625; bias = 0.4375.

## truth:7:balanced

truth table, input integer 0 first.

```text
+-+++---+-+++----+------+-----+-+++-++--++-++---+-------+-+-----++++++-++++++++----+++++-+++++-++-+-----+++-+-----+---+++++++++-
```

Gamma = 1.2809318012185438 bits; I = 2.84375; bias = 0.

## block:8:ordinary

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 3, 5.

```text
-++---++----+---+-+----+
```

Gamma = 1.4994472183112153 bits; I = 2.390625; bias = -0.5859375.

## symmetric:8:balanced

Hamming layers, weight 0 first.

```text
+---++--+
```

Gamma = 2.0022504481489589 bits; I = 3.625; bias = 0.

## symmetric:9:ordinary

Hamming layers, weight 0 first.

```text
+-++---++-
```

Gamma = 2.3543679707288967 bits; I = 3.3046875; bias = -0.3515625.

## block:9:balanced

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 4, 5.

```text
++++---+++---++----+---++--++-
```

Gamma = 1.808613416494947 bits; I = 3.2578125; bias = 0.

## embedding:10:symmetric:9:ordinary

Use `symmetric:9:ordinary` on its 9 inputs and ignore the remaining inputs.

Gamma = 2.3543679707288967 bits; I = 3.3046875; bias = -0.3515625.

## embedding:10:block:9:balanced

Use `block:9:balanced` on its 9 inputs and ignore the remaining inputs.

Gamma = 1.808613416494947 bits; I = 3.2578125; bias = 0.

## block:11:ordinary

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 5, 6.

```text
---++----++----++---+++---+++---+++---+++-
```

Gamma = 3.0517368141931907 bits; I = 4.0390625; bias = -0.291015625.

## block:11:balanced

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 5, 6.

```text
-+--++-++++---++++----++--++-+---++----+++
```

Gamma = 2.3286383645451849 bits; I = 3.791015625; bias = 0.

## embedding:12:block:11:ordinary

Use `block:11:ordinary` on its 11 inputs and ignore the remaining inputs.

Gamma = 3.0517368141931907 bits; I = 4.0390625; bias = -0.291015625.

## block:12:balanced

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 5, 7.

```text
----+++++---++--+-+++-----++---+-++---+++++-----
```

Gamma = 3.0930556684591863 bits; I = 4.4482421875; bias = 0.

## symmetric:13:ordinary

Hamming layers, weight 0 first.

```text
++++--+++---+-
```

Gamma = 3.8184856849055686 bits; I = 4.82421875; bias = 0.24755859375.

## embedding:13:block:12:balanced

Use `block:12:balanced` on its 12 inputs and ignore the remaining inputs.

Gamma = 3.0930556684591863 bits; I = 4.4482421875; bias = 0.

## block:14:ordinary

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 7, 7.

```text
+--++------++--+-+++---+-++-----++------+-----++-----+++-++--+++
```

Gamma = 2.4072410976568457 bits; I = 2.99755859375; bias = -0.5579833984375.

## embedding:14:block:12:balanced

Use `block:12:balanced` on its 12 inputs and ignore the remaining inputs.

Gamma = 3.0930556684591863 bits; I = 4.4482421875; bias = 0.

## block:15:ordinary

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 7, 8.

```text
-++-----++--+++---+---+++--++---+++--++---+++-++----+++-++-----+--+++++-
```

Gamma = 3.7419451829485038 bits; I = 4.570068359375; bias = -0.2418212890625.

## block:15:balanced

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 7, 8.

```text
++--++--+-++--+++-+++---+++++++---++--+++-------+++---+---++--+-++--++--
```

Gamma = 3.6565991862034113 bits; I = 4.998046875; bias = 0.

## block:16:ordinary

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 7, 9.

```text
--+++-----++--+++--+++---++--++-----++--+------++--++-----+--+++----+++--++++--+
```

Gamma = 3.1203499771475869 bits; I = 3.728759765625; bias = -0.52117919921875.

## embedding:16:block:15:balanced

Use `block:15:balanced` on its 15 inputs and ignore the remaining inputs.

Gamma = 3.6565991862034113 bits; I = 4.998046875; bias = 0.

## block:17:ordinary

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 8, 9.

```text
+-++++++++++++-----++++---+++-+++--+++--++--+++------+++----+-+++-----+++++-----++-----+++
```

Gamma = 4.891971574326206 bits; I = 5.7660675048828125; bias = 0.1422576904296875.

## block:17:balanced

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 8, 9.

```text
-+----++--++---++--++---+++--++--+++--+++++++--+++++++---++++++------+++--++--+-++--++---+
```

Gamma = 4.551763387794086 bits; I = 5.629791259765625; bias = 0.

## symmetric:18:ordinary

Hamming layers, weight 0 first.

```text
++++--+++++---++---
```

Gamma = 3.4127208528297759 bits; I = 3.95947265625; bias = 0.460174560546875.

## block:18:balanced

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 9, 9.

```text
+++-++----+++++---++--++----++++----++-+-+---+++------+++---+--+++------+++------++----+--+---+++---
```

Gamma = 5.036126884621722 bits; I = 5.8992462158203125; bias = 0.

## block:19:ordinary

row-major Hamming layers: first-block weight, then second-block weight.

Block sizes: 9, 10.

```text
+-++++--+++----+++---------+++----++-----++-++++----++-+-+++---+++---+++---++-+--+++--+++++--++++++--+-++-++++
```

Gamma = 4.7571963908653867 bits; I = 5.4566154479980469; bias = -0.22885513305664062.

## embedding:19:block:18:balanced

Use `block:18:balanced` on its 18 inputs and ignore the remaining inputs.

Gamma = 5.036126884621722 bits; I = 5.8992462158203125; bias = 0.

## symmetric:20:ordinary

Hamming layers, weight 0 first.

```text
++--++---+++++--++++-
```

Gamma = 4.0515166028866147 bits; I = 4.5473861694335938; bias = 0.43190574645996094.

## embedding:20:block:18:balanced

Use `block:18:balanced` on its 18 inputs and ignore the remaining inputs.

Gamma = 5.036126884621722 bits; I = 5.8992462158203125; bias = 0.

