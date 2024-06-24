# sportsAlarm

# Basic Set Up  

Clone this repository  
Do ```python3 -m venv venv```
Do ```source venv/bin/activate```
Do ```python3 -m pip install flask```

# Documentation

**Register**
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

**Login**
* **URL**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/login

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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Successfully Log In"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 403    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Incorrect Credentials"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 500    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Internal Server Error"  

**Add Event**
* **URL**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/addEvent

* **Method:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST

* **URL Params**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Required:**

```
{
"eventName": "string",
"date": "d-m-Y H:M:S"
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Optional:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are no optional URL params

* **Success Response:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 200  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Successfully Added Event"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 422    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Invalid Date Format"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 403      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Event Already Exists"    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 500      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Internal Server Error"  

** Get Event**
* **URL**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/getEvent

* **Method:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GET

* **URL Params**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Required:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are no required URL params

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Optional:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/getEvent?userID=x  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/getEvent?eventID=x

* **Success Response:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**For /getEvents and /getEvents?userId=x**    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 200  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Content:  
```
[
    {
        "date": "Tue, 25 Dec 2018 23:50:55 GMT",
        "eventName": "test",
        "id": 1,
        "wakeUp": false
    },
    {
        "date": "Thu, 25 Dec 2025 23:50:55 GMT",
        "eventName": "test event",
        "id": 2,
        "wakeUp": false
    },
    {
        "date": "Thu, 25 Dec 2025 12:00:00 GMT",
        "eventName": "test event",
        "id": 3,
        "wakeUp": false
    }
]
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**For /getEvents and /getEvents?userId=x**    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 200  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Content:  
```
{
    "date": "Tue, 25 Dec 2018 23:50:55 GMT",
    "eventName": "test",
    "id": 1,
    "wakeUp": false
}
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 422    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Invalid Parameters"   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 500      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Internal Server Error"  

**Set Alarm**
* **URL**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/setAlarm

* **Method:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POST

* **URL Params**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Required:**

```
{
"userID": x (int),
"eventID": y (int)
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Optional:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are no optional URL params

* **Success Response:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 200  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Successfully Added Alarm"  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 404      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Event or User does not exist"   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 422      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Invalid JSON Format"
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Code: 500      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Message: "Internal Server Error"  

# Basic Tests Before Committing

Make sure you can get all correct errors codes from each route  