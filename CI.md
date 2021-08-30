# Best practices for writing CI using GitHub Actions

1. Keep your Actions minimal, because Actions’ virtual machines have high bandwidth and are reasonably fast, but the longer an action takes to set up and run, the more time you spend waiting.
2. Don’t install dependencies unnecessarily.
3. Never hardcode secrets. Use secrets that GitHub Actions provide. It automatically redact any secrets that get logged on purpose or on accident. 
4. Limit environment variables to the narrowest possible scope. Be specific to the workflow, job or step.
5. Store authors in Action metadata to promote code ownership
6. Ensure every repository contains a CI/CD workflow. You may want to consider using a tool like Datree to help you enforce that each repository within your organization or project contains a .github/workflows folder, which will help you keep track of what is being deployed properly.
7. Don’t use self-hosted runners in a public repository. The upside to use this is that Actions can run on machines can be more secure, performant, and optimized according to your needs. However, the downside is that if you’re working on a public Action, somebody could fork it and submit a pull request for a workflow containing malicious code.
8. Use certified Actions. Allow Uncertified Actions only Case by Case.

# Best practices for writing CI using Jenkins
1. Use declarative pipelines
2. Use docker agent
3. Use secrets to manage your credentials
4. Use env variables to reuse them in multiple locations
5. Cache docker layers for faster builds 
6. Parallel running of testing and linting

## References:
* https://www.datree.io/resources/github-actions-best-practices
* https://docs.github.com/en/actions/learn-github-actions/security-hardening-for-github-actions
