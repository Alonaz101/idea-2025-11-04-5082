# Overview of Mood-Based Recipe Recommendation Application

This repository contains the codebase implementing the features defined in the following Jira issues:

- **SCRUM-127:** Backend API for accepting mood inputs and returning matching recipes.
- **SCRUM-128:** React frontend for mood selection and display of recipe recommendations.
- **SCRUM-129:** User authentication, profile management, preferences storage, recipe feedback, and favorites management.
- **SCRUM-130:** Placeholder modules and architecture for future AI mood detection and advanced recommendation engine.

## Features

### Backend
- Flask API providing `/api/mood` endpoint to receive mood input and return recipes matching the mood.
- User authentication system with register and login endpoints.
- Endpoints for posting user feedback on recipes and managing favorites.
- Modular code structure with Flask blueprints.

### Frontend
- React SPA with a simple and responsive UI.
- Mood selection dropdown.
- Recipe recommendations displayed dynamically based on backend response.

### Future Expansion
- Stub modules for AI-based mood detection from text and facial recognition.
- Placeholder for advanced machine learning recommendation engine.

## Traceability

Each feature and commit includes references to the Jira issue key for easy tracking and maintenance.

## Repository Structure

- `backend/` - Flask application source code.
- `frontend/` - React SPA source code.
- `docs/overview.md` - This documentation overview.

---

This document will be updated with additional implementation details as the project evolves.
