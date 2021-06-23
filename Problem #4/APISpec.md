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
    "firstName": "ABCDEF",
    "lastName": "abcdef",
    "salary": 15000,
  }
  ```
  - **Request Params:** None
  - **Request Query:** None
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

- **Get all User**
  - **Description:** Get every user data
  - **Path:** /user
  - **Method:** GET
  - **Header:** None
  - **Request Body:** None
  - **Request Params:** None
  - **Request Query:** None
  - **Response:**
    - **Response Body:** JSON
    ```json
    [
      {
        "id": "123456",
        "password": "hello_world",
        "firstName": "ABCDEF",
        "lastName": "abcdef",
        "salary": 15000,
      }
    ]
    ```
    - **Response Status:** 200 OK

- **Modify user data by id**
  - **Description:** Get every user data
  - **Path:** /user
  - **Method:** GET
  - **Header:** None
  - **Request Body:** None
  - **Request Params:** None
  - **Request Query:** None
  - **Response:**
    - **Response Body:** JSON
    ```json
    [
      {
        "id": "123456",
        "password": "hello_world",
        "firstName": "ABCDEF",
        "lastName": "abcdef",
        "salary": 15000,
      }
    ]
    ```
    - **Response Status:** 200 OK

- **Delete user by id**
  - **Description:** Get every user data
  - **Path:** /user/{id}
  - **Method:** GET
  - **Header:** None
  - **Request Body:** None
  - **Request Params:** 
  ```
  {
  
  }
  ```
  - **Request Query:** None
  - **Response:**
    - **Response Body:** JSON
    ```json
    [
      {
        "id": "123456",
        "password": "hello_world",
        "firstName": "ABCDEF",
        "lastName": "abcdef",
        "salary": 15000,
      }
    ]
    ```
    - **Response Status:** 200 OK

- **User Searching**
  - **Description:** Get every user data
  - **Path:** /user
  - **Method:** GET
  - **Header:** None
  - **Request Body:** None
  - **Request Params:** None
  - **Request Query:** None
  - **Response:**
    - **Response Body:** JSON
    ```json
    [
      {
        "id": "123456",
        "password": "hello_world",
        "firstName": "ABCDEF",
        "lastName": "abcdef",
        "salary": 15000,
      }
    ]
    ```
    - **Response Status:** 200 OK


