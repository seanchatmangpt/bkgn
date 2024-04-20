# conftest.py
import dspy
import pytest
from typer.testing import CliRunner
from dspygen.utils.dspy_tools import init_dspy
from bookmaker_cli_typer import app

@pytest.fixture(scope="module")
def dummy_lm():
    dummy_responses = [
        "Fantasy Book Title",
        "Fantasy Chapter Prompt",
        "7",
        "Fantasy Author Name",
        "Fantasy Author Bio",
        "Evaluation Rubric Title",
        "Criteria 1, Criteria 2, Criteria 3",
        "Non-fiction Book Title",
        "Mystery Book Title",
        "Updated Mystery Book Title",
        "10",
        "Science Fiction Book Title",
        "Romance Book Title",
        "Thriller Book Title",
    ]
    return DummyLM(answers=dummy_responses)

@pytest.fixture(scope="function", autouse=True)
def init_dspy_with_dummy_lm(dummy_lm):
    init_dspy(lm_instance=dummy_lm)

@pytest.fixture(scope="module")
def runner():
    return CliRunner()