# Environment Variable Migration Summary

## ✅ COMPLETE: Migrated from OS Environment Variables to `.env` Files

---

## What Changed

### BEFORE (Using `os.environ`)
```python
# Set in shell
export OPENAI_API_KEY=sk-proj-...

# Read in code
os.environ.get('OPENAI_API_KEY')
```

**Problems**:
- Not persistent across sessions
- Platform-specific (different syntax Windows vs Linux)
- Hard to manage multiple variables
- Easy to forget to set

### AFTER (Using `.env` files)
```bash
# Set in .env file
OPENAI_API_KEY=sk-proj-...

# Automatically loaded on startup
# Read in code
os.getenv('OPENAI_API_KEY')
```

**Benefits**:
✅ Persistent across sessions
✅ Works same on all platforms
✅ Easy to manage many variables
✅ Clear template (`.env.example`)
✅ Excluded from git (secure)

---

## Files Created

### 1. `.env.example`
**Purpose**: Template showing all available environment variables
**Status**: Committed to git (safe)
**Contents**:
```bash
# Django Settings
SECRET_KEY=django-insecure-dev-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,*

# OpenAI API Configuration (REQUIRED)
OPENAI_API_KEY=sk-proj-your-actual-api-key-here

# OpenAI Model Configuration (Optional)
OPENAI_MODEL=gpt-4o-mini
OPENAI_MAX_TOKENS=2000
```

### 2. `.env` (User Creates This)
**Purpose**: Actual configuration with real values
**Status**: NOT committed (in `.gitignore`)
**How to create**:
```bash
cp .env.example .env
# Then edit with your real API key
```

### 3. `.gitignore`
**Purpose**: Prevent sensitive files from being committed
**Added**:
```
.env
.env.local
.env.*.local
```

### 4. `ENV_CONFIGURATION.md`
**Purpose**: Complete documentation of environment variable system
**Contents**: Full guide on setup, usage, troubleshooting

---

## Code Changes

### `buddybud/settings.py`

**Added dotenv import**:
```python
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
```

**Updated variable reads**:
```python
# BEFORE
SECRET_KEY = 'hardcoded-value'

# AFTER
SECRET_KEY = os.getenv('SECRET_KEY', 'default-value')
```

**New OpenAI settings**:
```python
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # REQUIRED
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', '2000'))
```

### `core/ai_service.py`

**Updated initialization**:
```python
# BEFORE
api_key = getattr(settings, 'OPENAI_API_KEY', os.environ.get('OPENAI_API_KEY'))

# AFTER
api_key = settings.OPENAI_API_KEY
```

**Updated error message**:
```python
raise ValueError(
    "❌ OPENAI_API_KEY not configured!\n\n"
    "Set your API key in .env file:\n"
    "  1. Copy .env.example to .env\n"
    "  2. Edit .env and set: OPENAI_API_KEY=sk-proj-your-key\n"
    "  3. Restart the server\n\n"
    "Get key from: https://platform.openai.com/api-keys"
)
```

**Now reads model config**:
```python
self.model = settings.OPENAI_MODEL
self.max_tokens = settings.OPENAI_MAX_TOKENS
```

---

## Updated Documentation

### 1. `SETUP_INSTRUCTIONS.md`
**Section 2 Updated**:
- Old: "Configure OpenAI API Key" (shell commands)
- New: "Configure Environment Variables" (.env file)

**Added**:
- Steps to copy `.env.example`
- How to edit `.env`
- Optional settings available

### 2. `README.md`
**Quick Start Section**:
- Updated step 2 to use `.env`
- Removed shell export commands
- Added `.env` file instructions

### 3. `QUICK_START.txt`
**Step 2 Rewritten**:
```
STEP 2: CONFIGURE ENVIRONMENT VARIABLES (REQUIRED!)

1. Copy .env template:
   cp .env.example .env

2. Edit .env file and set:
   OPENAI_API_KEY=sk-proj-your-actual-key
```

---

## Environment Variables Available

### Required

| Variable | Purpose | Example |
|----------|---------|---------|
| `OPENAI_API_KEY` | OpenAI API authentication | `sk-proj-abc123...` |

### Optional (Django)

| Variable | Purpose | Default |
|----------|---------|---------|
| `SECRET_KEY` | Django cryptographic signing | Auto-generated dev key |
| `DEBUG` | Enable debug mode | `True` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1,*` |

### Optional (OpenAI)

| Variable | Purpose | Default |
|----------|---------|---------|
| `OPENAI_MODEL` | GPT model to use | `gpt-4o-mini` |
| `OPENAI_MAX_TOKENS` | Max tokens per call | `2000` |

### Future/Advanced

| Variable | Purpose |
|----------|---------|
| `DATABASE_URL` | PostgreSQL connection |
| `AWS_ACCESS_KEY_ID` | AWS S3 for file storage |
| `AWS_SECRET_ACCESS_KEY` | AWS S3 secret |
| `AWS_STORAGE_BUCKET_NAME` | S3 bucket name |

---

## Migration Steps for Existing Installations

If you were using the old system:

### 1. Stop the server
```bash
Ctrl+C
```

### 2. Create `.env` file
```bash
cp .env.example .env
```

### 3. Transfer your API key
```bash
# If you had it in shell
echo $OPENAI_API_KEY  # See your current key

