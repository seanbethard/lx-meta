class CorpusReader(object):

    def __iter__(self, txt):
        for line in open(txt):
            yield line
