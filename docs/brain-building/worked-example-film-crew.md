# Worked example: a film crew's brain from framework/filmbrain

The starter in `examples/field_brain_starter/` keeps a team's records as Markdown files. `framework/filmbrain/` is
the other shape a field brain can take: a graph of craft knowledge in SQLite, with lessons and measured runs attached
to the nodes they are about. This page builds one from a fresh copy of this repository and shows each command with
what it printed. Nothing outside the standard library is needed for the steps below; the ffmpeg and Blender harvesters
are optional and were not run.

Every command runs from `framework/filmbrain/`. `FILMBRAIN_ROOT` says where the store goes; leave it out and the store
sits beside the code.

```
cd framework/filmbrain
export FILMBRAIN_ROOT=/tmp/filmbrain_store     # on Windows: set FILMBRAIN_ROOT=C:\temp\filmbrain_store
```

## 1. Build the store

The database is not shipped. The authored craft layer is Python in `craft/`, one file per domain (camera, light and
colour, editing and sound, narration, recipes, symptoms and so on), and one command loads it:

```
python ingest/load_craft.py
```

```
craft: 596 nodes 997 edges, 11 stubs
stubs to fill: craft.flattering_portrait, craft.focus_reliability, craft.format, ...
```

A stub is a node something points at that nobody has written yet. It is a to-do list, not an error.
`python filmbrain.py stats` then counts what is in the store by kind and by relation: 462 craft nodes, 72 failures,
20 tools, 19 metrics, and edges such as `part_of`, `requires`, `prevents` and `causes`.

## 2. Ask it something

```
python filmbrain.py recall "how do I stop a render looking computer generated"
```

```
  [craft] it looks computer generated / fake / plastic  (symptom.looks_cgi)
      Almost never a modelling problem. Motion blur off, no depth of field or a fake uniform blur,
      no contact shadow where things touch, perfect symmetry and perfect cleanliness, lighting with
      no bounce, and no grain to bind the layers together. Fix them in that order; ...

  [craft] stop a render looking computer-generated  (recipe.make_a_render_look_shot)
      In the order that buys the most per minute of work. 1. Turn motion blur ON ...
```

The first card names the symptom the question describes, the second the recipe that fixes it, with the command.
`python filmbrain.py node craft.narration_pacing` reads one node whole: its text, its status and source, and every
edge in and out (`measured_by words per minute`, `part_of narration`, `requires the speed dial, measured`).

## 3. Ask it to plan a piece

```
python fbplan.py "a ten minute documentary from old photographs" --minutes 10
```

The plan read the request as a documentary and printed, in order: a five-beat shape for the form; the budget at ten
minutes (about 1,650 words of narration, about 24 beats of 25 seconds); the craft nodes that apply (documentary form,
working with archive, cutaways, what an edit implies, grain, the wrong aspect ratio); recipes with their commands,
such as a contact sheet of every shot for quality control:

```
ffmpeg -i in.mp4 -vf "fps=1/10,scale=320:-1,tile=6x5" -frames:v 1 sheet.png
```

and last a checklist of what goes wrong (a jump cut, banding in gradients, an upscale that reads as plastic, a map
with every label printed), each with the node that prevents it. Its cost figures for rendering are marked as upper
bounds: they scale one measured unit and assume nothing is reused. Write your own machine's figures into
`craft/this_machine.py`, which ships empty on purpose.

## 4. Teach it something

A lesson is attached to the node it is about and carries its evidence and how far it has been checked
(`provisional`, `verified` or `owner-stated`). The lesson below is made up for the walk:

```
python filmbrain.py learn "a read near 180 words a minute is fine on headphones but too fast for new terms on a phone speaker" \
    --node craft.narration_pacing --evidence "one test read played both ways" --confidence provisional
```

```
learned les_36ae9f7acb5458a3
```

The lesson now appears under `learned` when the node is read, and recall prints it under "what we learned, in our
own runs" for a question in other words:

```
python filmbrain.py recall "narration too fast on a phone" --brief
```

```
  what we learned, in our own runs
    [provisional] a read near 180 words a minute is fine on headphones but too fast for new terms on
    a phone speaker
        evidence: one test read played both ways
```

The node's authored text already says explainer narration sits at 160 to 180 words a minute. The lesson narrows that
for one kind of listener, and recall now brings both back together.

## 5. Let a run record itself

`fbrun.py` wraps any render or synthesis command and stores the command, its wall time, its exit status and anything
the command prints after `FBMETRIC` or `FBLEARN`. Here the wrapped command is a stand-in for a render script:

```
python fbrun.py --kind render --tool python --node craft.grain -- \
    python -c "print('FBMETRIC seconds_per_clip=2.5'); print('FBLEARN grain at strength 4 hides banding in a dark sky')"
```

```
[filmbrain] run_20261103_011144_eb03e4 ok 0.4s python metrics=1 lessons=1
```

`stats` now reads `runs 1   observations 3   lessons 2`, and `recall "banding in a dark sky"` prints the new lesson with
the run's id as its evidence. A render script that prints those two kinds of line teaches the brain without anyone
remembering to file a note.

## What the two shapes are for

The starter's Markdown records suit a team whose knowledge is decisions, incidents and rules: a few hundred records a
person can read and correct by hand, served to agents by hooks. The film brain suits a craft with a large technical
surface. Its authored layer says what to do and why, the harvesters read what the installed tools can actually do,
and lessons and runs attach measurements to both. A film crew can run both: the starter for its own decisions and
mistakes, and this graph for the craft. The investigations desk in
[worked-example-investigations-desk.md](worked-example-investigations-desk.md) runs the starter alone.
