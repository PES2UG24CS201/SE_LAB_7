from hypothesis import given, strategies as st
from library_fines import parse_member_id, total_fine, shelf_code


@given(st.text() | st.none())
def test_parse_member_id_no_crash(s):
    try:
        result = parse_member_id(s)
    except Exception as e:
        assert False, f"parse_member_id crashed with: {type(e).__name__}: {e}"
    assert result is None or (
        isinstance(result, tuple) and isinstance(result[0], str) and isinstance(result[1], int)
    )


@given(st.text() | st.none())
def test_total_fine_no_crash(s):
    try:
        result = total_fine(s)
    except Exception as e:
        assert False, f"total_fine crashed with: {type(e).__name__}: {e}"
    assert isinstance(result, int) and result >= 0


@given(st.text() | st.none())
def test_shelf_code_no_crash(s):
    try:
        result = shelf_code(s)
    except Exception as e:
        assert False, f"shelf_code crashed with: {type(e).__name__}: {e}"
    assert result is None or isinstance(result, str)
