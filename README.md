# Kahn Game

A full-stack web application featuring a card game built with Django and React.

## Tech Stack

### Frontend
- React 18 with TypeScript
- Vite for build tooling
- Chakra UI for component library
- Tailwind CSS for styling
- React Router for navigation
- Zustand for state management
- Formik & Yup for form handling
- Axios for API requests
- Framer Motion for animations
- Express for production server

### Backend
- Django 4.2
- Django REST Framework
- MySQL 8.0
- Gunicorn for production server

## Prerequisites

- Docker and Docker Compose
- Node.js (v16 or higher)
- Python 3.9 or higher
- MySQL 8.0 (if running without Docker)

## Getting Started

### Environment Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd kahn-game
```

2. Create environment file:
```bash
cp .env.example .env
```

3. Update the `.env` file with your configuration:
```env
# Database Configuration
DB_NAME=kahn_game
DB_USERNAME=kahn_user
DB_PASSWORD=your-secure-password
DB_HOST=db
DB_PORT=3306

# Django Configuration
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
BACKEND_URL=http://localhost:8000

# Frontend Configuration
FRONTEND_URL=http://localhost:5173

# Server Configuration
SERVER_IP=127.0.0.1
```

### Using Docker (Recommended)

1. Build and start all services:
```bash
docker-compose up --build
```

This will:
- Start MySQL database on port 3306
- Run database migrations
- Start Django backend on port 8000
- Start Vite development server on port 5173

2. Access the application:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Database: localhost:3306

Note: The first build might take a few minutes as it needs to install all dependencies for both frontend and backend.

### Manual Setup

#### Backend Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the configuration from step 3 above.

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the Django server:
```bash
python manage.py runserver
```

#### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

## Project Structure

```
kahn-game/
├── frontend/           # React frontend application
│   ├── src/           # Source code
│   ├── public/        # Static assets
│   └── package.json   # Frontend dependencies
├── backend/           # Django project root
│   ├── settings.py    # Django settings
│   └── urls.py        # Main URL configuration
├── api/              # Django application
│   ├── models.py     # Database models
│   ├── views.py      # API views
│   ├── auth.py       # Authentication logic
│   └── deck.py       # Game deck logic
├── .env              # Environment variables
├── .env.example      # Example environment variables
├── docker-compose.yml # Docker configuration
└── Dockerfile        # Docker build configuration
```

## Development

### Frontend Development
- The frontend runs on Vite's development server
- Hot module replacement is enabled
- TypeScript and ESLint are configured for code quality

### Backend Development
- Django REST Framework provides API endpoints
- MySQL database stores game state and user data
- CORS is configured for frontend-backend communication
- Database migrations are automatically applied on container startup

### Docker Development
- The application uses Docker Compose for orchestration
- Database data is persisted using Docker volumes
- Health checks ensure services start in the correct order
- Environment variables are managed through .env file

## Production Deployment

1. Update environment variables for production:
```bash
cp .env.example .env.production
# Edit .env.production with production values
```

2. Build the frontend:
```bash
cd frontend
npm run build
```

3. Start production servers:
```bash
# Using Docker Compose
docker-compose -f docker-compose.prod.yml up --build

# Or manually
# Backend
gunicorn backend.wsgi:application

# Frontend
npm run prod
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 