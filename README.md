# sportsAlarm

# Basic Set Up  

Clone this repository  
Do ```python3 -m venv venv```
Do ```source venv/bin/activate```
Do ```python3 -m pip install flask```

# Documentation

**Return all artists**
* **URL**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/register

* **Method:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST

* **URL Params**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Required:**

```
{
"email": "string",
"password": "string"
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Optional:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are no optional URL params

* **Success Response:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 200  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Successfully Registered User"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 403    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "User Already Exists"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 500    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Internal Server Error"  

