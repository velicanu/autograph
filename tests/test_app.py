import os

from app import df_from_md, get_graphs, main

script_dir = os.path.dirname(os.path.realpath(__file__))
examples_dir = os.path.join(script_dir, "../examples")


def test_main():
    expected = "done"
    actual = main(examples_dir)
    assert actual == expected


def test_df_from_md():
    expected = {
        "date": {0: "2023-11-23", 1: "2023-12-14", 2: "2023-12-26", 3: "2024-01-23"},
        "height": {0: 52.5, 1: 53.3, 2: 55.2, 3: 59.7},
    }
    actual = df_from_md(os.path.join(examples_dir, "example-line.md")).to_dict()
    assert actual == expected


def test_get_graphs():
    expected = ["example-line"]
    actual = get_graphs(examples_dir)
    assert actual == expected
