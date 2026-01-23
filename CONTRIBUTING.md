# Contributing to Telegram Channel Scraper

Thank you for your interest in contributing to Telegram Channel Scraper! We welcome contributions from the community.

## 🌟 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Detailed steps to reproduce the issue
- Expected vs. actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant error messages or logs

### Suggesting Features

We love new ideas! To suggest a feature:
- Check if it's already been suggested in [Issues](https://github.com/MarufxAlchemist/Telegram-scrapper/issues)
- Create a new issue with the "Feature Request" template
- Clearly describe the feature and its benefits
- Provide examples of how it would work

### Pull Requests

1. **Fork the Repository**
   ```bash
   git clone https://github.com/MarufxAlchemist/Telegram-scrapper.git
   cd Telegram-scrapper
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Write clean, readable code
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test Your Changes**
   - Ensure the script runs without errors
   - Test with different channel types (public/private)
   - Verify CSV output is correct

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```
   
   Use conventional commit messages:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for updates to existing features
   - `Docs:` for documentation changes
   - `Refactor:` for code refactoring

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template
   - Wait for review

## 📝 Code Style Guidelines

### Python Style
- Follow [PEP 8](https://pep8.org/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable and function names
- Add docstrings to functions and classes

### Example:
```python
async def fetch_channel_messages(channel_name: str, limit: int = 100) -> list:
    """
    Fetch messages from a Telegram channel.
    
    Args:
        channel_name: Username or invite link of the channel
        limit: Maximum number of messages to fetch
        
    Returns:
        List of message objects
    """
    # Implementation here
    pass
```

### Documentation
- Update README.md for user-facing changes
- Add inline comments for complex logic
- Update docstrings when modifying functions
- Include examples in documentation

## 🧪 Testing

Before submitting a PR:
- [ ] Test with a public channel
- [ ] Test with a private channel (if applicable)
- [ ] Verify CSV output format
- [ ] Check for any error messages
- [ ] Ensure no credentials are hardcoded
- [ ] Test authentication flow

## 🔒 Security

- **Never commit credentials** or API keys
- **Use environment variables** for sensitive data
- **Review .gitignore** before committing
- **Report security vulnerabilities** privately via email

## 📋 Pull Request Checklist

Before submitting your PR, ensure:
- [ ] Code follows the style guidelines
- [ ] Changes have been tested
- [ ] Documentation has been updated
- [ ] Commit messages are clear and descriptive
- [ ] No sensitive information is included
- [ ] Branch is up to date with main

## 🤔 Questions?

If you have questions about contributing:
- Check existing [Issues](https://github.com/MarufxAlchemist/Telegram-scrapper/issues)
- Start a [Discussion](https://github.com/MarufxAlchemist/Telegram-scrapper/discussions)
- Reach out via email

## 📜 Code of Conduct

Please note that this project follows a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

## 🎉 Recognition

Contributors will be recognized in:
- The project README
- Release notes
- Our hearts ❤️

Thank you for making Telegram Channel Scraper better!
