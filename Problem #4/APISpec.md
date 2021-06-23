**SGCU Company API Specification**

- **Create User**
  - **Description:** Create User with given input. Return the instance of user that stored in database only **id**
  - **Path:** /user
  - **Method:** POST
  - **Header:** None
  - **Request Body:** JSON
  ```json
  {
    "id": "123456",
    "password": "hello_world",
    "firstName": "",
    "lastName": "",
    "salary": 15000,
  }
  ```
  - **Request Params:**
  - **Request Query:**
  - **Response:**
    - Create Successfully
      - **Response Body:** JSON
      ```json
      {
        "id": "123456"
      }
      ```
      - **Response Status:** 201 Created
    - Invalid request body
      - **Response Body:**: JSON
      ```json
      {
        "msg": "Invalid"
      }
      ```
      - **Response Status**: 400 Bad Request
