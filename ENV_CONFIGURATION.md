# Environment Variable Configuration

## Overview

BuddyBud uses `.env` files for configuration management via `python-dotenv`. This keeps sensitive data like API keys out of version control and makes deployment configuration easier.

---

## Files

### `.env.example`
**Purpose**: Template file showing all available environment variables
**Location**: Committed to git
**Usage**: Copy this to create your `.env` file

### `.env`
**Purpose**: Your actual configuration with real values
**Location**: NOT committed to git (in `.gitignore`)
**Usage**: System reads from this file on startup

---

## Setup

### 1. Create `.env` file

```bash
# Copy the template
cp .env.example .env

# Windows
copy .env.example .env
```

### 2. Edit `.env` file

Open `.env` in your editor and set your values:

```bash
# REQUIRED - Get from https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-proj-abc123...

# OPTIONAL - Defaults shown
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,*
OPENAI_MODEL=gpt-4o-mini
OPENAI_MAX_TOKENS=2000
```

### 3. Restart server

Environment variables are loaded on server start. After editing `.env`:

```bash
# Stop server (Ctrl+C)
# Start again
python manage.py runserver
```

---

## Available Variables

### Required

**`OPENAI_API_KEY`**
- **Required**: Yes
- **Purpose**: OpenAI API authentication
- **Get from**: https://platform.openai.com/api-keys
- **Example**: `sk-proj-abc123xyz...`
- **Error if missing**: AI service won't initialize

### Django Settings

**`SECRET_KEY`**
- **Required**: No (has default)
- **Purpose**: Django cryptographic signing
- **Default**: `django-insecure-dev-key-change-in-production`
- **Production**: Generate strong key with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

**`DEBUG`**
- **Required**: No
- **Purpose**: Enable/disable debug mode
- **Default**: `True`
- **Values**: `True` or `False`
- **Production**: Set to `False`

**`ALLOWED_HOSTS`**
- **Required**: No
- **Purpose**: Allowed hostnames for Django
- **Default**: `localhost,127.0.0.1,*`
- **Format**: Comma-separated list
- **Production**: Set to your actual domain(s)

### OpenAI Configuration

**`OPENAI_MODEL`**
- **Required**: No
- **Purpose**: Which GPT model to use
- **Default**: `gpt-4o-mini`
- **Options**: 
  - `gpt-4o-mini` (recommended, cost-effective)
  - `gpt-4o` (more powerful, more expensive)
  - `gpt-3.5-turbo` (cheaper, less capable)

**`OPENAI_MAX_TOKENS`**
- **Required**: No
- **Purpose**: Maximum tokens per API call
- **Default**: `2000`
- **Range**: 100-4096 (depends on model)
- **Impact**: Higher = more detailed responses but higher cost

### Database (Optional - Advanced)

**`DATABASE_URL`**
- **Required**: No (defaults to SQLite)
- **Purpose**: PostgreSQL connection string
- **Format**: `postgresql://user:password@host:port/dbname`
- **Example**: `postgresql://admin:pass123@localhost:5432/buddybud`
- **Production**: Recommended for scalability

### File Storage (Optional - Advanced)

**`AWS_ACCESS_KEY_ID`**
- **Required**: No (defaults to local storage)
- **Purpose**: AWS S3 access for file storage

**`AWS_SECRET_ACCESS_KEY`**
- **Purpose**: AWS S3 secret key

**`AWS_STORAGE_BUCKET_NAME`**
- **Purpose**: S3 bucket name

**`AWS_S3_REGION_NAME`**
- **Purpose**: AWS region (e.g., us-east-1)

---

## How It Works

### 1. Load Order

```python
# buddybud/settings.py
from dotenv import load_dotenv

# Loads .env file from project root
load_dotenv()

# Now can use os.getenv()
API_KEY = os.getenv('OPENAI_API_KEY')
```

### 2. Reading Values

```python
# Get value with default
value = os.getenv('VARIABLE_NAME', 'default_value')

# Get required value (no default)
value = os.getenv('VARIABLE_NAME')
# Returns None if not set
```

### 3. Type Conversion

```python
# Boolean
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Integer
MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', '2000'))

# List (comma-separated)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
```

