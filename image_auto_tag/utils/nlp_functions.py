import wikipedia
from nltk.corpus import wordnet as wn

#Category lists with no meaning
discard_tag_list = ['entity', 'object', 'whole', 'physical_entity','artifact','matter', 'substance', 'organism', 'natural_object', 'plant_organ', 'reproductive_structure','abstraction', 'attribute']


''' Function to find similar words using wikipedia API
    ##INPUT##
        tag -> single charecter
        categories -> categories list
        number -> Number of categories to return
    ##OUTPUT##
        categories list
'''
def wikiSearch(tag, categories, number = 2):
    if tag:
        terms = wikipedia.search(tag)
        for term in terms:
            if len(categories) < number:
                if term.replace(' ', '').lower() != tag.replace(' ', '').lower():
                    categories.append(term)
    return categories

    
''' Function to fetch the hypernyms using nltk wordnet
    ##INPUT##
        tags -> tags in array format
        number -> Number of categories to return
    ##OUTPUT##
        categories list
'''
def get_categories(tags, number = 2):
    categories = []
    for tag in tags:
        if len(categories) < number:
            try:
                word = wn.synsets(tag)[0]
                for path in word.hypernym_paths()[0]:
                    if len(categories) < number:
                        entity = path.name().split('.')[0]
                        if entity not in discard_tag_list:
                            if(entity.replace(' ', '').lower() != tag.replace(' ', '').lower()):
                                categories.append(entity)
                if len(categories) < number:
                    categories = wikiSearch(tag, categories, number)

            except IndexError:
                categories = wikiSearch(tag, categories, number)
            if tag:
                categories.append(tag)
        else:
            break
    return categories