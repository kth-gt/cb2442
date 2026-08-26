import streamlit as st
import time

# Functions for helping us calculating alignments

match = 3
mismatch = -1
gap = -2

# A scoring function for two letters.
def match_score(letterA,letterB): # Score an individual alignment position
    if letterA == '-' and letterB == '-':
        return 0   # Irrelevant position, the alignments we generate have none
    elif letterA == '-' or letterB == '-':
        return gap  # Gap penalty
    elif letterA == letterB:
        return match   # Match
    else:
        return mismatch  # Mismatch

# A function that give a global alignmen scor of two gapped sequences.
def scoreSequences(a_seq,b_seq): # Score a alignment
    score, score_seq = 0, ""
    for a, b in zip(a_seq, b_seq):
        s = match_score(a, b)
        score += s
        score_seq += f"{s:<3}"  # left aligned, so it lines up under the letters
    return score, score_seq


# Generate every alignment of the two sequences, one column at a time. A column
# either pairs a letter from each sequence, or pairs a letter with a gap. We
# never emit a column with a gap in both sequences, and we stop as soon as both
# sequences are used up, so there are no unmatched gaps at the 3' end either.
def alignments(a_seq, b_seq):
    if not a_seq and not b_seq:
        yield "", ""
        return
    if a_seq and b_seq:                                # pair a letter from each
        for a, b in alignments(a_seq[1:], b_seq[1:]):
            yield a_seq[0] + a, b_seq[0] + b
    if a_seq:                                          # letter from A over a gap
        for a, b in alignments(a_seq[1:], b_seq):
            yield a_seq[0] + a, "-" + b
    if b_seq:                                          # gap over a letter from B
        for a, b in alignments(a_seq, b_seq[1:]):
            yield "-" + a, b_seq[0] + b


# How many alignments the generator above yields, without generating them. This
# is a Delannoy number: D(m,n) = D(m-1,n) + D(m,n-1) + D(m-1,n-1).
def countAlignments(m, n):
    row = [1] * (n + 1)
    for _ in range(m):
        next_row = [1]
        for j in range(1, n + 1):
            next_row.append(next_row[j-1] + row[j] + row[j-1])
        row = next_row
    return row[n]


# Utility function that spaces out a gapped sequence for display, padded to a
# fixed width so that the boxes keep their size as the alignments change length.
def showSeq(seq, width):
    return '  '.join(list(seq)).ljust(width)




# Streamlit code setting up a webform
st.set_page_config(layout="wide", page_icon="🎓", page_title="Naive Alignment Calculator")
st.title("🎓 Naive Alignment Calculator")

st.write(
    "This shows you a very naive way to calculate an optimal alignment"
)

left, mid, right = st.columns(3)

left.write("Fill in the two sequences you want to align:")

form = left.form("template_form")
a_seq = form.text_input("sequence A","CGA").strip().upper()
b_seq = form.text_input("sequence B","ACG").strip().upper()
match = form.number_input("match score", value = match, max_value = 9, min_value = -9)
mismatch = form.number_input("mismatch score", value = mismatch, max_value = 9, min_value = -9)
gap = form.number_input("gap penalty", value = gap, max_value = 9, min_value = -9)
delay = form.slider("seconds per alignment", 0.0, 1.0, 0.5, 0.05)
submit = form.form_submit_button("Calculate!")

# The widest alignment possible is one where no letters are paired at all.
display_width = (len(a_seq) + len(b_seq)) * 3

mid.subheader("Alignment being evaluated")
counter_box = mid.empty()
a_box, b_box, score_seq_box, score_box = mid.empty(), mid.empty(), mid.empty(), mid.empty()

right.subheader("Maximal alignment found so far")
m_counter_box = right.empty()
m_a_box, m_b_box, m_score_seq_box, m_score_box = right.empty(), right.empty(), right.empty(), right.empty()


if submit:
    # execute an excaustive alignment algorithm
    total = countAlignments(len(a_seq), len(b_seq))
    m = None
    # Loop over every alignment of the two sequences
    for n, (a, b) in enumerate(alignments(a_seq, b_seq), start = 1):
        # Update status text.
        counter_box.text(f"alignment {n} of {total}")
        a_box.text(showSeq(a, display_width))
        b_box.text(showSeq(b, display_width))
        # Calculate the score of the alignment
        score, score_seq = scoreSequences(a, b)
        # Output the score to the webform
        score_box.text(f"{score: >3}")
        score_seq_box.text(score_seq)

        # Update the best alignment if we found a better one.
        if m is None or score > m:
            m_counter_box.text(f"found at alignment {n}")
            m_a_box.text(showSeq(a, display_width))
            m_b_box.text(showSeq(b, display_width))
            m_score_seq_box.text(score_seq)
            m_score_box.text(f"{score: >3}")
            m = score
        # Slow us down a bit.
        time.sleep(delay)
    st.balloons()
