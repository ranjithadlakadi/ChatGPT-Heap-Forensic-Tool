import json
import sys
from pathlib import Path

if len(sys.argv) < 3:
    print('Usage:')
    print('python recover_deleted_chat.py after_delete.heapsnapshot "FORENSIC_TEST_RANJITH_937461"')
    sys.exit(1)

snapshot_path = Path(sys.argv[1])
marker = sys.argv[2].lower()

print("[+] Loading heap snapshot...")
print("[+] This may take a little time because the file is large.")

with snapshot_path.open("r", encoding="utf-8") as f:
    heap = json.load(f)

strings = heap.get("strings", [])

print(f"[+] Loaded {len(strings):,} V8 strings")
print(f'[+] Searching for marker: "{marker}"')
print()

hits = []

for i, value in enumerate(strings):
    if not isinstance(value, str):
        continue

    if marker in value.lower():
        hits.append((i, value))

print("=" * 90)
print(f"DIRECT MATCHES: {len(hits)}")
print("=" * 90)

for idx, value in hits:
    print(f"\n[STRING INDEX {idx}]")
    print(value)

if not hits:
    print("\n[-] Marker was not found in the V8 string table.")
    sys.exit()

#
# Look around the matching strings in the V8 string table.
#
nearby = set()

WINDOW = 100

for idx, _ in hits:
    start = max(0, idx - WINDOW)
    end = min(len(strings), idx + WINDOW + 1)

    for n in range(start, end):
        value = strings[n]

        if not isinstance(value, str):
            continue

        value = value.strip()

        # Ignore tiny/internal-looking strings
        if len(value) < 12:
            continue

        nearby.add((n, value))

print()
print("=" * 90)
print("POSSIBLE NEARBY CONVERSATION STRINGS")
print("=" * 90)

for idx, value in sorted(nearby):
    # Limit extremely huge internal strings
    shown = value[:3000]

    print(f"\n[{idx}]")
    print(shown)

#
# Write everything to a text report
#
output = snapshot_path.parent / "recovered_deleted_chat.txt"

with output.open("w", encoding="utf-8") as out:

    out.write("DIRECT MATCHES\n")
    out.write("=" * 90 + "\n\n")

    for idx, value in hits:
        out.write(f"[STRING INDEX {idx}]\n")
        out.write(value + "\n\n")

    out.write("\n")
    out.write("POSSIBLE NEARBY STRINGS\n")
    out.write("=" * 90 + "\n\n")

    for idx, value in sorted(nearby):
        out.write(f"[{idx}]\n")
        out.write(value + "\n\n")

print()
print("=" * 90)
print("[+] FINISHED")
print(f"[+] Report written to:")
print(output)
print("=" * 90)