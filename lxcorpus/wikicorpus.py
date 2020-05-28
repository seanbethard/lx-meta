from multiprocessing.dummy import freeze_support
from gensim.test.utils import datapath, get_tmpfile
from gensim.corpora import WikiCorpus, MmCorpus


def main(path_to_wiki_dump):
    wiki_dump = datapath(path_to_wiki_dump)
    corpus_path = get_tmpfile("wiki-corpus.mm")
    wiki = WikiCorpus(wiki_dump)
    MmCorpus.serialize(corpus_path, wiki)


if __name__ == '__main__':
    freeze_support()
    import plac; plac.call(main)
