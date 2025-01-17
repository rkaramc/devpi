# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import tomllib


def main() -> None:
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    section_data = data["tool"]["uv"]["index"]
    print(section_data)


if __name__ == "__main__":
    main()
