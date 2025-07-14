# Django ERP System

A comprehensive Enterprise Resource Planning (ERP) system built with Django, featuring complete modules for Sales, Accounting, Human Resources, and Inventory management with a full frontend interface.

## Features

### 🎯 Core Features
- **Dashboard**: Comprehensive overview with charts, statistics, and recent activities
- **User Management**: Role-based access control with different user types
- **Responsive Design**: Modern Bootstrap 5 interface that works on all devices

### 💰 Sales Module
- **Customer Management**: Track individual and business customers
- **Product Management**: Manage products and services with SKU tracking
- **Quote Management**: Create and manage sales quotes
- **Order Management**: Process sales orders from quotes to delivery
- **Invoice Management**: Generate and track invoices with payment status

### 📊 Accounting Module
- **Chart of Accounts**: Complete accounting structure with account types
- **Journal Entries**: Double-entry bookkeeping system
- **Vendor Management**: Track suppliers and vendors
- **Bills Management**: Handle vendor bills and payments
- **Payment Processing**: Record and track all payment transactions
- **Budget Management**: Create and monitor budgets vs actuals
- **Financial Reports**: Generate P&L, Balance Sheet, and Cash Flow reports

### 👥 Human Resources Module
- **Employee Management**: Complete employee records and profiles
- **Department Management**: Organize employees by departments
- **Attendance Tracking**: Daily attendance and time tracking
- **Leave Management**: Request and approve employee leave
- **Payroll Processing**: Calculate and process employee salaries
- **Performance Reviews**: Conduct and track employee evaluations
- **Training Management**: Organize and track employee training programs

### 📦 Inventory Module
- **Warehouse Management**: Multiple warehouse support
- **Stock Movements**: Track all inventory movements (in/out/adjustments)
- **Purchase Orders**: Create and manage purchase orders to vendors
- **Stock Level Monitoring**: Track product quantities and minimum levels

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/ahmed/erp_system
   ```

2. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies (already installed):**
   ```bash
   pip install django djangorestframework pillow reportlab python-decouple
   ```

4. **Run migrations (already done):**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (already created):**
   ```bash
   python manage.py create_admin
   ```
   This creates a superuser with:
   - Username: `admin`
   - Password: `admin123`
   - Email: `admin@example.com`

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Main Application: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/

## Project Structure

```
erp_system/
├── erp_project/           # Main Django project
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── core/                 # Core functionality and dashboard
│   ├── models.py         # Company, User Profile, Address models
│   ├── views.py          # Dashboard and core views
│   └── admin.py          # Admin configuration
├── sales/                # Sales management module
│   ├── models.py         # Customer, Product, Quote, Order, Invoice models
│   ├── views.py          # Sales views and logic
│   └── admin.py          # Sales admin configuration
├── accounting/           # Accounting and finance module
│   ├── models.py         # Account, Vendor, Journal, Bill, Payment models
│   ├── views.py          # Accounting views and logic
│   └── admin.py          # Accounting admin configuration
├── hr/                   # Human resources module
│   ├── models.py         # Employee, Department, Attendance, Payroll models
│   ├── views.py          # HR views and logic
│   └── admin.py          # HR admin configuration
├── inventory/            # Inventory management module
│   ├── models.py         # Warehouse, Stock Movement, Purchase Order models
│   ├── views.py          # Inventory views and logic
│   └── admin.py          # Inventory admin configuration
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── core/             # Core module templates
│   ├── sales/            # Sales module templates
│   ├── accounting/       # Accounting module templates
│   └── hr/               # HR module templates
└── static/               # Static files (CSS, JS, images)
```

## Usage

### Getting Started
1. Login using the admin credentials (admin/admin123)
2. Access the main dashboard to see system overview
3. Navigate through different modules using the sidebar menu

### Key Workflows

#### Sales Process:
1. **Add Customers**: Go to Sales > Customers > Add Customer
2. **Create Products**: Go to Sales > Products > Add Product
3. **Generate Quotes**: Go to Sales > Quotes > Add Quote
4. **Convert to Orders**: Convert accepted quotes to sales orders
5. **Create Invoices**: Generate invoices from completed orders

#### Accounting Process:
1. **Setup Chart of Accounts**: Define your accounting structure
2. **Add Vendors**: Register your suppliers
3. **Record Transactions**: Use journal entries for all transactions
4. **Process Bills**: Handle vendor bills and payments
5. **Generate Reports**: Access financial reports for analysis

#### HR Process:
1. **Setup Departments**: Create organizational structure
2. **Add Employees**: Register all staff members
3. **Track Attendance**: Record daily attendance
4. **Process Payroll**: Calculate and process salaries
5. **Manage Leave**: Handle leave requests and approvals

## Technical Details

### Technology Stack
- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (development) - easily configurable for PostgreSQL/MySQL
- **Charts**: Chart.js for data visualization
- **Icons**: Font Awesome 6
- **File Handling**: Pillow for image processing
- **Reports**: ReportLab for PDF generation

### Key Features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Role-based Access**: Different permissions for different user roles
- **Data Integrity**: Foreign key relationships and validation
- **Audit Trail**: Automatic tracking of created/updated timestamps
- **Search & Filter**: Advanced filtering on all list views
- **Export Capabilities**: Export data to various formats

### Security Features
- **Authentication Required**: All views require login
- **CSRF Protection**: Built-in Django CSRF protection
- **SQL Injection Protection**: Django ORM prevents SQL injection
- **User Permission System**: Role-based access control

## Customization

The system is designed to be easily customizable:

1. **Add New Modules**: Create new Django apps for additional functionality
2. **Modify Models**: Extend existing models or create new ones
3. **Custom Reports**: Add new report types and formats
4. **UI Customization**: Modify templates and CSS for branding
5. **Business Logic**: Add custom validation and business rules

## Development

### Adding New Features
1. Create new models in the appropriate app
2. Generate and run migrations
3. Create views and templates
4. Add URL patterns
5. Update navigation in base template

### Database Management
- Use Django migrations for all schema changes
- Regular backups recommended for production
- Consider PostgreSQL for production deployment

## Production Deployment

For production deployment:
1. Set `DEBUG = False` in settings
2. Configure proper database (PostgreSQL recommended)
3. Set up static file serving
4. Configure email settings
5. Set up proper logging
6. Use a production WSGI server (Gunicorn)
7. Set up reverse proxy (Nginx)

## Support

This is a comprehensive ERP system built for demonstration purposes. The system includes:
- Complete database models for all business processes
- Full CRUD operations for all entities
- Responsive web interface
- Admin panel for system administration
- Proper Django project structure
- Extensible architecture for future enhancements

For customization or enterprise deployment, consider:
- Adding more detailed business logic
- Implementing advanced reporting
- Adding API endpoints for mobile apps
- Integrating with external services
- Adding more sophisticated user permissions
- Implementing workflow management

## License

This project is created for educational and demonstration purposes.
