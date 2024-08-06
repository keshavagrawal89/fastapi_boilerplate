## As Simple As It Can Get


## FastAPI Boilerplate

### Overview

A simple, synchronous FastAPI boilerplate to kickstart your projects. Includes authentication, modular routes, and PostgreSQL support.

### Features

- **Custom Auth Middleware**: Uses **Supabase** for authentication.
- **Modular Routing**: Separate route modules with API versioning.
- **PostgreSQL Integration**: Single connection pool.
- **API Versioning**: `/api/v1/` base path.

### Setup

1. **Clone Repo**

   ```bash
   git clone https://github.com/yourusername/fastapi-boilerplate.git
   cd fastapi-boilerplate

2. **Create Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    
4. **Configure `.env`**
    ```bash
    SUPABASE_URL=https://your-supabase-url.supabase.co
    SUPABASE_ANON_KEY=your-supabase-anon-key
    DATABASE_URL=postgresql://user:password@localhost/dbname
    
5. **Run Application**
    ```bash
    uvicorn app.main:app --reload

### Testing the API
#### Sign-in API

To test the sign-in API, you need to create a user on the **Supabase dashboard** or use a client SDK for user signup. Then, use the following `curl` command to sign in:

    curl -X POST "https://YOUR_SUPABASE_URL/auth/v1/token?grant_type=password" \
        -H "Content-Type: application/json" \
        -H "apikey: YOUR_SUPABASE_ANON_KEY" \
        -d '{
            "email": "user@example.com",
            "password": "your_password"
            }'

This will return a JSON response with an access token.

#### Protected API Call

To make a protected API call, include the `Bearer` token in the `Authorization` header:

    curl -X GET "http://localhost:8000/api/v1/protected-route" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

#### Public API Call

To make a public API call, no authorization header is needed:
    
    curl -X GET "http://localhost:8000/api/v1/public-route"

    

### Docker?
To build and run this application using Docker, you'll need to set up Docker Compose for PostgreSQL services. This involves creating a Dockerfile for the app and a docker-compose.yml file that includes Nginx, the app, and PostgreSQL services. Sample `Dockerfile` and `docker-compose.yml` files are provided in this repository.
A sample `nginx` config is also provided.

Important: Ensure your database configuration (DATABASE_URL) points to the correct IP address. When running the backend as a Docker container, it will search for PostgreSQL on localhost (which refers to the container itself). Use your local system's IP address in DATABASE_URL instead of localhost to avoid connection issues.

Here is a summary of the steps:

Create a Dockerfile: This defines how to build the Docker image for the FastAPI app.
Create a docker-compose.yml: This sets up the app, Nginx, and PostgreSQL services.
Adjust DB Config: Update DATABASE_URL to use your local system's IP address.
