"""
@Author: Abhishek P
Date: 17/08/17
Readability Scores using the text stats
Built as part of ReadabilityScores


Indices to be calculated:
1. Flei
"""
SCORES = {"fk", "dc", "gf", "cl"}

# flesch-kincaid https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
def flesch_kincaid_score(stats):
    return 0.39 * (stats["word_count"]/stats["sentence_count"]) \
           + 11.8 * (stats["syllable_count"]/stats["word_count"]) - 15.59


# dale-chall https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formulas
def dale_chall_score(stats):
    return 0.1579 * ( ( stats["complex_words"] / stats["word_count"] ) * 100 ) \
            + 0.0496 * (stats["word_count"]/stats["sentence_count"])


def gunning_fog_score(stats):
    return 0.4 * ((stats["word_count"] / stats["sentence_count"])\
                   + 100 * (stats["complex_words"] / stats["word_count"]))


#def smog_score(stats):
#    return 1.0430 * (stats["complex_words"]) * (30)


def coleman_liau_score(stats):
    L = (stats["letter_count"]/stats["word_count"]) * 100
    S = (stats["sentence_count"]/stats["word_count"]) * 100
    return 0.0588 * L - 0.296 * S - 15.8


def automated_score(stats):
    return 4.71 * (stats["letter_count"] / stats["word_count"] ) + 0.5 * (stats["word_count"] / stats["sentence_count"]) - 21.43

