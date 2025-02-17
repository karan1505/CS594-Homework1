# CS 594 - Homework 1 Execution

Follow the instructions below to run moments

# Install the Following Packages Using Pip Install:

azure-cognitiveservices-vision-computervision, Flask, python-dotenv

# Env File

Add .env file with AZURE_VISION_ENDPOINT and AZURE_VISION_KEY, Utilize Azure services to sign up for a Computer Vision API key and endpoint to be used, place the ENV file in Moments Folder

# Upload file: Deliverables Features Confirmation

First, Upload a photo using the plus icon, after uploading;

Feature One: Go back to home page, select the photo you uploaded, the photo should now have an auto generated description. Alternatively, you can press F12 and use the alt text given in the <> image tags for your description.

Feature Two: Check the tags of your image, type the tag in the search bar and navigate to tags, you should see your image there

# Regular Setup

# Moments

A photo sharing social networking app built with Python and Flask. The example application for the book _[Python Web Development with Flask (2nd edition)](https://helloflask.com/en/book/4)_ (《[Flask Web 开发实战（第 2 版）](https://helloflask.com/book/4)》).

Demo: http://moments.helloflask.com

![Screenshot](demo.png)

## Installation

Clone the repo:

```
$ git clone https://github.com/greyli/moments
$ cd moments
```

Install dependencies with [PDM](https://pdm.fming.dev):

```
$ pdm install
```

> [!TIP]
> If you don't have PDM installed, you can create a virtual environment with `venv` and install dependencies with `pip install -r requirements.txt`.

To initialize the app, run the `flask init-app` command:

```
$ pdm run flask init-app
```

If you just want to try it out, generate fake data with `flask lorem` command then run the app:

```
$ pdm run flask lorem
```

It will create a test account:

-   email: `admin@helloflask.com`
-   password: `moments`

Now you can run the app:

```
$ pdm run flask run
* Running on http://127.0.0.1:5000/
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
