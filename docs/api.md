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
  5. JSON is always written back, with a top level data structure containing an
  optional `error` and a `data` container.

# Types

There are some shared types used throughout the API defined here.

```typescript
type UserProfile = {
  "username": string,
  "pronouns": string,
  "profilePicture": string,
  "tags": Array<string>,
  "biography": string
};
```

## User Registration

```
POST /users/register
```

Crate a new user account, resulting in an email being sent to the user
containing a one-time registration token.  Sending that token to the
[Complete Registration](#complete-registration) endpoint will establish the
user.

**Parameters**

```typescript
{
  "username": string,
  "email": string,
  "password": string,
  "account_type": "womanfemme" | "manmasc"
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null
}
```

**Status Codes**

## Complete Registration

```
GET /users/register/complete
```

Complete a user registration when a user clicks a link in their email
containing a one-time, short-lived token.

**Parameters**

```typescript
{
  "token": string,
  "sent": date
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null | {
    "session": string
  }
}
```

## User Login

```
POST /users/login
```

Establish a session for a user.

**Parameters**

```typescript
{
  "username": string,
  "password": string
}
```

**Response**

```typescript
{
  "error": null | sting,
  "data": null | {
    "session": string
  }
}
```

## User Logout

```
POST /users/logout
```

Terminate a user's session.

**Parameters**

```typescript
{
  "session": string
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null
}
```

## Read Profile

```
GET /users/
```

Retrieve a user's profile for viewing.

**Parameters**

```typescript
{
  "username": string
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null | UserProfile
}
```

## Update Profile

```
PUT /users/
```

Update a user's profile.

**Parameters**

```typescript
{
  "session": string,
  "profile": UserProfile
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null
}
```

## Upload Photo

```
POST /users/photos
```

Upload a photo encoded as base64.

  * Photos must be no larger than 1MB.
  * Users are limited to 4 photos each.

**Parameters**

```typescript
{
  "session": string,
  "photo": string
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null
}
```

## Delete a Photo

```
DELETE /users/photos
```

Remove a photo from the user's profile.

**Parameters**

```typescript
{
  "session": string,
  "photo": string
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null
}
```

## List Potential Matches

```
GET /users/suggest
```

Retrieve a list of users suggested as potential matches.

**Parameters**

```typescript
{
  "session": string
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null | {
    "users": Array<UserProfile>
  }
```


## Send a Like

```
PUT /users/like
```

Send a like to a user.

**Parameters**

```typescript
{
  "session": string,
  "username": string
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null
}
```

## List Established Matches

```
GET /matches
```

Retrieve a list of current matches.

**Parameters**

```typescript
{
  "session": string
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null | Array<UserProfile>
```

## Unmatch a User

```
DELETE /matches
```

Remove a match from the user's queue.

**Parameters**

```typescript
{
  "session": string,
  "username": string
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null
}
```

## Send Experience Rating

```
POST /matches/experience
```

After a match expires, send a rating from a woman/femme user about a man/masc
user.  Rating scores must be `1 <= x <= 5`.

**Parameters**

```typescript
{
  "session": string,
  "username": string,
  "respectfulness": number,
  "knowledge": number,
  "supportiveness": number
}
```

**Response**

```typescript
{
  "error": null | string,
  "data": null
}
```
