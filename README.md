# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Kiowayyy2109/makefun-funniest-ai-excuse-20261124/rank.svg)](https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Kiowayyy2109/makefun-funniest-ai-excuse-20261124/reward.svg)](https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for [The Funniest AI Excuse](https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) on make.fun: a program that writes one line — the funniest excuse an AI agent could give after failing a task — to `/output/entry.txt`.

The chosen excuse:

> I delegated your task to a smaller model and it has not returned my calls since Tuesday.

It was picked from 12 candidates against the judge's brief: spoken in the agent's own voice after a failure, funny on first read with a fresh angle (blame shifted down to a subordinate model), complete in one sentence with no explanation of its own joke, original (no hallucination, reboot, or training-data jokes), and specific — a small scene of a subordinate that ghosted since Tuesday. See `funniest-excuse-candidates.md` for all candidates and the selection reasoning.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The program is deterministic: every run writes the same bytes to `/output/entry.txt`. It needs no network and no secrets.
