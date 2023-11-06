from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from calliope_plot.mpl_based import plot_stacked_bar

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "energy_cap.csv")

fig, ax = plt.subplots()
plot_stacked_bar(ax, df, x="locs", y="energy_cap", fill="techs", stacked=True)
plt.savefig(HERE / "mpl_plot_energy_cap.png")
