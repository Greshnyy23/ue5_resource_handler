import pytest
from src.ue5_resource_handler import UE5ResourceHandler


def test_initialization():
    handler = UE5ResourceHandler("/path/to/UnrealPak.exe")
    assert handler.unrealpak_path == "/path/to/UnrealPak.exe"


def test_extract_pak_mock(monkeypatch):
    def mock_run(*args, **kwargs):
        print("Mocked subprocess.run called.")
    
    # Замена subprocess.run на mock
    monkeypatch.setattr("subprocess.run", mock_run)
    
    handler = UE5ResourceHandler("/path/to/UnrealPak.exe")
    handler.extract_pak("example.pak", "extract_to")