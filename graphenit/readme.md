
thre's no appimage - due to size and issue - so there's link of direct appimage (mediafire): https://www.mediafire.com/file/p9s5drgm147kyev/Graphenit.appimage/file
---

# Graphenit

> A quiet graph-making tool for people who just want a graph —
> not an ecosystem, not an account, not a headache.

---

## What is Graphenit?

**Graphenit** is a lightweight desktop application for creating clean bar graphs from simple name–value data.

It’s built for:

* students
* researchers
* teachers
* anyone who just wants a graph **without ads, accounts, or complexity**

No dashboards.
No cloud.
No subscriptions.
No “AI magic”.

Just:

> **Input → Preview → Save**

---

## Why Graphenit exists

Most graph tools today are either:

* **too simple** (online sites with ads and limits), or
* **too heavy** (developer tools meant for programmers, not people)

Graphenit sits in between.

It respects two things:

1. **Human focus** (simple UI, readable output)
2. **Context** (dark/light mode for working, clean exports for sharing)

It doesn’t try to impress — it tries to be useful.

---

## Core Philosophy

* **One job, done well**
* **Local-first** (no internet required)
* **Predictable behavior**
* **No hidden state**
* **No forced opinions**

If something is slow, it’s honest about it.
If something is wrong, it shows it clearly.

---

## Features

* 📊 Bar graph creation from names and values
* 👀 Live preview before saving
* 🌗 Light & Dark UI modes
* 🎨 Separate export styling (UI ≠ output)
* 🖼️ High-quality image export (PNG)
* 💾 Fully offline
* 🧠 Minimal memory usage (~60–80 MB at runtime)
* 🧩 No external dependencies at runtime (AppImage)
* 4k image output

---

## What Graphenit is *not*

* ❌ Not a spreadsheet
* ❌ Not a statistics suite
* ❌ Not a plotting framework
* ❌ Not a cloud service
* ❌ Not a “low-code platform”

Graphenit doesn’t try to solve everything.
That’s why it works.

---

## Requirements

### To run (AppImage)

* Linux (most distributions)
* 4 GB RAM recommended (runs on less)
* No Python required
* No internet required

### To develop

* Python 3.9+
* `customtkinter`
* `matplotlib`
* `numpy`

---

## Installation

### Using AppImage

1. Download the AppImage
2. Make it executable:

   ```bash
   chmod +x Graphenit.appimage
   ```
3. Run it:

   ```bash
   ./Graphenit.appimage
   ```

That’s it.

---

## Usage

1. Enter **names** (labels)
2. Enter **values** (numbers)
3. Click **Preview**
4. Adjust if needed
5. Click **Save**

If something doesn’t match, Graphenit tells you.
It doesn’t guess.

---

## Design Decisions (intentional)

* **Matplotlib backend** for correctness and reliability
* **CustomTkinter** for readable UI
* **No autosave** (explicit user intent matters)
* **No silent coercion** (numbers must be numbers)
* **Separate UI/export themes** (comfort ≠ output)

These are not accidents.

---

## Performance Notes

* Startup may take a moment on older systems (Python + matplotlib initialization)
* Runtime performance is stable and low-memory
* No background processes
* No telemetry
* No tracking

Once open, it stays out of your way.

---

## Who this is for

You’ll like Graphenit if you:

* hate ads
* hate accounts
* hate web tools for simple tasks
* want something that just works
* value clarity over cleverness

You won’t like it if you want:

* animations
* dashboards
* AI-generated charts
* automation pipelines

That’s fine.

---

## License

Graphenit is built to be **used**, not trapped.

(Choose your license here — MIT / GPL / etc.)

---

## Final note

Graphenit was built because sometimes the best software is the one that:

> doesn’t ask for attention
> doesn’t collect data
> doesn’t try to be smarter than you

It just does the job — and lets you move on.

---


