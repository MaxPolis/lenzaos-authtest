import pytest

class TestAuthentication:
    def test_language_switch(self, auth):
        """Проверка переключения языка"""
        auth.switch_language("English (США)")
        assert "English" in auth.driver.page_source

    @pytest.mark.parametrize("email, is_valid", [
        ("test@test.com", True),
        ("invalid-email", False),
        ("", False)
    ])
    def test_email_validation(self, auth, email, is_valid):
        """Проверка валидации email"""
        result = auth.enter_email(email)
        assert (result.__class__.__name__ == "WorkspacePage") == is_valid