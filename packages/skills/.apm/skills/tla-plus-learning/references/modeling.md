# Modeling reactive algorithms

## Start with behaviors

TLA+ describes allowed behaviors: sequences of states connected by actions.
Choose variables that retain only information relevant to the claim. An action
is an atomic relation between an old state and a new state; it is not a direct
translation of each Ada statement.

A conventional specification has:

```tla
VARIABLES x, phase
vars == <<x, phase>>

Init == x = Initial /\ phase = "Ready"

Advance ==
  /\ phase = "Ready"
  /\ x' = NextValue(x)
  /\ phase' = "Done"

Next == Advance \/ OtherAction
Spec == Init /\ [][Next]_vars
```

Every action must constrain every variable, either with a primed expression or
`UNCHANGED`. `[][Next]_vars` permits stuttering steps, which is necessary for
composition and refinement: a concrete step may leave all abstract variables
unchanged.

## Choose properties deliberately

- A state invariant rules out a bad state, for example duplicated ownership or
  a visible value that was never published.
- A safety property says that no finite prefix demonstrates something bad.
- A liveness property says that something good eventually happens. Termination
  is liveness.
- `P ~> Q` says every occurrence of `P` is followed by `Q` now or later.
- Fairness rules out behaviors that postpone an enabled action forever. Weak
  fairness applies to an action that remains continuously enabled; strong
  fairness applies when it becomes enabled infinitely often.

Do not add fairness merely to make TLC green. It is an assumption about the
algorithm or environment and must be justified by the implementation contract.
Deadlock freedom is not enough: an algorithm may livelock, or one participant
may starve while the system continues to move.

## Abstract without changing the question

Collapse implementation detail when it does not affect the property: byte
buffers may become values, protected regions may become one action, and a large
identifier space may become two or three model values. Preserve distinctions
that affect outcomes: ownership, generations, retries, unknown results,
failure timing, cancellation, or ordering.

Finite TLC constants are test geometry, not product limits. Keep them in model
configuration unless an independently authorized product contract fixes them.

When an Ada implementation already exists, derive a model from its intended
contract rather than mirroring its bugs. Record an explicit mapping from TLA+
actions/state to Ada entry points and observable state. A successful trace
replay validates selected behaviors; a refinement theorem must explicitly
prove that every concrete behavior maps to an allowed abstract behavior.

## Primary sources

- Leslie Lamport, [A High-Level View of TLA+](https://lamport.azurewebsites.net/tla/high-level-view.html)
- Leslie Lamport, [Safety, Liveness, and Fairness](https://lamport.azurewebsites.net/tla/safety-liveness.pdf)
- Leslie Lamport, [PlusCal Tutorial: Liveness](https://lamport.azurewebsites.net/tla/tutorial/session9.html)
- Leslie Lamport, [Specifying Systems](https://lamport.azurewebsites.net/tla/book.html)
