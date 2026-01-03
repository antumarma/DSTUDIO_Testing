import os
import pytest

os.makedirs("reports", exist_ok=True)

pytest.main([
    "test_contact.py",
    "-m", "sanity",
    "--html=reports/report.html",
    "--self-contained-html"
])
