from django.test import TestCase
# from itertools import chain
# from nltk.tokenize import word_tokenize
# from nltk import pos_tag

# import nltk
# # nltk.download('wordnet')
# # nltk.download('punkt')
# # nltk.download('averaged_perceptron_tagger')
# # from nltk.corpus import wordnet as wn
# # # is_noun = lambda pos: pos[:2] == 'NN'
# # # words = []
# # # synt = 'game of thrones'
# # # words = word_tokenize(synt)
# # # print(words)
# # # syn_sets = [wn.synsets(token) for token in words]
# # # split_syn_sets = [(syn_set.lemma_names(), syn_set.hyponyms()) for syn_set in syn_sets]
# # # print(split_syn_sets)


# # # print([word for (word, pos) in nltk.pos_tag(words) if is_noun(pos)])
# # # Create your tests here.
# # vehicle = wn.synsets("Titanic")
# # # vehicle = wn.synsets('game of thrones')
# # print(vehicle)
# # typesOfVehicles = list(set([w for s in vehicle[0].closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))
# # #     # print('Meaning', i, 'NLTK ID', j.name())
# # #     # print('Definition:', j.definition())
# # print(typesOfVehicles)

# from nltk import Tree
# from nltk import ne_chunk, pos_tag, word_tokenize
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# def get_continuous_chunks(text, chunk_func=ne_chunk):
#     chunked = chunk_func(pos_tag(word_tokenize(text)))
#     continuous_chunk = []
#     current_chunk = []

#     for subtree in chunked:
#         if type(subtree) == Tree:
#             current_chunk.append(" ".join([token for token, pos in subtree.leaves()]))
#         elif current_chunk:
#             named_entity = " ".join(current_chunk)
#             if named_entity not in continuous_chunk:
#                 continuous_chunk.append(named_entity)
#                 current_chunk = []
#         else:
#             continue

#     return continuous_chunk


# text = 'Scarlett Johansson is an American actress.'
# print(get_continuous_chunks(text))




