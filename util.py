def find_target_spans(words_to_be_searched, words_in_target_phrase):

    spans = []
    len_of_target_phrase = len(words_in_target_phrase)
    for i in range(len(words_to_be_searched)-len_of_target_phrase+1):
        if words_in_target_phrase == words_to_be_searched[i:i+len_of_target_phrase]:
            spans.append((i, i+len_of_target_phrase))

    return spans
