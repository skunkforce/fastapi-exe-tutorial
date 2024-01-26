# FastAPI as Executable
This Repository gives a brief idea of how you can package a FastAPI program as a standalone executable.
To get started, fork this repository and add an endpoint-decorator to the `tutorial.py` file. 

In order to get an executable, you need to run the `github` workflow, which is already included in the repository, and as such also in your fork.
To run the workflow, you need to push a tag to the repo. 
You may do that by first creating a tag on a certain commit and then push that:
```
user@machine ~/r/f/app (master)> git tag v0.1.5
user@machine ~/r/f/app (master)> git push --tags
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:skunkforce/fastapi-exe-tutorial.git
 * [new tag]         v0.1.5 -> v0.1.5
```
The workflow will take the FastAPI program and use the tool `pyinstaller` in a github-action to create a release, containing a `.zip` for Windows and `.tar.gz` for Linux.
When the workflow has finished, download this release and unzip it into a directory of your choice. 
Use the Windows-CMD to navigate into the chosen directory and run it by typing `.\tutorial.exe`.
FastAPI will launch a server on your loopback-IP device and will claim port `8000` by default. 
If you'd like to change the port, or even expose your server into your local network, you may change the line `uvicorn.run(app, host="127.0.0.1", port=8000)` to a different port, respectively to the IP `0.0.0.0`, since `127.0.0.1` only exposes the port to your own loopback, making the service only available from the very device you are running it on.

In a later commit, handling of commandline arguments was added.
Please run the executable with `--help` to find out how to use the options.

Have Fun!
