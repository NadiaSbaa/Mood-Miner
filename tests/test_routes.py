from app import app


def test_predict_endpoint():
    # Test with valid input data
    client = app.test_client()
    data = {'text': 'I love this movie!', 'sentiment': 'positive'}
    response = client.get('/predict', json=data)
    assert response.status_code == 200
    assert 'selected_text' in response.json


def test_missing_text():
    # Test with missing 'text' field
    client = app.test_client()
    data = {'sentiment': 'positive'}
    response = client.get('/predict', json=data)
    assert response.status_code == 400
    assert 'error' in response.json


def test_missing_sentiment():
    # Test with missing 'sentiment' field
    client = app.test_client()
    data = {'text': 'I love this movie!'}
    response = client.get('/predict', json=data)
    assert response.status_code == 400
    assert 'error' in response.json


def test_empty_text():
    # Test with empty 'text' field
    client = app.test_client()
    data = {'text': '', 'sentiment': 'positive'}
    response = client.get('/predict', json=data)
    assert response.status_code == 400
    assert 'error' in response.json


def test_empty_sentiment():
    # Test with empty 'sentiment' field
    client = app.test_client()
    data = {'text': 'I love this movie!', 'sentiment': ''}
    response = client.get('/predict', json=data)
    assert response.status_code == 400
    assert 'error' in response.json

