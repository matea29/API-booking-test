from urllib import response
from webbrowser import get
import requests
import uuid
import getpass


ENDPOINT = 'https://restful-booker.herokuapp.com'

def test_create_booking():
    payload = new_booking_payload()
    response_new_booking = create_booking(payload)
    assert response_new_booking.status_code == 200

    data = response_new_booking.json()

    booking_id = data["bookingid"]
    response_get_booking = get_booking(booking_id)
    assert response_get_booking.status_code == 200
    get_booking_data = response_get_booking.json()
    assert get_booking_data['firstname'] == payload['firstname']
    assert get_booking_data['lastname'] == payload['lastname']

def test_update_booking():
    payload = new_booking_payload()
    response_new_booking = create_booking(payload)
    assert response_new_booking.status_code == 200
    data = response_new_booking.json()
    booking_id = data["bookingid"]

    #update booking
    new_payload = {
    "firstname" : str(uuid.uuid4()),
    "lastname" : str(uuid.uuid4()),
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

    update_booking_response = update_booking(booking_id, new_payload)
    assert update_booking_response.status_code == 200
    print(update_booking_response)
    

    #validate response
    get_booking_response = get_booking(booking_id)
    assert get_booking_response.status_code == 200
    get_booking_data = get_booking_response.json()
    assert get_booking_data['firstname'] == new_payload['firstname']
    assert get_booking_data['lastname'] == new_payload['lastname']
    
        
def create_booking(payload):
    return requests.post(ENDPOINT + '/booking', json=payload)

def get_booking(booking_id):
    return requests.get(ENDPOINT + f'/booking/{booking_id}')

def update_booking(booking_id, payload):
    return requests.put(ENDPOINT + f'/booking/{booking_id}', json=payload)

def new_booking_payload():
    first_name = str(uuid.uuid4())
    last_name = str(uuid.uuid4())
    total_price = {uuid.uuid4()}
    return {
    "firstname" : first_name,
    "lastname" : last_name,
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
