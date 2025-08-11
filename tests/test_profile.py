import pytest

class TestProfile:
    def test_profile_setup(self, profile):
        """Проверка заполнения профиля"""
        profile.set_names("John", "Doe")
        assert "John Doe" in profile.driver.page_source

    def test_complete_flow(self, profile):
        """Проверка завершения регистрации"""
        profile.set_names("John", "Doe").complete_registration()
        assert "dashboard" in profile.driver.current_url