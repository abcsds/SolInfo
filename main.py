import json
import re

def analyze(f,scores,outfile):
    with open(f, mode="r",encoding=None, errors="ignore") as infile:
        data = infile.readlines()
        # data = json.loads(infile.read())
        # re.sub(r"[^\x00-\x7F]+"," ", data)

    of = open(outfile, mode="w")
    for line in data:
        folio = line.split(",")[0].replace("'","")
        descr = line.split(",")[6]

        words = descr.split(" ")
        descrScore = 0
        for word in words:
            if word in scores:
                descrScore += scores[word]
    #     if descrScore == 0:
    #         continue
    #     for word in words:
    #         if word in sentiments and word not in scores:
    #             sentiments[word] = int(sentiments[word])+descrScore
    #         elif word not in scores:
    #             sentiments[word] = descrScore
    # for key in sentiments:
    #     print(u" ".join((key, unicode(sentiments[key]))).encode("utf-8"))
        of.write(folio+","+str(round(descrScore,4))+";\n")
    of.close()


def main():
    scores = {} # initialize an empty dictionary
    # dates = [2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
    outfile = "results.txt"
    dates = [2014]
    extention = ".csv"
    files = ["solicitudes"+str(year)+extention for year in dates ]

    with open("meanAndStdev.csv", "r") as infile:
        # load sdal
        lines = infile.readlines()

    for line in lines:
        # create scores dictionary
        word, pleasure, activation, imagination, p_sdev, a_sdev, i_sdev = line.split(";")
        pleasure = float(pleasure) - 2
        word, obj = word.split("_")
        scores[word] = pleasure


    for f in files:
        analyze(f,scores,outfile)


if __name__ == "__main__":
    main()
