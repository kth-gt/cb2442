# General course information

## Editing the schedule

`schedule.md` is the source; **`schedule.html` is generated from it — never edit
the HTML by hand**, your changes will be overwritten.

To make a change:

1. Edit `schedule.md`.
2. Run `./md2html.sh schedule.md` (needs `pandoc`, `sudo apt install pandoc`).
3. Commit both files.

The colours come from the `<oth>`, `<ali>`, `<sf>`, `<phyl>` and `<cncl>` tags
and the `<style>` block at the top of `schedule.md`; the conversion passes them
through untouched.

## Room lists for the labs

The KTH Social calendar truncates the list of computer rooms ("Grå, Grön,
Karmosin, …"). The full list is in the TimeEdit feed for the course, or by
clicking the "…" on a lab in the KTH Social calendar.
