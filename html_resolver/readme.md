

# HTML Resolver

HTML Resolver is a **line-based HTML placeholder resolver**.

It replaces specific lines in an HTML file with user-provided content, based on a **very simple and strict rule**.

---

## How it works (actual logic)

* The resolver reads the HTML file **line by line**
* **Only lines whose FIRST character is `{` are considered**
* From those lines, placeholders of the form `{{key.work}}` are extracted
* The rest of the HTML is untouched

That’s it.
No DOM parsing. No regex madness. No guessing.

---

## Placeholder rule (THIS IS IMPORTANT)

### ✅ Condition to be detected

* The **first column of the line must start with `{`**

If this condition is met, the line is captured.

### Placeholder format used inside the line

```html
{{key.work}}
```

* `.` is mandatory
* `key.work` is used for grouping and selection
* The placeholder line is later **fully replaced**

---

### ✅ Valid example

```html
<p>
{{identify.replacer}}
</p>
```

Here:

* Line starts with `{` → detected
* `identify.replacer` → extracted

---

### ❌ Invalid examples

```html
<p>{{identify.replacer}}</p>   // first column is `<`, ignored
 text {{a.b}}                  // first column is space, ignored
{{key}}                        // dot missing, ignored
```

---

## Replacement behavior

* When a placeholder is selected and replaced:

  * the **entire line** containing `{{key.work}}` is replaced
  * the placeholder is removed from the available list
* Replacement happens **in memory**
* Final output is written only when the user saves

---

## information.txt format (strict)

The optional info file must follow this format:

```text
key.work{information}
```

Rules:

* `key.work` must start at **first column**
* Must exactly match the HTML placeholder (without `{{ }}`)
* Information must be inside `{}`

### Example

```text
identify.replacer{Main identification block}
user.name{User full name}
```

---

## What this tool does NOT do

* ❌ Inline replacements
* ❌ HTML parsing
* ❌ Regex-based guessing
* ❌ Partial line edits

It only replaces **whole lines** whose first character is `{`.

---

## Why it’s built this way

* Predictable behavior
* Zero ambiguity
* Easy to debug
* No accidental replacements

If the format is wrong → the tool ignores it.
That’s intentional.

---

## Distribution

* Packaged as **Linux AppImage**
* Single executable
* No installation required

---

## Author

**Pawan (INTRIXLABS)**

---

