import streamlit as st
import numpy as np
import time
import sys
import itertools

# Functions for helping us calculating alignments

match = 3
mismatch = -1
gap = -2


def match_score(letterA,letterB): # Score an individual alignment position
    if letterA == '-' and letterB == '-':
        return 0   # Irrelevant position
    elif letterA == '-' or letterB == '-':
        return gap  # Gap penalty
    elif letterA == letterB:
        return match   # Match
    else:
        return mismatch  # Mismatch

def scoreSequences(a_seq,b_seq): # Score a alignment
    score, score_seq = 0, ""
    for a, b in zip(a_seq, b_seq):
        s = match_score(a, b)
        score += s
        score_seq += f"{s:3}"
    return score, score_seq

def getSeq(seq, inserts, alignment_length):
    out = ""
    for i,s in zip(inserts,seq):
        out += '-'*i
        out += s
    out += '-'*(alignment_length-len(out))
    return out




st.set_page_config(layout="wide", page_icon="🎓", page_title="Naive Alignment Calculator")
st.title("🎓 Naive Alignment Calculator")

st.write(
    "This shows you a very naive way to calculate an optimal alignment"
)

left, mid, right = st.columns(3)

left.write("Fill in the two sequences you want to align:")
mid.write("Calculations:")
right.write("Optimal Alignment:")

form = left.form("template_form")
a_seq = form.text_input("sequence A","CGA")
b_seq = form.text_input("sequence B","ACG")
match = form.number_input("match score", value = match, max_value = 9, min_value = -9)
mismatch = form.number_input("mismatch score", value = mismatch, max_value = 9, min_value = -9)
gap = form.number_input("gap penalty", value = gap, max_value = 9, min_value = -9)
submit = form.form_submit_button("Calculate!")

alignment_length = max(len(a_seq),len(b_seq))**2


a_box, b_box, score_seq_box, score_box = mid.empty(), mid.empty(), mid.empty(), mid.empty()
m_a_box, m_b_box, m_score_seq_box, m_score_box = right.empty(), right.empty(), right.empty(), right.empty()


if submit:
    m = - sys.maxsize
    for a_inserts in itertools.product(list(range(len(a_seq))), repeat = len(a_seq)):
        a = getSeq(a_seq, a_inserts, alignment_length)
        a_box.text('  '.join(list(a)))
        for b_inserts in itertools.product(list(range(len(b_seq))),repeat = len(b_seq)):
            b = getSeq(b_seq,b_inserts, alignment_length)
            # Update status text.
            b_box.text('  '.join(list(b)))
            score, score_seq = scoreSequences(a, b)
            score_box.text(f"{score: >3}")
            score_seq_box.text(score_seq)

            if score > m:
                m_a_box.text('  '.join(list(a)))
                m_b_box.text('  '.join(list(b)))
                m_score_seq_box.text(score_seq)
                m_score_box.text(f"{score}")
                m = score
            # Slow us down a bit.
            time.sleep(.5)            
    st.balloons()
