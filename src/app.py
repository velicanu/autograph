import os
import tempfile

import pandas as pd
import plotly.express as px
import streamlit as st


def get_graphs(path):
    return sorted([v.replace(".md", "") for v in os.listdir(path) if v.endswith(".md")])


def df_from_md(filename):
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "out"), "w") as fout, open(filename) as fin:
            fout.write(fin.read().replace(" - ", ","))
        return pd.read_csv(os.path.join(tmpdir, "out"), sep=",")


def line(df, title):
    fig = px.line(df, x=df.columns[0], y=df.columns[1], title=title)
    st.plotly_chart(fig, use_container_width=True)


def plot(datadir, graph):
    df = df_from_md(os.path.join(datadir, graph + ".md"))
    if graph.endswith("-line"):
        line(df, graph.replace("-line", ""))


def main(datadir):
    default_graphs = st.query_params.get_all("graphs")
    graphs_ = get_graphs(datadir)
    print(default_graphs)

    graphs = st.multiselect(
        label="Graphs",
        options=graphs_,
        default=default_graphs
        if "graphs" not in st.session_state
        else st.session_state["graphs"],
        key="graphs",
    )
    st.query_params["graphs"] = graphs
    for graph in graphs:
        plot(datadir=datadir, graph=graph)

    return "done"


if __name__ == "__main__":
    main("data")
