
from collections import Counter

# change this to whatever the cutoff is for visitors
filterminimumcount = 20
filenametoparse = "ufwtest.log"
verbosemode = True


def main():
    ipaddresses = []
    with open(filenametoparse) as f:
        for line in f.readlines():
            ipaddress = [x.split(
                'SRC=')[1] for x in line.split(' ') if "SRC=" in x][0]
            # print(ipaddress[0])
            ipaddresses.append(ipaddress)

    # get the counts as a dict
    c = Counter(ipaddresses)

    # filter out to the top n
    filteredc = [el for el in c.items() if el[1] > filterminimumcount]

    # recreate nice dict out of it
    fixeddict = dict()
    for k, v in filteredc:
        fixeddict[k] = v

    # order by count desc
    sorteddict = dict(sorted(fixeddict.items(),
                             key=lambda x: x[1], reverse=True))

    # write to file
    with open("highestvisitors.txt", "w+") as f:
        if verbosemode:
            print("top visitor source ip addresses and visit count")
        for k, v in sorteddict.items():
            f.write(f"{k} {v} \n")
            if verbosemode:
                print(k, v)


if __name__ == "__main__":
    main()
