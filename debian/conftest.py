import pytest

from joblib import Memory

@pytest.fixture(scope='function')
def memory(tmp_path):
    "Fixture to get an independent and self-cleaning Memory"
    mem = Memory(location=tmp_path, verbose=0)
    yield mem
    mem.clear()
