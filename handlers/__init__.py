"""Report handlers. Report name -> run(files) for each report type."""

from handlers import average_gdp

REPORTS = {
    "average-gdp": average_gdp.generate,
}
