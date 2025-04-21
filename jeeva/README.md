# Personal Portfolio Website

A modern and responsive portfolio website designed specifically for freshers to showcase their skills, projects, and achievements. Built with HTML, Tailwind CSS, and Python Flask.

## Features

- Responsive design that works on all devices
- Modern and clean UI with Tailwind CSS
- Smooth scrolling navigation
- Contact form with backend integration
- Skills showcase section
- Projects portfolio
- Social media integration
- Custom animations and transitions

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio-website
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Customization

1. Update your personal information in `templates/index.html`
2. Modify the skills section to reflect your expertise
3. Add your projects to the projects section
4. Update social media links in the footer
5. Customize colors and styles in `static/css/style.css`

## Project Structure

```
portfolio-website/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── static/
│   └── css/
│       └── style.css  # Custom CSS styles
└── templates/
    └── index.html     # Main HTML template
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 