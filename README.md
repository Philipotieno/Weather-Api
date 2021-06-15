<h1 align="center">Weather API Backend</h1>
<p align="center">

[![Build Status](https://www.travis-ci.com/Philipotieno/Weather-Api.svg?branch=master)](https://www.travis-ci.com/Philipotieno/Weather-Api)
[![Coverage Status](https://coveralls.io/repos/github/Philipotieno/Weather-Api/badge.svg?branch=master)](https://coveralls.io/github/Philipotieno/Weather-Api?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/1dfc3f4c536a327c53d8/maintainability)](https://codeclimate.com/github/Philipotieno/Weather-Api/maintainability)
<img alt="PyPI - Python Version" src="https://img.shields.io/badge/Python-3.6-blue">
<img alt="PyPI - Django Version" src="https://img.shields.io/badge/Django-3.2-brightgreen">

</p>

## Getting Started

1. Clone the repository

   ```
   $ git clone https://github.com/Philipotieno/Weather-Api.git
   ```

2. Get into the cloned folder

   ```
   $ cd Weather-Api
   ```

3. Create a virtual environment

   ```
   $ virtualenv -p python3 -name of virtualenv-
   ```

4. Activate the virtual environment

   ```
   $ source ./bin/activate
   ```

5. Install dependancies

   ```
   $ pip install -r requirements.txt
   ```

6. Run the server

   ```
   $ python manage.py runserver
   ```

7. To test the endpoint with [Postman](https://getpostman.com).

   - Import the postman collection [https://www.getpostman.com/collections/27695b41296879c367f9](https://www.getpostman.com/collections/27695b41296879c367f9)

## To run tests

```
$ python test_app.py
```

## Test Coverage

```
$ coverage report
```

### GET '/api/locations?city=Mombasa$days=4'

- Fetches a temperature of given days
- Returns:

```json5
{
  maximum: 41.3,
  minimum: 30.3,
  average: 35.8,
  median: 35.8,
}
```

### screenshot

![getting data](https://github.com/Philipotieno/Weather-Api/blob/master/weatherPI.png)

## Errors Codes

### Bad request (400)

```json5
{
  success: false,
  error: 400,
  message: 'Bad request',
}
```

### Not found (404)

```json5
{
  success: false,
  error: 404,
  message: 'Resource Not Found',
}
```

### Internal server error (500)

```json5
{
  success: false,
  error: 500,
  message: 'Internal server error',
}
```
