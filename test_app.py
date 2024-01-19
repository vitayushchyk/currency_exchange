from unittest.mock import patch, MagicMock


def test_check_endpoint(client):
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_receive_currency(client):
    with patch('app.storage.add_currency') as mock_add_currency:
        response = client.post(
            "/currency/",
            json={
                "short_name_currency": "Test",
                "rate": -1,
                "exchange_date": "2024-01-18T19:31:15.989Z",
                "user_ip": "123"
            }
        )
        assert response.status_code == 200
        mock_add_currency.assert_called_once()


def test_store_nbu_data(client):
    with patch('app.storage.add_nbu_currency') as mock_add_nbu_currency:
        response = client.post(
            "/nbu/",
            json={
                "digital_currency_code": 67,
                "full_name_currency": "Test",
                "rate": 4,
                "short_name_currency": "tst",
                "exchange_date": "2024-01-18T20:35:08.515Z"
            }
        )
        assert response.status_code == 200
        mock_add_nbu_currency.assert_called_once()


def test_get_currency_info(client):
    with (patch('app.storage.get_nbu_info', MagicMock(return_value=None)) as mock_get_nbu_info):
        with patch('app.storage.get_user_info', MagicMock(return_value=[])) as mock_get_user_info:
            response = client.get(
                "/currency/2024-01-17"
            )
            assert response.status_code == 200
            mock_get_nbu_info.assert_called_once()
            mock_get_user_info.assert_called_once()
