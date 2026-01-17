# Environment Setup

## Creating `.env` file

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Update the values in `.env` with your actual credentials:
   - `EMAIL_HOST_USER`: Your Gmail address
   - `EMAIL_HOST_PASSWORD`: Your Gmail App Password (not your regular password)
   - `ADMIN_EMAIL`: Email to receive contact form submissions
   - `DJANGO_SECRET_KEY`: Django secret key for your application

## Getting Gmail App Password

1. Enable 2-Factor Authentication on your Google account
2. Go to [myaccount.google.com/app-passwords](https://myaccount.google.com/app-passwords)
3. Select "Mail" and "Windows Computer" (or your device)
4. Google will generate a 16-character app password
5. Use this password in your `.env` file (NOT your regular Gmail password)

## Important Security Notes

- **Never commit `.env` to version control**
- `.env` is in `.gitignore` and will not be tracked
- Each environment (local, staging, production) should have its own `.env` file
- Keep your `.env` file private and secure
