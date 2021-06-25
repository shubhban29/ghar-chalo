# Pizza

Django Application to store information about different types of Pizza
# Steps to run the project
To run the project on local server
1. Fork and clone the Repository
2. Change the directory to project directory and create virtual environment
3. Install all the required packages using command 
    
    $ pip install -r requirements.txt
4. Then make migrations and migrate command
   
    $ python3 manage.py makemigrations
    
    $ python3 manage.py migrate 
5. Then just run the command to run the server
    
    $ python3 manage.py runserver


# All the End Points are documented below
## /pizza/{pk}:
### get

>Response
``` python
{
  id: "60d2f0a2be50318db06e4590",
  type: "regular",
  size: "small",
  topping: [
    "tomato"
  ]
}
```
### put

>request body
``` python
{
  type: "regular",
  size: "small",
  topping: [
    "tomato"
  ]
}
```
>response 
``` python
{
  id: "60d2f0a2be50318db06e4590",
  type: "regular",
  size: "small",
  topping: [
    "tomato"
  ]
}
```
### patch 

>request body
``` python
{
  type: "regular",
  size: "small",
  topping: [
    "tomato"
  ]
}
```
>response

``` python
{
  id: "60d2f0a2be50318db06e4590",
  type: "regular",
  size: "small",
  topping: [
    "tomato"
  ]
}
```

### delete

>response
``` python
{
  "succesfully deleted"
}
```
## /pizza-list/{page}:
### get
``` python
[
  {
    "id": "60d2d5da825f49aa80a5d8bf",
    "type": "square",
    "size": "small",
    "topping": [
      "tomato",
      "onion"
    ]
  },
  {
    "id": "60d2e2f1973ea360c07b8145",
    "type": "square",
    "size": "small",
    "topping": [
      "tomato"
    ]
  },
  {
    "id": "60d2f0a2be50318db06e4590",
    "type": "regular",
    "size": "small",
    "topping": [
      "tomato"
    ]
  }
]
```
## /pizza-topping/{pk}:
### get

>Response
``` python
{
  id: "60d2f0a2be50318db06e4590",
  topping: "string"
}
```
### put

>request body

``` python
{
  topping: "string"
}
```

>response 

``` python
{
  id: "60d2f0a2be50318db06e4590",
  topping: "string"
}
```

### patch 

>request body
``` python
{
  topping: "string"
}
```
>response
``` python
{
  id: "60d2f0a2be50318db06e4590",
  topping: "string"
}
```

### delete

>response
``` python
{
  "succesfully deleted"
}
```

## /pizza-size/{pk}:
### get

>Response
``` python
{
  id: "60d2f0a2be50318db06e4590",
  size: "string"
}
```
### put

>request body

``` python
{
  size: "string"
}
```

>response 

``` python
{
  id: "60d2f0a2be50318db06e4590",
  size: "string"
}
```

### patch 

>request body
``` python
{
  size: "string"
}
```
>response
``` python
{
  id: "60d2f0a2be50318db06e4590",
  size: "string"
}
```

### delete

>response
``` python
{
  "succesfully deleted"
}
```
>## Another way to check API is documented below

# HandsOn
I have deployed the app on heroku and to have a hands-on I have created open API 3.0 documentation 

>The link for deployed Django Application is 
>>[Django API deployement](https://pizza-c3.herokuapp.com/)



>The link for API documentation is 
>>[API documentation](https://app.swaggerhub.com/apis-docs/shubhban29/C3-pizza/1.0.0)


