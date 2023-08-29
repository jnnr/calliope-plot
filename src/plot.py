import plotnine as pn


def get_tidy_data(model, coefficient):
    r"""
    Get data from a model and format it for plotting.
    """
    data = (
        model.get_formatted_array(coefficient, index_format="multiindex")
        .to_dataframe()
        .reset_index()
    )

    return data


def aggregate(data, to_aggregate, values):
    r"""
    Aggregate data by summing over `to_aggregate`.
    """
    # TODO: How to handle transmission?
    if isinstance(to_aggregate, str):
        to_aggregate = [to_aggregate]

    groupby = list(data.columns)
    groupby.remove(values)

    for column in to_aggregate:
        groupby.remove(column)

    return data.groupby(groupby, sort=False).sum().reset_index()


def normalize(data, by, method="max", where=None):
    _data = data.copy()

    if method == "max":
        normalizing_factor = _data[by].max()
    elif method == "sum":
        normalizing_factor = _data[by].sum()
    else:
        raise ValueError(f"'method' must be either 'max' or 'sum', but is {method}")

    if not where:
        where = by

    # TODO: Normalize all data, or only column coefficecient?
    _data[where] = _data[where] / normalizing_factor

    return _data


def prepare_load_duration(data, sort_by):
    # TODO: Generalize assertion
    for column in ["timesteps", "techs", "locs", sort_by]:
        assert column in data.columns
    _data = data.copy()
    _data = _data.drop(columns=["timesteps"])
    _data = _data.groupby(["locs", "techs"], sort=False).apply(
        lambda x: x.sort_values(sort_by, ascending=False).reset_index(drop=True)
    )
    _data = _data.droplevel(level=["locs", "techs"], axis=0)
    return _data


def plot_dispatch(data, facet=None):
    # TODO: Handle optional features
    return (
        pn.ggplot(data, pn.aes(x="timesteps", y="resource_con", fill="techs"))
        + pn.geom_area(position="stack")
        # + pn.facet_wrap("locs", nrow=3) if facet
        + pn.theme_minimal()
    )


def plot_load_duration(data):
    return (
        pn.ggplot(data, pn.aes(x=data.index, y="resource_con", fill="techs"))
        + pn.geom_area(position="stack")
        + pn.theme_minimal()
        + pn.labs(x="Sorted timesteps", y="Resource con", title="Load duration curve")
    )


def plot_map(model):
    raise NotImplementedError


def plot_simple_map(coordinates):
    r"""
    Takes coordinate data containing location names and lat, lon and plots a simple map of the coordinates as dots on a map
    """
    return (
        pn.ggplot(coordinates, pn.aes(x="lon", y="lat"))
        + pn.geom_point()
        + pn.coord_fixed()
        + pn.theme_minimal()
    )
