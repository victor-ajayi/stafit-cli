import pytest
from handlers.average_gdp import generate


def test_single_file_returns_correct_headers(single_file):
    headers, rows = generate(single_file)
    assert headers == ["Country", "Average GDP"]


def test_single_file_multiple_countries_present(single_file):
    headers, rows = generate(single_file)
    assert len(rows) == 13


def test_single_file_united_states_average_gdp(single_file):
    headers, rows = generate(single_file)
    us_row = next(row for row in rows if row[0] == "United States")
    expected = (25462 + 23315 + 22994) / 3
    assert float(us_row[1]) == pytest.approx(expected)


def test_single_file_sorted_by_average_gdp_descending(single_file):
    headers, rows = generate(single_file)
    for i in range(len(rows) - 1):
        assert float(rows[i][1]) >= float(rows[i + 1][1])


def test_single_file_first_country_highest_gdp(single_file):
    headers, rows = generate(single_file)
    assert rows[0][0] == "United States"


def test_multiple_files_returns_correct_headers(multiple_files):
    headers, rows = generate(multiple_files)
    assert headers == ["Country", "Average GDP"]


def test_multiple_files_united_states_average(multiple_files):
    headers, rows = generate(multiple_files)
    us_row = next(row for row in rows if row[0] == "United States")
    assert us_row is not None
    assert isinstance(us_row[1], str)


def test_multiple_files_sorted_by_average_gdp_descending(multiple_files):
    headers, rows = generate(multiple_files)
    for i in range(len(rows) - 1):
        assert float(rows[i][1]) >= float(rows[i + 1][1])
