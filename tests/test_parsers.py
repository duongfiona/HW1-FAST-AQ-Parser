# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/blank.fa
    """
    # testing that example Fasta is properly read
    ex_file = "data/test.fa"
    parser = FastaParser(ex_file)
    sequences = list(parser)
    assert len(sequences) > 0
    assert all(isinstance(seq, tuple) and len(seq)==2 for seq in sequences)

    # testing that parser throws ValueError with blank fasta file
    with pytest.raises(ValueError):
        blank_parser = FastaParser("tests/blank.fa")
        list(blank_parser)

    # testing that parser throws ValueError with bad fasta file
    with pytest.raises(ValueError):
        bad_parser = FastaParser("tests/bad.fa")
        list(bad_parser)


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # testing that fasta files is being read in
    ex_file = "data/test.fa"
    parser = FastaParser(ex_file)
    sequences = list(parser)
    
    assert all(seq[0] is not None for seq in sequences)

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # testing that example Fastq is properly read
    ex_file = "data/test.fq"
    parser = FastqParser(ex_file)
    sequences = list(parser)

    assert len(sequences) > 0
    assert all(isinstance(seq, tuple) and len(seq)==3 for seq in sequences)

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # testing that fastq file is being read in
    ex_file = "data/test.fq"
    parser = FastqParser(ex_file)
    sequences = list(parser)

    assert all(seq[0] is not None for seq in sequences)