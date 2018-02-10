from nltk.corpus import wordnet

prime_index = ""
def get_synonyms(word):
    return wordnet.synsets(word)
def get_best_replacement(text_obj, sentence_no, word_no,word_raw):
    syn_shifts = dict()
    for syn in get_synonyms(word_raw):
        for lemma in syn.lemma_names():
            syn_shifts[lemma] = text_obj.get_shift(text_obj,sentence_no, word_no, lemma)
    for i in syn_shifts:
        print(i,syn_shifts[i])
    return reduce(lambda x,y: x if syn_shifts[x] > syn_shifts[y] else y, syn_shifts)

if __name__ == "__main__":
    print(get_synonyms("Devastation"))
