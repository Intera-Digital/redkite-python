"""Command-line entry point for `python -m redkite`."""

from redkite import __version__


def main() -> None:
    """Print the installed Redkite package version."""
    print(f"Redkite {__version__}")


if __name__ == "__main__":
    main()
