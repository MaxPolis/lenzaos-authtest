import pytest

class TestWorkspace:
    def test_workspace_creation(self, workspace):
        """Проверка создания workspace"""
        workspace.set_workspace_name("TestCompany")
        assert "TestCompany" in workspace.driver.page_source

    def test_name_validation(self, workspace):
        """Проверка валидации имени"""
        workspace.set_workspace_name("A")
        assert "Минимум 2 символа" in workspace.driver.page_source