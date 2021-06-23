**SGCU Company API Specification**

- **Create User**
  - **Description:** Create User with given input. Return only **id** of the user instance that stored in database 
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
            "msg": "Invalid request body"
          }
          ```
      - **Response Status**: 400 Bad Request

- **Get all User**
  - **Description:** Get every user data by return as list of user
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
  - **Description:** Modify the user information which specify by user id. The request body need not to fill all the field (Forbid to modify user id)
  - **Path:** /user/{userId}
  - **Method:** PUT
  - **Header:** None
  - **Request Body:** 
    ```json
    {
      "firstName": "123456",
      "lastName": "123456",
      "salary": 10000
    }
    ```
  - **Request Params:** 
    ```
    {
      userId: string
    }
    ```
  - **Request Query:** None
  - **Response:**
    - Modify Successfully
      - **Response Body:** None
      - **Response Status:** 204 No Content
    - Request body have forbidden field
      - **Response Body:** JSON
        ```json
        {
          "msg": "Forbidden to change user id"
        }
        ```
      - **Response Status:** 403 Forbidden
    - User Not Found 
      - **Response Body:** JSON
        ```json
        {
          "msg": "User Not found"
        }
        ```
      - **Response Status:** 404 Not Found

- **Delete user by id**
  - **Description:** Delete user data by user id
  - **Path:** /user/{userId}
  - **Method:** DELETE
  - **Header:** None
  - **Request Body:** None
  - **Request Params:** 
    ```
    {
      userId: string
    }
    ```
  - **Request Query:** None
  - **Response:**
    - Delete Successfully
      - **Response Body:** JSON
        ```json
        {
          "id": "<userId>"
        }
        ```
      - **Response Status:** 200 OK
    - Not Found User
      - **Response Body:** JSON
        ```json
        {
          "msg": "User Not found"
        }
        ```
      - **Response Status:** 404 Not Found

- **Search user**
  - **Description:** Get user data by searching from firstName or lastName or both that will return as list of user
  - **Path:** /user?firstName={firstName}&lastName={lastName}
  - **Method:** GET
  - **Header:** None
  - **Request Body:** None
  - **Request Params:** None
  - **Request Query:** 
    ```
    {
      firstName: string
      lastName: string
    }
    ```
  - **Response:**
    - **Response Body:** JSON
      ```json
      [
        {
          "id": "123456",
          "firstName": "ABCDEF",
          "lastName": "abcdef",
          "salary": 15000,
        }
      ]
      ```
      Not matching to any user case
      
      ```json
      []
      ```
    - **Response Status:** 200 OK
