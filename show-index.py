# /// script
# requires-python = ">=3.12"
# dependencies = ["attridict>=0.0.9"]
# ///

import pprint

import tomllib
from attridict import AttriDict


def main() -> None:
    with open("pyproject.toml", "rb") as f:
        data = AttriDict(tomllib.load(f))

    index_data = data.tool.uv.index[0]
    pprint.pprint(index_data, indent=4, sort_dicts=False)

    index_url = index_data.get("url", "")
    index_default = index_data.get("default", False)

    if not index_url.startswith("http://localhost:3141/"):
        print(
            f"The devpi index has not been configured in pyproject.toml.\nurl={index_url}"
        )

    if not index_default:
        print("The devpi index is not the default index url.")


if __name__ == "__main__":
    main()
