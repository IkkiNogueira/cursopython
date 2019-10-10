def count():
    from math import sqrt
    for x in range(10**5):
        sqrt(x)

if __name__ == '__main__':
    import cProfile, pstats
    cProfile.run("count()", '{}.profile'.format(__file__))
    s = pstats.Stats('{}.profile'.format(__file__))
    s.strip_dirs()
    s.sort_stats("time").print_stats(10)
