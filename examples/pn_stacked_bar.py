from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from calliope_plot.pn_based import plot_stacked_bar

HERE = Path(__file__).parent
df = pd.read_csv(HERE / "energy_cap.csv")

fig, ax = plt.subplots()
plot_stacked_bar(df, x="locs", y="energy_cap", fill="techs").save(
    HERE / "pn_plot_energy_cap.png"
)
