![Cover](https://imagedelivery.net/Dr98IMl5gQ9tPkFM5JRcng/b3d73058-e3ae-4809-1388-e42c71676400/Ultra)

# NoteAid Agent Template

This template is the foundation code base for writing a medical agent that could be adapted by main NoteAid service. It is highly recommended to use this template while defining your agent as it brings simplicity on integrating with NoteAid data arguments and also provides a simple way to deploy your agent on AWS Lambda, as simple as a Git push.

This repository does not contain any sensitive content that might affect our main NoteAid service. All variables and database context will be passed into the agent while it is called. All parameters will be mapped into an agent class defined in Python, and what you need to do is put your code into the function of that class, where you can access all the data you need from function parameters.

## Usage

### Environment Preparation

Before doing agent development, you need to prepare your environment properly.

You don't need to write any JavaScript code, but in order to run our environment, you need to install Node.js and npm (usually they are installed together).

If you need help installing Node.js and npm or updating them, please refer to [this blog post](https://lingxi.li/writings/8fbd500e-6fd6-4ec1-b7e5-5354a40da305).

After installing Node.js and npm, you need to install the dependencies of this project. Simply run the following command in your terminal:

```bash
npm install
```

And then, install Python dependencies in your local Python environment. You can use `conda` for managing different Python environments for different projects if you want. Simply run the following command in your terminal:

```bash
pip install -r requirements.txt
```

And then, you are all set! If your project requires some sensitive data like OpenAI API Key, put them into the `.env` file for local development. Your deployed version will have its own environment variables configured somewhere else (by our maintainers).

### Production Deployment

For deploying your agent to the production environment, simply push it into the `main` branch. Our CI/CD will push it to AWS Lambda automatically if everything is fine. You don't have to do anything manually! If you don't want to deploy it yet, simply push your changes into a working branch that is different from `main` branch.

### Local Development

For starting up your agent service locally, run the following command:

```bash
npm run dev
```

After that, you will see a localhost URL that you can call to test your agent. You can use any tool you want to fire the request, such as Insomnia or Postman.

In a very sooner future, you will be able to test your local-hosted agent directly on our website (with a well-crafted debug tool).

### Update Agent Template

You don't really need to worry about that! Our maintainers will update the agent template regularly, and if there is a major update on the API schema or on the data structure, our maintainers will let you know, thus you can update your agent accordingly.

In most cases, your agent should not break if NoteAid API is updated but your agent is not. For modularization, we make sure that all changes to API mappings and exposed data will happen within `notebridge` package, which is a dependency of this project. Thus, the code of this repo will not be ruined at all during any API updates or regular maintenance. It will just be a version number on your end.
