This repository features a curated list of AI agents that are production-ready and easy to use. To be included in this index, an agent must meet the following criteria:

1. The code must be open source.
2. The agent must be easy to install and use (e.g., like [a Nerve agent](https://github.com/evilsocket/nerve)).
3. The agent must solve a specific use case - no platforms or generic agentic frameworks.
4. The agent must be stable and ideally production ready.

If the agent you’d like to add meets these requirements, simply fork this repository, create a new YAML file in the data folder, and submit a pull request.

A sample YAML file might look like this:

```yaml
name: Name of the Agent
description: Example agent description.
author: Your Name <email@gmail.com>
homepage: https://my-cool-agent.com
repo: https://github.com/username/my-cool-agent
readme: https://github.com/username/my-cool-agent/blob/main/README.md
license: GPL-3.0
image: https://my-cool-agent.com/image.png

# specify which technologies the agent is based on
stack:
  - smolagents
  - python

# specify categories
categories:
  - software-development
  - software-security

# usage steps, can have any name and will be rendered as terminal commands
usage:
  # a good idea is to add a setup step to install whatever is required
  setup: pip install whatever
  install: pip install my-cool-agent
  run: my-cool-agent ...
```