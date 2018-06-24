# pip install spacy
# python -m spacy download en_core_web_sm

import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('pt_core_news_sm')

# Process whole documents
# text = (u"When Rodrigo Thrun started working on self-driving cars at "
#         u"Google in 2007, few people outside of the company took him "
#         u"seriously. “I can tell you very senior CEOs of major American "
#         u"car companies would shake my hand and turn away because I wasn’t "
#         u"worth talking to,” said Thrun, now the co-founder and CEO of "
#         u"online higher education startup Udacity, in an interview with "
#         u"Recode earlier this week.")

# text = (u"Quando Rodrigo Cipriani da começou a trabalhar como motorista no "
#         u"Banco do Brasil em 2008, algumas pessoas de fora falaram para ele "
#         u"seriamente. “Eu posso falar para você que muitos seniors CEOs dos maiores "
#         u"bancos poderiam apartar minha mão e ir embora porque eu não "
#         u"vou falar com eles,” disse rodrigo, agora co-fundador e CEO da "
#         u"empresa de fidelização, chamada Fidello, em uma entrevista com  "
#         u"Globo semanas atrás.")
# doc = nlp(text)

# Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)

# Determine semantic similarities
intent1 = nlp(u"Problema com ar condicionado")
intent2 = nlp(u"ar condicionado falhando")
intent3 = nlp(u"meu ar condicionado está ruim")
intent4 = nlp(u"arrumar meu ar condicionado")
intent5 = nlp(u"comprar novo ar condicionado")
intent6 = nlp(u"a temperatura da agência está alta")
intent7 = nlp(u"falha no piso")
busca = nlp(u"falha no ar condicionado")

intents = [intent1, intent2, intent3, intent4, intent5, intent6, intent7]

for entity in intent6.ents:
    print(entity.text, entity.label_)


# for intent in intents:
#     print(intent, " - ", intent.similarity(busca))

# similarity = doc1.similarity(doc2)
# print(doc1.text, doc2.text, similarity)