# Add to .env file
echo "OPENAI_API_KEY=sk-proj-your-actual-key" >> .env
```

Or manually edit `.env`:
```bash
# Windows
notepad .env

# Linux/Mac
nano .env
```

### 4. Remove shell environment variables (optional)
```bash
# Windows
set OPENAI_API_KEY=

# Linux/Mac
unset OPENAI_API_KEY
```

### 5. Restart server
```bash
python manage.py runserver
```

### 6. Verify
Should see:
```
✅ AI Service initialized with model: gpt-4o-mini
```

---

## Advantages of This Approach

### 1. **Cross-Platform Consistency**
- Same setup process on Windows, Linux, Mac
- No platform-specific shell commands
- Works identically everywhere

### 2. **Ease of Use**
- One-time setup
- Persists across sessions
- No need to re-export variables
- Clear template to follow

### 3. **Security**
- `.env` excluded from git automatically
- Can't accidentally commit secrets
- Easy to rotate keys (just edit file)

### 4. **Deployment Friendly**
- Easy to have different configs per environment
- `.env.development`, `.env.staging`, `.env.production`
- Platform services (Heroku, AWS) natively support .env

### 5. **Developer Experience**
- New developers: Just copy and edit `.env`
- No hunting for what variables are needed
- `.env.example` documents all options

---

## Troubleshooting

### ❌ "OPENAI_API_KEY not configured"

**Cause**: `.env` file doesn't exist or is empty

**Fix**:
1. Check file exists: `ls .env` (Linux/Mac) or `dir .env` (Windows)
2. If missing: `cp .env.example .env`
3. Edit `.env` and add your API key
4. Restart server

### ❌ Changes to `.env` not applying

**Cause**: Server not restarted

**Fix**:
- Stop server (Ctrl+C)
- Start again: `python manage.py runserver`
- Environment variables are loaded on startup only

### ❌ `.env` file in wrong location

**Cause**: Must be in project root (same directory as `manage.py`)

**Fix**:
```
buddybud/
├── .env              ← HERE
├── .env.example
├── manage.py
└── buddybud/
```

### ❌ Getting error about `load_dotenv`

**Cause**: `python-dotenv` not installed

**Fix**:
```bash
pip install python-dotenv
```

---

## Testing the Setup

### 1. Verify `.env` exists
```bash
# Should show your .env file
ls -la .env

# Windows
dir .env
```

### 2. Check it has the key
```bash
# Linux/Mac
cat .env | grep OPENAI_API_KEY

# Windows
type .env | findstr OPENAI_API_KEY
```

Should output: `OPENAI_API_KEY=sk-proj-...`

### 3. Start server and watch logs
```bash
python manage.py runserver
```

**Success**:
```
✅ AI Service initialized with model: gpt-4o-mini
```

**Failure**:
```
⚠️  AI SERVICE INITIALIZATION FAILED
❌ OPENAI_API_KEY not configured!
```

---

## Backward Compatibility

### System env vars still work!

If you set `OPENAI_API_KEY` in your shell, it will be used.

**Priority**:
1. System environment variables (highest)
2. `.env` file
3. Default values (lowest)

So if you have both:
```bash
# In shell
export OPENAI_API_KEY=sk-from-shell

# In .env
OPENAI_API_KEY=sk-from-file
```

The **shell version** will be used (system env vars override `.env`)

**Recommendation**: Use **only** `.env` file for consistency

---

## Production Deployment

### Option 1: Use `.env` file
```bash
# Create .env on server
OPENAI_API_KEY=sk-prod-key...
DEBUG=False
SECRET_KEY=strong-random-key
```

### Option 2: Use platform environment variables
Most platforms let you set env vars in dashboard:

**Heroku**:
```bash
heroku config:set OPENAI_API_KEY=sk-proj-...
```

**AWS Elastic Beanstalk**:
Configure in `.ebextensions/environment.config`

**Docker**:
```yaml
environment:
  - OPENAI_API_KEY=${OPENAI_API_KEY}
```

Both methods work! `.env` file is read first, then system env vars override.

---

## Summary

### ✅ What You Get

1. **`.env.example`** - Template for all environment variables
2. **`.gitignore`** - Ensures `.env` never committed
3. **`dotenv` integration** - Automatic loading from `.env`
4. **Flexible config** - Easy to change model, tokens, etc.
5. **Better errors** - Clear instructions if setup incomplete
6. **Complete docs** - `ENV_CONFIGURATION.md` for deep dive

### 📋 Quick Setup (New Users)

```bash
# 1. Copy template
cp .env.example .env

# 2. Edit .env and add your API key
# OPENAI_API_KEY=sk-proj-your-actual-key

# 3. Run server
python manage.py runserver

# 4. Should see: ✅ AI Service initialized
```

### 🔄 Migration (Existing Users)

```bash
# 1. Create .env
cp .env.example .env

# 2. Add your existing API key to .env
# (Same key you were using before)

# 3. Restart server
# Works exactly the same!
```

---

**Your environment variables are now managed via `.env` files!** 🎉
**More secure, easier to use, and deployment-ready!**

