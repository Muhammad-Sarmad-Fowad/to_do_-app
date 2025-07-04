

# 📝 To-Do App — FastAPI Project

This is a simple To-Do application built with **FastAPI**. It allows users to **sign up**, **log in**, and perform full ** operations** on tasks. You can test the routes using **Postman** or any REST API client.

---

## ✅ ROUTE 1: `/signup` (POST)

**📩 Request:**

* **Method:** `POST`
* **URL:** `http://127.0.0.1:8000/signup`
* **Body Format:** `x-www-form-urlencoded`

**Body Parameters:**

```
username: testuser  
password: 123456
```

**✅ Expected Response:**

```json
{
  "message": "Signup successful!"
}
```

**🧨 Error Case: User already exists**

```json
{
  "detail": "User already exists"
}
```

---

## ✅ ROUTE 2: `/login` (POST)

**📩 Request:**

* **Method:** `POST`
* **URL:** `http://127.0.0.1:8000/login`
* **Body Format:** `x-www-form-urlencoded`

**Body Parameters:**

```
username: testuser  
password: 123456
```

**✅ Expected Response:**

```json
{
  "message": "Login successful!"
}
```

**🧨 Error Case: Invalid login**

```json
{
  "detail": "Wrong username or password"
}
```

---

## ✅ ROUTE 3: `/add-task` (POST)

**📩 Request:**

* **Method:** `POST`
* **URL:** `http://127.0.0.1:8000/add-task`
* **Body Format:** `x-www-form-urlencoded`

**Body Parameters:**

```
username: testuser  
title: Finish homework  
description: Finish math exercises  
status: pending
```

**✅ Expected Response:**

```json
{
  "message": "Task added",
  "task": {
    "id": 1,
    "title": "Finish homework",
    "description": "Finish math exercises",
    "status": "pending"
  }
}
```

**🧨 Error Case: Missing field**

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "status"],
      "msg": "Field required",
      "input": null
    }
  ]
}
```

---

## ✅ ROUTE 4: `/tasks` (GET)

**📩 Request:**

* **Method:** `GET`
* **URL:**
  `http://127.0.0.1:8000/tasks?username=testuser`

**✅ Expected Response:**

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Finish homework",
      "description": "Finish math exercises",
      "status": "pending"
    }
  ]
}
```

**🧨 Error Case: No tasks exist**

```json
{
  "tasks": []
}
```

---

## ✅ ROUTE 5: `/edit-task/{task_id}` (PUT)

**📩 Request:**

* **Method:** `PUT`
* **URL:**
  `http://127.0.0.1:8000/edit-task/1`
* **Body Format:** `x-www-form-urlencoded`

**Body Parameters:**

```
username: testuser  
title: Math Homework Updated  
description: All exercises  
status: done
```

**✅ Expected Response:**

```json
{
  "message": "Task updated",
  "task": {
    "id": 1,
    "title": "Math Homework Updated",
    "description": "All exercises",
    "status": "done"
  }
}
```

**🧨 Error Case: Task not found**

```json
{
  "detail": "Task not found"
}
```

---

## ✅ ROUTE 6: `/delete-task/{task_id}` (DELETE)

**📩 Request:**

* **Method:** `DELETE`
* **URL:**
  `http://127.0.0.1:8000/delete-task/1`
* **Body Format:** `x-www-form-urlencoded`

**Body Parameters:**

```
username: testuser
```

**✅ Expected Response:**

```json
{
  "message": "Task deleted"
}
```

**🧨 Error Case: Task not found**

```json
{
  "detail": "Task not found"
}
```

---
