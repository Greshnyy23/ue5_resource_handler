import os
import sys
import os.path as op
import pytest

sys.path.insert(0, op.abspath(op.join(op.dirname(__file__), "..")))
from src.ue5_resource_handler import UE5ResourceHandler

def test_init():
    h = UE5ResourceHandler("unrealpak.exe")
    assert h.unrealpak_path == "unrealpak.exe"

def test_extract_pak_no_path(tmp_path):
    h = UE5ResourceHandler("not_exists.exe")
    with pytest.raises(FileNotFoundError):
        h.extract_pak("nofile.pak", tmp_path)


def test_parse_ucas_not_found(tmp_path):
    h = UE5ResourceHandler()
    with pytest.raises(FileNotFoundError):
        h.parse_ucas(tmp_path / "f.ucas", tmp_path / "f.utoc")


def test_extract_ubulk_copy(tmp_path):
    h = UE5ResourceHandler()
    src = tmp_path / "a.ubulk"
    src.write_text("data")
    dest_dir = tmp_path / "out"
    result = h.extract_ubulk(str(src), str(dest_dir))
    assert os.path.exists(result)


def test_parse_ucas_header(tmp_path):
    h = UE5ResourceHandler()
    ucas = tmp_path / "f.ucas"
    utoc = tmp_path / "f.utoc"
    ucas.write_bytes(b"data")
    utoc.write_bytes(b"UTOC" + (1).to_bytes(4, "little"))

    info = h.parse_ucas(str(ucas), str(utoc))
    assert info["magic"] == b"UTOC"
    assert info["version"] == 1
    assert info["ucas_size"] == os.path.getsize(ucas)


