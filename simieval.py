# !/usr/bin/python
# -*- coding: utf-8 -*-


"""
create_author : Bilery Zoo(652645572@qq.com)
create_time   : 2017-06-01
program       : *_* evaluate the similarity between two files *_*
"""


import commands


def simieval(lf, rf):
    """
    UDF of evaluating the similarity between two files.
    Rely on "diff" handler on Linux platform.
    Default to ignore blanks by "-bB".
    :param lf: string
        File to diff at left.
    :param rf: string
        File to diff at right.
    :return: float
        Similarity ratio between two files.
    """
    le = float(commands.getoutput("diff -bB %s %s | awk 'BEGIN {cnt = 0}; /^[0-9]/ {cnt -= 1}; /^[<>]/ {cnt += 1}; END {print cnt}'" % (lf, rf)))
    re = float(commands.getoutput("nl %s %s | awk '{print $2}' | grep -v '^$' | wc -l" % (lf, rf)))
    result = 1 - le / re
    return result


if __name__ == "__main__":
    writer = "/home/student/"

    ll = """
    Ubuntu
    MySQL
    C
    JAVA
    Shell
    """
    wl = open(writer + "lf", 'w')
    wl.writelines(ll)
    wl.close()

    lr = """
    CentOS
    MySQL
    C
    Python
    """
    wr = open(writer + "rf", 'w')
    wr.writelines(lr)
    wr.close()

    se = simieval(lf=writer + "lf", rf=writer + "rf")
    print(se)
