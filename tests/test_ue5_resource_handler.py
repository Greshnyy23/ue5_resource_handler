import pytest
from src.ue5_resource_handler import UE5ResourceHandler

def test_init():
    h = UE5ResourceHandler("unrealpak.exe")
    assert h.unrealpak_path == "unrealpak.exe"

def test_extract_pak_no_path(tmp_path):
    h = UE5ResourceHandler("not_exists.exe")
    with pytest.raises(FileNotFoundError):
        h.extract_pak("nofile.pak", tmp_path)
