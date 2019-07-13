# Daylight API

Daylight serves a relatively simple RESTful API to power the frontend.

Throughout this document, the following conventions are used:

  1. Request bodies must be and responses are always JSON.
  2. [TypeScript](
  https://www.typescriptlang.org/docs/handbook/advanced-types.html) notation
  is used to represent request and response data structures.
  3. URLs _never_ contain path parameters such as `/users/:id/profile`.
  4. Requests using HTTP methods that do no accept bodies such as `GET` take
  their arguments as query parameters like `GET /users?id=abd123`.

## User Registration

```
POST /users/register
```

**Parameters**

```json
```

**Response**

```json
```

## User Login

```
POST /users/login
```

**Parameters**

```json
```

**Response**

```json
```

## User Logout

```
POST /users/logout
```

**Parameters**

```json
```

**Response**

```json
```

## Read Profile

```
GET /users/
```

**Parameters**

```json
```

**Response**

```json
```

## Update Profile

```
PUT /users/
```

**Parameters**

```json
```

**Response**

```json
```

## Upload Photo

```
POST /users/photos
```

**Parameters**

```json
```

**Response**

```json
```

## Delete a Photo

```
DELETE /users/photos
```

**Parameters**

```json
```

**Response**

```json
```

## List Potential Matches

```
GET /users/suggest
```

**Parameters**

```json
```

**Response**

```json
```


## Send a Like

```
PUT /users/like
```

**Parameters**

```json
```

**Response**

```json
```

## List Established Matches

```
GET /matches
```

**Parameters**

```json
```

**Response**

```json
```

## Unmatch a User

```
DELETE /matches
```

**Parameters**

```json
```

**Response**

```json
```

## Send Experience Rating

```
POST /matches/experience
```

**Parameters**

```json
```

**Response**

```json
```
