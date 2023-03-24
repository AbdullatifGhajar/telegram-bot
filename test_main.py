import pytest

from main import execute_text

given = pytest.mark.parametrize


@given(
    "message, expected_result",
   [ 
        ("", "ERROR: no text is provided"),
        ("print(1 + 1)", "2"),
        ("a, b = 1, 2\nprint(a + b)", "3"),
        ("print(1/0)", "ERROR: division by zero"),
    ]
)
def test_execute_text(text: str, expected_result: str):
    # get a clean string, e.g. replace \n with newline character
    text = text.replace(r"\\n", "\n")
    assert execute_text(text).strip() == expected_result
