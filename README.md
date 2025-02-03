# Backend- Number Classification API

## Description

A simple REST API that returns interesting mathematical properties about it, along with a fun fact.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tha-Orakkle/hng-stage-1-backend.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hng-stage-1-backend
   ```
3. Create a virtual environment:
   ```bash
   virtualenv venv
   ```
4. Activate the virtual environment:

   ```bash
   # On Windows
   .\venv\Scripts\activate

   # On Unix or MacOS
   source venv/bin/activate
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Start the server:
   ```bash
   python manage.py runserver
   ```
3. Access the API at `https://`

# API Documentation

- **Endpoint**: `GET /api/classify-number?number=371`
- **Response Format**:

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11, // sum of its digits
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
}
```

## Error Responses

### 400 Bad Request

- **Description**: This response indicates that the request was invalid or cannot be otherwise served. An error message will be returned explaining the reason.
- **Response Format**:

```json
{
  "number": "alphabet",
  "error": "true"
}
```
