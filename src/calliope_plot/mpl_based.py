import pandas as pd


def plot_stacked_bar(
    ax, df, x, y, fill, color_dict=None, stacked=False, width=0.8, rot=0, zorder=None
):
    r"""
    This function plots scalar data as grouped bar plot. The index of the DataFrame
    will be interpreted as groups (e.g. regions), the columns as different categories (e.g. energy
    carriers) within the groups which will be plotted in different colors.

    Parameters
    ----------
    ax: matplotlib Axes object
        Axes to draw the plot.
    df: pd.DataFrame
        DataFrame with an index defining the groups and columns defining the bars of different color
        with in the group.
    color_dict: dict
        Dictionary defining colors of the categories
    unit: str
        Unit of the variables
    stacked : boolean
        Stack bars of a group. False by default.
    """
    # apply EngFormatter if power is plotted
    # ax = plots._eng_format(ax, unit)

    _df = pd.pivot_table(df, values=y, index=x, columns=fill)

    color = None
    if color_dict is not None:
        color = [color_dict[key] for key in df.columns]

    _df.plot.bar(
        ax=ax,
        color=color,
        width=width,
        zorder=zorder,
        stacked=stacked,
        rot=rot,
    )

    return ax
