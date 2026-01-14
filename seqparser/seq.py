# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # raise ValueError if input seq contains anything besides A, C, T, G
    if not all(base in ALLOWED_NUC for base in seq):
        raise ValueError("Input sequence string contains invalid nucleotides")

    # iteratively transcribe input seq using TRANSCRIPTION_MAPPING dict
    transcript = ""
    for base in seq:
        transcript += TRANSCRIPTION_MAPPING[base]

    # if reverse=True, reverse the order of complement transcript
    if reverse:
        transcript = transcript[::-1]

    return transcript

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, reverse=True)