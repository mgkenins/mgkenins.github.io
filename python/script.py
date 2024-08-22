import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


def transform(axis, axis2, val, offset, scale):
    return offset + (val - scale) * (axis2.get_ylim()[1] - axis2.get_ylim()[0]) / (axis.get_ylim()[1] - axis.get_ylim()[0])



def plot_data(data:list[tuple[str,str,float,int]]) -> None:
    dates = []
    scores = []
    impdates = []
    impscores = []
    for tuple in data:
        if tuple[1] == "m":
            dates.append(dt.datetime.strptime(tuple[0], "%d%m%Y").date())
            scores.append(tuple[2])
        elif tuple[1] == "i":
            impdates.append(dt.datetime.strptime(tuple[0], "%d%m%Y").date())
            impscores.append(tuple[2])
        else:
            raise ValueError(f"Wrong scoring type formatting for {tuple}")

    fig, ax = plt.subplots(1,1,constrained_layout=True)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
    ax.scatter(
            dates,
            scores,
            s=75,
            c='b',
            marker='o',
            label="MP"
            )

    ax.vlines(dates, ymin=50, ymax=scores, color='b', linestyle='-')
    ax2 = ax.twinx()
    ax2.scatter(
            impdates,
            impscores,
            s=75,
            c='r',
            marker='o',
            label="IMP"
            )
    ax2.vlines(impdates, ymin=0, ymax=impscores, color='r', linestyle='-')
    
    ax.axhline(y=50, color='black', linewidth=2)
    ax.set_ylim(40, 70)
    ax2.set_ylim(-10, 20)

    ax.set_ylabel(r"%, MP scoring")
    ax2.set_ylabel(r"IMPs, IMP scoring")

    handles, labels = ax.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()

    handles.extend(handles2)
    labels.extend(labels2)

    ax.legend(handles, labels, loc='lower left')


    fig.autofmt_xdate()

    fig.tight_layout()
    fig.savefig("bridge-data.pdf")
    fig.savefig("bridge-data.svg", dpi=2000)




DATA = [
        #day, month, year, scoring (mp "m", imp "i"), % or imps, rank
        ("16072024","m",66.56,1330),
        ("17072024","i",17.18,1981),
        ("09082024","m",54.52,7677),
        ("11082024","m",54.84,6617),
        ("14082024","i",3.04,8669),
        ("15082024","m",64.25,1988),
        ("20082024","m",54.25,7444),
        ("21082024","i",14.79,2713),
        ]



if __name__ == "__main__":
    date = dt.datetime.strptime(DATA[0][0], "%d%m%Y")
    plot_data(DATA)








