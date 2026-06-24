def test_signup_flow_is_visible_via_activities_endpoint(client):
    # Arrange
    activity_name = "Debate Team"
    email = "flow.student@mergington.edu"
    signup_url = f"/activities/{activity_name}/signup"

    # Act
    signup_response = client.post(signup_url, params={"email": email})
    activities_response = client.get("/activities")
    activities_payload = activities_response.json()

    # Assert
    assert signup_response.status_code == 200
    assert activities_response.status_code == 200
    assert email in activities_payload[activity_name]["participants"]