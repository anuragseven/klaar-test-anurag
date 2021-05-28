# klaar-test-anurag

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d4598fe0a57129408e50)


## Autocomplete API :
Autocomplete REST API which returns possible matches based on the branch name:           
```
curl --location --request GET 'https://klaar-test-anurag.herokuapp.com/api/branches/autocomplete?query=RTGS&limit=4&offset=0' \
```
**Parameters:**

**query:** Parameter is required                                      
**limit:** Parameter is required                             
**offset:** Optional

**Sample Response:**
```
curl --location --request GET 'https://klaar-test-anurag.herokuapp.com/api/branches/autocomplete?query=RTGS&limit=1&offset=0' \

Response:

{
    "branches": [{
        "ifsc": "ABHY0065001",
        "bank_id": "60",
        "branch": "RTGS-HO",
        "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
        "city": "MUMBAI",
        "district": "GREATER MUMBAI",
        "state": "MAHARASHTRA",
        "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED"
    }]
}

```

## Search API:
Search API to return possible matches across all columns and all rows.
```
curl --location --request GET 'https://klaar-test-anurag.herokuapp.com/api/branches?query=Banglore&limit=1&offset=0' \
```

**Parameters:**

**query:** Parameter is required                                      
**limit:** Parameter is required                             
**offset:** Optional

**Sample Response:**
```
curl --location --request GET 'https://klaar-test-anurag.herokuapp.com/api/branches?query=Banglore&limit=1&offset=0' \

Response:

{
    "branches": [{
        "ifsc": "HDFC0000549",
        "bank_id": "5",
        "branch": "BANGLORE-ELECTRONIC CITY-KARNATAKA",
        "address": "FLAT NO.A112,GROUND FLOOR, 3RD BLOCK, KSSIDC COMPLEX, ELECTRONIC CITY, BANGALORE, KARNATAKA - 561229",
        "city": "BANGALORE",
        "district": "BANGALORE URBAN",
        "state": "KARNATAKA",
        "bank_name": "HDFC BANK"
    }]
}

```

You can also run the APIs in the postman by clicking on "Run in Postman" button at the top.