---

## Best Practices

### 1. Never Commit `.env`

✅ `.env.example` → Committed (safe template)
❌ `.env` → NOT committed (has secrets)

Already configured in `.gitignore`:
```
.env
.env.local
.env.*.local
```

### 2. Document All Variables

When adding new env vars:
1. Add to `.env.example` with example value
2. Document in this file
3. Update setup instructions

### 3. Use Defaults

Provide sensible defaults where possible:
```python
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
```

### 4. Validate Required Vars

Check critical vars are set:
```python
api_key = settings.OPENAI_API_KEY
if not api_key:
    raise ValueError("OPENAI_API_KEY not configured!")
```

---

## Different Environments

### Development (Local)

```bash
# .env
DEBUG=True
OPENAI_API_KEY=sk-proj-dev-key...
```

### Staging

```bash
# .env.staging
DEBUG=True
OPENAI_API_KEY=sk-proj-staging-key...
DATABASE_URL=postgresql://...staging-db
```

Load specific env file:
```python
load_dotenv('.env.staging')
```

### Production

```bash
# .env.production (or use platform env vars)
DEBUG=False
SECRET_KEY=super-strong-random-key-here
ALLOWED_HOSTS=buddybud.com,www.buddybud.com
OPENAI_API_KEY=sk-proj-production-key...
DATABASE_URL=postgresql://...production-db
AWS_ACCESS_KEY_ID=...
```

---

## Platform-Specific Setup

### Heroku

Set env vars in dashboard or via CLI:
```bash
heroku config:set OPENAI_API_KEY=sk-proj-...
heroku config:set DEBUG=False
```

### AWS Elastic Beanstalk

Configure in `.ebextensions/environment.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:application:environment:
    OPENAI_API_KEY: sk-proj-...
    DEBUG: False
```

### Docker

Pass via docker-compose.yml:
```yaml
services:
  web:
    env_file:
      - .env
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
```

Or use Docker secrets for sensitive data.

### GitHub Actions / CI

Set as repository secrets:
1. Go to Settings → Secrets
2. Add `OPENAI_API_KEY`
3. Access in workflow:
```yaml
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

---

## Troubleshooting

### "OPENAI_API_KEY not configured"

**Cause**: `.env` file missing or empty
**Fix**:
1. Check `.env` file exists in project root
2. Verify it contains `OPENAI_API_KEY=sk-proj-...`
3. Restart server

### Variables not loading

**Cause**: `.env` in wrong location
**Fix**: Must be in same directory as `manage.py`

```
buddybud/
├── .env              ← HERE (project root)
├── .env.example
├── manage.py
└── buddybud/
    └── settings.py
```

### Changes not applying

**Cause**: Server not restarted
**Fix**: Stop (Ctrl+C) and restart `python manage.py runserver`

### Still using environment variables

**Cause**: System env vars override `.env`
**Fix**: Unset system env vars:
```bash
# Windows
set OPENAI_API_KEY=

# Linux/Mac
unset OPENAI_API_KEY
```

---

## Migration from Environment Variables

### Old way (deprecated):
```bash
# Set in shell
export OPENAI_API_KEY=sk-proj-...
python manage.py runserver
```

### New way (recommended):
```bash
# Set in .env file
echo "OPENAI_API_KEY=sk-proj-..." > .env
python manage.py runserver
```

**Benefits**:
- ✅ Persistent across sessions
- ✅ No need to re-export
- ✅ Easy to manage multiple vars
- ✅ Works consistently across platforms
- ✅ Better for deployment

---

## Security Notes

⚠️ **Never commit `.env` to git**
⚠️ **Don't share `.env` file publicly**
⚠️ **Rotate API keys if exposed**
⚠️ **Use different keys for dev/staging/prod**
⚠️ **Set restrictive permissions**: `chmod 600 .env`

---

## Summary

1. ✅ Copy `.env.example` to `.env`
2. ✅ Edit `.env` with your API key
3. ✅ Restart server to load changes
4. ✅ Never commit `.env` to git
5. ✅ Use platform env vars in production

**That's it! Your configuration is now managed via `.env` files!**

