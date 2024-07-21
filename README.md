# Source Radar

A tool to analyze source code and generate metrics.

## Features

- [x] Support for multiple languages
- [x] Centralized configuration
- [x] Add support for new languages using plugins

## Installation

We are working on a PyPI package, but for now you can install it using the following command:

Server:

```bash
$ pip install pip install -e "git+https://github.com/inputforge/source-radar#egg=source_radar&subdirectory=source_radar"
```

Client:

```bash
$ pip install pip install -e "git+https://github.com/inputforge/source-radar#egg=source_radar_client&subdirectory=source_radar_client"
```

## Usage

Create a configuration file in the root of your project like this:

```toml
server = "http://localhost:5000"
project = "source-radar"
linters = ["ruff"]
roots = [
    "source_radar",
    "source_radar_client",
]
```

Then run the following command:

```bash
$ source-radar analyze
```

This will analyze the source code and print the results.

To upload the results to the server, run the following command:

```bash
$ source-radar upload
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
