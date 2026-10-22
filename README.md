# ChatGPT-Heap-Forensic-Tool
ChatGPT Deleted Chat Forensics POC | Browser Heap Snapshot Analysis Using Python

A Python-based proof of concept (POC) for examining Chrome/Chromium JavaScript heap snapshots to check whether a unique marker and related text remain in browser memory after a ChatGPT conversation is deleted.

**Purpose:** Demonstrate browser-memory forensics in a controlled lab environment for educational purposes.

## How It Works

1. Create a ChatGPT conversation containing a unique test keyword.
2. Delete the test conversation while keeping the browser session open.
3. Capture a JavaScript heap snapshot using Chrome DevTools.
4. Run the Python recovery script to search the snapshot for the test keyword.
5. Generate a text report containing matching and potentially related strings.
6. Convert the text report into an HTML page for easier viewing.

**Note:** Results depend on what remains in the captured snapshot. Recovery of the complete deleted conversation is not guaranteed.

## Requirements

- Windows, macOS, or Linux computer
- Google Chrome or a compatible Chromium-based browser
- Python 3
- The two Python scripts provided in this repository

The scripts use Python's standard library. No additional Python packages are required for the supplied code.

## Step 1: Install Python

If Python 3 is not installed, download it from:

https://www.python.org/downloads/

On Windows, select **Add Python to PATH** during installation.

Verify the installation by opening Command Prompt or a terminal and running:

```bash
python --version
```

If your system uses `python3`, use that command instead.

## Step 2: Download the Repository

Download or clone this repository and extract it into a folder.

The folder should contain these two scripts:

```text
ChatGPT-Heap-Forensic-Tool/
├── recover_deleted_chat.py
└── view_recovered.py
```

## Step 3: Create a Test Conversation

1. Open ChatGPT in Chrome.
2. Create a test conversation using harmless sample content.
3. Include a unique keyword or marker, for example:

   `FORENSIC_TEST_RANJITH_937461`

4. Keep the browser session open.
5. Delete the test conversation.

Use only your own test account and non-sensitive sample data.

## Step 4: Capture the Browser Heap Snapshot

1. Do not refresh the page or close the browser during the experiment.
2. Right-click the page and select **Inspect**, or press `Ctrl + Shift + I` on Windows.
3. Open the **Memory** tab in Chrome DevTools.
4. Select **Heap snapshot** as the profiling type.
5. Click **Take snapshot**.
6. Wait for the snapshot to finish loading.
7. Save or export the snapshot as a `.heapsnapshot` file, if available in your DevTools workflow.

Save the snapshot in the same folder as the two Python scripts.

Your folder should now contain three files:

```text
ChatGPT-Heap-Forensic-Tool/
├── recover_deleted_chat.py
├── view_recovered.py
└── after_delete.heapsnapshot
```

The snapshot filename can be different, but you must use the actual filename in the next command.

## Step 5: Run the Recovery Script

Open Command Prompt or a terminal in the project folder.

For Windows, you can open the folder in File Explorer, click the address bar, type `cmd`, and press Enter.

Run:

```bash
python recover_deleted_chat.py after_delete.heapsnapshot "FORENSIC_TEST_RANJITH_937461"
```

Replace the example marker with the exact keyword used in your test conversation.

The script will:

- Load the heap snapshot.
- Search the snapshot's V8 string table for the marker.
- Display direct matches and potentially related nearby strings.
- Generate a text report named `recovered_deleted_chat.txt`.

If the marker is not found, the script will report that no direct match was found.

## Step 6: View the Results in HTML

After the recovery script finishes, run:

```bash
python view_recovered.py
```

The script will create:

```text
recovered_chat_view.html
```

Open this HTML file in your browser to inspect the generated report in a more readable format.

## Troubleshooting

| Issue | What to do |
|---|---|
| Python is not recognized | Install Python 3 or check your PATH. |
| Snapshot file not found | Check the filename and ensure the snapshot is in the project folder. |
| Marker not found | Verify the marker and check whether the relevant text remains in the snapshot. |
| Text report not found | Run the recovery script successfully before running the HTML viewer. |
| Results contain unrelated strings | The script collects nearby string-table entries; they are not necessarily part of the same conversation. |

## Important Limitations

- This is an experimental proof of concept, not a guaranteed deleted-chat recovery tool.
- A heap snapshot captures JavaScript memory at a particular point in time; it does not capture every piece of browser or server data.
- The script searches the snapshot's string table and nearby entries. It does not reconstruct the original conversation structure or verify every question-and-answer pair.
- Refreshing or closing the browser may change the available in-memory data, but neither action guarantees that all relevant data is erased.
- Finding a marker in a snapshot does not prove that a deleted conversation can be restored through ChatGPT.
- Heap snapshots can contain sensitive information. Keep them private, and do not upload real conversation data or snapshots to a public repository.

## POC Demo Video

A short demonstration video is available alongside this repository to show the workflow from creating a test conversation to examining the generated report.

## Disclaimer

This project is intended for educational purposes and authorized testing on your own browser session and test data. It demonstrates examining browser memory and does not bypass ChatGPT account authentication or guarantee recovery of deleted conversations.

## Credits & Inspiration

This project was inspired by [ChatGPT-V8-Heap-Forensics](https://github.com/jihunjoun/ChatGPT-V8-Heap-Forensics), created by **Jihun Joun**.

I explored the original project and its approach to analyzing Chrome V8 heap snapshots for ChatGPT conversation artifacts. Based on that inspiration, I developed this simplified proof of concept with a marker-based Python search workflow and an HTML report viewer to make the demonstration easier for beginners to follow.

The original repository served as the inspiration for this project. Please refer to the original repository for its implementation, research, and licensing details.

**Original project:** https://github.com/jihunjoun/ChatGPT-V8-Heap-Forensics

Thank you to Jihun Joun for sharing this work and contributing to research in browser-memory forensics.
