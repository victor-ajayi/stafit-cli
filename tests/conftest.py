from pathlib import Path

import pytest

DATA_DIR = Path(__file__).parent.parent / "data"


@pytest.fixture
def single_file() -> list[Path]:
    return [DATA_DIR / "economic1.csv"]


@pytest.fixture
def multiple_files() -> list[Path]:
    return [DATA_DIR / "economic1.csv", DATA_DIR / "economic2.csv"]
