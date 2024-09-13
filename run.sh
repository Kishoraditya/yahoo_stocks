#!/bin/bash

# yahoo_stocks Run Script

echo "Starting yahoo_stocks setup and run process..."

# Step 1: Check if Docker is installed (5 seconds)
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi
echo "Docker is installed."
sleep 5

# Step 2: Check if Docker Compose is installed (5 seconds)
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose and try again."
    exit 1
fi
echo "Docker Compose is installed."
sleep 5

# Step 3: Create necessary directories and files (10 seconds)
mkdir -p backend frontend
touch backend/.env frontend/.env
echo "SECRET_KEY=ZZFW5NfM5qSxLNVP547oJHQ4TvsjAJLlwgAAraOKZbw
DATABASE_URL=postgresql://yahoo_stocks:yahoo_stocks@db/yahoo_stocks
API_KEY_YAHOO_FINANCE=gnTsEpxy6j9WtNSPGdxsl9c4MFGsBGZ9nC2yawGc" > backend/.env
echo "REACT_APP_API_URL=http://localhost:8000/api" > frontend/.env
echo "Directories and environment files created."
sleep 10

# Step 4: Build and start Docker containers (60 seconds)
echo "Building and starting Docker containers..."
docker-compose up --build -d
echo "Waiting for containers to start..."
sleep 60

# Step 5: Check if containers are running (10 seconds)
if [ "$(docker ps -q -f name=yahoo_stocks_db_1)" ] && \
   [ "$(docker ps -q -f name=yahoo_stocks_backend_1)" ] && \
   [ "$(docker ps -q -f name=yahoo_stocks_frontend_1)" ]; then
    echo "All containers are running successfully."
else
    echo "Error: Not all containers are running. Please check Docker logs for more information."
    exit 1
fi
sleep 10

# Step 6: Run database migrations (30 seconds)
echo "Running database migrations..."
docker-compose exec backend alembic upgrade head
sleep 30

# Step 7: Run backend tests (30 seconds)
echo "Running backend tests..."
docker-compose exec backend pytest
sleep 30

# Step 8: Run frontend tests (30 seconds)
echo "Running frontend tests..."
docker-compose exec frontend npm test -- --watchAll=false
sleep 30

# Step 9: Final check and instructions
echo "Setup and tests completed successfully."
echo "You can now access the yahoo_stocks application at http://localhost:3000"
echo "API is available at http://localhost:8000/api"
echo "To stop the application, run: docker-compose down"

# End of script

