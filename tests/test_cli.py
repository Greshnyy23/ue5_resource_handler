import os
import sys
import os.path as op
import pytest

sys.path.insert(0, op.abspath(op.join(op.dirname(__file__), "..")))
from src.ue5_resource_handler import UE5ResourceHandler


def test_initialization():
    handler = UE5ResourceHandler("/path/to/UnrealPak.exe")
    assert handler.unrealpak_path == "/path/to/UnrealPak.exe"


def test_extract_pak_mock(monkeypatch):
    def mock_run(*args, **kwargs):
        print("Mocked subprocess.run called.")

    # Замена subprocess.run на mock
    monkeypatch.setattr("subprocess.run", mock_run)
    monkeypatch.setattr("os.path.exists", lambda p: True)
    monkeypatch.setattr("os.makedirs", lambda *a, **k: None)

    handler = UE5ResourceHandler("/path/to/UnrealPak.exe")
    handler.extract_pak("example.pak", "extract_to")


