# X Clone - Twitter-like Social Media Platform (Made With Augment Code)

A full-featured social media platform inspired by X.com (formerly Twitter), built with Django and modern web technologies. This project demonstrates comprehensive full-stack development skills and modern web application architecture.

## 🚀 Live Demo

- **Production**: [https://web-production-bc5e1.up.railway.app](https://web-production-bc5e1.up.railway.app)
- **Repository**: [https://github.com/atharvak-3000/X-clone](https://github.com/atharvak-3000/X-clone)

## 🎯 Project Overview

This X Clone is a comprehensive social media platform that replicates core Twitter functionality with modern design and user experience. The project showcases advanced Django development, responsive UI design, and production deployment capabilities.

### 🤖 Development Approach
This project was developed collaboratively with **Augment AI**, demonstrating:
- **AI-Assisted Development**: Leveraging cutting-edge AI tools for rapid prototyping and problem-solving
- **Code Architecture**: Designing scalable, maintainable Django applications
- **Problem-Solving**: Debugging complex issues and implementing robust solutions
- **Modern Development Workflow**: Git version control, deployment automation, and best practices

## ✨ Features

### 🔐 Authentication & User Management
- User registration and login system
- Custom User model with extended profile fields
- Profile editing with avatar and cover photo uploads
- Secure password handling and session management

### 📝 Post Management
- Create posts with 280-character limit
- Image upload support for posts
- Real-time character counter
- Post editing and deletion capabilities

### 👥 Social Features
- Follow/Unfollow users
- Like and retweet posts
- User profiles with follower/following counts
- Social interaction notifications

### 🔍 Discovery & Search
- Global search functionality (users, posts, hashtags)
- Hashtag support with automatic extraction
- Trending hashtags and topics
- User mention system (@username)

### 🌙 Modern UI/UX
- **Dark Mode Toggle**: Seamless theme switching with localStorage persistence
- **Responsive Design**: Mobile-first approach using Bootstrap 5
- **Interactive Elements**: AJAX-powered likes, retweets, and follows
- **Modern Styling**: Twitter-inspired design with custom CSS variables

### 📱 Technical Features
- Pagination for optimal performance
- Image optimization and resizing
- Automatic avatar generation for new users
- Real-time form validation
- Error handling and user feedback

## 🛠️ Technology Stack

### Backend
- **Django 5.2.5**: Python web framework
- **SQLite/PostgreSQL**: Database management
- **Pillow**: Image processing and optimization
- **WhiteNoise**: Static file serving

### Frontend
- **Bootstrap 5**: Responsive CSS framework
- **jQuery**: DOM manipulation and AJAX
- **Font Awesome**: Icon library
- **Custom CSS**: Advanced theming with CSS variables

### Deployment & DevOps
- **Railway**: Cloud platform deployment
- **Git**: Version control
- **Gunicorn**: WSGI HTTP Server
- **Environment Variables**: Secure configuration management

## 🏗️ Architecture & Skills Demonstrated

### Django Expertise
- **Custom User Models**: Extended Django's built-in User model
- **Model Relationships**: Complex many-to-many and foreign key relationships
- **Django Admin**: Custom admin interface configuration
- **URL Routing**: Clean, RESTful URL patterns
- **Template System**: Advanced template inheritance and custom filters

### Database Design
- **Normalized Schema**: Efficient database structure
- **Model Methods**: Custom model methods for business logic
- **Query Optimization**: Efficient database queries with select_related and prefetch_related

### Frontend Development
- **Responsive Design**: Mobile-first, cross-browser compatibility
- **JavaScript/jQuery**: Interactive user interfaces
- **AJAX Implementation**: Seamless user experience without page reloads
- **CSS Architecture**: Maintainable styling with CSS variables and themes

### DevOps & Deployment
- **Production Configuration**: Separate development and production settings
- **Static File Management**: Optimized static file serving
- **Environment Management**: Secure configuration with environment variables
- **Cloud Deployment**: Railway platform deployment with automatic builds

## 📁 Project Structure

```
X-clone/
├── accounts/              # User authentication and profiles
│   ├── models.py         # Custom User model
│   ├── views.py          # Authentication views
│   ├── forms.py          # User forms
│   └── urls.py           # Account URLs
├── posts/                # Post management
│   ├── models.py         # Post, Hashtag, Notification models
│   ├── views.py          # Post CRUD operations
│   ├── forms.py          # Post forms
│   └── urls.py           # Post URLs
├── templates/            # HTML templates
│   ├── base.html         # Base template with dark mode
│   ├── accounts/         # Authentication templates
│   └── posts/            # Post-related templates
├── static/               # Static files (CSS, JS, images)
├── media/                # User uploads
├── xclone/               # Project configuration
│   ├── settings.py       # Development settings
│   ├── production_settings.py  # Production configuration
│   └── urls.py           # Main URL configuration
└── requirements.txt      # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/atharvak-3000/X-clone.git
   cd X-clone
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open http://127.0.0.1:8000/ in your browser
   - Admin panel: http://127.0.0.1:8000/admin/

## 🌐 Deployment

This project is configured for easy deployment on Railway:

1. **Environment Variables**
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=*.railway.app
   DJANGO_SETTINGS_MODULE=xclone.production_settings
   USE_SQLITE=True
   ```

2. **Automatic Deployment**
   - Connected to GitHub for automatic deployments
   - Railway handles static file collection and migrations
   - Production-ready configuration included

## 🎯 Key Learning Outcomes

### Technical Skills Developed
- **Full-Stack Development**: End-to-end web application development
- **Django Mastery**: Advanced Django concepts and best practices
- **Database Design**: Relational database modeling and optimization
- **Frontend Integration**: Modern JavaScript and responsive design
- **Deployment**: Production deployment and DevOps practices

### Problem-Solving Abilities
- **Debugging**: Complex error resolution and troubleshooting
- **Performance Optimization**: Database query optimization and caching
- **User Experience**: Intuitive interface design and interaction patterns
- **Security**: Authentication, authorization, and data protection

### Modern Development Practices
- **Version Control**: Git workflow and collaboration
- **Code Organization**: Clean, maintainable code architecture
- **Documentation**: Comprehensive project documentation
- **Testing**: Application testing and quality assurance

## 🤝 Contributing

This project demonstrates collaborative development with AI assistance. Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Augment AI**: AI-assisted development and problem-solving
- **Django Community**: Excellent documentation and community support
- **Bootstrap Team**: Responsive design framework
- **Railway**: Seamless deployment platform

---

**Built with passion for modern web development and AI-assisted coding** 🚀

*This project showcases the power of combining human creativity with AI assistance to build production-ready applications.*
