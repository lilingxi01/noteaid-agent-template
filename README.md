![Cover](https://imagedelivery.net/Dr98IMl5gQ9tPkFM5JRcng/bfb776fc-da7e-45b9-7070-fff96cab8c00/Ultra)

# NoteAid Agent Template

This template is the foundation code base for writing a medical agent that could be adapted by main NoteAid service. It is highly recommended to use this template while defining your agent as it brings simplicity on integrating with NoteAid data arguments and also provides a simple way to deploy your agent on AWS Lambda, as simple as a Git push.

This repository does not contain any sensitive content that might affect our main NoteAid service. All variables and database context will be passed into the agent while it is called. All parameters will be mapped into an agent class defined in Python, and what you need to do is put your code into the function of that class, where you can access all the data you need from function parameters.

If you want to learn more about our architecture and our limitations, please read our public technical documentation on Slab: https://noteaid.slab.com/topics/agent-development-gtvedcxv

## Usage

### Note: Migration Guide from Notebridge 0.2 to 0.4

If you have set up the environment before, you should read this section. Otherwise, you can skip this section.

Previously, we are using NPM (Node.js environment) to start up the local development environment and final deployment. However, due to the complexity and the limitation of AWS environment, we decided to migrate the whole project into Python environment with no Node.js needed. This will bring simplicity to the deployment process and also make the whole project more maintainable.

There are a few folders that you need to delete because they are no longer needed:
* `node_modules/`
* `.serverless/`

Plus, the local development environment gets downgraded from Python 3.10 to Python 3.9 for matching the configuration of our new production environment. You can simply remove the previous-created Conda environment and create a new Conda environment from our new `requirements.txt`. Most of the dependencies remain the same, but we have added Flask as our new base architecture for running the code.

### 0. Environment Preparation

Before doing agent development, you need to prepare your environment properly.

And then, install Python dependencies in your local Python environment. Python 3.9 is required for dependency simplicity and behavior consistency purposes. You can use `conda` for managing different Python environments (including different Python versions) for different projects if you want. Once you set up the Python environment, simply run the following command in your terminal:

```bash
pip install -r requirements.txt
```

And then, you are all set! If your project requires some sensitive data like OpenAI API Key, put them into the `.env` file for local development. In production environment, our software engineers will have the environment variables set up for you, so you don't need to worry about that.

### 1. Local Development

For starting up your agent service locally, run the following command:

```bash
python ./api/index.py
```

After that, you will see a localhost URL that you can call to test your agent (usually http://localhost:4680). You can then put the URL into the NoteAid Agent Debugger to test your agent.

### 2. Production Deployment

For deploying your agent to the production environment, simply push it into the `main` Git branch. Our CI/CD will handle everything else! Super easy, right?

If you don't want to deploy it yet, simply push your changes into a working branch that is different from `main` branch.

## Folders / Files

- `api/index.py` - This file is for running the base architecture of the agent. You should not touch this file unless you know what you are doing.
- `requirements.txt` - This file is the dependency list of the agent. You should update this file if you want to add more dependencies. OpenAI and Langchain (a slightly old version) are included by default.
- `handler.py` - **This file is IMPORTANT for you!** You should define your main agent within this file. The agent class will then be imported into the `api/index.py` file for feeding into the executor.
- You can add more files as wishes, but please do not overlap with the existing reserved files. Organize them into a sub-folder like `utils` would be helpful.

## Technical Note: Update Agent Template

You don't really need to worry about that! Our maintainers will update the agent template regularly, and if there is a major update on the API schema or on the data structure, our maintainers will let you know, thus you can update your agent accordingly (which should barely happen).

In most cases, your agent should not break if NoteAid API is updated but your agent is not. For modularization, we make sure that all changes to API mappings and exposed data will happen within `notebridge` package, which is a dependency of this project. Thus, the code of this repo will not be ruined at all during any API updates or regular maintenance. It will just be a version number on your end.

## Questions?

If you have any question, feel free to contact Lingxi! If you don't know how to find Lingxi in any way (usually I am on Slack or on WeChat), you can send email to `research@lingxi.li`. He will try to reply you as soon as possible. If I did not reply, follow up with him! He might be busy with something else.
