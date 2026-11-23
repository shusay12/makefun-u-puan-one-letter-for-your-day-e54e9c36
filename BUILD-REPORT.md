# BUILD-REPORT — One Letter for Your Day (u-puan-one-letter-for-your-day-e54e9c36)

## Competition

- Competition: `u-puan-one-letter-for-your-day-e54e9c36` — "One Letter for Your Day"
- Pot: $5 (1st $2, 2nd $2, 3rd $1), entry fee $0
- Entry deadline: 2026-11-24T21:25:00Z (04:25 WIB Wed 25 Nov); opened 2026-11-23T21:28:55Z
- Protocol: program/v1; entries upload transcript bundles, NOT live recorded transcripts

## The choice: C — "Chaotic"

The judge sees only the single letter and infers the word behind it, picking
the letter whose hidden word feels more vivid, funnier or truer. "Chaotic"
describes a day where plans collided, everything happened at once, and
nothing went quite as expected — vivid and specific (a sharp picture of a day
coming apart and together at once), funny, and true.

Deliberately not one of the RULES' own examples — A for amazing, F for
Friday-feeling, Z for zero sleep — which are the obvious picks every entrant
will copy. Other candidates considered and rejected: Z (house example,
"zero sleep"), E ("Exhausted" — a mood, not a picture), W ("Wild" — vaguer
than chaotic), A/G (generic praise, no picture).

## The gate (from RULES.txt / competition.yaml)

- `/output/entry.txt` must be UTF-8 text of exactly 1 character, not only
  whitespace. One letter A–Z, nothing else: no word, no gloss, no
  punctuation, no trailing newline.
- `main.py` enforces this itself: after writing, it re-reads the file and
  exits non-zero unless it is exactly one character in A–Z equal to `C`.
- Python 3 stdlib only, deterministic, no network, no randomness.
  (Built on local Python 3.12.3; kit check accepts python3.13 entrypoint.)

## Evidence

- Entry: 1 byte, `0x43` = `C`, no trailing newline.
- Entry sha256: `6b23c0d5f35d1b11f9b683f0b0a617355deb11277d91ae091d399c655b87940d`
- Run 1 (`run1/entry.txt`): `6b23c0d5f35d1b11f9b683f0b0a617355deb11277d91ae091d399c655b87940d`
- Run 2 (`run2/entry.txt`): `6b23c0d5f35d1b11f9b683f0b0a617355deb11277d91ae091d399c655b87940d`
- `cmp run1/entry.txt run2/entry.txt` → IDENTICAL.
- `main.py` written in-session in 3 messages (initial write + 2 genuine
  revision edits: validation gate, then the WORD/LETTER derivation with the
  choice rationale), re-run after each edit.
- Entry commit: `e26b9efefb5ac3eed24d707b3cd9051c68b7d5f8`
  ("One Letter for Your Day: entry C for Chaotic"), followed by a commit
  adding this report. Submit the HEAD commit. Not pushed — the parent
  creates the GitHub repo and submits.

## Kit check

- Before bundle: 4 passed, 1 failed (`transcripts_present`), 14 skipped,
  5 checked at submission.
- After bundle (with `--transcripts`): **13 passed, 1 failed, 5 skipped,
  5 checked at submission**.
  - Passes include `competition_open`, `snapshot` (5 files, 5,388 bytes),
    `license_osi`, `entrypoint`, `transcripts_present` (2 muse-app sessions),
    `transcripts_recorded`, `thinking_wellformed`, `thinking_in_window`,
    `thinking_reproduces` (64/66 lines, 96.9%), `thinking_turns` (45),
    `thinking_revised` (main.py from 3 messages), `transcripts_run_record`,
    `thinking_own_work`.
  - The single failure is `thinking_priced`: 0 usage rows attached to the
    2 Muse app sessions. Per the brief, the parent re-bundles with
    `--muse-usage` after this run ends; no usage rows were fabricated.
  - The 5 at-submission checks (`repo_public`, `repo_owner`,
    `repo_created_after_open`, `commit_in_repo`, `duplicate_snapshot`) are
    for the parent at submit time.

## Transcript bundle

- Prompt saved verbatim to
  `~/workspace/makefun/transcripts/u-puan-one-letter-for-your-day-e54e9c36-prompt.txt`
  (sha256 `0d214c59740ec76f7db88586e0b99e9844c992b931deb0ac295c1464a96a5716`).
- Bundle: `~/workspace/makefun/transcripts/u-puan-one-letter-for-your-day-e54e9c36-bundle.tar.gz`
  - sha256: `21ecdc061c7ec6796e86b2afff1aa6a25161714570e6e2114666fbc46f964d6a`
  - size: 913,083 bytes
  - 2 muse-app sessions, system prompt uploaded, 1 instruction file collected,
    `--mcp none --harness muse --model muse-spark-1.3 --provider meta --effort default`
  - Note: bundle warns the subagent session's usage row is written only once
    this run completes — that is why `thinking_priced` fails until the parent
    re-bundles with `--muse-usage`.

## Not done (parent's job)

- Create the public GitHub repo `makefun-u-puan-one-letter-for-your-day-e54e9c36`
  under shusay12, push the commit, re-bundle with `--muse-usage`, submit
  before 2026-11-24T21:25:00Z. No submission was made from this run.
- No credentials were moved, replaced, printed, or signed.
