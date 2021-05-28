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
```


