from fastapi import status


def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post(
        "/jobs/create-job/", json=data, headers=normal_user_token_headers
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


def test_read_job(client, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post(
        "/jobs/create-job/", json=data, headers=normal_user_token_headers
    )

    response = client.get("/jobs/get/1/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == "SDE super"


def test_read_all_jobs(client, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post(
        "/jobs/create-job/", json=data, headers=normal_user_token_headers
    )
    client.post(
        "/jobs/create-job/", json=data, headers=normal_user_token_headers
    )

    response = client.get("/jobs/all/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client, normal_user_token_headers):
    NEW_TITLE = "test new title"
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }

    client.post("/jobs/create-job/", json=data)
    data["title"] = NEW_TITLE

    response = client.put(
        "/jobs/update/1", json=data, headers=normal_user_token_headers
    )
    expected_title = client.get("/jobs/get/1/").json()["title"]

    assert response.json()["msg"] == "Successfully updated data."
    assert expected_title == NEW_TITLE


def test_delete_a_job(client, normal_user_token_headers):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20",
    }
    client.post(
        "/jobs/create-job/", json=data, headers=normal_user_token_headers
    )
    client.delete("/jobs/delete/1", headers=normal_user_token_headers)
    response = client.get("/jobs/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
