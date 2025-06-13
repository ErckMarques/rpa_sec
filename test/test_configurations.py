import os
import pytest
from src.core import settings

def test_default_config():
    """
    Valida se as configurações em [default] estão sendo carregadas.
    """
    # Se nenhum ambiente for forçado, espera os valores de [default] definidos em settings.toml
    assert settings.RPA_LOG_DIR == "log"
    assert settings.RPA_LOG_LEVEL == "INFO"
    assert settings.RPA_DEBUG is False
    assert settings.RPA_DEV is False
    assert settings.RPA_BASE_PATH == "./src/"

@pytest.fixture(autouse=True)
def force_development_env(monkeypatch):
    """
    Força o ambiente para 'development' para os testes abaixo.
    É importante usar o monkeypatch para setar a variável de ambiente
    e, em seguida, alterar o ambiente do settings.
    """
    monkeypatch.setenv("ENV_FOR_DYNACONF", "development")
    # Altera o ambiente do settings para 'development'
    settings.setenv("development")
    settings.reload()
    yield
    # Após o teste, volta para o ambiente default
    settings.setenv("default")
    settings.reload()

def test_development_config():
    """
    Valida se, em ambiente de desenvolvimento, as configurações são sobrescritas como esperado.
    """
    # No ambiente development, conforme settings.toml:
    # RPA_LOG_LEVEL deve ser "DEBUG" e RPA_DEBUG deve ser true
    assert settings.RPA_LOG_LEVEL == "DEBUG"
    assert settings.RPA_DEBUG is True
