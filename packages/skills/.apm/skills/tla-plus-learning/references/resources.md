# Learning and reusable resources

## Primary learning path

1. Use Leslie Lamport's [TLA+ Video Course](https://lamport.azurewebsites.net/video/videos.html)
   or the early [Hyperbook](https://lamport.azurewebsites.net/tla/hyperbook.html)
   chapters for states, actions, PlusCal, and TLC.
2. Use the [PlusCal Tutorial](https://lamport.azurewebsites.net/tla/tutorial/contents.html)
   for an algorithm-oriented route, including explicit liveness and fairness.
3. Use [Specifying Systems](https://lamport.azurewebsites.net/tla/book.html)
   as the language/tool reference and for composition and refinement.
4. Use the Hyperbook proof track and the
   [TLAPS tutorial](https://proofs.tlapl.us/doc/web/content/Documentation/Tutorial/The_example.html)
   for mechanically checked proofs.
5. Search the maintained [TLA+ Examples](https://github.com/tlaplus/Examples)
   manifests for beginner examples, proofs, trace generation, simulation,
   liveness failures, `ALIAS`, `VIEW`, symmetry, or constraints.

## Existing official agent skills

The TLA+ organization's MIT-licensed
[`tlaplus/AgentSkills`](https://github.com/tlaplus/AgentSkills) repository is
the strongest existing agent-skill source found in the survey. Its current
skills are narrow transformations:

- `tlaplus-from-source`: understand an existing concurrent/distributed
  implementation, abstract relevant state/actions, produce a runnable model,
  and propose safety/liveness properties;
- `tlaplus-add-variable`: update declarations, `Init`, `vars`, `TypeOk`, and
  every affected `UNCHANGED` clause consistently;
- `tlaplus-split-action`: refine atomicity by introducing an intermediate
  program-counter state and updating `Next`, type, unchanged, and fairness
  references.

Consult those skills when performing the matching transformation. They do not
replace Flyology's end-to-end requirement to combine TLC exploration, TLAPS
proof, and Ada trace replay, and they do not establish product-specific policy
or evidence boundaries.

## Tool references

- [TLC and TLA+ tools](https://github.com/tlaplus/tlaplus)
- [TLAPM/TLAPS](https://github.com/tlaplus/tlapm)
- [TLA+ language and tools notes](https://github.com/tlaplus/tlaplus/blob/master/general/docs/current-tools.md)
