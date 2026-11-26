"""V94 Fixed Bug Where Brain: one-line entry for make.fun.

The program writes exactly one line - the drafted winning line for the 'Fix Human Sleep: Funniest Patch Note' bounty - to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 108 UTF-8 characters, inside the 1-200 gate.
"""
import os

LINE = 'v9.4: fixed bug where brain replays embarrassing 2014 conversation at 2 a.m. instead of entering sleep mode.'

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
