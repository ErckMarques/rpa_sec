import os
import pathlib
import logging
from src import get_logger
from src import settings

def test_logger_cria_arquivo(monkeypatch, tmp_path):
    """
    Verifica se, ao obter um logger, o arquivo de log é criado no diretório configurado.
    Para o teste, usaremos tmp_path (diretório temporário fornecido pelo pytest) para não interferir na configuração real.
    """
    # Força a configuração para usar tmp_path como diretório de logs
    monkeypatch.setenv("RPA_LOG_DIR", str(tmp_path))
    # Atualiza a configuração no objeto settings (se necessário, force um reload)
    settings.reload()

    # Obtemos um logger para um módulo fictício "test_module"
    logger = get_logger("test_module")
    # Disparamos um log para forçar a escrita no arquivo
    logger.info("Teste de criação do arquivo de log.")

    # Verifica se o arquivo de log foi criado
    log_file = pathlib.Path(tmp_path) / "test_module.log"
    assert log_file.exists(), f"Arquivo de log {log_file} não foi criado."

    # (Opcional) Lê o conteúdo para garantir que a mensagem log esteja presente
    log_content = log_file.read_text(encoding="utf-8")
    assert "Teste de criação do arquivo de log." in log_content
