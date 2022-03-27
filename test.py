from os import path


def test_necessary_files():
    assert path.exists("classification_model.pkl")
    assert path.exists("preprocessing.py")
    assert path.exists("sample_data.csv")
