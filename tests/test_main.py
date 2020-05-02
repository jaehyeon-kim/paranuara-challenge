import pytest
from fastapi.testclient import TestClient

from main import app
from src.crud import FOOD_GROUPS, get_intersection

client = TestClient(app)


def test_get_companies():
    resp = client.get("/company/list", params={"skip": 0, "limit": 20})
    assert resp.status_code == 200, resp.text

    data = resp.json()
    assert len(data["companies"]) == 20


@pytest.mark.parametrize(
    "test_input",
    [
        {"company_id": -1, "status_code": 422, "note": "invalid id"},
        {"company_id": 1, "status_code": 200, "note": "success"},
        {"company_id": 0, "status_code": 404, "note": "no employee"},
        {"company_id": 200, "status_code": 404, "note": "no company"},
    ],
)
def test_get_company_employees(test_input):
    resp = client.get(f"/company/{test_input['company_id']}/employee")
    assert resp.status_code == test_input["status_code"], resp.text

    if resp.status_code == 200:
        data = resp.json()
        assert all([d["company_id"] == test_input["company_id"] for d in data])


@pytest.mark.parametrize(
    "test_input",
    [
        {
            "first_employee_id": -1,
            "second_employee_id": 2,
            "status_code": 422,
            "note": "invalid id",
        },
        {"first_employee_id": 1, "second_employee_id": 2, "status_code": 200, "note": "success"},
        {
            "first_employee_id": 2000,
            "second_employee_id": 2,
            "status_code": 404,
            "note": "no employee",
        },
    ],
)
def test_get_employee_relation(test_input):
    resp = client.get(
        "/employee/relation/",
        params={
            "first_employee_id": test_input["first_employee_id"],
            "second_employee_id": test_input["second_employee_id"],
        },
    )
    assert resp.status_code == test_input["status_code"], resp.text

    if resp.status_code == 200:
        data = resp.json()
        friend_ids = get_intersection(
            [e["friend_id"] for e in data["first_employee"]["friends"]],
            [e["friend_id"] for e in data["second_employee"]["friends"]],
        )
        assert all(
            map(
                lambda x: x["id"] in friend_ids
                and x["eye_colour"] == "brown"
                and x["has_died"] == False,
                data["friends"],
            )
        )


@pytest.mark.parametrize(
    "test_input",
    [
        {"employee_id": -1, "status_code": 422, "note": "invalid id"},
        {"employee_id": 1, "status_code": 200, "note": "success"},
        {"employee_id": 2000, "status_code": 404, "note": "no employee"},
    ],
)
def test_get_employee_food(test_input):
    resp = client.get(f"/employee/{test_input['employee_id']}/favourite_food")
    assert resp.status_code == test_input["status_code"], resp.text

    if resp.status_code == 200:

        def match_group(data, which="fruits"):
            return all(map(lambda x: x in FOOD_GROUPS[which], data[which]))

        data = resp.json()
        assert match_group(data, "fruits")
        assert match_group(data, "vegetables")
