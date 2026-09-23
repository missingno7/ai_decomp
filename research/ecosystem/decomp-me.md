# decomp.me: a collaborative compiler experiment bench

Inspected 2026-09-23 at commit `b908a4f32af89721fc0db3d8155ffe9696a91c13`.
**EXTERNAL IMPLEMENTATION FACT** below means inspected source, not a service
availability test. No hosted scratch was created, compiler downloaded or build run.
The application is MIT; historical compilers and its dependencies have separate
rights. Structured capabilities and source anchors are in [decomp-me.json](decomp-me.json).

## What is already solved

The application combines editable C/C++ and context, a selected compiler and
flags, target assembly or object, recompilation, asm-differ feedback, saved
scratches and forks. It is a practical collaborative matching workbench. It does
not generate an adaptive series of source hypotheses by itself. Automatic
recompilation of edits is different from automatic search.

The compiler wrapper concatenates context and candidate into one temporary
source, inserts source/context line directives, adds configured libraries and
includes, executes a compiler recipe under resource limits, and checks for
nonempty object output. Compiler results are memoized by inputs. This is a
valuable existing execution boundary; it is not effective-output clustering.
Compiler definitions encode command-line quirks and historical execution
routes, including IDO/MWCC accommodations. They do not provide a general inverse
compiler model or infer compiler provenance. See
[compiler wrapper](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/compiler_wrapper.py#L92-L214)
and [compiler definitions](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/compilers.py).

Architecture settings cover MIPS variants, PPC, ARM/Thumb, AArch64, SuperH,
DOS x86 and Win32/i686. Object support follows the configured assembler and
objdump pair: ELF-oriented console/platform workflows, COFF Win32, and DOS OMF.
This does not imply a whole-executable comparator for every listed platform.
An m2c seed can use the scratch's context and supported compiler triple;
the wrapper has MIPS/PPC/ARM/SH2 mappings, not x86 reconstruction. Sources:
[platform definitions](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/platforms.py),
[m2c wrapper](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/m2c_wrapper.py).

The [dependency lock](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/uv.lock)
pins m2c `708d2d2cb2698f091a92492b328f73b24209f72d` and asm-differ
`0dd09af8f8008f1f880327cf0aca3b26d2562ea2`, the same revisions inspected
separately in this pass.

## Historical x86 is already present, with exact-version caveats

The DOS platform invokes JWasm, `omf-objdump --no-objects` and `omf-nm`.
The Linux compiler manifest includes MSC 5.1, Borland C++ 2.0/3.1 and Watcom
10/11 variants. MSC 5.1 runs `CL.EXE /c` through DOSEMU. This is directly
relevant to Stunts' compiler family and to comparing OMF disassembly. It is
evidence of implemented recipes, not a verified replacement for Stunts' pinned
compiler bytes, runtime, include set or runner.

Do not mistake **Borland C++ 2.0** for Empires' **Turbo C 2.0**, or **Win32
MSVC 7.0** for SimAnt's **Win16 MSC 7.00**. The inspected manifest does not
establish an exact runner for those two projects or Icy Tower's TDM GCC 4.4.1.
The DOS disassembler package is pinned to `decompals/binutils-omf` v0.4;
the [diff-tools study](diff-tools.md) examines its narrower reuse boundary.
Sources: [manifest](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/compilers/compilers.linux.yaml#L215-L223),
[DOS recipes](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/compilers.py#L1675-L1704),
[compiler names](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/frontend/src/lib/i18n/locales/en/compilers.json),
[dependency pins](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/Dockerfile#L110-L128).

## Feedback is richer than a number, but narrower than acceptance

`diff_wrapper.py` delegates object disassembly and alignment to asm-differ and
returns structured formatter rows and scores. Its configured comparison is
`.text`, enables branches, disables source/line display in this backend, and
sets `ignore_addr_diffs=True`. Relocation interpretation is inherited from
platform objdump output and asm-differ's processor. It is not raw FIXUPP order,
private DATA/BSS placement, selector pairing or link-topology certification.
Levenshtein is the default alignment algorithm; an option selects difflib.
See [diff configuration and execution](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/diff_wrapper.py).

There is already a **Target / Current / Saved-or-Previous** three-column
comparison. Thus candidate-versus-parent-versus-oracle *display* is not a new
idea. It differs from a causal experiment record that binds changed source
dimensions, context identity, output classes, residual mechanism and independent
proof. See [implemented columns](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/frontend/src/components/Diff/Diff.tsx#L334-L439).

Scratch records retain compiler/flags, code/context, target, score, parent and
family. Uploaded targets use SHA-256; context deduplication uses an eight-byte
BLAKE2b value with a collision check. Source text is stored, not a full
hash-addressed experiment fingerprint. These mechanisms support
sharing and version lineage, not a search beam or a durable compiler-mechanism
database. Crucially, `Scratch.is_match` accepts either zero score **or a manual
match override**. Never import a scratch badge as a strict receipt.
Sources: [scratch model](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/models/scratch.py),
[target caching and compilation](https://github.com/decompme/decomp.me/blob/b908a4f32af89721fc0db3d8155ffe9696a91c13/backend/coreapp/views/scratch.py).

## Reuse decision

**INFERENCE.** Learn from its historical compiler recipes, scratch/context
packaging, bounded execution and three-way feedback. Use an optional local
scratch/viewer if a real workflow calls for one. Do not build a second web
workbench or extract the backend merely to run existing project compilers.
Our local runners already preserve more relevant proof context. Context text
can include neighboring declarations/functions, but that is not automatic
historical TU membership, order, private-data or compiler-pass reconstruction.

No LLM, adaptive candidate batching, compiled-output clustering or autonomous
source revision was found in the inspected compiler/diff/scratch path. These
are scoped implementation findings, not claims about every plugin, branch or
future hosted feature. The app provides a useful part of the loop, while
project-owned acceptance must remain independent.
