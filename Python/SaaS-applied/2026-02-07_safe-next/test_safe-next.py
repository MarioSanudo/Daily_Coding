import pytest
from solution_safe_next import is_safe_next

@pytest.mark.parametrize("next_url",
                         [("/dashboard"), ("/perfil?tab=1"), ("/"), ("/auth/login?next=/dashboard")])
def test_url_safe(next_url):
    assert is_safe_next(next_url) is True


@pytest.mark.parametrize("next_url",
                         [(None), (""), ("//evil.com"), ("https://evil.com"),("javascript:alert(1)"), ("/ok\nx"), ("/dashboard.com")])
def test_not_url_safe(next_url):
    assert is_safe_next(next_url) is False